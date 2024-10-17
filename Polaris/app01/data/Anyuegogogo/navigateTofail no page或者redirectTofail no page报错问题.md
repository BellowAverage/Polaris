
--- 
title:  navigateTo:fail no page或者redirectTo:fail no page报错问题 
tags: []
categories: [] 

---
>  
 前段时间小程序项目的一个页面跳转突然出现了问题，在此之前这部分的代码一直是好的，突然就页面跳转不过去了。并且还时好时坏，有时候突然能跳转，但大部分时候不能跳转。 无论是用navigateTo还是redirectTo都会报错fail no page，后面发现原因如下。 


之前的老代码是如下这个逻辑

```
wx.navigateBack({<!-- -->delta: 1}) 
// 紧接着调了个异步函数，在异步函数成功后
fn()

...

async fn() {<!-- -->
   await ...
   // 成功后
   wx.redirectTo({<!-- -->
     url: '...',
   })
}

```

其实页面的跳转是异步的，所以上面就有个异步的顺序问题，如果两个页面同时跳转就很容易出现上述问题。 解决方式可以是在第一个页面跳转前面加一个await , 或者是在前一个页面跳转的成功回调里面再执行第二步操作。

```
// (1)
await wx.navigateBack({<!-- -->delta: 1}) 

// (2)
wx.navigateBack({<!-- --> 
 delta: 1, // 回退前 delta(默认为1) 页面 
 success: function (res) {<!-- --> 
 // success 
 fn()
 }, 
 fail: function () {<!-- --> 
 // fail 
 }, 
 complete: function () {<!-- --> 
 // complete 
 } 
 })

```
