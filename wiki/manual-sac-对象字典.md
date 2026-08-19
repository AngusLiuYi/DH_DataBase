---
类型: manual
源文件: raw/manuals/适配文档/SAC_2Axis_V1.7.2对象字典.xlsx
文档版本: V1.7.2
适配产品线: 驱动器
编译日期: 2026-08-19
状态: 已编译
---

# SAC 双轴驱动器对象字典（V1.7.2）

> ⚠️ **用途**：SAC 双轴伺服驱动器（SAC-NP2 等）EtherCAT CoE 对象字典，轴 1 + 轴 2 + 预设 PDO
> **产品线**：[[entity-驱动器]]
> **关联**：[[manual-sac-xml-modify]]（XML 模块/PDO，与对象字典同用处，[[corrections]] C031）、[[manual-sac-n2-ethercat-application]]（CIA402）

---

## 一、结构

| Sheet | 内容 |
|---|---|
| **轴 1** | 轴 1 对象字典（0x1000 起，618 行） |
| **轴 2** | 轴 2 对象字典（0x2800 起，547 行） |
| **预设 PDO** | 3 个模块（CSP/CSV/CST、BYD、Force Control）的 RxPdo/TxPdo 映射 |

## 二、标准对象（轴 1，CIA402 通用）

| 索引 | 名称 | 说明 |
|---|---|---|
| 0x1000 | Device Type | 设备类型 |
| 0x1001 | Error Register | 故障寄存器 |
| 0x1008/1009/100A | 设备名称/硬件版本/软件版本 | 厂商信息 |
| 0x1018 | Identity | 厂商代码 0x620A0000、产品代码等 |
| 0x1600/1601 | RxPDO Mapping | 接收 PDO 映射 |
| 0x1A00/1A01 | TxPDO Mapping | 发送 PDO 映射 |
| 0x1C00 | Sync Manager | SM 通讯类型 |

## 三、预设 PDO 三模块（印证 C030）⭐

| 模块 | 定位 | 关键对象 |
|---|---|---|
| **Module 1 = CSP/CSV/CST** | 周期同步位置/速度/力矩（0x101） | 控制字 0x6040、目标位置 0x607A、目标速度 0x60FF、目标力矩 0x6071、操作模式 0x6060 |
| **Module 2 = BYD Customization** | 比亚迪定制（0x102） | 控制字 0x6040、转矩限制 0x5012 |
| **Module 3 = Force Control** | 力控（0x103） | 控制字 0x6040、目标力矩 0x6071、探针功能 0x60B8 |

**TxPdo（从站→主站）通用**：状态字 0x6041、实际位置 0x6064、实际速度 0x606C、实际力矩 0x6077、操作模式显示 0x6061

> 三个模块对应 XML 里 Slot 语法的 0x101/0x102/0x103（见 [[manual-sac-xml-modify]]，[[corrections]] C030）。

## 四、轴 2 对象（0x2800 起）

轴 2 对象从 **0x2800** 开始（轴 1 从 0x1000），包含电机参数（额定电压/功率/电流、电流环/速度环/位置环增益、载波频率、死区时间等），是轴 2 的伺服参数区。

## 售后关键口径 ⭐

- **轴 1 对象 0x1000 起，轴 2 对象 0x2800 起**——读轴 2 参数时注意地址偏移
- 本表与 XML 内 Object 标签对象定义**同一个用处**（C031），可互相参照
- 预设 PDO 三模块：0x101=CSP/CSV/CST、0x102=BYD、0x103=Force Control（C030）
- 完整对象清单（618+547 行）见原 xlsx

---

## See Also

- [[manual-sac-xml-modify]] — XML 模块/PDO 修改（与本表同用处）
- [[manual-sac-n2-ethercat-application]] — EtherCAT/CIA402 应用手册
- [[entity-驱动器]] — SAC 驱动器谱系
- [[concept-CIA402对象字典]] — CIA402 对象字典概念
- [[corrections]] C030/C031
