
--- 
title:  【Unity3D】伽马校正 
tags: []
categories: [] 

---
#### 1 伽马相关概念

##### 1.1 人眼对亮度变化的感知

人眼对亮度变化的感知不是线性的，如下图，人眼对亮区的亮度变化不太敏感，对暗区的亮度变化较敏感。另外，我们可以想象一下，在一个黑暗的房间里，由 1 根蜡烛到 2 根蜡烛的变化，我们很容易感知到，但是由 100 根蜡烛到 101 根蜡烛的变化，我们就不容易感知到。因此，对于固定的存储空间，我们应该给暗区分配更多的存储空间，而给亮区少分配些空间，这样能让更多的细节在暗区呈现，而亮区不必呈现太多细节（因为人眼感知不到亮区的细微变化，呈现太多细节只会浪费空间）。

<img src="https://img-blog.csdnimg.cn/771f32b4156b4d988249d7fb10ec15b9.png" alt="">

##### 1.2 伽马编码和伽马解码

**1）伽马函数**

公式如下，因其指数部分 γ 读音为伽马（gamma）而来。

<img src="https://img-blog.csdnimg.cn/87fdfe02cc6f476baa60db049e71df5e.png" alt="">

当 0 &lt; γ &lt; 1 时，伽马函数的图像从左往右逐渐平缓，通常作为伽马编码处理；当 γ &gt; 1 时，伽马函数的图像从左往右逐渐陡峭，
