
--- 
title:  maya2022 ubuntu22 安装笔记 
tags: []
categories: [] 

---
**目录**























### ubuntu安装maya2022 官方教程：





sudo apt-get install ./adlmapps23_23.0.21-1_amd64.deb sudo apt-get install ./adlmflexnetserveripv6_23.0.21-1_amd64.deb sudo apt-get install ./adlmflexnetclient_23.0.21-1_amd64.deb

sudo apt-get install ./adsklicensing11.0.0.4854_0-1_amd64.deb

 sudo /opt/Autodesk/AdskLicensing/11.0.0.4854/AdskLicensingService/AdskLicensingService --run

sudo apt-get install ./substance-in-maya-2022_2.2.1-2_amd64.deb

 /opt/Autodesk/AdskLicensing/&lt;version_number&gt;/helper/AdskLicensingInstHelper list

/opt/Autodesk/AdskLicensing/11.0.0.4854/helper/AdskLicensingInstHelper list

 sudo /opt/Autodesk/AdskLicensing/11.0.0.4854/helper/AdskLicensingInstHelper register -pk 657N1 -pv 2022.0.0.F -el EN_US -cf /var/opt/Autodesk/Adlm/Maya2022/MayaConfig.pit

#### 创建脚本 测试启动ok

mkdir -p ~/maya/2022/

touch ~/maya/2022/Maya.env

```
sudo apt remove adsklicensing*
sudo apt remove adlmflexnetclient
sudo apt remove adlmapps*
sudo mv /usr/autodesk/maya2022/bin/ADPClientService /usr/autodesk/maya2022/bin/ADPClientServiceNOTHANKS
```

#### 启动命令

```
sudo /opt/Autodesk/AdskLicensing/11.0.0.4854/AdskLicensingService/AdskLicensingService --run
```

#### this computer does not meet the operating system requirements for autodesk maya 2022







#### 报错filed to load module canberra-gtk-module 解决

udo apt-get install libcanberra-gtk-module libcanberra-gtk3-module



### ubuntu安装maya2020







#### 报错 libssl.so.10: cannot open shared object file: No such file or directory

 wget ftp://rpmfind.net/linux/fedora/linux/releases/16/Everything/x86_64/os/Packages/openssl-1.0.0e-1.fc16.x86_64.rpm rpm -Ivh ./openssl-1.0.0e-1.fc16.x86_64.rpm



### linux系统安装

2020





下载地址：

https://up.autodesk.com/2020/MAYA/18BBDBD5-9A15-4095-8D5E-089938EB8E24/Autodesk_Maya_2020_1_ML_Linux_64bit.tgz 



参考：

1.获取转换 rpm 软件包所需的软件包。

sudo apt-get install alien dpkg-dev debhelper build-essential zlib1g-dev lsb-core libfam0 libcurl4 libpcre16-3 libjpeg62 libxm4 xfonts-100dpi xfonts-75dpi -y 2.获取并安装 libXp6和libpng15。

sudo add-apt-repository ppa:zeehio/libxp  sudo apt-get update  sudo apt-get install libxp6 wget http://ftp.altlinux.org/pub/distributions/ALTLinux/Sisyphus/x86_64/RPMS.classic/libpng15-1.5.30-alt1.x86_64.rpm sudo alien -vc libpng15-1.5.30-alt1.x86_64.rpm sudo dpkg -i libpng15_1.5.30-1_amd64.deb

 3.提取 Maya 安装软件包的内容，并将目录更改为其安装/软件包目录。 4.将安装中的 rpm 软件包转换为 deb 软件包。

sudo alien -vc *.rpm 5.安装单机许可软件包。

sudo apt install lsb-core 6.安装许可软件包：adlmapps、adlmflexnetserveripv6、adlmflexnetclient 和 adsklicensing。例如：

sudo apt-get install ./adlmapps17_17.0.49-1_amd64.deb  sudo apt-get install ./adlmflexnetserveripv6_17.0.50-1_amd64.deb  sudo apt-get install ./adlmflexnetclient_17.0.49-1_amd64 后面不完整
