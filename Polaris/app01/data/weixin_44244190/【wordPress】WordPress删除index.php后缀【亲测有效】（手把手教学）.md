
--- 
title:  【wordPress】WordPress删除index.php后缀【亲测有效】（手把手教学） 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>WordPress删除index.php后缀【亲测有效】（手把手教学）</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - -  
  
  


## 一、 WordPress为什么要删除index.php后缀

删除URL中的“index.php”或其他脚本文件扩展名（如“.php”，“.html”等）通常是出于以下几个原因：
1.  **美观**：没有文件扩展名的URL更加简洁，易于阅读，对用户来说更加友好。例如，`https://example.com/products` 看起来比 `https://example.com/products.php` 更加简洁。 1.  **语义化URL**：语义化URLs更易于理解，可以使内容更容易被搜索引擎识别，并且提高用户体验。例如，`https://example.com/products/shoes` 更直观地表示内容，而不是 `https://example.com/index.php?page=shoes`。 1.  **隐藏实现细节**：删除文件扩展名可以隐藏网站的技术实现细节，这对于一些安全理由来说是有益的。通过这种方式，攻击者或普通用户不容易得知您正在使用哪种编程语言或技术。 1.  **灵活性**：如果您决定更改后端技术或文件扩展名，不需要更改URL，这意味着搜索引擎的排名和任何链接到您网站的链接都不会受到影响。 1.  **搜索引擎优化 (SEO)**：虽然现代搜索引擎对URL的文件扩展名不太敏感，但简洁、结构化和语义化的URLs仍然被认为是搜索引擎优化的最佳实践。简洁的URL更有可能被用户点击，这可能会对点击率产生正面影响。 
## 二、具体操作

第一步：使用宝塔控制面板，进入你的网站，选择 ` 伪静态` ，并选择 `wordpress`，输入伪静态代码，并点击 `保存`：

<img src="https://img-blog.csdnimg.cn/13458097017c430fab0feeba08ed819a.png" alt="在这里插入图片描述"> 代码如下：

```
location /
{<!-- -->
	 try_files $uri $uri/ /index.php?$args;
}

rewrite /wp-admin$ $scheme://$host$uri/ permanent;


```

第二步：打开 `WordPress`后台管理，点击 `设置` - `固定连接` ，`自定义结构` 中删除 `/php.index/` 并点击保存。

<img src="https://img-blog.csdnimg.cn/b19df31ea9604e19bf9c68fe99e3de56.png" alt="在这里插入图片描述">

刷新页面就可以看到index.php已经消失了。

<img src="https://img-blog.csdnimg.cn/0389f845cd9c416e900bf7519e45f101.png" alt="在这里插入图片描述">
