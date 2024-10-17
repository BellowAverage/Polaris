
--- 
title:  python-删除文件夹下后缀是.jpg的图片 
tags: []
categories: [] 

---
```
import os

images_files = os.listdir(" ")
for file in image_flies:
   if file.endswith('.jpg'):
       os.remove(os.path.join(" ", file))

```


