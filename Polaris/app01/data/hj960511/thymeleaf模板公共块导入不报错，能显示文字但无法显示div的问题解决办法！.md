
--- 
title:  thymeleaf模板公共块导入不报错，能显示文字但无法显示div的问题解决办法！ 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解thymeleaf模板公共块导入时，没有任何报错信息，但是进行排查后发现能够显示文字，改成html标签后就无法显示div的问题解决办法！ 日期：2024年3月24日 作者：任聪聪 


## 问题现象：

说明：代码好好的，引入的路径也是对的，可以显示文字，但不可以div，自定义公共模板输入了就不行！

```
&lt;!DOCTYPE html&gt;
&lt;html xmlns:th="http://www.thymeleaf.org"&gt;
&lt;head&gt;
    &lt;th:block th:replace="fragments/xxxx::xxxxxx"&gt;
```
