# viral-copywriter

一个 AI 驱动的爆款文案生成器，通过深度分析文案的结构、情绪和心理学原理，自动生成多个自然亲切的变体，并提供多语言翻译。

## 特性

- 🧠 **深度分析**：解构文案的结构、情绪、认知劫持原理
- 🎯 **智能生成**：3-5 个自然亲切的文案变体
- 🌍 **多语言翻译**：中文、英文、西班牙语、日语
- 📚 **持续学习**：自动积累样本库，质量持续提升
- 🔄 **可迭代优化**：根据反馈不断改进

## 安装

### 方法 1：直接使用（推荐）

将整个 `viral-copywriter/` 文件夹复制到你的项目根目录，AI 会自动识别并使用。

### 方法 2：通过 skills CLI 安装

```bash
# 如果你使用 skills 管理工具
npx skills add <your-repo>/viral-copywriter
```

### 方法 3：符号链接（适合多项目共享）

```bash
# 在你的 AI IDE skills 目录创建符号链接
# Claude Code
ln -s /path/to/viral-copywriter ~/.claude/skills/viral-copywriter

# Kiro
ln -s /path/to/viral-copywriter ~/.kiro/skills/viral-copywriter

# Cursor
ln -s /path/to/viral-copywriter ~/.cursor/skills/viral-copywriter
```

## 快速开始

1. 在 AI 对话框中直接粘贴一段爆款文案
2. AI 会自动分析并生成变体
3. 回复"翻译"获取多语言版本

详细使用方法见 [README.md](README.md)

## 兼容性

- ✅ Claude Code
- ✅ Kiro
- ✅ Cursor
- ✅ 其他支持 SKILL.md 格式的 AI IDE

## 文件结构

```
viral-copywriter/
├── SKILL.md          # Skill 核心定义
├── README.md         # 详细使用指南
├── INSTALL.md        # 本文件：安装说明
├── templates/        # 文案模板
└── references/       # 参考资料
```

## 依赖

- 无外部依赖
- 使用 Claude 内置的文案生成和翻译能力

## 配置

无需配置，开箱即用。

如果需要自定义，可以编辑 `SKILL.md` 中的：
- 触发条件
- 分析维度
- 生成规则
- 翻译语言

## 示例

```
你：[粘贴一段爆款文案]

AI：收到！正在分析中...

📊 **文案深度分析**
[详细分析]

🎯 **生成的文案变体**
变体1：[好奇心驱动版本]
变体2：[故事叙述版本]
变体3：[用户见证版本]

你：翻译变体2

AI：🌍 **多语言翻译**
[中/英/西/日]
```

## 许可证

MIT

## 作者

YY

## 版本

v1.0.0 (2026-03-04)

## 问题反馈

如有问题或建议，请在项目中告诉 AI，系统会持续优化。

## 更新日志

- **v1.0.0** (2026-03-04)
  - 初始版本
  - 支持深度多维度分析
  - 支持 3-5 个变体生成
  - 支持 4 种语言翻译
  - 支持样本库学习
