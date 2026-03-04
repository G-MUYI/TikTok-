# .ai 目录说明

这是项目的统一 AI 配置目录。

## 目录结构

```
.ai/
├── README.md           # 本文件
└── skills/             # 统一的 skills 存储目录
    └── dev-workflow-init/
        ├── SKILL.md
        └── ...
```

## 工作原理

- 所有 skill 文件实际存储在 `.ai/skills/` 目录中
- 各个 AI IDE 的 skills 目录（如 `.claude/skills/`、`.kiro/skills/` 等）通过符号链接指向这里
- 这样只需维护一份文件，所有 IDE 都能访问

## 支持的 IDE

- Claude Code (`.claude/skills/` → `.ai/skills/`)
- Kiro (`.kiro/skills/` → `.ai/skills/`)
- Cursor (`.cursor/skills/` → `.ai/skills/`)
- VSCode (`.vscode/skills/` → `.ai/skills/`)
- Windsurf (`.windsurf/skills/` → `.ai/skills/`)

## 添加新 Skill

将新的 skill 文件夹放入 `.ai/skills/` 目录即可，所有 IDE 会自动识别。

