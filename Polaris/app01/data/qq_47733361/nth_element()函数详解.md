
--- 
title:  nth_element()函数详解 
tags: []
categories: [] 

---
>  
 在强大的STL库中存在一个神奇的函数，那就是nth_element，这个函数主要用来将数组元素中第k小的整数排出来并在数组中就位，随时调用，可谓十分实用。 


### 一、nth_element()函数的用法：

函数语句：nth_element(数组名,数组名+第k小元素,数组名+元素个数) 该函数仅排序第n个元素（从0开始索引），即将位置n（从0开始）的元素放在第n大的位置，处理完之后，默认排在它前面的元素都不比它大，排在它后面的元素都不比它小。

### 二、头文件：

在使用此函数时需要有如下头文件：

```
#include &lt;algorithm&gt;

```

### 三、测试代码：

```
#include&lt;iostream&gt;
#include&lt;algorithm&gt;

using namespace std;

int main(){<!-- -->
	int a[10] = {<!-- -->9, 8, 7, 6, 5, 4, 3, 2, 1, 10};
	int k = 2; //第k小的数
	cout &lt;&lt; "原数组：";
	for(int i = 0; i &lt; 10; i++)	cout &lt;&lt; a[i] &lt;&lt; " ";
	cout &lt;&lt; endl;
	sort(a, a + 10); 
	cout &lt;&lt; "由小到大排序后的数组：";
	for(int i = 0; i &lt; 10; i++) cout &lt;&lt; a[i] &lt;&lt; " ";
	cout &lt;&lt; endl;
	cout &lt;&lt; "第k小的数：";
	nth_element(a, a+k, a+10);
	cout &lt;&lt; a[k] &lt;&lt; endl;
	return 0; 
} 

```

<img src="https://img-blog.csdnimg.cn/2020111218413940.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述">
