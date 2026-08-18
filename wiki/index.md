# Wiki 索引

> 总页面数: 13 ｜ 已编译资料: 8/41 ｜ 最后更新: 2026-08-18
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

### 手册编译页 (8)
- [[manual-sac-n2-driver-debug-sop]] — SAC-N2 驱动器调试软件操作及故障分析（V1.1, 29页）
- [[manual-sac-n2-motor-tuning]] — SAC-N2 电机整定参考（参数/编码器/刚性表/寻相/三环整定/3案例）
- [[manual-sac-n2-faq]] — SAC-N2 FAQ（12条高频故障问答：使能/编码器/运动控制/供电/总线通信）
- [[manual-sac-n2-ethercat-application]] — SAC-N2 EtherCAT 应用手册（总线通讯/CIA402状态机/6种控制模式/35种回零/探针/7种PLC适配）
- [[manual-dh-电缸选型手册]] — DH 电缸选型手册 CN-2025.10（MCEA/RCEA 四型号+命名规则+8款驱动器谱系+ECAT盒子+布线规范）⭐
- [[manual-sac-n2-first-power-on-sop]] — SAC-N2 初次上电 SOP（连接上位机/参数备份导入/电机确认/寻相/IO配置/屏蔽轴 6 步）
- [[manual-dh-音圈选型手册]] — DH 音圈选型手册 CN-3.3.2025.10（在售5系列全参数+VLAR退市/更名记录+驱动器线缆匹配+研控第三方）⭐
- [[manual-dh-电爪选型手册]] — DH 电爪选型手册 CN-2025.08（四大家族+定货码+485≤4台+通讯转换模块+灵巧手）⭐

### 元数据 (1)
- [[corrections]] — 纠正记录（C001-C023，编译与使用过程中被纠正的点）

## 按产品线

### 音圈电机 (6 手册)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
- [[manual-dh-音圈选型手册]] ⭐

### 电缸 (1 手册, 1 实体页)
- [[manual-dh-电缸选型手册]] ⭐
- [[entity-电缸]] — MCEA/RCEA 在售体系 + 三种驱动器形态 + ECAT 盒子正式型号

### 电爪 (1 手册, 1 实体页)
- [[manual-dh-电爪选型手册]] ⭐
- [[entity-电爪]] — 四大家族 + 售后要点速查

### 驱动器 (7 手册, 跨线)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
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
- [ ] 其余 33 件待编译（下一本：SAC 系列 USB 升级操作指导）

## 已确认的疑点（原编译不确定点，Fly 已逐条确认）

1. 音圈：**DLA 已退市（出货量很少）**（C019）
2. 音圈：线缆表 "SAC-N2H" 为文档错误，**应为 NP2**（C020）
3. 音圈：DLARA-13-25/13-45、VLA-25-10 为**客户定制特殊尺寸（非标品）**，仅厚度区别、使用与标品一样（C021）
4. 音圈：末位 A 迭代年份口径**以音圈手册为准 = 2025.06**（C022）
5. 电爪：**PGHL-400-80 为 400N 档主力机型**（C023）

> 当前无待确认疑点。后续编译中发现新疑点将列在此处并标注"待确认"。
