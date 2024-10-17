
--- 
title:  wepy项目报警告，找不到编译器：wepy-compiler-typescript 
tags: []
categories: [] 

---
网上看到有说：

```
cnpm install wepy-compiler-typescript --save-dev

```

但是我执行命令行报错：Cannot find module ‘fs/promises’ 然后用npm下载成功了

```
npm install wepy-compiler-typescript --save-dev

```

针对 Cannot find module ‘fs/promises’ 问题，看到过一篇文章，是因为node版本太低而cnpm版本太高所导致的。要么提高node版本，要么降低cnpm版本。 
