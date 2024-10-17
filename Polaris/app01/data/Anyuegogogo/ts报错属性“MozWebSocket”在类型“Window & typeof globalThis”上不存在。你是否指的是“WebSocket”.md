
--- 
title:  ts报错属性“MozWebSocket”在类型“Window & typeof globalThis”上不存在。你是否指的是“WebSocket”? 
tags: []
categories: [] 

---
报错信息： <img src="https://img-blog.csdnimg.cn/direct/6e37a3bc8fff4804a685d9e74391ff69.png" alt="在这里插入图片描述"> 解决： （vue项目）src文件下添加global.d.ts文件，添加申明

```
declare interface Window {<!-- -->
  WebSocket: any;
  MozWebSocket: any;
}

```
