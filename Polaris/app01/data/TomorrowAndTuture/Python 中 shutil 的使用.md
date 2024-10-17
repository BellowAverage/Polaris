
--- 
title:  Python 中 shutil 的使用 
tags: []
categories: [] 

---
Python 里边 os 模块虽然有一些文件目录创建和删除的部分简单操作，但是有一点很不太友好，就是删除目录的时候还必须让目录为空——虽然比较安全，我也能理解，但是让我很不爽，毕竟我想要的是 rm -rf 的那种摧枯拉朽的气势：

```
os.makedirs()
os.makedir()
os.remove()
os.removedirs()
os.rmdir()


root@master ~# python3
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import os
&gt;&gt;&gt; os.removedirs('/root/pandas')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib64/python3.6/os.py", line 238, in removedirs
    rmdir(name)
OSError: [Errno 39] Directory not empty: '/root/pandas'
&gt;&gt;&gt; os.rmdir('/root/pandas')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 39] Directory not empty: '/root/pandas'

```

以致于每当我想递归删除目录，或者递归拷贝目录的时候，只能求助于 subprocess 了。

```
import subprocess

subprocess.run(['rm', '-rf', 'run'],
               stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
subprocess.run(['cp', '-r', config_dir, root_path],
               stderr=subprocess.STDOUT, stdout=subprocess.DEVNULL)
```

这时候，shutil 就上场了，如果用 shutil 的话，语法就很简单了。

（注意：shell 命令 cp 是不会主动创建 dst 目录的，但是 shutil.copytree 会；简单理解就是：shutil.copytree 会将 src 文件夹里的所有内容拷贝至 dst 文件夹，和 cp 命令稍微有点差异）。

```
import shutil

shutil.rmtree('run')
shutil.copytree(config_dir, os.path.join(root_path, 'config'))
```

具体用法如下。

### copytree

**copytree(src, dst, symlinks=False, ignore=None)**： 拷贝文档树，将 src 文件夹里的所有内容拷贝至 dst 文件夹
- src：源文件夹- dst：复制至 dst 文件夹，该文件夹会自动创建，需保证此文件夹不存在，否则将报错- symlinks：是否复制软连接，True复制软连接，False不复制，软连接会被当成文件复制过来，默认False。
### rmtree

**rmtree(path, ignore_errors=False, οnerrοr=None)**： 移除文档树，将文件夹目录删除。我自己感觉有点像  rm -rf path

### copyfile

**copyfile(src, dst)**： 将 src 文件内容复制至 dst 文件
- src： 源文件路径- dst： 复制至 dst 文件，若 dst 文件不存在，将会生成一个 dst 文件；若存在将会被覆盖
```
import shutil
shutil.copyfile("file.txt","file_copy.txt")
```

### copymode 

**copymode(src, dst)**： 将 src 文件权限复制至 dst 文件。文件内容，所有者和组不受影响
- src： 源文件路径- dst： 将权限复制至 dst 文件，dst 路径必须是真实的路径，并且文件必须存在，否则将会报文件找不到错误
```
import shutil
shutil.copymode("file.txt","file_copy.txt")
```

### copystat 

**copystat(src, dst)**： 将权限，上次访问时间，上次修改时间以及 src 标志复制到 dst。文件内容，所有者和组不受影响
- src： 源文件路径- dst： 将**权限**复制至 dst 文件，dst 路径必须是真实的路径，并且文件必须存在，否则将会报文件找不到错误。
```
import shutil
shutil.copystat("file.txt","file_copy.txt")
```

### copy 

**copy(src, dst)**： 将文件 src 复制至 dst。dst 如果是个目录，会在该目录下创建与 src 同名的文件。权限会被一并复制。本质是先后调用了 copyfile 与 copymode 而已。
- src：源文件路径- dst：复制至 dst 文件夹或文件
```
&gt;&gt;&gt; import shutil
&gt;&gt;&gt; shutil.copy('file', 'filecopy')
'filecopy'
&gt;&gt;&gt; shutil.copy('file', './upload')
'./upload/file'
&gt;&gt;&gt; shutil.copy('file', './upload/file')
'./upload/file'
&gt;&gt;&gt; shutil.copy('file', './upload/filecopy')
'./upload/filecopy'

```

### copy2 

**copy2(src, dst)**： 将文件 src 复制至 dst。dst 如果是个目录，会在该目录下创建与 src 同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限、上次访问时间、上次修改时间和 src 的标志会一并复制至 dst。本质是先后调用了copyfile 与 copystat方法而已。
- src：源文件路径- dst：复制至 dst 文件夹或文件
```
&gt;&gt;&gt; import shutil
&gt;&gt;&gt; shutil.copy2('file', 'filecopy')
'filecopy'
&gt;&gt;&gt; shutil.copy2('file', './upload')
'./upload/file'
&gt;&gt;&gt; shutil.copy2('file', './upload/filecopy')
'./upload/filecopy'

```

### move 

**move(src, dst)**： 将 src 移动至 dst 目录下。若 dst 目录不存在，则效果等同于 src 改名为 dst。若 dst 目录存在，将会把 src 文件夹的所有内容移动至该目录下面
- src：源文件夹或文件- dst：移动至 dst 文件夹，或将文件改名为 dst 文件。如果 src 为文件夹，而 dst 为文件将会报错
```
import shutil,os
# 示例一，将src文件夹移动至dst文件夹下面，如果bbb文件夹不存在，则变成了重命名操作
folder1 = os.path.join(os.getcwd(),"aaa")
folder2 = os.path.join(os.getcwd(),"bbb")
shutil.move(folder1, folder2)
# 示例二，将src文件移动至dst文件夹下面，如果bbb文件夹不存在，则变成了重命名操作
file1 = os.path.join(os.getcwd(),"aaa.txt")
folder2 = os.path.join(os.getcwd(),"bbb")
shutil.move(file1, folder2)
# 示例三，将src文件重命名为dst文件(dst文件存在，将会覆盖)
file1 = os.path.join(os.getcwd(),"aaa.txt")
file2 = os.path.join(os.getcwd(),"bbb.txt")
shutil.move(file1, file2)
```

### chown 

**chown(path, user=None, group=None)**： 修改路径指向的文件或文件夹的所有者或分组。
- path：路径- user：所有者，传递user的值必须是真实的，否则将报错no such user- group：分组，传递group的值必须是真实的，否则将报错no such group
```
import shutil,os
path = os.path.join(os.getcwd(),"file.txt")
shutil.chown(path,user="root",group="root")
```

### which 

**which(cmd, mode=os.F_OK | os.X_OK, path=None)**： 获取给定的cmd命令的可执行文件的路径。

```
import shutil
info = shutil.which("python3")
print(info)   # /usr/bin/python3
```


