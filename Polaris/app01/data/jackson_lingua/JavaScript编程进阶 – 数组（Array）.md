
--- 
title:  JavaScript编程进阶 – 数组（Array） 
tags: []
categories: [] 

---
## JavaScript编程进阶 – 数组（Array）

### JavaScript Programming Advanced – Array

By Jackson@ML

>  
 在JavaScript编程语言中，数组（Array）用于遍历。同时，数组可用来存储、操作和查找数据，以及转换数据格式。 


本文简要介绍如何使用数组操作处理数据以及存储数据等。

#### 1. 数组对象

Array（数组）作为对象，在Javascript语言中不是基本类型，而是具备特定属性的Array对象。它有以下主要特征：

**1）** 数组可以调整大小，并且可以包含不同数据类型。当不需要该特征时，可以按需使用类型化数组； **2）** 数组不是关联数组。这样一来，不能用任意字符串作为索引值访问数组元素，但必须使用非负整数作为索引值访问； **3）** 数组的索引从零开始。索引值由0，1，2这样逐渐递增。最后一个索引值时数组的length属性减去1的值； **4）** 数组复制操作创建浅拷贝。

#### 2. 数组下标

每个数组看上去都像是个特殊的变量，它有不止一个元素。以如下代码为例： <img src="https://img-blog.csdnimg.cn/direct/d8e64415317a4e33a3aac0aa635aed43.png" alt="在这里插入图片描述"> 如果数组元素众多，也可以在不同行显示元素。以如下代码为例： <img src="https://img-blog.csdnimg.cn/direct/3674c62096f84301ae05ec575c5b9e27.png" alt="在这里插入图片描述"> 获取每个数组元素，则需要按照数组下标来获取，索引值从零开始。如下代码： <img src="https://img-blog.csdnimg.cn/direct/cfc7fbcd560049f39e4fbc8ce7ca8f61.png" alt="在这里插入图片描述"> 添加新的数组元素，也按照数组下标来添加，如下代码： <img src="https://img-blog.csdnimg.cn/direct/d66028075b354993890ba4bd68ca9c81.png" alt="在这里插入图片描述"> 当我们添加了下标（即索引值）为5的元素后，该数组stars出现了六个元素。

#### 3. Push()方法

我们创建一个新的数组fruits, 添加几个元素，代码如下： <img src="https://img-blog.csdnimg.cn/direct/c7938a6d53bf42dfbca51632f882e538.png" alt="在这里插入图片描述"> 添加了四个元素的fruits数组对象，现在有了9个成员。

#### 4. 数组遍历

如果要求遍历一个数组，那么，需要用数组下标来标识每个元素，然后用循环语句遍历。判断数组长度需要使用数组的length属性。代码如下所示：

<img src="https://img-blog.csdnimg.cn/direct/aa01fae12a7143f48ffa6b3d004a8808.png" alt="在这里插入图片描述">

#### 5. 转换到字符串

Javascript方法 toString() 可以将一个数组转换为数组值的字符串。示例代码如下：

```
&gt; const ide = [“PyCharm”, “WebStorm”, “Visual Studio Code”, “IntelliJ IDEA”, “Eclipse”];
&gt; document.getElementById(“demo”).innerHTML = ide.toString();

```

执行结果如下：

```
&gt; PyCharm, WebStorm, Visual Studio Code, IntelliJ IDEA, Eclipse

```

#### 6. 数组是对象

数组是一种特殊类型的对象。JavaScript 中的 typeof 运算符为数组返回“object”。但是，最好将 JavaScript 数组描述为数组。

数组使用数字来访问其“元素”。在此示例中，person[0] 返回 John：

```
const person = [“John”, “Doe”, 28];

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/5b4d76a9c17d402e90b4ad823380f2f5.png" alt="在这里插入图片描述"> 对象使用名称来访问其成员。在以下实例中，engineer.firstname将返回值John。

<img src="https://img-blog.csdnimg.cn/direct/fd6459a5b63a4354aa21cb8d3a2cbdac.png" alt="在这里插入图片描述">

#### 7. 数组元素可以是对象

JavaScript 变量可以是对象。数组是特殊类型的对象。因此，您可以在同一个 Array 中拥有不同类型的变量。

您可以在 Array 中拥有对象。您可以在 Array 中拥有函数。您可以在 Array 中包含数组。

例如：声明一个数组arr, 分别将日期数值、函数赋给数组元素。示例代码如下： <img src="https://img-blog.csdnimg.cn/direct/af554e1569a84f5da5ee893d7dcfc57b.png" alt="在这里插入图片描述"> 将该数组以for循环遍历，执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/9fc5a3fb32404c4e9e05e76e49b891d2.png" alt="在这里插入图片描述"> 分别输出日期对象，以及两个匿名函数对象。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！ 您的认可，我的动力。😊
