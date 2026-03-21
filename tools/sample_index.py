#!/usr/bin/env python3
"""
samples/index.json integrity helper.

This repository is primarily a "skill + templates + sample library" project.
Over time it is easy for `samples/index.json` and `samples/cases/*.md` to drift.

This script provides two subcommands:

  - check: validate consistency (no writes)
  - fix:   sync index.json to match the cases directory (writes if needed)

Examples (Windows):
  py -3 tools/sample_index.py check
  py -3 tools/sample_index.py fix
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any


REQUIRED_ENTRY_KEYS: list[str] = [
    "id",
    "category",
    "product",
    "date",
    "source",
    "tags",
    "emotion_score",
    "key_patterns",
    "summary",
]


def _repo_root() -> Path:
    # tools/sample_index.py -> repo root
    return Path(__file__).resolve().parent.parent


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _dump_json(path: Path, data: Any) -> None:
    # Keep UTF-8 and human-friendly formatting (Chinese text in values).
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def _read_text(path: Path) -> str:
    # Be tolerant of BOM and unexpected characters.
    return path.read_text(encoding="utf-8-sig", errors="replace")


def _case_id_from_filename(path: Path) -> str | None:
    stem = path.stem
    parts = stem.split("-")
    if len(parts) >= 2 and parts[0].lower() == "sample":
        return f"sample-{parts[1]}"
    if stem.lower().startswith("sample-"):
        segs = stem.split("-", 2)
        if len(segs) >= 2:
            return f"sample-{segs[1]}"
    return None


def _product_from_filename(path: Path) -> str:
    stem = path.stem
    parts = stem.split("-")
    if len(parts) >= 3 and parts[0].lower() == "sample":
        return parts[2]
    # Fallback: best-effort, do not crash
    return ""


def _dedup_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for it in items:
        if it in seen:
            continue
        seen.add(it)
        out.append(it)
    return out


def _extract_first(pattern: str, text: str) -> str | None:
    m = re.search(pattern, text, flags=re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def _extract_tags(md_text: str) -> list[str]:
    # Typical format:
    #   ## 标签
    #   #标签1 #标签2 ...
    lines = md_text.splitlines()
    start_idx: int | None = None
    for i, line in enumerate(lines):
        if line.strip().startswith("##") and "标签" in line:
            start_idx = i + 1
            break
    if start_idx is None:
        return []

    # Find first non-empty block that contains #tags
    buf: list[str] = []
    in_block = False
    for j in range(start_idx, len(lines)):
        s = lines[j].strip()
        if s.startswith("##"):
            break
        if not s:
            if in_block:
                break
            continue
        if "#" in s:
            in_block = True
            buf.append(s)
        elif in_block:
            # Stop when leaving the tag block
            break

    raw = " ".join(buf).strip()
    if not raw:
        return []

    tags: list[str] = []
    for tok in raw.split():
        if not tok.startswith("#"):
            continue
        t = tok.lstrip("#").strip()
        if not t:
            continue
        tags.append(t)
    return _dedup_keep_order(tags)


def _extract_metadata_from_md(md_text: str) -> dict[str, Any]:
    collected: dict[str, Any] = {}

    # date
    d = _extract_first(r"收集日期[:：]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", md_text)
    if d:
        collected["date"] = d

    # source
    src = _extract_first(r"来源平台[:：]\s*([^\n]+)", md_text)
    if not src:
        src = _extract_first(r"来源[:：]\s*([^\n]+)", md_text)
    if src:
        collected["source"] = re.sub(r"[\r\n]+", " ", src).strip()

    # category/product type
    cat = _extract_first(r"产品类型[^:：]*[:：]\s*([^\n]+)", md_text)
    if cat:
        cat = re.sub(r"[`*]", "", cat).strip()
        # Keep only the leading group when authors provide extra sub-types.
        for sep in ["/", "（", "("]:
            if sep in cat:
                cat = cat.split(sep, 1)[0].strip()
        collected["category"] = cat

    # emotion score
    emo = _extract_first(r"情绪强度[:：]\s*([0-9]{1,2})\s*/\s*10", md_text)
    if not emo:
        emo = _extract_first(r"强度\s*([0-9]{1,2})\s*/\s*10", md_text)
    if emo:
        try:
            score = int(emo)
        except ValueError:
            score = 0
        collected["emotion_score"] = max(0, min(10, score))

    tags = _extract_tags(md_text)
    if tags:
        collected["tags"] = tags

    return collected


def _default_entry(sample_id: str) -> dict[str, Any]:
    return {
        "id": sample_id,
        "category": "",
        "product": "",
        "date": "",
        "source": "",
        "tags": [],
        "emotion_score": 0,
        "key_patterns": [],
        "summary": "",
    }


def _normalize_entry(entry: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    # Keep a stable key order for readability/diffs.
    for k in REQUIRED_ENTRY_KEYS:
        if k in entry:
            normalized[k] = entry[k]
        else:
            normalized[k] = _default_entry(entry.get("id", "")).get(k)
    # Preserve any extra keys (if the user extends the schema later).
    for k, v in entry.items():
        if k not in normalized:
            normalized[k] = v

    # Normalize types minimally.
    if not isinstance(normalized.get("tags"), list):
        normalized["tags"] = []
    if not isinstance(normalized.get("key_patterns"), list):
        normalized["key_patterns"] = []
    if not isinstance(normalized.get("emotion_score"), int):
        try:
            normalized["emotion_score"] = int(normalized.get("emotion_score", 0))
        except Exception:
            normalized["emotion_score"] = 0
    return normalized


def _sort_key(sample_id: str) -> tuple[int, str]:
    # Prefer numeric sort when ids are like sample-016.
    m = re.match(r"^sample-([0-9]+)$", sample_id)
    if m:
        return (int(m.group(1)), sample_id)
    return (sys.maxsize, sample_id)


def _discover_cases(cases_dir: Path) -> tuple[dict[str, Path], list[Path], dict[str, list[Path]]]:
    if not cases_dir.exists():
        return ({}, [], {})

    md_files = sorted([p for p in cases_dir.glob("*.md") if p.name != ".gitkeep"])
    bad: list[Path] = []
    id_to_file: dict[str, Path] = {}
    dup: dict[str, list[Path]] = {}
    for p in md_files:
        sample_id = _case_id_from_filename(p)
        if not sample_id:
            bad.append(p)
            continue
        if sample_id in id_to_file:
            dup.setdefault(sample_id, [id_to_file[sample_id]]).append(p)
            continue
        id_to_file[sample_id] = p
    return (id_to_file, bad, dup)


def _validate_index(index_data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(index_data, dict):
        return ["index.json root must be an object"]

    samples = index_data.get("samples")
    if not isinstance(samples, list):
        errors.append("index.json must contain a 'samples' array")
        return errors

    # Basic entry validation
    seen: set[str] = set()
    for i, entry in enumerate(samples):
        if not isinstance(entry, dict):
            errors.append(f"samples[{i}] must be an object")
            continue
        sid = entry.get("id")
        if not isinstance(sid, str) or not sid:
            errors.append(f"samples[{i}].id must be a non-empty string")
            continue
        if sid in seen:
            errors.append(f"duplicate id in index: {sid}")
        seen.add(sid)
        for k in REQUIRED_ENTRY_KEYS:
            if k not in entry:
                errors.append(f"missing key for {sid}: {k}")
    return errors


def cmd_check(index_path: Path, cases_dir: Path) -> int:
    if not index_path.exists():
        print(f"[ERROR] Missing index file: {index_path}")
        return 1

    try:
        index_data = _load_json(index_path)
    except Exception as e:
        print(f"[ERROR] Failed to parse JSON: {index_path}")
        print(f"        {e}")
        return 1

    errors = _validate_index(index_data)
    if errors:
        print("[ERROR] index.json schema issues:")
        for e in errors:
            print(f"  - {e}")
        return 1

    id_to_file, bad_files, dup_files = _discover_cases(cases_dir)
    if bad_files:
        print("[WARN] Case files with unsupported name format (ignored):")
        for p in bad_files:
            print(f"  - {p.name}")

    if dup_files:
        print("[ERROR] Duplicate sample ids in cases directory:")
        for sid, files in dup_files.items():
            names = ", ".join(p.name for p in files)
            print(f"  - {sid}: {names}")
        return 1

    case_ids = set(id_to_file.keys())
    index_ids = {e["id"] for e in index_data.get("samples", []) if isinstance(e, dict) and isinstance(e.get("id"), str)}

    missing_index = sorted(case_ids - index_ids, key=_sort_key)
    missing_files = sorted(index_ids - case_ids, key=_sort_key)

    ok = True
    if missing_index:
        ok = False
        print("[ERROR] Case files missing index entries:")
        for sid in missing_index:
            print(f"  - {sid} ({id_to_file[sid].name})")
    if missing_files:
        ok = False
        print("[ERROR] Index entries missing case files:")
        for sid in missing_files:
            print(f"  - {sid}")

    expected_total = len(case_ids)
    current_total = index_data.get("total_samples")
    if not isinstance(current_total, int) or current_total != expected_total:
        ok = False
        print(f"[ERROR] total_samples mismatch: index={current_total!r}, cases={expected_total}")

    if ok:
        print(f"[OK] samples/index.json matches samples/cases ({expected_total} samples).")
        return 0
    return 1


def cmd_fix(index_path: Path, cases_dir: Path, *, dry_run: bool) -> int:
    id_to_file, bad_files, dup_files = _discover_cases(cases_dir)
    if bad_files:
        print("[WARN] Case files with unsupported name format (ignored):")
        for p in bad_files:
            print(f"  - {p.name}")

    if dup_files:
        print("[ERROR] Duplicate sample ids in cases directory:")
        for sid, files in dup_files.items():
            names = ", ".join(p.name for p in files)
            print(f"  - {sid}: {names}")
        return 1

    case_ids = sorted(id_to_file.keys(), key=_sort_key)

    existing: dict[str, dict[str, Any]] = {}
    original_data: dict[str, Any] | None = None
    if index_path.exists():
        try:
            loaded = _load_json(index_path)
            if isinstance(loaded, dict):
                original_data = loaded
                samples = loaded.get("samples", [])
                if isinstance(samples, list):
                    for entry in samples:
                        if not isinstance(entry, dict):
                            continue
                        sid = entry.get("id")
                        if isinstance(sid, str) and sid:
                            if sid not in existing:
                                existing[sid] = entry
                            else:
                                print(f"[WARN] Duplicate id in index.json, keeping first: {sid}")
        except Exception as e:
            print(f"[ERROR] Failed to parse JSON: {index_path}")
            print(f"        {e}")
            return 1

    new_samples: list[dict[str, Any]] = []
    added: list[str] = []
    for sid in case_ids:
        if sid in existing:
            entry = existing[sid]
        else:
            added.append(sid)
            entry = _default_entry(sid)
            entry["product"] = _product_from_filename(id_to_file[sid])
            md_text = _read_text(id_to_file[sid])
            meta = _extract_metadata_from_md(md_text)
            entry.update(meta)
            # Helpful placeholders.
            if not entry.get("summary"):
                entry["summary"] = "TBD"
        new_samples.append(_normalize_entry(entry))

    removed = []
    if original_data and isinstance(original_data.get("samples"), list):
        for entry in original_data["samples"]:
            if not isinstance(entry, dict):
                continue
            sid = entry.get("id")
            if isinstance(sid, str) and sid and sid not in id_to_file:
                removed.append(sid)

    # Build normalized index object with stable key order.
    new_index: dict[str, Any] = {
        "version": (original_data or {}).get("version", "1.0.0") if isinstance(original_data, dict) else "1.0.0",
        "last_updated": (original_data or {}).get("last_updated", "") if isinstance(original_data, dict) else "",
        "total_samples": len(new_samples),
        "samples": new_samples,
    }

    # Only update last_updated when something changes.
    changed = True
    if original_data is not None:
        try:
            changed = json.dumps(original_data, ensure_ascii=False, sort_keys=True) != json.dumps(new_index, ensure_ascii=False, sort_keys=True)
        except Exception:
            changed = True

    if changed:
        new_index["last_updated"] = date.today().isoformat()

    if added:
        print("[INFO] Added index entries:")
        for sid in added:
            print(f"  - {sid}")
    if removed:
        print("[INFO] Removed stale index entries (missing case file):")
        for sid in sorted(removed, key=_sort_key):
            print(f"  - {sid}")

    if not changed:
        print("[OK] No changes needed.")
        return 0

    if dry_run:
        print("[OK] Dry-run only; no files written.")
        return 0

    index_path.parent.mkdir(parents=True, exist_ok=True)
    _dump_json(index_path, new_index)
    print(f"[OK] Updated index: {index_path}")
    return 0


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description="Check/sync samples/index.json against samples/cases/*.md")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_check = sub.add_parser("check", help="Validate index.json and cases directory consistency")
    p_check.add_argument("--index", default=None, help="Path to samples/index.json (defaults to repo samples/index.json)")
    p_check.add_argument("--cases", default=None, help="Path to samples/cases (defaults to repo samples/cases)")

    p_fix = sub.add_parser("fix", help="Sync index.json to match cases directory (adds/removes entries)")
    p_fix.add_argument("--index", default=None, help="Path to samples/index.json (defaults to repo samples/index.json)")
    p_fix.add_argument("--cases", default=None, help="Path to samples/cases (defaults to repo samples/cases)")
    p_fix.add_argument("--dry-run", action="store_true", help="Show what would change without writing files")

    args = p.parse_args(argv)
    root = _repo_root()
    index_path = Path(args.index) if args.index else root / "samples" / "index.json"
    cases_dir = Path(args.cases) if args.cases else root / "samples" / "cases"

    if args.cmd == "check":
        return cmd_check(index_path=index_path, cases_dir=cases_dir)
    if args.cmd == "fix":
        return cmd_fix(index_path=index_path, cases_dir=cases_dir, dry_run=bool(args.dry_run))

    p.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
