
--- 
title:  python中阿里云oss对象存储的使用 
tags: []
categories: [] 

---
## python中阿里云oss对象存储的使用

### 1.需要购买阿里云oss对象存储服务

在oss下建立文件夹filename

### 2.python交互代码

```
# -*- coding: utf-8 -*-
import oss2

# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。
# 强烈建议您创建并使用RAM账号进行API访问或日常运维，
# 请登录 https://ram.console.aliyun.com 创建RAM账号。
from itertools import islice

auth = oss2.Auth('HJH78JKJL4VJMJHHKHFHFYTACSBQ',
                 'LSJFLSJ7SJL9JSLJFBMA0SJLSJJLS')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth,
                     'http://oss-cn-beijing.aliyuncs.com',
                     'filename')

# 设置存储空间为私有读写权限。
# bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)

# 上传文件
# &lt;yourObjectName&gt;上传文件到OSS时需要指定包含文件后缀在内的完整路径，例如abc/efg/123.jpg。
# &lt;yourLocalFile&gt;由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
# for i in range(2, 5):
#     bucket.put_object_from_file('image_1/美女%d.jpg' % i, '/Users/admin/Desktop/美女%d.jpg' % i)

# 下载文件
# &lt;yourObjectName&gt;从OSS下载文件时需要指定包含文件后缀在内的完整路径，例如abc/efg/123.jpg。
# &lt;yourLocalFile&gt;由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
# bucket.get_object_to_file('image_1/1.jpg', '/Users/admin/Desktop/美女1.jpg')

# 删除文件
# &lt;yourObjectName&gt;表示删除OSS文件时需要指定包含文件后缀在内的完整路径，例如abc/efg/123.jpg。
# bucket.delete_object('video/七朵组合-玉生烟.mkv')

# 列举文件
# oss2.ObjectIteratorr用于遍历文件。
for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)


```
