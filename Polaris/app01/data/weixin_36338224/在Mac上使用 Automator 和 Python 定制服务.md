
--- 
title:  在Mac上使用 Automator 和 Python 定制服务 
tags: []
categories: [] 

---
### 1. 前言

由于我经常会制作一些资源压缩包，在这个资源压缩包里会有一个引流用的二维码

之前手工的时候，一次就要花费5-10 分钟，特别不划算。

因此我就打算借助 Automator + Python 在右键菜单里添加一个按钮，可以一键复制这些重复性的操作。

实际使用效果如下：

<img src="https://img-blog.csdnimg.cn/20210228152752381.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="">

### 2. 打开 automator

使用 ⌘ + Space，搜索 `automator`进入 `自动操作`。

<img src="https://img-blog.csdnimg.cn/img_convert/167eae67a0ae57a4a00afbb044348bba.png" alt="">

双击选择 `服务`

<img src="https://img-blog.csdnimg.cn/20210228152827932.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="">

### 3. 编排工作流

要实现我这个功能，首先要有个触发的入口，由于我是右击文件，因此要在资源库里选择 `文件和文件夹`，由于我在脚本中要获取目标文件的文件名，因此 我还要选择 `获取所选的访达项目`。

所有的逻辑实现，你可以通过 Shell 脚本编写，也可以使用 Python 脚本。

但无论是哪一种语言，都需要在工作流中引入 `运行 Shell 脚本` 这个模块。

由于我这边使用的是 Python ，所以在 `Shell` 选项中，选择 `/usr/bin/pyhton` （写代码时要注意这是 Python2 噢）

<img src="https://img-blog.csdnimg.cn/2021022815281540.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

此时你应该已经注意到，`运行 Shell 脚本` 右边有一个选项问你：参数要如何传入脚本内呢？

默认选项是：传递到 stdin，也就是标准输入中。

因此我要想在 python 脚本中获取 目标文件的文件名，需要从 sys.stdin 中去获取。

整个脚本的内容如下，若有需要，可以参考

```
# coding: utf-8

import os
import sys
import shutil
import commands

def encrypt_file(file):
    filename, ext = os.path.splitext(file)
    dir_name = filename
    os.mkdir(dir_name)
    shutil.copy(src=file, dst=dir_name)
    os.chdir(dir_name)
    zip_cmd = '/usr/bin/zip -P "iswbm.com" "{}.zip" "{}"'.format(filename, file)
    zip_cmd_no_pass = '/usr/bin/zip -r "{}.zip" "{}"'.format(dir_name, dir_name)
    wget_cmd = '/usr/local/bin/wget -q http://image.iswbm.com/get_zip_pass_01.png'

    commands.getstatusoutput(zip_cmd)
    commands.getstatusoutput(wget_cmd)
    os.rename("get_zip_pass_01.png", "解压密码，看这里.png")
    os.remove(file)

    os.chdir("..")
    commands.getstatusoutput(zip_cmd_no_pass)
    shutil.rmtree(dir_name)
    print("Success!")

for file in sys.stdin:
    dir,file = os.path.split(file.strip())
    os.chdir(dir)
    if os.path.isfile(file):
        encrypt_file(file)
    else:
        print("Can not zip directionary({})!".format(file))

```

为了让脚本在运行完成后，能有个通知，你可以和我一样在最后再添加两个模块
1. `设定变量的值` ：把标准输出的内容赋值给 `output` 变量1. `显示通知`：把 `output` 变量的内容，在通知里打印出来
<img src="https://img-blog.csdnimg.cn/20210228152844389.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zNjMzODIyNA==,size_16,color_FFFFFF,t_70" alt="">

一切完成后，使用快捷键 ⌘ + S 进行保存。

代码初步编写完成后，并不是一帆风顺的，需要调试来不断改正，

在调试的时候遇到几个问题，在这里记录一下：
- sys.stdin 传入是文件的绝对路径，而不是文件名，因此要注意处理- 由于使用的是 python2，若脚本中有中文，记得在开头要注明 `# coding: utf-8`- 通过使用右键来调试，错误信息显示不全，建议使用 automator 的步进来调试，或者在终端中手动执行脚本来调试。