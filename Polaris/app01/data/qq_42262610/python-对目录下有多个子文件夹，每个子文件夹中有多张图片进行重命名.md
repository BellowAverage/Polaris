
--- 
title:  python-对目录下有多个子文件夹，每个子文件夹中有多张图片进行重命名 
tags: []
categories: [] 

---
```
import os

for root, dirs, files in os.walk(" ") # 图片路径的根目录
    for d in dirs:
        path = os.path.join(root, d)
        for i, f in enumerate(path):
            os.rename(os.path.join(path, f), os.path.join(path, '{}.jpg'.format(i)))
```


