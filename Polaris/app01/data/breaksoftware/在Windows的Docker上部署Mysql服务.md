
--- 
title:  在Windows的Docker上部署Mysql服务 
tags: []
categories: [] 

---
在我们做一些和数据库相关的测试时，往往需要快速部署一个数据库作为数据源。如果开发环境是Windows，且开发的代码不依赖于系统，即不用在linux上做开发，则可以将全套环境都部署在Windows上。 本地安装数据库会污染操作系统环境，且后期维护成本都比较高。而使用Windows Docker Desktop去做部署是一个很好的选择。 本文就以Mysql部署为例，讲解操作和验证方法。

## 获取镜像

打开Docker Desktop，在搜索框中检索

>  
 mysql 


<img src="https://img-blog.csdnimg.cn/direct/b9dc3e2e254d4f108c1ec759c74ca808.png" alt="请添加图片描述"> 点击该镜像（Image），此时有一个下载的过程。

## 启动服务

待镜像下载完毕，点击“RUN”，进入配置页面 <img src="https://img-blog.csdnimg.cn/direct/5b568b9b41c6458eb6e28a7ce48685cb.png" alt="请添加图片描述"> 需要注意的是两个端口号和环境变量MYSQL_ROOT_PASSWORD。 端口号指定后，我们就可以在Windows中其他软件上访问数据库。这一步非常重要，很多启动后连不上数据库的情况都是这两项没配置。 MYSQL_ROOT_PASSWORD用于指定root账号的密码。 下图就展现出mysql已经启动成功了。 <img src="https://img-blog.csdnimg.cn/direct/2b7743c1c55a426787ef52fea126b091.png" alt="请添加图片描述">

## 验证

### 容器内部验证

在Exec标签页，我们在容器内部登录

```
mysql -u root -p

```

<img src="https://img-blog.csdnimg.cn/direct/6203ff27598d460e8f20f23958dff852.png" alt="请添加图片描述"> 输入密码，即MYSQL_ROOT_PASSWORD的值，就可以进入控制台。 <img src="https://img-blog.csdnimg.cn/direct/d9125203410847c5b2cddd43d6f6c0e2.png" alt="请添加图片描述">

### 容器外部验证

我们选用vscode的mysql shell插件，它是甲骨文公司的产品，值得信赖。 <img src="https://img-blog.csdnimg.cn/direct/c0379e698c7b49b69f5beb12abebc79e.png" alt="请添加图片描述"> 安装完成后，在右侧窗口下侧有一个证书安装按钮 <img src="https://img-blog.csdnimg.cn/direct/afc7381b81db4015b565e8198e82c1d0.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/7aae2b24924440cda5d336ba44fae2eb.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/direct/197e74554fe64d6dae0fc6be4d208c87.png" alt="请添加图片描述"> 新建一个连接 <img src="https://img-blog.csdnimg.cn/direct/c7d45eee0792468f9a541e709eb3b4f3.png" alt="请添加图片描述"> 然后输入数据库的信息 <img src="https://img-blog.csdnimg.cn/direct/b6e5f970ad864fe7bd5b117c61ce6db2.png" alt="请添加图片描述"> 连接成功后，我们就可以操作数据库了。 <img src="https://img-blog.csdnimg.cn/direct/5f8e687a90904e9b9d3762f0fce295ef.png" alt="请添加图片描述">
