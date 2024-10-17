
--- 
title:  Python 的 os.path() 和 pathlib.Path() 
tags: []
categories: [] 

---
### os.path()

```
&gt;&gt;&gt; import os

```

在 Python 中一旦涉及到路径相关的操作，os.path() 模块无疑是用得最多的了，下面就让我们一块来看看吧！
|方法|说明
|os.path.abspath(path)|返回绝对路径
|os.path.basename(path)|返回文件名
|os.path.commonprefix(list)|返回list(多个路径)中，所有path共有的最长的路径
|os.path.dirname(path)|返回文件所在目录路径
|os.path.exists(path)|路径存在则返回True,路径损坏返回False
|os.path.lexists(path)|路径存在则返回True,路径损坏也返回True  (Test whether a path exists. Returns True for broken symbolic links)
|os.path.expanduser(path)|把path中包含的"~"和"~user"转换成用户目录
|os.path.expandvars(path)|根据环境变量的值替换path中包含的"$name"和"${name}"
|os.path.getatime(path)|返回最近访问时间（浮点型秒数）
|os.path.getmtime(path)|返回最近文件修改时间
|os.path.getctime(path)|返回文件 path 创建时间
|os.path.getsize(path)|返回文件大小，如果文件不存在就返回错误
|os.path.isabs(path)|判断是否为绝对路径
|os.path.isfile(path)|判断路径是否为文件
|os.path.isdir(path)|判断路径是否为目录
|os.path.islink(path)|判断路径是否为链接
|os.path.ismount(path)|判断路径是否为挂载点
|os.path.join(path1[, path2[, ...]])|把目录和文件名合成一个路径
|os.path.normcase(path)|转换path的大小写和斜杠
|os.path.normpath(path)|规范path字符串形式
|os.path.realpath(path)|返回path的真实路径
|os.path.relpath(path[, start])|从start开始计算相对路径
|os.path.samefile(path1, path2)|判断目录或文件是否相同
|os.path.sameopenfile(fp1, fp2)|判断fp1和fp2是否指向同一文件
|os.path.samestat(stat1, stat2)|判断stat tuple stat1和stat2是否指向同一个文件
|os.path.split(path)|把路径分割成 dirname 和 basename，返回一个元组
|os.path.splitdrive(path)|一般用在 windows 下，返回驱动器名和路径组成的元组
|os.path.splitext(path)|分割路径中的文件名与拓展名
|os.path.splitunc(path)|把路径分割为加载点与文件
|os.path.walk(path, visit, arg)|Python3 好像没这个了，应该变成 os.walk() 了。
|os.path.supports_unicode_filenames|设置是否支持unicode路径名

#### os.path.abspath(path) 

```
&gt;&gt;&gt; os.path.abspath('test.py')
'/root/workspace/python3_learning/test.py'

```

#### os.path.basename(path)

```
&gt;&gt;&gt; os.path.basename('/root/workspace/python3_learning/test.py')
'test.py'

```

#### os.path.commonprefix(list)

```
&gt;&gt;&gt; os.path.commonprefix(['/root/test.py', '/root/workspace/python3_learning'])
'/root/'

```

#### os.path.dirname(path)

```
&gt;&gt;&gt; os.path.dirname('/root/workspace/python3_learning/test.py')
'/root/workspace/python3_learning'
```

#### os.path.exists(path)

```
&gt;&gt;&gt; os.path.exists('/root/workspace/python3_learning/test.py')
True
&gt;&gt;&gt; os.path.exists('/root/workspace/python3_learning/test3.py')
False

```

#### os.path.lexists(path)

test.py.bak 是 test.py 的符号链接。符号链接所指向的文件即使不存在了，只要符号链接仍然存在，也仍然返回 True。

```
&gt;&gt;&gt; os.path.lexists('test.py.link')
True
&gt;&gt;&gt; os.path.exists('test.py.link')
True
&gt;&gt;&gt; os.remove('test.py')
&gt;&gt;&gt; os.path.lexists('test.py.link')
True
&gt;&gt;&gt; os.path.exists('test.py.link')
False

```

#### os.path.expanduser(path)

```
# root
&gt;&gt;&gt; os.path.expanduser('~/workspace')
'/root/workspace'

# looking
&gt;&gt;&gt; os.path.expanduser('~/workspace')
'/home/looking/workspace'

```

#### os.path.expandvars(path)

```
&gt;&gt;&gt; os.path.expandvars('${HOME}/workspace')
'/root/workspace'

```

#### os.path.getatime(path)

```
&gt;&gt;&gt; os.path.getatime('test2.py')
1611627917.5157754

```

#### os.path.getmtime(path)

```
&gt;&gt;&gt; os.path.getmtime('test2.py')
1609834946.9199047

```

#### os.path.getctime(path)

```
&gt;&gt;&gt; os.path.getctime('test2.py')
1609834946.9209046

```

#### os.path.getsize(path) 

```
&gt;&gt;&gt; os.path.getsize('test2.py')
196

```

#### os.path.isabs(path)

```
&gt;&gt;&gt; os.path.isabs('/root/workspace/python3_learning/test.py')
True
&gt;&gt;&gt; os.path.isabs('python3_learning/test.py')
False

```

#### os.path.isfile(path)

```
&gt;&gt;&gt; os.path.isfile('test.py')
True
&gt;&gt;&gt; os.path.isfile('non-exists')
False

```

#### os.path.isdir(path)

```
&gt;&gt;&gt; os.path.isdir('.')
True
&gt;&gt;&gt; os.path.isdir('test.py')
False

```

#### os.path.islink(path)

```
&gt;&gt;&gt; os.path.islink('test.py')
False
&gt;&gt;&gt; os.path.islink('test.py.link')
True

```

#### os.path.ismount(path)

```
&gt;&gt;&gt; os.path.ismount('/dev/mapper/centos-root')
False
&gt;&gt;&gt; os.path.ismount('/')
True
&gt;&gt;&gt; os.path.ismount('/dev')
True

```

#### os.path.join(path1[, path2[, ...]])

```
&gt;&gt;&gt; os.path.join('/root', 'workspace', 'python3_learning/')
'/root/workspace/python3_learning/'

```

#### os.path.normcase(path)

```
&gt;&gt;&gt; os.path.normcase('/root\/dft')
'/root\\/dft'

```

#### os.path.normpath(path)

```
&gt;&gt;&gt; os.path.normpath('./../a/b/../c')
'../a/c'
```

#### os.path.realpath(path)

```
&gt;&gt;&gt; os.path.realpath('test.py')
'/root/workspace/python3_learning/test.py'

```

####  os.path.samefile(path1, path2)

```
&gt;&gt;&gt; os.path.samefile('test.py', 'test2.py')
False
&gt;&gt;&gt; os.path.samefile('test.py', 'test.py')
True
&gt;&gt;&gt; os.path.samefile('test.py', 'test.py.link')
True

```

#### os.path.sameopenfile(fp1, fp2)

```
&gt;&gt;&gt; fd1 = os.open('test.txt', os.O_RDWR|os.O_CREAT)
&gt;&gt;&gt; fd2 = os.open('test.txt', os.O_RDWR|os.O_CREAT)
&gt;&gt;&gt; os.path.sameopenfile(fd1, fd2)
True
&gt;&gt;&gt; fd3 = os.open('foo.txt', os.O_RDWR|os.O_CREAT)
&gt;&gt;&gt; os.path.sameopenfile(fd1, fd3)
False

```

#### os.path.samestat(stat1, stat2)

```
&gt;&gt;&gt; os.path.samestat(os.stat('test.py'), os.stat('test.py'))
True
&gt;&gt;&gt; os.path.samestat(os.stat('test.py'), os.stat('test.py.link'))
True
&gt;&gt;&gt; os.path.samestat(os.stat('test.py'), os.stat('test2.py'))
False

```

#### os.path.split(path)

```
&gt;&gt;&gt; os.path.split('/root/workspace/python3_learning/test.py')
('/root/workspace/python3_learning', 'test.py')

```

#### os.path.splitext(path)

```
&gt;&gt;&gt; os.path.splitext('/root/workspace/python3_learning/test.py')
('/root/workspace/python3_learning/test', '.py')
&gt;&gt;&gt; os.path.splitext('test.py')
('test', '.py')
&gt;&gt;&gt; 

```

### pathlib.Path()

当然还有纯路径对象 **pathlib.PurePath()**，纯路径对象提供了不实际访问文件系统的路径处理操作。如果你处理的路径，并不关心它在当前文件系统上是否存在，就最好用它了。

```
&gt;&gt;&gt; import pathlib
```

和 os、os.path 的部分功能很像。 

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6a8367c7680f005b42e0f715c1a525af.png">

#### Path.as_posix()

```
C:\Users\xxx&gt;python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import pathlib
&gt;&gt;&gt; pathlib.Path(r".\src\scan\system\test.py")
WindowsPath('src/scan/system/test.py')
&gt;&gt;&gt; pathlib.Path(r".\src\scan\system\test.py").as_posix()
'src/scan/system/test.py'
```

#### Path.chmod() 

```
[root@master python3_learning]# ll
total 0
-rw-r--r--. 1 root root 0 Nov 26 09:17 test.py
[root@master python3_learning]# python3
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import pathlib
&gt;&gt;&gt; pathlib.Path('test.py').chmod(0o750)
&gt;&gt;&gt; 
[root@master python3_learning]# ll
total 0
-rwxr-x---. 1 root root 0 Nov 26 09:17 test.py*

```

#### Path.iterdir()

和 os.listdir() 比较像，只不过这儿返回的是一个可迭代对象。

```
&gt;&gt;&gt; import pathlib
&gt;&gt;&gt; pathlib.Path('.').iterdir()    # 生成目录的可迭代对象
&lt;generator object Path.iterdir at 0x7fef228979e8&gt;
&gt;&gt;&gt; [x for x in pathlib.Path('.').iterdir()]
[PosixPath('test.py'), PosixPath('test')]

```

#### Path.cwd()

```
&gt;&gt;&gt; os.getcwd()
'/root/workspace/python3_learning'
&gt;&gt;&gt; str(pathlib.Path().cwd())
'/root/workspace/python3_learning'

```

#### Path.resolve()

类似于 os.path.abspath()，一般可以用来查找软链接文件对应的真实文件。不过 Path.resolve() 似乎一直返回的绝对路径，os.readlink() 如果读取到真实文件就在当前目录，就不返回绝对路径了。**推荐先使用  来解析符号链接以及消除 `".."` 组件。**

```
&gt;&gt;&gt; import pathlib
&gt;&gt;&gt; pathlib.Path('test.py').resolve()
PosixPath('/root/workspace/python3_learning/test.py')
&gt;&gt;&gt; pathlib.Path('test.py.link').resolve()
PosixPath('/root/workspace/python3_learning/test.py')

&gt;&gt;&gt; import os
&gt;&gt;&gt; os.readlink('test.py.link')
'test.py'
&gt;&gt;&gt; os.readlink(os.path.abspath('test.py.link'))
'test.py'
&gt;&gt;&gt; os.path.abspath('test.py.link')
'/root/workspace/python3_learning/test.py.link'
&gt;&gt;&gt; os.path.abspath(os.readlink('test.py.link'))
'/root/workspace/python3_learning/test.py'

```

```
[root@master python3_learning]# ll
total 76
-rw-r--r--. 1 root root   422 Mar 10 09:55 test.py
lrwxrwxrwx. 1 root root     7 Feb  3 17:37 test.py.link -&gt; test.py
lrwxrwxrwx. 1 root root    13 Mar 11 09:01 test.sh.link -&gt; /root/test.sh
-rwxr-xr-x. 1 root root     0 Feb  3 18:31 test.txt


&gt;&gt;&gt; os.path.abspath(os.readlink('test.sh.link'))
'/root/test.sh'
&gt;&gt;&gt; str(pathlib.Path('test.sh.link').resolve())
'/root/test.sh'
&gt;&gt;&gt; os.readlink('test.py.link')
'test.py'
&gt;&gt;&gt; str(pathlib.Path('test.py.link').resolve())
'/root/workspace/python3_learning/test.py'
```

#### Path.exists()

```
&gt;&gt;&gt; pathlib.Path('test.py').exists()
True
&gt;&gt;&gt; pathlib.Path('tet.py').exists()
False
```

#### Path.is_dir()

```
&gt;&gt;&gt; pathlib.Path('test.py').is_dir()
False
&gt;&gt;&gt; pathlib.Path('test3').is_dir()
True

```

#### Path.is_file()

```
&gt;&gt;&gt; pathlib.Path('test.py').is_file()
True
&gt;&gt;&gt; pathlib.Path('test3').is_file()
False

```

#### Path.is_symlink()

```
&gt;&gt;&gt; pathlib.Path('test.py').is_symlink()
False
&gt;&gt;&gt; pathlib.Path('test.py.link').is_symlink()
True

```

#### Path.symlink_to()

创建一个指向已有路径的符号链接

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.link').symlink_to('test.py')
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.link').is_symlink()
True

```

#### Path.is_absolute()

```
&gt;&gt;&gt; pathlib.Path('test.py').is_absolute()
False
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').is_absolute()
True

```

#### Path.joinpath()

```
&gt;&gt;&gt; str(pathlib.Path('/root').joinpath('hello', 'world'))
'/root/hello/world'
&gt;&gt;&gt; pathlib.Path('/root').joinpath('hello', 'world').name
'world'
&gt;&gt;&gt; pathlib.Path('/root').joinpath('hello', 'world').parent
PosixPath('/root/hello')

```

**下面这种路径的拼接方式是不是挺简单粗暴的！！！:)**

```
&gt;&gt;&gt; pathlib.Path('/root') / 'hello'
PosixPath('/root/hello')
&gt;&gt;&gt; pathlib.Path('/root') / pathlib.Path('hello')
PosixPath('/root/hello')
&gt;&gt;&gt; pathlib.Path('/root') / pathlib.Path('hello', 'world')
PosixPath('/root/hello/world')

```

#### Path.expanduser()

```
&gt;&gt;&gt; pathlib.Path('~/workspace').expanduser()
PosixPath('/root/workspace')
```

#### Path.rename() 

```
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').glob('*.py'))
[PosixPath('/root/workspace/python3_learning/test.py')]
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').rename('test2.py')
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').glob('*.py'))
[PosixPath('/root/workspace/python3_learning/test2.py')]

```

#### Path.replace()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test2.py').replace('test.py')
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').glob('*.py'))
[PosixPath('/root/workspace/python3_learning/test.py')]

```

#### Path.write_text()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').write_text('hello world')
11
[root@master python3_learning]# cat test.py
hello world

```

#### Path.read_text() 

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').read_text()
'hello world'

```

#### Path.rmdir()

只可以删除空目录

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test').rmdir()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib64/python3.6/pathlib.py", line 1292, in rmdir
    self._accessor.rmdir(self)
  File "/usr/lib64/python3.6/pathlib.py", line 387, in wrapped
    return strfunc(str(pathobj), *args)
OSError: [Errno 39] Directory not empty: '/root/workspace/python3_learning/test'
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test2').rmdir()

```

#### Path.touch()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').touch()

```

#### Path.unlink()

删除文件或符号链接

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.link').unlink()
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').unlink()
```

#### Path.owner()

```
&gt;&gt;&gt; pathlib.Path('/home/looking').owner()
'looking'
&gt;&gt;&gt; pathlib.Path('/root').owner()
'root'

```

#### Path.group()

```
&gt;&gt;&gt; pathlib.Path('/home/looking').group()
'looking'
&gt;&gt;&gt; pathlib.Path('/root').group()
'root'

```

#### Path.name

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').name
'test.py'

```

#### Path.stem 

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').stem
'test'
```

#### Path.parent

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').parent
PosixPath('/root/workspace/python3_learning')
```

#### Path.parents

```
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/test.py').parents)
[PosixPath('/root/workspace/python3_learning'), PosixPath('/root/workspace'), PosixPath('/root'), PosixPath('/')]
```

#### Path.suffix

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').suffix
'.py'

```

#### Path.suffixes

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py.bak').suffixes
['.py', '.bak']

```

#### Path.parts

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').parts
('/', 'root', 'workspace', 'python3_learning', 'test.py')
```

#### Path.root

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').root
'/'

```

#### Path.with_name()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').with_name('hello.py')
PosixPath('/root/workspace/python3_learning/hello.py')

```

#### Path.with_suffix()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').with_suffix('.rb')
PosixPath('/root/workspace/python3_learning/test.rb')
```

#### Path.match()

```
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').match('*.py')
True
&gt;&gt;&gt; pathlib.Path('/root/workspace/python3_learning/test.py').match('*.rb')
False

```

#### Path.glob()

解析相对于此路径的通配符 **pattern**，产生所有匹配的文件。使用 *.py 的话会在当前目录匹配，使用 */*.py 会在相对于当前目录的二级目录进行匹配。使用 ** 会启用递归匹配（很实用的），比如查找当前目录及所有子目录使用 **，使用 **/*.py 则会匹配目录下所有 py 文件。

```
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').glob('*.py'))
[PosixPath('/root/workspace/python3_learning/world.py'), 
PosixPath('/root/workspace/python3_learning/ip-address.py'), 
PosixPath('/root/workspace/python3_learning/test.py'), 
PosixPath('/root/workspace/python3_learning/minio_client.py'), 
PosixPath('/root/workspace/python3_learning/test2.py'), 
PosixPath('/root/workspace/python3_learning/find_symbolic_links.py')]
```

#### Path.rglob()

比 glob 多了一个 r，r 表示递归（recursive）的意思。下面这两种通配方式等价。

```
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').rglob('*.py'))
[PosixPath('/root/workspace/python3_learning/world.py'), 
PosixPath('/root/workspace/python3_learning/ip-address.py'), 
PosixPath('/root/workspace/python3_learning/test.py'), 
PosixPath('/root/workspace/python3_learning/minio_client.py'), 
PosixPath('/root/workspace/python3_learning/test2.py'), 
PosixPath('/root/workspace/python3_learning/find_symbolic_links.py'), 
PosixPath('/root/workspace/python3_learning/test3/test.py')]

```

"`**`" 模式表示 “此目录以及所有子目录，递归”。换句话说，它启用递归通配。 

```
&gt;&gt;&gt; list(pathlib.Path('/root/workspace/python3_learning/').glob('**/*.py'))
[PosixPath('/root/workspace/python3_learning/world.py'), 
PosixPath('/root/workspace/python3_learning/ip-address.py'), 
PosixPath('/root/workspace/python3_learning/test.py'), 
PosixPath('/root/workspace/python3_learning/minio_client.py'), 
PosixPath('/root/workspace/python3_learning/test2.py'), 
PosixPath('/root/workspace/python3_learning/find_symbolic_links.py'),
PosixPath('/root/workspace/python3_learning/test3/test.py')]
```




