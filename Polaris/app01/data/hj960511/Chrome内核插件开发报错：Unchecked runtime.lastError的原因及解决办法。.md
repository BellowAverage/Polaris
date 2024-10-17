
--- 
title:  Chrome内核插件开发报错：Unchecked runtime.lastError:的原因及解决办法。 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，chrome内核插件开发时报错：Unchecked runtime.lastError: Extensions using event pages or Service Workers must pass an id parameter to chrome.contextMenus.create 的原因及解决办法。 日期：2023年6月10日 作者：任聪聪 


### 报错现象：

查看报错路径，在谷歌浏览器扩展程序界面，点击如下入口即可弹出！ <img src="https://img-blog.csdnimg.cn/e2dbe6b9496d4a25949d6ab593f7baea.png" alt="在这里插入图片描述"> 报错信息： <img src="https://img-blog.csdnimg.cn/cdd55123029e4e5791db110c70b16612.png" alt="在这里插入图片描述">

### 相关原因及解决办法

#### 原因一、插件为右键菜单功能类型，缺少声明的参数

说明：在你制作右键菜单时，没有在json文件中声明权限，又或者没有在bg.js文件中填写完整参数。

##### 解决办法：

```
  "permissions": [
    
```
