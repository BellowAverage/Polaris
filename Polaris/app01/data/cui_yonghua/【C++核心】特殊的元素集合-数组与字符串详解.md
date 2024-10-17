
--- 
title:  【C++核心】特殊的元素集合-数组与字符串详解 
tags: []
categories: [] 

---
### 一. 数组

#### 1.1 概述

所谓数组，就是一个集合，里面存放了相同类型的数据元素

**特点1：** 数组中的每个<mark>数据元素都是相同的数据类型</mark>

**特点2：** 数组是由<mark>连续的内存</mark>位置组成的

#### 1.2 一维数组

##### 1.2.1 一维数组定义方式

一维数组定义的三种方式：
1. `数据类型 数组名[ 数组长度 ];`1. `数据类型 数组名[ 数组长度 ] = { 值1，值2 ...};`1. `数据类型 数组名[ ] = { 值1，值2 ...};`
示例

```
int main() {<!-- -->

	//定义方式1
	//数据类型 数组名[元素个数];
	int score[10];

	//利用下标赋值
	score[0] = 100;
	score[1] = 99;
	score[2] = 85;

	//利用下标输出
	cout &lt;&lt; score[0] &lt;&lt; endl;
	cout &lt;&lt; score[1] &lt;&lt; endl;
	cout &lt;&lt; score[2] &lt;&lt; endl;

	//第二种定义方式
	//数据类型 数组名[元素个数] =  {值1，值2 ，值3 ...};
	//如果{}内不足10个数据，剩余数据用0补全
	int score2[10] = {<!-- --> 100, 90,80,70,60,50,40,30,20,10 };
	
	//逐个输出
	//cout &lt;&lt; score2[0] &lt;&lt; endl;
	//cout &lt;&lt; score2[1] &lt;&lt; endl;

	//一个一个输出太麻烦，因此可以利用循环进行输出
	for (int i = 0; i &lt; 10; i++)
	{<!-- -->
		cout &lt;&lt; score2[i] &lt;&lt; endl;
	}

	//定义方式3
	//数据类型 数组名[] =  {值1，值2 ，值3 ...};
	int score3[] = {<!-- --> 100,90,80,70,60,50,40,30,20,10 };

	for (int i = 0; i &lt; 10; i++)
	{<!-- -->
		cout &lt;&lt; score3[i] &lt;&lt; endl;
	}

	system("pause");

	return 0;
}

```

>  
 总结1：数组名的命名规范与变量名命名规范一致，不要和变量重名 总结2：数组中下标是从0开始索引 


##### 1.2.2 一维数组数组名

一维数组名称的 **用途**：
1. 可以统计整个数组在内存中的长度1. 可以获取数组在内存中的首地址
**示例：**

```
int main() {<!-- -->

	//数组名用途
	//1、可以获取整个数组占用内存空间大小
	int arr[10] = {<!-- --> 1,2,3,4,5,6,7,8,9,10 };

	cout &lt;&lt; "整个数组所占内存空间为： " &lt;&lt; sizeof(arr) &lt;&lt; endl;
	cout &lt;&lt; "每个元素所占内存空间为： " &lt;&lt; sizeof(arr[0]) &lt;&lt; endl;
	cout &lt;&lt; "数组的元素个数为： " &lt;&lt; sizeof(arr) / sizeof(arr[0]) &lt;&lt; endl;

	//2、可以通过数组名获取到数组首地址
	cout &lt;&lt; "数组首地址为： " &lt;&lt; (int)arr &lt;&lt; endl;
	cout &lt;&lt; "数组中第一个元素地址为： " &lt;&lt; (int)&amp;arr[0] &lt;&lt; endl;
	cout &lt;&lt; "数组中第二个元素地址为： " &lt;&lt; (int)&amp;arr[1] &lt;&lt; endl;

	//arr = 100; 错误，数组名是常量，因此不可以赋值


	system("pause");

	return 0;
}

```

>  
 注意：数组名是常量，不可以赋值 总结1：直接打印数组名，可以查看数组所占内存的首地址 总结2：对数组名进行sizeof，可以获取整个数组占内存空间的大小 


##### 1.2.3 冒泡排序

**作用：** 最常用的排序算法，对数组内元素进行排序
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。1. 对每一对相邻元素做同样的工作，执行完毕后，找到第一个最大值。1. 重复以上的步骤，每次比较次数-1，直到不需要比较
**示例：** 将数组 { 4,2,8,0,5,7,1,3,9 } 进行升序排序

```
int main() {<!-- -->

	int arr[9] = {<!-- --> 4,2,8,0,5,7,1,3,9 };

	for (int i = 0; i &lt; 9 - 1; i++)
	{<!-- -->
		for (int j = 0; j &lt; 9 - 1 - i; j++)
		{<!-- -->
			if (arr[j] &gt; arr[j + 1])
			{<!-- -->
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}

	for (int i = 0; i &lt; 9; i++)
	{<!-- -->
		cout &lt;&lt; arr[i] &lt;&lt; endl;
	}
    
	system("pause");

	return 0;
}

```

#### 1.3 二维数组

二维数组就是在一维数组上，多加一个维度。

##### 1.3.1 二维数组定义方式

二维数组定义的四种方式：
1. `数据类型 数组名[ 行数 ][ 列数 ];`1. `数据类型 数组名[ 行数 ][ 列数 ] = { {数据1，数据2 } ，{数据3，数据4 } };`1. `数据类型 数组名[ 行数 ][ 列数 ] = { 数据1，数据2，数据3，数据4};`1. ` 数据类型 数组名[ ][ 列数 ] = { 数据1，数据2，数据3，数据4};`
>  
 建议：以上4种定义方式，利用<mark>第二种更加直观，提高代码的可读性</mark> 


示例：

```
int main() {<!-- -->

	//方式1  
	//数组类型 数组名 [行数][列数]
	int arr[2][3];
	arr[0][0] = 1;
	arr[0][1] = 2;
	arr[0][2] = 3;
	arr[1][0] = 4;
	arr[1][1] = 5;
	arr[1][2] = 6;

	for (int i = 0; i &lt; 2; i++)
	{<!-- -->
		for (int j = 0; j &lt; 3; j++)
		{<!-- -->
			cout &lt;&lt; arr[i][j] &lt;&lt; " ";
		}
		cout &lt;&lt; endl;
	}

	//方式2 
	//数据类型 数组名[行数][列数] = { {数据1，数据2 } ，{数据3，数据4 } };
	int arr2[2][3] =
	{<!-- -->
		{<!-- -->1,2,3},
		{<!-- -->4,5,6}
	};

	//方式3
	//数据类型 数组名[行数][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr3[2][3] = {<!-- --> 1,2,3,4,5,6 }; 

	//方式4 
	//数据类型 数组名[][列数] = { 数据1，数据2 ,数据3，数据4  };
	int arr4[][3] = {<!-- --> 1,2,3,4,5,6 };
	
	system("pause");

	return 0;
}

```

>  
 总结：在定义二维数组时，如果初始化了数据，可以省略行数 


##### 1.3.2 二维数组数组名
- 查看二维数组所占内存空间- 获取二维数组首地址
**示例：**

```
int main() {<!-- -->

	//二维数组数组名
	int arr[2][3] =
	{<!-- -->
		{<!-- -->1,2,3},
		{<!-- -->4,5,6}
	};

	cout &lt;&lt; "二维数组大小： " &lt;&lt; sizeof(arr) &lt;&lt; endl;
	cout &lt;&lt; "二维数组一行大小： " &lt;&lt; sizeof(arr[0]) &lt;&lt; endl;
	cout &lt;&lt; "二维数组元素大小： " &lt;&lt; sizeof(arr[0][0]) &lt;&lt; endl;

	cout &lt;&lt; "二维数组行数： " &lt;&lt; sizeof(arr) / sizeof(arr[0]) &lt;&lt; endl;
	cout &lt;&lt; "二维数组列数： " &lt;&lt; sizeof(arr[0]) / sizeof(arr[0][0]) &lt;&lt; endl;

	//地址
	cout &lt;&lt; "二维数组首地址：" &lt;&lt; arr &lt;&lt; endl;
	cout &lt;&lt; "二维数组第一行地址：" &lt;&lt; arr[0] &lt;&lt; endl;
	cout &lt;&lt; "二维数组第二行地址：" &lt;&lt; arr[1] &lt;&lt; endl;

	cout &lt;&lt; "二维数组第一个元素地址：" &lt;&lt; &amp;arr[0][0] &lt;&lt; endl;
	cout &lt;&lt; "二维数组第二个元素地址：" &lt;&lt; &amp;arr[0][1] &lt;&lt; endl;

	system("pause");

	return 0;
}

```

>  
 总结1：二维数组名就是这个数组的首地址 总结2：对二维数组名进行sizeof时，可以获取整个二维数组占用的内存空间大小 


##### **1.3.3 二维数组应用案例**

**考试成绩统计：**

案例描述：有三名同学（张三，李四，王五），在一次考试中的成绩分别如下表，**请分别输出三名同学的总成绩**

||语文|数学|英语
|------
|张三|100|100|100
|李四|90|50|100
|王五|60|70|80

**参考答案：**

```
int main() {<!-- -->

	int scores[3][3] =
	{<!-- -->
		{<!-- -->100,100,100},
		{<!-- -->90,50,100},
		{<!-- -->60,70,80},
	};

	string names[3] = {<!-- --> "张三","李四","王五" };

	for (int i = 0; i &lt; 3; i++)
	{<!-- -->
		int sum = 0;
		for (int j = 0; j &lt; 3; j++)
		{<!-- -->
			sum += scores[i][j];
		}
		cout &lt;&lt; names[i] &lt;&lt; "同学总成绩为： " &lt;&lt; sum &lt;&lt; endl;
	}

	system("pause");

	return 0;
}

```

### 二. 字符串

C++ 提供了以下两种类型的字符串表示形式：
- C 风格字符串- C++ 引入的 string 类类型
#### 2.1 C 风格字符串

C 风格的字符串起源于 C 语言，并在 C++ 中继续得到支持。字符串实际上是使用 null 字符 \0 终止的一维字符数组。因此，一个以 null 结尾的字符串，包含了组成字符串的字符。

C/C++ 中的字符串表示 其实，您不需要把 null 字符放在字符串常量的末尾。C++ 编译器会在初始化数组时，自动把 \0 放在字符串的末尾。让我们尝试输出上面的字符串：

```
#include &lt;iostream&gt;
 
using namespace std;
 
int main ()
{<!-- -->
   char site[7] = {<!-- -->'A', 'B', 'C', 'D', 'E', 'F', '\0'};
 
   cout &lt;&lt; "char类型: " &lt;&lt; site &lt;&lt; endl;

   return 0;
}

```

C++ 中有大量的函数用来操作以 null 结尾的字符串:

>  
 `strcpy(s1, s2)`：复制字符串 s2 到字符串 s1。 `strcat(s1, s2)`：连接字符串 s2 到字符串 s1 的末尾。连接字符串也可以用 + 号，例如: `strlen(s1)`：返回字符串 s1 的长度。 `strcmp(s1, s2)`：如果 s1 和 s2 是相同的，则返回 0；如果 s1&lt;s2 则返回值小于 0；如果 s1&gt;s2 则返回值大于 0。 `strchr(s1, ch)`：返回一个指针，指向字符串 s1 中字符 ch 的第一次出现的位置。 `strstr(s1, s2)`：返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。 示例： 


```
#include &lt;iostream&gt;
#include &lt;cstring&gt;
 
using namespace std;
 
int main ()
{<!-- -->
   char str1[13] = "baidu";
   char str2[13] = "google";
   char str3[13];
   int  len ;
 
   // 复制 str1 到 str3
   strcpy( str3, str1);
   cout &lt;&lt; "strcpy( str3, str1) : " &lt;&lt; str3 &lt;&lt; endl;
 
   // 连接 str1 和 str2
   strcat( str1, str2);
   cout &lt;&lt; "strcat( str1, str2): " &lt;&lt; str1 &lt;&lt; endl;
 
   // 连接后，str1 的总长度
   len = strlen(str1);
   cout &lt;&lt; "strlen(str1) : " &lt;&lt; len &lt;&lt; endl;
 
   return 0;
}

```

执行结果如下：

```
strcpy( str3, str1) : baidu
strcat( str1, str2): baidugoogle
strlen(str1) : 11

```

#### 2.2 C++ 中的 String 类

C++ 标准库提供了 string 类类型，支持上述所有的操作，另外还增加了其他更多的功能。

示例：

```
#include &lt;iostream&gt;
#include &lt;string&gt;
 
using namespace std;
 
int main ()
{<!-- -->
   string str1 = "baidu";
   string str2 = "google";
   string str3;
   int  len ;
 
   // 复制 str1 到 str3
   str3 = str1;
   cout &lt;&lt; "str3 : " &lt;&lt; str3 &lt;&lt; endl;
 
   // 连接 str1 和 str2
   str3 = str1 + str2;
   cout &lt;&lt; "str1 + str2 : " &lt;&lt; str3 &lt;&lt; endl;
 
   // 连接后，str3 的总长度
   len = str3.size();
   cout &lt;&lt; "str3.size() :  " &lt;&lt; len &lt;&lt; endl;
 
   return 0;
}

```

执行结果如下：

```
str3 : baidu
str1 + str2 : baidugoogle
str3.size() :  11

```
