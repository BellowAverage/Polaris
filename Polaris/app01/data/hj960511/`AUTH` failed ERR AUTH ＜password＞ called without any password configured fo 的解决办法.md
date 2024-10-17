
--- 
title:  `AUTH` failed: ERR AUTH ＜password＞ called without any password configured fo 的解决办法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解安装和更新redis报错：`AUTH` failed: ERR AUTH called without any password configured fo 的解决办法。 日期：2023年10月27日 作者：任聪聪 


## 问题现象：
1. 提示报错为：
```
`AUTH` failed: ERR AUTH &lt;password&gt; called without any password configured fo 

```

2.服务器页面打开报错：500 错误 3.密码检查了发现没有错误。

## 解决办法：

说明：这个问题不是什么大问题，或许在你的日志报错中有报错权限错误，但实际上这里是没有重新加载配置，没有让redis生效导致的报错。

重启redis或者重载配置即可解决这个问题。
