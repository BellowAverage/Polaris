
--- 
title:  Unknown custom element: ＜el-empty＞ - did you register the component correctly? For recursive compone 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/591d7205fb294edda30ccaff7bd48a6c.png" alt="在这里插入图片描述">

#### 问题描述：＜el-empty＞未注册

未知自定义元素：＜el-empty＞您是否正确注册了组件？

#### 解决：出现此问题是因为 ElementUI 的版本太低了，需要重新安装更高版本的饿了么UI

##### 1、首先打开 ElementUI官网

 <img src="https://img-blog.csdnimg.cn/0321cd8941c0408e8dab556af0e72129.png" alt="在这里插入图片描述"> 在右上角查看版本

##### 2、使用如下命令更新版本

```
npm i element-ui@2.15.13 -S

```

##### 3、刷新网页，问题解决
