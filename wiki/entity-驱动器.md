---
title: 驱动器（产品线）
type: entity
created: 2026-08-18
updated: 2026-08-18
sources: [SCHEMA.md, MANIFEST.xlsx, 大寰电机调试SOP_V1.1.pdf]
tags: [产品线, 驱动器, EtherCAT, CIA402]
---

# 驱动器

> 大寰四大产品线之一。**限定定义**：仅指原生 ECAT 通讯、符合标准 CIA402 轴控协议的伺服驱动器。

## 定义（限定）

驱动器产品线 = 原生 EtherCAT 通讯、符合标准 CiA402 轴控协议的伺服驱动器。

⚠️ **外置 485 驱动器（SAC-S / SAC-N）不单列驱动器产品线**：它仅是电缸/电爪内部控制板外置，用法与内驱一致，附属于对应 [[entity-电缸]] / [[entity-电爪]]。

## 型号清单

| 型号 | 说明 | 来源 |
|---|---|---|
| SAC-N2 驱动器 | 单/双轴伺服驱动器，配音圈电机/电缸 | 调试 SOP、初次上电 SOP |
| SAC2-N1 驱动器 | 伺服驱动器 | 适配技术样本 |
| SAC-NP2 双轴驱动器 | EtherCAT 型双轴驱动器 | 产品操作手册 Ver-M-1.00.12 |
| SAC 系列（ECAT 型） | ECAT 驱动器 | USB 升级指导、对象字典 |

## 关键特性

- **通讯**：原生 EtherCAT
- **轴控协议**：CiA402（标准伺服轴控协议）
- **对象字典**：[[concept-CIA402对象字典]] — SAC_2Axis_V1.7.2 对象字典
- **双轴**：轴1 = Z 轴（直线），轴2 = R 轴（旋转）⚠️ *待确认*
- **配置文件**：XML / ESI 文件（[[manual-sac-n2-xml更新指导]]、[[manual-sac-xml修改方法]]）

## 关联资料（6 件）

- [[manual-sac-np2-driver-debug-sop]] — SAC-N2 驱动器调试软件操作及故障分析（跨音圈电机线）
- SAC-NP2 EtherCAT 型双轴驱动器产品操作手册（Ver-M-1.00.12, 2025-10-07）
- SAC-N2 驱动器初次上电 SOP（20260415）
- SAC 系列驱动器 USB 升级操作指导文档（20260818）
- SAC-N2 XML 文件更新指导手册（20260818，跨音圈电机线）
- SAC XML 文件修改方法（20260818）
- SAC_2Axis_V1.7.2 对象字典（xlsx）

## ECAT 盒子（485→ECAT 网关）

⚠️ ECAT 盒子**不属于驱动器产品线**，是 485→EtherCAT 网关，用途是适配外置 485 驱动器型的 [[entity-电缸]] 和 [[entity-电爪]]。相关 SOP 归电缸;电爪。

## See Also

- [[entity-音圈电机]] — 配套电机
- [[entity-电缸]] — 外驱配伺服驱动器形态
- [[concept-CIA402对象字典]]
- [[concept-XML-ESI配置]]
