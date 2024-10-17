
--- 
title:  【科普文】JavaScript前世今生 and 安全隐患 
tags: []
categories: [] 

---
**目录**



javascript前世今生



























## ECMAScript

###  JavaScript的前世今生

ECMAScript是一种由ECMA国际通过ECMA-262标准化的脚本程序设计语言，它往往被称为JavaScript或JScript。简单的，可以认为ECMAScript是JavaScript的一个标准，但实际上后两者是ECMA-262标准的实现和扩展。

###  版本

1997年6月，首版发布。1998年6月，进行了格式修正，以使得其形式与ISO/IEC16262国际标准一致。1999年12月，引入强大的正则表达式，更好的词法作用域链处理，新的控制指令，异常处理，错误定义更加明确，数据输出的格式化及其它改变。而后由于关于语言的复杂性出现分歧，第4版本被放弃，其中的部分成为了第5版本及Harmony的基础。

2009年12月，第五版发布，新增“严格模式（strict mode）”，澄清了许多第3版本的模糊规范，并适应了与规范不一致的真实世界实现的行为。增加了部分新功能，如getters及setters，支持JSON以及在对象属性上更完整的反射。

2015年6月，第6版发布，最早被称作是 ECMAScript 6（ES6），添加了类和模块的语法，迭代器，Python风格的生成器和生成器表达式，箭头函数，二进制数据，静态类型数组，集合（maps，sets 和 weak maps），promise，reflection 和 proxies。

2016年6月，ECMAScript 2016（ES2016）发布，引入 `Array.prototype.includes` 、指数运算符、SIMD等新特性。

2017年6月，ECMAScript 2017（ES2017）发布，多个新的概念和语言特性。

2018年6月，ECMAScript 2018 （ES2018）发布包含了异步循环，生成器，新的正则表达式特性和 rest/spread 语法。

###  ES6 特性

>  
 <ul>- `const` / `let`- 模板字面量<li> 解构 
   - `[a, b] = [10, 20]`</li>- 对象字面量简写法- `for...of` 循环- `...xxx` 展开运算符- 可变参数- 箭头函数- 默认参数函数- 默认值与解构- 类</ul> 


##  引擎

###  V8

>  
 V8是Chrome的JavaScript语言处理程序（VM）。其引擎由TurboFan、Ignition和Liftoff组成。其中Turbofan是其优化编译器，Ignition则是其解释器，Liftoff是WebAssembly的代码生成器。 


###  SpiderMonkey

SpiderMonkey是Mozilla项目的一部分，是一个用 C/C++ 实现的JavaScript脚本引擎。

###  JavaScriptCore

JavaScriptCore的优化执行分为四个部分，LLInt、Baseline、DFG、FTL。LLInt是最开始的解释执行部分，Baseline是暂时的JIT，DFG阶段开始做一定的优化，FTL阶段做了充分的优化。

###  ChakraCore

ChakraCore是一个完整的JavaScript虚拟机，由微软实现，用于Edge浏览器以及IE的后期版本中。

###  JScript

JScript是由微软开发的脚本语言，是微软对ECMAScript规范的实现，用于IE的早期版本中。

###  JerryScript

JerryScript是一个适用于嵌入式设备的小型JavaScript引擎，由三星开发并维护。

 

##  WebAssembly

###  简介

>  
 简而言之，WASM是一种分发要在浏览器中执行的代码的新方法。它是一种二进制语言，但是无法直接在处理器上运行。在运行时，代码被编译为中间字节代码，可以在浏览器内快速转换为机器代码，然后比传统JavaScript更有效地执行。 


###  执行

>  
 虽然浏览器可能以不同的方式来实现Wasm支持，但是使用的沙盒环境通常是JavaScript沙箱。 
 在浏览器中运行时，Wasm应用程序需要将其代码定义为单独的文件或JavaScript块内的字节数组。 然后使用JavaScript实例化文件或代码块，目前不能在没有JavaScript包装器的情况下直接在页面中调用Wasm。 
 虽然Wasm可以用C / C++等语言编写，但它本身不能与沙箱之外的环境进行交互。这意味着当Wasm应用程序想要进行输出文本等操作时，它需要调用浏览器提供的功能，然后使用浏览器在某处输出文本。 
 Wasm中的内存是线性的，它在Wasm应用程序和JavaScript之间共享。 当Wasm函数将字符串返回给JavaScript时，它实际上返回一个指向Wasm应用程序内存空间内位置的指针。 Wasm应用程序本身只能访问分配给它的JavaScript内存部分，而不是整个内存空间。 


###  安全

Wasm的设计从如下几个方面考虑来保证Wasm的安全性

>  
 - 保护用户免受由于无意的错误而导致漏洞的应用程序的侵害- 保护用户免受故意编写为恶意的应用程序的侵害- 为开发人员提供良好的缓解措施 


具体的安全措施有
- Wasm应用程序在沙箱内运行- Wasm无法对任意地址进行函数调用。Wasm采用对函数进行编号的方式，编号存储在函数表中- 间接函数调用受类型签名检查的约束- 调用堆栈受到保护，这意味着无法覆盖返回指针- 实现了控制流完整性，这意味着调用意外的函数将失败
###  

###  推荐阅读

**<strong>**</strong>

**优质资源**
1. ** Java实现照片GPS定位【完整脚本】**1. 1. **Python实现照片GPS定位【完整脚本】**1. 1. **女神忘记相册密码 python20行代码打开【完整脚本】**1. 1. **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>1. 
<img src="https://img-blog.csdnimg.cn/4c540ef37f8f47f093ecded44e044c3b.png" alt="4c540ef37f8f47f093ecded44e044c3b.png">

 

**python实战**
- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>
####  【资源推荐】

#### **渗透测试专用系统**

kali-linux-e17-2019.1a-amd64.iso系统镜像



kali-linux-2018.4-amd64 操作系统



manjaro-xfce-17.1.7-stable-x86_64.iso系统镜像



WiFi专用渗透系统 nst-32-11992.x86_64.iso操作系统镜像



Parrot-security-4.1_amd64.iso 操作系统镜像



manjaro-xfce-17.1.7-stable-x86_64 操作系统



cyborg-hawk-linux-v-1.1 操作系统



<img src="https://img-blog.csdnimg.cn/d5574bcb9135412ca9ad247f467a7a73.png" alt="d5574bcb9135412ca9ad247f467a7a73.png"> 【kali常用工具】上网行为监控工具       

 



【kali常用工具】抓包工具Charles Windows64位 免费版



【kali常用工具】图印工具stamp.zip



 【kali常用工具】brutecrack工具[WIFIPR中文版]及wpa/wpa2字典



 

 
