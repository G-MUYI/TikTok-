# 爆款文案生成器 - 安装与常见问题

## 安装

### 方法 1：直接使用（推荐）

将整个 `viral-copywriter/` 文件夹复制到你的项目根目录，AI 会自动识别并使用。

### 方法 2：符号链接（多项目共享）

```bash
# Claude Code
ln -s /path/to/viral-copywriter ~/.claude/skills/viral-copywriter

# Kiro
ln -s /path/to/viral-copywriter ~/.kiro/skills/viral-copywriter

# Cursor
ln -s /path/to/viral-copywriter ~/.cursor/skills/viral-copywriter
```

## 兼容性

- Claude Code、Kiro、Cursor 及其他支持 SKILL.md 格式的 AI IDE
- 无外部依赖，使用 Claude 内置能力

## 常见问题

**Q: AI 没有自动识别我的文案？**
A: 使用 `/爆款文案` 指令触发，然后粘贴文案。

**Q: 生成的变体不满意？**
A: 直接告诉 AI 调整方向："更口语化"、"换个情绪基调"、"针对年轻人"。

**Q: 可以批量处理多段文案吗？**
A: 使用 `/爆款文案 --批量`，AI 会询问处理方式。

**Q: 支持哪些语言？**
A: 中文、英文、西班牙语、日语。可用 `--语言=ja,en` 指定。

**Q: 样本库中品牌名会被保护吗？**
A: 是的，系统自动将品牌名替换为占位符。

**Q: 文件操作失败（中文路径）？**
A: 确保使用 Git Bash 而非 PowerShell。

**Q: 如何修改默认配置？**
A: 编辑 `.ai/config.yaml`。

## 文件结构

```
viral-copywriter/
├── SKILL.md              # Skill 执行定义（指令/流程/输出格式）
├── README.md             # 本文件
└── templates/            # 输出模板
    ├── analysis-output.md
    ├── variant-output.md
    ├── translation-output.md
    ├── fish-audio-output.md
    └── sample-save.md
```

## 相关文档

- [SKILL.md](SKILL.md) - 完整 Skill 定义
- [../AGENTS.md](../AGENTS.md) - 项目规则源
- [../README.md](../README.md) - 项目总览

## 版本

- **v1.5.0** (2026-03-22) - 文档优化，数据一致性修复
- **v1.4.0** (2026-03-07) - 新增 Fish Audio 配音标签
- **v1.0.0** (2026-03-04) - 初始版本
