path = r'D:\AI\DH_DataBase\.workbuddy\memory\2026-08-20.md'
add = """

## 知识库语料「投喂」备料（华东工单FAQ → markdown 语料）
- Fly 投喂新文件 raw/fae-qa/华东工单提取仅技术服务&高价值FAQ_20260820.xlsx（2772 条，是 LLM 重筛结果的子集：仅 解决方式=技术服务 且 参考价值=高价值）。校验确认 2772 条全部满足这两个条件，无杂质。
- 动作：Fly 跳过「投喂意图」追问，按最合理默认——转成知识库可直接导入的 markdown Q&A 语料（每条含 现象/排查步骤/结论 + 元数据：问题类型/产品线/型号/客户/单号/部件）。脚本 scripts/gen_corpus.py。
- 产物：raw/fae-qa/华东工单FAQ_技术服务高价值_语料_20260820.md（2.34MB，2772 条）。
- 待办：FastGPT/Dify/RAGFlow 三 connector 当前均 disconnected，无法直接 API 投喂。需 Fly 连接系统后以此 md 为导入物料；或指定换格式(csv/拆分每篇一文件)/直连投喂。原 xlsx 未改动。
- 经验：PowerShell stdout 在此 sandbox 常被吞，查进程/输出一律写文件再 Read；杀后台卡死任务用 Stop-Process -Id <pid> -Force（无 TaskStop 工具）。
"""
with open(path, 'a', encoding='utf-8') as f:
    f.write(add)
print('appended ok')
