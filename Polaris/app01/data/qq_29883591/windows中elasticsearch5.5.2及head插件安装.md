
--- 
title:  windows中elasticsearch5.5.2及head插件安装 
tags: []
categories: [] 

---
   在安装es5.5.2的head插件过程中，遇到了一些问题，这里做一下分享。

### 安装过程如下：

#### 1、安装elasticsearch5.5.2

（1）首先进入elasticsearch官网进行下载，网址为：，如下所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716162213147?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（2）上图中是es最新版本的下载，其他版本的下载如图中标记所示，点击past releses进行选择，如下所示，然后在列表框进行相应的选择，我这里用的是es5.5.2版本。

<img alt="" class="has" src="https://img-blog.csdn.net/20180716162500553?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（3）点击上图中的Download，进入如下的界面，然后点击ZIP进行下载。

<img alt="" class="has" src="https://img-blog.csdn.net/20180716162858250?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（4）解压下载好的zip安装包到自己设置的位置。

<img alt="" class="has" src="https://img-blog.csdn.net/20180716163058703?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（5）进入到elasticsearch的目录中bin文件夹，双击图中的bat程序启动es，如下所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716163428153?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

<img alt="" class="has" src="https://img-blog.csdn.net/20180716163632844?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（6）至此启动成功，在浏览器中输入：，显示如下图所示的信息则表示成功：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716163942799?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

#### 2、安装head插件

（1）安装node

         <img alt="" class="has" src="https://img-blog.csdn.net/20180716165328652?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70"> 

        <img alt="" class="has" src="https://img-blog.csdn.net/20180716165657998?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">
- 进入node安装的官网，选择图中箭头所指的版本进行下载： <img alt="" class="has" src="https://img-blog.csdn.net/20180716164709802?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">- 双击下载的msi安装文件，然后直接进行安装即可（按照图形化界面进行安装即可，对于文件安装位置进行修改可自行进行修改，其它选项默认即可）。- 对node、npm进行验证：- 使用npm安装grunt：
注：如果在使用npm的时候出现了故障的话，如下所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716170227205?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

错误信息关键字为：Error: Cannot find module 'D:\software2\nodejs\node_modules\npm\bin\npm-cli.js'

解决方法：对于这个错误信息，找了很多解决办法都没有见效，最后再网上找到一个方案是将node安装包卸载后重新安装便可以成功了。

#### 3、安装head插件

（1）在github上找到head插件，如下所示，然后点击Download ZIP进行下载：

<img alt="" class="has" src="https://img-blog.csdn.net/2018071617074244?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（2）将下载好的elasticsearch-head-master.zip安装包解压缩到自己设定的位置。

（3）打开cmd命令窗口，然后进入到head插件的文件夹，执行命令：npm install，如下所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716171210938?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

<img alt="" class="has" src="https://img-blog.csdn.net/20180716171518231?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（4）修改Elasticsearch配置文件，编辑elasticsearch-5.1.1/config/elasticsearch.yml,加入以下内容，：

```
http.cors.enabled: true
http.cors.allow-origin: "*"
```

注意：上面两行的设置中，“：”后面需要有一个空格。

（4）执行命令：npm run start，如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20180716171655579?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

（5）在浏览器中输入网址：，显示如下图所示的界面：

<img alt="" class="has" src="https://img-blog.csdn.net/201807161718439?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70">

注：要想展示如下的界面，首先要先启动es，然后在启动head插件进行连接。

     至此，此次的分享完毕，欢迎交流指正。

 

 

 

 
