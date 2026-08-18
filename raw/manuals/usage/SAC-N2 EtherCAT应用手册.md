# SAC-N2 EtherCAT应用手册

# 封面

# 前言

首先感谢您使用 DH Robotics SAC-N2 双轴驱动器！

DH Robotics SAC-N2 双轴驱动器（以下简称 SAC-N2），是由大寰机器人最新推出的一款通用双轴伺服驱动器，其主要应用与机器人、光伏半导体制造设备、医疗设备、机床、物流设备、仪表测量等高精密工业自动化行业。

本手册仅针对 DH Robotics SAC-N2 双轴驱动器 EtherCAT相关功能进行叙述。对于初次使用的用户，请认真阅读本手册，若还对 EtherCAT使用有疑问，请咨询我公司的技术人员以获得帮助。

**本说明书使用以下使用者参考：**

*   伺服系统设计者
    
*   设备调试人员
    
*   维护、检查人员
    
*   技术支持工程师
    

本公司保留对产品不断改进的权利，恕不另行通知。

# 修订记录

| **时间** | **修订记录** |
| --- | --- |
| 2023/05/31 | *   第一次发布 |
| 2023/07/06 | *   增加基恩士和汇川PLC的通讯案例<br>    <br>*   增加EtherCAT操作时上位机的配置<br>    <br>*   修改了网口灯定义 |

# 目录

# 第一章 硬件配置

## 1.1 接口定义

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2608f6d1-d2c0-4fe7-93d3-6fd65e66a9a3.png)

## 1.2 驱动器接线

![lQDPJx-rFZErdEbNBLLNB16wvP74dcEW858EnBXQh0D0AA_1886_1202.jpg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/4252ca9f-ed99-4268-94e6-03f6cd4da2fb.jpg)

# 第二章 总线通讯

## 2.1 EtherCAT简介

EtherCAT 是一种实时工业以太网技术，它充分利用了以太网的 “全双工”特性。 使用主从模式介质访问控制(MAC)，主站发送以太网帧给各从站，从站从数据帧中抽取数据或将数据插入数据帧。主站使用标准的以太网接口卡，从站使用专门的 EtherCAT 从站控制器 ESC ( EtherCAT Slave Controller)。EtherCAT 物理层使用标准的以太网物理层器件。

从以太网的角度来看，一个 EtherCAT网段就是一个以太网设备，它接收和发送标准的 ISO/IEC8802\-3 以太网数据帧。但是，这种以太网设备并不局限于一个以太网控制器及相应的微处理器，它可由多个EtherCAT从站组成，如下图所示。 这些从站可以直接处理接收的报文，并从报文中提取或插入相关的用户数据，然后将该报文传输到下一个EtherCAT从站。最后一个EtherCAT从站发回经过完全处理的报文，并由第一个从站作为响应报文将其发送给控制单元。

![lQDPJx6RJBFKFEbNA23NB8ewJqZlXZV7HdoEnBXQiMAMAA_1991_877.jpg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/010f3fbf-8623-41d2-9d3b-7c3b70de57a1.jpg)

## 2.2 节点参考模型

EtherCAT是使用开放系统互连基本参考模型(OSI)来描述的。OSI模型为通信标准提供了一种分层的方法，从而可以独立地开发和修改各层。EtherCAT规范从上到下定义了一个完整的OSI堆栈的功能，并为堆栈的用户定义了一些功能。OSI中间层(第3 -6层)的功能被合并到EtherCAT数据链路层或EtherCAT应用层。同样，EtherCAT应用层也可以提供现场总线应用层用户共有的特性，以简化用户操作，如图下图所示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5cb9045f-71fb-4eb7-acce-f1b5c006939b.png?x-oss-process=image/crop,x_0,y_0,w_1126,h_717/ignore-error,1)

CANopen最初是为CAN ( Control Aera Netwαk)总线控制系统所开发的应用层协议。

EtherCAT协议在应用层支持CANopen协议，并作了相应的扩充。主要功能有:

*   使用邮箱通信访问CANopen对象字典及其对象，实现网络初始化；
    
*   使用CANopen应急对象和可变的事件驱动PDO消息，实现网络管理 ;
    
*   使用对象字典映射过程数据，周期性传输指令数据和状态数据。
    

## 2.3 EtherCAT规格

| **项目** | **规格** |
| --- | --- |
| 适用标准 | IEC 61158 Type12<br>IEC 61800-7 CiA402 Drive Profile |
| 传输协议 | 100BASE-TX（IEEE802.3） |
| 总线接口 | EtherCAT Signal IN 接口10<br>Ether CAT Signal OUT 接口11 |
| 缆线 | 5 类双绞线 |
| SM通道 | SM0：输出邮箱<br>SM1：输入有效<br>SM2：输出过程数据<br>SM3：输入过程数据 |
| FMMU单元 | FMMU0：映射到过程数据（RxPDO）输出区域<br>FMMU1：映射到过程数据（TxPDO）输出区域<br>FMMU2：映射到邮箱状态 |
| PDO数据 | 动态PDO映射 |
| Mailbox（COE） | 紧急时间，SDO请求，SDO响应 |
| 分布时钟（DC） | Free Run模式和DC模式 同步周期最低500us |

## 2.3 LED指示灯状态

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/624331a0-e862-4cc1-99e8-43d11e9030d4.png)

| **状态** | **说明** |
| --- | --- |
| ACT | 长灭，无定义 |
| LINK常亮 | 链路上有连接，但没有数据交互 |
| LINK熄灭 | 物理层上没有连接，EtherCAT未启动 |
| LINK闪烁 | 正在进行数据交互 |

## 2.4 对象字典

SAC-N2伺服具有4个可配置的PDO，包括2个RxPDO（1600H，1610H）和2个TxPDO（1A00H，1A10H）。轴1分配1600H和1A00H，轴2分配1610H和1A10H，并且提供3组可用配置（csp，csv，cst），可对RxPDO和TxPDO进行修改，说明如下：

**RxPDO：**

| **索引号** | **对象类型** | **默认值** |
| --- | --- | --- |
| 1600H / 1610H | \- | \- |
| 00 | UINT8 | 3 |
| 01 | UINT16 | 控制字 Control Word 6040H |
| 02(CSP) | UINT32 | 目标位置 Target Position 607AH |
| 02(CSV) | UINT32 | 目标速度 Target Velocity 60FFH |
| 02(CST) | UINT32 | 目标力矩 Target Torque 6071H |
| 03 | UINT8 | 操作模式 Modes Of Operation 6060H |

**TxPDO：**

| **索引号** | **对象类型** | **默认值** |
| --- | --- | --- |
| 1A00H / 1A10H | \- | \- |
| 00 | UINT8 | 3 |
| 01 | UINT16 | 状态字 Status Word 6041H |
| 02(CSP) | UINT32 | 位置反馈 Actual Position 6064H |
| 02(CSV) | UINT32 | 速度反馈 Actual Velocity 606CH |
| 02(CST) | UINT32 | 力矩反馈 Actual Torque 6077H |
| 03 | UINT8 | 工作模式反馈 Modes Of Operation Display 6061H |

## 2.5 EtherCAT从站信息ESI

从站设备描述文件ESI（EtherCAT Slave Information）是EtherCAT从站设备的配置文件，文件为XML格式。XML文件编写好后，通过主站程序下载到从站设备的EEPROM中，通过I2C总线与EtherCAT从站芯片内部的寄存器进行数据交换，实现配置信息的读取。从站设备描述文件的主要功能是描述EtherCAT从站的配置信息，主要包含以下两个部分内容：EtherCAT从站制造商信息和therCAT从站描述信息。从站设备描述文件的结构图如图所示：

![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/R9Az1mV12sNZakB8/a20c3535637e4b75a8110324940afb161788.png)

## 2.6 EtherCAT状态机

ESM(EtherCAT State Machine)负责协调主站和从站应用程序在初始化和运行时的状态关系及转换，转换过程如下图所示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2cbf50c5-e21a-4177-a4b5-92db9c847c9b.png)

| **状态或状态转换** | **操作说明** |
| --- | --- |
| 初始化<br>(Init, I) | *   没有邮箱通讯<br>    <br>*   没有过程数据通讯 |
| 初始化->预运行<br>(Init to Pre-OP, IP) | *   主站配置链路层地址，启动邮箱通讯<br>    <br>*   主站初始化DC同步时钟<br>    <br>*   主站请求向Pre-OP状态转换<br>    <br>*   主站设置AL控制寄存器<br>    <br>*   从站检查邮箱是否初始化正确 |
| 预运行<br>(Pre-Operation, P) | *   邮箱通讯被激活<br>    <br>*   不能进行过程数据通讯 |
| 预运行->安全运行<br>(Pre-OP to Safe-OP, PS) | *   主站为过程数据配置同步管理器（SM）和FMMU通道<br>    <br>*   主站通过SDO对从站进行PDO数据映射及SM PDO参数设置<br>    <br>*   主站请求向Safe-OP状态转换<br>    <br>*   从站检查负责PDO数据的SM配置是否正确，如果主站发出启动同步请求，检查分布式时钟的设置是否正确。 |
| 安全运行<br>(Safe-Operation, S) | *   从站应用程序将传送实际输入数据，不对输出进行操作，输出被设置为安全状态 |
| 安全运行->运行<br>(Safe-OP to OP, SO) | *   主站发送有效的输出数据<br>    <br>*   主站请求向OP状态转换 |
| 运行<br>(Operational, O) | *   可进行过程数据通讯 |

## 2.7 EtherCAT通讯模式

在实际自动化控制系统中，应用程序之间通常有两种数据交换形式：时间关键（time-critical）和非时间关键（non-time\-critical）。 时间关键表示特定的动作必须在确定的时间窗口内完成。 如果不能在要求的时间窗口内完成通信，则有可能引起控制失效。时间关键的数据通常周期性发送，称为周期性过程数据通信。非时间关键数据可以非周期性发送，在EtheCAT 中采用非周期性邮箱（mailbox）数据通信。

### 2.7.1 周期性过程数据通讯

**Free Run模式：**

在Free Run模式下，本地控制周期由一个本地定时器中断产生。在一个周期时间内完成数据的拷贝，处理和数据上传，各个从站的本地定时器节拍并不同步，所以在Free Run模式下，从站的动作也是不同步的。

![freeRun.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b365a588-3763-415b-95f4-d5465cb6d188.jpeg)

**SM模式：**

本地周期在发生数据输入或输出事件的时候触发。主站可以将过程数据帧的发送周期写给从站，从站可以检查是否支持这个周期时间或对周期时间进行本地优化。从站可以选择支持这个功能。通常同步于数据输出事件，如果从站只有输入数据，则同步于数据输入事件 。

![SM2.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/28fd1217-f64a-4cc3-8f19-2c813742670e.jpeg)

**DC模式：**

本地周期由SYNC事件触发，主站必须在SYNC事件之前完成数据帧的发送。 此时要求主站时钟也要同步于参考时钟。

为了进一步优化从站同步性能 ，从站应该在数据收发事件发生时从接收到的过程数据帧复制输出数据，然后后等待SYNC信号到达后继续本地操作。数据帧必须比SYNC信号到达，从站在SYNC事件之前已经完成数据交换和控制计算，接收SYNC信号后可以马上执行输出操作，从而进一步提高同步性能。

![DC.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/d546c148-52a4-4f1a-a6b4-369982a9ffba.jpeg)

### 2.7.2 非周期性邮箱数据通讯

EtherCAT协议中非周期性数据通信称为邮箱数据通信，它可以双向进行，主站到l从

站和从站到主站。它支持全双工、两个方向独立通信和多用户协议。从站到从站的通信由

主站作为路由器来管理。邮箱通信数据头中包括一个地址域 ， 使主站可以重寄邮箱数据。

邮箱数据通信是实现参数交换的标准方式，如果需要配置周期性过程数据通信或需要其他

非周期性服务时需要使用邮箱数据通信。

# 第三章 通讯案例

双轴驱动器支持EtherCAT控制和USB控制，USB控制主要用于上位机调试，运行位置，速度，转矩控制。当客户使用EtherCAT控制时，需要先通过上位机参数表的0x2002.01参数，设置为EtherCAT总线控制，保存参数后重启驱动器，然后才能通过EtherCAT控制，配置如下图所示。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/08690f47-6404-4efc-87e9-b90345a2dd5a.png)

## 3.1适配倍福TwinCAT3

### 3.1.1 点动，定位测试

新建一个TwinCAT3工程，将xml文件放入指定目录中 C:\TwinCAT\3.1\Config\Io\EtherCAT

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/cdeb9374-659f-4879-b043-e440b5bea134.png)

右键IO->Devices，选择下拉框中的Scan，可以观察到搜索到从站设备，点击OK完成组态。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/c79b54fc-2ade-4398-a308-df1d7fe30730.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/11ec17f9-f917-41fb-8f68-9f81eb2701b1.png)

加载设备后，点击上方工具栏激活配置，TwinCAT选择NC控制后，默认已经绑定好相关的对象，不需要自己手动绑定。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b54767e6-da30-4275-a521-111ba3bf6a7c.png)

通过点击Axes->Axis1->Enc对编码器单位进行配置。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/61725282-fb85-45dd-a44e-6610472fca91.png)

点击Axes->Axis 1中的Online选项卡可以运行CSP模式。点击Set按钮，并勾选其中的3项，最后点击OK可以对电机进行使能。操作下方黄色按钮，可以对电机进行点动操作。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2a541f2a-482e-4bc9-8e26-92c109af430a.png)

新建一个PLC工程，用于测试倍福的运动控制功能块，展开PLC->新建工程名字->新建工程名字 Project->References，右键加载运动控制库Tc2\_MC2。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/3f9cf550-75c8-47f7-a7c8-40768739c01f.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/0b77433d-92a4-4d9f-922d-21d069b64f56.png)

定义一个轴变量axis1，并为刚添加的使能模块定义一个变量power，如下图所示。对程序进行编译，会在Instance中看到多出了一个轴变量。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/88c8a78e-3710-459a-af4b-01aa36848690.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/a9afc7ec-5418-4c7e-b4e8-82ed9af11366.png)

点击Axes->Axis1，选择Setting选项卡，点击Link to PLC... 选择上面程序中的实例，将NC轴绑定到PLC轴中。并重新激活配置，登录虚拟PLC后，运行程序，修改变量power\_enable，可以对点击执行使能操作。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2a799e3a-8927-473b-a1de-40c4f8314b6b.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f007fa07-e5b8-4619-b457-f0cc6282c7c3.png)

### 3.1.2 回零测试

#### 3.1.2.1 原点开关回零

#### 3.1.2.2 挡板回零

没有原点开关的情况下，回零参考如下：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/3147c587-2eff-4bd1-84f8-accfa0bacc05.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/07476420-2af6-46be-a5dd-4dd97c3d90e5.png)

#### 3.1.2.3 Z相回零

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/8068fe0c-5309-494f-8ec0-13d4fe029725.png)

## 3.2 适配欧姆龙NX1P2

新建一个欧姆龙工程，欧姆龙PLC的默认IP是192.168.250.1，并选择Ethernet connection via a hub，最后电机OK，建立电脑与欧姆龙PLC的网络连接。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/ac18918b-0068-48cc-ac22-091d3c9362ff.png)

双击EtherCAT，在右侧界面右键Master，电机Display ESI Library，加载xml文件。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/243ec1bf-0bfd-4af1-bf65-b77fd6986b28.png)

点击Install(File)按钮，选择SAC-N2双轴驱动器xml文件，并点击Yes，完成加载后点击Close按钮。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/869df37d-9a48-44eb-aef4-5211ad46c735.png)

此时在上位机的右侧界面可以看到新加载的xml文件，按住左键拖动到Master的下方，可以完成组态。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/0830acde-8d96-446c-989f-a0641df73d59.png)

点击左侧Motion Control Setup ->Axis Settings -> Add -> Motion Control Axis添加轴变量。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2f7a9258-8ff7-442d-ad30-f27c7fee6bc7.png)

在Axis type下拉框中选择Servo axis，在Output device 1下拉框中选择Node 1 Slot0 ，绑定驱动器的轴1。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/0f50fe7d-b1e9-490d-b594-15d021724b45.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/4383647d-b92f-4531-8e6a-e221b1830011.png)

展开Detailed Settings，绑定相关对象，如下图所示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b562a5c1-2957-41aa-a42b-65a97c44a635.png)

点击工具栏的黄色三角按钮登录到PLC，右键Master，选择Write Slave Node Address更改节点地址，必须要修改节点地址跟网络中分配的地址一致后面才能组态成功。写入新的地址后需要重启PLC生效。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5c9148dd-daa0-4965-85a5-6ad1551056c2.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/bdb891ed-e281-4c4c-b9d5-9273907c1502.png)

点击工具栏下载程序图标，将程序下载到PLC中。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b67cdd70-bf37-40ee-a007-00e856902aea.png)

确认组态成功后，双轴设备图标下会出现黑色小三角形，然后可以直接在程序编辑区调用欧姆龙自带的Motion Control库中的模块驱动电机，模块的详细说明可以参考欧姆龙的帮助手册：

*   MC\_Power 电机上使能
    
*   MC\_MoveAbsolute 电机运行CSP模式
    
*   MC\_TorqueControl 电机运行CST模式
    
*   MC\_SyncMoveVelocity 电机运行CSV模式
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/d73d4ac4-983d-4e17-bb71-6a6c1cd4a7f8.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f0fa4e02-52dc-469d-a5c0-1ee3fc0ffdaa.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/d7702ad7-1065-46e0-8dc3-8fa457f1bcc6.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/86a4ec1b-28cd-4dbe-9395-916ea9c8565c.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/78613a22-4f8b-4cb8-8bec-8879eb6f457e.png)

## 3.3 适配基恩士KV7500

新建一个基恩士KV7500工程，基恩士PLC的默认IP是192.168.0.10，使用Ethernet与基恩士进行通讯；

1、添加运动控制模块

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5d2b41f4-480a-4212-8ea1-77a312818aff.png)

2、添加xml文件，添加从站配置PDO参数，注意选择使用扩展设定，把从站属性修改成双轴驱动；

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b66552a7-fc9c-47fe-9e96-e989c9c04674.png)

3、把程序下载到PLC，登录到监控器

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/b0295487-712a-4ba5-b32b-b4a1cb00d40f.png)

4、右键运动模块，点击单元监控器，点击试运转

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/0a464cf7-31b1-466a-9eff-aaca93ffed12.png)

5、点击试运转的定位，选择轴号，打开了轴调试控制面板即可调试控制

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/93e56a88-f7c7-446f-8f1f-a9ac02832cdf.png)

## 3.4 适配汇川AM403

1、建立一个新的标准工程文件，文件名称和存放位置根据实际需求设置。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/762956ac-4be3-4ca1-bb5e-adbefcdaad52.png)

2、添加EterCAT主站，便于后面轴控制程序任务配置修改

![1687946745272.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/efd63605-c2aa-4b22-9788-80746f202faf.png)

3、双轴驱动器XML文件添加

![1687947093471.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/31e0202f-2448-4fdd-a309-7a1fe4fac67f.png)

4、从站设备添加。

![1687947413914.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/2535e4e1-f092-4958-81b3-0acb7c257ca5.png)

5、网络配置，左键双击Device，单击右侧Scan network，选择对应的PLC型号，完成网络配置，保证PC，PLC，驱动器成功组态。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/920893d3-6ce3-4658-b6e5-8b34b39a18ff.png)

6、两个电机添加如图

![1687947725252.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f97f662f-d9c8-4f5a-ba74-b58dc17f0197.png)

添加后

![1687947788678.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/45871c57-b4c9-4adc-94f2-ea79c9234538.png)

7、电机配置参数修改

![1698292618467.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/648a66be-0193-4117-94b4-a4e62727debc.png)

![1698292693549.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/cf9bac48-a5db-40b8-a852-280ebd46de26.png)

8、轴程序添加

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/c147a779-1ae5-479b-a3a5-38a4b40eb792.png)

9、轴控制程序应在EterCAT任务下，故进行任务更换

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/0818bc65-556f-454e-91ca-3a3d1ec1aab2.png)

更改后

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/6a2e88d8-78cd-407a-ab37-5c83f936b101.png)

10、电机回零

10.1 Z轴采用的极限回零后寻找第一个Z相信号，故采用34回原方式（index标记正向移动；在启动参数（SDO设置）里面添加6098（Homing Method）、6099：16#01（Speed during search for switch）、6099：16#02（Speed during search for zero）、689A（Homing acceleration）。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f1b2fa30-0aa0-4fb3-ad99-e4703efe91e8.png)

10.2 R轴采用的采集到光电信号后，寻找第一个Z相信号，故采用3回原方式（index标记正向移动；在启动参数（SDO设置）里面添加6898（Homing Method）、6899：16#01（Speed during search for switch）、6899：16#02（Speed during search for zero）、689A（Homing acceleration）。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5b800ca5-95c6-4779-9cfa-56d3d3557541.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f1b2fa30-0aa0-4fb3-ad99-e4703efe91e8.png)

11.力矩控制

可以使用MC\_TorqueControl或者SMC\_SetTorque功能块，切换为力矩模式进行力矩控制。但是MC\_TorqueControl需要绑定607F对象Max profile velocity，但是双轴607F目前设置为不可映射，所以改用SMC\_SetTorque。

注意切换模式的时候，MC\_Stop的使能信号K必须断使能，否则模式没有办法切换成功。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/1bf44c78-c083-485c-8d41-ca46c4aaab0b.png)

需要注意的是，双轴力矩控制如果要控制速度，需要设置6080对象，给一个速度限制值，如果设置为0，则电机因为没有速度而不会运动，6080对象的单位为RPM。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/031c05a8-ead2-406e-a3ad-35cd1bec1652.png)

## 3.5 适配汇川H5U

变量表

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/54c6ad39-0b37-48da-a45d-8ebf04ebc1bf.png)

编码器分辨率配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f08aa4ee-7457-42ab-883b-c16f1b514925.png)

梯形图程序

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/24b96de2-6291-4941-9df7-5f0a67525ac8.png)

回零配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/ce322035-f33d-4fe0-a248-4b16749085cc.png)

## 3.6 适配MaxTang NX6412

![1712563462047_D747151C-E431-48a5-9F54-B43C6BA3F124.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/fb46e730-3cbe-4918-9b2d-d2dc92aacc83.png)

安装丢失的库文件：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/c4617b5e-b906-4d31-b68f-c75e436c76fd.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/d978d3ce-ab94-466d-bf5c-9603ac43f881.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/782aab24-959f-4d3c-930c-b7052a9c1d29.png)

## 3.7 适配固高GEN控制卡

将双轴xml文件放入Devices目录下

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/808c96fc-a36e-479e-9d55-e1eddb8f0f25.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/9f6902fa-2671-4e68-afe5-9d9f8f41240f.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/d7ef82d1-78f5-4a6a-b8cd-852520d2588c.png)

# 第四章 CIA402协议设备控制

## 4.1 CIA402状态机

SAC-N2伺服驱动器按照CIA402的状态机工作，当连接主站是，主站也必须做相应配置，从而遵循CIA402协议。该设备由PDO和SDO直接从CANopen网络进行控制，通过控制字6040H对伺服的状态进行控制，并通过状态字6041H读取驱动器的实时状态。

CIA402状态机描述设备状态和驱动器的可能控制顺序，单个状态表示一种特殊的内部或外部行为。驱动器的状态还决定接受哪些命令，例如，只有当驱动器处于OPERATION ENABLE（操作启用）状态时，才能开始点对点移动。

下图描述了从站设备由于用户命令或接收到内部错误后的状态机转换流程：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f94afafd-cff8-421e-b95c-5d3c5620cf82.png)

各状态描述如下表：

| 状态 | 说明 |
| --- | --- |
| 初始化<br>Not ready to switch on | 驱动器初始化，内部自检已完成。<br>驱动器参数不可设定，也不能执行驱动功能。 |
| 伺服无故障<br>Switch on disabled | 驱动器无故障或错误，驱动器参数可以设定。 |
| 伺服准备好<br>Ready to switch on | 驱动器已准备就绪。<br>驱动器参数可以设定。 |
| 等待打开伺服使能<br>Switched on | 驱动器等待打开伺服使能。<br>驱动器参数可以设定。 |
| 伺服运行<br>Operation enable | 驱动器正常运行，已使能某一种运行模式，电机已通电。<br>驱动器参数可以设定。 |
| 快速停机<br>Quick stop | 快速停机功能被激活，驱动器正常执行快速停机功能。<br>驱动器参数可以设定。 |
| 故障停机<br>Fault reaction active | 驱动器发生故障，正在执行故障停机功能。<br>驱动器参数可以设定。 |
| 故障<br>Fault | 故障停机已完成。所有驱动功能被进制。<br>允许更改驱动器参数以便排除故障。 |

控制命令与状态切换说明如下：

| 状态切换 | 控制字(6040H) | 状态字(6041H) |
| --- | --- | --- |
| 0 | 自然过渡，无需控制指令。 | 0000H |
| 1 | 自然过渡，无需控制指令。<br>若初始化种发生错误，直接进入13 | 0250H |
| 2 | 0006H | 0231H |
| 3 | 0007H | 0233H |
| 4 | 000FH | 0237H |
| 5 | 0007H | 0233H |
| 6 | 0006H | 0231H |
| 7 | 0000H | 0250H |
| 8 | 0006H | 0231H |
| 9 | 0000H | 0250H |
| 10 | 0000H | 0250H |
| 11 | 0002H | 0217H |
| 12 | 快速停机方式，对象605A写入0~2。<br>停机完成后，自然过渡，无需控制指令。 | 0250H |
| 13 | 除”故障“状态外其他任意状态下，驱动器一旦发生故障，自然切换到故障停机状态，无需控制指令。 | 021FH |
| 14 | 故障停机完成后，自然过渡，无需控制指令。 | 0218H |
| 15 | 0080H | 0250H |
| 16 | 快速停机方式 605A 选择5~6，停机完成后，发送0FH。 | 0237H |

控制字6040H说明：

| 索引 | 名称 | PDO 映射 | 数据类型 |
| --- | --- | --- | --- |
| 6040H | Controlword 控制字 | RxPDO | UINT16 |
|  | 主控制器通过该对象来控制驱动器。Controlword 的各个 bit 的详细信息如下：<br>\| 15 \| 14 \| 13 \| 12 \| 11 \| 10 \| 9 \| 8 \| 7 \| 6 \| 5 \| 4 \| 3 \| 2 \| 1 \| 0 \|<br>\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|<br>\| Manufacture specific \|  \|  \|  \|  \|  \|  \| h \| fr \| oms \|  \|  \| eo \| qs \| ev \| so \|<br>其中：  so＝switch on ev＝enable voltage    qs＝quick stop <br>             eo＝enable operation fr＝fault reset h＝halt <br>oms＝operation mode specific<br>状态机的传输由 bit0～bit3 和 bit7 组成的控制命令来触发。<br>\| 控制命令 \| bit7 \| bit3 \| bit2 \| bit1 \| bit0 \| 传输 \|<br>\| --- \| --- \| --- \| --- \| --- \| --- \| --- \|<br>\|  \| fr \| eo \| qs \| ev \| so \|<br>\| Shutdown \| 0 \| － \| 1 \| 1 \| 0 \| 2, 6, 8 \|<br>\| Switch on \| 0 \| 0 \| 1 \| 1 \| 1 \| 3 \|<br>\| Switch on + Enable operation \| 0 \| 1 \| 1 \| 1 \| 1 \| 3+4 \|<br>\| Enabled operation \| 0 \| 1 \| 1 \| 1 \| 1 \| 4,16 \|<br>\| Disable voltage \| 0 \| － \| － \| 0 \| － \| 7,9,10,12 \|<br>\| Quick stop \| 0 \| － \| 0 \| 1 \| － \| 7,10,11 \|<br>\| Disabled operation \| 0 \| 0 \| 1 \| 1 \| 1 \| 5 \|<br>\| Fault reset \|  \| － \| － \| － \| － \| 15 \|<br>bit4、bit5 和 bit6：在如下控制模式下的定义不同。（“－”表示未使用，设定为 0）<br>\| 控制模式 \| bit6 \| bit5 \| bit4 \|<br>\| --- \| --- \| --- \| --- \|<br>\| PP \| Absolute／Relative \| Change set immediately \| New set-point \|<br>\| HM \| － \| － \| Start homing \|<br>\| IP \| － \| － \| Enable interpolation \|<br>bit8：halt 位。置为 1，通过 605Dh（halt 选项）执行电机减速暂停；<br>暂停后，返回 0 再开始动作。HM 模式下，置为 1 表示中断，返回 0 也无法再次动作。 |  |  |

状态字6041H说明：

| 索引 | 名称／描述 | PDO 映射 | 数据类型 |
| --- | --- | --- | --- |
| 6041H | Statusword 状态字 | TxPDO | UINT16 |
|  | 主控制器通过该对象来控制驱动器。Statusword 的各个bit 的详细信息如下：<br>\| 15 \| 14 \| 13 \| 12 \| 11 \| 10 \| 9 \| 8 \| 7 \| 6 \| 5 \| 4 \| 3 \| 2 \| 1 \| 0 \|<br>\| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \| --- \|<br>\| r \| r \| oms \|  \| ila \| oms \| rm \| r \| w \| sod \| qs \| ve \| f \| oe \| so \| rtso \|<br>其中: r＝reserved w＝warning sod＝switch on disabled <br>ve＝voltage enabled f＝fault           ila＝internal limit active <br>oe＝operation enabled so＝switched on   rm＝remote<br>rtso＝ready to switch on  hf＝homeflag oms＝operation mode specific<br>根据bit6、bit5、bit3～bit0（switch on disabled／quick stop／fault／<br>operation enabled／ switched on／ready to switch on）可确认驱动器的状态。<br>\| Statuword \| 驱动器状态 \|  \|<br>\| --- \| --- \| --- \|<br>\| xxxx xxxx x0xx 0000 \| Not ready to switch on \| 初始化 \|<br>\| xxxx xxxx x1xx 0000 \| Switch on disabled \| 伺服无故障 \|<br>\| xxxx xxxx x01x 0001 \| Ready to switch on \| 伺服准备好 \|<br>\| xxxx xxxx x01x 0011 \| Switched on \| 等待打开伺服使能 \|<br>\| xxxx xxxx x01x 0111 \| Operation enabled \| 伺服运行 \|<br>\| xxxx xxxx x00x 0111 \| Quick stop active \| 快速停机 \|<br>\| xxxx xxxx x0xx 1111 \| Fault reaction active \| 故障停机 \|<br>\| xxxx xxxx x0xx 1000 \| Fault \| 故障 \|<br>bit4(voltage enabled)：置为1时，表示主电源已接通；置为0时，表示主电源已断开。<br>bit5 (quick stop)：置为 0时，表示驱动器通过605Ah（快速停机选项）执行电机停止。<br>bit7 (Warning)：置为 1 时，表示警告正在发生。发生警告后，电机继续运行。<br>bit8 (reserved)：未使用，固定为 0。<br>bit9 (Remote)：固定为 1。<br>bit13、bit12、bit10 (operation mode specific)：在如下控制模式下的定义不同。<br>\| 控制模式 \| bit13 \| bit12 \| bit10 \|<br>\| --- \| --- \| --- \| --- \|<br>\| PP／CSP \| following error \| Set-point acknowledge \| Target reached \|<br>\| PV \| Max slippage error \| Speed is equal 0 \| Target reached \|<br>\| HM \| Homing error \| Homing attained \| Target reached \|<br>bit11 (Internal limit active)：置为 1 时，表示内部转矩超过设定值或者机械撞到外部正负限位开关。 |  |  |

## 4.2 位置控制

### 4.2.1 轮廓位置模式

**功能简介**

轮廓位置模式，即profile position mode，用于点到点运动，通过给定速度，加速度等信息，通过内部的轨迹发生器生成位置指令，以此控制伺服运动。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/a7575b0b-6043-48aa-90f1-951399fbda1a.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5b0656b7-ea19-423c-a555-0afd6c9667b7.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 607AH | 00H | Target position | 指令单位 | RxPDO |
| 6081H | 00H | Profile velocity | 指令单位/s | RxPDO |
| 6083H | 00H | Profile acceleration | 单位指令/s² | RxPDO |
| 6084H | 00H | Profile deceleration | 单位指令/s² | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 6064H | 00H | Position actual value | 指令单位 | TxPDO |

**操作方法**

1.  设置6060H对象为1，切换为轮廓位置模式。
    
2.  设置6081H对象，设置规划速度。
    
3.  设置6083H对象，设置规划加速度。
    
4.  设置6084H对象，设置规划减速度。
    
5.  设置607AH对象，设置目标位置。
    
6.  设置6040H对象，使能伺服驱动器并触发电机运动。
    
7.  查询对象6061H，获取伺服驱动器的状态反馈。
    
8.  查询对象6064H，获取电机的实际位置。
    

### 4.2.2 同步位置模式

**功能简介**

周期同步位置模式，即Cyclic sync position mode，由主站生成位置轨迹规划并发送到伺服，以此驱动电机运动。该模式与轮廓位置模式最大的区别是生成运动轨迹的对象不同，轮廓位置模式通过驱动器内部生成轨迹规划。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/e7798f5c-6b77-46bf-b8ef-e5bbc4fee17f.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/98860e81-69dd-4fa7-b4aa-9062a10d477b.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 607AH | 00H | Target position | 指令单位 | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 6064H | 00H | Position actual value | 指令单位 | TxPDO |

**操作方法**

1.  设置6060H对象为8，切换为同步位置模式。
    
2.  主站启动DC模式。
    
3.  设置607AH对象，设置目标位置。
    
4.  设置6040H对象，使能伺服驱动器并触发电机运动。
    
5.  查询对象6061H，获取伺服驱动器的状态反馈。
    
6.  查询对象6064H，获取电机的实际位置。
    

## 4.3 速度控制

### 4.3.1 轮廓速度模式

**功能简介**

轮廓速度模式，即profile velocity mode，通过给定速度，加速度等信息，通过内部的轨迹发生器生成速度指令，以此控制伺服的速度。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f22cf2b6-422d-4407-97d3-258ad6bc7b36.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 607FH | 00H | Max profile velocity | 指令单位/s | RxPDO |
| 6083H | 00H | Profile acceleration | 单位指令/s² | RxPDO |
| 6084H | 00H | Profile deceleration | 单位指令/s² | RxPDO |
| 60FFH | 00H | Target velocity | 指令单位/s | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 606CH | 00H | Velocity actual value | 指令单位 | TxPDO |

操作方法

1.  设置6060H对象为3，切换为轮廓速度模式。
    
2.  设置6083H对象，设置加速度。
    
3.  设置6084H对象，设置减速度
    
4.  设置607FH对象，设置最大速度。
    
5.  设置6040H对象，使能伺服驱动器。
    
6.  设置60FFH对象，设置目标速度。
    
7.  查询对象6061H，获取伺服驱动器的状态反馈。
    
8.  查询对象606CH，获取电机的实际速度。
    

### 4.3.2 同步速度模式

**功能简介**

周期同步速度模式，即Cyclic sync velocity mode，由主站生成速度轨迹规划并发送到伺服，以此实现速度控制。该模式与轮廓速度模式最大的区别是生成速度轨迹的对象不同，轮廓速度模式通过驱动器内部生成速度轨迹规划。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/1d88afd4-e040-4bbc-831f-e42526f7fe85.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/12a5a7d4-0be0-454e-9514-18e3bb66df4d.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 60FFH | 00H | Target velocity | 指令单位/s | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 606CH | 00H | Velocity actual value | 指令单位 | TxPDO |

**操作方法**

1.  设置6060H对象为9，切换为同步速度模式。
    
2.  主站启动DC模式。
    
3.  设置6040H对象，使能伺服驱动器。
    
4.  设置60FFH对象，设置目标速度。
    
5.  查询对象6061H，获取伺服驱动器的状态反馈。
    
6.  查询对象606CH，获取电机的实际速度。
    

## 4.4 转矩控制

### 4.4.1 轮廓转矩模式

**功能简介**

轮廓转矩模式，即profile torque mode，通过给定目标转矩，加速度等信息，通过内部的轨迹发生器生成转矩指令，以此控制伺服输出恒定转矩。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/832ce1a6-12e5-4296-86d6-9856cb4f5079.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 6071H | 00H | Target torque | 0.1% | RxPDO |
| 6072H | 00H | Max torque | 0.1% | RxPDO |
| 6087H | 00H | Torque slope | 0.1%/s | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 6077H | 00H | Torque actual value | 0.1% | TxPDO |

**操作方法**

1.  设置6060H对象为4，切换为轮廓力矩模式。
    
2.  设置6071H对象，设置目标力矩。
    
3.  设置6072H对象，限制最大力矩输出。
    
4.  设置6087H对象，设置力矩变化率。
    
5.  设置6040H对象，使能伺服驱动器，启动电机运转。
    
6.  查询对象6061H，获取伺服驱动器的状态反馈。
    
7.  查询对象6077H，获取电机的实际力矩输出。
    

### 4.4.2 同步转矩模式

**功能简介**

周期同步转矩模式，即Cyclic sync torque mode，由主站给定输出力矩，速度等参数到伺服，以此实现伺服输出恒定力矩，恒定速度的功能。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/cdb218c4-4d36-44a2-b2f0-532a77513189.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/6404acdb-4d44-47d5-a27b-8ebaa9f07f17.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6060H | 00H | Modes of operation | \- | RxPDO |
| 6071H | 00H | Target torque | 0.1% | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |
| 6061H | 00H | Modes of operation display | \- | TxPDO |
| 6077H | 00H | Torque actual value | 0.1% | TxPDO |

**操作方法**

1.  设置6060H对象为10，切换为同步转矩模式。
    
2.  主站启动DC模式。
    
3.  设置6040H对象，使能伺服驱动器。
    
4.  设置60F1H对象，设置目标转矩。
    
5.  查询对象6061H，获取伺服驱动器的状态反馈。
    
6.  查询对象6077H，获取电机的实际电流反馈。
    

## 4.5 回零

**功能简介**

回零模式，即Homing Mode，指设定电机寻找原点/零点的方式。有多种方式可以实现这一功能，包括使用行程末端的限位开关、行程中间的原点开关，还可以使用增量式编码器的索引脉冲信号，控制框图如下所示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/437104bb-4baf-4ae8-bf8f-9d6710e72db8.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 6040H | 00H | Control word | \- | RxPDO |
| 6098H | 00H | Homing method | \- | RxPDO |
| 6099H | \- | Homing speeds | \- | \- |
|  | 01H | Speed during search for switch | 指令单位/s | RxPDO |
|  | 02H | Speed during search for zero | 指令单位/s | RxPDO |
| 609AH | 00H | Homing acceleration | 指令单位/s | RxPDO |
| 607CH | 00H | Homing offset | 指令单位 | RxPDO |
| 6041H | 00H | Status word | \- | TxPDO |

**操作方法**

1.  设置6060H对象为6，切换为回零模式。
    
2.  设置6098H对象，设置范围1~35，选择回零方法。
    
3.  设置607CH对象，设置原点偏移。
    
4.  设置6099H:01，修改回零过程中寻找原点开关的速度。
    
5.  设置6099H:02，修改回零过程种寻找零点的速度。
    
6.  设置609AH对象，设置回零加减速度。
    
7.  设置6040H对象，使能伺服驱动器，并启动回零过程。
    
8.  电机查找限位开关以及原点开关，完成回零动作。
    
9.  查询6041H对象获取驱动器状态反馈。
    

## 4.6 回零方法

回零模式中可以通过6098H对象设置回零方法，标准方法共35种，下面简单介绍各种方法的区别，如果想要深入了解回零方法的客户，可以参考CIA402协议文档。

备注1：默认运动方向从左到右，向左运动视为负方向，向右运动视为正方向。

备注2：原点开关在电机右侧视为正向原点开关，在左侧视为负向原点开关。

**方法1 负限位开关下降沿+Z相信号回零：**

在该方法中，电机会负向运动至负限位开关处，检测到堵转后反向搜索Z相回零。

![hm1.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/5b6078cf-2472-4553-bde4-c3d1589f502c.jpeg)

**方法2 正限位开关下降沿+Z相信号回零：**

在该方法中，电机会正向运动至正限位开关处，检测到堵转后反向搜索Z相回零。

![hm2.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/6ff80b37-1588-48a8-a0e9-867f0e7519b2.jpeg)

**方法3、4 正向原点开关边沿+Z相脉冲回零：**

此类方法中，原点开关在电机正方向位置，电机的运动方向依赖于原点开关的初始电平状态，当检测到原点开关的边沿信号后，遇到第一个Z向信号后停止，完成回零。

![hm3-4.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/89d319aa-c9c6-4a28-961b-0ba5b6707560.jpeg)

**方法5、6 负向原点开关边沿+Z相脉冲回零：**

此类方法中，原点开关在电机负方向位置，电机的运动方向依赖于原点开关的初始电平状态，当检测到原点开关的边沿信号后，遇到第一个Z向信号后停止，完成回零。

![hm5-6.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/26148e59-902f-47ad-8333-bb5b32382ea0.jpeg)

方法7~10 原点开关边沿+Z相脉冲+正限位开关回零：

此类方法对应上面提到的3~6回零方法，在此基础上增加了正限位开关，当电机运动时，检测到正限位开关上升沿信号时会反向运动。

![hm7-10.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/8973af48-c89e-4f8d-ad29-c377d0272819.jpeg)

方法11~14 原点开关边沿+Z相脉冲+负限位开关回零：

此类方法对应上面提到的3~6回零方法，在此基础上增加了负限位开关，当电机运动时，检测到负限位开关上升沿信号时会反向运动。

![hm11-14.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/18296b34-1c67-419d-a0a8-a6698d6b8043.jpeg)

方法15、16保留。

方法17 负限位开关下降沿回零：

此方法与回零方法1类似，不使用Z相信号，仅依赖负限位开关信号。

![hm17.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/cf7e2563-fd85-44e9-bc9f-fa53d24b08e9.jpeg)

方法18 正限位开关下降沿回零：

此方法与回零方法2类似，不使用Z相信号，仅依赖正限位开关信号。

![hm18.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/1188f422-9df5-4803-9376-31da8d19aea2.jpeg)

方法19、20 正向原点开关边沿回零：

此类方法与回零方法3、4类似，外部信号不使用Z相信号，只依赖于正向原点开关。

![hm19-20.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/4c0e35de-ad6e-4064-a15b-145b55a81c20.jpeg)

方法21、22 负向原点开关边沿回零：

此类方法与回零方法5、6类似，外部信号不使用Z相信号，只依赖于负向原点开关。

![hm21-22.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/a4bc7182-a754-4ce1-9b2e-bdc3e1338749.jpeg)

方法23~26 原点开关边沿+正限位开关回零：

此类方法与回零方法7~10类似，外部信号不使用Z相信号，只依赖原点开关和正限位开关。

![hm23-26.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/566c1580-8c56-435f-8c34-743aa7a70894.jpeg)

方法27~30 原点开关边沿+负限位开关回零：

此类方法与回零方法11~14类似，外部信号不使用Z相信号，只依赖原点开关和负限位开关。

![hm27-30.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/4066a5f1-fcd9-465f-a89d-069bc7c863a0.jpeg)

方法31、32保留。

方法33、34 单向移动零位脉冲：

此方法只依赖Z相信号回零，电机往一个方向运动，当检测到第一个Z相信号后停止，完成回零。

![hm33-34.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/8124f59d-1c64-459c-97a6-2acc2c81a684.jpeg)

方法35 当前位置回零：

此方法直接将当前位置设置为零点。

![35.jpeg](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/a6806ea5-adaa-442b-9ee9-53574ddce1b3.jpeg)

## 4.7 探针功能

**功能简介**

探针功能又称位置锁存功能，可通过外部数字输入信号或者编码器Z相信号实时锁存伺服轴或者编码器值。探针功能在模切，印刷等需要位置同步的场合应用广泛。探针功能可通过对象60B8H的bit1/9设置探针模式，分别是事件模式（Trigger first event）和连续模式（Continuous）。同时可以配置触发信号，外部输入或者Z相信号。也可以配置上升沿还是下降沿触发探针。

**Touch probe事件模式：**

探针功能启动后，当检测到触发信号的上升沿或下降沿时，驱动器内部记录此时编码器的实际位置，并上传到PLC，同时会通过探针状态对象60B9H告诉PLC已经锁存位置。此时如果用户想要触发下一次的探针功能，则需要重复上述操作，通过60B8H对象重新启动下一次的探针功能。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/c982bc18-a64f-4480-928e-ab0599d0b8ef.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/808db8a8-87dd-4ba5-8cf7-5d7904c5f112.png)

**Touch probe连续模式：**

探针功能启动后，当前侧到第一个触发信号的边沿信号时，驱动器内部开始记录此时编码器的实际位置，并上传到PLC，同时会通过探针状态对象60B9H告诉PLC已经锁存位置。与事件模式不同的是，在连续模式中，驱动器在每次上升沿时，都会锁存当前位置，当新的位置被锁存，旧的数据会被覆盖。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/f6bb53b3-48e3-46a1-8d66-4c5da6ffcd91.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVYyXBx9l4XB/img/1cb78089-0aa0-4fef-b02b-db9cb900735c.png)

**推荐关联对象**

| 索引 | 子索引 | 对象名字 | 单位 | PDO |
| --- | --- | --- | --- | --- |
| 60B8H | 00H | Touch probe function | \- | RxPDO |
| 60B9H | 00H | Touch probe status | \- | TxPDO |
| 60BAH | 00H | Touch probe pos1 pos value | 指令单位 | TxPDO |
| 60BBH | 00H | Touch probe pos1 neg value | 指令单位 | TxPDO |
| 60BCH | 00H | Touch probe pos2 pos value | 指令单位 | TxPDO |
| 60BDH | 00H | Touch probe pos2 neg value | 指令单位 | TxPDO |

**操作方法**

1.  设置60B8H对象，配置探针模式的模式，触发信号和边沿触发等功能。
    
2.  设置60B8H对象，启动探针功能。
    
3.  查询60B9H对象，监控探针状态，位置是否锁存成功。
    
4.  查询60BAH~60BDH对象，获取锁存的位置值。