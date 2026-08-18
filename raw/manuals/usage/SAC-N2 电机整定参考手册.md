# SAC-N2 电机整定参考手册

## 电机参数配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/a174b70d-e7ab-481c-99d5-d670d65ac674.png)

备注：

1.  D轴电感和Q轴电感设置为一样即可。
    
2.  电机极对数 = 电机极数 / 2。
    

## 编码器配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/a050d2b7-6e1a-46bc-9d99-688dc8231dac.png)

### ABZ增量编码器

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/d1c8027d-b238-456b-b128-5dc985009f65.png)

备注：

1.  图中红色框框中的参数是旋转电机+ABZ编码器时，需要配置的参数。
    
2.  要注意，使用增量编码器时，也需要设置编码器单圈分辨率，1024线的编码器，一圈脉冲数为4096，要求设置编码器单圈分辨率（sub14）≥4倍增量编码器精度（sub16），因此设置为12bit。
    

### biss-c编码器

### 多摩川编码器

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/31e2194a-0f0f-4a0a-8715-6a0c72726420.png)

备注：

1.  图中红色框框中的参数是旋转电机+多摩川编码器时，需要配置的参数。
    
2.  多摩川编码器需要配置多圈值（Sub.16），一般为16bit。
    

### SSI编码器

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/64c57e08-73b0-4e19-92b9-e84543f44467.png)

备注：

1.  图中红色框框中的参数是直线电机+SSI编码器时，需要配置的参数。
    
2.  图中的SSI协议为22bit数据位（Sub.13）+1bit状态位（Sub.26）。
    
3.  当电机类型（Sub.19）选择直线电机时，需要同时配置直线电机极距（Sub.21）和直线电机分辨率（Sub.22）,其中，直线电机分辨率需要通过实际测量确认，单位是 脉冲/mm。
    

## 利用刚性表快速整定电机

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/d233b59b-9e91-4147-ac45-bd3e9d3f0ddd.png)

备注：

1.  通过修改0x2009.Sub0写1，启动标准刚性表模式，并在0x2009.Sub1选择刚性等级。
    
2.  刚性等级越高，增益越强，相应越快，但过强的刚性会引起振动。
    

## 电机寻相

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/09181cba-b145-4c9b-b40a-b859881d4f25.png)

备注：

1.  电机运动前必须先寻相，否则会有飞车的风险。
    
2.  寻相需要查看励磁电流（7）和位置反馈（13），图中蓝色波形为实际位置反馈，红色为励磁电流（D轴电流），图中电流值是放大了1000倍后的结果，实际的寻相电流为2A。
    
3.  寻相的流程为给定正向励磁电流，电机往正方向前进4段位移，结束后返回原来位置，完成寻相。假如实际位置往反方向移动，可以调整0x2001.Sub.24，换相后重复上述动作。
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/ade0519f-49b5-4449-a661-d0ce5a5262a3.png)

备注：

1.  对于增量式编码器，每次上电都需要重新寻相，因此可以将上电自动寻相功能（2001.Sub.20）打开，防止重启后飞车的风险。
    

## 调节电流环

寻相成功后，可以通过跑往复运动，来让电机动起来，确认电机能动起来后，我们将参数表中的2009.Sub.0设置为0，关闭自调整模式，只有关闭掉自调整模式，后续才能调节PID参数。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/97b640ce-286b-4b83-96cb-0a8b319c0641.png)

我们首先调试的是电流环。电机上使能后，先听有没有电流噪声，如果有电流噪声，可以尝试减少DQ轴电感（2001.Sub.10和2001.Sub.11）或者调小电流环增益（2000.Sub.13），直到上使能后没有噪声。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/1db5b0c2-d731-4bc9-bd40-cbf8832f6452.png)

## 调节速度环

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/a4e67650-7eeb-4ef2-a130-27012d790583.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/7127a977-ff84-4aa4-9ce6-4db69887fd36.png)

## 调节位置环

## 调试案例 （LCE-5ML）

### 电机配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/7dcd5399-90e3-45f7-a8c8-725f1587305c.png)

### 编码器配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/2c313abb-78e0-4eff-9bfb-e937168c51c9.png)

### 通过刚性表快速启动电机

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/4015c2ad-0ba8-4810-8590-5bfa1070c1b9.png)

设定刚性表等级为20，然后给电机上使能，发现电流噪声比较大，接下来把DQ轴电感调小，直到电流噪声消失，最终将电感值又原来的0.53改为0.12。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/c243b3d6-7d4b-4a67-bf1c-85b391f0291e.png)

## 调试案例 （MCE-3GD）

电机参数配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/57f42506-eba7-4d4e-b6e0-d90cbd677f34.png)

刚性表选择

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/0a9305e7-5ddd-4d01-900c-1f708aaae650.png)

电流给定与电流反馈

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/a5a75390-fc07-43b9-bfd5-cd8eb105ee80.png)

速度给定与速度反馈

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/aac69003-b50f-47d9-843b-f99e94ba6097.png)

退出刚性表模式，对增益类参数进行调整。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/c285433e-9e1b-49e6-b152-81bebdd8e66e.png)

电流反馈

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/b34aceaa-48b6-4a35-b1d8-fc5ade7f9c12.png)

## 调试案例（RCE-5ML-05-065）

### 电机参数配置

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/00db38b1-a03d-490d-965c-dd3f76a3141b.png)

### 电机寻相

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/190dfd84-3880-48f3-b530-67a5ab297197.png)

### 利用刚性表调试

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/9908cd12-f79d-4f8c-bd85-0ec3ff5ba0b3.png)

### 调试电流环

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/a2b07e6f-562e-452c-b8a6-519330faa84c.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/7a958f0f-aa89-45fa-9fc5-05836cbaaadd.png)

dq轴电感为0.05时，电流无法跟上，需要增大电感。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/4faebcf5-87de-4303-8509-beb2cdbd0bfc.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/78ef3ccd-8e47-40ae-8084-25b8d2643f79.png)

### 调试速度环

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/ced20304-aacc-488d-a471-fd5d9dd1c615.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/83cccd51-9f6c-4e48-849b-a5eae7905a3d.png)

## 常见错误分析

### 数码管 1A 错误

编码器读取错误。当没有连接编码器线，或者编码器协议，配置不对时，会出现该报警，此时需要确认加载的.csv配置文件是否正确，并且检查编码器线有没有接错或者接触不良的情况。

### 数码管 22 错误

电机功率过小错误。一般在使用高压板驱动器驱动功率比较小的电机时，会出现该错误，可以尝试在电机参数中将额定功率和额定电流调大

### 电流反馈与运动方向相反

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/31593b2c-5b1e-4468-a560-d41194a3c9f8.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/d602ecc7-b41e-49b1-aafe-60b6d6c1e2f3.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ldGw7Jw0WOBQN/img/0e3dab7a-786c-452c-a24b-2c05041668d6.png)