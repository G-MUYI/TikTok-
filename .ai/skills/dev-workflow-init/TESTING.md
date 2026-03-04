# 测试指南

## 快速测试步骤

### 1. 安装 skill

确保 `dev-workflow-init` 文件夹位于正确的位置：

```bash
# Claude Code
.claude/skills/dev-workflow-init/

# Kiro
.kiro/skills/dev-workflow-init/

# Cursor
.agents/skills/dev-workflow-init/
```

### 2. 测试触发

在 AI 对话框中输入以下任一指令：

```
启动
```

或

```
start
```

或

```
请使用 dev-workflow-init skill
```

### 3. 预期行为

AI 应该立即回复：

```
你好！我会通过 8 个问题帮你梳理项目需求，然后生成 AGENTS.md 规则文件、推荐适配的 skills 和工具、编排开发工作流。

现在开始第一个问题：

1️⃣ 你想实现的核心效果是什么？请用 1-2 句话描述。
```

### 4. 完整流程测试

回答所有 8 个问题后，AI 应该：

1. 输出需求摘要让你确认
2. 在项目根目录生成 `AGENTS.md`
3. 联网搜索并推荐适配的 skills/工具
4. 编排工作流步骤并写入 `AGENTS.md`

## 常见问题排查

### 问题 1: AI 没有识别"启动"指令

**可能原因：**
- skill 文件夹位置不正确
- SKILL.md 文件格式有误
- AI 上下文中有其他优先级更高的指令

**解决方法：**
1. 检查文件夹路径是否正确
2. 明确说："请使用 dev-workflow-init skill"
3. 重启 AI IDE 重新加载 skills

### 问题 2: AI 开始访谈但中途停止

**可能原因：**
- 用户回答过于简短或模糊
- AI 误判用户想要退出

**解决方法：**
- 提供更详细的回答
- 说"继续"让 AI 继续下一个问题

### 问题 3: 生成的 AGENTS.md 内容不完整

**可能原因：**
- 某些问题被跳过
- 网络搜索失败

**解决方法：**
- 说"重新生成 AGENTS.md"
- 或"补充完整 AGENTS.md 的工作流部分"

## 调试模式

如果需要查看 AI 的内部状态，可以在访谈过程中随时问：

```
当前收集了哪些信息？
```

AI 会列出已收集的字段和内容。
