
--- 
title:  vue + ts 使用watch监听对象的某个属性 
tags: []
categories: [] 

---
>  
 immediate和deep，默认值为false,代表立即实行和深度监听 immediate为true的时候，会刚开始时就执行一次，比如第一次渲染该页面 deep为true时，代表同时监听对象内部属性情况，内部变化，也会触发该函数 


```
  @Watch("addForm.startTime", {<!-- --> immediate: true, deep: true })
  onStartTimeChange(newVal, oldVal) {<!-- -->
     console.log(newVal + ',' + oldVal);
   }

```
