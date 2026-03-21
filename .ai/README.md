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

- 本项目的 Skill 分两类：
  - **项目主 Skill**：`viral-copywriter/`（位于项目根目录，便于拷贝/分发）
  - **通用/辅助 Skill**：`.ai/skills/`（例如 `dev-workflow-init/`）
- 使用时，把需要的 skill 文件夹复制/链接到你的 AI IDE 对应的 skills 目录即可。

## 支持的 IDE

- Claude Code（`~/.claude/skills/`）
- Kiro（`~/.kiro/skills/`）
- Cursor（以 Cursor 的 skills 目录为准）
- VSCode / Windsurf（以各自的 skills 目录为准）

## 配置文件

全局配置文件：`.ai/config.yaml`

你可以在配置文件中自定义：
- Shell 设置（强制使用 Git Bash）
- 中文路径处理规则
- Skills 默认参数
- 用户偏好设置

## 添加新 Skill

推荐约定：
- 项目专用 skill（例如爆款文案）放在项目根目录（便于复制给其他项目）
- 可复用的通用 skill 放在 `.ai/skills/`（便于集中管理）

## 重要提示

**Windows 中文路径处理**：
- 本项目强制使用 Git Bash，禁用 PowerShell
- 所有路径使用正斜杠 `/` 和双引号包裹
- 支持中文文件名和目录名

