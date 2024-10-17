
--- 
title:  python 报错python.exe -m pip install --upgrade pip‘ command. 
tags: []
categories: [] 

---
WARNING: You are using pip version 21.1.1; however, version 22.3.1 is available.

You should consider upgrading via the 'd:\python\python38\python.exe -m pip install --upgrade pip' command.

提示这个报错，一般是pip没更新吧，我们更新一下就好了。

在终端这里输入以下代码

```
python -m pip install -U pip
```

按回车就行。

也可以这样设置

```
python -m pip install --upgrade pip
```

两个效果是一样的，都是更新pip

记不住代码？没关系，其实报错早有提示了....

你看报错的最后一行，最后的代码

d:\python\python38\python.exe -m pip install --upgrade pip' command.

从python.exe 开始，到 pip 结束就行，只需要把 python.exe 改错python

然后在终端输出 

python -m pip install --upgrade pip

按回车，大功告成


