
--- 
title:  C语言基础 – 循环 
tags: []
categories: [] 

---
## C语言基础 – 循环

### C Programming Essentials – Loops

C语言控制语句中，非常重要的当属循环。C的循环包括以下三张：for, while, do while。

>  
 大多数人都希望自己天资聪颖、颜值高、体格壮，尽管有时候事与愿违，但至少能写出美妙健壮的程序。 
 对于计算机科学而言，好的程序离不开良好的控制流，也就是有效控制程序的逻辑，以完成预定的任务。 有效的控制应该提供以下三种程序流： 1、 平顺执行语句序列； 2、 满足特定条件时，就重复执行语句序列（循环）； 3、 通过测试，选择执行哪一个语句序列（分支）。 


第一种为通用程序语句，必须满足；**第二种**是本文**重点**讲述的；而第三种为选择不同方案提供了可能，可以使程序更加“智能”，将在后续文章详述。

本文简要介绍如何通过不同循环，来遍历一个系列的数据，从而高效实现一些重复性工作，避免由此产生的程序错误。本次编程采用的开发工具是Visual Studio Code。 （关于如何安装配置Visual Studio Code以便开始C语言编程，参看文章： ）

#### 前言： 为什么使用循环？

现在，先提出这个简单的问题。

假如，需要用一个程序打印输出一些整数，例如：从1到5都需要打印出来，那么按照前述的平顺执行语句的话，需要写一下程序：

```
# include &lt;stdio.h&gt;
int main(void)
{<!-- -->
    int i = 1;
    printf("%d", i);
    i = i + 1;
    printf("%d", i);
    i = i + 1;
    printf("%d", i);
    i = i + 1;
    printf("%d", i);
    i = i + 1;
    printf("%d", i);
    return 0;
}

```

执行结果如下图所示。 <img src="https://img-blog.csdnimg.cn/b6f45a673ac24987a6e148087cce2324.png" alt="在这里插入图片描述"> 可以看出，共有15行代码，5次printf() 函数打印输出。而这仅仅是5个整数！

如果需要输出100个，或者更多呢? 无疑程序将执行多次代码，而且这个程序代码也会变得冗长。

还有，在代码输出的过程中，任何标点符号的错误，或者代码因缩进和其它问题带来的异常，都将使人苦不堪言。

既然需要**遍历所有有规律的整数**，也就是说，把所有整数都看一遍，那么，为何不采用循环呢？

## 1. While循环

While循环是所谓的**采用入口条件的有条件循环**。“有条件”指的是语句部分的执行取决于测试表达式描述的条件。

例如：index &lt; 5, 那么该表达式是一个入口条件，因为必须满足条件，才能进入循环体。看下面这段while循环相关的代码：

```
int index = 1;
while (index &lt;=5){<!-- -->
	printf(“%d”, index);
	index = index + 1;
}

```

补全该C程序，执行结果如下图（共11行代码，一次printf()打印输出语句）。

<img src="https://img-blog.csdnimg.cn/2df2d5bb219049edbba8b2985a1e4942.png" alt="在这里插入图片描述">

#### 2. For循环

同样是上述的程序思路，我们用for循环来实现，看看有什么不同。

For循环会在循环开始前初始化表达式一次，也就是给变量赋值，例如：x = 1; 然后指定数值范围，即x &lt;= 5; 最后为变量自增1，即x++. ( 如果需要在执行后续运算前加1，则变为++x), 相关代码段如下：

```
int x;
for (x = 1; x &lt;= 5; x++)
{<!-- -->
    printf("%d", x);
}

```

补全C程序，执行如下图所示。

<img src="https://img-blog.csdnimg.cn/04b334786e164d2eb0f11aa42e2748ac.png" alt="在这里插入图片描述"> 我们看到，该程序同样是遍历1至5的整数，但仅用了10行语句，和一个printf()打印输出语句，并且代码更加紧凑和易读。

#### 3. Do while循环

Do…while循环，是个典型的**出口条件循环**。

在前述例子中，while和for循环都是入口条件循环，也就是说，在每次循环迭代前要检查测试条件，满足了才执行循环体内容。

C语言还提供了出口条件循环，即在每次循环迭代之后检查测试条件，这保证了至少执行循环体一次，这被称为do… while循环。

仍然看整型变量如何遍历1至5的例子。

```
int n = 1, times = 5;
do {<!-- -->
      printf("%d", n);
      n = n + 1;
} while (n &lt;= times)

```

补全代码，执行结果如下图。

<img src="https://img-blog.csdnimg.cn/065372a3c09a446597041206b93c434d.png" alt="在这里插入图片描述">

可以看到，执行do…while循环，总共有10行代码，和一行printf() 函数打印输出。

毋庸置疑，执行循环要比每次都简单输出效率高很多，同时，代码还简洁易读。

#### 结语：如何选择循环？

了解了三种循环后，那么，究竟选择哪种循环呢?

根据工作的需求来看，编写入口条件测试的循环比较常见。也就是说，在执行循环之前测试条件比较好，其次，测试放在循环的开头，代码可读性更高。

总而言之，循环在C程序中的应用非常广泛，后续会探讨嵌套循环和其它可用的复杂循环。

喜欢就点赞哈。😊

技术好文陆续推出，欢迎关注。

相关阅读：
1. 