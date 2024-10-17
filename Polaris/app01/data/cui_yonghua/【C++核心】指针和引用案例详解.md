
--- 
title:  【C++核心】指针和引用案例详解 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- <ul><li>- - - - - - - - - - - - - 


### 一. 指针

#### 1.1 指针的基本概念

**指针的作用：** <mark>可以通过指针间接访问内存</mark>
- 内存编号是从0开始记录的，一般用十六进制数字表示- 可以利用指针变量保存地址
#### 1.2 指针变量的定义和使用

指针变量定义语法： `数据类型 * 变量名；`

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	//1、指针的定义
	int a = 10; //定义整型变量a
	
	//指针定义语法： 数据类型 * 变量名 ;
	int * p;

	//指针变量赋值
	p = &amp;a; //指针指向变量a的地址
	cout &lt;&lt; &amp;a &lt;&lt; endl; //打印数据a的地址
	cout &lt;&lt; p &lt;&lt; endl;  //打印指针变量p

	//2、指针的使用
	//通过*操作指针变量指向的内存
	cout &lt;&lt; "*p = " &lt;&lt; *p &lt;&lt; endl;

	return 0;
}

```

指针变量和普通变量的区别
- 普通变量存放的是数据,<mark>指针变量存放的是地址</mark>- 指针变量可以通过" * "操作符，操作指针变量指向的内存空间，这个过程称为解引用
>  
 总结1： 我们可以通过 &amp; 符号 获取变量的地址 总结2：利用指针可以记录地址 总结3：对指针变量解引用，可以操作指针指向的内存 


#### 1.3 指针所占内存空间

提问：指针也是种数据类型，那么这种数据类型占用多少内存空间？

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	int a = 10;

	int * p;
	p = &amp;a; //指针指向数据a的地址

	cout &lt;&lt; *p &lt;&lt; endl; //* 解引用
	cout &lt;&lt; sizeof(p) &lt;&lt; endl;
	cout &lt;&lt; sizeof(char *) &lt;&lt; endl;
	cout &lt;&lt; sizeof(float *) &lt;&lt; endl;
	cout &lt;&lt; sizeof(double *) &lt;&lt; endl;

	return 0;
}

```

>  
 总结：所有指针类型在32位操作系统下是4个字节 


#### 1.4 空指针和野指针

**空指针**：指针变量指向内存中编号为0的空间

**用途：** 初始化指针变量

**注意：** 空指针指向的内存是不可以访问的

**示例1：空指针**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	//指针变量p指向内存地址编号为0的空间
	int * p = NULL;

	//访问空指针报错 
	//内存编号0 ~255为系统占用内存，不允许用户访问
	cout &lt;&lt; *p &lt;&lt; endl;

	system("pause");
	return 0;
}

```

**野指针**：指针变量指向非法的内存空间

**示例2：野指针**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	//指针变量p指向内存地址编号为0x1100的空间
	int * p = (int *)0x1100;

	//访问野指针报错 
	cout &lt;&lt; *p &lt;&lt; endl;

	system("pause");
	return 0;
}

```

>  
 总结：空指针和野指针都不是我们申请的空间，因此不要访问。 


#### 1.5 const修饰指针

const修饰指针有三种情况
1. const修饰指针 — 常量指针1. const修饰常量 — 指针常量1. const即修饰指针，又修饰常量
**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	int a = 10;
	int b = 10;

	//const修饰的是指针，指针指向可以改，指针指向的值不可以更改
	const int * p1 = &amp;a; 
	p1 = &amp;b; //正确
	//*p1 = 100;  报错
	
	//const修饰的是常量，指针指向不可以改，指针指向的值可以更改
	int * const p2 = &amp;a;
	//p2 = &amp;b; //错误
	*p2 = 100; //正确

    //const既修饰指针又修饰常量
	const int * const p3 = &amp;a;
	//p3 = &amp;b; //错误
	//*p3 = 100; //错误

	system("pause");
	return 0;
}

```

>  
 技巧：看const右侧紧跟着的是指针还是常量, 是指针就是常量指针，是常量就是指针常量 


#### 1.6 指针和数组

**作用：** 利用指针访问数组中元素

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	int arr[] = {<!-- --> 1,2,3,4,5,6,7,8,9,10 };

	int * p = arr;  //指向数组的指针

	cout &lt;&lt; "第一个元素： " &lt;&lt; arr[0] &lt;&lt; endl;
	cout &lt;&lt; "指针访问第一个元素： " &lt;&lt; *p &lt;&lt; endl;

	for (int i = 0; i &lt; 10; i++)
	{<!-- -->
		//利用指针遍历数组
		cout &lt;&lt; *p &lt;&lt; endl;
		p++;
	}

	system("pause");
	return 0;
}

```

#### 1.7 指针和函数

**作用：** 利用指针作函数参数，可以修改实参的值

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

//值传递
void swap1(int a ,int b)
{<!-- -->
	int temp = a;
	a = b; 
	b = temp;
}
//地址传递
void swap2(int * p1, int *p2)
{<!-- -->
	int temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}

int main() {<!-- -->

	int a = 10;
	int b = 20;
	swap1(a, b); // 值传递不会改变实参

	swap2(&amp;a, &amp;b); //地址传递会改变实参

	cout &lt;&lt; "a = " &lt;&lt; a &lt;&lt; endl;
	cout &lt;&lt; "b = " &lt;&lt; b &lt;&lt; endl;

	system("pause");
	return 0;
}

```

>  
 总结：如果不想修改实参，就用值传递，如果想修改实参，就用地址传递 


#### 1.8 指针、数组、函数

**案例描述：** 封装一个函数，利用冒泡排序，实现对整型数组的升序排序

例如数组：`int arr[10] = { 4,3,6,9,1,2,10,8,7,5 };`

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

//冒泡排序函数
void bubbleSort(int * arr, int len)  //int * arr 也可以写为int arr[]
{<!-- -->
	for (int i = 0; i &lt; len - 1; i++)
	{<!-- -->
		for (int j = 0; j &lt; len - 1 - i; j++)
		{<!-- -->
			if (arr[j] &gt; arr[j + 1])
			{<!-- -->
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

//打印数组函数
void printArray(int arr[], int len)
{<!-- -->
	for (int i = 0; i &lt; len; i++)
	{<!-- -->
		cout &lt;&lt; arr[i] &lt;&lt; endl;
	}
}

int main() {<!-- -->

	int arr[10] = {<!-- --> 4,3,6,9,1,2,10,8,7,5 };
	int len = sizeof(arr) / sizeof(int);

	bubbleSort(arr, len);

	printArray(arr, len);

	system("pause");
	return 0;
}

```

>  
 总结：当数组名传入到函数作为参数时，被退化为指向首元素的指针 


### 二. 引用

#### 2.1 引用的基本使用

**作用：** 给变量起别名

**语法：** `数据类型 &amp;别名 = 原名`

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	int a = 10;
	int &amp;b = a;

	cout &lt;&lt; "a = " &lt;&lt; a &lt;&lt; endl;
	cout &lt;&lt; "b = " &lt;&lt; b &lt;&lt; endl;

	b = 100;

	cout &lt;&lt; "a = " &lt;&lt; a &lt;&lt; endl;
	cout &lt;&lt; "b = " &lt;&lt; b &lt;&lt; endl;

	return 0;
}

```

#### 2.2 引用注意事项
- 引用必须初始化- 引用在初始化后，不可以改变
示例：

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	int a = 10;
	int b = 20;
	//int &amp;c; //错误，引用必须初始化
	int &amp;c = a; //一旦初始化后，就不可以更改
	c = b; //这是赋值操作，不是更改引用

	cout &lt;&lt; "a = " &lt;&lt; a &lt;&lt; endl;
	cout &lt;&lt; "b = " &lt;&lt; b &lt;&lt; endl;
	cout &lt;&lt; "c = " &lt;&lt; c &lt;&lt; endl;

	return 0;
}

```

#### 2.3 引用做函数参数

**作用：** 函数传参时，可以利用引用的技术让形参修饰实参

**优点：** 可以简化指针修改实参

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

//1. 值传递
void mySwap01(int a, int b) {<!-- -->
	int temp = a;
	a = b;
	b = temp;
}

//2. 地址传递
void mySwap02(int* a, int* b) {<!-- -->
	int temp = *a;
	*a = *b;
	*b = temp;
}

//3. 引用传递
void mySwap03(int&amp; a, int&amp; b) {<!-- -->
	int temp = a;
	a = b;
	b = temp;
}

int main() {<!-- -->

	int a = 10;
	int b = 20;

	mySwap01(a, b);
	cout &lt;&lt; "a:" &lt;&lt; a &lt;&lt; " b:" &lt;&lt; b &lt;&lt; endl;

	mySwap02(&amp;a, &amp;b);
	cout &lt;&lt; "a:" &lt;&lt; a &lt;&lt; " b:" &lt;&lt; b &lt;&lt; endl;

	mySwap03(a, b);
	cout &lt;&lt; "a:" &lt;&lt; a &lt;&lt; " b:" &lt;&lt; b &lt;&lt; endl;

	system("pause");

	return 0;
}


```

>  
 总结：通过引用参数产生的效果同按地址传递是一样的。引用的语法更清楚简单 


#### 2.4 引用做函数返回值

作用：引用是可以作为函数的返回值存在的

注意：**不要返回局部变量引用**

用法：函数调用作为左值

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

//返回局部变量引用
int&amp; test01() {<!-- -->
	int a = 10; //局部变量
	return a;
}

//返回静态变量引用
int&amp; test02() {<!-- -->
	static int a = 20;
	return a;
}

int main() {<!-- -->

	//不能返回局部变量的引用
	int&amp; ref = test01();
	cout &lt;&lt; "ref = " &lt;&lt; ref &lt;&lt; endl;
	cout &lt;&lt; "ref = " &lt;&lt; ref &lt;&lt; endl;

	//如果函数做左值，那么必须返回引用
	int&amp; ref2 = test02();
	cout &lt;&lt; "ref2 = " &lt;&lt; ref2 &lt;&lt; endl;
	cout &lt;&lt; "ref2 = " &lt;&lt; ref2 &lt;&lt; endl;

	test02() = 1000;

	cout &lt;&lt; "ref2 = " &lt;&lt; ref2 &lt;&lt; endl;
	cout &lt;&lt; "ref2 = " &lt;&lt; ref2 &lt;&lt; endl;

	return 0;
}

```

#### 2.5 引用的本质

本质：**引用的本质在c++内部实现是一个指针常量.**

讲解示例：

```
#include&lt;iostream&gt;
using namespace std;

//发现是引用，转换为 int* const ref = &amp;a;
void func(int&amp; ref){<!-- -->
	ref = 100; // ref是引用，转换为*ref = 100
}
int main(){<!-- -->
	int a = 10;
    
    //自动转换为 int* const ref = &amp;a; 指针常量是指针指向不可改，也说明为什么引用不可更改
	int&amp; ref = a; 
	ref = 20; //内部发现ref是引用，自动帮我们转换为: *ref = 20;
    
	cout &lt;&lt; "a:" &lt;&lt; a &lt;&lt; endl;
	cout &lt;&lt; "ref:" &lt;&lt; ref &lt;&lt; endl;
    
	func(a);
	return 0;
}

```

结论：C++推荐用引用技术，因为语法方便，引用本质是指针常量，但是所有的指针操作编译器都帮我们做了

#### 2.6 常量引用

**作用：** 常量引用主要用来修饰形参，防止误操作

在函数形参列表中，可以加<mark>const修饰形参</mark>，防止形参改变实参

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

//引用使用的场景，通常用来修饰形参
void showValue(const int&amp; v) {<!-- -->
	//v += 10;
	cout &lt;&lt; v &lt;&lt; endl;
}

int main() {<!-- -->

	//int&amp; ref = 10;  引用本身需要一个合法的内存空间，因此这行错误
	//加入const就可以了，编译器优化代码，int temp = 10; const int&amp; ref = temp;
	const int&amp; ref = 10;

	//ref = 100;  //加入const后不可以修改变量
	cout &lt;&lt; ref &lt;&lt; endl;

	//函数中利用常量引用防止误操作修改实参
	int a = 10;
	showValue(a);

	system("pause");

	return 0;
}
``

```
