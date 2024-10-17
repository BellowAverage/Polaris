
--- 
title:  相控与斩控交交调压（THD的计算） 
tags: []
categories: [] 

---
****相控与斩控交交调压（THD的计算）****

<img src="https://img-blog.csdnimg.cn/direct/6313d4ecdc124c56978f330357521e56.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/d80d816aaa44407bb8276a4363bda55d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/0d42e841bbb244fe8cd5e652b14e2f84.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/113ae19e998a4f7e8b2bd6fdb4f0f52d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/ebe1d1ec412a478a96b826314990e919.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b5d93aec40c345cd9499978e66423854.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1744e952f4684ab7a5dbf35e448bf30d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/350a7348414d4439be124f3a71616f2a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/4bea960ce0094f2ca2cf0b4774da2278.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/82f3fc3b6742458c955fae0e83f48bd1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/28d4c4293379438fb825237027f77258.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/ec7c50a62ea44a1abc5a68683435d5c7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/44dd74c3cd9c4c8193f535f7cb903088.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1a0637ab80cb4a7e8a486ddc2011a3a8.png" alt="在这里插入图片描述">

然后需要用滤波器进行滤波

<img src="https://img-blog.csdnimg.cn/direct/5ee041a24e2d4e04887d1e85287d57e5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/2efe0b5e55304c4983c4d2aa6e730663.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/0c3ac512e6de4c58b7714e7e813c43ed.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/0e8fe690efca4ad09d9c4eaf74b7b87b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a313d9e97831480eae0e9349ace0f867.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a2766998a21c4eb3812e1d909d07e470.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/45b7a136024f42cfb5e63236f7848a70.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/19efbb340e7d4f2291aac0a322ed1637.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/779956e81fef40be93885e77e158c77e.png" alt="在这里插入图片描述">

最后对比输出的电压和电流：

<img src="https://img-blog.csdnimg.cn/direct/bb10871ef6944fd7863fe0957ca790ae.png" alt="在这里插入图片描述"> 蓝色通过加了滤波以后，稍微好很多了，近似于正弦函数。相控黄色输出的波形不太好，失真很严重，峰值还是没改变，还是311V。

改一下相控，占空比和移向角度，看看效果：

改了角度变成60，占空比变成30，看看效果：

<img src="https://img-blog.csdnimg.cn/direct/dc8f9ebc3c2d4dd4adbe14b967e7520f.png" alt="在这里插入图片描述"> 相控黄色，偏移的更严重了。
