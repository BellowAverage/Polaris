
--- 
title:  Python版本与opencv版本的对应关系 
tags: []
categories: [] 

---
python版本要和opencv版本相对应，否则安装的时候会报错。

可以到上面查看python版本和opencv版本的对应关系，如图，红框内是python版本，绿框内是opencv版本。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/direct/84bbbdb69e5f4769979766c4b146b6db.png" width="1200">

查看自己的python版本后，使用下面命令进行opencv安装：

```
pip install opencv-python==3.4.9.33  # 此处 opencv 版本要和 python 版本对应，否则报错
```

安装 opencv-contrib-python，相当于加了一些额外拓展，比如一些特征提取的算法，在直接的 opencv 中是没有的，需要额外装这个扩展包。  

```
pip install opencv-contrib-python==3.4.9.33  # 版本号要与opencv 版本号一致
```


