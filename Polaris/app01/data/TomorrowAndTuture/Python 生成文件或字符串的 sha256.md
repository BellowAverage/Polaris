
--- 
title:  Python 生成文件或字符串的 sha256 
tags: []
categories: [] 

---
例子当然要简洁，废话当然要少说，这块主要以 sha256 为例来进行说明，当然你可以选择 sha512 、md5 等其他算法！

### 文件的 sha256

这里唯一要注意的一点：**文件一定要以二进制的形式打开读取！**

```
import hashlib

path = 'setup.py'
algorithm = hashlib.sha256()  # hashlib.sha512()  or hashlib.md5()
with open(path, 'rb') as f:
    algorithm.update(f.read())
print(algorithm.hexdigest(), path)
```

如果读取的文件比较大的话，可以尝试分片读取：

```
import hashlib
import os

path = 'setup.py'
algorithm = hashlib.sha256()
size = os.path.getsize(path)
with open(path, 'rb') as f:
    while size &gt;= 1024 * 1024:
        algorithm.update(f.read(1024 * 1024))
        size -= 1024 * 1024
    algorithm.update(f.read())
print(algorithm.hexdigest(), path)
```

```
74765dc4880fe7759c0206e2bcfe30c8d3e8e305526434b4c62d6c6ed2141c12 setup.py
```

可以看到，结果和直接在 Linux 上使用 sha256sum命令（如果使用 sha512 或 md5 算法，在 Linux 请用 sha512sum 或 md5sum 生成哈希码）得到的结果一致： 

```
[root@master test]# sha256sum setup.py 
```

```
74765dc4880fe7759c0206e2bcfe30c8d3e8e305526434b4c62d6c6ed2141c12  setup.py
```

### 字符串的 sha256

这里唯一要注意的一点：**字符串一定要先编码，即使是空字符串也不例外（和文件要以二进制形式读取的原因类似）！**

```
import hashlib
text = 'hello world'
algorithm = hashlib.sha256()
algorithm.update(text.encode(encoding='UTF-8'))
print(algorithm.hexdigest(), text)
```

```
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9 hello world
```

不然的话会报错：

```
Traceback (most recent call last):
  File "D:/Projects/insight-tools-rest/test.py", line 4, in &lt;module&gt;
    algorithm.update(text)
TypeError: Unicode-objects must be encoded before hashing
```

校验的话就是多了一层比较哈希字符串的逻辑，这个我就不多啰嗦了！
