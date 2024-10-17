
--- 
title:  [@vue/compiler-sfc] the ＞＞＞ and /deep/ combinators have been deprecated. Use :deep() instead. 
tags: []
categories: [] 

---
vue2.X版本构建版本报错：

```
[@vue/compiler-sfc] the &gt;&gt;&gt; and /deep/ combinators have been deprecated. Use :deep() instead.

```

意思是：&gt;&gt;&gt; 和 /deep/ 组合器已被弃用，需要使用 :deep() 代替。 解决办法： 锁定vue的版本号

```
"vue": "^2.5.17",
"vue-template-compiler": "^2.5.17",
// 改为
"vue": "2.5.17",
"vue-template-compiler": "2.5.17",

```

参考链接：
