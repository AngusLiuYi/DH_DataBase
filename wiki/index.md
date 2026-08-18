# Wiki 索引

> 总页面数: 19 ｜ 已编译资料: 14/41 ｜ 最后更新: 2026-08-18
> 覆盖产品线: 音圈电机, 电缸, 电爪, 驱动器

## 按类型

### 实体 (4)
- [[entity-音圈电机]] — 音圈电机产品线：在售 VLA/DLARA/DLSRA/DLE/VLM·VLMF；VLAR 退市、DLAR/DLSR 更名记录；ZR默认NP2/单Z默认NP1
- [[entity-电缸]] — 电缸产品线：MCEA/RCEA 在售体系 + LCE/MCE/RCE 老版（含外驱伺服型/外驱485型/内置驱动器型三种形态）
- [[entity-电爪]] — 电爪产品线：四大家族（平行/旋转/关节/三指对心）+ 485≤4台规则 + 抱闸85%保持 + RGIC背隙口径 ⭐ 新建
- [[entity-驱动器]] — 驱动器产品线（限定：原生 ECAT/CIA402 伺服驱动器；8 款完整谱系；SAC-N2 退市中→SAC-NP2；研控第三方选配记录）

### 概念 (1)
- [[concept-开环力控]] — 两段位置+电流限制实现力控，含标定公式 y=kx+b

### 主题 / 案例 (0)

### 手册编译页 (14)
- [[manual-sac-n2-driver-debug-sop]] — SAC-N2 驱动器调试软件操作及故障分析（V1.1, 29页）
- [[manual-sac-n2-motor-tuning]] — SAC-N2 电机整定参考（参数/编码器/刚性表/寻相/三环整定/3案例）
- [[manual-sac-n2-faq]] — SAC-N2 FAQ（12条高频故障问答：使能/编码器/运动控制/供电/总线通信）
- [[manual-sac-n2-ethercat-application]] — SAC-N2 EtherCAT 应用手册（总线通讯/CIA402状态机/6种控制模式/35种回零/探针/7种PLC适配）
- [[manual-dh-电缸选型手册]] — DH 电缸选型手册 CN-2025.10（MCEA/RCEA 四型号+命名规则+8款驱动器谱系+ECAT盒子+布线规范）⭐
- [[manual-sac-n2-first-power-on-sop]] — SAC-N2 初次上电 SOP（连接上位机/参数备份导入/电机确认/寻相/IO配置/屏蔽轴 6 步）
- [[manual-dh-音圈选型手册]] — DH 音圈选型手册 CN-3.3.2025.10（在售5系列全参数+VLAR退市/更名记录+驱动器线缆匹配+研控第三方）⭐
- [[manual-dh-电爪选型手册]] — DH 电爪选型手册 CN-2025.08（四大家族+定货码+485≤4台+通讯转换模块+灵巧手）⭐
- [[manual-sac-usb-upgrade]] — SAC 系列驱动器 USB 固件升级指导（7步流程）⭐ 新增
- [[manual-dh-mcea-电缸操作手册]] — MCEA 电缸操作手册 V4.0（内置驱动型，两套 Modbus 协议+完整报警表）⭐ 新增
- [[manual-dh-pgia-pgea-电爪操作手册]] — PGIA/PGEA 电爪操作手册 V3.3（Modbus 寄存器+NPN/PNP IO+掉落状态）⭐ 新增
- [[manual-sac-n2-xml-update]] — SAC-N2 XML 文件更新指导（0x13 错误烧录 ESI 流程）⭐ 新增
- [[manual-sac-xml-modify]] — SAC XML 文件修改方法（Slot 模块 + PDO 列表增删）⭐ 新增
- [[manual-sac-np2-param-import-export]] — SAC-NP2 驱动参数导入导出 SOP（轴1=Z/轴2=R）⭐ 新增

### 元数据 (1)
- [[corrections]] — 纠正记录（C001-C031，编译与使用过程中被纠正的点）

## 按产品线

### 音圈电机 (6 手册)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
- [[manual-dh-音圈选型手册]] ⭐

### 电缸 (2 手册, 1 实体页)
- [[manual-dh-电缸选型手册]] ⭐
- [[manual-dh-mcea-电缸操作手册]] ⭐ 新增
- [[entity-电缸]] — MCEA/RCEA 在售体系 + 三种驱动器形态 + ECAT 盒子正式型号

### 电爪 (2 手册, 1 实体页)
- [[manual-dh-电爪选型手册]] ⭐
- [[manual-dh-pgia-pgea-电爪操作手册]] ⭐ 新增
- [[entity-电爪]] — 四大家族 + 售后要点速查

### 驱动器 (11 手册, 跨线)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
- [[manual-sac-usb-upgrade]] ⭐
- [[manual-sac-n2-xml-update]] ⭐ 新增
- [[manual-sac-xml-modify]] ⭐ 新增
- [[manual-sac-np2-param-import-export]] ⭐ 新增
- [[manual-dh-电缸选型手册]]（驱动器完整谱系表）
- [[manual-dh-音圈选型手册]]（驱动器选配表 + 研控第三方）

### 通用 (0)

## 编译进度

- [x] 大寰电机调试SOP_V1.1.pdf → [[manual-sac-n2-driver-debug-sop]]
- [x] SAC-N2 电机整定参考手册_20260818.md → [[manual-sac-n2-motor-tuning]]
- [x] SAC-N2 FAQ_20260818.md → [[manual-sac-n2-faq]]
- [x] SAC-N2 EtherCAT应用手册_20260818.md → [[manual-sac-n2-ethercat-application]]
- [x] DH_电缸选型手册_中文版_1029.pdf → [[manual-dh-电缸选型手册]]（Fly 指定优先编译，建立产品线全貌）
- [x] SAC-N2驱动器初次上电SOP_20260415.pdf → [[manual-sac-n2-first-power-on-sop]]
- [x] DH_音圈选型手册_中文版_CN2510.pdf → [[manual-dh-音圈选型手册]]（Fly 新投喂，指定优先）
- [x] DH_电爪选型手册-CN-电子版-2508.pdf → [[manual-dh-电爪选型手册]]（Fly 新投喂，指定优先）
- [x] SAC系列驱动器USB升级操作指导文档_20260818.md → [[manual-sac-usb-upgrade]]
- [x] 大寰MCEA电缸操作手册_V4.0.pdf → [[manual-dh-mcea-电缸操作手册]]
- [x] PGIA.PGEA系列电爪操作手册V3.3.pdf → [[manual-dh-pgia-pgea-电爪操作手册]]
- [x] SAC-N2 XML文件更新指导手册_20260818.md → [[manual-sac-n2-xml-update]]
- [x] SAC XML文件修改方法_20260818.md → [[manual-sac-xml-modify]]
- [x] 大寰电机SAC-NP2驱动参数导入导出SOP_20260408.pdf → [[manual-sac-np2-param-import-export]]
- [ ] 其余 27 件待编译

## 已确认的疑点（原编译不确定点，Fly 已逐条确认）

1. 音圈：**DLA 已退市（出货量很少）**（C019）
2. 音圈：线缆表 "SAC-N2H" 为文档错误，**应为 NP2**（C020）
3. 音圈：DLARA-13-25/13-45、VLA-25-10 为**客户定制特殊尺寸（非标品）**，仅厚度区别、使用与标品一样（C021）
4. 音圈：末位 A 迭代年份口径**以音圈手册为准 = 2025.06**（C022）
5. 电爪：**PGHL-400-80 为 400N 档主力机型**（C023）
6. MCEA 电缸：报警表 = **内驱&485外驱版本**；SAC-N2 伺服驱动器故障码表是另一套（C024）
7. MCEA 电缸：两套 Modbus 协议**所有版本并存，推荐 0x1600**（C025）
8. MCEA 电缸：橙色线 = **通讯线负**（手册"正"为笔误）（C026）
9. MCEA 电缸：报警码以 **HEX 列**为准（0x80/0x82…），ALM_DO 列不参考（C027）
10. 电爪：**PGEA 基本内置驱动**，仅 PGEA-2/15-10 外置；外置款上电堵转根因=**未配对**（C028）
11. XML：**版本持续更新但基础内容不变，各版本基本通用**（C029）
12. XML：**Force Control = 0x103**（原文第二处"0x102"为笔误）（C030）
13. XML：对象定义与对象字典 xlsx **同一个用处**，可互相参照（C031）

> 当前无待确认疑点。后续编译中发现新疑点将列在此处并标注"待确认"。

## 待 Fly 确认的疑点（本轮编译新发现，未采信推断）

> 当前无待确认疑点。上一轮 3 个疑点已由 Fly 逐条确认（C029-C031），见下方"已确认的疑点"。
