
--- 
title:  YOLOv5训练后利用权重对特征图可视化 
tags: []
categories: [] 

---
我们可以可视化某层的特征图添加到论文中，属于锦上添花了！

小小的技巧，有需要的同学可以自取代码尝试一下。

```
python detect.py --weights best.pt --imgsz 640 --source ./data/image/ --visualize

```

运行过程中：

<img alt="" height="512" src="https://img-blog.csdnimg.cn/d7ede2a8d1314ac886336a0879b3f05a.png" width="979">



运行后即可生成特征图：

<img alt="" height="424" src="https://img-blog.csdnimg.cn/484b01cd63794b149a7a5581bcbdcf2c.png" width="213">

<img alt="" height="1140" src="https://img-blog.csdnimg.cn/9c8860acd3764739aa4cd1e0fa723d77.png" width="1200">

<img alt="" height="1093" src="https://img-blog.csdnimg.cn/d0db9ed39bbe4def8b9e4b3f1b352191.png" width="1200">







------------------今天不学习，明天变垃圾--------------------
