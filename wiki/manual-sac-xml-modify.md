---
类型: manual
源文件: raw/manuals/usage/SAC XML文件修改方法_20260818.md
文档版本: 20260818
适配产品线: 驱动器
编译日期: 2026-08-18
状态: 已编译（2 个待确认疑点已汇总上报 Fly，见文末）
---

# SAC XML 文件修改方法

> ⚠️ **用途**：修改驱动器 XML 的**默认模块（Slot 语法）** 与 **PDO 列表**，适配不同客户的使用场景
> **产品线**：[[entity-驱动器]]
> **关联**：[[manual-sac-n2-xml-update]]（XML 烧录）、[[manual-sac-n2-ethercat-application]]、[[concept-XML-ESI配置]]

---

## 一、模块（Slot）语法与默认模块设置 ⭐

驱动器 XML 采用 **slot 语法**，有 **3 个模块**，ID 分别为 **0x101 / 0x102 / 0x103**。通过修改 `Default="1"` 设定默认使用的模块。

**模块 ID 对应关系**：

| 模块 ID | 对应功能 |
|---|---|
| **0x101** | **CSP / CSV / CST**（周期同步位置/速度/力矩） |
| **0x102** | **BYD Customization**（比亚迪定制） |
| **0x103** | **Force Control**（力控） |

> ⚠️ **3 个模块只能有 1 个 Default=1**。

默认模块设置示例（Slot 标签内，每个轴 Slot 都要改）：

```xml
<Slot MinInstances="1" MaxInstances="1">
  <Name LcId="1033">Axis 1</Name>
  <ModuleIdent Default="0">#x0101</ModuleIdent>
  <ModuleIdent Default="0">#x0102</ModuleIdent>
  <ModuleIdent Default="1">#x0103</ModuleIdent>
</Slot>
```

## 二、修改默认 PDO 列表 ⭐

出厂 XML 默认配置了一些 PDO，无法覆盖所有客户场景：
- 有的客户要**尽可能多的对象映射到 PDO**（方便操作）
- 有的要**尽可能少的 PDO**（保证通讯性能）

### PDO 定位

定位到 **Modules → Module（如 0x101）→ RxPdo / TxPdo**：
- **RxPdo** = 主站发送到从站的数据（如控制字）
- **TxPdo** = 从站返回给主站的数据（如状态字）

### 增删 PDO 对象

展开 RxPdo/TxPdo，可看到 6040、607A 等对象定义。要修改默认 PDO 对象，**增加 Entry 标签**即可。

### Entry 标签字段

| 字段 | 说明 |
|---|---|
| `<Entry></Entry>` | 定义一个 PDO |
| `<Index></Index>` | 对象索引，如 5018 对象写 `#x5018`（x 表 16 进制） |
| `<SubIndex></SubIndex>` | 对象的子索引 |
| `<BitLen></BitLen>` | 对象长度，单位 bit |
| `<Name></Name>` | 对象显示名 |
| `<Comment></Comment>` | 附加说明（可选） |
| `<DataType></DataType>` | 对象类型 |

> 对象的 Index/SubIndex/BitLen/DataType 等信息，翻看 XML 前面 Object 标签下的对象定义填入即可。

---

## 已确认的疑点（原编译不确定点，Fly 已确认）

1. **模块 ID 归属**：确认笔误，**0x101=CSP/CSV/CST、0x102=BYD Customization、0x103=Force Control**（C030）——上文模块表已按正确写法记录
2. **对象定义与字典口径**：XML 内 Object 标签的对象定义与对象字典 xlsx **是同一个用处**，可互相参照（C031）

---

## See Also

- [[manual-sac-n2-xml-update]] — XML 烧录/更新
- [[manual-sac-n2-ethercat-application]] — EtherCAT 应用手册（CIA402 + PDO 映射）
- [[concept-XML-ESI配置]] — XML/ESI 概念
- [[entity-驱动器]] — SAC-NP2 谱系
