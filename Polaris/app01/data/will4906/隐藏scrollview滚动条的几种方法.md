
--- 
title:  隐藏scrollview滚动条的几种方法 
tags: []
categories: [] 

---
xml修改：  android:scrollbars = “none”  即可

java代码动态修改  1、setScrollBarSize(0)，将scrollbar的大小设为0就看不见了  2、setHorizontalScrollBarEnabled(false) 这个是horizontalscrollview的，scrollview应该有类似的。
