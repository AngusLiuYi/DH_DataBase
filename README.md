# DH_DataBase

3C 自动化 FAE 知识库（LLM Wiki 架构）。

## 目录结构
- `raw/`        原始资料（只读，AI 不修改原件）
  - `manuals/`  手册按类型分目录：selection 选型 / usage 使用 / adaptation 适配 / troubleshooting 故障排查
  - `fae-qa/`   FAE 历史 Q&A（Excel/CSV）
  - `docs/`     其他零散文档、聊天记录、Word
  - `_archived/` 被删减/废弃的原始资料（归档，不真删）
  - `MANIFEST.csv` 资料清单：文件名,类型,版本,状态,最后投喂日
- `wiki/`       AI 编译的知识层（Markdown）
  - `entities/` 实体页：产品/部件/设备/品牌
  - `concepts/` 概念页：技术/方法论
  - `topics/`   主题/案例页：故障案例、手册综述
  - `manuals/`  手册编译页：每本手册一页
  - `index.md` `log.md`
- `handover/`   交接文档（人写，AI 不编译，独立维护）
- `scripts/`    脚本（Python/Node）：`ingest/` 投喂编译，`build/` 建索引/微调
- `tools/`      生成的小工具（每工具一文件夹）
- `build/`      部署产物：`rag-index/` 向量索引，`model/` 微调参数，`configs/` 配置

## 投喂协议
（详见 `SCHEMA.md`）

## 使用路线
A 投喂+编译 → B 对话查 wiki → C 固化 RAG 服务 → D 可选微调
