
--- 
title:  Redis学习2——String数据类型的操作 
tags: []
categories: [] 

---
## Redis常用数据类型

### String

#### 数据结构

<img src="https://img-blog.csdnimg.cn/36122d0364764b6d8fa76c7ee9c28321.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e47bdee83ee24fb48886c43c3c2100a5.png" alt="在这里插入图片描述"> 有点像动态分区按边界对齐。

#### 基本操作

<img src="https://img-blog.csdnimg.cn/0de1b950216f467ea0828f5bb5cd7cae.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e2b341fb52dd44bfb8d822fb3f08a10f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/44f2c8c1045b4ce8b14ba83733ca2c1a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/0e15a9aaaff24cfabe392b741ce49cf1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2a25c1e015e949f4b088a6b9f3ea7b90.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b041cbbc757c4dd7a0b96a8f786228c9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/f49b5839fd674e7f93bfbf4a7e8c0290.png" alt="在这里插入图片描述">

也可以一次设置多个 <img src="https://img-blog.csdnimg.cn/99a4e9d469c44a4b95d8b67b91f08778.png" alt="在这里插入图片描述"> 得到范围值

<img src="https://img-blog.csdnimg.cn/c79c168a787c4dc5b6cb65a85a84914a.png" alt="在这里插入图片描述"> setrange和append的区别是宏观上看append是从尾部追加而setrange是从设置的起始位置开始的。

也可以在set时就对key设置过期时间， <img src="https://img-blog.csdnimg.cn/c4e78506d9c047ca90a1f2657213811e.png" alt="在这里插入图片描述"> 最后一个是 <img src="https://img-blog.csdnimg.cn/d1c03f8b31fa4c90b6c86e6de6415e09.png" alt="在这里插入图片描述">
