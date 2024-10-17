
--- 
title:  idea设置-个人笔记 
tags: []
categories: [] 

---
### 运行项目出现无符号问题
1. 添加jvm的配置（也可以解决java: 找不到符号 问题）
```
-Djps.track.ap.dependencies=false

```

**贴图：** <img src="https://img-blog.csdnimg.cn/cf044338843b485690830c3ea427f2d5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 2. 如果是编码问题的话 <img src="https://img-blog.csdnimg.cn/9791e708be24462b95d05738ebe14594.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCY5Y-26aOO5YeM,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 忽略大小写

<img src="https://img-blog.csdnimg.cn/558fbd256c5e42cfa2bd4a4c2be467d9.png" alt="在这里插入图片描述">

### 代码太长，自动换行

<img src="https://img-blog.csdnimg.cn/32b2760254344c27be388ed0d52572a3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/6088974beb9a48fc8fd0c5d57940d2a3.png" alt="在这里插入图片描述">

### 编译出现问题

>  
 如果出现这种报错： `javac &lt;options&gt; &lt;source files&gt;` 是因为编译的文件编码不一致导致的。 


**解决办法**

```
-DarchetypeCatalog=internal -Dfile.encoding=GBK

```

<img src="https://img-blog.csdnimg.cn/af0855050afc4b7d942125af0dc8d1e3.png" alt="在这里插入图片描述"> 这样就解决了

### sql使用#参数的设置

>  
 英文的搜这个 


```
User Parameters

```

>  
 中文的看如下图： 


<img src="https://img-blog.csdnimg.cn/3029a080e923406da5a57621c76be760.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/440b9d58526d411fab2ef625550e8845.png" alt="在这里插入图片描述">

>  
 代码 


```
#\{<!-- -->([^\{<!-- -->\}]*)\}

```

>  
 使用效果 


<img src="https://img-blog.csdnimg.cn/0723d8ba9e56481d8d6662c2ced8b619.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/50e1d47bf70a49a6a2cc5f63fc18a4cf.png" alt="在这里插入图片描述">
