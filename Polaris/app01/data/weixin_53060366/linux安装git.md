
--- 
title:  linux安装git 
tags: []
categories: [] 

---
### linux安装git 有两种方式：



#### 1、直接yum安装：

```
yum install git -y

# 查看版本：
git --version

```

推荐自定义安装，因为yum安装的Git版本比较老，并且配置文件不能指定位置。 

#### 2、自定义安装：
- 官网下载安装包：
<img src="https://img-blog.csdnimg.cn/img_convert/998bf6f9e6f0cbf177a48865668e6448.png#averageHue=#f2f1eb&amp;clientId=u1fa99049-7a91-4&amp;from=paste&amp;height=470&amp;id=ue1f4f290&amp;originHeight=587&amp;originWidth=1529&amp;originalType=binary&amp;ratio=1&amp;rotation=0&amp;showTitle=false&amp;size=212606&amp;status=done&amp;style=none&amp;taskId=uc8a8266c-ceb2-4eb5-9822-1ed986b3a11&amp;title=&amp;width=1223.2" alt="image.png">
- 解压安装包:
```
tar -zxvf git-2.39.0.tar.gz 

```
- 安装编译环境：
```
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker

```
- 安装上面编译环境的时候，yum自动帮你安装了git，这时候你需要先卸载这个旧版的git。
```
yum remove git

```
- 编译安装:（这个时候一定要在git-2.39.0的文件夹下执行）
```
make prefix=/opt/git all
make prefix=/opt/git install

```
- 配置环境变量：
```
vim /etc/profile
export GIT_HOME=/opt/git
export PATH=$GIT_HOME/bin:$PATH

#刷新源
source /etc/profile

#最后查看版本：
git --version

```

<img src="https://img-blog.csdnimg.cn/img_convert/291a209422a157d8182513b6e5209d44.png#averageHue=#32302f&amp;clientId=u1fa99049-7a91-4&amp;from=paste&amp;height=105&amp;id=uce287e54&amp;originHeight=131&amp;originWidth=1109&amp;originalType=binary&amp;ratio=1&amp;rotation=0&amp;showTitle=false&amp;size=43915&amp;status=done&amp;style=none&amp;taskId=u4b3a3f7a-e851-4c23-be63-0497891459a&amp;title=&amp;width=887.2" alt="image.png">
