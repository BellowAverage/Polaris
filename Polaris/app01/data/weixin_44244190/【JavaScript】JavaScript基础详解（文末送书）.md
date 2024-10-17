
--- 
title:  【JavaScript】JavaScript基础详解（文末送书） 
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
  - - - - <ul><li> 
   </li>- - <li>- - - - - - - -  
   </li>- - <li>- - -  
   </li>- - - </ul> 
  
  


## 一、变量声明

在 JavaScript 中，可以使用三种方式来声明变量：
<li> `var`: 这是传统的方式，但在 ES6 (ECMAScript 2015) 之后，它的使用开始逐渐被限制在函数作用域。 <pre><code class="prism language-javascript">var name = "ChatGPT";
</code></pre> </li><li> `let`: 从 ES6 开始引入，允许你声明块级作用域的变量。 <pre><code class="prism language-javascript">let age = 5;
</code></pre> </li><li> `const`: 同样从 ES6 开始引入，用于声明不可变的变量（常量）。一旦给它赋值，你就不能再更改它。 <pre><code class="prism language-javascript">const PI = 3.141592653589793;
</code></pre> </li>
## 二、数据类型
<li> **Number**：表示数值。 <pre><code class="prism language-javascript">let x = 123;
let y = 3.14;
</code></pre> </li><li> **String**：表示文本。 <pre><code class="prism language-javascript">let greeting = "Hello, World!";
</code></pre> </li><li> **Boolean**：表示真或假。 <pre><code class="prism language-javascript">let isTrue = true;
let isFalse = false;
</code></pre> </li><li> **Object**：用于存储键值对。 <pre><code class="prism language-javascript">let person = {<!-- -->firstName: "John", lastName: "Doe"};
</code></pre> </li><li> **Array**：用于存储元素的列表。 <pre><code class="prism language-javascript">let fruits = ["Apple", "Banana", "Cherry"];
</code></pre> </li><li> **null**：表示没有值。 <pre><code class="prism language-javascript">let emptyValue = null;
</code></pre> </li><li> **undefined**：表示变量已声明但尚未赋值。 <pre><code class="prism language-javascript">let testVar;
console.log(testVar); // 输出: undefined
</code></pre> </li>
### 三、控制结构
<li> **If 语句**： <pre><code class="prism language-javascript">if (age &gt; 18) {<!-- -->
    console.log("Adult");
} else {<!-- -->
    console.log("Child");
}
</code></pre> </li><li> **For 循环**： <pre><code class="prism language-javascript">for (let i = 0; i &lt; 5; i++) {<!-- -->
    console.log(i);
}
</code></pre> </li><li> **函数声明**： <pre><code class="prism language-javascript">function greet(name) {<!-- -->
    console.log("Hello, " + name);
}
</code></pre> </li>
## 四、函数

JavaScript 中的函数是其核心概念之一。函数允许将代码块组织在一起并在需要的地方调用它。

### 1. 函数声明

这是定义函数的一种方式，使用 `function` 关键字 followed by the function’s name:

```
function sayHello() {<!-- -->
    console.log("Hello, World!");
}

```

### 2. 函数表达式

函数也可以使用表达式来定义，并赋值给一个变量。这样的函数通常是匿名的（没有名称）：

```
const sayGoodbye = function() {<!-- -->
    console.log("Goodbye, World!");
};

```

### 3. 箭头函数（ES6）

从 ES6 开始，JavaScript 引入了箭头函数，为我们提供了定义函数的另一种简洁方式：

```
const add = (a, b) =&gt; a + b;

```

### 4. 参数

你可以将值传递给函数，这些值称为参数。函数可以接受多个参数：

```
function greet(firstName, lastName) {<!-- -->
    console.log("Hello, " + firstName + " " + lastName);
}

```

### 5. 默认参数（ES6）

如果调用函数时缺少参数，你可以为函数参数设置默认值：

```
function greet(name = "World") {<!-- -->
    console.log("Hello, " + name);
}

```

### 6. 返回值

使用 `return` 语句从函数返回一个值：

```
function square(number) {<!-- -->
    return number * number;
}

```

### 7. 函数作为参数

在 JavaScript 中，函数是第一类对象，这意味着你可以将函数作为另一个函数的参数：

```
function calculate(x, y, operation) {<!-- -->
    return operation(x, y);
}

const result = calculate(5, 3, (a, b) =&gt; a + b); // 8

```

### 8. 立即调用的函数表达式（IIFE）

这是一个定义后立即执行的函数：

```
(function() {<!-- -->
    console.log("This function runs as soon as it's defined!");
})();

```

### 9. 闭包

闭包是一个函数与其相关的词法作用域捆绑在一起。这使得函数可以访问其外部函数的变量，即使外部函数已经完成了执行：

```
function outerFunction() {<!-- -->
    let outerVariable = "I'm from outer function!";
    return function() {<!-- -->
        console.log(outerVariable);
    };
}

const innerFunction = outerFunction();
innerFunction(); // 输出: "I'm from outer function!"

```

## 五、类

JavaScript 支持面向对象编程，并且在 ES6 (ECMAScript 2015) 之后，正式引入了 `class` 语法来模拟经典的面向对象语言中的类的概念。尽管之前的版本中 JavaScript 使用了基于原型的继承，但 ES6 的 `class` 提供了一种更直观和结构化的方式来创建对象和处理继承。

以下是使用 JavaScript `class` 的一些基本概念：

### 1. 类的声明

你可以使用 `class` 关键字来声明一个类：

```
class Person {<!-- -->
    constructor(name, age) {<!-- -->
        this.name = name;
        this.age = age;
    }

    greet() {<!-- -->
        console.log(`Hello, my name is ${<!-- -->this.name} and I am ${<!-- -->this.age} years old.`);
    }
}

const john = new Person('John', 30);
john.greet(); // 输出: Hello, my name is John and I am 30 years old.

```

### 2. 继承

使用 `extends` 关键字可以从另一个类继承：

```
class Employee extends Person {<!-- -->
    constructor(name, age, jobTitle) {<!-- -->
        super(name, age);
        this.jobTitle = jobTitle;
    }

    introduce() {<!-- -->
        console.log(`Hello, my name is ${<!-- -->this.name}, I am ${<!-- -->this.age} years old and I work as a ${<!-- -->this.jobTitle}.`);
    }
}

const jane = new Employee('Jane', 28, 'Software Developer');
jane.introduce(); // 输出: Hello, my name is Jane, I am 28 years old and I work as a Software Developer.

```

### 3. 静态方法

使用 `static` 关键字，你可以在类上定义静态方法，而不是它的实例：

```
class Utility {<!-- -->
    static addNumbers(a, b) {<!-- -->
        return a + b;
    }
}

console.log(Utility.addNumbers(2, 3)); // 输出: 5

```

### 4. getter 和 setter

你可以使用 `get` 和 `set` 关键字为类定义访问器和设置器：

```
class Circle {<!-- -->
    constructor(radius) {<!-- -->
        this._radius = radius;
    }

    // getter
    get diameter() {<!-- -->
        return this._radius * 2;
    }

    // setter
    set diameter(value) {<!-- -->
        this._radius = value / 2;
    }
}

const circle = new Circle(5);
console.log(circle.diameter); // 输出: 10
circle.diameter = 14;
console.log(circle._radius); // 输出: 7

```

>  
 <h2> 
  <center>
    本期好书推荐《JavaScript从入门到精通（第5版）》 
  </center></h2> 
 <hr> 
 <h2>【书籍介绍】</h2> 
 JavaScript入门经典，42万Web前端程序员的入行选择。配备Web前端开发资源库，在线答疑，学习1小时，训练10小时，从入门到项目上线，打造全新学习生态。 
 <hr> 
 <h2>【购买链接】</h2> 
 京东： 当当： 


## 【书籍介绍】

<img src="https://img-blog.csdnimg.cn/e9b4e97011f34df795a4dfa0a93393a7.jpeg" alt="请添加图片描述">
