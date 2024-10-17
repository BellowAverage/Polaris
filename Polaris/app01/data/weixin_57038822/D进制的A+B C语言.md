
--- 
title:  D进制的A+B C语言 
tags: []
categories: [] 

---
****D进制的A+B C语言****

描述

输入两个非负 10 进制整数A和B(≤230−1)，输出A+B的D(1&lt;D≤10)进制数。

输入 输入在一行中依次给出 3 个整数A、B和D。

输出 输出A+B的D进制数。

输入样例 1 ：

>  
 123 456 8 


输出样例 1：

>  
 1103 


输入样例 2：

>  
 输入样例 2 


输出样例 2：

>  
 634 


输入样例 3 ：

>  
 456 789 2 


输出样例 3：

>  
 10011011101 


来源：

>  
 https://pintia.cn/problem-sets/994805260223102976/problems/994805299301433344 


C语言代码如下：

```
#include&lt;stdio.h&gt;
int main(){<!-- -->
	int a,b,c,i;
	scanf("%d%d%d",&amp;a,&amp;b,&amp;c);
	int sum = a+b;
	int ans[31]={<!-- -->0};
	int num=0;
	do{<!-- -->
		ans[num++]=sum%c;
		sum /= c;
	}while(sum!=0);
	for(i=num-1;i&gt;=0;i--){<!-- -->
	printf("%d",ans[i]);
	}
	return 0;
}

```
