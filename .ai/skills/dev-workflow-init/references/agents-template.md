# AGENTS.md 生成模板

用户确认需求摘要后，在项目根目录生成以下内容的 `AGENTS.md` 文件：

```markdown
# AGENTS 统一规则源

## 项目意图
- 核心目标：{project_goal}
- 目标用户：{target_users}
- 成功标准：{success_criteria}

## 工程约束
- 技术栈：{tech_stack}
- 约束条件：{constraints}
- 交付节奏：{delivery_timeline}
- 协作方式：{collaboration_mode}
- 外部集成：{required_integrations}

## 执行策略
- 采用增量交付，每个阶段产出可测试的里程碑。
- 关键决策需记录在案，便于回溯。
- 破坏性操作前必须确认。
- 优先使用确定性、可审计的操作方式。

## 工作流编排

### Step 1: 需求冻结
- 执行 skill: project-brief
- 输出: PROJECT_BRIEF.md

### Step 2: 架构设计
- 执行 skill: {matched_skill}
- 输出: 架构文档 / 技术方案

### Step 3: 核心开发
- 执行 skill: {matched_skill}
- 输出: 可运行代码

### Step 4: 测试验证
- 执行 skill: test-automation
- 输出: 测试报告

### Step 5: 部署上线
- 执行 skill: {matched_skill}
- 输出: 部署产物
```

步骤数量和内容根据实际项目需求动态调整，不必固定 5 步。
