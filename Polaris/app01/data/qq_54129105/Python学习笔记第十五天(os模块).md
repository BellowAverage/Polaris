
--- 
title:  Python学习笔记第十五天(os模块) 
tags: []
categories: [] 

---


#### Python学习笔记第十五天
- - <ul><li>- <ul><li>- - - - - 


## os模块

### 重命名和删除文件

Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。

要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。

#### rename() 方法

rename() 方法需要两个参数，当前的文件名和新文件名。

```
# 实例 7
import os
 
# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )

```

#### remove()方法

你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。

```
# 实例 8
import os
 
# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")

```

### 目录

所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。

#### mkdir()方法

可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。

```
# 实例 1
import os
 
# 创建目录test
os.mkdir("test")

```

#### chdir()方法

可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。

```
# 实例 2
import os
 
# 将当前目录改为"/home/newdir"
os.chdir("/home/newdir")

```

#### getcwd()方法

getcwd()方法显示当前的工作目录。

```
# 实例 3
import os
 
# 给出当前的目录
print(os.getcwd())

```

#### rmdir()方法

rmdir()方法删除目录，目录名称以参数传递。

在删除这个目录之前，它的所有内容应该先被清除。

以下是删除" /tmp/test"目录的例子。目录的完全合规的名称必须被给出，否则会在当前目录下搜索该目录。

```
# 实例 4
import os
 
# 删除”/tmp/test”目录
os.rmdir( "/tmp/test"  )

```

## 结束语

今天学习的是Pythonos模块学会了吗。 今天学习内容总结一下：
1. 重命名和删除文件1. 目录