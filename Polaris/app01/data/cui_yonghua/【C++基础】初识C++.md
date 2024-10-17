
--- 
title:  【C++基础】初识C++ 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li>- <ul><li>- - - - - 


### 一. C++初识

#### 1.1 第一个C++程序

编写第一个C++程序，编写代码如下：

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	cout &lt;&lt; "Hello world" &lt;&lt; endl;

	return 0;
}

```

然后，**编译 &amp; 执行 C++ 程序**，下面是简单的步骤： 1、打开一个文本编辑器，添加上述代码。 2、保存文件为 hello.cpp。 3、打开命令提示符，进入到保存文件所在的目录。 4、键入 `g++ hello.cpp`，输入回车，编译代码。如果代码中没有错误，命令提示符会跳到下一行，并生成 <mark>a.out</mark> 可执行文件。 5、现在，键入 ’ a.out’ 来运行程序。 6、您可以看到屏幕上显示 ’ Hello World '。

#### 1.2 注释

**作用**：在代码中加一些说明和解释，方便自己或其他程序员程序员阅读代码

**两种格式**
<li>**单行注释**：`// 描述信息` 
  1. 通常放在一行代码的上方，或者一条语句的末尾，<mark>对该行代码说明</mark> </li><li>**多行注释**： `/* 描述信息 */` 
  1. 通常放在一段代码的上方，<mark>对该段代码做整体说明</mark> </li>- 通常放在一段代码的上方，<mark>对该段代码做整体说明</mark>
>  
 提示：编译器在编译代码时，会忽略注释的内容 


#### 1.3 变量

**作用**：给一段指定的内存空间起名，方便操作这段内存

**语法**：`数据类型 变量名 = 初始值;`

**示例：**

```
#include&lt;iostream&gt;
using namespace std;

int main() {<!-- -->

	//变量的定义
	//语法：数据类型  变量名 = 初始值

	int a = 10;

	cout &lt;&lt; "a = " &lt;&lt; a &lt;&lt; endl;

	return 0;
}

```

>  
 注意：C++在创建变量时，必须给变量一个初始值，否则会报错 


#### 1.4 常量

**作用**：用于记录程序中不可更改的数据

C++定义常量两种方式
<li> **#define** 宏常量： `#define 常量名 常量值` 
  1. <mark>通常在文件上方定义</mark>，表示一个常量 </li><li> **const**修饰的变量 `const 数据类型 常量名 = 常量值` 
  1. <mark>通常在变量定义前加关键字const</mark>，修饰该变量为常量，不可修改 </li>- <mark>通常在变量定义前加关键字const</mark>，修饰该变量为常量，不可修改
**示例：**

```
#include&lt;iostream&gt;
using namespace std;
//1、宏常量
#define day 7

int main() {<!-- -->

	cout &lt;&lt; "一周里总共有 " &lt;&lt; day &lt;&lt; " 天" &lt;&lt; endl;
	//day = 8;  //报错，宏常量不可以修改

	//2、const修饰变量
	const int month = 12;
	cout &lt;&lt; "一年里总共有 " &lt;&lt; month &lt;&lt; " 个月份" &lt;&lt; endl;
	//month = 24; //报错，常量是不可以修改的

	return 0;
}

```

#### 1.5 关键字

**作用：** 关键字是C++中预先保留的单词（标识符）
- **在定义变量或者常量时候，不要用关键字**
C++关键字如下：

|asm|do|if|return|typedef
|------
|auto|double|inline|short|typeid
|bool|dynamic_cast|int|signed|typename
|break|else|long|sizeof|union
|case|enum|mutable|static|unsigned
|catch|explicit|namespace|static_cast|using
|char|export|new|struct|virtual
|class|extern|operator|switch|void
|const|false|private|template|volatile
|const_cast|float|protected|this|wchar_t
|continue|for|public|throw|while
|default|friend|register|true|
|delete|goto|reinterpret_cast|try|

`提示：在给变量或者常量起名称时候，不要用C++得关键字，否则会产生歧义。`

#### 1.6 标识符命名规则

**作用**：C++规定给标识符（变量、常量）命名时，有一套自己的规则
- 标识符不能是关键字- 标识符只能由字母、数字、下划线组成- 第一个字符必须为字母或下划线- 标识符中字母区分大小写
>  
 建议：给标识符命名时，争取做到见名知意的效果，方便自己和他人的阅读 

