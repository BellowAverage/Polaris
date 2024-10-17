
--- 
title:  JavaScript编程基础 – 关键字Let, Const和Var的区别 
tags: []
categories: [] 

---
## JavaScript编程基础 – 关键字Let, Const和Var的区别

### JavaScipt Programming Essentials -

#### The Differences Between The Keywords Let, Const and Var in JavaScript

>  
 传统的JavaScript编程语言，无一例外地可以利用var关键字来声明变量；但是，近些年来，尤其是从ECMAScript 2015（即ES6版本）开始，人们可以使用 var、let 和 const 这 3 个关键字声明变量。 ES6带来的额外关键字，就是let和const。 


在本文中，将简要介绍 var、let 和 const 关键字之间的区别。也将简要讨论每个关键字的范围和相关概念。

JavaScript var 关键字：var 是 JavaScript 中声明变量的最古老的关键字。 因此，最初学习JavaScript编程的时候，通用变量都用Var来声明，例如声明一个name变量， var name;

后来，为什么会出现let和const呢？让我们首先来看以下作用域的应用

作用域，实际上是变量起作用的范围；它分为全局作用域或函数作用域。

### 1. var关键字

var 关键字的作用域是全局作用域或函数作用域。这意味着既可以在函数外部定义的变量进行全局访问，又可以在函数内部访问在特定函数内部定义的变量。

**示例代码1：** 变量“a”是全局（globally）声明的。因此，变量“a”的作用域是全局的，并且可以在程序中的任何位置访问它。Console.log()语句得到控制台输出。

```
var a = 10
function myFunction() {<!-- -->
    console.log(a)
}
myFunction();
console.log(a);

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/09a8b8fd2c044b659f505f2e335d09e6.png" alt="在这里插入图片描述">

**示例代码 2：** 变量“a”在函数内部声明。如果用户尝试在函数外部访问它，系统会报错。 用户可以使用 var 关键字声明 2 个同名变量。此外，用户可以将值重新分配到 var 变量中。控制台显示输出结果。

```
function theFunction() {<!-- --> 
    var a = 10;
    console.log(a)
}
theFunction();
 
console.log(a);

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/343b2096c49c467c93e1ab4efdd0c343.png" alt="在这里插入图片描述"> 函数体外的console.log(a)语句报错为ReferenceError: a is not defined( 引用错误：未定义的a)

**示例代码3**：用户可以使用 var 重新声明变量，并且可以更新 var 变量。同样在控制台输出结果。

```
var a = 11;

```

将a在函数体外声明并初始化成不同的值，输出结果如下图：

<img src="https://img-blog.csdnimg.cn/ee2c42bf9def4fc994ccaa83209411ba.png" alt="在这里插入图片描述"> **示例代码 4**：还有一种可能，假如用户在声明之前就使用 var 变量，则该变量将使用未定义的值(undefined)进行初始化，并在控制台显示输出结果。 例如：

```
console.log(a);
var a = 12;

```

#### 2. let关键字

JavaScript let 关键字是 var 关键字的改进版本。 作用域为块作用域：let 变量的作用域仅为块作用域。它不能在特定块 （{block}） 之外访问。让我们看看下面的例子。

**示例代码 1**：控制台显示输出结果。

```
let a = 10;
function theFunc() {<!-- -->
    let b = 9;
    console.log(b);
    console.log(a);
}
theFunc();

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/76bca44dedf54667842bce7ca8d5ad78.png" alt="在这里插入图片描述"> **示例 代码2**：以下代码会返回错误，因为我们正在访问功能块外部的 let 变量。控制台显示输出结果。

```
let a = 10;
function thefunc() {<!-- -->
    if (true) {<!-- -->
        let b = 9
 		console.log(b);
}
Console.log(b);
}
thefunc();
console.log(a);

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/71aa5b8074a74178a72ee0230041dc4a.png" alt="在这里插入图片描述">

**示例代码 3**：用户不能够重新声明使用 let 关键字定义的变量，但可以更新它的值。 1） 允许的操作

```
let a = 10;
a = 15;

```

2） 禁止的操作

```
let a = 10;
let a = 15;

```

**示例代码 4**：用户可以使用 let 关键字在不同的块中声明具有相同名称的变量。

```
let a = 10
if (true) {<!-- -->
let a = 9
console.log(a)  
}
console.log(a) 

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/503c7e500fcf414b81823e133d205a34.png" alt="在这里插入图片描述"> **示例代码 5**：如果用户在声明之前就使用 let 变量，那么，它不会像 var 变量那样使用 undefined 进行初始化，会返回错误。 <img src="https://img-blog.csdnimg.cn/5f667c50672249d5946052ba9398b915.png" alt="在这里插入图片描述">

#### 3. Const关键字

JavaScript 中的 const 关键字，具有与 let 关键字相同的所有属性，但用户无法修改更新它；换句话说，它相当于常量。

作用域：块作用域。当用户声明一个 const 变量时，需要初始化它，否则会返回错误。一旦声明了 const 变量，用户就无法对其进行更新。

**示例代码 1**：我们正在更改 const 变量的值，使其返回错误。控制台显示输出结果。

```
const a = 10;
function thefunc() {<!-- -->
    a = 9;
    console.log(a);
}
thefunc();

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/1cfda051713c4d1488193e3669608167.png" alt="在这里插入图片描述"> 上图中显示TypeError（类型错误：为常量赋值）。

**示例代码 2**：用户无法更改 const 对象的属性，但可以更改 const 对象的属性值。

```
const a = {<!-- -->
    prop1: 10,
    prop2: 9
}
a.prop1 = 3;
 
a = {<!-- -->
    b: 10,
    prop2: 9
}

```

运行结果如下： <img src="https://img-blog.csdnimg.cn/585b5ad9f3284bd1ac749ff7c789b117.png" alt="在这里插入图片描述"> 出现**TypeError:Assignment to constant variable**.(类型错误：为常量赋值) a作为const类型对象，被重新赋值时报错。

根据以上示例代码，将三种关键字的区别小结如下： 1） **var变量的作用域**，是函数的作用域；它在作用域内能被更新和重新声明；未初始化时为undefined类型，此时也能被访问； 2） **let变量的作用域是块作用域**；它能被更新但不能够被在作用域里重复声明；可以无初始化声明；未初始化时，它不能被访问，否则报错”reference error”; 3） **const变量的作用域是块作用域**；在块内，它不能被更新或重复声明；未初始化它不能被声明；它不能被访问（未初始化）；未初始化时它不能被声明。

#### 结束语

有时，用户在使用 var 变量时会遇到问题，因为他们在特定块中更改了它的值。因此，用户应该使用 let 和 const 关键字在 JavaScript 中声明变量；这样也符合及遵守ES6的标准。

喜欢就点赞哈。😊 技术好文陆续推出，敬请关注。

相关阅读： 1. 2. 
