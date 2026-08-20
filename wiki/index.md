# Wiki 索引

> 总页面数: 59 ｜ 已编译资料: 51/56 ｜ 最后更新: 2026-08-20
> 覆盖产品线: 音圈电机, 电缸, 电爪, 驱动器

## 按类型

### 实体 (4)
- [[entity-音圈电机]] — 音圈电机产品线：在售 VLA/DLARA/DLSRA/DLE/VLM·VLMF；VLAR 退市、DLAR/DLSR 更名记录；ZR默认NP2/单Z默认NP1
- [[entity-电缸]] — 电缸产品线：MCEA/RCEA 在售体系 + LCE/MCE/RCE 老版（含外驱伺服型/外驱485型/内置驱动器型三种形态）
- [[entity-电爪]] — 电爪产品线：四大家族（平行/旋转/关节/三指对心）+ 485≤4台规则 + 抱闸85%保持 + RGIC背隙口径 ⭐ 新建
- [[entity-驱动器]] — 驱动器产品线（限定：原生 ECAT/CIA402 伺服驱动器；8 款完整谱系；SAC-N2 退市中→SAC-NP2；研控第三方选配记录）

### 概念 (1)
- [[concept-开环力控]] — 两段位置+电流限制实现力控，含标定公式 y=kx+b

### 主题 / 案例 (7)
- [[topic-售后排查引导清单]] — 微信式追问排查模板（定位产品线→看灯→分支追问→高频根因速查）⭐ 新增
- [[topic-电缸电爪基础考试题库]] — 53 题新人 FAE 培训考核题库（初始化/指示灯/Modbus/IO/推压/报警/选型 + 记忆卡片）⭐ 新增
- [[topic-华东工单案例库]] — 华东工单案例库总索引（2771 条技术服务&高价值工单，2026-01~08，含【禁】类）⭐ 新增
- [[topic-华东工单-电爪]] — 电爪工单 1148 条（按问题类型分组）⭐ 新增
- [[topic-华东工单-电缸]] — 电缸工单 812 条（按问题类型分组）⭐ 新增
- [[topic-华东工单-音圈直驱]] — 音圈/直驱工单 648 条（按问题类型分组）⭐ 新增
- [[topic-华东工单-驱动及其他]] — 驱动/通讯盒/柔性线/灵巧手等工单 163 条（按问题类型分组）⭐ 新增

### 性能测试 (3) ⭐ 新增
- [[topic-性能测试-直驱]] — DLAR-20-40-H1 节拍测试（2g/3g/5g 加速度下的规划+整定时间）
- [[topic-性能测试-电缸]] — MCE-3G&3WG-02-50 测试数据与结论（行程/电气/16 条极限工况结论）
- [[topic-性能测试-电爪]] — RGI-100-14 旋转力测试（0.5~1.5N·m 力-电流线性标定）

### FAQ 速查 (5, 噗元项目) ⭐ 新增
- [[faq-电爪]] — 78 条电爪 FAQ（初始化/指示灯/Modbus/IO/夹持掉落/硬件）
- [[faq-电缸]] — 50 条电缸 FAQ（推压段/初始化/回零/报警/IO/通讯）
- [[faq-直驱]] — 46 条直驱 FAQ（音圈/直线电机 + SAC-N2 总线：寻相/回零/力控/软着陆）
- [[faq-驱动器]] — 10 条驱动器 FAQ（SAC-N2 规格 8 条 + SAC-N 2 条）
- [[faq-通讯盒]] — 4 条通讯盒 FAQ（固高扫描/XML-BIN-CFG 含义）

### 案例库 (仅已闭环, 5 条初始)
- [[cases/00-案例库索引]] — 案例库索引 + 频次统计汇总表 ⭐ 新增
- [[cases/案例-001-PGEA上电堵转未配对]] — 上电堵转=电爪与驱动盒未配对（C028）
- [[cases/案例-002-位置丢失抱闸时间]] — 位置丢失/夹持状态消失=抱闸时间参数（C036）
- [[cases/案例-003-垂直寻相失败ABZ]] — 垂直重载寻相失败=ABZ 每次上电寻相（C018）
- [[cases/案例-004-RGIC旋转背隙]] — 旋转位置不准=RGIC 齿轮背隙（C033）
- [[cases/案例-005-回零堵转反向距离设0]] — 回零堵转=-1 回零反向距离设 0（C038）

### 手册编译页 (33)
- [[manual-sac-n2-driver-debug-sop]] — SAC-N2 驱动器调试软件操作及故障分析（V1.1, 29页）
- [[manual-sac-n2-motor-tuning]] — SAC-N2 电机整定参考（参数/编码器/刚性表/寻相/三环整定/3案例）
- [[manual-sac-n2-faq]] — SAC-N2 FAQ（12条高频故障问答：使能/编码器/运动控制/供电/总线通信）
- [[manual-sac-n2-ethercat-application]] — SAC-N2 EtherCAT 应用手册（总线通讯/CIA402状态机/6种控制模式/35种回零/探针/7种PLC适配）
- [[manual-dh-电缸选型手册]] — DH 电缸选型手册 CN-2025.10（MCEA/RCEA 四型号+命名规则+8款驱动器谱系+ECAT盒子+布线规范）⭐
- [[manual-sac-n2-first-power-on-sop]] — SAC-N2 初次上电 SOP（连接上位机/参数备份导入/电机确认/寻相/IO配置/屏蔽轴 6 步）
- [[manual-dh-音圈选型手册]] — DH 音圈选型手册 CN-3.3.2025.10（在售5系列全参数+VLAR退市/更名记录+驱动器线缆匹配+研控第三方）⭐
- [[manual-dh-电爪选型手册]] — DH 电爪选型手册 CN-2025.08（四大家族+定货码+485≤4台+通讯转换模块+灵巧手）⭐
- [[manual-sac-usb-upgrade]] — SAC 系列驱动器 USB 固件升级指导（7步流程）⭐
- [[manual-dh-mcea-电缸操作手册]] — MCEA 电缸操作手册 V4.0（内置驱动型，两套 Modbus 协议+完整报警表）⭐
- [[manual-dh-pgia-pgea-电爪操作手册]] — PGIA/PGEA 电爪操作手册 V3.3（Modbus 寄存器+NPN/PNP IO+掉落状态）⭐
- [[manual-sac-n2-xml-update]] — SAC-N2 XML 文件更新指导（0x13 错误烧录 ESI 流程）⭐
- [[manual-sac-xml-modify]] — SAC XML 文件修改方法（Slot 模块 + PDO 列表增删）⭐
- [[manual-sac-np2-param-import-export]] — SAC-NP2 驱动参数导入导出 SOP（轴1=Z/轴2=R）⭐
- [[manual-sac-nf2-force-control]] — SAC-NF2 柔性力控使用手册（MCK 模型 + 对象字典 + 调参）⭐
- [[manual-dh-电缸报警代码解析]] — DH 电缸故障码表（内驱版，HEX 列）⭐
- [[manual-sac-np2-product]] — SAC-NP2 双轴驱动器产品操作手册（规格/接口/数码管/错误码/寻相）⭐
- [[manual-dh-电爪抱闸时间修改]] — 电爪抱闸触发时间修改（0x1108 组）⭐
- [[manual-dh-pgls-电爪校准偏置值]] — PGLS 电爪零电角/绝对值/偏置校准（联赢激光）⭐
- [[manual-dh-电缸软重启]] — 电缸软重启 SOP（替代物理断电）⭐
- [[manual-dh-485寄存器表总览]] — 485 寄存器操作地址速查（电缸+电爪通用，DHGripperUI）⭐
- [[manual-dh-ecat盒子固件升级]] — ECAT 盒子固件升级（ESI/Bin/CFG）⭐ 新增
- [[manual-dh-夹爪固件升级]] — RGD/RGI/RGIC 夹爪固件更新 + 校准 ⭐ 新增
- [[manual-dh-基恩士适配ecat盒子]] — 基恩士 KV8000/7500 适配 ECAT 盒子 SOP ⭐ 新增
- [[manual-dh-m2e-b1-4通讯盒使用说明]] — M2E-B1-4 EtherCAT 通讯盒使用说明（5.x）⭐ 新增
- [[manual-xjc-608t-操作说明SOP]] — XJC-608T-F 压力显示器操作说明（力控标定硬件）⭐ 新增
- [[manual-dh-控制卡适配技术样本]] — 控制卡适配技术样本总览（7样本合并：凌臣/汇川/固高 × SAC-N2/NP4/N1）⭐ 新增
- [[manual-dh-旋转零点校准]] — 电爪旋转轴零点校准（0x0500 写 0）⭐ 新增
- [[manual-dh-电气篇应用指导]] — 产品应用指导-电气篇（供电/接地/末端安装）⭐ 新增
- [[manual-鑫精诚力显示器参数修改说明]] — 力显示器参数修改（小数点/砝码/模拟量）⭐ 新增
- [[manual-dh-三菱卓岚通讯配置]] — 三菱 PLC + 卓岚网关简单 CPU 通讯配置 ⭐ 新增
- [[manual-sac-对象字典]] — SAC 双轴驱动器对象字典 V1.7.2（预设 PDO 三模块）⭐ 新增
- [[manual-sac-伺服驱动器报警代码表]] — SAC 伺服驱动器报警代码表（0x603F 总线代码，闭环 C003）⭐ 新增

### 元数据 (1)
- [[corrections]] — 纠正记录（C001-C040，编译与使用过程中被纠正的点）

## 按产品线

### 音圈电机 (7 手册)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
- [[manual-dh-音圈选型手册]] ⭐
- [[manual-dh-控制卡适配技术样本]] ⭐ 新增

### 电缸 (6 手册, 1 实体页)
- [[manual-dh-电缸选型手册]] ⭐
- [[manual-dh-mcea-电缸操作手册]] ⭐
- [[manual-dh-电缸报警代码解析]] ⭐
- [[manual-dh-电缸软重启]] ⭐
- [[manual-dh-485寄存器表总览]] ⭐
- [[manual-dh-m2e-b1-4通讯盒使用说明]] ⭐ 新增
- [[entity-电缸]] — MCEA/RCEA 在售体系 + 三种驱动器形态 + ECAT 盒子正式型号

### 电爪 (6 手册, 1 实体页)
- [[manual-dh-电爪选型手册]] ⭐
- [[manual-dh-pgia-pgea-电爪操作手册]] ⭐
- [[manual-dh-电爪抱闸时间修改]] ⭐
- [[manual-dh-pgls-电爪校准偏置值]] ⭐
- [[manual-dh-夹爪固件升级]] ⭐ 新增
- [[manual-dh-485寄存器表总览]] ⭐
- [[entity-电爪]] — 四大家族 + 售后要点速查

### 驱动器 (14 手册, 跨线)
- [[manual-sac-n2-driver-debug-sop]]
- [[manual-sac-n2-motor-tuning]]
- [[manual-sac-n2-faq]]
- [[manual-sac-n2-ethercat-application]]
- [[manual-sac-n2-first-power-on-sop]]
- [[manual-sac-usb-upgrade]] ⭐
- [[manual-sac-n2-xml-update]] ⭐
- [[manual-sac-xml-modify]] ⭐
- [[manual-sac-np2-param-import-export]] ⭐
- [[manual-sac-nf2-force-control]] ⭐ 新增
- [[manual-sac-np2-product]] ⭐ 新增
- [[manual-dh-电缸选型手册]]（驱动器完整谱系表）
- [[manual-dh-音圈选型手册]]（驱动器选配表 + 研控第三方）
- [[manual-dh-电缸报警代码解析]]（电缸故障码，SAC 伺服驱动器故障码见 NP2 产品手册）

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
- [x] SAC-NF2-柔性力控使用手册_v20260305.docx → [[manual-sac-nf2-force-control]]
- [x] 电缸报警代码解析_20241111.xlsx → [[manual-dh-电缸报警代码解析]]（内驱电缸故障码表，C032）
- [x] SAC-NP2 EtherCAT型双轴驱动器-产品操作手册 → [[manual-sac-np2-product]]
- [x] 大寰电爪更改抱闸时间SOP_20240820.docx → [[manual-dh-电爪抱闸时间修改]]
- [x] PGLS电爪校准偏置值SOP-联赢激光_20260602.docx → [[manual-dh-pgls-电爪校准偏置值]]
- [x] 大寰电缸软重启SOP_v20240819.docx → [[manual-dh-电缸软重启]]
- [x] 4 份寄存器表（电爪/一体式电缸/分体式电缸/PGLS）→ [[manual-dh-485寄存器表总览]]
- [x] ECAT盒子固件升级SOP（含ESI与CFG + 仅ESI与CFG）→ [[manual-dh-ecat盒子固件升级]]
- [x] RGD，RGI，RGIC夹爪固件升级手册 → [[manual-dh-夹爪固件升级]]
- [x] 基恩士KV8000&7500PLC适配DHetherCAT盒子SOP → [[manual-dh-基恩士适配ecat盒子]]
- [x] M2E-B1-4+V5.x+使用说明书 → [[manual-dh-m2e-b1-4通讯盒使用说明]]
- [x] XJC-608T-F操作说明SOP → [[manual-xjc-608t-操作说明SOP]]
- [x] 7 个控制卡适配技术样本 → [[manual-dh-控制卡适配技术样本]]
- [x] 旋转零点校准_20240524.docx → [[manual-dh-旋转零点校准]]
- [x] 产品应用指导手册-电气篇v20241029.pdf → [[manual-dh-电气篇应用指导]]
- [x] 鑫精诚力显示器参数修改说明_20260416.pdf → [[manual-鑫精诚力显示器参数修改说明]]
- [x] 三菱-卓岚-简单CPU通讯配置SOP_v20141119.docx → [[manual-dh-三菱卓岚通讯配置]]
- [x] SAC_2Axis_V1.7.2对象字典.xlsx → [[manual-sac-对象字典]]
- [x] 两段位置限制电流实现力控_20230915.pdf → 并入 [[concept-开环力控]]
- [x] SAC伺服驱动器报警代码表_20260819.xlsx → [[manual-sac-伺服驱动器报警代码表]]（闭环 C003）
- [x] 噗元FAQ_20250424.xlsx → [[faq-电爪]] [[faq-电缸]] [[faq-直驱]] [[faq-驱动器]] [[faq-通讯盒]]（188 条 FAQ 按产品线拆 5 页）⭐ 新增
- [x] DLAR-20-40-H1节拍测试 → [[topic-性能测试-直驱]] ⭐ 新增
- [x] MCE-3G&3WG-02-50测试数据与结论 → [[topic-性能测试-电缸]] ⭐ 新增
- [x] RGI-100-14旋转力测试 → [[topic-性能测试-电爪]] ⭐ 新增
- [x] 电缸电爪基础考试_20260819.docx → [[topic-电缸电爪基础考试题库]]（53 题新人培训考核，含答案）⭐ 新增
- [x] 华东工单提取仅技术服务&高价值FAQ_20260820.xlsx → [[topic-华东工单案例库]]（2771 条工单按产品线拆 4 子页 + 总索引，含【禁】类，Fly 决策全部纳入）⭐ 新增
- [ ] 其余 5 件待编译（均为视频/演示 mp4/pptx，不适合编译成文本页）

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
14. 电缸报警代码解析 xlsx：**也是内驱电缸故障码表**，非 C003 待补的伺服驱动器表（C032）
15. 电爪结构：**平行爪单电机（正转夹持反转张开）vs 旋转爪双电机耦合插补**；主流双芯片（C033）
16. **SAC-NF（早期 485 闭环力控电缸驱动器）≠ SAC-NF2（伺服驱动器）**，逻辑完全不同（C034）
17. **485 系列电缸电爪寄存器大量相同**，电缸操作在电爪上通用；共用 DHGripperUI（C035）
18. **抱闸时间参数**：防长时夹持大电流过热；旧固件 bug 开闭抱闸丢编码器圈数→位置丢失/夹持状态消失（C036）
19. **PGHL/PGLS 用「电缸方案」**：功率大、夹持电池，寄存器单位与 0x1600 控制字同电缸；其他电爪不支持控制字（C037）
20. **回零方式 -1 = 碰挡板后反向走固定脉冲距离**（≠ -3 碰挡板反向找 Z 脉冲）；-1 反向距离参数设 0 会堵转（C038）

> 当前无待确认疑点。后续编译中发现新疑点将列在此处并标注"待确认"。

## 待 Fly 确认的疑点（本轮编译新发现，未采信推断）

> 当前无待确认疑点。
