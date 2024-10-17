
--- 
title:  c++学习笔记1_封装CMatrix类 
tags: []
categories: [] 

---
实验要求：熟悉C++类的使用，和对类的封装 <img src="https://img-blog.csdnimg.cn/3ef7b5f4731749619e07d1833a24a302.png" alt="在这里插入图片描述"> 

#### 文章目录
- - - <ul><li>- <ul><li>- - <ul><li>- - - - - <ul><li>- - - - - - - - - - - - 


## 为何要数据抽象和封装
- 避免类内部出现无意的、可能破坏对象状态的用户级错误- 随时间推移可以根据需求改变货缺陷报告来完善类实现，而无需改变用户级代码
## 一、类

### 1. 类的定义和声明

#### 1.1 概念

**类：** 类是一种将抽象转化为用户定义类型（用户定义类型：实现**抽象接口**的类设计）的C++工具。

**接口：** 接口是一个共享框架，共两个系统（eg：我与计算机）交互时使用。比如我们使用计算机时，程序接口将我们的意图转化为存储在计算机中的具体信息。 通常，将接口（类定义）放在**头文件（类声明)<strong>中，将实现（类方法的代码）放在**源代码</strong>文件中。 一般，我们将类名首字母大写（常见但不通用的约定）

**类设计：** 类设计应尽可能将公有接口与实现细节分开。例如，将类函数定义和类声明放在不同的文件中。 公有接口表示设计的抽象组件————————————类声明 将实现细节放在一起并将细节与抽象分开（封装）——类函数定义

#### 1.2 类声明

##### 1.2.1 访问控制

防止程序直接访问数据-》数据隐藏 public (都可以访问） private（数据隐藏：数据部分的访问状态时私有的，这意味这程序不能直接访问数据成员，只能通过成员函数来访问数据成员） protected（与private类似，区别只有在基类派生的类中才会表现出来）

由于隐藏数据时OOP的主要目标之一，通常将**数据项放在私有部分**，**组成类接口的成员函数放在公有部分**。 <img src="https://img-blog.csdnimg.cn/be939a0e745142cdaf7b949bb810e89d.png" alt="在这里插入图片描述">

##### 1. 2. #ifndef：

**#ifndef** 来访问多次包含包含同一个文件

```
#ifndef &lt;标识&gt; 
...
#endif 

```

>  
 #ifndef起到的效果是**防止一个源文件两次包含同一个头文件**，而不是防止两个源文件包含同一个头文件。事实上，防止同一头文件被两个不同的源文件包含这种要求本身就是不合理的，头文件存在的价值就是被不同的源文件包含。 假如你有一个C源文件，它包含了多个头文件，比如头文件A和头文件B，而头文件B又包含了头文件A，则最终的效果是，该源文件包含了两次头文件A。如果你在头文件A里定义了结构体或者类类型（这是最常见的情况），那么问题来了，编译时会报大量的重复定义错误。 


#### 1.3 实现类成员函数

基本与常规函数定义类似，有两个特征：
- 定义成员函数时，使用**作用域解析运算符**(::)来标识函数所属的类- 类方法可以访问类的**private**组件（非成员函数禁止这样做，友元函数除外）
#### 1.4 const成员函数

<img src="https://img-blog.csdnimg.cn/283b546fa8d042e99f0ae092ab7c991c.png" alt="在这里插入图片描述"> 像这种方式声明和定义的类函数——&gt;const成员函数 只要类方法不修改调用对象，就应该声明为const
1. 在C++中，只有被声明为const的成员函数才能被一个const类对象调用。 值得注意的是，如果类中存在指针类型的数据成员即便是const函数只能保证不修改该指针的值，并不能保证不修改指针指向的对象。1. const成员函数可以被对应的具有相同形参列表的非const成员函数重载
### 2. this指针

this为对象的地址，*this为对象本身

当类成员函数涉及到两个对象时，需要使用this指针 每个成员函数（包括构造函数和析构函数）都有一个this指针，this指针指向调用对象。

如果在函数后面加上const(const成员函数)，将this限定为从const，则不能使用this来修改对象的值。 返回类型为引用（* this 专门用于表示当前对象的地址）——返回的时调用对象本身而不是副本 <img src="https://img-blog.csdnimg.cn/45917752b9a8425cbb93116296f6b46c.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/45da0b6866194585ab68d9d43ad71309.png" alt="在这里插入图片描述"> 关于**运算符重载**可以看文章的后面部分

### 3. 构造函数与析构函数

#### 3.1 构造函数

最好在创建对象时对它进行初始化，C++提供了一个特殊的成员函数——类构造函数，专门用于构造新对象、将值赋给它们的数据成员（在创建类对象时被调用）。 由于类名的唯一性和类对象名的随意性，得以想到使用类名而不是对象名来作为构造函数的名称。

通过**函数重载**，可以创建多个同名的构造函数，条件是他们的 **参数列表** 不同 默认构造函数 （如果没有提供任何构造函数，c++将自动提供默认构造函数,但是为类定义了构造函数之后，程序员就必须为其提供默认构造函数） <img src="https://img-blog.csdnimg.cn/e3cc4317d55e4e0884067843b5c9fc9a.png" alt="在这里插入图片描述"> **构造函数是特殊的成员函数，只要创建类类型的新对象，都要执行构造函数，其目的是保证每个对象的数据成员具有合适的初始值。**

构造对象创建实体，如果创建失败，将导致程序异常终止（例如内存空间短缺），因此，构造函数不以对象体作为函数的返回值。 又因为它是类型名称引导的定义语句，不是无返回的函数调用语句，故也不是无类型（void）函数。

**无名对象:**

```
cout&lt;&lt;CMatrix(0,0,0);//无名对象在执行完&lt;&lt;后就烟消云散了

```

如果创建对象时不给出对象名，直接使用类名调用构造函数，即产生无名对象。一般在创建后不需要重复使用的场合出现。

#### 3.2 析构函数

在构造函数创建对象后，程序负责跟踪该对象，直到其过期为止。**对象过期时，程序将自动调用析构函数。<strong>析构函数将完成清理工作，如果构造函数中使用**new</strong>来分配内存，那么析构函数将使用**delete**来释放这些内存。 动态内存申请是人为的，与之对应，释放也是人为的，系统不会自动为对象做内存释放工作。

构造函数和析构函数都可以没有返回值和声明类型。 <img src="https://img-blog.csdnimg.cn/d10a6532a74b40e7b74f5c39ddea92ec.png" alt="在这里插入图片描述"> 此外，析构函数还可以没有参数。

对象构造和析构关系是栈数据结构中入栈和出栈的关系。（顺序正好相反）

### 4. 对象数组

初始化对象数组的方案是，首先使用默认构造函数创建数组元素，然后花括号中的构造函数将创建临时对象，然后将临时对象的内容复制到相应的元素中。因此，要创建类对象数组，则这个类必须有默认构造函数。

实验中没有涉及 到。

### 5. 类作用域
1. 在类中定义的名称（如类数据成员名和类成员函数名）的作用域都为**整个类**，作用域为整个类的名称只在该类中是已知的，在类外是不可知的。因此，可以在不同类中使用相同的类成员名而不会引起冲突。1. 类作用域意味着不能从外部直接访问类的成员，公有成员函数也是如此。也就是说，要调用公有成员函数，必须通过对象。 
### 6. 抽象数据类型

CMatrix 类非常具体。然而，程序员常常通过定义类来表示更通用的概念。 例如，就实现计算机专家们所说的抽象数据类型(abstract data type，ADT)而言，使用类是一种非常好的方式。顾名思义，ADT 以通用的方式描述数据类型，而没有引入语言或实现细节。例如，通过使用栈，可以以这样的方式存储数据，即总是从堆顶添加或删除数据。例如，C++程序使用栈来管理自动变量。当新的自动变量被生成后，它们被添加到堆顶;消亡时,从栈中删除它们。

## 二、使用类

### 1. 运算符重载

函数多态（函数重载）指的是可以有多个同名的函数，因此对函数的名称进行了重载。 **特征标**——函数的参数列表（特征标相同==参数数目和类型相同+参数的排列顺序相同（与变量名无关））

**注意点：**
- C++进行检查时，为了避免混乱，将类型引用 &amp;x 和类型本身 x 是为同一特征标- const指针和常规指针要注意：将**非const值赋给const是合法**的，但反之是非法的- 如果函数调用没有和任何原型匹配，C++将尝试使用标准类型转换 强制进行匹配
运算符重载是一种形式的C++**多态**。

**重载限制：**
1. 重载后的运算符必须至少有一个操作数是用定义的类型（防止用户为标准类型重载运算符）1. 使用运算符时不能违反运算符原来的句法规则（例如，不能改变运算符的优先级）1. 不能创建新的运算符 <img src="https://img-blog.csdnimg.cn/b7eeb5520e404730b504ff7d5d772bb4.png" alt="在这里插入图片描述">
<img src="https://img-blog.csdnimg.cn/1e17cc34f62643ae8c9a5bfb82a62855.png" alt=""> <img src="https://img-blog.csdnimg.cn/c5a7d878f362495b96ee99f69c162e4d.png" alt="在这里插入图片描述">

#### 1. 1 赋值操作符

```
// 重载=运算符
CMatrix &amp; CMatrix::operator=(const CMatrix &amp; mIn)
{<!-- -->
	Release();
	m_nRow=mIn.m_nRow;
	m_nCol=mIn.m_nCol;
	m_pData=new double[m_nRow*m_nCol];
	memcpy(m_pData,mIn.m_pData,sizeof(double)*m_nRow*m_nCol);
	return *this;
}
// 重载+=运算符 写法一（使用时只能写一种写法）
CMatrix &amp; CMatrix:: operator+=(const CMatrix &amp;b)
{<!-- -->	// 该函数隐式地访问一个对象，显式地访问另一个对象，并返回其中一个对象的引用
	if(m_nRow==b.m_nRow&amp;&amp;m_nCol==b.m_nCol)
	{<!-- -->
		for(int i=0;i&lt;m_nRow*m_nCol;i++)
		{<!-- -->
			m_pData[i]=m_pData[i]+b.m_pData[i];
		}
	}
	return *this;
}
// 重载+=运算符 写法二（使用时只能写一种写法）
CMatrix &amp; CMatrix::operator+=(const CMatrix &amp;a,const CMatrix &amp;b)
{<!-- -->
	CMatrix c;
	if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
	{<!-- -->
		c.Create(a.m_nRow,a.m_nCol);
		for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
		{<!-- -->
			c.m_pData[i]=a.m_pData[i]+b.m_pData[i];
		}
	}
	return c;
}

```

#### 1. 2 输入和输出运输符

```
// 重载&lt;&lt;运算符
ostream &amp; operator&lt;&lt;(ostream &amp;out, const CMatrix &amp; s) 
{<!-- -->
	out&lt;&lt;s.m_nRow&lt;&lt;"\t"&lt;&lt;s.m_nCol&lt;&lt;"\t";
	for(int i=0;i&lt;s.m_nRow*s.m_nCol;i++)
		out&lt;&lt;s.m_pData[i]&lt;&lt;"\t";
	return out;
}
// 重载&gt;&gt;运算符
istream &amp; operator&gt;&gt;(istream &amp;in, CMatrix &amp; s) 
{<!-- -->
	if(s.m_pData)
	{<!-- -->
		delete[] s.m_pData;
		s.m_nRow=0;
		s.m_nCol=0; 
	}
	in&gt;&gt;s.m_nRow&gt;&gt;s.m_nCol;
	s.m_pData = new double[s.m_nRow*s.m_nCol];
	for(int i=0;i&lt;s.m_nRow*s.m_nCol;i++)
	{<!-- -->
		in&gt;&gt;s.m_pData[i];
	}
	return in;
}

```

#### 1. 3 算术运算符重载

```
CMatrix &amp; CMatrix::operator+(const CMatrix &amp;a,const CMatrix &amp;b)
{<!-- -->
	CMatrix c;
	if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
	{<!-- -->
		c.Create(a.m_nRow,a.m_nCol);
		for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
		{<!-- -->
			c.m_pData[i]=a.m_pData[i]+b.m_pData[i];
		}
	}
	return c;
}

```

#### 1. 4 关系运算符重载

```
bool &amp; CMatrix::operator==(const CMatrix &amp;b)
{<!-- -->
	bool flag=true;
	if(m_nRow==b.m_nRow&amp;&amp;m_nCol==b.m_nCol)
		{<!-- -->
			for(int i=0;i&lt;m_nRow*m_nCol;i++)
			{<!-- -->
				if(m_pData[i]!=b.m_pData[i])
					flag=false;		
			}
		}
		return flag;
}

```

#### 1. 5 下标操作符

```
double &amp; CMatrix::operator[](int nIndex){<!-- -->
	return m_pData[nIndex];
}

```

#### 1. 6 调用操作符

```
double &amp; CMatrix::operator()(int i,int j){<!-- -->
	return m_pData[i*m_nRow+j];
}

```

#### 1.7 增量操作符

（实验中未涉及）

“++”操作有前增量与后增量之分。因此再重载增量操作符时，虽然操作符（函数名）相同，但实现的功能不同。其差别反映在**特征标**的不同；此外，为了反映操作的本质，返回类型的表现也可以不同。

```
int a=1,b=1,c=1,d=1;
(++a)++; //a=3
(b++)++; //b=2 因为(b++)的结果是临时变量，在其加上1之后被抛弃
++(++c); //c=3
++(d++); //d=2

```

`前增量`（++a）是**左值**，操作可以连贯，故变量最终值与后增量结果是一致的。 前增量操作数与返回值是同一个变量。故其重载要求参数为对象的引用，返回值仍为该对象参数的引用。

```
X operator++(x &amp;a);
++a;   //等价于 operator++(a)

```

`后增量`（a++）的结果是增量之前的**临时变量**，为临时变量，当表达式计算工作完成之后，该临时变量随即消失，故变量最终值与后增量结果是错位的。 故其重载要求参数为对象的引用。 因为在调用的上下文中，实参将发生变化，则返回为临时变量。 为了防止两个操作符的特征标相同，C++做了一个技术处理（防止编译报错）

```
X operator++(x &amp;a,int b);
a++;   //等价于 operator++(a,1)

```

### 2. 友元

友元（Friends） <img src="https://img-blog.csdnimg.cn/11e656751ba94c0aa972654fb23baa07.png" alt="在这里插入图片描述">通过让函数成为类的友元，可以赋予该函数与类的成员函数相同的访问权限（可以访问私有数据）。 友元声明可以位于公有、私有或保护部分，其所在位置无关紧要。

作用：给予了不同性质对象之间的亲密无间性，提高了公用接口的灵活性

### 3. 转换

C++是如何处理内置类型转换： 将一个标准类型变量的值赋给另一种标准类型的变量时，如果这两种类型兼容，则C++自动将这个值转换为接收变量的类型。

```
// 自动转换
int side = 3.33; // double value 3.33 converted to type int 3
// 强制转换
int * p =(int *) 10; // ok, p and (int *) 10 both pointers

```

类的自动转换和强制类型转换 <img src="https://img-blog.csdnimg.cn/70b607bdd7634e67b70d6f88bb895570.png" alt="在这里插入图片描述">

```
CMatrix::operator double() const
{<!-- -->
	// 不需要返回值，这个是隐式类型转换
	// 虽然没有声明返回类型，但是这个函数也将返回所需的值。
	double sum=0;
	for(int i=0;i&lt;m_nRow*m_nCol;i++)
	{<!-- -->
		sum+=m_pData[i];
	} 
	return sum;
}

```

### 4. static 类成员

>  
 注意：不要将静态成员的定义放在头文件中，除非保证该头文件不会被两个不同的源文件包含，不然会报重复定义错误，相当于是在两个源文件中都定义了同一个变量。对于这种同一头文件被不同源文件包含的情况，使用#ifndef或者#pragma once是没用的。这种预编译宏是为了解决一个源文件两次包含同一个头文件的问题。 同时，对静态数据成员的定义也不能放在main()函数里，否则编译报错：error C2655: “Box::height”: 当前范围内的定义或重新声明非法。正确的做法，就如上面所说，把它放在定义类的成员函数的源文件中。 原文链接：https://blog.csdn.net/fb_941219/article/details/101024110 


**作用： 使得记录对象们的整体数据不必随单一数据而苟合，也不必随单一对象而捆绑操作**。

#### 4.1 静态数据成员

类的静态成员，保证每个类只有一个实体，保存在类名空间的全局数据区中，不属于各个对象，每个对象中不再有它的副本。整个类中只有一份拷贝，所有对象都共享这份拷贝。 类的静态成员，属于脱离对象存在的性质，所有应该在实体对象产生之前存在，因此适合在程序启动的时候，将其初始化。

该实体在程序中的唯一性，要求不能随着类定义放在头文件中，但是其有时类成员的一部分，因此放在类的实现代码中是最合适的。

在类外分配空间和初始化。（需要:: 以表明该成员的类属 ） 如果不将其初始化，则系统将为成员清0。

#### 4.1 静态成员函数

将数据成员做成私有的，用静态成员函数去访问静态数据成员 静态成员函数不受对象前置，可以用类名加上域操作符调用静态成员函数。

```
// 声明.h
static int GetDim();
// 实现.cpp
int CMatrix::GetDim()
{<!-- -->
	cout&lt;&lt;"GetDim()" &lt;&lt;endl;
	return m_nDim;
}
// 使用类.cpp
CMatrix::GetDim();

```

## 实验部分（封装CMatrix类）

### 1. 类声明——cmatrix.h

```
#ifndef CMATRIX_R
#define CMATRIX_R
#include &lt;string&gt;
#include &lt;iostream&gt;
using namespace std;

class CMatrix
{<!-- -->
public:
	 CMatrix():m_pData(0),m_nCol(0),m_nRow(0){<!-- -->}
	 CMatrix(int nRow,int nCol,double * pData=NULL);
	 bool Create(int nRow,int nCol);
	 void Release();
	 ~CMatrix();//析构函数
	 
	 bool Read(string strPath);
	 bool Write(string strPath) const;
	 
	 inline double Get(int nIndex) const;
	 inline double Get(int nRow,int nCol) const;
	 
	 CMatrix &amp; Set(int nIndex,double dVal);
	 CMatrix &amp; Set(int nRow,int nCol,double dVal);
	 
	 CMatrix &amp;operator=(const CMatrix &amp;mIn);
	 CMatrix &amp;operator+=(const CMatrix &amp;b);
	 bool &amp;operator==(const CMatrix &amp;b);
	 double &amp;operator[](int nIndex);
	 double &amp;operator()(int i,int j);
	 //CMatrix &amp;operator+(const CMatrix &amp;a,const CMatrix &amp;b);
	 operator double() const;
	 static int GetDim();
private:
	// 友元函数
	// 直接定义（不需要声明） 
	friend ostream &amp; operator&lt;&lt;(ostream &amp;out, const CMatrix &amp; s) 
	{<!-- -->
		cout&lt;&lt;"重载&lt;&lt;" &lt;&lt;endl;
		out&lt;&lt;s.m_nRow&lt;&lt;"\t"&lt;&lt;s.m_nCol&lt;&lt;"\t";
		for(int i=0;i&lt;s.m_nRow*s.m_nCol;i++)
			out&lt;&lt;s.m_pData[i]&lt;&lt;"\t";
		return out;
	}
	friend istream &amp; operator&gt;&gt;(istream &amp;in, CMatrix &amp; s) 
	{<!-- -->
		cout&lt;&lt;"重载&gt;&gt;" &lt;&lt;endl;
		if(s.m_pData)
		{<!-- -->
			delete[] s.m_pData;
			s.m_nRow=0;
			s.m_nCol=0; 
		}
		in&gt;&gt;s.m_nRow&gt;&gt;s.m_nCol;
		s.m_pData = new double[s.m_nRow*s.m_nCol];
		for(int i=0;i&lt;s.m_nRow*s.m_nCol;i++)
		{<!-- -->
			in&gt;&gt;s.m_pData[i];
		}
		return in;
	}
	friend CMatrix operator+(const CMatrix &amp;a,const CMatrix &amp;b)
	{<!-- -->
		cout&lt;&lt;"重载+" &lt;&lt;endl;
		CMatrix c;
		if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
		{<!-- -->
			c.Create(a.m_nRow,a.m_nCol);
			for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
			{<!-- -->
				c.m_pData[i]=a.m_pData[i]+b.m_pData[i];
			}
		}
		return c;
	}
	/* 
	//这部分在cmatrix.cpp中定义 需要先声明
	friend  CMatrix operator+=(const CMatrix &amp;a,const CMatrix &amp;b)
	{
		CMatrix c;
		if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
		{
			c.Create(a.m_nRow,a.m_nCol);
			for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
			{
				c.m_pData[i]=a.m_pData[i]+b.m_pData[i];
			}
		}
		return c;
	}
	friend  bool operator==(const CMatrix &amp;a,const CMatrix &amp;b)
	{
		bool flag=true;
		if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
		{
			for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
			{
				if(a.m_pData[i]!=b.m_pData[i])
					flag=false;
			}
		}
		return flag;
	}
	*/
	
	double * m_pData;
	int m_nCol;//列数 
	int m_nRow;//行数 
	
	static const int m_nDim=2;//const 修饰成员变量 
};
// 内联函数 需要先声明
inline double CMatrix::Get(int nIndex) const
{<!-- -->
	cout&lt;&lt;"Get(int)" &lt;&lt;endl;
	return m_pData[nIndex];
}
inline double CMatrix::Get(int nRow,int nCol) const
{<!-- -->
	cout&lt;&lt;"Get(int,int)" &lt;&lt;endl;
	return m_pData[nRow*nCol+nCol];
}

#endif //CMATRIX_H

```

### 2. 实现类成员函数——cmatrix.cpp

```
#include "cmatrix.h"
#include &lt;fstream&gt;
#include&lt;string&gt;
#include&lt;string.h&gt;
CMatrix::CMatrix(int nRow,int nCol,double * pData)// 构造函数
{<!-- -->
	cout&lt;&lt;"CMatrix(int,int,double)" &lt;&lt;endl;
	m_pData=NULL;
	Create(nRow,nCol);
	if(pData)
	{<!-- -->
		//memcpy 函数用于 把资源内存（src所指向的内存区域） 拷贝到目标内存（dest所指向的内存区域）；拷贝多少个？有一个size变量控制
		memcpy(m_pData,pData,sizeof(double)*nRow*nCol);
	}
}
CMatrix::~CMatrix()// 析构函数
{<!-- -->
	cout&lt;&lt;"~CMatrix()" &lt;&lt;endl;
	if(m_pData!=NULL)
	{<!-- -->
		delete []m_pData; 
	}
}
CMatrix &amp; CMatrix::Set(int nIndex,double dVal)
{<!-- -->
	cout&lt;&lt;"Set(int,double)" &lt;&lt;endl;
	m_pData[nIndex]=dVal;
	return *this;  
} 

CMatrix &amp; CMatrix::Set(int nRow,int nCol,double dVal)
{<!-- -->
	cout&lt;&lt;"Set(int,int,double)" &lt;&lt;endl;
	m_pData[nRow*nCol+nCol]=dVal;
	return *this; 
} 
int CMatrix::GetDim()
{<!-- -->
	cout&lt;&lt;"GetDim()" &lt;&lt;endl;
	return m_nDim;
}

bool CMatrix::Read(string strPath)
{<!-- -->
	cout&lt;&lt;"Read(string)" &lt;&lt;endl;
	if(m_pData)
	{<!-- -->
		delete[] m_pData;
		m_pData=NULL;
		m_nRow=m_nCol=0; 
	}
	const char* p = strPath.data();
	ifstream in(p);
	if(in&gt;&gt;m_nRow&gt;&gt;m_nCol)
	{<!-- -->
		m_pData=new double[m_nRow*m_nCol];
		printf("m_nRow=%d m_nCol=%d\n",m_nRow,m_nCol);
		printf("m_nRow*m_nCol=%d\n",m_nRow*m_nCol);
		for(int i=0;i&lt;m_nRow*m_nCol;i++)
		{<!-- -->
			printf("i=%d\n",i);
			in&gt;&gt;m_pData[i];
/*			if(in&gt;&gt;m_pData[i])
			{
				printf("m_pData[%d]=%d",i,m_pData[i]);
				return false;
			}

*/
		}
		return true;
	}
	else
	{<!-- -->
		return false;
	}

}

bool CMatrix::Write(string strPath) const
{<!-- -->
	cout&lt;&lt;"Write(string) const" &lt;&lt;endl;
	const char* p = strPath.data();
	ofstream out(p);
	out&lt;&lt;m_nRow&lt;&lt;"\t"&lt;&lt;m_nCol&lt;&lt;"\n";
	for(int i=0;i&lt;m_nRow*m_nCol;i++)
		out&lt;&lt;m_pData[i]&lt;&lt;"\t";
	return true;
}
bool CMatrix::Create(int nRow,int nCol) 
{<!-- -->
	cout&lt;&lt;"Create(int,int)" &lt;&lt;endl;
	Release();
	m_nRow=nRow;
	m_nCol=nCol;
	m_pData=new double[nRow*nCol];
}
void CMatrix::Release()
{<!-- -->
	cout&lt;&lt;"Release()" &lt;&lt;endl;
	if(m_pData)
	{<!-- -->
		delete []m_pData;
		m_pData=NULL; 
	}
	m_nRow=m_nCol=0;
}
CMatrix &amp; CMatrix::operator=(const CMatrix &amp; mIn)
{<!-- -->
	cout&lt;&lt;"重载=" &lt;&lt;endl;
	Release();
	m_nRow=mIn.m_nRow;
	m_nCol=mIn.m_nCol;
	m_pData=new double[m_nRow*m_nCol];
	memcpy(m_pData,mIn.m_pData,sizeof(double)*m_nRow*m_nCol);
	return *this;
}
bool &amp; CMatrix::operator==(const CMatrix &amp;b)
{<!-- -->
	cout&lt;&lt;"重载==" &lt;&lt;endl;
	bool flag=true;
	if(m_nRow==b.m_nRow&amp;&amp;m_nCol==b.m_nCol)
	{<!-- -->
		for(int i=0;i&lt;m_nRow*m_nCol;i++)
		{<!-- -->
			if(m_pData[i]!=b.m_pData[i])
				flag=false;
					
		}
	}
	return flag;
}

CMatrix &amp; CMatrix:: operator+=(const CMatrix &amp;b)
{<!-- -->
	cout&lt;&lt;"重载+=" &lt;&lt;endl;
	if(m_nRow==b.m_nRow&amp;&amp;m_nCol==b.m_nCol)
	{<!-- -->
			
		for(int i=0;i&lt;m_nRow*m_nCol;i++)
		{<!-- -->
			m_pData[i]=m_pData[i]+b.m_pData[i];
		}
	}
	return *this;
}
/*
CMatrix &amp; CMatrix::operator+(const CMatrix &amp;a,const CMatrix &amp;b)
{
	CMatrix c;
	this-&gt;c = c;
	if(a.m_nRow==b.m_nRow&amp;&amp;a.m_nCol==b.m_nCol)
	{
		c.Create(a.m_nRow,a.m_nCol);
		for(int i=0;i&lt;a.m_nRow*a.m_nCol;i++)
		{
			c.m_pData=a.m_pData[i]+b.m_pData[i];
		}
	}
	
	//return c;
	return *this;
	//不能使用，除非是new一个新的，因为this默认是传进来的那个（只有1个） 
}
*/
double &amp; CMatrix::operator[](int nIndex){<!-- -->
	cout&lt;&lt;"重载下标操作符([]" &lt;&lt;endl;
	return m_pData[nIndex];
}
double &amp; CMatrix::operator()(int i,int j){<!-- -->
	cout&lt;&lt;"重载调用操作符()" &lt;&lt;endl;
	return m_pData[i*m_nRow+j];
}
CMatrix::operator double() const
{<!-- -->
	//不需要返回值，这个是隐式类型转换
	cout&lt;&lt;"重载double()" &lt;&lt;endl;
	double sum=0;
	for(int i=0;i&lt;m_nRow*m_nCol;i++)
	{<!-- -->
		sum+=m_pData[i];
	} 
	return sum;
}

```

### 3.使用类——mian.cpp

```
#include &lt;iostream&gt;
#include &lt;stdio.h&gt;
#include &lt;fstream&gt;
#include "cmatrix.h"
using namespace std;

int main() {<!-- -->
	
	CMatrix m;    				//创建对象（类的实例） 
	double d[10]={<!-- -->1,2,3,6};
	CMatrix m1(2,2,d);
	m1.Write("out.txt");		//通过 类对象 来调用 类成员函数（方法） 

	CMatrix m2;
	m2.Read("in.txt");
	m2.Write("out1.txt");
	cout&lt;&lt;m2&lt;&lt;endl;
	m2.Set(0,0,3);
	int getint=m2.Get(0,0);
	printf("getint=%d\n",getint);
	m2.Write("out2.txt");
	cout&lt;&lt;m2&lt;&lt;endl;
	
	CMatrix a;
	a.Read("in.txt");
	//CMatrix b(a);
	CMatrix b;
	b=a;
	bool flag=(a==b);
	cout&lt;&lt;"flag(a==b)="&lt;&lt;flag&lt;&lt;endl;
	bool flag2=(m2==b);
	cout&lt;&lt;"flag(m2==b)="&lt;&lt;flag2&lt;&lt;endl;
	cout&lt;&lt;"m2 "&lt;&lt;m2&lt;&lt;endl;
	cout&lt;&lt;"b "&lt;&lt;a&lt;&lt;endl;
	CMatrix c;
	c=a+b;
	cout&lt;&lt;"a "&lt;&lt;a&lt;&lt;endl;
	cout&lt;&lt;"b "&lt;&lt;b&lt;&lt;endl;
	a+=b; 
	cout&lt;&lt;"a+=b "&lt;&lt;a&lt;&lt;endl;
	
	cout&lt;&lt;"c=a+b "&lt;&lt;c&lt;&lt;endl;
	cout&lt;&lt;"c[0]"&lt;&lt;c[0]&lt;&lt;endl;
	cout&lt;&lt;"c(1,1)"&lt;&lt;c(1,1)&lt;&lt;endl;
	double sum=(double)(a);
	cout&lt;&lt;"sum="&lt;&lt;sum&lt;&lt;endl;
//	double sum=(double)a; //报错 

	return 0;
}

```

<img src="https://img-blog.csdnimg.cn/96e4137427094b1a80bdea28aeb512fb.png" alt="在这里插入图片描述">

### 结果

<img src="https://img-blog.csdnimg.cn/00f1ae9d905e42abb8eab98b05671f3d.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/257fd0f8527345ae82f0f0caf0dc5942.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e74b3f08b208475f972b977e444e5756.png" alt="在这里插入图片描述"> **输出：**

```
CMatrix(int,int,double)
Create(int,int)
Release()
Write(string) const
Read(string)
m_nRow=3 m_nCol=3
m_nRow*m_nCol=9
i=0
i=1
i=2
i=3
i=4
i=5
i=6
i=7
i=8
Write(string) const
重载&lt;&lt;
3       3       1       2       3       2       2       2       3       3       3
Set(int,int,double)
Get(int,int)
getint=3
Write(string) const
重载&lt;&lt;
3       3       3       2       3       2       2       2       3       3       3
Read(string)
m_nRow=3 m_nCol=3
m_nRow*m_nCol=9
i=0
i=1
i=2
i=3
i=4
i=5
i=6
i=7
i=8
重载=
Release()
重载==
flag(a==b)=1
重载==
flag(m2==b)=0
m2 重载&lt;&lt;
3       3       3       2       3       2       2       2       3       3       3
b 重载&lt;&lt;
3       3       1       2       3       2       2       2       3       3       3
重载+
Create(int,int)
Release()
重载=
Release()
~CMatrix()
a 重载&lt;&lt;
3       3       1       2       3       2       2       2       3       3       3
b 重载&lt;&lt;
3       3       1       2       3       2       2       2       3       3       3
重载+=
a+=b 重载&lt;&lt;
3       3       2       4       6       4       4       4       6       6       6
c=a+b 重载&lt;&lt;
3       3       2       4       6       4       4       4       6       6       6
重载下标操作符([]
c[0]2
重载调用操作符()
c(1,1)4
重载double()
sum=42
~CMatrix()
~CMatrix()
~CMatrix()
~CMatrix()
~CMatrix()
~CMatrix()

```
