
--- 
title:  记录下oom排查配置和工具 
tags: []
categories: [] 

---
今天刚接触的，记录一下。

## 配置IDEA

我用的是最新2021版本的idea。需要在Jvm里面写入参数： <img src="https://img-blog.csdnimg.cn/9c66ead012b042c291bdcc434cde2acb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 默认是没有VM的，需要配置一下才有VM参数。 <img src="https://img-blog.csdnimg.cn/310c3836f948443ba6b44949e707a5ce.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6b85f83eb5944eb9816e811720eb1110.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 输入参数即可进行调整。 记录了3个参数：

```
-Xms1000m
-Xmx1000m
-XX:+HeapDumpOnOutOfMemoryError参数表示当JVM发生OOM时，自动生成DUMP文件

```

第一个参数：-Xms1000M的意思是：正常开启1000M的内存。（默认值似乎是系统的64分之一） 第二个参数：-Xms1000M的意思是：最大开启1000M的内存，如果超过则OOM（默认是内存的四分之一） 第三个参数，意思是当JVM发生OOM时，自动生成DUMP文件。

## 查看JVM内存

```
        long i = Runtime.getRuntime().maxMemory();
        System.out.println(i / 1024 / 1024);

```

<img src="https://img-blog.csdnimg.cn/31a520982c844dfaa62fa2134f043624.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这个代码的意思是：查询系统的最大内存，由于是字节，所以直接除以两个1024即为MB内存占用。

默认内存是 ****totoalMemory****，其余的都差不多，直接看iDE即可：

<img src="https://img-blog.csdnimg.cn/4202eac9ac314207a6be35abe2d0c5c5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 查看dump日志

当加入-XX:+HeapDumpOnOutOfMemoryError时，oom会生成dump文件，对dump文件进行分析即可。

我写个代码让内存溢出 <img src="https://img-blog.csdnimg.cn/77e3591ab387400ba822ede2dd1d279d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 报错不是OOM了，而是heap <img src="https://img-blog.csdnimg.cn/d22afd8473fb4799a7e0ad6f129b385b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 也会在系统目录下生成对应的分析文件 <img src="https://img-blog.csdnimg.cn/adc2317cd6e64d4d951b3a7eb5783693.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这个dump文件可以用很多工具进行分析，我用的是别人推荐的Jprofiler。

<img src="https://img-blog.csdnimg.cn/635a5c808e7b4f219863b5df865dfa7c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 这个可以看代码的内存占用。

调优我自己暂时不会，只是记录一下oom工具的使用即可。
