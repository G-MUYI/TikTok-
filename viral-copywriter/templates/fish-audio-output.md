# Fish Audio 配音标签输出模板

> 本模板用于AI输出带 Fish Audio 情感标签的配音版文案
> 参考文档：https://docs.fish.audio/developer-guide/best-practices/emotion-control

---

## 🎙️ Fish Audio 配音版

### 变体 [N]：[变体标签] - [语言标签]

#### 情感标签版文案

```
[带情绪标签的完整文案]

示例：
(curious) 智能手表用户先别划走
(excited) 乐天这两款大神款真的太能打了
(confident) 蓝牙5.4直接手表接电话
(impressed) 1.96寸大屏看着就舒服
(caring) 24小时帮你盯着心率血氧体温
(excited) 意大利真皮磁吸表带一戴上高级感直接拉满
(confident) 磁吸设计怎么甩都不掉
(enthusiastic) 关键还IP68防水 这配置谁懂
```

#### 情绪流设计

```
[情绪1] → [情绪2] → [情绪3] → [情绪4]
[对应]：开头钩子 → 价值展示 → 情绪共鸣 → 行动暗示
```

#### 配音建议

- **语速**：[建议语速 - 如：中速偏快，适合短视频节奏]
- **重音词**：[需要强调的关键词列表]
- **停顿点**：[建议停顿的位置，用 | 标记]
- **音效建议**：[可选的音效标签位置]

---

## 📋 情绪标签速查

### 基础情绪（最常用）

| 标签 | 适用场景 | TikTok文案用法 |
|------|---------|---------------|
| `(excited)` | 兴奋/惊喜 | 价值展示、惊喜发现 |
| `(curious)` | 好奇/悬念 | 开头钩子、反问 |
| `(confident)` | 自信/肯定 | 功能实证、品质保证 |
| `(friendly)` | 友好/亲切 | 朋友分享、用户见证 |
| `(happy)` | 开心/满足 | 使用体验、推荐 |
| `(impressed)` | 惊叹/赞赏 | 颜值展示、效果惊艳 |
| `(enthusiastic)` | 热情/积极 | 行动暗示、推荐 |
| `(encouraging)` | 鼓励/推动 | 收尾催促、邀请尝试 |

### 进阶情绪

| 标签 | 适用场景 | TikTok文案用法 |
|------|---------|---------------|
| `(empathetic)` | 共情/理解 | 痛点切入、问题共鸣 |
| `(concerned)` | 关心/担忧 | 健康类产品、安全类 |
| `(skeptical)` | 质疑/反问 | 反差对比开头 |
| `(relieved)` | 放松/释然 | 问题解决后的轻松感 |
| `(sincere)` | 真诚/走心 | 用户见证、真实分享 |
| `(satisfied)` | 满意/满足 | 使用后感受、好评 |
| `(warm)` | 温暖/贴心 | 情感类产品、礼物 |
| `(mysterious)` | 神秘/悬念 | 揭秘型开头 |

### 音效/语气标签（可放任意位置）

| 标签 | 效果 | 适用场景 |
|------|------|---------|
| `(whispering)` | 低声/私密 | 分享秘密、种草 |
| `(laughing)` | 笑声 | 轻松幽默段落 |
| `(sighing)` | 叹气 | 表达感慨、遗憾 |
| `(panting)` | 气喘 | 运动类产品 |

---

## 🎯 情绪流模板

### 模板 A：好奇心驱动型
```
(curious) → (excited) → (impressed) → (enthusiastic)
悬念开头 → 惊喜发现 → 品质惊叹 → 热情推荐
```

### 模板 B：故事叙述型
```
(concerned) → (relieved) → (excited) → (happy)
顾虑切入 → 转机出现 → 惊艳体验 → 满足收尾
```

### 模板 C：用户见证型
```
(friendly) → (satisfied) → (impressed) → (encouraging)
亲切开场 → 满意分享 → 效果惊叹 → 推荐收尾
```

### 模板 D：反差对比型
```
(skeptical) → (curious) → (impressed) → (confident)
质疑开头 → 好奇探索 → 品质惊艳 → 自信推荐
```

### 模板 E：痛点解决型
```
(empathetic) → (confident) → (excited) → (encouraging)
共情痛点 → 自信方案 → 效果展示 → 鼓励行动
```

---

## ⚠️ 重要规则

1. **情绪标签必须放在句子/段落开头**
2. **每个句子/段落只用一个情绪标签**
3. **避免相邻句子使用冲突情绪**（如 happy 紧接 sad）
4. **标签必须用英文小括号**：`(excited)` 而非 `（excited）`
5. **音效标签可以放在文本任意位置**
6. **完整情绪标签列表**：https://docs.fish.audio/api-reference/emotion-reference

---

✅ **配音标签生成完成！**

可直接复制到 [Fish Audio](https://fish.audio) 生成 AI 配音。
