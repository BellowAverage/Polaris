
--- 
title:  vue3 ＜img /＞的使用图片不显示 
tags: []
categories: [] 

---
在页面中使用img，图片死活不显示

```
// 这样写不显示
&lt;img src="/@/assets/images/info.png" alt=""&gt;

// 解决办法：先用import引入
import info from '/@/assets/images/info.png'
&lt;img :src="info" alt=""&gt;

```
