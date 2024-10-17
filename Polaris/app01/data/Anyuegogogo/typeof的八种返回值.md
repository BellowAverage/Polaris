
--- 
title:  typeof的八种返回值 
tags: []
categories: [] 

---
>  
 JavaScript 里面，typeof运算符只可能返回八种结果，而且都是字符串。 


```
typeof undefined; // "undefined"
typeof true; // "boolean"
typeof 1337; // "number"
typeof "foo"; // "string"
typeof {<!-- -->}; // "object"
typeof parseInt; // "function"
typeof Symbol(); // "symbol"
typeof 127n // "bigint"

```

需要注意的是：

```
typeof null // "object"
typeof [1] // "object"

```
