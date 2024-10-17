
--- 
title:  axios请求拦截，token失效，多个请求报错导致多次显示弹框的问题 
tags: []
categories: [] 

---
>  
 token失效，请求头中需要带上token的请求就会报错，axios的请求拦截中会对异常做处理并显示弹框。如果同时多个请求报错就会显示多个弹框。这样很影响用户体验，我们只需要弹出框弹出一次。 以下是解决方法： 


```
// 设置一个变量
let tokenAbnormal = false;
// 下面是部分异常处理的代码
// 异常处理
if (res.statusCode === 401 || res.statusCode === 402 || res.statusCode === 403 || res.statusCode === 400) {<!-- -->
  const tips = {<!-- -->
    400: '请重新登录',
    401: '您的帐号已解矫',
    402: '您的帐号已解除绑定，请重新登录',
    403: '您的帐号已被移出'
  }
  // token无效 清空auth缓存
  wepy.$instance.globalData.authInfo = null
  if (!tokenAbnormal) {<!-- -->
    tokenAbnormal = true
    // 弹出框
    await Tips.modal(tips[res.statusCode])
    // 设置定时器，确保下次异常时弹出框正常弹出
    setTimeout(() =&gt; {<!-- -->
      tokenAbnormal = false;
    }, 3000);
  }
  console.log('账号异常：', obj)
  wx.redirectTo({<!-- -->
    url: '/pages/login/index'
  })
}

```

如果有不对的地方，欢迎指正哦~
