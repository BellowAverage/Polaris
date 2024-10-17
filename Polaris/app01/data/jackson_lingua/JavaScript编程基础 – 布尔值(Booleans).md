
--- 
title:  JavaScript编程基础 – 布尔值(Booleans) 
tags: []
categories: [] 

---
## JavaScript编程基础 – 布尔值(Booleans)

### Javascript Programming Essentials – Booleans

>  
 一个JavaScript布尔值包含两个值中的一个，即 true 或者 false。 


本文简要介绍JavaScript布尔值的具体应用，以及可能作为对象的布尔值等。

#### 1. 布尔值(Booleans)

布尔值在通用编程语言中，就如同判断两种可能性的数据类型，例如：
- Yes / No- On / Off- True / False
##### 1) Boolean数据类型

JavaScript有一个Boolean的数据类型，那么，很显然，它仅能使用两个值：true 或者 false.

例如，用变量isTimeToEat判断到吃饭时间了，如果确定**是**，那么赋值**true**给它：

```
isTimeToEat = true;

```

true 和 false 都是关键字，内置在JavaScript中。因此，当JavaScript看到关键字true, false时，就会视为布尔值来处理。

##### 2) 输出布尔值

要显示一个布尔值的内容，可以用console.log()函数

```
console.log(isTimeToEat);

```

也可以弹出消息框，用alert()函数：

```
Alert(isTimeToEat);

```

#### 2. Boolean()函数

我们使用条件表达式判断是否为“真”时，可以用Boolean(0函数。

以下示例代码，用来判断比较大小的结果，结果是真，就返回true; 反之，就返回false.

```
Boolean(10 &gt; 9);
Boolean(2 &gt; (8 / 3));

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/e75f52ec858d49f7b0a0831ae43209db.png" alt="在这里插入图片描述"> 无穷大的值，会被视为true, 例如：

```
var b3 = Boolean(1 / 0);
console.log(b3);

```

结果：true

#### 3. 比较和条件

以比较运算符来比较数值的大小，有几种运算符如下表（具体以实际例子为准）：

<img src="https://img-blog.csdnimg.cn/1180dcaffb2b46f2a91e0fde08c22662.png" alt="在这里插入图片描述"> 表达式的布尔值结果，是JavaScript比较和条件的基础。

##### 1） 示例一：比较两个表达式的值。

得出结果为true/false, 看一下代码： <img src="https://img-blog.csdnimg.cn/4d4748170b114c6ab86602cc706dd65a.png" alt="在这里插入图片描述">

##### 2） 零与负零的布尔值

**零的布尔值都是false**. 看以下例子：

```
let x = 0;
console.log(Boolean(x));

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/2accc4cc327e4ee18bb16ca1a2dbf5e5.png" alt="在这里插入图片描述">

同样，-0也是如此。

##### 3） 空字符串的布尔值

```
let x = “”;
Boolean(x);

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/daa8dfdefc8b42dcb2ac0d2c5743753f.png" alt="在这里插入图片描述">

##### 4） 未定义变量(undefined)的布尔值

```
let x;
console.log(Boolean(x));

```

可以看到，执行结果是：false. <img src="https://img-blog.csdnimg.cn/238d52e5780a479fbe4a97ecbb27e5bc.png" alt="在这里插入图片描述">

同样，false的布尔值，也是false.

##### 5） NaN的布尔值

以下示例说明NaN的布尔值：

```
let x = 10 / “Hello”;
console.log(Boolean(x));

```

执行结果是：false, 如下图所示： <img src="https://img-blog.csdnimg.cn/6d5826466c584295a9bdac1e6958b358.png" alt="在这里插入图片描述">

##### 6） JavaScript布尔值对象

通常，JavaScript布尔值是从字面量创建的原始值。例如：

```
let x = false;

```

但同时，布尔值也能用new关键字定义为对象。例如：

```
let y = new Boolean(false);
console.log(typeof(x));
console.log(typeof(y));

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/ba0e1a6acbba43d89bc62ed5dae4bab4.png" alt="在这里插入图片描述">

##### 7） 是否全等于？

前面列出了诸如==(等于) 和===（全等于）等的逻辑运算符。要比较两个布尔值是否相等或全等，有以下示例：

```
let x = new Boolean(false);
let y = new Boolean(false);
console.log(x == y);
console.log(x === y);
console.log(x != y);
console.log(x !== y);

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/a1e86bd924704b6380cf11f0d7855755.png" alt="在这里插入图片描述"> 这就说明一点，比较两个JavaScript对象，会返回false.

对这些例子感兴趣吗？是不是还想跟我继续了解JavaScript编程呢？ 技术好文陆续推出，欢迎关注。

喜欢就点赞哈，您的认可，我的动力。😊

## 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1.  10.