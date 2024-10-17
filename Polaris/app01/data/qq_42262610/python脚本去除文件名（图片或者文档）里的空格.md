
--- 
title:  python脚本去除文件名（图片或者文档）里的空格 
tags: []
categories: [] 

---
```
import os
 
filepath="image" # 文件目录名
zimulus = os.listdir(filepath)
 
for musicname in zimulus:#改目录下的文件名
    oldmusicpath = filepath +'\\' + musicname
    newmusicname = musicname.replace(' ','')
    newmusicpath = filepath +'\\' + newmusicname
    os.rename(oldmusicpath,newmusicpath)
print(zimulus)
```


