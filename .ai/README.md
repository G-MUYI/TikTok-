# .ai 目录说明

这是项目的统一 AI 配置目录。

## 目录结构

```
.ai/
├── README.md           # 本文件
├── config.yaml         # Skills 全局配置文件
├── SKILLS_INDEX.md     # Skills 索引与帮助系统
└── skills/             # 统一的 skills 存储目录
    ├── dev-workflow-init/
    │   ├── SKILL.md
    │   └── ...
    └── [其他 skills]
```

## 📚 快速开始

### 查看可用 Skills
```
/技能列表
```

### 查看帮助
```
/帮助
/帮助 爆款文案
```

### 使用 Skills（中文指令）
```
/爆款文案          # 启动爆款文案生成器
/初始化            # 启动项目初始化工具
```

详细说明请查看：[SKILLS_INDEX.md](SKILLS_INDEX.md)

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

## 配置文件

全局配置文件：`.ai/config.yaml`

你可以在配置文件中自定义：
- Shell 设置（强制使用 Git Bash）
- 中文路径处理规则
- Skills 默认参数
- 用户偏好设置

## 添加新 Skill

将新的 skill 文件夹放入 `.ai/skills/` 目录即可，所有 IDE 会自动识别。

## 重要提示

**Windows 中文路径处理**：
- 本项目强制使用 Git Bash，禁用 PowerShell
- 所有路径使用正斜杠 `/` 和双引号包裹
- 支持中文文件名和目录名

