
--- 
title:  JavaScript编程基础 – 闭包（Closure) 
tags: []
categories: [] 

---
## JavaScript编程基础 – 闭包

### JavaScript Programming Essentials - Closure

By Jackson@ML

>  
 闭包和JavaScript的作用域有关。 


我们需要先理解闭包的概念。

本文简要介绍闭包函数以及环境状态，并用实例说明闭包的创建及其基本用法。希望对学习及开发有所帮助。

#### 1. 闭包的概念

**闭包 (closure)** **是一个函数，以及它捆绑的周边环境状态**（即**词法环境，Lexical Environment**）的引用的组合。 简言之，闭包的开发者可以从内部函数访问外部函数的作用域。

#### 2. 词法环境

##### 1) 变量和嵌套函数

我们先分析下面这段代码：

```
// a lexical environment sample
function initialize() {<!-- -->
    // create a local variable
    var name = "Jackson";
    // displayName() is an internal so-called 'closure'
    function displayName() {<!-- -->      
      // using a variable declared by its parent function
      console.log("Hello! Welcome Mr.", name);      
    }
    displayName();
}
initialize();

```

函数initialize( ) 创建了局部变量name, 和displayName() 函数，所以，在initialize()函数体形成了嵌套函数。创建初期，displayName()函数在initialize()函数内部定义，且仅在该函数体内可用。

显然，displayName()函数没有声明自己的局部变量。然而，它可以访问到外部函数的变量，因此，displayName()可以使用父函数initialize()中声明的变量name。

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/d7f84a9143174db38f6ea43fa178fe58.png" alt="在这里插入图片描述"> 运行成功！ 通过运行该代码，我们发现在displayName()函数内的console.log()函数输出了变量name的值，而这个值是在其父函数中声明和初始化的。

##### 2) 词法及词法作用域

**词法(lexical)** 一词指的是，**词法作用域根据源代码中声明变量的位置确定该变量在何处可用**。

这个词法作用域的例子简要描述了分析器如何在函数嵌套的情况下解析变量名。嵌套函数可访问声明于它们外部作用域的变量。

#### 3. 闭包

##### 1) 返回函数

接下来，继续一个例子，代码如下：

```
function createFunction() {<!-- -->
    var name = "Jackson";
    function displayName() {<!-- -->
      console.log("Hello! Welcome, Mr.",name);
    }
    return displayName;
  }  
  var myFun = createFunction();
  myFun();

```

createFunction()函数同样内嵌了一个displayName()函数，与前一个示例类似。唯一不同的是，在于内部函数displayName()在执行之前，以return语句从外部函数返回。

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/7cf801a9aec94c5d9baf0972a3505fdd.png" alt="在这里插入图片描述"> 咋一看上述代码，可能觉得不确定能否直接运行成功。

>  
 在其它某些编程语言中，局部变量一旦在函数体内部声明，生命周期仅在于该函数的执行期间。 


例如，createFunction()函数执行完毕后，大家可能认为变量name不再能够被访问。但事实上，代码仍按照预期执行完毕。

这就是JavaScript的特定情况。原因在于JavaScript函数形成了闭包。

##### 2) 什么是闭包？

**闭包**是由函数以及声明该函数的词法环境组合而成的。**该词法环境包含了这个闭包创建时作用域内的任何局部变量**。

本例中，myFun()函数执行createFunction()函数创建的displayName()函数实例的引用。

在这里，displayName（）实例维持了对它的词法环境（也就是变量name存在于其中的环境）的引用。因此，当myFun被调用时，变量name仍然可用，它的值Jackson被传递给console.log()函数并输出到屏幕。

#### 4. 更多的闭包示例

下面我们再看一个更加有趣的函数multiply(x),代码如下：

```
function multiply(x) {<!-- -->
    return function(y) {<!-- -->
        return x * y;
    };
}
var mt10 = multiply(10);
var mt20 = multiply(20);
console.log(mt10(2));
console.log(mt20(3));

```

在这个示例中，定义了multiply(x)函数，用来实现变量的乘积；它接受一个参数x，并返回一个新的函数；返回的函数接受一个参数y，并返回x * y的乘积的值。

从本质上看，multiply是一个函数工厂，它可以创建将指定的值和它的参数相乘求积的函数。上面的例子使用函数工厂创建了两个新的函数：一个将其参数乘以10，另一个将其参数乘以20求积。

mt10和mt20都是闭包。它们共享相同的函数定义，但是保存了各自不同的词法环境。例如，在mt10中，x为10；而在mt20中，x则为20。

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/01efe50a18ad4ce8a5f3e65985ef2770.png" alt="在这里插入图片描述">

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😊

#### 5. 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 