
--- 
title:  对于C++ string类的一些基本方法的重载 
tags: []
categories: [] 

---
## 对于C++ string类的一些基本方法的重载

### 一.简单描述

在C++等高级语言中已经对string这种数据类型及其相关方法进行了封装，给用户提供了更为方便的体验。但理解清楚string本身的运作方式及其相关方法极其重要，本人重载其中的几个方法，方便理解。

### 二.命名规范

**1、类的成员变量命名规范：** 以m_开头，p表示pointer指针，Str代表String字符串，如m_pStr指的便是存储字符串的指针，同理m_strLen便代表字符串长度。 **2、函数名命名规范：** 使用英文单词的缩写或全拼作为函数名与函数参数名，或借鉴c语言string库的函数名与函数参数名。 **3、函数内的局部变量命名规则：** 重要的有意义的字符串使用单词缩写命名，对于无意义的用于循环的变量，使用I,j,k等简单的字母命名。

### 三.函数的分布

<img src="https://img-blog.csdnimg.cn/20200110230040781.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzM0OTkxNg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

### 四.实现细节

### 1.string.h文件定义

本模块中最有亮点的是对成员变量（字符串地址和字符串长度）的封装，为之后的操作省去很多不必要的麻烦，方便之后对于字符串的操作。

```
#ifndef _STRING_H
#define _STRING_H

#include&lt;iostream&gt;

class string
{<!-- -->
public:
	//  构造函数
	string(const char * str = nullptr);
	// 析构函数
	~string();
	//  拷贝构造
	string(const string &amp;other);

public:
	// 重载 =
	void operator=(const string &amp; other);
	// 重载 &lt;&lt; 与 &gt;&gt;
	friend std::ostream &amp; operator&lt;&lt;(std::ostream &amp;out, string &amp;obj);
	friend std::istream &amp; operator &gt;&gt; (std::istream &amp;in, string &amp;obj);

public:
	//  编写一个方法，实现用c类型字符串s的赋值
	string &amp;assign(const char *s);
	// 重载以上方法，实现c类型字符串s开始的第n个字符的赋值。
	string &amp;assign(const char *s, int n);
	// 重载以上方法，实现将n个字符c赋值给当前字符串。
	string &amp;assign(int n, char c);
	// 实现把字符串s连接到当前字符串的结尾
	string &amp;operator+=(const string &amp;s);
	//实现把c类型字符串s连接到当前字符串结尾
	string &amp;append(const char *s);

public:
	//比较两个指定的字符串对象
	static int Compare(string strA, string strB);
	// 是否忽视大小写
	static int Compare(string strA, string strB, bool ignoreCase);

public:
	// 返回指定的字符串在此字符串中的第一个匹配项的索引，如果找到该字符，则为value从零开始的索引位置；如未找到，则返回 - 1。
	int Indexof(string value);
	// 返回从指定位置开始的匹配索引结果如未找到，则返回 - 1。
	int Indexof(string value, int startIndex);
	// ，返回从指定位置开始的匹配索引结果，并只检查指定数量的字符位，如果找到该字符，则为value从零开始的索引位置；如未找到，则返回-1。
	int Indexof(string value, int startIndex, int count);
	// 扩充 
	int Indexof(int endIndex, string value, int startIndex);
	// 替换
	string replace(string oldValue, string newValue);
	// 所有空白字符都去除
	string trim(string value);
	//重载以上方法返回去除指定的字符后的结果。
	string trim(string value, string trimString);
	// 从当前字符串中去除指定的前导匹配字符串，并返回去除后的结果。
	string trimStart(string value, string trimString);
	// 从当前字符串中去除指定的尾部匹配字符串，并返回去除后的结果。
	string trimEnd(string value, string trimString);
	// 返回当前字符串的长度
	int getLength(string value);
	// 重载以上方法，加入第二个参数(string insertString)，返回插入新的字符串后，当前字符串的长度
	int getLength(string value, string insertString);
	// 重载以上方法，加入第三个参数(string trimString)，返回插入新的字符串之后，去除掉指定字符串后的当前字符串长度。
	int getLength(string value, string insertString, string trimString);
	// 扩展
	int insertString(string value, int index);
	

public:
	int GetStringLength(const char* str);
	int GetStringLength();
	void strcpy(char *dest, const char* src);

private:
	char *m_pStr;                              //储存字符串
	int m_strLen;                              //储存字符串长度
};

#endif


```

### 2.string.cpp文件

代码量有点大，先列举几个有亮点的模块仅供赏玩。 **(1)重载运算符的操作：** 方便对字符串之间的操作，本程序重载了=（检查字符串地址是否相同）、&gt;&gt;、&lt;&lt;（输入输出串）、+=（连接两字符串）

```
//重载=
void string::operator=(const string &amp; other)
{<!-- -->
	int i = 0;
	if (other.m_pStr != m_pStr){<!-- -->
		delete[] m_pStr;

		m_strLen = other.m_strLen;
		m_pStr = new char[m_strLen + 1];
		strcpy(m_pStr, other.m_pStr);
		m_pStr[m_strLen] = '\0';
	}
}
//重载&lt;&lt;和&gt;&gt;
std::ostream &amp; operator&lt;&lt;(std::ostream &amp;out, string &amp;obj)
{<!-- -->
    out &lt;&lt; obj.m_pStr;
    return out;
}

std::istream &amp; operator&gt;&gt;(std::istream &amp;in, string &amp;obj)
{<!-- -->
	int i;
	char str[1025];
	char c;
	for (i = 0; i &lt; 1024; i++){<!-- -->
		std::cin.get(c);
		if (c == '\n'){<!-- -->
			break;
		}
		str[i] = c;
	}

	str[i] = '\0';
	obj = str;
    return in;
}
//重载+=连接到当前字符串的结尾
string&amp; string::operator+=(const string &amp;s)
{<!-- -->
	int i = 0;
	int len = s.m_strLen + this-&gt;m_strLen + 10;
	char *pStr = new char[len];
	memset(pStr, 0, len);
	strcpy(pStr, m_pStr);
	strcpy(pStr + m_strLen, s.m_pStr);

	*this = string(pStr);
	delete[] pStr;

	return *this;
}

```

**(2)忽略字符串字符大小进行比较：** 在对于忽略两字符串大小进行比较时，我选择了将全部字符转换成小写，在转换小写的过程中我的方法比较新颖，基于相同大小写字母ascii相差32，我直接进行对其进行操作得到全部为小写的字符串。

```
int string::Compare(string strA, string strB, bool ignoreCase)
{<!-- -->
	int i = 0;
	int len = 0;
	if (ignoreCase == false){<!-- -->
		return Compare(strA, strB);
	}
	// 化为小写
	len = strA.m_strLen &gt; strB.m_strLen ? strB.m_strLen : strA.m_strLen;
	for (i = 0; i &lt; len; i++){<!-- -->
		if ((strA.m_pStr[i] &gt; 'a') &amp;&amp; (strA.m_pStr[i] &lt; 'z')){<!-- -->
			strA.m_pStr[i] -= 32;
		}
		if ((strB.m_pStr[i] &gt; 'a') &amp;&amp; (strB.m_pStr[i] &lt; 'z')){<!-- -->
			strB.m_pStr[i] -= 32;
		}
	}
	if (strA.m_strLen &gt; len){<!-- -->
		for (i = len; i &lt; strA.m_strLen; i++){<!-- -->
			if ((strA.m_pStr[i] &gt; 'a') &amp;&amp; (strA.m_pStr[i] &lt; 'z')){<!-- -->
				strA.m_pStr[i] -= 32;
			}
		}
	}
	else if (strB.m_strLen &gt; len){<!-- -->
		for (i = len; i &lt; strB.m_strLen; i++){<!-- -->
			if ((strB.m_pStr[i] &gt; 'a') &amp;&amp; (strB.m_pStr[i] &lt; 'z')){<!-- -->
				strB.m_pStr[i] -= 32;
			}
		}
	}

	return Compare(strA, strB);
}

```

剩下代码量有点大，嘿嘿，大家悠着点看

```
#include "string.h"

#define DEFAULT_STRING_LENGTH 100

string::string(const char * str)
{<!-- -->
	int i = 0;

	if (str != nullptr){<!-- -->
		m_strLen = GetStringLength(str);
	}
	else{<!-- -->
		m_strLen = DEFAULT_STRING_LENGTH;
	}
	m_pStr = new char[m_strLen + 1];
	memset(m_pStr, 0, m_strLen + 1);

	if (str != nullptr){<!-- -->
		strcpy(m_pStr, str);
	}
}


string::~string()
{<!-- -->
	if (m_pStr != nullptr){<!-- -->
		delete[] m_pStr;
		m_pStr = nullptr;
	}
}

string::string(const string &amp;other)
{<!-- -->
	m_strLen = other.m_strLen;
	m_pStr = new char[other.m_strLen + 1];

	strcpy(m_pStr, other.m_pStr);
	m_pStr[m_strLen] = '\0';
}
//重载=
void string::operator=(const string &amp; other)
{<!-- -->
	int i = 0;
	if (other.m_pStr != m_pStr){<!-- -->
		delete[] m_pStr;

		m_strLen = other.m_strLen;
		m_pStr = new char[m_strLen + 1];
		strcpy(m_pStr, other.m_pStr);
		m_pStr[m_strLen] = '\0';
	}
}
//重载&lt;&lt;和&gt;&gt;
std::ostream &amp; operator&lt;&lt;(std::ostream &amp;out, string &amp;obj)
{<!-- -->
    out &lt;&lt; obj.m_pStr;
    return out;
}

std::istream &amp; operator&gt;&gt;(std::istream &amp;in, string &amp;obj)
{<!-- -->
	int i;
	char str[1025];
	char c;
	for (i = 0; i &lt; 1024; i++){<!-- -->
		std::cin.get(c);
		if (c == '\n'){<!-- -->
			break;
		}
		str[i] = c;
	}

	str[i] = '\0';
	obj = str;
    return in;
}
// 赋值
string&amp; string::assign(const char *s)
{<!-- -->
	*this = string(s);
	return *this;
}
//从第n个字符开始赋值
string&amp; string::assign(const char *s, int n)
{<!-- -->
	m_pStr[n - 1] = s[n - 1];
	return *this;
}

//实现把c类型字符串s连接到当前字符串结尾
string&amp; string::assign(int n, char c)
{<!-- -->
	int i = 0;
	delete[] m_pStr;            //释放字符串
	m_strLen = n;
	m_pStr = new char[m_strLen + 1];
	
	for (i = 0; i &lt; n; i++){<!-- -->
		m_pStr[i] = c;     
	}
	m_pStr[m_strLen] = '\0';
	
	return *this;
}

//重载+=连接到当前字符串的结尾
string&amp; string::operator+=(const string &amp;s)
{<!-- -->
	int i = 0;
	int len = s.m_strLen + this-&gt;m_strLen + 10;
	char *pStr = new char[len];
	memset(pStr, 0, len);
	strcpy(pStr, m_pStr);
	strcpy(pStr + m_strLen, s.m_pStr);

	*this = string(pStr);
	delete[] pStr;

	return *this;
}

//字符串s连接到当前字符串结尾
string &amp;string::append(const char *s)
{<!-- -->
	int i = 0;
	char *pStr = new char[this-&gt;GetStringLength(s) + this-&gt;m_strLen + 1];
	strcpy(pStr, m_pStr);
	strcpy(pStr + this-&gt;m_strLen, s);

	*this = string(pStr);
	delete[] pStr;

	return *this;
}
// 比较函数
int string::Compare(string strA, string strB)
{<!-- -->
	int flag = 1;
	int i = 0;
	while (1){<!-- -->
		if (strA.m_pStr[i] == 0){<!-- -->
			break;
		}
		else if (strB.m_pStr[i] == 0){<!-- -->
			break;
		}
		else if (strA.m_pStr[i] != strB.m_pStr[i]){<!-- -->
			break;
		}

		++i;
	}
	//逐个字符比对
	if (strA.m_pStr[i] &gt; strB.m_pStr[i]){<!-- -->
		return 1;
	}
	else if (strA.m_pStr[i] == strB.m_pStr[i]){<!-- -->
		return 0;
	}
	else{<!-- -->
		return -1;
	}
}

int string::Compare(string strA, string strB, bool ignoreCase)
{<!-- -->
	int i = 0;
	int len = 0;
	if (ignoreCase == false){<!-- -->
		return Compare(strA, strB);
	}
	// 化为小写
	len = strA.m_strLen &gt; strB.m_strLen ? strB.m_strLen : strA.m_strLen;
	for (i = 0; i &lt; len; i++){<!-- -->
		if ((strA.m_pStr[i] &gt; 'a') &amp;&amp; (strA.m_pStr[i] &lt; 'z')){<!-- -->
			strA.m_pStr[i] -= 32;
		}
		if ((strB.m_pStr[i] &gt; 'a') &amp;&amp; (strB.m_pStr[i] &lt; 'z')){<!-- -->
			strB.m_pStr[i] -= 32;
		}
	}
	if (strA.m_strLen &gt; len){<!-- -->
		for (i = len; i &lt; strA.m_strLen; i++){<!-- -->
			if ((strA.m_pStr[i] &gt; 'a') &amp;&amp; (strA.m_pStr[i] &lt; 'z')){<!-- -->
				strA.m_pStr[i] -= 32;
			}
		}
	}
	else if (strB.m_strLen &gt; len){<!-- -->
		for (i = len; i &lt; strB.m_strLen; i++){<!-- -->
			if ((strB.m_pStr[i] &gt; 'a') &amp;&amp; (strB.m_pStr[i] &lt; 'z')){<!-- -->
				strB.m_pStr[i] -= 32;
			}
		}
	}

	return Compare(strA, strB);
}

int string::Indexof(string value)
{<!-- -->
	int i = 0;
	int j = 0;
	int length = m_strLen - value.m_strLen + 1;
	for (i = 0; i &lt; length; i++)
	{<!-- -->
		for (j = 0; j &lt; value.m_strLen; j++){<!-- -->
			if (m_pStr[i + j] != value.m_pStr[j]){<!-- -->
				break;
			}
		}
		if (j == value.m_strLen){<!-- -->
			return i;
		}
	}
	return -1;
}

int string::Indexof(string value, int startIndex)
{<!-- -->
	int i = 0;
	int j = 0;
	int length = m_strLen - value.m_strLen;
	for (i = startIndex; i &lt; length; i++)
	{<!-- -->
		for (j = 0; j &lt; value.m_strLen; j++){<!-- -->
			if (m_pStr[i + j] != value.m_pStr[j]){<!-- -->
				break;
			}
		}
		if (j == value.m_strLen &amp;&amp; value.m_pStr[j - 1] == m_pStr[i + j - 1]) {<!-- -->
			return i;
		}
	}
	return -1;
}

int string::Indexof(string value, int startIndex, int count)
{<!-- -->
	int i = 0;
	int j = 0;
	int length = m_strLen - value.m_strLen + 1;
	if (value.m_strLen &lt; count){<!-- -->
		throw "count &gt; value.length";
	}

	for (i = startIndex; i &lt; length; i++)
	{<!-- -->
		for (j = 0; j &lt; count; j++){<!-- -->
			if (m_pStr[i + j] != value.m_pStr[j]){<!-- -->
				break;
			}
		}
		if (j == count){<!-- -->
			return i;
		}
	}
	return -1;
}


int string::Indexof(int endIndex, string value, int startIndex)
{<!-- -->
	int i = 0;
	int j = 0;
	if (m_strLen &lt; endIndex){<!-- -->
		throw "count &gt; value.length";
	}

	for (i = startIndex; i &lt; endIndex; i++)
	{<!-- -->
		for (j = 0; j &lt; value.m_strLen; j++){<!-- -->
			if (m_pStr[i + j] != value.m_pStr[j]){<!-- -->
				break;
			}
		}
		if (j == value.m_strLen){<!-- -->
			return i;
		}
	}
	return -1;
}
//字符串替换
string string::replace(string oldValue, string newValue)
{<!-- -->
	int index = 0;
	int j = 0, i = 0;
	int k = 0;
	int temp = 0;
	int l = newValue.m_strLen - oldValue.m_strLen;
	char *pStr = new char[m_strLen + l + 10];
	memset(pStr, 0, m_strLen + l + 10);

	index = Indexof(oldValue);
	if (index == -1){<!-- -->                //防止翻车
		return *this;
	}
	while (index != -1 &amp;&amp; k &lt; m_strLen){<!-- -->
		for (i = 0; i &lt; index - temp; i++){<!-- -->
			pStr[j ++] = m_pStr[k++];
		}
		k += oldValue.m_strLen;
		for (i = 0; i &lt; newValue.m_strLen; i++){<!-- -->
			pStr[j++] = newValue.m_pStr[i];
		}
		temp = index + oldValue.m_strLen;
		index = Indexof(oldValue, index + 1);
	}
	
	while (m_pStr[k] != 0){<!-- -->
		pStr[j++] = m_pStr[k++];
	}
	pStr[j] = '\0';
	string rStr(pStr);
	delete[] pStr;

	return rStr;
}

string string::trim(string value)
{<!-- -->
	int i = 0;
	int begin, end;                        //确定字符串的起点终点位置
	string s = value;
	int knum = 0;
	char *pStr = new char[s.m_strLen + 1];
	memset(pStr, 0, s.m_strLen + 1);
	while (s.m_pStr[i++] != ' ' &amp;&amp; s.m_pStr[i++] != '\0');       
	begin = i - 1;

	i = value.m_strLen - 1;
	while (s.m_pStr[i--] == ' ');
	end = i + 1;

	for (i = begin; i &lt; end; i++){<!-- -->
		pStr[i - begin] = m_pStr[i];
	}
	pStr[i - begin] = '\0';
	string rStr(pStr);
	delete[] pStr;

	return rStr;
}

string string::trim(string value, string trimString)
{<!-- -->
	int i = 0, j = 0, k = 0;
	int temp = 0;
	int index = value.Indexof(trimString);       //获取trimString位置
	if (index == -1){<!-- -->
		return value;
	}
	char* pStr = new char[value.m_strLen + 1];
	memset(pStr, 0, value.m_strLen + 1);

	while (index != -1){<!-- -->
		for (i = temp; i &lt; index; i++){<!-- -->
			pStr[k] = value.m_pStr[i];
			++k;
		}
		temp = index + 1;
		index = value.Indexof(trimString, temp);
	}
	for (i = temp; i &lt; value.m_strLen; i++){<!-- -->
		pStr[k] = value.m_pStr[i];
		++k;
	}
	pStr[k] = 0;
	string rStr(pStr);
	delete[] pStr;

	return rStr;             
}
//前导匹配字符串替换
string string::trimStart(string value, string trimString)
{<!-- -->
	int i = 0, j = 0;
	int start = value.Indexof(trimString);
	if (start != 0){<!-- -->
		return value;
	}
	char* pStr = new char[value.m_strLen + 1];
	memset(pStr, 0, value.m_strLen + 1);
	while (i &lt; start){<!-- -->
		pStr[j] = value.m_pStr[i];
		++i;
		++j;
	}
	i += trimString.m_strLen;
	while (i &lt; value.m_strLen){<!-- -->
		pStr[j] = value.m_pStr[i];
		++i;
		++j;
	}
	string rStr(pStr);
	delete[] pStr;

	return rStr;
}

string string::trimEnd(string value, string trimString)
{<!-- -->
	int i = 0, j = 0;
	int index = 0;
	int end = -1;
	index = value.Indexof(trimString);
	while (index != -1){<!-- -->
		end = index;
		index = value.Indexof(trimString, index + 1);
	}
	if (end == -1){<!-- -->
		return value;
	}
	char* pStr = new char[value.m_strLen + 1];
	memset(pStr, 0, value.m_strLen + 1);
	while (i &lt; end){<!-- -->
		pStr[j] = value.m_pStr[i];
		++i;
		++j;
	}
	i += trimString.m_strLen;
	while (i &lt; value.m_strLen){<!-- -->
		pStr[j] = value.m_pStr[i];
		++i;
		++j;
	}
	string rStr(pStr);
	delete[] pStr;

	return rStr;
}
// 返回当前字符串的长度
int string::getLength(string value)
{<!-- -->
	return value.m_strLen;
}

int string::getLength(string value, string insertString)
{<!-- -->
	return value.m_strLen + insertString.m_strLen;
}

int string::getLength(string value, string insertString, string trimString)
{<!-- -->
	return value.m_strLen + insertString.m_strLen - trimString.m_strLen;
}

int string::GetStringLength(const char* str){<!-- -->
	int i = 0;
	while (str[i++] != 0);

	return i - 1;
}
//插入字符串
int string::insertString(string value, int index)
{<!-- -->
	int i = 0;
	int j = 0;
	char *pStr = new char[m_strLen + value.m_strLen + 1];
	if (m_strLen &lt; index){<!-- -->                         //判断目标位置和原字符串的长度
		return -1;
	}
	while (i &lt; index){<!-- -->
		pStr[i] = m_pStr[i];
		++i;
	}
	for (j = 0; j  &lt; value.m_strLen; j ++){<!-- -->
		pStr[j + i] = value.m_pStr[j];
	}
	while (i &lt; m_strLen){<!-- -->
		pStr[i + j] = m_pStr[i];
		++i;
	}
	pStr[i + j] = 0;
	*this = pStr;

	return index;
}

int string::GetStringLength(){<!-- -->
	return m_strLen;
}

void string::strcpy(char *dest, const char* src)
{<!-- -->
	int i = 0;
	while (src[i] != '\0'){<!-- -->
		dest[i] = src[i];                //拷贝字符串
		++i;
	}
}

```

### 3、 测试用例main函数

3.1 编写控制台程序，调用string类对象的方法，实现以下的运算结果： 3.1.1. 对比"Hello World"和"HELLO WORLD"并返回结果 3.1.2. 对比"Hello World"和"HELLO WORLD"，忽略大小写后返回结果 3.1.3. 获取"China stocks extend rally on positive policy outlook"的长度 3.1.4. 在上述字符串后面加上"Chinese shares remained in positive territory for the second-consecutive day on Wednesday following the government’s fresh fiscal stimulus measures"并获取新字符串的长度。 3.1.5. 将上述新字符串中的"o"去掉并获取长度。 3.1.6. 查询"China"和"Chinese"在上述字符串中的索引结果。 3.1.7. 查询"China"和"Chinese"在上述字符串中索引40开始的结果。 3.1.8. 查询"day"在上述字符串中索引35开始到索引60的结果。 3.1.9. 将该字符串中的"positive"全部替换为"negative"并获取字符串长度。 3.1.10. 将字符串" CCCentral bank defends measures taken to regulate forex markettt “中的空格全部去除并获取字符串长度。 3.1.11. 将字符串中多余的C和t去掉，变为"Central bank defends measures taken to regulate forex market”。 3.2编写一个控制台程序，并扩充string类，通过调用string类对象实现以下功能： 编写一个文本信息程序 3.2.1. 能够输入英文文本，并显示该文本去除空格后的长度，如果输入为空或者空格，则提示用户需要输入文本。 3.2.2. 能够显示该文本中某一单词的索引位置，并能对其进行替换。 3.2.3. 能够在文本任意位置插入或者删除特定单词。 **代码如下：**

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include "string.h"

int main(int argc, char* argv[])
{<!-- -->
	string s1("Hello World");  
	string s2("HELLO WORLD");
	string s3("China stocks extend rally on positive policy outlook");
	string s4;

	//对比"Hello World"和"HELLO WORLD"并返回结果
	if (1 == string::Compare(s1, s2)){<!-- -->
		printf("s1 &gt; s2, success\n");
	}
	else{<!-- -->
		printf(" error\n");
	}
	//对比"Hello World"和"HELLO WORLD"，忽略大小写后返回结果
	if (string::Compare(s1, s2, true) == 0){<!-- -->
		printf("s1 == s2, success\n");
	}else{<!-- -->
		printf("s1 &lt; s2,error\n");
	}
	//获取"China stocks extend rally on positive policy outlook"的长度
	std::cout &lt;&lt; "s3长度为： " &lt;&lt; s3.getLength(s3) &lt;&lt; std::endl;
	//在上述字符串后面加上"Chinese shares remained in positive territory for the second-consecutive day on Wednesday following the government's fresh fiscal stimulus measures"并获取新字符串的长度。
	s3 += "Chinese shares remained in positive territory for the second-consecutive day on Wednesday following the government's fresh fiscal stimulus measures";
	std::cout &lt;&lt; "新的s3长度为： " &lt;&lt; s3.getLength(s3) &lt;&lt; std::endl;
	//将上述新字符串中的"o"去掉并获取长度。
	s4 = s3;
	s4 = s4.trim(s3, "o"); 
	std::cout &lt;&lt; "新的s4长度为： " &lt;&lt; s4.getLength(s4) &lt;&lt; std::endl;
	std::cout &lt;&lt; s4 &lt;&lt; std::endl;
	//查询"China"和"Chinese"在上述字符串中的索引结果。
	printf("China index is %d, begin index is 0\n", s3.Indexof("China"));
	printf("China index is %d, begin index is 0\n", s3.Indexof("Chinese"));
	//查询"China"和"Chinese"在上述字符串中索引40开始的结果。
	printf("China index is %d, begin index is 40\n", s3.Indexof("China", 40));
	printf("China index is %d, begin index is 40\n", s3.Indexof("Chinese", 40));
	//查询"day"在上述字符串中索引35开始到索引60的结果。
	printf("day index is %d, begin index is 35\n", s3.Indexof(60, "day", 35));
	//将该字符串中的"positive"全部替换为"negative"并获取字符串长度。
	s3 = s3.replace("positive", "negative");
	std::cout &lt;&lt; s3 &lt;&lt; std::endl;
	//将字符串"  CCCentral bank defends measures taken to regulate forex markettt  "中的空格全部去除并获取字符串长度。
	string s5("  CCCentral bank defends measures taken to regulate forex markettt  ");
	s5 = s5.trim(s5, " ");
	std::cout &lt;&lt; std::endl &lt;&lt; s5 &lt;&lt; std::endl &lt;&lt; s5.GetStringLength() &lt;&lt; std::endl;
	//将字符串中多余的C和t去掉，变为"Central bank defends measures taken to regulate forex market"。
	string s6("  CCCentral bank defends measures taken to regulate forex markettt  ");
	s6 = s6.trimStart(s6, "  CC");
	s6 = s6.trimEnd(s6, "tt  ");
	//编写一个控制台程序，并扩充string类，通过调用string类对象实现以下功能：
	//编写一个文本信息程序
	//能够输入英文文本，并显示该文本去除空格后的长度，如果输入为空或者空格，则提示用户需要输入文本。
	string str;
	string fStr;
	string nStr;
	std::cout &lt;&lt; std::endl &lt;&lt; "please input english text：" &lt;&lt; std::endl;
	std::cin &gt;&gt; str;
	printf("character number is %d\n", (str.trim(str, " ")).GetStringLength());
	std::cout &lt;&lt;"you input english text : " &lt;&lt; str &lt;&lt; std::endl;
	//能够显示该文本中某一单词的索引位置，并能对其进行替换。
	std::cout &lt;&lt; "please input need find text: ";
	std::cin &gt;&gt; fStr;
	int len = str.Indexof(fStr);
	std::cout &lt;&lt; "you find string index : " &lt;&lt; len &lt;&lt; std::endl;
	if (-1 != len){<!-- -->
		std::cout &lt;&lt; "please input new text: ";
		std::cin &gt;&gt; nStr;
		str = str.replace(fStr, nStr);
	}
	std::cout &lt;&lt; "you english text : " &lt;&lt; str &lt;&lt; std::endl;
	//能够在文本任意位置插入或者删除特定单词。
	str.insertString("Bullshit ！", 0);
	std::cout &lt;&lt; "you english text : " &lt;&lt; str &lt;&lt; std::endl;

	system("pause");
	return 0;
}


```
