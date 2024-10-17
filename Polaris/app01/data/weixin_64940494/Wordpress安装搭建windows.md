
--- 
title:  Wordpress安装搭建windows 
tags: []
categories: [] 

---
        WordPress 是用PHP语言开发的博客平台，用户可以用它来搭建属于自己的门户网站和品牌网站，也可以把它当作一个CMS（内容管理系统）来使用。

        WordPress 的特点是功能强大、扩展性强，有很好的seo搜索引擎，可以切换多种主题，也可以自定义主题，WordPress 的社区用户也很多，社区活跃度高。

        这里我们介绍一下WordPress 在本地的搭建。

 一、下载安装包

        进入到WordPress的 ，如图可以看到目前最新的版本为 6.0.2。

<img alt="" height="240" src="https://img-blog.csdnimg.cn/12ac422e679341b4a6c375b3fb3689a3.png" width="468">

同时往下还描述了推荐的运行环境

<img alt="" height="462" src="https://img-blog.csdnimg.cn/a9c99c038f0b4f33ad85cd8003d86784.png" width="1052">

因为WordPress是用PHP编写的所以本地需要安装好PHP的运行环境，这里我就不做介绍。

下载完安装包后进行解压，解压完成之后把解压后的文件放在PHP环境的目录下。

这里我的PHP环境目录在 F:/wordpress

二、安装

在浏览器上输入localhost,上面我提到我的localhost指向的是F:/wordpress目录下。

<img alt="" height="603" src="https://img-blog.csdnimg.cn/3ccf9122496243118638ed05bfefed19.png" width="844">

点击现在开始按钮,进入到数据库配置，这里我也是本地安装的数据库，同时新建了一个mywordpress的数据库。 

<img alt="" height="558" src="https://img-blog.csdnimg.cn/6fe49651c3f04e1b941ea27c58bfb84b.png" width="866">

 提交完成后，进入到站点安装步骤,填写站点的相关信息，点击安装WordPress按钮进行安装。

<img alt="" height="637" src="https://img-blog.csdnimg.cn/aa596ed76d444cc6b48b31bfb6d59636.png" width="764">

安装完成后，可以点击登录到后台。

<img alt="" height="472" src="https://img-blog.csdnimg.cn/4a69007aa4554e69bc08b32fb1e31464.png" width="867">

登录成功后可以进入到wordpress后台。

<img alt="" height="551" src="https://img-blog.csdnimg.cn/d48e937a59934869a1ab066aa375d149.png" width="1200"> 访问站点前台，在浏览器中输入localhost,因为这里是本地安装所以没有用域名，如果是真实环境的化需要域名解析完，输入域名就可以访问了。

<img alt="" height="492" src="https://img-blog.csdnimg.cn/7c6ce6c89cf245eaa1fba81f5f48b324.png" width="1200">

 这样前后台都可以访问成功，本地的安装也算正式完成。






