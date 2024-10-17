
--- 
title:  【前端设计】HTML+CSS+JavaScript基本特性 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>系列文章目录</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - <ul><li>-  
   </li>- - <li>-  
   </li>- - <li>- - -  
   </li>- </ul> 
  
  


## HTML (HyperText Markup Language)

### 标签与属性

HTML 使用标签来定义内容。每个标签通常都有一个开始标签和结束标签。例如，`&lt;p&gt;` 是段落标签的开始标签，`&lt;/p&gt;` 是其结束标签。

```
&lt;p&gt;这是一个段落。&lt;/p&gt;

```

许多标签还可以有属性，属性为标签提供额外的信息。例如，`&lt;a&gt;` 标签可以有 `href` 属性指定链接地址。

```
&lt;a href="https://www.example.com"&gt;访问 example.com&lt;/a&gt;

```

### 表单

HTML 中的表单允许用户输入数据：

```
&lt;form action="/submit" method="post"&gt;
    &lt;input type="text" name="username" placeholder="输入用户名"&gt;
    &lt;input type="password" name="password" placeholder="输入密码"&gt;
    &lt;input type="submit" value="登录"&gt;
&lt;/form&gt;

```

## CSS (Cascading Style Sheets)

### 选择器

CSS 使用选择器来确定哪些元素应该应用哪些样式：
- **元素选择器**：如 `h1`, `p`, `a` 等。- **类选择器**：以`.`开头，如 `.highlight`。- **ID 选择器**：以`#`开头，如 `#header`。
### 盒模型

每个 HTML 元素都可以视为一个盒子，并且有 `padding`, `border`, `margin` 和 `content`。这被称为 CSS 盒模型。

## JavaScript

### 数据类型

JavaScript 中有几种基本的数据类型：
- **Number**: 如 123, 12.3- **String**: 如 “Hello”, ‘World’- **Boolean**: `true` 或 `false`- **Object**: 如 `{ name: 'John', age: 30 }`- **Array**: 如 `[1, 2, 3]`
### 函数

函数是一组代码，可以接受参数并返回一个值：

```
function add(x, y) {<!-- -->
    return x + y;
}

```

### 事件

JavaScript 可以响应各种事件，例如点击、键盘按键、鼠标移动等。这使得网页具有交互性。

```
document.getElementById('myButton').addEventListener('click', function() {<!-- -->
    alert('按钮被点击了！');
});

```

### DOM (Document Object Model)

DOM 是一个编程接口，它表示页面的结构。通过 DOM，JavaScript 可以访问和修改页面内容。

```
// 获取一个元素
var elem = document.getElementById('myDiv');

// 修改元素内容
elem.innerHTML = '新的内容';

```

>  
 <h2> 
  <center>
    本期好书推荐 
  </center></h2> 
 <center>
   《HTML5+CSS3+JavaScript从入门到精通（微课精编版）（第2版）（清华社“视频大讲堂"大系 网络开发视频大讲堂）》 
 </center> 


>  
 京东： 当当： 


<img src="https://img-blog.csdnimg.cn/f6ce304e7b6a4fc28b5e17cf85e034d1.png" alt="在这里插入图片描述">
