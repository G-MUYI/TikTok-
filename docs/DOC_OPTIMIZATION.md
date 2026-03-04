# 文档结构优化总结

## 优化目标
精简文档结构，让用户更容易找到需要的信息。

## 优化方案
采用**方案2：温和整理** - 创建 `docs/` 目录，把非核心文档移进去，保留核心文档在根目录。

---

## 优化前后对比

### 优化前（根目录文档）
```
TikTok-/
├── README.md
├── AGENTS.md
├── CHANGELOG.md                    ❌ 冗余
├── OPTIMIZATION_SUMMARY.md         ❌ 临时文档
├── .ai/
│   ├── SESSION_PERSISTENCE.md      ❌ 可合并
│   └── ...
├── tests/
│   ├── SESSION_PERSISTENCE_TEST.md ❌ 可合并
│   └── ...
└── ...
```

### 优化后（清晰分层）
```
TikTok-/
├── README.md                       ✅ 核心：项目总览
├── AGENTS.md                       ✅ 核心：AI规则源
├── viral-copywriter/
│   ├── README.md                   ✅ 核心：使用指南
│   └── SKILL.md                    ✅ 核心：技术定义
├── docs/                           ✅ 新增：归档文档
│   ├── README.md                   ✅ 文档索引
│   ├── CHANGELOG.md                ✅ 更新日志
│   ├── OPTIMIZATION_SUMMARY.md     ✅ 优化总结
│   ├── SESSION_PERSISTENCE.md      ✅ 会话持久化说明
│   └── SESSION_PERSISTENCE_TEST.md ✅ 会话持久化测试
└── ...
```

---

## 文档分类

### 📖 核心文档（必读）
放在根目录和主要功能目录，用户必须阅读：
- `README.md` - 项目总览
- `AGENTS.md` - AI规则源
- `viral-copywriter/README.md` - 使用指南
- `viral-copywriter/SKILL.md` - Skill定义

### 📚 参考文档（可选）
放在各自的功能目录，用户按需查阅：
- `.ai/SKILLS_INDEX.md` - Skills索引
- `.ai/config.yaml` - 配置文件
- `samples/README.md` - 样本库管理
- `tests/README.md` - 测试指南

### 📝 归档文档（docs/）
放在 `docs/` 目录，历史记录和详细说明：
- `docs/CHANGELOG.md` - 完整更新日志
- `docs/OPTIMIZATION_SUMMARY.md` - 优化总结
- `docs/SESSION_PERSISTENCE.md` - 会话持久化详细说明
- `docs/SESSION_PERSISTENCE_TEST.md` - 会话持久化测试

### 🔧 模板文件（给AI用）
放在 `viral-copywriter/templates/`，不是给用户看的：
- `analysis-output.md`
- `variant-output.md`
- `translation-output.md`
- `sample-save.md`

---

## 优化效果

### ✅ 改进
1. **根目录更清爽**：从5个文档减少到2个核心文档
2. **分类更清晰**：核心、参考、归档三层结构
3. **导航更明确**：在主README中增加文档导航部分
4. **维护更简单**：归档文档集中管理

### 📊 数据对比
- **根目录文档**：5个 → 2个（减少60%）
- **文档总数**：不变（只是重新组织）
- **新增导航**：1个（docs/README.md）

---

## 用户体验提升

### 新手用户
- ✅ 打开项目，只看到2个核心文档（README.md、AGENTS.md）
- ✅ 通过README中的文档导航，快速找到需要的文档
- ✅ 不会被大量文档吓到

### 高级用户
- ✅ 可以通过 `docs/` 目录查看详细的历史记录
- ✅ 可以通过 `docs/README.md` 快速定位需要的归档文档
- ✅ 所有文档都保留，没有丢失信息

---

## 后续建议

### 可以进一步精简的地方
1. **viral-copywriter/INSTALL.md**
   - 如果内容很简单，可以合并到 `viral-copywriter/README.md`

2. **samples/template.md**
   - 可以合并到 `samples/README.md`

3. **.ai/README.md**
   - 如果内容很简单，可以删除或合并到主README

### 保持精简的原则
1. **一个主题一个文档**：避免重复
2. **核心文档放根目录**：用户必读
3. **参考文档放功能目录**：按需查阅
4. **历史文档放docs/**：归档管理

---

## 文件变更记录

### 移动的文件
- `CHANGELOG.md` → `docs/CHANGELOG.md`
- `OPTIMIZATION_SUMMARY.md` → `docs/OPTIMIZATION_SUMMARY.md`
- `.ai/SESSION_PERSISTENCE.md` → `docs/SESSION_PERSISTENCE.md`
- `tests/SESSION_PERSISTENCE_TEST.md` → `docs/SESSION_PERSISTENCE_TEST.md`

### 新增的文件
- `docs/README.md` - 归档文档索引

### 更新的文件
- `README.md` - 增加文档导航部分，更新项目结构
- `.ai/SKILLS_INDEX.md` - 更新SESSION_PERSISTENCE.md链接
- `tests/README.md` - 更新SESSION_PERSISTENCE_TEST.md链接

---

**优化完成日期**：2026-03-04
**优化方案**：方案2 - 温和整理
