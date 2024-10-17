
--- 
title:  -bash usrbinpython3^M 坏的解释器 没有那个文件或目录 
tags: []
categories: [] 

---
## -bash: /usr/bin/python3^M: 坏的解释器: 没有那个文件或目录

### 【1】问题现象

执行python脚本，提示错误：/usr/bin/python^M: 解释器错误: 没有那个文件或目录

>  
 这个错误，对于刚用linux 运行 python 脚本的人都遇到过，或者运行一些其他用Windows 编写好的代码，这个问题不太理解的都无从下手，只能上网寻求帮助。这也是好事，自己找答案解决也蛮有成就感的。 


### 【2】原因分析
- 一般这种问题，是编码的问题，Windows 的编码格式与 linux 的编码格式不对。- 大多数是因为脚本文件在windows下编辑过。- 在Windows中，每一行的结尾是\r\n，而在linux下文件的结尾是\n。
### 【3】问题解决
- 打开文件，查看编码格式
```
vi filename.py

:set ff   或者   :set fileformat

```
- 格式信息：
```
fileformat=dos 或 fileformat=unix
# dos 表示windows系统
# unix 表示 Unix系统，linux 也属于类Unix 系统

```
- 修改格式：
```
:set ff=unix  或   :set fileformat=unix
#再次查看格式是否改变
:set ff

```
- `:wq` 保存退出，运行脚本
## Python安装包报错ERROR: Could not find a version that satisfies the requirement XXX解决方法

>  
 我们在使用 pip 安装 python 包时，经常会出现如下错误： 


```
ERROR: Could not find a version that satisfies the requirement xxxx(from versions: none)
ERROR: No matching distribution found for xxxx

```
-  问题出现主要是pip 源的问题 -  直接选用pip 源并且信任它的来源就可以解决这种问题。 -  下面使用了豆瓣源，将其换成清华源、阿里源等都适用。 
```
pip install 库包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

```

**pip 国内的一些镜像地址：**
<li> 
  <blockquote> 
   阿里云 http://mirrors.aliyun.com/pypi/simple/ 
  </blockquote> </li><li> 
  <blockquote> 
   中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
  </blockquote> </li><li> 
  <blockquote> 
   豆瓣(douban) http://pypi.douban.com/simple/ 
  </blockquote> </li><li> 
  <blockquote> 
   清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
  </blockquote> </li><li> 
  <blockquote> 
   中国科学院 http://pypi.mirrors.opencas.cn/simple/ 
  </blockquote> </li>
>  
   中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
  

>  
   清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
  

## windows及linux环境下永久修改pip镜像源的方法

##### 1、在windows环境下修改pip镜像源的方法
- 在windows文件管理器中,输入 **%APPDATA%**- 会定位到一个新的目录下，在该目录下新建pip 文件夹，然后到pip文件夹里面去新建个pip.ini文件- 在新建的pip.ini文件中输入以下内容
```
[global]
timeout = 6000
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com

```

##### 2、在linux系统中更新pip源的方式
- 在用户的家目录下面创建名为.pip文件夹
```
cd /root
mkdir .pip

```
- 在创建好的.pip文件夹中创建名为pip.conf的文件
```
vi pip.conf

```
- 在pip.conf文件中输入以下内容
```
[global]
timeout = 6000
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com

```

注意：
1. `http://mirrors.aliyun.com/pypi/simple/`中的simple目录必须有。1. `trusted-host = mirrors.aliyun.com`一定要加上这行，否则会报错。