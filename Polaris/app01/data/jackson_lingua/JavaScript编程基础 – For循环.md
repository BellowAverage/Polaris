
--- 
title:  JavaScript编程基础 – For循环 
tags: []
categories: [] 

---
## JavaScript编程基础 – For循环

### JavaScript Programming Essentials – For Loop

By Jackson@ML

循环可以多次执行代码块，而不用反复重写相同的语句。这无疑对提升代码质量、减少错误大有脾益。本文将简要介绍for循环的几种案例，希望对读者有所帮助。

#### 1. 顺序遍历

按照一定顺序遍历数值，如果需要输出一下代码结果：

```
Number 1 
Number 2
Number 3 
Number 4 
Number 5 

```

那么，可能需要重复5次使用console.log()函数。

```
console.log(“Number 1”);
console.log(“Number 2”);
console.log(“Number 3”);
console.log(“Number 4”);
console.log(“Number 5”);

```

现在，我们使用for循环，仅仅三行代码，以简化该程序：

```
for (let i = 1; i &lt;= 5; i++) {<!-- -->
    console.log("Number " + i );
}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/b21fdf1f549040bba6eeb60d890d63d1.png" alt="在这里插入图片描述"> 换个例子，以序数词数组丰富一下输出，看以下代码：

```
arr1 = ['first','second','third','fourth','fifth'];

for (let i = 1; i &lt;= arr1.length; i++){<!-- -->
    console.log("The " + arr1[i-1] + " number is " + i);
}

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/09303cd1c7544b8dad654cc16e85a7bb.png" alt="在这里插入图片描述">

#### 2. 嵌套循环

当采用内外循环时，可能涉及到两个或多个变量变化带来的遍历，例如乘法表。

被乘数和乘数分别以变量i和变量j来标注，依次变化形成乘法表等式。代码如下：

```
for (let i = 1; i &lt;= 5; i++) {<!-- -->
    for (let j = 1; j &lt;= i; j++){<!-- -->
        console.log(i + "*" + j + "=" + i * j);
    }    
}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/0468f6f817a344ecb1c456fd8eb160fb.png" alt="在这里插入图片描述">

#### 3. 添加条件的循环

如果想从普通的整数序列过滤出符合条件的数，例如遍历偶数，如下面代码：

```
for (i = 0; i &lt;= 6; i++){<!-- -->
    if (i % 2 == 0) {<!-- -->
        console.log("The even number:", i);
    }
}

```

执行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/direct/a626f7c99013440c886846eaf2fa4cd2.png" alt="在这里插入图片描述"> 同样，如果需要遍历能被7整除的数，可以写代码如下：

```
for (i = 1; i &lt;= 30; i++) {<!-- -->
    if (i % 7 == 0) {<!-- -->
        console.log(i);
    }    
}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/46241f7262694cfdb202dff2a352d146.png" alt="在这里插入图片描述">

#### 4. 变量作用域

用来遍历数据的变量，如果在循环体声明，则服务于循环体，如果不是，则可能服务于更广的范围。假如需要遍历1至10的奇数，如下所示：

```
var i = 5;
for (var i = 0; i &lt; 10; i++){<!-- -->
    if (i % 2 != 0) {<!-- -->
        console.log("The odd number is:", i)
    }
}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/ce1f7f8841ef40a9a9308e0975e66122.png" alt="在这里插入图片描述"> 我们看到，尽管i变量被声明且初始化为5，但是循环体内声明的i不受任何影响，仍然按照它自己的状态进行声明和初始化，输出结果也基于这个局部变量i。

但是，如果在循环体内部不再声明和初始化，而是利用全局变量i，又有什么变化呢？看以下代码：

```
var i = 5;
for (; i &lt; 10; i++){<!-- -->
    if (i % 2 != 0) {<!-- -->
        console.log("The odd number is:", i)
    }
}

```

执行结果如下图所示： <img src="https://img-blog.csdnimg.cn/direct/4618c623058845c0ad840e48b022aae5.png" alt="在这里插入图片描述"> 本文简要介绍了for循环遍历数值的几种情况。

工作中，如果需要重复输出类似的结果，for循环将帮助您事半功倍。

技术好文陆续推出，敬请关注。

喜欢就点赞哈！您的认可，我的动力。😊

#### 相关阅读：
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 