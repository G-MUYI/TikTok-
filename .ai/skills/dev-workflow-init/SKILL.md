---
name: dev-workflow-init
description: Interactive project initialization skill. Conducts a requirements interview, generates an AGENTS.md rule file, recommends matching skills/tools, and orchestrates a development workflow. Trigger with "启动" or "start".
license: MIT
compatibility: Claude Code, Kiro, Cursor
metadata:
  author: YY
  version: "1.0.0"
  category: methodology
  complexity: beginner
---

# 开发工作流初始化

通过对话式访谈收集项目需求，自动生成 AGENTS 规则文件、推荐适配 skills、编排开发工作流。

## When to Use

**IMPORTANT: 这个 skill 应该在以下情况下主动激活：**

1. 用户明确说 `启动`、`start`、`开始`、`初始化项目` 等启动指令
2. 用户询问"如何开始一个新项目"、"怎么初始化开发流程"等类似问题
3. 用户在一个新的空项目文件夹中询问 AI 如何开始
4. 用户提到需要"梳理需求"、"生成 AGENTS.md"、"设置工作流"等相关需求

**激活后的第一句话：**
```
你好！我会通过 8 个问题帮你梳理项目需求，然后生成 AGENTS.md 规则文件、推荐适配的 skills 和工具、编排开发工作流。

现在开始第一个问题：

1️⃣ 你想实现的核心效果是什么？请用 1-2 句话描述。
```

**CRITICAL: 一旦识别到触发条件，立即输出上述内容并开始访谈，不要等待用户再次确认。**

**如果用户的请求不明确是否要启动此 skill，先简短确认：**
> 看起来你想初始化一个新项目的开发工作流。我可以通过访谈帮你生成 AGENTS.md 和推荐工具，要开始吗？（回复「是」或「启动」）

## How It Works

整个流程分为三个阶段，依次推进：

### 阶段一：需求访谈

**开始访谈时，直接问第一个问题，不要等待用户再次确认。**

按以下顺序**逐个提问**，每次只问一个问题，等用户回答后再问下一个。
如果用户一次性回答了多个问题，识别并记录已回答的内容，只继续追问未回答的部分。

**访谈问题清单：**

| # | 字段 ID | 问题 |
|---|---------|------|
| 1 | project_goal | 你想实现的核心效果是什么？请用 1-2 句话描述。 |
| 2 | target_users | 主要面向哪些用户或角色？ |
| 3 | success_criteria | 你怎么判断这个项目成功了？请给 2-3 条可验证的标准。 |
| 4 | tech_stack | 计划使用什么技术栈（语言 / 框架 / 平台）？ |
| 5 | constraints | 有哪些约束条件（时间、预算、合规、性能等）？ |
| 6 | delivery_timeline | 期望的交付节奏是什么（例如 1 周 POC、1 月上线）？ |
| 7 | collaboration_mode | 你希望 AI 的协作方式是怎样的？（先出方案后实现 / 边聊边改 / 全自动执行） |
| 8 | required_integrations | 需要接入哪些外部系统或服务？没有可以说"无"。 |

**访谈行为规则：**

- 每次提问时，先简短确认上一个回答已记录（如"好的，已记录"），再问下一个。
- 如果用户的回答模糊，追问一次以获取更具体的信息，但不要反复追问同一个问题。
- 用户说「跳过」某个问题时，记录为"未指定"并继续。
- 所有 8 个字段收集完毕后，输出**需求摘要**让用户确认：

```
📋 需求摘要确认

1. 核心目标：{project_goal}
2. 目标用户：{target_users}
3. 成功标准：{success_criteria}
4. 技术栈：{tech_stack}
5. 约束条件：{constraints}
6. 交付节奏：{delivery_timeline}
7. 协作方式：{collaboration_mode}
8. 外部集成：{required_integrations}

请确认以上信息是否正确，或告诉我需要修改的地方。
```

用户确认后，进入阶段二。

### 阶段二：生成 AGENTS 统一规则源

在项目根目录生成 `AGENTS.md`，内容结构参见 `references/agents-template.md`。

生成后告知用户：
> AGENTS.md 已生成。接下来为你推荐适配的 skills 并编排工作流。

### 阶段三：推荐 Skills 并编排工作流

根据用户的 `tech_stack`、`project_goal`、`required_integrations` 等信息，实时联网搜索最匹配的 skills / 插件 / 工具。

搜索策略和来源详见 `references/search-strategy.md`。

**推荐输出格式：**

```
🔍 已根据你的项目需求搜索全网，推荐以下 Skills / 工具：

1. {skill_name}
   - 来源：{GitHub / MCP / Kiro / VS Code 等}
   - 链接：{URL}
   - 推荐理由：{一句话说明为什么适配}

2. ...

你可以告诉我需要调整推荐，或回复「继续」进入工作流编排。
```

用户确认 skills 列表后，生成工作流步骤并回填到 AGENTS.md 的「工作流编排」部分。
工作流模板详见 `references/agents-template.md`。

编排完成后告知用户：
> 工作流已编排完成并写入 AGENTS.md。你可以随时回复「执行 Step N」来启动对应步骤，或回复「全部执行」按顺序推进。

## Global Rules

- 始终使用中文对话，除非用户切换语言。
- 不要一次性输出大段内容，保持对话节奏。
- 每个阶段完成后明确告知用户当前进度和下一步。
- 如果用户说「重来」或「重新开始」，清空已收集的信息，从阶段一重新开始。
- Windows 中文路径处理：优先使用 Git Bash（MSYS2），路径用双引号包裹，使用正斜杠 `/`。
- 文件生命周期管理：每次生成或转换文件后，主动检查项目目录中是否存在被新文件替代的旧文件（如旧的 AGENTS.md、重复的配置文件等）。如果发现冗余文件，列出清单并建议用户删除，经确认后执行清理。不要留下孤立的过时文件等用户自己发现。
