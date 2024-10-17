
--- 
title:  JavaScript编程进阶 – Return语句 
tags: []
categories: [] 

---
## JavaScript编程进阶 – Return语句

### JavaScript Programming Advanced – Return Statement

By Jackson@ML

>  
 就像人们习惯的函数一样，总觉得在函数体最后需要一个return语句，标志着函数的结束,就像下面这个函数 theFunc() 那样。 


```
function theFunc() {<!-- --> 
	return 0
} 

```

本文简要介绍一下可选的return语句，以及用return语句返回函数(而不是具体数值)的例子。希望对您有所帮助。

#### 1. 可选的return

让我们先来看一个JavaScript函数，符合ES5规范。这个函数用于打招呼，函数名称为：sayHello()，代码如下：

```
"use strict";
var sayHello = function sayHello() {<!-- -->
    return "Hello, world!";
};
console.log(sayHello());

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/6ee4467d8f764b7a9b913d7cc07f623f.png" alt="在这里插入图片描述"> 如果变换一下，即不用声明显示的函数，取而代之的是匿名函数，代码如下：

```
"use strict";

var sayHello = () =&gt; "Hello, world!"
console.log(sayHello());

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/fcf982cc614a423a92f17814fe926025.png" alt="在这里插入图片描述"> 由上述代码可以看到，sayHello()已经成为一个被函数被赋值的变量。而此时，并没有出现return语句。

因此，return语句在ES6中是可选的。

#### 2. 返回函数

如何把一个函数传递给另一个函数呢？既然我们讲过，函数是JavaScript中的数据，那么，就能把它从其它函数中返回，就如同其它数据类型一样。

下面有一个例子，代码如下：

```
let crazy = () =&gt; {<!-- --> return String }

let func = crazy()
console.log(func("Hello, world!"))

```

上例可以看出，crazy函数返回了一个指向String字符串函数的函数引用；在调用crazy函数时， 返回了一个String函数。

注意：它仅仅返回了函数引用，并未执行函数！

执行结果如下图所示：<img src="https://img-blog.csdnimg.cn/direct/638e22b0d04345cdb139799f497bd51b.png" alt="在这里插入图片描述"> 当然，用如下的方式执行，可能会更好些：

```
let crazy = () =&gt; {<!-- --> return String }
console.log(crazy()("Hello, world!"))

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/19ca8f8970da440f8c07e455df4fe6cd.png" alt="在这里插入图片描述">

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力！😃

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 