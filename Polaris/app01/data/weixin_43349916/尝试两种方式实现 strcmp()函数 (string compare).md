
--- 
title:  尝试两种方式实现 strcmp()函数 (string compare) 
tags: []
categories: [] 

---
### 关于strcmp() 函数

strcmp()是我们平时非常常见的一个string类中的库函数，用于比较两个字符串并根据比较结果返回整数。通常情况下，基本形式为strcmp(str1,str2)，若str1=str2，则返回零；若str1&lt;str2，则返回负数；若str1&gt;str2，则返回正数。

#### 比较规则

两个字符串自左向右逐个字符相比（按ASCII值大小相比较），直到出现不同的字符或遇’\0’为止。

###### #今天我将尝试使用两种方式来实现这个函数#

**注意传入的字符串均为const，我们不改变字符串只是作比较**

### 方式一：数组

```
int strcmp(const char* s1,const char* s2)
{<!-- -->
	int index=0;
	
	while(s1[index]==s2[index])
	{<!-- -->
		if (s1[index]=='\0')
		{<!-- -->
			return 0;
			break;
		}
		index++;
	
	}
	/*
		出现不匹配项
	*/
	int result= s1[index]-s2[index];
	/*if(result&gt;0)           //根据需求 调节返回值
	{
		return 1;
	}
	else
		return-1;*/
	return result;
}

```

### 方式二：指针

我们都知道所有的数组都是指针，只不过这个指针指的是数组第一个元素所在的地址。那么我们在遍历数组唯一需要做的就是让这个指针指向下一个元素就OK。 **但是我们如何让他指向下一个元素呐？** 我们会去使用让地址先自增，再去指向新的地址所储存的元素。

#### *p++来了

就p而言，我们可以知道他们的优先级相同，并且++和 * 都是自右向左结合的，那么在这个* p++中，便会先会对地址操作，然后再指向新的地址，所以说* p++等同于 * (p++)。

```
int mycmp(const char* s1,const char* s2)
{<!-- -->
	while(*s1==*s2)
	{<!-- -->
		if(!*s1)
		{<!-- -->
			return 0;
		}
		*s1++;
		*s2++;
	}
	return *s1-*s2;
}

```
