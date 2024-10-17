
--- 
title:  [Linux shell] 脚本格式转换 ‘\r’: command not found 
tags: []
categories: [] 

---
>  
 背景 在windows下编写的shell脚本, 在linux中执行报错 $‘\r’: command not found 


## 解决方法

这个错误通常是由于脚本文件的格式问题引起的，特别是在 Windows 系统中编辑的脚本在 Linux 系统下执行时可能会遇到这个问题。

这错误提示 `$'\r': command not found` 表示在脚本的某一行中包含了 `\r`（Carriage Return，回车符），这是 Windows 文本文件中的换行符。在 Linux 中，换行符应该是 `\n`（Line Feed，换行符），而不是 `\r\n`。

为了解决这个问题，可以使用一些文本编辑器或转换工具来修复脚本文件。下面是一些方法：

#### 1. 使用dos2unix

```
dos2unix a.sh

```

`dos2unix` 命令可以将 Windows 格式的文本文件转换为 Unix 格式。确保在 CentOS 中安装了 `dos2unix` 工具。

`sudo yum install dos2unix`

#### 2. 使用sed

```
sed -i 's/\r$//' a.sh

```

这个命令使用 `sed`（流编辑器）将文件中的 `\r` 替换为空字符串。

#### 3. 使用编辑器

打开脚本文件，使用编辑器将换行符转换为 Unix 格式。在大多数文本编辑器中，你可以在保存文件时选择文件格式为 Unix/Linux。

```
vi a.sh
# 在vi编辑器中，可以输入以下命令来保存文件：
# :set ff=unix
# :wq

```

选择其中一种方法，根据你的实际需求来修复脚本文件，然后再次执行脚本。这应该能够解决报错问题。
