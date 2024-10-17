
--- 
title:  Java中web的css、js、img等静态资源引入详细操作教程 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：Java中web的css、js、img等静态资源引入详细操作教程 日期：2024年2月27日 作者：任聪聪 


## java中web单体项目静态资源webjar引入形式说明

说明：通过webjar进行静态资源的导入，使用maven进行版本的管理。

### 步骤一、打开webjar

地址：https://www.webjars.org/ <img src="https://img-blog.csdnimg.cn/direct/964ffd12e0ba4300b40db4a85c357ae5.png" alt="https://www.webjars.org/">

### 步骤二、搜索layui，如下图：

<img src="https://img-blog.csdnimg.cn/direct/9bfec2476ab942b497d56670b906589b.png" alt="在这里插入图片描述">

## 步骤三、配置maven，并安装，引入静态资源

<img src="https://img-blog.csdnimg.cn/direct/7ed79b18e989408db2b3e8d0e423fa2c.png" alt="在这里插入图片描述"> 使用`mvn install`进行安装，安装完毕后即可进行引入，将如下的代码写入到自己的html中即可。

```
&lt;link rel="stylesheet" href="/webjars/xxxxxx.css"&gt;

```

## java中web单体项目静态资源默认引入新式说明

### 支持目录说明

```
resources/resources 存放静态资源
resources/static 
resources/public
resources/

```

### 引入方式

诸如如下类型即可，无需带上static、public等。

```
/lib/js/jquery3.2.0.min.js

```
