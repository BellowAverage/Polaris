
--- 
title:  解决uniapp token失效跳到登录页showToast不显示 
tags: []
categories: [] 

---
```
uni.reLaunch({<!-- -->
	url: "/pages/login/login"
})
setTimeout(() =&gt; {<!-- -->
	uni.showToast({<!-- -->
		title: '请先登录',
		icon: 'none'
	})
})

```
