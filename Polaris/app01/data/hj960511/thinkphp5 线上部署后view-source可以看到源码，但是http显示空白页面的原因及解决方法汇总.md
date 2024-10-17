
--- 
title:  thinkphp5 线上部署后view-source:可以看到源码，但是http显示空白页面的原因及解决方法汇总 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解：thinkphp5 项目线上部署后view-source:可以看到源码，但是http显示空白页面的原因及解决方法教程 作者：任聪聪 日期：2023年4月17日 thinkphp版本5.1 


### 现象说明：

线下测试环境，显示可以看到界面 <img src="https://img-blog.csdnimg.cn/564403394bf345e58643bb183547c90d.png" alt="在这里插入图片描述"> 部署到线上配置完毕后发现页面空白 <img src="https://img-blog.csdnimg.cn/a24c4d252df14635b1f1e01d2c7809f2.png" alt="在这里插入图片描述"> 在php中写入`echo 1232;die;` 可以看到1232 <img src="https://img-blog.csdnimg.cn/73ec4097b09c4448b7e5b6ab60fa902b.png" alt="在这里插入图片描述">

### 问题一、伪静态

#### 原因：

伪静态的规则配置错误，缺少last；break；参数。

#### 解决办法：

使用下方的正确伪静态

##### nginx用

```
location / {
   <!-- -->
	if 
```
