
--- 
title:  【单片机】51单片机入门教程中（LED流水灯） 
tags: []
categories: [] 

---
>  
 ✌ 作者简介：盐焗小星球_wyb，一名在读的电子信息工程专业大学生. 📑 个人主页： 📫 如果文章知识点有错误的地方，请指正！和大家一起学习，一起进步👀 🔥 如果感觉博主的文章还不错的话，还请不吝👍关注、点赞、收藏三连支持👍一下博主哦！ 我一直在写一篇初学者最快入门的文章，希望大家能以最快的速度掌握51单片机！（后续文章会更新） 




#### 学习目录
- - - <ul><li>- <ul><li>- - - - - 


## 前言

`提示：以下是本篇文章前言内容`

在大家学习用点亮LED之前希望大家去复习一下51单片机的**最小系统**！



**大家需要了解一下进制转换，如下图：** 1.十进制： 都是以0-9这九个数字组成，不能以0开头。 2.二进制： 由0和1两个数字组成。 3.八进制： 由0-7数字组成，为了区分与其他进制的数字区别，开头都是以0开始。 4.十六进制：由0-9和A-F组成。为了区分于其他数字的区别，开头都是以0x开始。 <img src="https://img-blog.csdnimg.cn/f9eaaecd4ac04b47a40698fed22ba1c4.png#pic_center" alt="在这里插入图片描述">

## 正文

`提示：以下是本篇文章正文内容`

### 一、了解LED的工作原理

简单的理解一下：发光二极管与普通二极管一样是由一个PN结组成，也具有单向导电性。**当给发光二极管加上正向电压后，从P区注入到N区的空穴和由N区注入到P区的电子，在PN结附近数微米内分别与N区的电子和P区的空穴复合，产生自发辐射的荧光**。常用的是发红光、绿光或黄光的二极管。发光二极管的反向击穿电压大于5伏。它的正向伏安特性曲线很陡，使用时必须串联限流电阻以控制通过二极管的电流。

实物图如下： <img src="https://img-blog.csdnimg.cn/318c3b329260449da3de4ae670310aa7.png#pic_center" alt="在这里插入图片描述"> 电路原理图如下：

<img src="https://img-blog.csdnimg.cn/16a4a9837ce44e9f8f37cabe8b554ce7.png#pic_center" alt="在这里插入图片描述">

#### 如何计算发光二极管电压

发光二极管的压降是比较固定的，通常红色为1.6V左右，绿色有2V和3V两种，黄色和橙色约为2.2V，蓝色为3.2V左右。对于常用的几毫米大小的二极管，其工作电流一般在2毫安至20毫安之间，电流越大亮度越高，用电源电压减去二极管的压降，再除以设定的工作电流，就得出限流电阻的阻值

串联R＝（U－LED压降）／设定的工作电流

简单了解一下即可，如果想深入了解的话可以学学《模拟电路》，第一章就是讲的二极管，在这里就不过多赘述了！

### 二、用Proteus画原理图

#### 共阴接法：

<img src="https://img-blog.csdnimg.cn/6512e0010fe14fa0bc4957926c3b007d.png#pic_center" alt="在这里插入图片描述">

#### 共阳接法：

<img src="https://img-blog.csdnimg.cn/4404467fec924d38a97c5c10b0c9420c.bmp#pic_center" alt="在这里插入图片描述">

### 三、用Keil写代码

#### 方法一：点亮流水灯-位操作（共阴）

```
#include &lt;REGX51.H&gt;

sbit led1=P1^0;
sbit led2=P1^1;
sbit led3=P1^2;
sbit led4=P1^3;
sbit led5=P1^4;
sbit led6=P1^5;
sbit led7=P1^6;
sbit led8=P1^7;

void Delay500ms();

void main()
{<!-- -->
	while(1)
	{<!-- -->
		P1=0x00;
		led1=1;
		Delay500ms();
		led1=0;
		Delay500ms();
		led2=1;
		Delay500ms();
		led2=0;
		Delay500ms();
		led3=1;
		Delay500ms();
		led3=0;
		Delay500ms();
		led4=1;
		Delay500ms();
		led4=0;
		Delay500ms();
		led5=1;
		Delay500ms();
		led5=0;
		Delay500ms();
		led6=1;
		Delay500ms();
		led6=0;
		Delay500ms();
		led7=1;
		Delay500ms();
		led7=0;
		Delay500ms();
		led8=1;
		Delay500ms();
		led8=0;
		Delay500ms();
		
		led8=1;
		Delay500ms();
		led8=0;
		Delay500ms();
		led7=1;
		Delay500ms();
		led7=0;
		Delay500ms();
		led6=1;
		Delay500ms();
		led6=0;
		Delay500ms();
		led5=1;
		Delay500ms();
		led5=0;
		Delay500ms();
		led4=1;
		Delay500ms();
		led4=0;
		Delay500ms();
		led3=1;
		Delay500ms();
		led3=0;
		Delay500ms();
		led2=1;
		Delay500ms();
		led2=0;
		Delay500ms();
		led1=1;
		Delay500ms();
		led1=0;
		Delay500ms();
	}
}


void Delay500ms()		//@11.0592MHz
{<!-- -->
	unsigned char i, j, k;
	i = 4;
	j = 129;
	k = 119;
	do
	{<!-- -->
		do
		{<!-- -->
			while (--k);
		} while (--j);
	} while (--i);
}


```

#### 方法二：点亮流水灯-左移右移（共阴）

```
#include &lt;REGX51.H&gt;
void Delay100ms();

unsigned char  i=0;

//主函数
void main()
{<!-- -->
	while(1)
	{<!-- -->
		//for循环让Led依次点亮
		for(i=0;i&lt;8;i++)
		{<!-- -->
			P1=~(0x01&lt;&lt;i);
			Delay100ms();
		}
	}
}

//100ms的延时函数
void Delay100ms()		//@11.0592MHz
{<!-- -->
	unsigned char i, j;

	i = 180;
	j = 73;
	do
	{<!-- -->
		while (--j);
	} while (--i);
}


```

#### 方法三：点亮流水灯-用数组点亮（共阴）

```
#include &lt;REGX51.H&gt;
#define uchar unsigned char
uchar tab[]={<!-- -->0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f,
							0xbf,0xdf,0xef,0xf7,0xfb,0xfd,0xfe,0xff};
uchar tab1[]={<!-- -->0xfe,0xfc,0xf8,0xf0,0xe0,0xc0,0x80,0x00,
							0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff};

void delay();
void main()
{<!-- -->
	uchar i;
	while(1)
	{<!-- -->
		for(i=0;i&lt;16;i++)
		{<!-- -->
			P1=tab1[i];
			delay();
		}
	}
}

void delay()
{<!-- -->
	uchar i,j;
	for(i=0;i&lt;255;i++)
		for(j=0;j&lt;255;j++);
}


```

### 四、下载代码

**双击芯片，然后会弹出如下界面，然后点击黄色文件夹** <img src="https://img-blog.csdnimg.cn/5bda8ce936904f09985cd3ce3226b526.bmp#pic_center" alt="在这里插入图片描述"> **找到刚刚编译完生成的hex文件** <img src="https://img-blog.csdnimg.cn/07536396f7dd449c92cc7ab0a0e9f2a4.bmp#pic_center" alt="在这里插入图片描述"> **选择OK就可以了！** <img src="https://img-blog.csdnimg.cn/fe5c9148223c48df8b3a82388ec7e36f.bmp#pic_center" alt="在这里插入图片描述"> 然后点击左下角的蓝色三角就可以开始运行程序了

<img src="https://img-blog.csdnimg.cn/4f85bc0ef1f64949a152f6c7e5f7c129.bmp#pic_center" alt="在这里插入图片描述">

### 五、调试代码

在写代码的时候需要不停的调试，直到能实现自己想要的现象！

## 总结

那么今天的知识点就先到这里吧 如果觉得博主的这篇文章不错的话麻烦给博主一个三连。你的三连就是对我最大的支持。这句话感觉好耳熟啊(doge)
