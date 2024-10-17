
--- 
title:  vue3想要在setup中使用this, 以及使用中遇到vue3 线上环境 ctx 无法识别问题 
tags: []
categories: [] 

---
如果要在vue3中使用this，vue为我们提供了getCurrentInstance方法，该方法返回了ctx和proxy。控制台打印出来的和vue2的this相同

```
  import {<!-- --> getCurrentInstance } from 'vue'
  // const {<!-- --> ctx } = getCurrentInstance() as any;
  // 而出现 线上环境 ctx 无法识别问题 解决如下：
  const {<!-- --> proxy  } = getCurrentInstance() as any;

```
