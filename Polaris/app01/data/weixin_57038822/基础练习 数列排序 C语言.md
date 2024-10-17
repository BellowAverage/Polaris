
--- 
title:  基础练习 数列排序 C语言 
tags: []
categories: [] 

---
****基础练习 数列排序 C语言****

描述：

给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1&lt;=n&lt;=200

输入：

输入描述: 　　第一行为一个整数n。 　　第二行包含n个整数，为待排序的数，每个整数的绝对值小于10000。

输入样例: 5 8 3 6 4 9

输出：

输出描述: 　　输出一行，按从小到大的顺序输出排序后的数列。 　　 输出样例: 3 4 6 8 9

提示：

>  
 HINT:时间限制：1.0s 内存限制：512.0MB 


来源：

>  
 蓝桥杯练习系统 ID: 52 原题链接: http://lx.lanqiao.cn/problem.page?gpid=T52 


实现代码如下：

```
#include&lt;stdio.h&gt;
int main()
{<!-- -->
	unsigned int n,i,j,t;
	scanf("%d",&amp;n);
	int P[n];
	for(i=0;i&lt;=n-1;i++)
	{<!-- -->
		scanf("%d",&amp;P[i]);
	}
	for(j=n;j&gt;=1;j--)
	{<!-- -->
		for(i=0;i&lt;j-1;i++)
		if(P[i]&gt;P[i+1])
		{<!-- -->
			t=P[i+1];
			P[i+1]=P[i];
			P[i]=t;
		}
	}
		for(i=0;i&lt;=n-1;i++)	
		{<!-- -->
		printf("%d",P[i]);
		printf(" ");
		}
	return 0;
}

```
