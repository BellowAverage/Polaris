
--- 
title:  Python 从 pyc 中获取编译 pyc 的 python 版本 
tags: []
categories: [] 

---
参考链接：

话不多说，直接上菜！！！ 

### 从 pyc 文件提取版本

```
import struct

PYTHON_MAGIC = {
    # Python 1
    20121: (1, 5),
    50428: (1, 6),

    # Python 2
    50823: (2, 0),
    60202: (2, 1),
    60717: (2, 2),
    62011: (2, 3),  # a0
    62021: (2, 3),  # a0
    62041: (2, 4),  # a0
    62051: (2, 4),  # a3
    62061: (2, 4),  # b1
    62071: (2, 5),  # a0
    62081: (2, 5),  # a0
    62091: (2, 5),  # a0
    62092: (2, 5),  # a0
    62101: (2, 5),  # b3
    62111: (2, 5),  # b3
    62121: (2, 5),  # c1
    62131: (2, 5),  # c2
    62151: (2, 6),  # a0
    62161: (2, 6),  # a1
    62171: (2, 7),  # a0
    62181: (2, 7),  # a0
    62191: (2, 7),  # a0
    62201: (2, 7),  # a0
    62211: (2, 7),  # a0

    # Python 3
    3000: (3, 0),
    3010: (3, 0),
    3020: (3, 0),
    3030: (3, 0),
    3040: (3, 0),
    3050: (3, 0),
    3060: (3, 0),
    3061: (3, 0),
    3071: (3, 0),
    3081: (3, 0),
    3091: (3, 0),
    3101: (3, 0),
    3103: (3, 0),
    3111: (3, 0),  # a4
    3131: (3, 0),  # a5

    # Python 3.1
    3141: (3, 1),  # a0
    3151: (3, 1),  # a0

    # Python 3.2
    3160: (3, 2),  # a0
    3170: (3, 2),  # a1
    3180: (3, 2),  # a2

    # Python 3.3
    3190: (3, 3),  # a0
    3200: (3, 3),  # a0
    3220: (3, 3),  # a1
    3230: (3, 3),  # a4

    # Python 3.4
    3250: (3, 4),  # a1
    3260: (3, 4),  # a1
    3270: (3, 4),  # a1
    3280: (3, 4),  # a1
    3290: (3, 4),  # a4
    3300: (3, 4),  # a4
    3310: (3, 4),  # rc2

    # Python 3.5
    3320: (3, 5),  # a0
    3330: (3, 5),  # b1
    3340: (3, 5),  # b2
    3350: (3, 5),  # b2
    3351: (3, 5),  # 3.5.2

    # Python 3.6
    3360: (3, 6),  # a0
    3361: (3, 6),  # a0
    3370: (3, 6),  # a1
    3371: (3, 6),  # a1
    3372: (3, 6),  # a1
    3373: (3, 6),  # b1
    3375: (3, 6),  # b1
    3376: (3, 6),  # b1
    3377: (3, 6),  # b1
    3378: (3, 6),  # b2
    3379: (3, 6),  # rc1

    # Python 3.7
    3390: (3, 7),  # a1
    3391: (3, 7),  # a2
    3392: (3, 7),  # a4
    3393: (3, 7),  # b1
    3394: (3, 7),  # b5

    # Python 3.8
    3400: (3, 8),  # a1
    3401: (3, 8),  # a1
    3410: (3, 8),  # a1
    3411: (3, 8),  # b2
    3412: (3, 8),  # b2
    3413: (3, 8),  # b4

    # Python 3.9
    3420: (3, 9),  # a0
    3421: (3, 9),  # a0
    3422: (3, 9),  # a0
    3423: (3, 9),  # a2
    3424: (3, 9),  # a2
    3425: (3, 9),  # a2
}


def magic_word_to_version(magic_word):
    if not isinstance(magic_word, int):
        magic_word = struct.unpack("&lt;H", magic_word)[0]
    return PYTHON_MAGIC[magic_word]


def pyc_file_to_magic_word(pyc_file):
    with open(pyc_file, 'rb') as f:
        magic = f.read(4)
    magic_word = int.from_bytes(magic[:2], 'little')
    return magic_word


file = r"test.pyc"
magic_number = pyc_file_to_magic_word(file)
python_version = magic_word_to_version(magic_number)
print(python_version)

```

```
C:\Users\lukaiyi\AppData\Local\Programs\Python\Python36\python.exe C:/Users/lukaiyi/insight-tools-rest/test.py
(3, 7)

Process finished with exit code 0
```

### PYTHON_MAGIC 获取方式

**授人以鱼，不如授人以渔。**PYTHON_MAGIC 其实在 importlib._bootstrap_external.py 文件的注释里边都有的，所以你只要能找到** importlib** 所在的目录位置就好了。那么，怎么找到 importlib 模块所在的路径呢？按照下边这么做就好了。

```
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import importlib
&gt;&gt;&gt; importlib.__file__
'/usr/lib64/python3.6/importlib/__init__.py'

```

```
Python 3.7.0 (default, Aug 10 2021, 10:51:33) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import importlib
&gt;&gt;&gt; importlib.__file__
'/usr/local/python3.7/lib/python3.7/importlib/__init__.py'

```

然后在 importlib 目录下，_bootstrap_external.py 就很容易找到了。

```
root@master /u/l/p/l/p/importlib# pwd
/usr/local/python3.7/lib/python3.7/importlib
root@master /u/l/p/l/p/importlib# ll
total 160K
-rw-r--r--. 1 root root  13K Aug 10 10:52 abc.py
-rw-r--r--. 1 root root  58K Aug 10 10:52 _bootstrap_external.py
-rw-r--r--. 1 root root  39K Aug 10 10:52 _bootstrap.py
-rw-r--r--. 1 root root 5.9K Aug 10 10:52 __init__.py
-rw-r--r--. 1 root root  844 Aug 10 10:52 machinery.py
drwxr-xr-x. 2 root root 4.0K Aug 10 10:52 __pycache__/
-rw-r--r--. 1 root root  13K Aug 10 10:52 resources.py
-rw-r--r--. 1 root root  12K Aug 10 10:52 util.py

```

如果你的解释器是 python3.6 ，里边的 python_magic 就更新到了 3.6，如果你的解释器是 python3.7 ，里边的 python_magic 就更新到了 3.7。



 




