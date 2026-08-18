---
类型: manual
源文件: raw/manuals/usage/SAC-N2 XML文件更新指导手册_20260818.md
文档版本: 20260818
适配产品线: 驱动器
编译日期: 2026-08-18
状态: 已编译（1 个待确认疑点已汇总上报 Fly，见文末）
---

# SAC-N2 XML 文件更新指导手册

> ⚠️ **用途**：双轴驱动器**烧录/更新 EtherCAT XML 文件**（ESI 描述文件），解决 0x13 错误导致 EtherCAT 主站无法连接的问题
> **产品线**：[[entity-驱动器]]（SAC-NP2 双轴 EtherCAT 型）
> **关联**：[[manual-sac-xml-modify]]（XML 模块/PDO 修改）、[[concept-XML-ESI配置]]

---

## 触发场景 ⭐

上位机连接双轴驱动器后，**数码管提示 0x13 错误** = 双轴驱动器**没有烧录 EtherCAT XML 文件**，导致 EtherCAT 主站无法连接。需先确保已烧录正确 XML。

## 更新流程（8 步）

| 步 | 操作 | 要点 |
|---|---|---|
| 1 | 上位机点「驱动器信息 → 查看 xml 版本」 | 弹出 eeprom programmer 工具（上位机已集成） |
| 2 | **网线连接，非 USB** | ⚠️ 关键前提：电脑与双轴驱动器必须网线连接 |
| 3 | File → Open | 选择要烧录的 XML 文件 |
| 4 | 打开 `SAC_2Axis_V1.6.1.xml` | ⚠️ XML 文件后续持续更新，**选哪个版本需跟技术支持确认** |
| 5 | Slaves → Scan | 扫描连接的 ECAT 从站设备 |
| 6 | 选对应网卡 | ⚠️ 选网线连接电脑的那个网卡 |
| 7 | Slave → Program Selected | 开始升级，**约 40 秒**，期间软件会卡住，耐心等待 |
| 8 | 等待提示「升级已完成」 | 成功 |

---

## 已确认的疑点（原编译不确定点，Fly 已确认）

1. **XML 文件版本**：XML 版本持续更新，但**基础内容不变，各版本基本通用**（C029）；V1.6.1 示例仍有效，选版本时跟技术支持确认即可

---

## See Also

- [[manual-sac-xml-modify]] — XML 模块/PDO 修改方法
- [[manual-sac-n2-ethercat-application]] — SAC-N2 EtherCAT 应用手册（XML 是 EtherCAT 从站描述文件）
- [[concept-XML-ESI配置]] — XML/ESI 配置概念
- [[entity-驱动器]] — SAC-NP2 谱系
