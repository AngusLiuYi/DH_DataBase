---
类型: manual
源文件: raw/manuals/使用手册/固件更新SOP/ECAT盒子固件升级SOP_（包括ESI与CFG_20240518 + 仅升级ESI与CFG_20250222）.docx
文档版本: 20240518 / 20250222
适配产品线: 电缸;电爪
编译日期: 2026-08-19
状态: 已编译
---

# DH ECAT 盒子固件升级 SOP

> ⚠️ **用途**：ECAT 盒子（485→EtherCAT 网关）的 **ESI / Bin / CFG 三类文件升级**
> **产品线**：[[entity-电缸]] / [[entity-电爪]]（ECAT 盒子归属，见 [[corrections]] C005）
> **两个版本**：`包括ESI与CFG`（全量升级，含 Bin 固件）+ `仅升级ESI与CFG`（跳过 Bin，适用已烧录固件的盒子）

---

## 一、升级 ESI 文件（两版通用）

| 步 | 操作 |
|---|---|
| 1 | ECAT 盒子正常上电，**断开网络总线** |
| 2 | 网线连接盒子的 **ECAT_IN** 与 PC |
| 3 | 电脑打开 EEPROM 软件，选连接的网卡，扫描 |
| 4 | 连接成功后显示当前 ESI 版本 |
| 5 | 选要刷入的 ESI 文件（⚠️ 一定选 `M2E_B1_x_ESI_xxxxxxx.xml`） |
| 6 | 点 Program Selected 刷入，**界面假死 30~60s 不要重复点**，等状态栏 finished |

## 二、升级 Bin 文件（固件，仅"包括ESI与CFG"版）

| 步 | 操作 |
|---|---|
| 1 | 安装升级软件与驱动 |
| 2 | MicroUSB 线连电脑与盒子 |
| 3 | 设备管理器查看端口 |
| 4 | 升级软件选正确端口 |
| 5 | Browse 选相应 bin 文件 |
| 6 | 进升级模式，点升级，等完成 |
| 7 | 重启通讯盒 |

## 三、升级 CFG 文件

| 步 | 操作 |
|---|---|
| 1 | Bin 升级后盒子自动重启，**重新插拔确保端口识别** |
| 2 | Browse 选 `M2E_1_x_CGF_xxxxxxxx.xml` |
| 3 | 点 **Clear Xml Data** 擦除原 CFG，等绿灯亮（⚠️ 绿灯不亮基本是端口没识别） |
| 4 | 点 **Enter Config** 进升级 Config 模式，等绿灯亮 + Download 按钮亮 |
| 5 | 点 Download 升级成功 |

> 新版（20250222）在选端口后多了"点 Query 读取版本号与 CFG 文件号"来判别是否连上盒子。

## 售后关键口径 ⭐

- **三类文件**：ESI（EtherCAT 从站描述，网线 + EEPROM 软件）、Bin（固件，USB + 升级软件）、CFG（配置，USB）
- ESI 升级会**假死 30~60s**，别重复点
- CFG 绿灯不亮 = 端口没识别到，先查端口

---

## See Also

- [[manual-dh-m2e-b1-4通讯盒使用说明]] — 通讯盒使用说明（5.x）
- [[manual-dh-电缸选型手册]] 第六章 / [[manual-dh-电爪选型手册]] 第六章 — 通讯转换模块表
- [[entity-电缸]] / [[entity-电爪]]
- [[corrections]] C005（ECAT 盒子归属电缸;电爪）
