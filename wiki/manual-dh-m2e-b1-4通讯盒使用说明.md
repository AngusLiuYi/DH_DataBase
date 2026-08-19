---
类型: manual
源文件: raw/manuals/使用手册/标准使用手册/M2E-B1-4+V5.x+使用说明书.docx
文档版本: V5.x
适配产品线: 电缸;电爪
编译日期: 2026-08-19
状态: 已编译
---

# DH EtherCAT 5.x 通讯盒使用说明（M2E-B1-4）

> ⚠️ **用途**：M2E-B1-4 通讯协议转换网关，把一体式执行器（夹爪/电缸）的 Modbus-RTU 转成 EtherCAT(CoE)，对接 PLC/机器人
> **产品线**：[[entity-电缸]] / [[entity-电爪]]（ECAT 盒子归属，C005）
> **关联**：[[manual-dh-ecat盒子固件升级]]、[[manual-dh-基恩士适配ecat盒子]]

---

## 一、概述

一体式执行器（电缸/电爪）仅支持 Modbus-RTU 和 IO，需用 CoE 协议时用本设备转换。本盒子对应 **4 路执行器**（一拖四）。

## 二、设备信息

- **兼容**：目前只兼容 **485 通讯**夹爪/电缸；CAN 接口预留
- **接口**：ECAT_IN / ECAT_OUT（组态下一从站）、4 路执行器插座、电源

### 指示灯状态 ⭐ 售后判态

| LED 状态 | 含义 |
|---|---|
| 绿蓝红全亮 | 上电底层升级程序运行中 |
| 仅绿灯亮 | 电源接通、应用运行正常 |
| 绿灯 + 蓝灯 | 接夹爪、通讯成功 |
| 绿灯 + 红灯 | **通讯不上或没接夹爪 / 未烧录 ESI 文件** |

## 三、快速使用指南

### 连接硬件
1. 执行器电源 + 485 接盒子插座
2. PLC ECAT 输出网线接盒子 **ECAT_IN**（ECAT_OUT 接下一从站 IN）
3. 上电：正常时**绿蓝常亮**；没接执行器或未烧 ESI 时**绿红常亮**

### 适配倍福 TwinCAT 主站（3.2）
- XML 文件放 `C:\TwinCAT\3.1\Config\Io\EtherCAT`
- 扫描从站 → 组态 → Box1 的 Online 看 Current State = **OP** 为正常
- ⚠️ **盒子默认适配电缸**，用夹爪需切 PDO；**电缸和电爪 PDO 互斥**，先取消原组再勾选新组
- 回零：PDO 映射 ECylinder1 RxPDO → Return Home，Write 输入 165；**PDO 值改变才生效**，再次回零先写 0 再写 165

### 适配欧姆龙主站（3.3）
- PC 与 PLC 同网段（欧姆龙默认 IP 192.168.250.1）
- 安装 ESI → 拖到 Master → Write Slave Node Address 改节点地址 1 → 重启 PLC → To Controller 下载

### 适配基恩士主站（3.4）
- 见 [[manual-dh-基恩士适配ecat盒子]] 专项 SOP

## 四、软件升级（第四章）

- USB 连盒子（需供电），上位机 EnterBoot 进升级模式（三 LED 全亮）
- Browse 选 bin 文件（联系技术支持确认）→ Start 烧录 → IAP Finish → 断电等 LED 全灭再上电

## 五、ESI 文件更新（第五章）

- 上位机 → 通讯盒升级 → EEPROM，网线连盒子，可查看/更新 ESI 版本

## 售后关键口径 ⭐

- **绿红常亮** = 通讯不上 / 没接夹爪 / 未烧 ESI——先查这三点
- **电缸电爪 PDO 互斥**，切换要先把原来的取消勾选
- **盒子默认适配电缸**，夹爪要手动切 PDO
- PDO 值改变才生效（回零写 165，再次回零先写 0）

---

## See Also

- [[manual-dh-ecat盒子固件升级]] — 固件/ESI/CFG 升级
- [[manual-dh-基恩士适配ecat盒子]] — 基恩士 KV 专项适配
- [[manual-dh-电缸选型手册]] 第六章 / [[manual-dh-电爪选型手册]] 第六章 — 通讯转换模块表
- [[entity-电缸]] / [[entity-电爪]]
