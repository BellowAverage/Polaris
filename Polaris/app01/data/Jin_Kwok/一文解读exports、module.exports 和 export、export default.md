
--- 
title:  一文解读exports、module.exports 和 export、export default 
tags: []
categories: [] 

---
>  
 对于前端初学者来说，exports、module.exports 和 export、export default 容易让人产生误解，笔者顺便写篇文章解读一下。 


## 第一部分：exports 和 module.exports

为了让Node.js的文件可以相互调用，Node.js提供了一个简单的模块系统。模块是Node.js 应用程序的基本组成部分，文件和模块是一一对应的。换言之，一个 Node.js 文件就是一个模块，这个文件可能是JavaScript 代码、JSON 或者编译过的C/C++ 扩展。

### 1. exports

#### 1.1 导出模块

exports 对象是由模块系统创建的。在我们自己写模块的时候，需要在模块最后写好模块接口，声明这个模块对外暴露什么内容，exports 提供了暴露接口的方法。如下代码示例：

```
//hello.js
var sayHello = function () {<!-- -->
    console.log('hello')
}
var sos = 110;
var app = {<!-- -->
    name: 'testApp',
    version: '1.0.0',
    help: function () {<!-- -->
        console.log('what can i do for you?')
    }
}
//导出一个方法
exports.sayHello = sayHello;
//导出一个变量
exports.sos = sos;
//导出一个JSON对象
exports.app = app;

```

或者写成下面的形式：

```
//hello.js
exports.sayHello = function () {<!-- -->
    console.log('hello')
}
exports.sos = 110;
exports.app = {<!-- -->
    name: 'testApp',
    version: '1.0.0',
    help: function () {<!-- -->
        console.log('what can i do for you?')
    }
}

```

在以上示例中，hello.js 通过 exports 对象把 sayHello 作为模块的访问接口，在其他模块（或js文件）中通过 require(’./hello’) 加载这个模块，然后就可以直接访 问 hello.js 中 exports 对象的成员函数了。

#### 1.2 引入模块

在 Node.js 中，引入一个模块非常简单，如下我们创建一个 main.js 文件并引入 hello 模块，代码如下:

```
//main.js
var hello = require('./hello');
//调用模块hello中的方法
hello.sayHello();
//调用模块hello中的变量
console.log(hello.sos)
console.log(hello.app.version)
//调用模块hello中的JSON对象属性
hello.app.help()

```

执行命令（node main.js）运行main.js，结果如下：

```
hello
110
1.0.0
what can i do for you?

```

以上实例中，代码 require(’./hello’) 引入了当前目录下的 hello.js 文件（./ 为当前目录，node.js 默认后缀为 js）。

Node.js 提供了 exports 和 require 两个对象，其中 exports 是模块公开的接口，require 用于从外部获取一个模块的接口，即所获取模块的 exports 对象。

### 2. module.exports

#### 2.1 导出模块

有时候我们希望把一个对象封装到模块中，格式如下：

```
//hello.js 
function Hello() {<!-- -->
    var name;
    var sos = '110';
    this.setName = function (thyName) {<!-- -->
        name = thyName;
    };
    this.sayHello = function () {<!-- -->
        console.log('Hello ' + name);
    };
    this.app = {<!-- -->
        name: 'testApp',
        version: '1.0.0',
        help: function () {<!-- -->
            console.log('what can i do for you?')
        }
    };
};
// 把变量、方法、JSON对象等封装在一起，一并导出
module.exports = Hello;

```

#### 2.2 引入模块

```
//main.js
var Hello = require('./hello')
//通过new关键字，实例化一个hello模块的对象，通过这个对象才能调用hello模块相关的方法。
hello = new Hello();

hello.setName("zhangSan")
hello.sayHello()

console.log(hello.app.version)
hello.app.help()

```

执行命令，运行main.js，结果如下：

```
Hello zhangSan
1.0.0
what can i do for you?

```

### 3. exports 和 module.exports 的区别是什么？

上面两节的内容可以知道：相较于 exports，模块接口的唯一变化是使用 module.exports = Hello 代替了exports.sayHello = function(){}，exports.sos，exports.app。 在外部引用该模块时，其接口对象就是要输出的 Hello 对象本身，而不是原先的 exports。

为了直观地展现两者的异同点，我们先来看两个实例：

#### 3.1 exports 模式下两者的异同

```
//hello.js
var sayHello = function () {<!-- -->
    console.log('hello')
}
var sos = 110;
var app = {<!-- -->
    name: 'testApp',
    version: '1.0.0',
    help: function () {<!-- -->
        console.log('what can i do for you?')
    }
}
exports.sayHello = sayHello;
exports.sos = sos;
exports.app = app;
//打印exports和module.exports的内容
console.log(exports);
console.log(module.exports);
console.log(exports === module.exports);

```

运行如下 main.js 代码：

```
//main.js
var Hello = require('./exports_mode')

Hello.sayHello()

```

运行结果如下：

```
{<!-- -->
  sayHello: [Function: sayHello],
  sos: 110,
  app: {<!-- --> name: 'testApp', version: '1.0.0', help: [Function: help] }
}
{<!-- -->
  sayHello: [Function: sayHello],
  sos: 110,
  app: {<!-- --> name: 'testApp', version: '1.0.0', help: [Function: help] }
}
true

```

>  
 很明显！！！ exports 和 module.exports 的内容是完全一样的，换言之：exports 指向的是 module.exports。 


#### 3.2 module.exports 模式下两者的异同

```
//hello.js
function Hello() {<!-- -->
    var name;
    this.setName = function (thyName) {<!-- -->
        name = thyName;
    };
    this.sayHello = function () {<!-- -->
        console.log('Hello ' + name);
    };
    this.app = {<!-- -->
        name: 'testApp',
        version: '1.0.0',
        help: function () {<!-- -->
            console.log('what can i do for you?')
        }
    };
};

// 把变量、方法、JSON对象等封装在一起，一并导出
module.exports = Hello;
//打印exports和module.exports的内容
console.log(exports);
console.log(module.exports);
console.log(exports === module.exports);

```

运行main.js如下：

```
var Hello = require('./exports_mode')
hello = new Hello();

hello.setName("zhangSan")
hello.sayHello()

```

运行结果如下：

```
{<!-- -->}
[Function: Hello]
false
Hello zhangSan

```

>  
 很明显！！！module.exports 模式下，module.exports 和 exports 的内容是完全不同的，module.exports 导出的是模块（hello.js）对象本身（类别Java，可以理解为导出的是一个类，而不是实例化的对象），在此场景下 exports 是空的（类比Java，理解为一个空对象，没有实例化就是null）。 


#### 3.3 小结

基于上面的实例，我们可以看到，输出的 module.exports 对象内容就是一个[Function]，在 javascript 里面是一个类。使用这种方式的好处是： exports 只能对外暴露单个函数，但是 module.exports 却能暴露一个类。

## 第二部分：export 和 export default

exports 和 module.exports 是Node.js的模块系统关键字，而 export 和 export default 则是 ES6模块系统的关键字。很明显，两者属于两个体系：

>  
 require: node 和 es6 都支持的引入 export / import : 只有es6 支持的导出引入 module.exports / exports: 只有 node 支持的导出 


### 1.export

export 用于对外输出本模块（一个文件可以理解为一个模块）变量的接口，import 用于在一个模块中加载另一个含有export接口的模块。也就是说使用export命令定义了模块的对外接口以后，其他JS文件就可以通过import命令加载这个模块（文件）。这几个都是ES6的语法。

示例1：

```
//app.js
export var name="ZhangSan";

```

示例2:

```
//app.js
var name1="ZhangSan";
var name2="LiSi";
export {<!-- --> name1 ,name2 }

```

### 2.import

import 用于在一个模块中加载另一个含有export接口的模块。具体见下面的示例。

对于上面的 示例1，引入方式为：

```
//main.js
import {<!-- --> name } from "./app.js" //路径根据实际情况填写

```

对于上面的 示例2，引入方式为：

```
//main.js
import {<!-- --> name1 , name2 } from "./app.js" //路径根据实际情况填写

```

### 3.export 和 export default

通过上面这几个例子，读者一定了解了如何使用export，import，如果还是不懂可以自己动手试一试。上面讲的是export和import，但是export跟export default 有什么区别呢？如下：
1. export与export default均可用于导出常量、函数、文件、模块等；1. 你可以在其它文件或模块中通过import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用；1. 在一个文件或模块中，export、import可以有多个，**export default仅有一个**；1. 通过export方式导出，在导入时要加{ }，export default则不需要
实际上，很多时候export与export default可以实现同样的目的，只是用法有些区别。注意第4条，通过export方式导出，在导入时要加{ }，export default则不需要。使用export default命令，为模块指定默认输出，这样就不需要知道所要加载模块的变量名。

## 第三部分：CommonJS 和 ES6

### 1. CommonJS

Node里面的模块系统遵循的是CommonJS规范。那问题又来了，什么是CommonJS规范呢？由于js以前比较混乱，各写各的代码，没有一个模块的概念，而这个规范出来其实就是对模块的一个定义。

CommonJS定义的模块分为:

>  
 模块标识(module)、模块定义(exports) 、模块引用(require) 


#### 1.1 exports 和 module.exports

在一个node执行一个文件时，会给这个文件内生成一个 exports和module对象，而module又有一个exports属性。他们之间的关系如下图，都指向一块{}内存区域。

```
exports = module.exports = {<!-- -->};

```

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly91c2VyLWdvbGQtY2RuLnhpdHUuaW8vMjAxNy83LzMxLzYyMjdkNGUwOTE3ZjRhZjY0OWQ5ZjllNzUwZWRkYjA5?x-oss-process=image/format,png#pic_center" alt="在这里插入图片描述">

实际上，require导出的内容是module.exports的指向的内存块内容，并不是exports的。简而言之，区分他们之间的区别就是 exports 只是 module.exports的引用，辅助后者添加内容用的。

#### 1.2 注意事项

在实际应用中，为了避免糊涂，尽量都用 module.exports 导出，然后用require导入。

### 2. ES6

ES6， 全称 ECMAScript 6.0 ，是 JavaScript 的下一个版本标准，2015.06 发版。ES6 主要是为了解决 ES5 的先天不足，比如 JavaScript 里并没有类的概念，但是目前浏览器的 JavaScript 是 ES5 版本，大多数高版本的浏览器也支持 ES6，不过只实现了 ES6 的部分特性和功能。

在 ES6 前， 实现模块化使用的是 RequireJS 或者 seaJS（分别是基于 AMD 规范的模块化库， 和基于 CMD 规范的模块化库）。ES6 引入了模块化，其设计思想是在编译时就能确定模块的依赖关系，以及输入和输出的变量。

>  
 ES6 的模块化分为导出（export） 与导入（import）两个模块。 


#### 2.1 ES6 的特点
- ES6 的模块自动开启严格模式，不管你有没有在模块头部加上 use strict;- 模块中可以导入和导出各种类型的变量，如函数，对象，字符串，数字，布尔值，类等。- 每个模块都有自己的上下文，每一个模块内声明的变量都是局部变量，不会污染全局作用域。- 每一个模块只加载一次（是单例的）， 若再去加载同目录下同文件，直接从内存中读取。
#### 2.2 基本用法
- 模块导入导出各种类型的变量，如字符串，数值，函数，类。- 导出的函数声明与类声明必须要有名称（export default 命令另外考虑）。- 不仅能导出声明还能导出引用（例如函数）。- export 命令可以出现在模块的任何位置，但必需处于模块顶层。- import 命令会提升到整个模块的头部，首先执行。
#### 参考文献
1. https://segmentfault.com/a/1190000010426778；1. https://www.runoob.com/nodejs/nodejs-module-system.html；1. https://www.runoob.com/w3cnote/es6-module.html