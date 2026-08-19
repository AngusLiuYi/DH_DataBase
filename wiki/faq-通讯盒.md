---
title: 通讯盒 FAQ（噗元项目）
type: faq
created: 2026-08-19
updated: 2026-08-19
sources: [噗元FAQ_20250424.xlsx]
product_lines: [电缸, 电爪]
tags: [通讯盒, ECAT盒子, FAQ, XML, BIN, CFG, 固高]
---

# 通讯盒 FAQ（噗元项目）

> **源文件**：`raw/fae-qa/噗元FAQ_20250424.xlsx`（HDFAQ 表，欧姆龙噗元项目，大寰内部 FAE 整理）
> **产品线**：[[entity-电缸]] / [[entity-电爪]]（EC 盒子 = 485→ECAT 网关）
> **配套**：[[manual-dh-ecat盒子固件升级]]（固件升级）、[[manual-dh-m2e-b1-4通讯盒使用说明]]（M2E-B1-4 使用）

## 概述

共 4 条通讯盒（EC 盒子/M2E-B1 系列）FAQ，覆盖固高扫描、IO 映射、XML/BIN/CFG 三类文件含义、盒子逻辑。

---

| 编号 | 问题 | 根因与解决要点 |
|---|---|---|
| 28209 | 固高软件扫描不到通讯盒 | 硬件：盒子通电、RJ-45 接口、网线；软件：XML 是否匹配 |
| 28210 | PLC 与盒子正常通讯但 IO 映射数据全 0 | （原表分析/措施为空，待补充；疑与 PDO 映射/IO 类型配置相关，见 [[manual-dh-m2e-b1-4通讯盒使用说明]]） |
| 28213 | 盒子内 XML/BIN/CFG 分别是什么 | XML=标签描述数据结构的标记语言文件（ESI 设备描述）；BIN=硬件内部程序编译的二进制文件（固件）；CFG=存储软件/系统设置信息的文本文件（配置） |
| 50506323 | EtherCAT 盒子逻辑 | （原表分析/措施为空，待补充；EC 盒子 = EtherCAT↔485 Modbus 转接，IO 类型非标准 402 轴，见 [[faq-电爪]] 24050 条） |

---

## See Also

- [[manual-dh-ecat盒子固件升级]] — EC 盒子固件升级（ESI/Bin/CFG 三类）
- [[manual-dh-m2e-b1-4通讯盒使用说明]] — M2E-B1-4 EtherCAT 通讯盒使用说明
- [[manual-dh-基恩士适配ecat盒子]] — 基恩士 KV8000/7500 适配
- [[entity-电缸]] — EC 盒子正式型号（M2E-B1-1/B1-4 等）
