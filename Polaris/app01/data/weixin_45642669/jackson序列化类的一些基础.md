
--- 
title:  jackson序列化类的一些基础 
tags: []
categories: [] 

---
今天刚接触jackson。记录一下。

## 环境准备

现在大多数代码都是用Maven构建，所以直接导入

```
        &lt;dependency&gt;
            &lt;groupId&gt;com.fasterxml.jackson.core&lt;/groupId&gt;
            &lt;artifactId&gt;jackson-databind&lt;/artifactId&gt;
            &lt;version&gt;2.12.1&lt;/version&gt;
        &lt;/dependency&gt;

```

<img src="https://img-blog.csdnimg.cn/7fea7c0b13984b439bf8a0bf42739de5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 写入以后刷新： <img src="https://img-blog.csdnimg.cn/b131ffc8884743e5b954d5225e0d2953.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 刷新一下即可下载对应的依赖包。 即可。

## 序列化类

导入这几个包，听网上的建议是这几个;

```
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;

```

<img src="https://img-blog.csdnimg.cn/4ab1e4042f80440c89decdf9ac41528a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 然后序列化 <img src="https://img-blog.csdnimg.cn/791ea99337be4d1a8b37e181a9517fba.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 序列化成功。 <img src="https://img-blog.csdnimg.cn/81be8a05a51145abbe98394fd900bd54.png" alt="在这里插入图片描述">

#### 序列化失败排除

出现这么一个问题： <img src="https://img-blog.csdnimg.cn/624902e86f4e40b4a7d9697b9966fa5b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">翻译一下，是说没有可序列化的内容……

我自己想要序列化的是一个ListNode类，然后提示是：只要pubulic或者写了get方法才能实现序列化。 <img src="https://img-blog.csdnimg.cn/7682e1de56584a73b2b73f4e4966dd89.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

于是把类的类型转化为public： <img src="https://img-blog.csdnimg.cn/77e1604cd21a456585adb41c8e3a6701.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"><img src="https://img-blog.csdnimg.cn/81be8a05a51145abbe98394fd900bd54.png" alt="在这里插入图片描述"> 问题解决

## 反序列化

<img src="https://img-blog.csdnimg.cn/f40a8d43092e4d7987075c8f26cebde0.png" alt="在这里插入图片描述">

第一个值为传入的String，第二个值是类的反射。即可将字符串转化为类。 <img src="https://img-blog.csdnimg.cn/40447e8780f04c7d83cee64195cdfdaa.png" alt="在这里插入图片描述"> 成功反序列化。

比较简单，记录一下。
