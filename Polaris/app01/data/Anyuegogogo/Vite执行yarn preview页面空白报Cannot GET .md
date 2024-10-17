
--- 
title:  Vite执行yarn preview页面空白报Cannot GET / 
tags: []
categories: [] 

---
因为我是直接 yarn preview 预览的，后面才知道，vite preview 实际上只是帮我们开启了一个静态 Web 服务器，并没有构建项目。需要先运行 yarn build 后，再运行 yarn preview。

```
    "build": "vue-tsc --noEmit &amp;&amp; vite build",
    "preview": "vite preview",

```
