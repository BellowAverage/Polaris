
--- 
title:  Linux之libreoffice安装 
tags: []
categories: [] 

---
## 一、libreoffice简介

  LibreOffice 是一款开放源代码的自由免费全能办公软件，可运行于 Microsoft Windows, GNU/Linux 以及 macOS 等操作系统上。它包含了 Writer, Calc, Impress, Draw, Math 以及 Base 等组件，可分别用于文本文档、电子表格、幻灯片演示文稿、绘图文档、数学公式编辑、数据库管理等工作。LibreOffice 支持各种文档格式。除了它原生支持的开放文档格式 (OpenDocument Format, ODF) 外，它还支持许多的非开放格式，比如微软的 Microsoft® Word, Excel, PowerPoint 以及 Publisher 的格式等。   LibreOffice和OpenOffice是两个开源办公软件套件，都是基于同一个代码库（原始的OpenOffice.org项目）开发的。在2010年，由于对OpenOffice.org的管理和发展方向不满意，一些开发者分离出了LibreOffice项目，成立了The Document Foundation（TDF）来管理该项目。因此，LibreOffice和OpenOffice之间存在很大的相似性和互相借鉴，但它们是由不同的组织和开发者团队维护和发展的。目前LibreOffice已经成为了开源办公软件领域的主要代表之一，而OpenOffice则已经逐渐退出了主流市场。博文是在centos7.9操作系统下安装libreoffice为例进行试验。

## 二、安装方式——YUM安装

### 1、yum安装libreoffice

>  
 [root@s178 opt]# yum install -y libreoffice … Installed: autocorr-zh.noarch 1:5.3.6.1-25.el7_9 libreoffice.x86_64 1:5.3.6.1-25.el7_9 libreoffice-langpack-zh-Hans.x86_64 1:5.3.6.1-25.el7_9 … 


### 2、版本验证

>  
 [root@s178 opt]# libreoffice --version LibreOffice 5.3.6.1 30(Build:1) 


## 三、安装方式——rpm包安装

### 1、下载软件包

  我们登录，根据操作系统环境选择对应的软件包，我们需要下载主程序包、中文语言支持包、帮助手册软件包，将压缩包下载到/opt目录下。 <img src="https://img-blog.csdnimg.cn/7184a74f7fd64e11af557b2ece96bf52.png" alt="在这里插入图片描述">

>  
 [root@s178 opt]# wget https://download.documentfoundation.org/libreoffice/stable/7.5.4/rpm/x86_64/LibreOffice_7.5.4_Linux_x86-64_rpm.tar.gz [root@s178 opt]# wget https://download.documentfoundation.org/libreoffice/stable/7.5.4/rpm/x86_64/LibreOffice_7.5.4_Linux_x86-64_rpm_langpack_zh-CN.tar.gz [root@s178 opt]# wget https://download.documentfoundation.org/libreoffice/stable/7.5.4/rpm/x86_64/LibreOffice_7.5.4_Linux_x86-64_rpm_helppack_zh-CN.tar.gz [root@s178 opt]# ll total 233696 -rw-r–r–. 1 root root 3116300 Jun 2 21:37 LibreOffice_7.5.4_Linux_x86-64_rpm_helppack_zh-CN.tar.gz -rw-r–r–. 1 root root 915283 Jun 2 21:37 LibreOffice_7.5.4_Linux_x86-64_rpm_langpack_zh-CN.tar.gz -rw-r–r–. 1 root root 235265947 Jun 2 21:37 LibreOffice_7.5.4_Linux_x86-64_rpm.tar.gz 


### 2、安装主程序软件包

  将下载的主程序软件包解压后使用rpm方式安装，可以使用*.rpm通配符的方式安装RPMS目录下的所有RPM包。安装完成后就会生成/opt/libreoffice7.5/目录，就是libreoffice7.5软件的实际安装目录。

>  
 [root@s178 opt]# tar -zxvf LibreOffice_7.5.4_Linux_x86-64_rpm.tar.gz [root@s178 opt]# cd LibreOffice_7.5.4.2_Linux_x86-64_rpm/RPMS/ [root@s178 RPMS]# rpm -ivh *.rpm … 42:libreoffice7.5-freedesktop-menus-################################# [100%] /bin/update-desktop-database /bin/update-mime-database /bin/gtk-update-icon-cache /bin/update-desktop-database /bin/update-desktop-database 


### 3、安装中文语言包

  安装中文语言包中的所有rpm包。

>  
 [root@s178 opt]# tar -zxvf LibreOffice_7.5.4_Linux_x86-64_rpm_langpack_zh-CN.tar.gz [root@s178 opt]# cd LibreOffice_7.5.4.2_Linux_x86-64_rpm_langpack_zh-CN/RPMS/ [root@s178 RPMS]# rpm -ivh *.rpm Preparing… ################################# [100%] Updating / installing… 1:libobasis7.5-zh-CN-7.5.4.2-2 ################################# [ 50%] 2:libreoffice7.5-zh-CN-7.5.4.2-2 ################################# [100%] 


### 4、安装中文离线帮助rpm包

  安装中文离线帮助文件中的所有rpm包。

>  
 [root@s178 opt]# tar -zxvf LibreOffice_7.5.4_Linux_x86-64_rpm_helppack_zh-CN.tar.gz [root@s178 opt]# cd LibreOffice_7.5.4.2_Linux_x86-64_rpm_helppack_zh-CN/RPMS/ [root@s178 RPMS]# rpm -ivh *.rpm Preparing… ################################# [100%] Updating / installing… 1:libobasis7.5-zh-CN-help-7.5.4.2-2################################# [100%] 


### 5、版本验证

>  
 [root@s178 RPMS]# libreoffice7.5 --version LibreOffice 7.5.4.2 36ccfdc35048b057fd9854c757a8b67ec53977b6 


## 四、libreoffice使用简介

### 1、查看libreoffice7.5命令

  查看libreoffice7.5命令我们可以发现这个命令是软连接到了soffice命令上，实际上libreoffice和openoffice都是基于openoffice.org项目开发的，可以理解libreoffice是openoffice的更新迭代版本。 <img src="https://img-blog.csdnimg.cn/6cc7594341b646258df8b53ea10394b7.png" alt="在这里插入图片描述">

### 2、开启接口服务

  同openoffice一样，我们可以使用相同的参数开启soffice服务，用于word转换为pdf的服务。 <img src="https://img-blog.csdnimg.cn/3446d67d83004b75a9eff4a69dc91dd0.png" alt="在这里插入图片描述">

### 3、命令方式word转PDF

  因为libreoffice一直保持持续的更新，不仅支持doc文档，也支持docx格式。 <img src="https://img-blog.csdnimg.cn/41662c7dbd974f5d9843eceb3577ccf0.png" alt="在这里插入图片描述">

>  
 [root@s178 tmp]# libreoffice7.5 --headless --convert-to pdf w20230618.doc convert /tmp/w20230618.doc -&gt; /tmp/w20230618.pdf using filter : writer_pdf_Export [root@s178 tmp]# libreoffice7.5 --headless --convert-to pdf 添加进程监控的方法.docx convert /tmp/添加进程监控的方法.docx -&gt; /tmp/添加进程监控的方法.pdf using filter : writer_pdf_Export 


### 4、批量word转PDF

>  
 [root@s178 tmp]# libreoffice7.5 --headless --convert-to pdf *.doc --outdir /tmp/test 

