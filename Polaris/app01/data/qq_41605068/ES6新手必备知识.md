
--- 
title:  ES6新手必备知识 
tags: []
categories: [] 

---
## 1. var、let和const
- var：ES5中用于声明变量的关键字，**存在各种问题**
```
 // 1.声明提升
 // 此处会正常打印，但这是错误的（属于先上车后买票了！）
 console.log(name); 
 var name = "大帅比";
 
 // 2. 变量覆盖
 var demo = "小明";
 var demo = "小红";
 // 此处会打印小红，这也是错误的（属于套牌车，违法的啊，兄弟）
 // 同一个项目中，发生变量覆盖可能会导致数据丢失以及各种不可预知的bug，原则上来说：变量不能重名
 console.log(demo)

// 3. 没有块级作用域
  function fn2(){
      for(var i = 0; i &lt; 5; i++){
          // do something
      }
      // 此处会正常打印出 i 的值，这是错误的
      // i是定义在循环体之内的，只能在循环体内打印，当前现象叫做红杏出墙！！！
      console.log(i);
  }
  fn2();

```
- let：ES6新增，用于声明变量，有**块级作用域**
```
 // 1. 不会存在声明提前
 // 此处会报错（这里必须报错，原则上来说不能先上车后买票）
 console.log(name); 
 let name = "大帅比";
 
 // 2. 不会有变量覆盖
 let demo = "小明";
 let demo = "小红";
 // 此处会报错（不能使用套牌车！）告诉你已经定义了此变量。避免了项目中存在变量覆盖的问题
 console.log(demo)

// 3. 有块级作用域
  function fn2(){
      for(let i = 0; i &lt; 5; i++){
          // do something
      }
      // 此处会报错，无法打印，防止红杏出墙！！！
      // i是定义在循环体之内的，循环体外当然无法打印 
      console.log(i);
  }
  fn2();

```
- const 声明一个只读的常量，一旦声明，常量的值就不能改变【用于全局变量】
```
const PI = "3.1415926";

```

## 2.结构赋值

针对数组或者对象进行模式匹配，然后对其中的变量进行赋值

### 2.1数组

```
let [a, b, c] = [1, 2, 3];
// a = 1，b = 2，c = 3 相当于重新定义了变量a,b,c，取值也更加方便

// , = 占位符
let arr = ["小明", "小花", "小鱼", "小猪"];
let [,,one] = arr; // 这里会取到小鱼

// 解析整个数组
let strArr = [...arr];
// 得到整个数组
console.log(strArr);

```

### 2.2对象

```
let obj = {
   className : "卡西诺",
   age: 18
}
let {className} = obj; // 得到卡西诺
let {age} = obj;	// 得到18

// 剩余运算符
let {a, b, ...demo} = {a: 1, b: 2, c: 3, d: 4};
// a = 1
// b = 2
// demo = {c: 3, d: 4}

```

## 3.模板字符串

模板字符串相当于**加强版的字符串**，用反引号 ``

### 3.1普通字符串

```
// 普通字符串
let string = "hello"+"小兄弟"; // hello小兄弟
// 如果想要换行
let string = "hello'\n'小兄弟"
// hello
// 小兄弟

```

### 3.2模板式字符串

```
let str1  = "穿堂而过的";
let str2 = "风";
// 模板字符串
let newStr = `我是${str1}${str2}`;
// 我是穿堂而过的风
console.log(newStr)

// 字符串中调用方法
function fn3(){
  return "帅的不行！";
}
let string2= `我真是${fn3 ()}`;
console.log(string2);  // 我真是帅的不行！

```

## 4.ES6函数

### 4.1箭头函数
- 基本语法：**参数 =&gt; 函数体**- **箭头函数本身没有作用域（无this）**
```
let fn2 = (num1,num2) =&gt; {
 let result = num1 + num2;
 return result;
}
fn2(3,2);  // 输出5

```

### 4.2函数参数

#### 1.默认参数

```
// num为默认参数，如果不传，则默认为10
// 需要注意的是：只有在未传递参数，或者参数为 undefined 时，才会使用默认参数，null 值被认为是有效的值传递
function fn(type, num=10){
 console.log(type, num);
}
fn(1);	// 打印 1，10
fn(1,2); // 打印 1，2 （此值会覆盖默认参数10）

```

#### 2.不定参数

```
// 此处的values是不定的，且无论你传多少个
function f(...values){
    console.log(values.length);
}
f(1,2);      // 2
f(1,2,3,4);  // 4

```

## 5.Class类
- class 的本质是 function，同样可以看成**一个块**- class (类)作为对象的模板被引入，可以通过 class 关键字定义类
### 5.1类定义

```
// 匿名类
let Demo = class {
    constructor(a) {
        this.a = a;
    }
}
// 命名类
let Demo = class Demo {
    constructor(a) {
        this.a = a;
    }
}

```

### 5.2类声明

```
// 请注意：
//    1.类不能重复声明
//    2.类定义不会被提升，必须在访问前对类进行定义，否则就会报错。
//    3.类中方法不需要 function 关键字。
//    4.方法间不能加分号
class Demo {
    constructor(a) {
        this.a = a;
    }
}

```

### 5.3类主体

```
class Demo {
    a = 2;
    //  如果不写constructor，也会默认添加
    constructor () {
        console.log(this.a);
        console.log("我是构造器");
    }
}

```

### 5.4实例化对象

```
class Demo {
    constructor(a, b) {
        this.a = a;
        this.b = b;
        console.log('Demo');
    }
    sum() {
        return this.a + this.b;
    }
}
let demo1 = new Demo(2, 1);
let demo2 = new Demo(3, 1);
// 两者原型链是相等的
console.log(demo1._proto_ == demo2._proto_); // true
 
demo1._proto_.sub = function() {
    return this.a - this.b;
}
console.log(demo1.sub()); // 1
console.log(demo2.sub()); // 2

```

## 6.Map

### 6.1** Maps 和 Objects 的区别**
- 一个 Object 的键只能是字符串或者 Symbols，但一个 Map 的键可以是任意值- Map 中的键值是有序的（FIFO 原则），而添加到对象中的键则不是- Map 的键值对个数可以从 size 属性获取，而 Object 的键值对个数只能手动计算
### 6.2Map中的key

```
// 1. key是字符串
let myMap = new Map();
let keyString = "string"; 
 
myMap.set(keyString, "和键'string'关联的值");

// keyString === 'string'
myMap.get(keyString);    // "和键'string'关联的值"
myMap.get("string");   // "和键'string'关联的值"

// 2.key是对象
let myMap = new Map();
let keyObj = {}, 
 
myMap.set(keyObj, "和键 keyObj 关联的值");
myMap.get(keyObj); // "和键 keyObj 关联的值"
myMap.get({}); // undefined, 因为 keyObj !== {}

// 3. key也可以是函数或者NaN                         

```

### 6.3**Map 的迭代**

```
// 1.使用 forEach
let myMap = new Map();
myMap.set(0, "zero");
myMap.set(1, "one");
 
// 0 = zero , 1 = one
myMap.forEach(function(value, key) {
  console.log(key + " = " + value);
}, myMap)

// 2. 也可以使用 for...of

```

### 6.4**Map 与 Array的转换**

```
letkvArray = [["key1", "value1"], ["key2", "value2"]];
 
// Map 构造函数可以将一个 二维 键值对数组转换成一个 Map 对象
let myMap = new Map(kvArray);
 
// 使用 Array.from 函数可以将一个 Map 对象转换成一个二维键值对数组
let outArray = Array.from(myMap);

```

### 6.5**关于map的重点面试题**

#### 1.请谈一下 Map()和ForEach() 的区别（问到map，必定问到此题）
- forEach()方法不会返回执行结果，而是undefined- map()方法会得到一个新的数组并返回- 同样的一组数组，map()的执行速度优于 forEach()（**map() 底层做了深度优化**）
因此，性质决定了用途：
- forEach() 适合于你并不打算改变数据的时候，而只是想用数据做一些事情
```
let arr = ['a', 'b', 'c', 'd'];
arr.forEach((val) =&gt; {
 console.log(val); // 依次打印出 a,b,c,d
});

```
- map() 适用于你要改变数据值的时候，它更快，而且返回一个新的数组
```
let arr = [1, 2, 3, 4, 5];
let arr2 = arr.map(num =&gt; num * 2).filter(num =&gt; num &gt; 5);
// arr2 = [6, 8, 10]

```


