
--- 
title:  《信号分析与处理》基于LabVIEW的心音信号的频域分析(数字信号、信号与系统实验、毕业设计、期末大作业) 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/117604640

## Labview心音信号频域分析分析处理



#### 目录
- - <ul><li>- - <ul><li>- - - - - - - - - 


### 1. 实验要求

（1）取一个周期的心音信号，画出它的频谱。

（2）给心音信号加上噪声（单频的正弦波就行），用滤波器去除噪声。画出噪声去除前后的频谱图。

（3）滤波器的种类、截止频率、所加噪声的频率、大小等参数都能输入。

（4）完成最终的GUI界面设计。

### 2. 实验基本原理

#### 2.1 傅里叶变换

<img src="https://img-blog.csdnimg.cn/20210605194909815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="公式">

傅里叶变换就是将一个信号波形分为多个不同频率的余弦波形，成为频率分量。每个频率的余弦波形都有其对应的频率、幅值、相位。如图2.1所示，黑色的是原信号波形，其他颜色的均为频率分量，直线代表该频率分量幅值为0。

<img src="https://img-blog.csdnimg.cn/2021060519494982.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_40,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/20210605195008260.gif#pic_center" alt="在这里插入图片描述">

#### 2.2 低通滤波器

低通滤波(Low-pass filter)是一种过滤方式，规则为低频信号能正常通过，而超过设定临界值的高频信号则被阻隔、减弱。但是阻隔、减弱的幅度则会依据不同的频率以及不同的滤波程序（目的）而改变。它有的时候也被叫做高频去除过滤（high-cut filter）或者最高去除过滤（treble-cut filter)。低通过滤是高通过滤的对立。

低通滤波可以简单的认为：设定一个频率点，当信号频率高于这个频率时不能通过，在数字信号中，这个频率点也就是截止频率，当频域高于这个截止频率时，则全部赋值为0。因为在这一处理过程中，让低频信号全部通过，所以称为低通滤波。

对于高于f0的频率，信号按该频率平方的速率下降。在频率f0处。阻尼值使输出信号衰减。您可以级联多个这样的滤波器部分来得到一个更高阶的（更陡峭的转降）滤波器。

对于不同滤波器而言，每个频率的信号的强弱程度不同。当使用在音频应用时，它有时被称为高频剪切滤波器，或高音消除滤波器。低通滤波器有很多种，其中，最通用的就是巴特沃斯滤波器和切比雪夫滤波器。

切比雪夫滤波器是滤波器的一种设计分类，其采用的是切比雪夫传递函数，也有高通、低通、带通、高阻、带阻等多种滤波器类型。同巴特沃斯滤波器相比，切比雪夫滤波器的过渡带很窄，但内部的幅频特性却很不稳定。

巴特沃斯滤波器是滤波器的一种设计分类，其采用的是巴特沃斯传递函数，有高通、低通、带通、带阻等多种滤波器类型。巴特沃斯滤波器的特点是通频带内的频率响应曲线最大限度平坦，没有起伏，而在阻频带则逐渐下降为零。在振幅的对数对角频率的波得图上，从某一边界角频率开始，振幅随着角频率的增加而逐渐减少，趋向负无穷大。

一阶巴特沃斯滤波器的衰减率为每倍频6分贝，每十倍频20分贝。二阶巴特沃斯滤波器的衰减率为每倍频12分贝，三阶巴特沃斯滤波器的衰减率为每倍频18分贝，如此类推。巴特沃斯滤波器的振幅对角频率单调下降，并且也是唯一的无论阶数、振幅对角频率曲线都保持同样的形状的滤波器。只不过滤波器阶数越高，在阻频带振幅衰减速度越快。其他滤波器高阶的振幅对角频率图和低级数的振幅对角频率有不同的形状。巴特沃斯滤波器在通频带内外都有平稳的幅频特性，但有较长的过渡带，在过渡带上很容易造成失真。

### 3. 实现方法

编程软件：LabView2015

总体设计框图如图3.1所示。

<img src="https://img-blog.csdnimg.cn/20210605195035590.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_30,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

首先是对原信号的处理，画出时域和频域的波形图。接着是噪声的处理，生成符合要求的噪声信号，并添加在原始心音信号上，画出相应的波形图。最后是对添加了噪声的信号进行滤噪处理，恢复出原始信号。另外为了更加直观的判断信号情况，要能够播放这三个状态下的信号。

#### 3.1 原信号处理

下载一段心音的音频文件，通过Audacity软件进行处理，裁取一个周期的波形，并进行频谱分析，得到如图3.2所示的时域波形图和频谱图。

<img src="https://img-blog.csdnimg.cn/20210605195112860.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_50,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

首先要读取本地的.wav音频文件，通过调用"简易读取声音文件"函数来读取前期准备好的一个周期的心音音频文件，程序框图如图3.3所示。输出数据接到显示控件——波形图，得到原始心音信号的时域波形。

接着要对读取的一个周期的心音信号作傅里叶变换得到频域波形，那么调用了"FFT"快速傅里叶变换函数，要输入FFT点数，本实验输入的值为256，输出取绝对值后接到波形图显示，得到原始心音信号的频域波形。 <img src="https://img-blog.csdnimg.cn/20210706144757757.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

#### 3.2 加噪处理

通过labview软件自带的波形生成函数生成一个单频正弦波的噪声加在原心音信号的波形上组合后的信号作为滤波器输入信号。该函数需要输入波的频率、幅值、采样信息等。由于原心音信号是一个较低频的信号，因此设计为其添加一个较高频的单频正弦波噪声信号。本实验设置的单频正弦波的噪声频率为10kHz，幅值为1，采样率为44.1kHz，采样点数为44100。

<img src="https://img-blog.csdnimg.cn/20210706145013418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

#### 3.3 滤波处理

滤波器通过调用波形调理的IIR低通滤波器，本实验选择巴特沃斯低通IIR数字滤波器。

将加有噪声的波形进行波形调理通过巴特沃斯IIR低通滤波器滤除高频的噪声信号，阶数设置为7阶。由图3.2原波形的频谱分析图可以看出波形主要集中在频率为4kHz时，因此设置低截止频率为4kHz。 <img src="https://img-blog.csdnimg.cn/20210706145201601.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">

### 4. 实验结果和讨论

设置好相应的各个参数后，运行程序得到以下实验结果：

#### 4.1 原信号处理结果

如图4.1所示的是原始心音信号读取后画出的波音图，得到y轴幅值在-1-1之间,x轴时间为0-1s。此时可以点击开关1，播放读取到的.wav文件，听到的是正常的心音。

<img src="https://img-blog.csdnimg.cn/20210605195241646.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_50,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

对原心音信号做快速傅里叶变换后取绝对值，画出了如图4.2所示的频域波形图，y轴的幅值为0-0.0093之间，n为256。 <img src="https://img-blog.csdnimg.cn/20210605195249745.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_50,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

#### 4.2 加噪处理结果

通过波形生成函数生成的单频正弦噪声的频域波形图如图4.3所示，为其设置的频率为10kHz，幅值为100m。

<img src="https://img-blog.csdnimg.cn/20210605195312517.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_40,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

在原信号的波形上添加了如图4.3的噪声后得到了如图4.4的信号时域波形图，很明显的是信号频率变大了。此时若点击开关2播放声音，将听到含有刺耳噪音的心音。

<img src="https://img-blog.csdnimg.cn/20210605195322454.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_40,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

#### 4.3 滤波处理结果

对加有噪声的信号通过巴特沃斯IIR低通数字滤波器进行滤波后得到了如图4.5所示的时域波形，与图4.1的原信号对比，几乎没有区别。幅值是在-1-1之间，时间是0-1s。 <img src="https://img-blog.csdnimg.cn/20210605195338511.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_40,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

对滤波后的信号做快速傅里叶变换得到它的频域图。（图4.6）此时可以看出波形的幅值在0-0.000095之间。此时可以点击开关3，将听到和原信号声音几乎无差别的心音。

<img src="https://img-blog.csdnimg.cn/20210605195354279.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_40,color_000ddd,t_70#pic_center" alt="在这里插入图片描述">

### 5. 总结

本次实验是对一个周期内的心音信号作频域分析，心音信号是一段时域的信号，若要得到频域波形，需要通过快速傅里叶变换得到它的频谱图。心音信号是一个较低频的信号，在为其添加一个较高频的单频正弦噪声信号后，再去播放声音就会听到含有刺耳的噪音的心音，那么此时再通过一个低通滤波器滤除掉较高频的噪声，尽可能的恢复原来的心音信号。

## 资料获取

**优先推荐途径一，若遇途径一失效，请再尝试途径二。**

### 途径一

**优先推荐该途径** 第一步：扫描下方二维码，或打开微信搜索并关注“ **2贰进制** ”公众号； 第二步：回复相应内容即可获取本文相关资料。 <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="250" height="250">

### 途径二

**优先推荐途径一，该途径管理可能不能秒回** 扫描下方二维码，加入学习交流QQ群“ **480558240** ”，联系管理员获取包括但不限于本篇内容的更多学习资料。 <img src="https://img-blog.csdnimg.cn/2020071217121655.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="300" height="300"> **2贰进制–Echo 2020年12月** 我认同兴趣是最好的老师，如果您觉得本文还不错，请点赞＋评论＋收藏，要是关注，更是是我前进的动力！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来给予我更大支持： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250"> 此致 感谢您的阅读、点赞、评论、收藏与打赏。
