# Skills 动态搜索策略

## 网页抓取增强方案

AI IDE 自带的网页抓取能力普遍较弱。按以下优先级选择抓取方案：

### 方案 1：Jina Reader API（最轻量，推荐首选）

无需安装任何依赖。在任意 URL 前加 `https://r.jina.ai/` 前缀即可将网页转为 Markdown。

```bash
# 示例：抓取 skills.sh 首页
curl -s "https://r.jina.ai/https://skills.sh/"

# 示例：抓取 GitHub 某个仓库页面
curl -s "https://r.jina.ai/https://github.com/anthropics/claude-code"
```

使用规则：
- 所有网页抓取操作，优先通过 `curl "https://r.jina.ai/{目标URL}"` 执行
- 免费额度足够日常使用，无需 API Key
- 如果返回结果为空或报错，再尝试方案 2

### 方案 2：Firecrawl MCP Server（处理 JS 渲染页面）

适用于需要执行 JavaScript 才能加载内容的页面（如 SPA 应用）。

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"]
    }
  }
}
```

如果用户未安装，提示：
> 当前页面需要 JS 渲染才能抓取内容。建议安装 Firecrawl MCP Server，我可以帮你配置。

### 方案 3：Playwright MCP Server（本地真实浏览器，完全离线可控）

适用于需要完整浏览器交互（登录、点击、滚动）的场景。

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-playwright"]
    }
  }
}
```

## 搜索来源与关键词

使用上述抓取方案，依次搜索以下来源：

| 来源 | 搜索方式 |
|------|---------|
| Skills.sh | `curl -s "https://r.jina.ai/https://skills.sh/"` 获取目录，或 Web 搜索 `site:skills.sh {tech_stack}` |
| Kiro Skills 市场 | Web 搜索 `Kiro skill {tech_stack}` |
| Claude Code MCP Servers | Web 搜索 `MCP server {tech_stack}` 或 `awesome MCP servers` |
| GitHub | `gh search repos "{tech_stack} agent skill" --sort stars --limit 5` |
| npm / PyPI | `curl -s "https://registry.npmjs.org/-/v1/search?text={tech_stack}+agent+skill&size=5"` |

## 搜索行为规则

- 每次搜索先用 Jina Reader（方案 1）尝试抓取，失败再降级
- 总搜索次数不超过 6 次，避免耗时过长
- 搜索结果需过滤：优先选择 star 数高、近 6 个月有更新、文档完善的项目
- 如果所有在线方式均不可用，请求用户协助搜索并粘贴结果，或基于 AI 自身知识给出离线推荐并标注 `⚠️ 离线推荐，建议联网后回复「重新搜索」`
