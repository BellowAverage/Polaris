
--- 
title:  mac下安装完python3以后,让默认执行的python变成python3的方法 
tags: []
categories: [] 

---
## 安装python

```
brew install python

```

安装成功提示:

```
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

```

按照上面提示我们打开目录/usr/local/opt/python@3.9/libexec/bin 这个就是python3.9的目录

```
open /usr/local/opt/python@3.9/libexec/bin

```

会看到下面文件 <img src="https://img-blog.csdnimg.cn/726cd5d8649243f5a8e06525cccfaa8f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5omL55C05biI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

这时系统里面同时有python2.7和新安装的python3 查看默认python版本

```
python -V 

```

得到默认版本:Python 2.7.16

执行python3 -V,得到版本3.9

```
python3 -V
Python 3.9.10

```

## 现在把默认执行python的时候,从python 2.7改成python3

### 让命令行每次输入python的时候都默认执行的是python3而不是python2.7

查找默认的python在哪里

```
which python

```

得到路径:/usr/bin/python

```
tdw@bogon ~ % which python
/usr/bin/python

```

查找python3的路径 which python3

```
tdw@bogon ~ % which python3
/usr/local/bin/python3

```

打开文件~/.bashrc

```
open ~/.bashrc 

```

在里面把默认的python重命名,把python2设置成python2.7的路径把 python设置成python3的路径

```
alias python2='/usr/bin/python'
alias python='/usr/local/bin/python3'

```

保存文件 运行.bashrc文件

```
source ~/.bashrc

```

现在再查看python和python2版本,发现默认的已经是python3了 python -V Python 3.9.10 python2 -V Python 2.7.16

<img src="https://img-blog.csdnimg.cn/a3bb5b60991c4ca8b99d8939dad284bc.png" alt="在这里插入图片描述">

### 添加python3的环境变量

打开文件~/.zshrc ,注意mac新版系统big sur 环境变量不在 ~/.bash_profile文件中,bash_profile每次都要source才能生效,关闭终端重新打开,还要再次source

```
open ~/.zshrc

```

添加环境变量的格式是这样:

```
export PATH="路径名:$PATH"

```

这个路径名就是上面我们安装完python3.9的时候提示的路径:/usr/local/opt/python@3.9/libexec/bin

```
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin


```

把这个路径拼接上上面的格式就成了这样:

```
export PATH="/usr/local/opt/python@3.9/libexec/bin:$PATH"

```

把这句话添加到 ~/.zshrc 文件中,可以看到里面还有其他的export PATH,这些都是其他的路径,如下图: <img src="https://img-blog.csdnimg.cn/a7a0fac901f24ba6b16fa9aa2fe46303.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5bCP5omL55C05biI,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

然后保存文件 运行文件

```
source ~/.zshrc

```
