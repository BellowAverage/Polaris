
--- 
title:  使用递归将十进制转换成任意进制（Number Conversion） 
tags: []
categories: [] 

---
### 关于递归

##### 什么是递归？

说白了，就是函数自己调用自己，然后被调用的函数继续调用自己，这将无限循环下去，除非代码中有终止调用链的的内容。

##### 解释一下递归的所经历的过程

递归需要有边界条件、递归前进段和递归返回段。当边界条件不满足时，递归前进；当边界条件满足时，递归返回。

###### 举个例子：

求解：**4！** <img src="https://img-blog.csdnimg.cn/20200302231100183.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzM0OTkxNg==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

```
#include&lt;stdio.h&gt;
int f(int num);
int main()
{<!-- -->
  int num=4;
  printf("%d\n",f(num)); 
   return 0;
}
int f(int num)
{<!-- -->
   if(num==0)
      return 1;
   return num*f(num-1);
}

```

### 通过递归将十进制转换成任意进制

#### 思路

首先我们知道十以上的进制有一个特点，从10开始均有大写字母表示，如十六进制（1,2,3,···9,A,B,C,D,E,F)，所以在程序中如何解决由字母表示数字成为我们面临的问题，这个问题解决后其实小于10的基数就好处理了，因为不会涉及到字母的问题。

```
int convert(int value,int radix)
{<!-- -->
   if(value/radix!=0)                                                  //边界条件
   convert(value/radix,radix);
   if(radix&gt;10)                                                        //判断基数
   {<!-- -->
      if(value%radix&gt;=10)
      {<!-- -->
         int temp=value%radix-10;
         char typeChange=(char)(temp+'A');
         printf("%c",typeChange);
      }
      else
      {<!-- -->
         printf("%d",value%radix );
      }
   }
   else
   {<!-- -->
      printf("%d",value%radix );
   }
   return 0;
}

```
