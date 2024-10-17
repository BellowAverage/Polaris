
--- 
title:  idea classes: does not exist的一个原因和解决 
tags: []
categories: [] 

---
今天出了一个问题，导致程序bug了。

我delete了idea的classes文件，然后提示：文件无法删除。再次构造的时候就提示： classes: does not exist。

于是去百度，发现：其实删除了没啥用，里面的东西delete会自动构建新的。

打开文件路径，找到class文件夹，提示：文件无法运行。 删除提示：文件无法删除，无权限。 打开文件安全，也提示无权限。 修改所属用户，提示：无权限。

也就是说：win10出bug了，导致没给程序赋权，无法新增class文件。所以程序新建class文件以后无法read，所以提示：class不存在。

用了360粉碎机直接粉碎了（大家不喜欢360也可以用其他的粉碎机）。 继续构建程序，问题解决。

记录一下。
