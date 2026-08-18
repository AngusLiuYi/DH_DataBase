# 变更日志

## 2026-08-17
- 📁 初始化目录结构 DH_DataBase（占位骨架）
- 📝 创建 README.md / SCHEMA.md / raw/MANIFEST.csv / wiki/index.md / wiki/log.md 占位

## 2026-08-18
- 📁 规范化 raw/ 下 41 个资料文件名：无版本号追加 `_YYYYMMDD`（文件最后修改日期），有版本号保持原名，清理末尾孤立 `-`（脚本 scripts/rename_raw_20260818_v2.py）
- 📝 更新 raw/MANIFEST.csv：新增「适配产品线」多选列，按四大产品线（音圈电机/电缸/电爪/驱动器）+ 通用归类
- 📐 固化产品线定义至 SCHEMA.md：驱动器限原生 ECAT/CIA402；外置 485 驱动器（SAC-S/SAC-N）附属于电缸/电爪，不单列；ECAT 盒子=485→ECAT 网关，归 `电缸;电爪`

### 首次编译（ingest）
- 🔧 读取能力确认：md ✅ ｜ pdf ✅（pypdf）｜ docx ✅（python-docx）｜ xlsx ✅（openpyxl）｜ pptx 待装库 ｜ mp4 待定方案
- 📝 创建 wiki/corrections.md 纠正记录文件（记录编译与使用中被纠正的点）
- 📖 编译第 1 本：`大寰电机调试SOP_V1.1.pdf` → `wiki/manual-sac-n2-driver-debug-sop.md`
  - 结构化提取：软件连接 / 参数导入导出 / 寻相 / 回零 / 运动控制 / 增益配置 / 开环力控（含标定公式 y=kx+b + 12 步流程）/ 故障码表（1A/0E/07/09/0A/19/1B/1C）
  - 标注 4 个不确定点：① DLAR/DLARA 电机归类 ② Z/R 双轴定义 ③ 第九章故障码表为截图（P25-29）文本未提取 ④ XJC-608T-F 传感器型号确认
- 🏗 建立关联页面骨架：[[entity-音圈电机]]、[[entity-驱动器]]、[[concept-开环力控]]
- 📑 更新 wiki/index.md（4 页，1/41 编译）

### Fly 首次纠正（C001-C004）
- ✅ C001 音圈电机型号体系：VLA/VLAR/DLA/DLAR/DLARA 全属音圈电机线；VL=Z 轴音圈、DL=Z 轴直线；A=仅 Z 轴、AR=ZR 一体 2DOF、ARA 末位 A=2026 新迭代版本（与 PGIA/PGEA/MCEA 同规则）。重写 [[entity-音圈电机]] 型号矩阵表。
- ✅ C002 双轴定义：Z=直线轴上下用、R=旋转轴内置滑环可 360° 无限旋转。修正 [[manual-sac-n2-driver-debug-sop]] 双轴定义与寻相章节，去掉"待确认"。
- ✅ C003 故障码表：第九章 P25-29 暂标"见原文件"，Fly 后续用 Excel 补充故障代码清单。
- ✅ C004 XJC-608T-F 力传感器：确认与通用线 SOP 同型号（鑫精诚品牌，后缀不关注）。修正 [[concept-开环力控]] 与手册页力控标定硬件段。
- 📝 corrections.md 写入 C001-C004，4 个待确认项全部闭环。

### 图片处理方案确认（C005）
- ✅ 采用**轻量索引法**：wiki 手册页不单独提图，用 `> 📷 界面截图：见原文件 P.XX — <面板名>` 索引到原文件页码（贴合 Fly「从原文件截图发客户」工作流）
- SCHEMA.md 编译协议新增「图片处理」节
- [[manual-sac-n2-driver-debug-sop]] 6 处截图标注统一改为新格式
- 例外：跨多本手册复用的高频界面可单独提图到 `wiki/assets/`（需 Fly 指定）
