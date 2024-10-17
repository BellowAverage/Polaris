
--- 
title:  egg开发环境搭建 
tags: []
categories: [] 

---
### 第一步：下载安装nodejs

下载官方网址： 本人是windows系统因此如图选择：

<img alt="" height="365" src="https://img-blog.csdnimg.cn/d34d3a4ab8e447a18f40177b8b217b00.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_20,color_FFFFFF,t_70,g_se,x_16" width="679">

下载安装十分方便，环境变量也自动配置完成。node

### 

### 第二步：eggjs环境搭配，建立运行项目

（注：nodejs版本最低要求 8.x，且须要LTS 版本） 　egg官方文档网址:**生成项目**： 1.`npm i egg-init -g`<img alt="" height="273" src="https://img-blog.csdnimg.cn/5f0a44e04d44431387e61be7042c9d76.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_20,color_FFFFFF,t_70,g_se,x_16" width="687"> 2. `egg-init egg-example --type=simple`

如果报错，找不到egg-init这个命令，可以将以下目录加到环境变量

<img alt="" height="176" src="https://img-blog.csdnimg.cn/ab0632e562cd4a40b134d198c4c237cf.png" width="290">

而后输入egg-init egg-example --type=simple（egg-example换成你本身要建立的项目名称）

以后设置名字，描述，做者等，想要快速看到效果可一路回车下一步。 3.`cd egg-example` 　cd到新建立的项目目录下 4.`npm i` 　安装项目的依赖：输入 `npm i`

**启动项目：** 　1. `npm run dev 或 npm start`

```
PS F:\Data\eggProject\egg-example&gt; npm start                                                                            npm WARN npm npm does not support Node.js v12.13.0
npm WARN npm You should probably upgrade to a newer version of node as we
npm WARN npm can't make any promises that npm will work with this version.
npm WARN npm Supported releases of Node.js are the latest release of 6, 8, 9, 10, 11.
npm WARN npm You can find the latest version at https://nodejs.org/

&gt; example@1.0.0 start F:\Data\eggProject\egg-example
&gt; egg-scripts start --daemon --title=egg-server-example

[egg-scripts] Starting egg application at F:\Data\eggProject\egg-example
[egg-scripts] Run node --no-deprecation F:\Data\eggProject\egg-example\node_modules\egg-scripts\lib\start-cluster {"title":"egg-server-example","baseDir":"F:\\Data\\eggProject\\egg-example","framework":"F:\\Data\\eggProject\\egg-example\\node_modules\\egg"} --title=egg-server-example
[egg-scripts] Save log file to C:\Users\lex\logs
[egg-scripts] Wait Start: 1...
[egg-scripts] Wait Start: 2...
[egg-scripts] Wait Start: 3...
[egg-scripts] Wait Start: 4...
[egg-scripts] Wait Start: 5...
[egg-scripts] egg started on http://127.0.0.1:7001
PS F:\Data\eggProject\egg-example&gt;    
```

 　2.将图中的网址复制到浏览器中便可看到效果

http://127.0.0.1:7001

<img alt="" height="154" src="https://img-blog.csdnimg.cn/b5360482f7e24d539abf7669619fba54.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBATGV4U2FpbnRz,size_13,color_FFFFFF,t_70,g_se,x_16" width="428">
