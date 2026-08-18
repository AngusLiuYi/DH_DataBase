# SAC-N2 XML文件更新指导手册

上位机连接双轴驱动器后，数码管提示0x13错误，表示双轴驱动器没有烧录EtherCAT xml文件，这会导致EtherCAT主站无法连接，因此需要先确保已经烧录正确的xml文件。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mPdnp8x0MZGvnw98/img/bc51ee47-2bc7-408d-8902-70549baf4178.png)

我们双轴的上位机集成了eeprom programmer工具，可用于更新双轴内部xml文件。点击驱动器信息 -> 查看xml版本，此时会弹出更新xml文件的软件界面。另外，需要确保此时电脑与双轴驱动器以网线连接，而并非USB。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mPdnp8x0MZGvnw98/img/e140f829-fe4c-4a1f-b395-e529d420cadc.png)

点击File->Open，选择烧录的XML文件。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/a142eb86-a735-46e4-a66c-5e3b347fefdf.png)

打开双轴驱动器的xml文件SAC\_2Axis\_V1.6.1.xml，点击右下角打开文件，因为xml文件后续会持续更新，因此选择哪一个xml文件需要跟技术支持确认。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mPdnp8x0MZGvnw98/img/9d279955-8be3-4e9a-b2fd-2e7c6b6f1559.png)

再次选择Slaves->Scan，扫描连接的ECAT从站设备。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/f438d5d3-d400-4dec-a0ae-eada6e5a27f8.png)

选择对应的网卡，注意选择的是网线连接电脑的那个网卡。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/3524963d-359f-4881-b6c1-e15669437772.png)

如果此时盒子与电脑连接正常，网卡选择正确的情况下，下方会提示找到EtherCAT从站设备，如果是其他提示，请检查前面的步骤是否正确操作。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/0b4fc351-1140-43fe-bba2-8491203b78e5.png)

点击Slave->Program Selected，开始升级XML文件，升级XML文件时间较长，可能需要40秒，期间软件会卡住，耐心等待即可。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/08d31e5c-c7bd-4caa-9596-633b20dbe002.png)

升级xml成功后，下方会提示升级已完成。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/ya2QnVomwXjDq4XB/img/1f994e97-57ca-426d-8598-5ca79a179190.png)