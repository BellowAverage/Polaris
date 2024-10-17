
--- 
title:  yii2框架安装教程windows 
tags: []
categories: [] 

---
Yii是一个基于组件、用于开发大型 Web 应用的 高性能 PHP 框架。采用严格的 OOP 编写，Yii 使用简单，非常灵活，具有很好的可扩展性。

yii2.0框架的安装分两种方式：这里针对windows环境的安装

####   一、通过下载归档文件安装

        1. 先从yii官方网站下载文件，下载地址  。选择basic版本下载。

<img alt="" src="https://img-blog.csdnimg.cn/b9cc15236951492b90da526a274e6712.jpeg">

       2. 下载后解压到配置好的PHP环境目录下，解压后的文件

<img alt="" height="589" src="https://img-blog.csdnimg.cn/1af9999153354cd5bc58f8aacdb3bf6e.png" width="261">

 3. 修改config/web.php 文件，输入cookieValidationKey

<img alt="" height="244" src="https://img-blog.csdnimg.cn/0e64167b725f4d3da1734ddaa8b6a755.png" width="794">

 4. 访问到web/index.php 出现这个页面就成功了

<img alt="" height="489" src="https://img-blog.csdnimg.cn/c95ce5d8ef844603bb9a90e8b73550d2.png" width="1200">

####  二、通过composer安装

         1. 先安装composer,下载安装包 

              点击安装包按照提示安装即可

        2. 通过cmd 命令进入到PHP环境目录下，我这里PHP环境配置在 F:\yiistudy         进入到这个文件下<img alt="" height="126" src="https://img-blog.csdnimg.cn/68939aae561c4ff7ad3b37cf3bc5445e.png" width="444">

         执行以下命令

>  
 <pre>composer create-project --prefer-dist yiisoft/yii2-app-basic basic</pre> 


       <img alt="" height="148" src="https://img-blog.csdnimg.cn/b28f21c158534f74924db03872a35e7c.png" width="961"> 

执行完成后能看到yii的文件，同样访问到web/index.php


