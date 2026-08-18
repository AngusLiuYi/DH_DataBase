# SAC-N2 FAQ

**1.上位机上使能后，电机无法锁住位置，跟没有使能一样，但是上位机显示电机已经上使能。**

解决方法：确认参数表中2007.04~2007.07 4个参数的值，如果其中有一个设置为0，则会出现上述现象，必须设置一个非零值，单位是%，电流限制值为额定电流的%。设置为300表示最大输出电流为额定电流的3倍。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/f55865d7-93a1-4b7e-a3fe-e9fba7f1fcf4.png)

**2.编码器配置正确，电机可以正常寻相，但是运动控制时，只能走大约一个极对的距离。如下图：**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/de9e0985-ffe3-4996-a3ae-4c2a5afafd08.png)

解决方法：检查电机参数里面的极对数是否正确，出现上图问题的原因是因为将4对极的电机配置成了5对极导致的。

**3.上位机在运动控制过程中，报过速错误，如下图：**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/89487da9-c3c5-40ff-bf2f-b4a3b41091bf.png)

解决方法：参数表故障与保护，将过速阈值设置为大于目标转速值即可，比如电机需要跑3000rpm，那么该参数建议设置为3500rpm。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/6dd75ad2-bbcc-48f2-803d-8d055b736627.png)

**4.驱动器误报编码器连接错误，如何解决？**

解决办法：通过加大断线重连次数和加大abz编码器窗口滤波时间，推荐值分辨是 50 和 0.1。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/1d866ddc-68b4-42e2-b9f6-bd36a1674168.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/4a47c956-f125-4dc5-a7c6-06cedc05a989.png)

**5.回零速度太快导致找不到原点开关或者正负限位开关信号。**

解决方法：适当降低回零速度，通过观察上位机IO配置上的电平状态来检查IO信号是否已经被触发。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/1fcb6cd1-9e7e-4dcb-93fb-5cb0ec80f85e.png)

**6.上电后直接报电机过载，软件过流，电流零点过大错误。**

解决方法：

*   检查供电是否正常，是否为24V或者48V。
    
*   电机UVW是否接好？没接好会误报这个错误。
    
*   STO有没有连接？没有连接会误报这个错误。
    

**7.更新固件或者更新参数表后，发现可以正常寻相，但是上使能后无法锁轴，电机可以推动。**

解决方法：

图中的这两个参数必须设置为0。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/d8947ad5-2f5c-43c1-919c-e561e773023f.png)

**8.驱动器上电后数码管显示RST，经过很长一段时间后可以正常显示100，此时上位机读取驱动器型号失败，提示读取异常，重启上位机后却能正常读取。**

解决方法：

功率检测时间设置为0，设置时间过长会导致驱动器无法快速启动，上位机无法读取驱动器型号。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/8c973ade-6221-4808-bfd2-776c8d1c3453.png)

**9.主站连接双轴驱动器，数码管并没有显示888，而是显示000。**

解决方法：

控制模式选择改为 “9.EtherCAT总线控制”。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/7f405b6f-32b1-4721-b23e-34e2490217d2.png)

**10.轴上使能后，手动去转动轴，发现电机不能回到原点，位置发生偏差。**

解决办法：

把图中的两个消抖相关的参数设置为0。

![67eb9b2e7e7577627cf3758b7963adea.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/dd6bdcb0-ca89-446c-ab5f-250ac41180fc.png)

**11.驱动器控制电与逻辑电分开供电，上电后，驱动器报错，伺服读取异常，导致“电机缺相错误”，电机剧烈震动。**

解决办法：

伺服读取控制电读取异常导致识别错误，导致内部计算错误，可以通过预设功能来避免识别错误。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/d66b8312-d659-45de-8339-1c9d72555d7e.png)

**12.驱动器组态失败，无法进入OP，欧姆龙PLC提示错误，通过上位机读取同步周期与PLC设置的同步周期不相同。**

解决办法：

检查xml文件是否与PLC的xml版本一致，更新xml文件；也可以通过通讯周期方式选择写入1，然后在对同步周期进行修改，强制把同步周期设置与PLC一致。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOkxKEZb32l4BX/img/76051780-d327-4de7-84f9-e58571ab494d.png)