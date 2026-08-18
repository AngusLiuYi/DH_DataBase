---
title: SAC-N2 EtherCAT 应用手册
type: manual
created: 2026-08-18
updated: 2026-08-18
sources: [SAC-N2 EtherCAT应用手册_20260818.md]
product_lines: [音圈电机, 驱动器]
tags: [SAC-N2, EtherCAT, CIA402, PDO, 状态机, 控制字, 状态字, 回零, 探针, PLC适配, TwinCAT, 欧姆龙, 基恩士, 汇川, 固高]
---

# SAC-N2 EtherCAT 应用手册

> **源文件**：`raw/manuals/usage/SAC-N2 EtherCAT应用手册_20260818.md`
> **产品线**：[[entity-音圈电机]] / [[entity-驱动器]]
> **配套**：[[manual-sac-n2-driver-debug-sop]]（调试 SOP）、[[manual-sac-n2-motor-tuning]]（整定参考）、[[manual-sac-n2-faq]]（FAQ）

## 概述

SAC-N2 双轴驱动器 EtherCAT 总线通讯完整手册，涵盖硬件配置、EtherCAT 协议规格、PDO 对象字典、7 种 PLC 适配案例、CIA402 状态机（控制字/状态字 bit 级定义）、6 种控制模式、回零 35 种方法、探针功能。FAE 总线通讯与协议级排查核心参考。

---

## 一、硬件配置

> 📷 界面截图：见原文件第一章 — 接口定义面板 + 驱动器接线图（用于硬件接线确认）

---

## 二、EtherCAT 总线通讯

### 2.1 EtherCAT 规格

| 项目 | 规格 |
|---|---|
| 适用标准 | IEC 61158 Type12 / IEC 61800-7 CiA402 Drive Profile |
| 传输协议 | 100BASE-TX（IEEE802.3） |
| 总线接口 | Signal IN 接口10 / Signal OUT 接口11 |
| 缆线 | 5 类双绞线 |
| SM 通道 | SM0 输出邮箱 / SM1 输入有效 / SM2 输出过程数据 / SM3 输入过程数据 |
| FMMU | FMMU0 RxPDO输出 / FMMU1 TxPDO输出 / FMMU2 邮箱状态 |
| PDO 数据 | 动态 PDO 映射 |
| Mailbox(COE) | 紧急时间 / SDO 请求 / SDO 响应 |
| 分布时钟(DC) | Free Run + DC 模式，同步周期最低 **500μs** |

### 2.2 LED 指示灯

| 状态 | 说明 |
|---|---|
| ACT 长灭 | 无定义 |
| LINK 常亮 | 链路已连接，无数据交互 |
| LINK 熄灭 | 物理层无连接，EtherCAT 未启动 |
| LINK 闪烁 | 正在进行数据交互 |

### 2.3 PDO 对象字典

SAC-N2 有 4 个可配置 PDO：2 个 RxPDO + 2 个 TxPDO，轴 1 分配 1600H/1A00H，轴 2 分配 1610H/1A10H。提供 3 组配置（CSP/CSV/CST）。

**RxPDO（主站→驱动器）**

| 索引 | Sub | 对象 | CSP | CSV | CST |
|---|---|---|---|---|---|
| 1600H/1610H | 01 | 控制字 Control Word 6040H | ✓ | ✓ | ✓ |
| | 02 | 目标位置 Target Position 607AH | ✓ | | |
| | 02 | 目标速度 Target Velocity 60FFH | | ✓ | |
| | 02 | 目标力矩 Target Torque 6071H | | | ✓ |
| | 03 | 操作模式 Modes Of Operation 6060H | ✓ | ✓ | ✓ |

**TxPDO（驱动器→主站）**

| 索引 | Sub | 对象 | CSP | CSV | CST |
|---|---|---|---|---|---|
| 1A00H/1A10H | 01 | 状态字 Status Word 6041H | ✓ | ✓ | ✓ |
| | 02 | 位置反馈 Actual Position 6064H | ✓ | | |
| | 02 | 速度反馈 Actual Velocity 606CH | | ✓ | |
| | 02 | 力矩反馈 Actual Torque 6077H | | | ✓ |
| | 03 | 工作模式反馈 6061H | ✓ | ✓ | ✓ |

### 2.4 ESI 设备描述文件

- XML 格式，描述从站配置信息（制造商信息 + 从站描述）
- 主站下载到从站 EEPROM，通过 I2C 与 ESC 芯片寄存器交换数据
- 详见 [[manual-sac-n2-xml-update-guide]]（XML 文件更新指导手册）

### 2.5 EtherCAT 状态机（ESM）

| 状态 | 通讯能力 |
|---|---|
| **Init (I)** | 无邮箱通讯，无过程数据 |
| **Pre-OP (P)** | 邮箱通讯激活，无过程数据 |
| **Safe-OP (S)** | 传送实际输入数据，输出设为安全状态 |
| **Operational (O)** | 可进行过程数据通讯 |

转换：Init → Pre-OP（配置邮箱+DC）→ Safe-OP（配置 SM/FMMU/PDO 映射）→ OP（发送有效输出数据）

### 2.6 通讯模式

| 模式 | 触发方式 | 同步性 |
|---|---|---|
| **Free Run** | 本地定时器中断 | 各从站不同步 |
| **SM** | 数据输入/输出事件触发 | 同步于数据事件 |
| **DC** | SYNC 信号触发 | 主从时钟同步，最高同步性能 |

> 注：DC 模式下数据帧须比 SYNC 信号先到，从站在 SYNC 前完成数据交换与控制计算。

---

## 三、切换 EtherCAT 控制

使用 EtherCAT 控制前，需通过上位机参数表 **0x2002.01** 设置为 EtherCAT 总线控制，保存参数后**重启驱动器**。

> **0x2002.01 为枚举型参数，值 9 = EtherCAT 控制**（与 FAQ Q9「控制模式选 9」是同一参数的地址与界面枚举值，见 [[corrections]] C011）。

> 📷 界面截图：见原文件第三章 — 0x2002.01 参数设置面板（用于切换总线控制模式）

> 交叉引用：[[manual-sac-n2-faq]] Q9 — 数码管显示 000 而非 888，根因为控制模式未设为 EtherCAT（值=9）。

---

## 四、PLC 适配案例（7 种）

### 4.1 倍福 TwinCAT3

| 步骤 | 操作 |
|---|---|
| XML 安装 | 放入 `C:\TwinCAT\3.1\Config\Io\EtherCAT` |
| 组态 | IO→Devices→Scan，搜索从站 |
| 激活 | 工具栏激活配置，TwinCAT 自动绑定 NC 轴 |
| 编码器单位 | Axes→Axis1→Enc 配置 |
| CSP 使能 | Online 选项卡→Set→勾选 3 项→OK |
| PLC 控制 | 加载 Tc2_MC2 库，定义轴变量，Link to PLC |

**回零测试**：支持原点开关回零、挡板回零（无原点开关）、Z 相回零三种方式。

> 📷 界面截图：见原文件 3.1 节 — TwinCAT3 工程配置/组态/编码器/使能/PLC 绑定面板

### 4.2 欧姆龙 NX1P2

| 步骤 | 操作 |
|---|---|
| 连接 | PLC 默认 IP 192.168.250.1，Ethernet via hub |
| XML 加载 | EtherCAT→Master→Display ESI Library→Install(File) |
| 组态 | 拖动 XML 到 Master 下方 |
| 轴绑定 | Motion Control Setup→Axis Settings→Add→Servo axis→Node 1 Slot0（轴1） |
| 节点地址 | 右键 Master→Write Slave Node Address，需与网络分配一致，**重启 PLC 生效** |

**可用 Motion Control 模块**：MC_Power（使能）/ MC_MoveAbsolute（CSP）/ MC_TorqueControl（CST）/ MC_SyncMoveVelocity（CSV）

> 📷 界面截图：见原文件 3.2 节 — 欧姆龙工程/XML 加载/轴绑定/节点地址面板

### 4.3 基恩士 KV7500

| 步骤 | 操作 |
|---|---|
| 连接 | PLC 默认 IP 192.168.0.10，Ethernet |
| XML 添加 | 添加从站配置 PDO 参数，**选择扩展设定**，从站属性改为双轴驱动 |
| 调试 | 下载程序→登录监控器→运动模块→单元监控器→试运转→定位→选轴号 |

> 📷 界面截图：见原文件 3.3 节 — 基恩士运动控制模块/XML 配置/试运转面板

### 4.4 汇川 AM403（含回零与力矩控制详解）

| 步骤 | 操作 |
|---|---|
| 工程 | 新建标准工程 |
| 主站 | 添加 EtherCAT 主站 |
| XML | 添加双轴驱动器 XML 文件 |
| 从站 | 添加从站设备 |
| 网络 | Device→Scan network→选 PLC 型号 |
| 电机 | 添加两个电机，配置参数 |
| 轴程序 | 添加轴控制程序，**须挂在 EtherCAT 任务下**（任务更换） |

**回零配置（关键）**：

| 轴 | 回零方式 | SDO 参数 |
|---|---|---|
| **Z 轴** | 方法 34（极限回零后寻 Z 相） | 6098H(Homing Method) / 6099:01(寻开关速度) / 6099:02(寻零点速度) / 609AH(加速度) |
| **R 轴** | 方法 3（光电信号后寻 Z 相） | **6898H**(Homing Method) / **6899:01**(寻开关速度) / **6899:02**(寻零点速度) / **689AH**(加速度) |

> 注：R 轴 SDO 地址为 68xx 系列。**68xx 是大寰自定义的轴 2 对象地址（非 CIA402 标准），对 SAC-N2 / SAC-NP2 通用；后期拓展 SAC-NP4 时会有差异，届时须重新确认**（见 [[corrections]] C012）。

**力矩控制（关键）**：

- 可用 `MC_TorqueControl` 或 `SMC_SetTorque` 切换力矩模式
- **限制**：`MC_TorqueControl` 需绑定 607F（Max profile velocity），但**双轴 607F 不可映射** → 改用 `SMC_SetTorque`。根因是**汇川 PLC 当前版本不兼容**（非驱动器固件限制）；汇川新版本优化之前，SMC_SetTorque 是标准替代方案（见 [[corrections]] C013）
- **模式切换**：`MC_Stop` 的使能信号 K **必须断使能**，否则模式无法切换成功
- **速度限制**：力矩控制下需设 6080（max motor speed）为非零值，单位 RPM；设 0 则电机不动

> 📷 界面截图：见原文件 3.4 节 — 汇川工程/主站/XML/从站/网络/电机配置/轴程序/回零 SDO/力矩控制面板

### 4.5 汇川 H5U

- 变量表配置 + 编码器分辨率配置 + 梯形图程序 + 回零配置

> 📷 界面截图：见原文件 3.5 节 — H5U 变量表/编码器/梯形图/回零配置面板

### 4.6 MaxTang NX6412

- 安装丢失的库文件后组态

> 📷 界面截图：见原文件 3.6 节 — MaxTang 库文件安装与组态面板

### 4.7 固高 GEN 控制卡

- XML 放入 Devices 目录后组态

> 📷 界面截图：见原文件 3.7 节 — 固高 GEN 控制卡 Devices 目录与组态面板

> 交叉引用：固高板卡适配大寰总线产品详见通用线「固高板卡适配大寰总线产品(电爪、音圈)」技术样本。

---

## 五、CIA402 协议设备控制

### 5.1 CIA402 状态机

SAC-N2 按 CIA402 状态机工作，通过 6040H 控制字控制状态，6041H 状态字读取实时状态。

**8 种状态**：

| 状态 | 说明 |
|---|---|
| Not ready to switch on | 初始化，参数不可设定，不能执行驱动功能 |
| Switch on disabled | 无故障，参数可设定 |
| Ready to switch on | 已准备就绪，参数可设定 |
| Switched on | 等待打开伺服使能，参数可设定 |
| **Operation enable** | 正常运行，已使能某模式，电机已通电，参数可设定 |
| Quick stop | 快速停机执行中，参数可设定 |
| Fault reaction active | 故障停机执行中，参数可设定 |
| Fault | 故障停机完成，所有驱动功能禁止，允许改参数排故 |

**状态转换表（控制字 → 状态字）**：

| 转换 | 控制字 6040H | 状态字 6041H |
|---|---|---|
| 0 (初始化) | 自然过渡 | 0000H |
| 1 | 自然过渡 | 0250H |
| 2 (→Ready) | 0006H | 0231H |
| 3 (→Switched on) | 0007H | 0233H |
| 4 (→Operation enable) | 000FH | 0237H |
| 5 (→Switched on) | 0007H | 0233H |
| 6 (→Ready) | 0006H | 0231H |
| 7 (→Switch on disabled) | 0000H | 0250H |
| 11 (→Quick stop) | 0002H | 0217H |
| 12 (Quick stop 完成) | 605A 写 0~2，自然过渡 | 0250H |
| 13 (→Fault reaction) | 故障自动切换 | 021FH |
| 14 (→Fault) | 自然过渡 | 0218H |
| 15 (Fault reset) | 0080H | 0250H |
| 16 (Quick stop 后→OP) | 605A 选 5~6，完成后发 0FH | 0237H |

### 5.2 控制字 6040H bit 定义

| bit | 名称 | 说明 |
|---|---|---|
| bit0 (so) | switch on | 上电 |
| bit1 (ev) | enable voltage | 使能电压 |
| bit2 (qs) | quick stop | 快速停机（0=触发） |
| bit3 (eo) | enable operation | 使能运行 |
| bit7 (fr) | fault reset | 故障复位 |
| bit8 (h) | halt | 暂停（置1按 605Dh 减速暂停） |

**常用控制命令**：

| 命令 | bit3 | bit2 | bit1 | bit0 | 转换 |
|---|---|---|---|---|---|
| Shutdown | - | 1 | 1 | 0 | 2,6,8 |
| Switch on | 0 | 1 | 1 | 1 | 3 |
| **Switch on + Enable operation** | 1 | 1 | 1 | 1 | 3+4 |
| Disable voltage | - | - | 0 | - | 7,9,10,12 |
| Quick stop | - | 0 | 1 | - | 7,10,11 |
| Fault reset | - | - | - | - | 15 |

bit4/5/6 因模式不同定义不同（PP: New set-point / Change set / Abs·Rel；HM: Start homing；IP: Enable interpolation）

### 5.3 状态字 6041H bit 定义

| bit | 名称 | 说明 |
|---|---|---|
| bit0 (rtso) | ready to switch on | 准备好 |
| bit1 (so) | switched on | 已使能 |
| bit2 (oe) | operation enabled | 运行中 |
| bit3 (f) | fault | 故障 |
| bit4 (ve) | voltage enabled | 主电源接通 |
| bit5 (qs) | quick stop | 0=正在快速停机 |
| bit7 (w) | warning | 警告中（电机继续运行） |
| bit9 (rm) | remote | 固定为 1 |
| bit11 (ila) | internal limit active | 内部转矩超限或撞限位 |

**状态字 → 驱动器状态对照**：

| 状态字模式 | 驱动器状态 |
|---|---|
| xxxx xxxx x1xx 0000 | Switch on disabled |
| xxxx xxxx x01x 0001 | Ready to switch on |
| xxxx xxxx x01x 0011 | Switched on |
| xxxx xxxx x01x 0111 | **Operation enabled** |
| xxxx xxxx x00x 0111 | Quick stop active |
| xxxx xxxx x0xx 1111 | Fault reaction active |
| xxxx xxxx x0xx 1000 | Fault |

---

## 六、控制模式（6 种）

### 6.1 位置控制

| 模式 | 6060H 值 | 轨迹生成 | 关键对象 |
|---|---|---|---|
| **PP（轮廓位置）** | 1 | 驱动器内部 | 607AH(目标位置) / 6081H(速度) / 6083H(加速度) / 6084H(减速度) |
| **CSP（同步位置）** | 8 | 主站 | 607AH(目标位置) + DC 模式 |

> 区别：PP 由驱动器内部轨迹发生器生成，CSP 由主站生成位置轨迹并发送。

### 6.2 速度控制

| 模式 | 6060H 值 | 轨迹生成 | 关键对象 |
|---|---|---|---|
| **PV（轮廓速度）** | 3 | 驱动器内部 | 60FFH(目标速度) / 607FH(最大速度) / 6083H(加速度) / 6084H(减速度) |
| **CSV（同步速度）** | 9 | 主站 | 60FFH(目标速度) + DC 模式 |

### 6.3 转矩控制

| 模式 | 6060H 值 | 轨迹生成 | 关键对象 |
|---|---|---|---|
| **PT（轮廓转矩）** | 4 | 驱动器内部 | 6071H(目标力矩,0.1%) / 6072H(最大力矩) / 6087H(力矩变化率) |
| **CST（同步转矩）** | 10 | 主站 | 60F1H(目标转矩) + DC 模式 |

> 交叉引用：力矩反馈 6077H 同见于 [[manual-sac-n2-driver-debug-sop]] 第七章开环力控（0x5018 力传感器对比值 ↔ 6077H 力矩反馈）与 [[concept-开环力控]]。

---

## 七、回零（Homing Mode）

### 7.1 关键对象

| 索引 | 子索引 | 对象 | 单位 |
|---|---|---|---|
| 6040H | 00 | Control word | - |
| 6098H | 00 | Homing method | - |
| 6099H | 01 | 寻开关速度 | 指令单位/s |
| 6099H | 02 | 寻零点速度 | 指令单位/s |
| 609AH | 00 | 回零加速度 | 指令单位/s |
| 607CH | 00 | 原点偏移 | 指令单位 |

> 操作：设 6060H=6 → 设 6098H(1~35) → 设速度/加速度 → 6040H 使能启动 → 查 6041H 状态

### 7.2 回零方法分类（35 种）

| 方法 | 信号组合 | 运动方向 |
|---|---|---|
| 1-2 | 限位开关下降沿 + Z 相 | 负/正限位 |
| 3-6 | 原点开关边沿 + Z 相脉冲 | 正/负向原点开关 |
| 7-10 | 原点开关 + Z 相 + 正限位 | 带正限位回退 |
| 11-14 | 原点开关 + Z 相 + 负限位 | 带负限位回退 |
| 15-16 | 保留 | - |
| 17-18 | 限位开关下降沿（无 Z 相） | 负/正限位 |
| 19-22 | 原点开关边沿（无 Z 相） | 正/负向 |
| 23-26 | 原点开关 + 正限位（无 Z 相） | 带正限位回退 |
| 27-30 | 原点开关 + 负限位（无 Z 相） | 带负限位回退 |
| 31-32 | 保留 | - |
| 33-34 | 单向移动 + Z 相脉冲 | 仅 Z 相 |
| 35 | 当前位置回零 | 直接置零 |

> 注：默认运动方向左→右为正。原点开关在电机右侧=正向，左侧=负向。

> 交叉引用：汇川 AM403 案例中 Z 轴用方法 34（极限+Z相），R 轴用方法 3（光电信号+Z相），详见第四章 4.4。

---

## 八、探针功能（Touch Probe）

位置锁存功能，通过外部数字输入或编码器 Z 相实时锁存位置。应用于模切、印刷等位置同步场合。

| 模式 | 说明 | 60B8H bit |
|---|---|---|
| 事件模式 (Trigger first event) | 触发后锁存一次，需重新启动下次 | bit1/9 设置 |
| 连续模式 (Continuous) | 每次上升沿都锁存，新数据覆盖旧数据 | bit1/9 设置 |

**关键对象**：

| 索引 | 对象 | PDO |
|---|---|---|
| 60B8H | Touch probe function（配置+启动） | RxPDO |
| 60B9H | Touch probe status（锁存状态） | TxPDO |
| 60BAH | Touch probe pos1 pos value | TxPDO |
| 60BBH | Touch probe pos1 neg value | TxPDO |
| 60BCH | Touch probe pos2 pos value | TxPDO |
| 60BDH | Touch probe pos2 neg value | TxPDO |

> 📷 界面截图：见原文件 4.7 节 — 探针事件/连续模式配置与状态面板

---

## 关键对象字典速查

> 本手册涉及的高频 CIA402 对象，按索引汇总。

| 索引 | 名称 | PDO | 出现章节 |
|---|---|---|---|
| 6040H | Control word 控制字 | RxPDO | 状态机/所有模式 |
| 6041H | Status word 状态字 | TxPDO | 状态机/所有模式 |
| 6060H | Modes of operation 操作模式 | RxPDO | 所有模式切换 |
| 6061H | Modes of operation display 模式反馈 | TxPDO | 所有模式 |
| 607AH | Target position 目标位置 | RxPDO | PP/CSP |
| 60FFH | Target velocity 目标速度 | RxPDO | PV/CSV |
| 6071H | Target torque 目标力矩(0.1%) | RxPDO | PT |
| 60F1H | Target torque 目标转矩 | RxPDO | CST |
| 6077H | Torque actual value 力矩反馈(0.1%) | TxPDO | PT/CST |
| 6064H | Position actual value 位置反馈 | TxPDO | PP/CSP |
| 606CH | Velocity actual value 速度反馈 | TxPDO | PV/CSV |
| 6098H | Homing method 回零方法 | RxPDO | 回零 |
| 6099H | Homing speeds 回零速度 | RxPDO | 回零 |
| 609AH | Homing acceleration 回零加速度 | RxPDO | 回零 |
| 607CH | Homing offset 原点偏移 | RxPDO | 回零 |
| 607FH | Max profile velocity 最大速度 | RxPDO | PV（双轴不可映射） |
| 6080H | Max motor speed 最大电机速度(RPM) | SDO | 力矩控制速度限制 |
| 605AH | Quick stop option 快速停机选项 | SDO | 状态转换 12/16 |
| 605DH | Halt option 暂停选项 | SDO | halt bit8 |
| 60B8H | Touch probe function 探针功能 | RxPDO | 探针 |
| 60B9H | Touch probe status 探针状态 | TxPDO | 探针 |
| 0x2002.01 | 总线控制模式选择 | 上位机 | EtherCAT 切换 |
| 6898H | Homing method (轴2) | SDO | R 轴回零 |
| 6899H | Homing speeds (轴2) | SDO | R 轴回零 |
| 689AH | Homing acceleration (轴2) | SDO | R 轴回零 |

> 注：68xx 系列为**大寰自定义的轴 2 对象地址**（非 CIA402 标准），对 SAC-N2 / SAC-NP2 通用，SAC-NP4 拓展时会有差异（见 [[corrections]] C012）。

---

## See Also

- [[manual-sac-n2-driver-debug-sop]] — SAC-N2 驱动器调试 SOP（回零操作流程、故障码、力控标定）
- [[manual-sac-n2-motor-tuning]] — SAC-N2 电机整定参考（编码器配置、刚性表、三环整定）
- [[manual-sac-n2-faq]] — SAC-N2 FAQ（Q9 控制模式、Q12 XML 同步、Q4 编码器误报）
- [[entity-音圈电机]] — 音圈电机产品线
- [[entity-驱动器]] — 驱动器产品线（SAC-N2 双轴伺服驱动器）
- [[concept-开环力控]] — 力控应用（6077H 力矩反馈）
- [[concept-CIA402对象字典]] — 对象地址体系
