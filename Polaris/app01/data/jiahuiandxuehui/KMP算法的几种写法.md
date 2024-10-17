
--- 
title:  KMP算法的几种写法 
tags: []
categories: [] 

---


#### 目录标题
- - - - - 


## 简介

>  
 KMP算法是一种改进的字符串匹配算法，由D.E.Knuth，J.H.Morris和V.R.Pratt提出的，因此人们称它为克努特—莫里斯—普拉特操作（简称KMP算法）。KMP算法的核心是利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的。具体实现就是通过一个next()函数实现，函数本身包含了模式串的局部匹配信息。KMP算法的时间复杂度O(m+n) 


## 主串和字串和next数组都从零位置开始

```
#include&lt;stdio.h&gt;
#include&lt;string&gt;

int kmp(char* mainStr,char* subStr,const int* next) {<!-- -->
	int len1 = strlen(mainStr);
	int len2 = strlen(subStr);
	int i = 0, j = 0;
	while (i &lt; len1&amp;&amp;j&lt;len2) {<!-- -->//当珠串被遍历完或者字串被遍历完就结束也就也就意味着没匹配到或者匹配到了第一次出现的位置
		if (mainStr[i] == subStr[j]) {<!-- -->//当i和j位置相等往下走
			i++;
			j++;
		}
		else {<!-- -->//不相等的时候
			
			if (j == 0) {<!-- -->//当j以经在0上了说明主串i位置之前的字符都无法和字串匹配到只能让i下移
				i++;
			}
			else {<!-- -->//当j还没有为0说明主串i之前还可能存在着和字串可以匹配的位置
				j = next[j ];//由于next数组的性质我们选取要和主串i位置对比的下一个字串的j位置
			}

		}

	}
	return i-len2;//若是匹配成功返回在主串的位置
}

int main() {<!-- -->
	char mainstr[] = "abacbababdabaabca";
	char sub[] = "abaabc";
	int next[] = {<!-- -->0,0,0,1,1,2 };//求出next数组
	
	int ans = kmp(mainstr, sub, next);
	printf("子串在主串中的位置（从0开始）%d\n", ans);
	printf("验证：");
	for (int i = 0; i &lt; strlen(sub); ++i) {<!-- -->
		printf("%c",mainstr[ans+i]);
	}

	return 0;
}

```

## 主串和字串和next数组都从1位置开始

```
#include&lt;stdio.h&gt;
#include&lt;string&gt;

int kmp(char* mainStr, char* subStr, const int* next) {<!-- -->
	int len1 = strlen(mainStr);
	int len2 = strlen(subStr);
	int i = 1, j = 1;
	while (i &lt; len1&amp;&amp;j &lt; len2) {<!-- -->

		if (j == 0 || mainStr[i] == subStr[j]) {<!-- -->
			i++;
			j++;
		}
		else {<!-- -->
			j = next[j];

		}

	}
	return i - j+1;//若是匹配成功返回在主串的位置
}

int main() {<!-- -->
	char mainstr[] = "0abacbababdabaabca";
	char sub[] = "0abaabc";
	int next[] = {<!-- --> NULL,0,1,1,2,2,3 };//求出next数组

	int ans = kmp(mainstr, sub, next);
	printf("子串在主串中的位置（从1开始）%d\n", ans);
	printf("验证：");
	for (int i = 0; i &lt; strlen(sub)-1; ++i) {<!-- -->
		printf("%c", mainstr[ans + i]);
	}

	return 0;
}

```

## 重头戏计算next数组

因为目前都是默认从1开始的，我们求next也从一开始了

```
void getNext(char* subStr,int* next) {<!-- -->
	int i = 1, j = 0,len=strlen(subStr);//模拟串的前后缀i为后缀j为前缀
	next[1] = 0;//1位置默认为零
	while (i &lt; len) {<!-- -->//求前后缀的匹配问题又回到了kmp

		if (j == 0 || subStr[i] == subStr[j]) {<!-- -->
			i++;
			j++;
			next[i] = j;
		}
		else {<!-- -->
			j = next[j];
		}
	}

}

```

## 求nextval

在next的基础上加上

```

void getNextVal(char* subStr,int* next,int* nextval) {<!-- -->
	int len = strlen(subStr);
	nextval[1] = 0;
	for (int i = 2; i &lt; len; i++) {<!-- -->
		if (subStr[next[i]] == subStr[i]) {<!-- -->
			nextval[i] = nextval[next[i]];
		}
		else {<!-- -->
			nextval[i] = next[i];
		}
	}

}


```
