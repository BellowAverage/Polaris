
--- 
title:  isdigit函数详解 
tags: []
categories: [] 

---
isdigit是计算机C(C++)语言中的一个函数，主要用于检查其参数是否为十进制数字字符。

函数定义：int isdigit(int c);

### 一、头文件

由于isdisit() 函数是属于C语言中的一个函数，因此头文件为

```
#include &lt;ctype.h&gt;

```

在C++中如下应用：

```
#include &lt;cctype&gt;

```

### 二、函数说明

检查参数 c 是否为阿拉伯数字0 到9。

### 三、返回值

若参数c为阿拉伯数字0~9，则返回非0值，否则返回0。

### 四、范例：

**（C语言）**

```
#include&lt;stdio.h&gt;
#include&lt;ctype.h&gt;

//判断一串字符中的阿拉伯数字，并输出 
int main(){<!-- -->
	char str[15] = "qaz521l5o2v1eq";
	printf("str字符串中的所有阿拉伯数字为："); 
	for(int i = 0; str[i] != '\0'; i++){<!-- -->
		if(isdigit(str[i])){<!-- -->
			printf("%c", str[i]);
		}
	}
	return 0;
} 

```

**（C++）**

```
#include&lt;iostream&gt;
#include&lt;cctype&gt;
#include&lt;string&gt;

using namespace std;

//判断一串字符中的数字，并输出 
int main(){<!-- -->
	string str = "qaz521l5o2v1eq";
	cout &lt;&lt; "str字符串中的所有阿拉伯数字为："; 
	for(int i = 0; i &lt; str.size(); i++){<!-- -->
		if(isdigit(str[i])){<!-- -->
			cout &lt;&lt; str[i];
		}
	}
	return 0;
} 

```
