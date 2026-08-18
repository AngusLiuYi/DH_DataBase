# 变更日志

## 2026-08-17
- 📁 初始化目录结构 DH_DataBase（占位骨架）
- 📝 创建 README.md / SCHEMA.md / raw/MANIFEST.csv / wiki/index.md / wiki/log.md 占位

## 2026-08-18
- 📁 规范化 raw/ 下 41 个资料文件名：无版本号追加 `_YYYYMMDD`（文件最后修改日期），有版本号保持原名，清理末尾孤立 `-`（脚本 scripts/rename_raw_20260818_v2.py）
- 📝 更新 raw/MANIFEST.csv：新增「适配产品线」多选列，按四大产品线（音圈电机/电缸/电爪/驱动器）+ 通用归类
- 📐 固化产品线定义至 SCHEMA.md：驱动器限原生 ECAT/CIA402；外置 485 驱动器（SAC-S/SAC-N）附属于电缸/电爪，不单列；ECAT 盒子=485→ECAT 网关，归 `电缸;电爪`
