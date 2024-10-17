
--- 
title:  htmlspecialchars() 函数实例 
tags: []
categories: [] 

---
htmlspecialchars() 函数实例，htmlspecialchars() 函数把预定义的字符转换为 HTML 实体。

预定义的字符是：
- &amp; （和号）成为 &amp;- " （双引号）成为 "- ' （单引号）成为 '- &lt; （小于）成为 &lt;- &gt; （大于）成为 &gt;
提示：如需把特殊的 HTML 实体转换回字符，请使用  函数。

### htmlspecialchars() 函数语法
|参数|描述
|**string**|必需。规定要转换的字符串。



把预定义的字符 "&lt;" （小于）和 "&gt;" （大于）转换为 HTML 实体：
| 1 | `&lt;?php ``$str` `= ``"This is some &lt;b&gt;bold&lt;/b&gt; text."``; ``echo` `htmlspecialchars(``$str``); ?&gt;` 

`&lt;?php ``$str` `= ``"This is some &lt;b&gt;bold&lt;/b&gt; text."``; ``echo` `htmlspecialchars(``$str``); ?&gt;`

上面代码的 HTML 输出如下（查看源代码）：

>  
 &lt;!DOCTYPE html&gt; &lt;html&gt; &lt;body&gt; This is some &amp;lt;b&amp;gt;bold&amp;lt;/b&amp;gt; text. &lt;/body&gt; &lt;/html&gt; 


上面代码的浏览器输出如下：

>  
 This is some &lt;b&gt;bold&lt;/b&gt; text. 


**htmlspecialchars() 函数定义和用法**

`htmlspecialchars()`函数把一些预定义的字符转换为 HTML 实体。

<img alt="" height="300" src="https://img-blog.csdnimg.cn/1ecfcea0e4c24fa9a8f0713e3b73ef27.png" width="748">

 
