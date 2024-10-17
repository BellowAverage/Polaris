
--- 
title:  python3压缩和解压文件总结（python经典编程案例） 
tags: []
categories: [] 

---
#### 1、tar压缩和解压

```
import tarfile
from pathlib import PurePath
path = PurePath(".") / "test"

zip_path = path / "123.tar.gz"
file_path = path / "123.txt"

# 压缩
# w:gz 写入代表gz压缩，还有其他用法
with tarfile.open(zip_path, "w:gz") as tar:
    tar.add(file_path, arcname=file_path.name)

# 解压
with tarfile.open(zip_path, "r:gz") as tar:
    tar.extractall(path / "1123")

```

#### 2、7z压缩和解压

```
import py7zr  # 需要先安装：pip install py7zr
import os
from pathlib import Path

path = Path(".") / "test"
zip_path = path / "123.7z"
file_path = path / "123.txt"

# 压缩
with py7zr.SevenZipFile(zip_path, 'w') as z:
    z.writeall(file_path, arcname=os.path.basename(file_path))

# 解压
with py7zr.SevenZipFile(zip_path, mode='r') as z:
    z.extractall()

```

#### 3、zip写入压缩和解压

```
from zipfile import ZipFile
from pathlib import PurePath

path = PurePath(".") / "test"

zip_path = path / "123.zip"
file_path = path / "123.txt"

# 这里的mode, w是写入，r是读取, a是追加
# write写入的是文件的路径
with ZipFile(zip_path, "w") as f:
    f.write(file_path)  # 注意这里写入的文件的路径会和file_path保持一致
    # 建议用下面这一步
    f.write(file_path, arcname=file_path.name)  # file_path.name等同于os.path.basename

# 解压文件
with ZipFile(zip_path, "r") as f:
    print(f.namelist())  # 打印压缩包里的文件
    f.extractall('out_path')  # out_path解压位置

```

#### 4、gzip写入压缩和解压

```
import gzip
# 写
filepath = f"file.txt.gz"
content = "Hello World"
with gzip.open(filepath, 'wt') as f:
    f.write(content)

# 读
with gzip.open(filepath, 'rt') as f:
    content_read = f.read()
print(content_read)

```
