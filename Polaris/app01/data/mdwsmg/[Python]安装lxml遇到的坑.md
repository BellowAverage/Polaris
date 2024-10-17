
--- 
title:  [Python]安装lxml遇到的坑 
tags: []
categories: [] 

---
使用pip命令安装 lxml时，报错如下

```
ERROR: lxml-4.9.0-cp310-cp310-win_amd64.whl is not a supported wheel on this platform.

```

错误原因：资源版本不对 ERROR: lxml-4.9.0-cp310-cp310-win_amd64.whl is not a supported wheel on this platform.

### 检查

1、 检查python版本 在cmd界面中，输入命令

```
python

```

查看对应python版本 ，输入 exit() 退出 <img src="https://img-blog.csdnimg.cn/374698770ec74320bc85a9ddd5c9c7ab.png" alt="在这里插入图片描述"> 可知，python版本为3.8 位数为 64

所以，**正确版本**为 “cp38+amd64”

### 下载正确版本

进入官网 https://pypi.org/project/lxml/#files ，选择正确的版本然后进行下载、安装 <img src="https://img-blog.csdnimg.cn/313c993085c04288bf7583b3d5496560.png" alt="在这里插入图片描述">

```
pip install lxml-4.9.0-cp38-cp38-win_amd64.whl

```

<img src="https://img-blog.csdnimg.cn/35f97e3e36d248b19ce59dd9650edc64.png" alt="在这里插入图片描述">

### warning信息

WARNING: Ignoring invalid distribution -ip (d:\python\python3.8.4\lib\site-packages)

```
WARNING: Ignoring invalid distribution -ip (d:\python\python3.8.4\lib\site-packages)

```

到报错目录下删除目录 ~ip-20.3.3.dist-info 即可，如有 ~pip 也删除

>  
 <s>warning不影响使用pip</s> 删除后再次使用pip就不会报这个警告了 


可以使用命令

```
pip list

```

查看python安装了哪些第三方库 <img src="https://img-blog.csdnimg.cn/a2d50dce215344d29b5b4e8510082b13.png" alt="在这里插入图片描述">

搞定
