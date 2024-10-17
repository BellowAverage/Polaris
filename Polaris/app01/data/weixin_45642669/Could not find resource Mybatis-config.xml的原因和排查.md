
--- 
title:  Could not find resource Mybatis-config.xml的原因和排查 
tags: []
categories: [] 

---
花了大概20分钟，一个很简单的知识点，记录一下。

## 故障定位

写入到目录里面Mybatis-config.xml报错Could not find resource Mybatis-config.xml。

配置文件位置： <img src="https://img-blog.csdnimg.cn/9e03b7a366dc415085ea26d1f8ac0242.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_14,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">代码： <img src="https://img-blog.csdnimg.cn/c564936062e64ce89f9992c23ca0c7b3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">xml文件：

```
&lt;?xml version="1.0" encoding="UTF-8" ?&gt;
&lt;!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd"&gt;
&lt;configuration&gt;
    &lt;environments default="text"&gt;
        &lt;environment id="text"&gt;
            &lt;transactionManager type="JDBC"/&gt;
            &lt;dataSource type="POOLED"&gt;
                &lt;property name="driver" value="com.mysql.jdbc.Driver"/&gt;
                &lt;property name="url" value="jdbc:mysql://localhost:3306"/&gt;
                &lt;property name="username" value="root"/&gt;
                &lt;property name="password" value="123456"/&gt;
            &lt;/dataSource&gt;
        &lt;/environment&gt;
    &lt;/environments&gt;
&lt;/configuration&gt;

```

提示： <img src="https://img-blog.csdnimg.cn/ddd8b3a0907749a5875786ad6a828628.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 解决问题

idea只会扫描配置文件夹里面的配置。也就是文件夹左边有黄色块的作为资源根 放到src里面没有用、放在根目录没有用，最后放在resources文件夹中立刻生效了。 <img src="https://img-blog.csdnimg.cn/d1869dcfe8f54fa1b2decf9919e92b08.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_15,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">把配置文件写入。

<img src="https://img-blog.csdnimg.cn/190836c5b2fd4c1a8f27f183a510cf8b.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/8ab4c429a3a148ba90040373a135bd82.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 成功解决。

## 添加资源根

如果已经有resource，那么加入resource。如果不是resource或者自定义了一个文件夹作为配置文件那么需要将其改名为资源根即可扫描。 <img src="https://img-blog.csdnimg.cn/576f1eec05b647bd8abed7fce670fa83.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6Z2S56Kn5Yed6Zyc,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 使用maven进行管理

除了java文件以外，其他所有的文件都不会进入源代码。 想要进入源代码的时候，需要添加到pom.xml文件也可以实现和加入资源根一样的效果

在pom.xml加入下面几行：

```
&lt;build&gt;
   &lt;resources&gt;
       &lt;resource&gt;
           &lt;directory&gt;src/main/java&lt;/directory&gt;
           &lt;includes&gt;
               &lt;include&gt;**/*.xml&lt;/include&gt;
               &lt;include&gt;**/*.yaml&lt;/include&gt;
           &lt;/includes&gt;
           &lt;filtering&gt;false&lt;/filtering&gt;
       &lt;/resource&gt;
       &lt;resource&gt;
           &lt;directory&gt;src/main/resources&lt;/directory&gt;
           &lt;includes&gt;
               &lt;include&gt;**/*.*&lt;/include&gt;
           &lt;/includes&gt;
           &lt;filtering&gt;false&lt;/filtering&gt;
       &lt;/resource&gt;
   &lt;/resources&gt;
&lt;/build&gt;

```

一个简单的问题，记录一下。
