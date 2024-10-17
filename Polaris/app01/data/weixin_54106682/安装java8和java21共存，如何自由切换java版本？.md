
--- 
title:  安装java8和java21共存，如何自由切换java版本？ 
tags: []
categories: [] 

---
### 问题与分析

**问题： **不同软件运行需要的java版本支持可能不一致，对不一致的java版本反复进行卸载与安装，显然是不明智的做法。而版本共生则可以解决这个问题。

**分析：**通过设置环境变量来实现不同版本java的自由切换。

### 具体步骤

#### 分别安装java8及java21

java8是我之前已经安装过的，这里演示java21的安装步骤。

**官网下载安装包：**

<img alt="" height="835" src="https://img-blog.csdnimg.cn/direct/9cfb758419e448c3b1e4d3db16b6a7ed.png" width="1200">

下载后打开.exe文件进行安装。

<img alt="" height="383" src="https://img-blog.csdnimg.cn/direct/f8efff63ea754057a097e69dc6039836.png" width="504">

更改安装路径后点击下一步。

<img alt="" height="383" src="https://img-blog.csdnimg.cn/direct/c7499ec62c3b4f3ea653157b2e322026.png" width="504">

安装成功。

<img alt="" height="383" src="https://img-blog.csdnimg.cn/direct/656103d6cbe44d839b33976e0463ab64.png" width="504">

#### 设置环境变量

```
JAVA8_HOME =jdk1.8的安装路径根目录
JAVA21_HOME =jdk21的安装路径根目录
JAVA_HOME = %JAVA21_HOME% (注意:如果你想切换jdk版本，就在此处设置即可)
```

<img alt="" height="207" src="https://img-blog.csdnimg.cn/direct/28b77b31b9ca4e7f934b2ad1ca2f16c2.png" width="594">

```
PATH=%JAVA_HOME%\bin
//jre的路径，由于java8版本还有jre，所以将jre的路径编辑好，后续无需修改
D:\java\jdk1.8.0_91\jre\bin
```

<img alt="" height="570" src="https://img-blog.csdnimg.cn/direct/1068898d0e404ccd99cfc635b815709a.png" width="511">

#### 版本切换失效解决方法

环境变量编辑为切换Java路径后，没有重新打开cmd窗口来查版本（java -version），可先尝试关闭cmd窗口重新打开；

如果还是没有切换过来，应该是在Path中默认启用了一个系统自带的jdk，优先启用排序最前的，可以把%JAVA_HOME%\bin移到其上方即可解决。

<img alt="" height="570" src="https://img-blog.csdnimg.cn/direct/b237d11e3321497eacad0bd3d28e8de4.png" width="541">​​​​​​​

#### 残留问题

<img alt="" height="289" src="https://img-blog.csdnimg.cn/direct/a0ba0c84b96b4b3ba361069e130047ed.png" width="636">

javac -version的版本依然为切换前21版本。

<img alt="" height="570" src="https://img-blog.csdnimg.cn/direct/0e028615020d4647a3771d5399f27add.png" width="541">

另外将java8的jre路径移到最上方或者JAVA_HOME路径下方，java -version的输出结果一直都是8版本；
