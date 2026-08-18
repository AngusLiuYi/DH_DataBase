# SAC XML文件修改方法

驱动器的xml中采用slot语法，有三个模块，对应的ID分别是0x101，0x102和0x103。可以通过修改Default=“1”，来设定默认使用的模块。比如想让PLC加载xml后默认使用0x101模块，则照搬下图中的设置：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/cc0a40ac-9152-4cf3-a20c-f91331a33e53.png)

如果像默认使用0x103模块，则需要改为，需要注意的是3个模块只能有一个Default等于1。

```c
<Slot MinInstances="1" MaxInstances="1">
  <Name LcId="1033">Axis 1</Name>
  <ModuleIdent Default="0">#x0101</ModuleIdent>
  <ModuleIdent Default="0">#x0102</ModuleIdent>
  <ModuleIdent Default="1">#x0103</ModuleIdent>
</Slot>
<Slot MinInstances="1" MaxInstances="1">
  <Name LcId="1033">Axis 2</Name>
  <ModuleIdent Default="0">#x0101</ModuleIdent>
  <ModuleIdent Default="0">#x0102</ModuleIdent>
  <ModuleIdent Default="1">#x0103</ModuleIdent>
</Slot>
```

模块ID 0x101对应 **CSP CSV CST**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/f74b80ac-7724-4a39-9684-4c2ed87bdd3c.png)

模块ID 0x102对应 **BYD Customization**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/3ac84ca0-e7f2-419d-8a29-7dcbc3bac1f4.png)

模块ID 0x102对应 **Force Control**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/e9a7f702-739e-4edc-8363-a40f8acce129.png)

我们出厂的xml文件都默认配置了一些PDO，不可能都满足所有的客户使用场景。有些用户需要把尽可能多的操作对应映射到PDO，方便自己操作；但有些时候又需要尽可能少的映射PDO来保证通讯性能，所以就免不了需要手动修改PDO列表，下面介绍如何修改默认PDO列表。

比如，我们现在默认使用模块0x101 CSP CSV CST。我们需要定位到 **Modules** 标签，下层又有3个 **Module** 标签，我们需要定位到 0x101的这一个。在Module标签下，还有 **RxPdo** 和 **TxPdo** 两个子标签，分别表示主站发送到从站的数据，如控制字；以及从站返回给主站的数据，如状态字。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/d05202e3-53fa-4a71-a437-47ea1eab1e14.png)

我们展开RxPDO标签，可以看到6040，607A等的对象定义，表示默认有哪些对象放置在了PDO列表中。如果我们需要修改默认的PDO对象，**增加Entry标签**就可以了。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/a18e56f5-46ca-4a03-aecd-e491de9d16dd.png)

其中：

<Entry></Entry> 表示要定义一个PDO。

<Index></Index> 表示对象索引，比如需要添加5018对象时，需要改为#x5018，x表示16进制。

<SubIndex></SubIndex> 表示对象的子索引。

<BitLen></BitLen> 对象的长度，单位时bit。

<Name></Name> 对象要显示的名字。

<Comment></Comment> 附加说明，可选字段，没有这个字段也可以。

<DataType></DataType> 对象类型。

如何或者我们要添加对象的以上信息？

我们可以翻看xml文件前面的对象定义，在Object标签下有详细的说明，我们把这些信息填入到上面提到的Entry标签内即可。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mxPOG5z1Dv5rbnKa/img/df9e2f09-1d12-4540-aa62-fc0efd32425c.png)