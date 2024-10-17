
--- 
title:  C语言课程设计，C语言学生管理系统源码含可执行文件 
tags: []
categories: [] 

---
一个基于 C 语言的学生管理系统，使用了并归排序，格式会自动调整对齐，对于某个非常长的条目也不会出现奇怪的显示格式，不需要连接数据库 完整代码下载地址： 运行截图： <img src="https://img-blog.csdnimg.cn/4a0e0715f5094bdfbf5cb85bc8af200f.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d071bd88b955420ca6c42707cbf54e95.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/bee95501219b446f9b4631a7bc800a07.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9ded9984feb04399940861c95e5f538b.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/605e7eca3dac4cfcb096b2502af0dd05.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/e554a16ab3a8487cadd2255275c59792.png#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/1fa434a0af3f42ee920e64135544352f.png#pic_center" alt="在这里插入图片描述">

```
#include &lt;stdlib.h&gt;

#include "InsertSort.h"
#include "MergeSort.h"

void Merge(DataType a[], int n, DataType swap[], int k)
{
	int m = 0;
	int u1, u2;
	int i, j;
	int l2;
	int l1 = 0;

	while (l1 + k &lt; n - 1)
	{
		l2 = l1 + k;
		u1 = l2 - 1;
		u2 = (l2 + k - 1 &lt;= n - 1) ? l2 + k - 1 : n - 1;

		for (i = l1, j = l2; i &lt;= u1 &amp;&amp; j &lt;= u2; m++)
		{
			if (a[i]._num &lt;= a[j]._num)
			{
				swap[m] = a[i];
				i++;
			}
			else
			{
				swap[m] = a[j];
				j++;
			}
		}

		while (i &lt; u1)
		{
			swap[m] = a[i];
			m++;
			i++;
		}
		while (j &lt;= u2)
		{
			swap[m] = a[j];
			m++;
			j++;
		}
		l1 = u2 + 1;
	}
	for (i = l1; i &lt; n; i++, m++) swap[m] = a[i];
}
void MergeSort(DataType a[], int n)
{
	int i, k = 1;
	DataType *swap;

	swap = (DataType*)malloc(sizeof(DataType)*n);
	/*for (int q = 0; q &lt; n; q++)
		swap[q]._name = (char*)malloc(sizeof(char) * 15);*/ //不需要
	while (k &lt; n)
	{
		Merge(a, n, swap, k);
		for (i = 0; i &lt; n; i++)
			a[i] = swap[i];
		k = 2 * k;
	}
	/*for (int q = 0; q &lt; n; q++)
		free(swap[q]._name);*/
	InsertSort(a, n);
	free(swap);
}

```

完整代码下载地址：
