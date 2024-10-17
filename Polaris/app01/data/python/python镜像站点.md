
--- 
title:  python镜像站点 
tags: []
categories: [] 

---
>  
 有时候使用默认镜像安装缓慢导致超时，可以切换镜像配置或临时使用以下国内镜像。 

-  <h2 id="%E5%9B%BD%E5%86%85%E4%B8%80%E4%BA%9B%E9%95%9C%E5%83%8F%E7%BD%91%E7%AB%99">国内一些镜像网站</h2> 
```
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple
中国科技大学 ：https://pypi.mirrors.ustc.edu.cn/simple
华中理工大学：http://pypi.hustunique.com
山东理工大学：http://pypi.sdutlinux.org
```

### 三方库安装示例--- pandas库安装

<img alt="" class="left" src="https://img-blog.csdnimg.cn/9a8108b879024b98aa7c15fdb463d22c.png">

```
//使用默认镜像安装缓慢导致超时
pip install pandas
//临时指定镜像(国内清华镜像)安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

<img alt="" src="https://img-blog.csdnimg.cn/4b075937925d4ac6950ce239b361384d.png">


