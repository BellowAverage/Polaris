
--- 
title:  Python修改文件名 
tags: []
categories: [] 

---
## 一.替换文件名称

示例：删掉文件名中的`.2019`，即替换`.2019`为空`replace('.2019', '')`

```
import os

# 文件路径
path = 'D:\\庆余年'

# 要替换的字段
rpc = '.2019'

# 获取路径内文件
file = os.listdir(path)

for i in range(len(file)):
    # 原文件名
    n1 = path + '\\' + file[i]
    # 新文件名
    n2 = n1.replace(rpc, '')
    # 调用改名函数，完成改名操作
    os.rename(n1, n2)

# 输出结束的提示信息
print('Over'.center(20, '='))

```

## 二.添加文件名前缀

开始时需要输入1或者2，来实现replace替换文件名称或add添加文件名前缀

```
import os

type_ = input('Replace名称输入1, Add前缀输入2: ')

path = 'E:\\人间正道是沧桑'

# 要被替换的
rpc = '人间正道是沧桑人间正道是沧桑'

# 替换成的名称，前缀的名称
rpc_result = '人间正道是沧桑'

file = os.listdir(path)

for i in range(len(file)):
    # 原文件名
    n1 = path + '\\' + file[i]

    if type_ == '1':
        # 替换成新文件名
        n2 = n1.replace(rpc, rpc_result)
    elif type_ == '2':
        # 添加文件名新文件名
        n2 = path + '\\' + rpc_result + file[i]

    # 调用所导入模块中的改名函数，完成具体改名操作
    os.rename(n1, n2)

print('Over'.center(20, '='))

```
