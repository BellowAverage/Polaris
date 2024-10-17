
--- 
title:  关于TI杯全国大学生电子设计竞赛 
tags: []
categories: [] 

---
CSDN话题挑战赛第1期

活动详情地址：https://marketing.csdn.net/p/bb5081d88a77db8d6ef45bb7b6ef3d7f

参赛话题：大学生竞赛指南



#### 本文目录
- - <ul><li>- <ul><li>- - - - <ul><li>- - - - - <ul><li>- 


## *实现2020年TI杯大学生电子设计竞赛F题简易无接触温度测量与身份识别装置的竞赛历程

### 1. 大赛组委会官方题目内容

：https://pan.baidu.com/s/1bdThaceiFNxGpfXNcrDOcA 提取码：amjh

2020年TI杯大学生电子设计竞赛赛题公示——F题简易无接触温度测量与身份识别装置 (https://www.nuedc-training.com.cn/index/news/details/new_id/227)

#### 1.1 设计任务

设计并制作一个简易<mark>无接触</mark>温度测量与<mark>身份识别</mark>装置，该装置包括无接触温度测量模块、身份识别模块、处理器模块和电源等，装置组成框图如下图 所示。 装置中无接触*温度测量模块可以无接触测量人体体温和容器中液态水的温度。测试时，应有<mark>光标指示被测点</mark>，当被测温度超过设定值时，应有<mark>报警功能</mark>；身份识别模块负责辨别被测人身份、是否符合防疫要求（如佩戴口罩）等。 <img src="https://img-blog.csdnimg.cn/20201029192931937.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="框图">

#### 1.2 设计要求

1.非接触温度测量：测试距离 1cm~4cm测量误差绝对值± 2℃ 。（30 分）

2.温度测量范围：28℃ ~48℃，并具有温度超标<mark>报警功能</mark> 。报警温度<mark>阈值</mark>在 30℃ ~46℃范围内<mark>可设置</mark>，报警方式自定。（15 分）

3.身份识别：被测人身份识别和身份不符报警功能。（20 分）

4.被测人是否符合防疫要求（如佩戴口罩）的判别功能。（10 分）

5.现场被测人身份特征学习与身份识别功能，学习时间＜10 分钟。（20 分）

6.其他（5 分）

7.设计报告（20 分）

#### 1.3 说明

（1） 该装置不能采用市售产品，否则无分。作品<mark>不能使用 PC 机</mark>，且测试中<mark>不能借助网络</mark>资源。 （2） 温度测量项。该装置的测量温度范围将超出<mark>人体温度</mark>范围，测试对象为现场人员和装在容器中的<mark>液态水</mark>，并采用相应标准温度测量设备作为测量误差对比装置。温度测量功能评测时，测量误差以作品测量数据与标准温度测量装置测量数据之差为准。作品测试时，参赛学生<mark>可自带容器和标准温度测量设备</mark>。 （3） 距离测量项。选作品测量误差对应的测试点，测量起始距离在 1cm~4cm 之间任选，在<mark>保持其误差水平的基础上，距离越远越好</mark>。 （4） 身份识别功能项。识别对象为参赛队 3 名队员，识别方法采用<mark>面部识别</mark>，识别结果可自选方式表示。 （5） 要求（4）可仅判断被测人<mark>是否符合佩戴口罩</mark>的防疫要求。 （6） 要求（5）在测量现场的准备阶段完成学习过程，学习对象为<mark>现场的工作人员</mark>，要求经过现场学习，能准确识别学习对象的身份。

### 2. 题目分析

仔细阅读题目要求和装置组成框图，捕捉到的关键功能信息有：
1. 无接触测量温度1. 身份识别1. 防疫要求：口罩检测、温度正常1. 光标指示1. 阈值可调1. 报警1. 现场学习
那么综合上述总结一下大体是有如下三个模块功能：
1. 无接触测量温度并有光标指示测温位置1. 身份识别和是否佩戴口罩的检测，且具有现场学习功能1. 对不符合防疫要求的会有报警，且温度报警阈值是可以设置的
### 3. 方案设计

#### 3.1 关键技术路线

首先来分析一下个人认为是最难的部分身份识别和口罩检测，对于这部分功能要求必然少不了要使用摄像头，检测识别常见的方案无非有两种：
1. OpenMV1. OpenCV
##### 3.1.1 openmv+STM32/MSP430+C

那么沿着识别检测的思路往下就是选择处理器，如果使用openmv，那么肯定还需要一块主控制器完成其他模块的设计任务。常见的是意法半导体STM32系列的或者德州仪器MSP430系列再或者Arduino系列的，这些控制器与openmv大概率是需要使用C或者C++来进行编程。除此之外虽然星瞳科技openmv新系列支持了MicroPython编程但是价格不菲！而经费有限，同时电赛又是有时间紧任务重的特点，用上述两种语言编程必然需要花费大量的时间，如果对STM32或者MSP430或者openmv还不是很熟悉的，那更是难上加难。 至此openmv的方案可作为暂定预备方案，如果是前期对openmv已经有学习或者有经验的同学是可以考虑该方案的。 那么再来分析一下另一种方案。

##### 3.1.2 opencv+树莓派+python

如果使用opencv，那最好的处理器方案是选择树莓派（），虽然题目要求不能使用PC机和网络资源，但是树莓派严格意义上又不能算是PC机，最终为了确保可以使用树莓派，报请大赛组委会询问，得到的结果是没有说不能用那就是能用，所以树莓派作为处理器的方案敲定！即便是在不能使用网络资源的情况下（如果再可以使用网络资源那简直就太过分了），opencv也足够完成身份识别和口罩检测的任务。至此已经确定了处理器模块，利用opencv则可以使用通用的免驱USB摄像头或者树莓派官方的CSI摄像头作为图像传感器即可。

#### 3.2 温度测量

在前期发布的中已经明确了有两类温度传感器，红外传感器和LMT70。结合疫情的原因有两道测温的题目也不是不可能。

清单链接：https://pan.baidu.com/s/1HLZuZAxHGkiBH4EYeomeXg 提取码：70tp

题目要求无接触测量温度，基本限制了温度传感器的原理只能是红外，其他传统的接触式传感器皆不可使用。赛前准备的LMT70也只得闲置。赛题发布后两小时重新下单选购了红外热电堆温度传感器。

#### 3.3 人机交互

人机交互两种可选择方案： 1、显示屏、HDMI转接板、键盘、鼠标、按键 2、显示触摸屏、按键

#### 3.4 报警与激光指示

蜂鸣器与激光头

### 4 实现效果

<img src="https://img-blog.csdnimg.cn/70675ecc4e7b4d0592398d869fc2289c.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_50,color_222FFF,t_70#pic_center" alt="封箱照片" width="300" height="320">

省级一等奖

## *干货获取

### **训练口罩检测分类器

训练口罩检测分类器的**步骤**、**正负样本数据集**以及训练好的**口罩检测分类器**等资源已经在另一篇文章中总结，详见下面地址：  文章地址： 

### **代码

`部分Python代码`

```
 # 采集


 # 训练
 
 
 # 识别
 
 
 # 检测
 
 
 # 测温



```

### **硬件类资料

#### ***树莓派资料

#### ***温度测量模块资料

（等待更新）

**2贰进制–Echo 2020年10月** 如果您觉得本文还不错，请点赞＋评论＋收藏，要是关注那更是我前进的动力！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

如果您需要本文的相关资料或者其它意见与建议，可通过下面方式联系：

扫描下方二维码，加入 2贰进制 学习交流QQ群“ **480558240** ”，下载群文件或者联系管理员咨询。 <img src="https://img-blog.csdnimg.cn/20210501161747688.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="QQ群" width="250" height="300">

也可扫描下方二维码，或打开微信搜索并关注“ **2贰进制** ”公众号，回复：“ **2020电赛F题** ”； <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="200" height="200">

本文未完待续。。。

CSDN话题挑战赛第1期

活动详情地址：https://marketing.csdn.net/p/bb5081d88a77db8d6ef45bb7b6ef3d7f
