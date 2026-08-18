# SCHEMA.md — DH_DataBase 知识库规则

> 状态：占位骨架，待填充完整规则。

## 三层结构
- 第一层 `raw/`：原始资料，只读，AI 绝不修改原件。
- 第二层 `wiki/`：AI 编译维护的知识层（Markdown + `[[链接]]`）。
- 第三层 `build/`：部署产物（RAG 索引 / 微调参数 / 配置）。

## 页面类型
- entity（实体页）：产品 / 部件 / 设备 / 品牌
- concept（概念页）：技术 / 方法论
- topic（案例 / 综述页）：故障案例、手册综述
- manual（手册编译页）：每本手册一页

## 命名约定（待细化）
- raw 手册：`<手册名>_v<版本>.<ext>`
- wiki 页：`<类型>-<标题>.md`（kebab-case）
- handover：`YYYYMMDD-主题.md`
- scripts：`<动词>_<名词>.py`
- tools：`tool-<name>/`

## 投喂协议（待细化）
- 新增 / 更新 / 删减，统一格式：`投喂：<动作> <文件名>`
- 每次维护 `raw/MANIFEST.csv`，AI 据此增量编译。
