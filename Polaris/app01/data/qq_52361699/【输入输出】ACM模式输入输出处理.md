
--- 
title:  【输入输出】ACM模式输入输出处理 
tags: []
categories: [] 

---
## 输入

### cin 

```
#include &lt;iostream&gt;

```

#### 批量输出

```
// 1 2 3 4 5
vector&lt;int&gt; nums(5);
for (int i = 0; i &lt; nums.size(); i++) {
	cin &gt;&gt; nums[i];
}
// 批量输出
for (auto it = nums.begin(); it != nums.end(); it++) {
	cout &lt;&lt; *it &lt;&lt; " ";
}

```

### getline()

读取一整行字符串（包括空格等字符），默认换行符结束。

两种用法：

 - &lt;string&gt;
 - &lt;istream&gt;

#### getline()

```
#include &lt;string&gt;

```

>  
 istream&amp; getline (istream&amp;  is, string&amp; str); istream&amp; getline (istream&amp;&amp; is, string&amp; str); istream&amp; getline (istream&amp;  is, string&amp; str, char delim); istream&amp; getline (istream&amp;&amp; is, string&amp; str, char delim);  


 - is：输入流，如cin
 - str：string，保存读取的字符串
 - delim：char，定义结束符，默认为 '\n'

```
string str;
getline(cin, str, '#'); // 以#作为结束符
```

#### cin.getline()

```
#include &lt;istream&gt;
```

>  
 istream&amp; getline (char* s, streamsize n ); istream&amp; getline (char* s, str

