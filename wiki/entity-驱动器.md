---
title: 驱动器（产品线）
type: entity
created: 2026-08-18
updated: 2026-08-18
sources: [SCHEMA.md, MANIFEST.xlsx, 大寰电机调试SOP_V1.1.pdf, DH_电缸选型手册_中文版_1029.pdf, DH_音圈选型手册_中文版_CN2510.pdf]
tags: [产品线, 驱动器, EtherCAT, CIA402]
---

# 驱动器

> 大寰四大产品线之一。**限定定义**：仅指原生 ECAT 通讯、符合标准 CIA402 轴控协议的伺服驱动器。

## 定义（限定）

驱动器产品线 = 原生 EtherCAT 通讯、符合标准 CiA402 轴控协议的伺服驱动器（SAC2-NP1-EC / SAC-N2 / SAC-NP2 / SAC-NP4）。

⚠️ **外置 485 驱动器/控制器（SAC-S / SAC-N / SAC-NF）不单列驱动器产品线**：它仅是电缸/电爪内部控制板外置，用法与内驱一致，附属于对应 [[entity-电缸]] / [[entity-电爪]]。

> ⚠️ **SAC-NF ≠ SAC-NF2**（[[corrections]] C034）：**SAC-NF 是最早期闭环力控电缸驱动器，基于 SAC-N 的 485 协议研发**，属外置 485 类、不单列。而 **SAC-NF2 是 EtherCAT/CIA402 伺服驱动器**（与 SAC-NP2 同硬件不同固件，见 C017）。两者逻辑完全不一样，读资料时先分清是"NF"还是"NF2"。

⚠️ **SAC-N2 逐渐退市**（选型手册 CN-2025.10 P20 注：可用 SAC-NP2 替代，具体差异咨询销售）。已编译的 SAC-N2 三件套 + EtherCAT 应用手册对在役设备仍有效；新项目选型优先 SAC-NP2。

## 型号清单（完整谱系，据选型手册 CN-2025.10）

> 选型手册将产品分为「控制器」（集成控制+驱动，RS485/IO/脉冲）与「驱动器」（进阶版，EtherCAT CIA402）两类。产品线归属仍按 Fly 定义的限定口径。

### 伺服驱动器（EtherCAT / CIA402，属驱动器产品线）

| 型号 | 定位 | 轴数 | 电源 | 电源容量 | 关键差异 |
|---|---|---|---|---|---|
| **SAC2-NP1-EC** | 单轴标准驱动器（进阶版） | 1 | DC24~72V | 最大 480W | EtherCAT CIA402；编码器 ABZ+HALL/BissC/SSI/多摩川；3A/10A |
| **SAC2-NP1-G** | 单轴标准驱动器（进阶版） | 1 | DC24~72V | 最大 480W | 同硬件，脉冲控制/Modbus-RTU/**CANopen**（General） |
| **SAC-N2** | 双轴控制器（标准版） | 2 | DC24/48V | 240W/480W | ⚠️ **逐渐退市，由 SAC-NP2 替代**；现有手册三件套+EtherCAT 应用仍适用 |
| **SAC-NP2** | 双轴驱动器（进阶版） | 2 | DC24/48V | 240W/480W | N2 替代型号；最小 EtherCAT 周期 **200μs**；速度环 3.5kHz；24bit 编码器 |
| **SAC-NP4** | 四轴标准驱动器（进阶版） | 4 | DC24/48V | 240W/480W | 最小 EtherCAT 周期 **1ms**（≠NP2）；编码器按轴选 A3(增量/BissC/多摩川/ABZ+HALL) 或 A4(增量/SSI/ABZ+HALL)；⚠️ [[corrections]] C012：68xx 轴 2 地址规则对 NP4 **会有差异，须重新确认** |

### 单轴控制器（RS485/IO/脉冲，附属电缸/电爪线，不单列）

| 型号 | 定位 | 电源 | 容量 | 关键差异 |
|---|---|---|---|---|
| **SAC-S** | 小型单轴控制器（简化版） | DC24V | 72W | I/O 16 点位；**不支持力控闭环、不支持抱闸控制**；须搭配泄放电阻 |
| **SAC-N** | 单轴控制器（标准版） | DC24V | 200W | I/O 64 点位；**支持力控闭环、抱闸控制**；3A/10A |
| **SAC-NF** | 单轴专用力控控制器 | 1 | — | — | NF 系列分多个型号，**主力机型 SAC-NF2**：与 SAC-NP2 **同硬件、同操作方式，仅烧录软件区别，后续会统一**（[[corrections]] C017）→ NP2 的调试操作/参数表可直接参照 |

> 通用：输出电流两档 03=3A/9A峰值、10=10A/25~30A峰值；三倍过载 >2.5s；位置/速度/力矩/混合模式；龙门 ns 级同步；STO； EtherCAT/RS485/EtherNet-IP/CC-Link 多协议。

### 音圈执行器配套规则（音圈选型手册 CN-3.3.2025.10 P30）⭐

- **ZR 一体机（DLARA/DLSRA）默认 SAC-NP2（双轴）；单 Z 机（VLA/DLE/VLM）默认 SAC2-NP1（单轴）**
- EtherCAT 细分型号：**SAC-NP2-EC-U-03A1-03A2**（双轴）/ **SAC2-NP1-EC-A-03A2**（单轴）
- NP2/NP1 工作模式：位置轨迹/速度轨迹/力矩轨迹 + 周期同步位置/速度/力矩；每轴 4进2出 数字 I/O；自带软着陆与电子齿轮比

### 第三方驱动器（研控步进，仅 DLSRA 经济型系列选配）

| 型号 | 轴数 | 通讯 | 特点 |
|---|---|---|---|
| 研控 **SSD2205PE-B1** | 单轴 | USB | 体积小、操作简便、性价比高 |
| 研控 **MS-MINI3E-2D** | 双轴 | USB | 集成双轴控制、力控精度优秀、支持力控、自带软着陆与电子齿轮比 |

> ⚠️ 第三方驱动的线材匹配需咨询大寰销售（手册 P30 备注）；不属于驱动器产品线（非原生 ECAT/CIA402），仅作选配记录。

## 关键特性

- **通讯**：原生 EtherCAT
- **轴控协议**：CiA402（标准伺服轴控协议）
- **对象字典**：[[concept-CIA402对象字典]] — SAC_2Axis_V1.7.2 对象字典
- **双轴**：轴1 = Z 轴（直线轴，上下方向），轴2 = R 轴（旋转轴，内置滑环可 360° 无限旋转）
- **轴 2 对象地址**：**68xx 系列是大寰自定义的轴 2 对象地址（非 CIA402 标准），对 SAC-N2 / SAC-NP2 通用；后期拓展 SAC-NP4 时会有差异，须重新确认**（见 [[corrections]] C012）
- **配置文件**：XML / ESI 文件（[[manual-sac-n2-xml-update-guide]]、[[manual-sac-xml-modify-method]]）
- **EtherCAT 协议**：详见 [[manual-sac-n2-ethercat-application]]（状态机/控制字/状态字/PDO/6种控制模式/35种回零/探针/7种PLC适配）

## 关联资料（14 件）

- [[manual-dh-电缸选型手册]] — 电缸选型手册（含驱动器完整谱系表、SAC-S/N 与 NP1/NP2/NP4 参数页）⭐
- [[manual-dh-音圈选型手册]] — 音圈选型手册（驱动器选配表 + X775 线缆料号体系 + 研控第三方驱动）⭐
- [[manual-sac-n2-driver-debug-sop]] — SAC-N2 驱动器调试软件操作及故障分析（跨音圈电机线）
- SAC-NP2 EtherCAT 型双轴驱动器产品操作手册（Ver-M-1.00.12, 2025-10-07）— [[manual-sac-np2-product]] ⭐
- [[manual-sac-nf2-force-control]] — SAC-NF2 柔性力控使用手册（MCK 闭环力控）⭐
- SAC-N2 EtherCAT 应用手册（20260818，跨音圈电机线）— [[manual-sac-n2-ethercat-application]]
- SAC-N2 驱动器初次上电 SOP（20260415）— [[manual-sac-n2-first-power-on-sop]]
- SAC 系列驱动器 USB 升级操作指导文档（20260818）— [[manual-sac-usb-upgrade]]
- SAC-N2 XML 文件更新指导手册（20260818）— [[manual-sac-n2-xml-update]]
- SAC XML 文件修改方法（20260818）— [[manual-sac-xml-modify]]
- 大寰电机 SAC-NP2 驱动参数导入导出 SOP（20260408）— [[manual-sac-np2-param-import-export]]
- SAC_2Axis_V1.7.2 对象字典（xlsx）

## ECAT 盒子（485→ECAT 网关）

⚠️ ECAT 盒子**不属于驱动器产品线**，是 485→EtherCAT 网关，用途是适配外置 485 驱动器型的 [[entity-电缸]] 和 [[entity-电爪]]。相关 SOP 归电缸;电爪。

## See Also

- [[entity-音圈电机]] — 配套电机
- [[entity-电缸]] — 外驱配伺服驱动器形态
- [[concept-CIA402对象字典]]
- [[concept-XML-ESI配置]]
