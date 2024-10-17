
--- 
title:  C语言编程入门 – main()函数 
tags: []
categories: [] 

---
## C语言编程入门 – main()函数

### C Programming Language Essentials - main() function

By Jackson@ML

初见C语言，总被一个全球闻名的”Hello, world!”打印输出所惊讶。

#### 1. 开启Hello, world!的C程序

代码如下：

```
# include &lt;stdio.h&gt;
int main(void)
{<!-- -->
    printf("Hello, world!");
    return 0;
}

```

用gcc编译及运行结果如下图：

<img src="https://img-blog.csdnimg.cn/direct/caaa0365268a4b5baa80d9bb6778fe51.png" alt="在这里插入图片描述"> 通常来讲，main函数被称为C/C++语言的重要组成部分，并且它也是C语言程序的入口，程序的执行从这里开始。

基于通识，我们不再质疑为什么非要写个main函数，而是按部就班地去做 – 反正能编译运行就得了。

但仔细看看，就越来越不明白了。

#### 2. 首先，为什么要用int类型放在main()函数前面？

听老师解释，这很简单，返回值是整型，所以要用int。那么，如果不是整形呢？该怎么办？

与其一味听从惯例，不如剖析一下main函数。可不可以把main函数这样来写呢？

```
return_type main() {<!-- -->
	// program statement 1;
	// program statement 2;
	return;
}

```

或者，把不相干的空格和换行去掉，这样写怎么样？

```
int main() {<!-- --> }

```

再或者，仍把void放进main()，表示不接受任何信息，这样写呢？

```
int main(void) {<!-- --> }

```

事实证明，这样的形式，编译器接受。（当然，还需要必要的内容）

#### 3. main()函数既然是函数，如何被用户调用呢？

我们看到的程序示例，似乎只有两大类，
- 一类main函数返回整型（例如，函数体最后的语句return 0; ）;- 另一类不返回值（例如，void main()）.
事实上，关于main函数，有几个重要特点：

1） main()函数是程序开始执行的函数； 2） 每个程序都仅有一个main()函数； 3） 程序的主函数为main(), 而不是其它名称； 4） Main()函数始终返回整型(int)或没有返回类型（void）. 5） Main函数编译时，就决定了由操作系统调用，而不是被用户来调用。

#### 4. main()函数看起来有三种类型：

1） 不参数但返回类型为int的main函数；

说明该函数返回整型，但不传递参数，如下代码：

```
# include &lt;stdio.h&gt;
int main(void)
{<!-- -->
    printf("Hello, world!");
    return 0;
}

```

运行结果为：

```
Hello, world!

```

2） 不带参数也没有返回类型的main函数；

说明main函数不返回值，也不传递参数。如下代码：

```
# include &lt;stdio.h&gt;
void main()
{<!-- -->
    printf("Hello, world!");    
}

```

运行结果为：

```
Hello，world!

```

3） 带有命令行参数的main函数。

在下面的示例中，向main()函数传递参数。这些参数成为命令行参数，预先不写入程序，，而是在编译完运行时给出，使得程序运行。其中：
- 第一个参数argc1表示计数，它存储命令行传递参数的个数；默认情况下，当没有传递参数时，它的值为1；- 第二个参数argc2是一个指针数组argv[ ], 它存储了所有传递的命令行参数。在输出中也可以看到，在不传递任何命令行参数的情况下运行程序时，argc的值为1。 代码如下所示：
```
# include &lt;stdio.h&gt;
int main(int argc, char* argv[])
{<!-- -->
    printf("Value of argc is %d\n", argc);
    for (int i = 0; i &lt; argc; i++ ){<!-- -->
        printf("%s \n", argv[i]);
    }
}

```

将该C程序文件命名为argc.c, 执行编译：

```
gcc argc.c

```

之后，执行带参数的运行命令：

```
./argc.exe Welcome Greetings Prosperity

```

运行结果如下图：

<img src="https://img-blog.csdnimg.cn/direct/8eba1b4f7313407391e2ca619f868e45.png" alt="在这里插入图片描述"> 以上简要介绍了main()函数在C程序中的应用。

后续有技术好文不断推出。敬请关注。😃
