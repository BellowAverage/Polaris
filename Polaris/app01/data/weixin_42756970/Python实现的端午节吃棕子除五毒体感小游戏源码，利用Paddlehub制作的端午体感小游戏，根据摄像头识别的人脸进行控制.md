
--- 
title:  Python实现的端午节吃棕子除五毒体感小游戏源码，利用Paddlehub制作的端午体感小游戏，根据摄像头识别的人脸进行控制 
tags: []
categories: [] 

---
### 利用Paddlehub制作端午体感小游戏

#### 前言

马上要端午节,所以干脆再重写一些逻辑,做个端午节定制小游戏吧.

#### 端午特色

游戏的贴图全换成了端午节相关贴图:三种粽子造型 <img src="https://img-blog.csdnimg.cn/img_convert/59e3d71e85c250e11f5fede54e60d3fa.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/6931a42dd02eee58c216b09c0b39c7fe.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/4657bf455f8217df04ab5bf89ac020c1.png" alt=""> 雄黄酒 <img src="https://img-blog.csdnimg.cn/img_convert/c3b011eb7d8626c31ac4ec702875ccf1.png" alt=""> 以及五毒:蛇,壁虎,蜈蚣,蟾蜍,蟹子 <img src="https://img-blog.csdnimg.cn/img_convert/d730b07779e03734173e0499042914e3.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/c84944a871f68ba8ad7aabc2c8e80059.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/e3986dcb83e406c01bfba6765d85492e.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/d9f07c90c53207f0e4fb43c54b8e8c9b.png" alt=""> <img src="https://img-blog.csdnimg.cn/img_convert/2798b670a877ebe6e64a1850a3525f94.png" alt="">

其实五毒也是我在逛了粽子博物馆才看到的哈哈哈,所以虽然做的是个游戏,但是也是有一些科普的性质在里面的. 其实除了避五毒,端午节还要吃五黄,分别是:黄鳝,黄鱼,黄瓜,黄泥蛋以及雄黄酒. 故人认为端午仲夏,"五毒"大量繁殖,易咬伤人,吃了"五黄"能够抵御"五毒"的侵害. 是不是觉得又掌握了一些小知识呢~

#### 运行游戏

由于需要摄像头,所以无法在aistudio上运行 `python duanwu.py --level(optional)`

#### 游戏说明

改变了之前可以随便移动的控制方式,这次控制的小熊只能在屏幕的最低端左右移动.根据摄像头的图像,映射出X轴的位置即可. 游戏一共100秒. 吃到粽子会加100分. 吃到雄黄酒会进行一次清屏一次性加1000分,但是喝酒后会左右颠倒进入眩晕状态,要注意操作方式.在眩晕的期间,吃到粽子分值翻倍. 吃到五毒的话…会直接结束游戏,哈哈,要注意喽

#### 改进

重新设计了UIManager, ResourceManager, GameManager, BallManager等等.代码的可读性更高更简洁,耦合性则更低.

#### 代码下载


