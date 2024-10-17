
--- 
title:  AttributeError: ‘str‘ object has no attribute ‘items‘ 
tags: []
categories: [] 

---
### AttributeError: ‘str’ object has no attribute ‘items’

<img src="https://img-blog.csdnimg.cn/9d7139a439984eddb335d1335504bc76.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/5e43f2d2a0164d85819765031ecee566.png" alt="在这里插入图片描述">

### 原因分析

导致报错的原因是redis版本过高，对redis进行降级

```
pip uninstall redis

```

<img src="https://img-blog.csdnimg.cn/33de967f5c474eb088869219b8a2971d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/5e38bc10194b4edc98a4d910eab48395.png" alt="在这里插入图片描述">

```
pip install redis==2.10.6

```

<img src="https://img-blog.csdnimg.cn/3632c7e504a545b08ba687da0d611e41.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/bfc09bc1006a494bb4a7a1b0698c01ad.png" alt="在这里插入图片描述">
