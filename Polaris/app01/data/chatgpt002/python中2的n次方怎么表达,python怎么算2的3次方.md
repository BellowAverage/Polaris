
--- 
title:  python中2的n次方怎么表达,python怎么算2的3次方 
tags: []
categories: [] 

---
大家好，给大家分享一下python中2的n次方怎么表达，很多人还不知道这一点。下面详细解释一下。现在让我们来看看！



<img alt="" height="292" src="https://img-blog.csdnimg.cn/img_convert/fc038f0177e360be5a89a0e13839fd1b.jpeg" width="500">

本篇文章给大家谈谈python中2的n次方输出结果为整数，以及python中2的n次方怎么表达，希望对各位有所帮助，不要忘了收藏本站喔。



<img alt="" height="292" src="https://img-blog.csdnimg.cn/img_convert/19c1e101db07ee3ec655c4c596858b72.jpeg" width="500">

题干

本题来自LeetCode Problem 50。其大意为给定 x （浮点数）和 n （整数），求 x 的 n 次幂。

解法

暴力解法

暴力解法……当然是直接拿 x 乘 n 次咯，注意如果 n 取负数的时候，要先对 x 求倒数，再乘以 -n 次。

class Solution:

def myPow(self, x: float, n: int) -&gt; float:

if n == 0:

return 1

if n &lt; 0:

return myPow(1 / x, -n)

ans = 1

for i in range(n):

ans *= x

return ans

但是很显然当 n 的绝对值很大的时候会有很恐怖的时间消耗，而且不必要。

快速幂算法

递归实现

由小学数学我们很容易得知，myPow(x, 2n) = myPow(x, n) * myPow(x, n)，因此我们对给定 n，只需计算其 n / 2 次幂，再将其相乘即可，注意如果 n 是奇数的话，例如 n = 5 时，先计算n // 2 = 2，向下取整，之后再计算myPow(x, 5) = myPow(x, 2) * myPow(x, 2) * x。这样就很容易地把时间复杂度降到了O(log n)级别。话不多说上代码：

class Solution:

def myPow(self, x: float, n: int) -&gt; float:

if n == 1:

return x

if n == 0:

return 1

if n &lt; 0:

return self.myPow(1/x, -n)

return self.myPow(x, n // 2) ** 2 if n % 2 == 0 else self.myPow(x, n // 2) ** 2 * x

迭代实现

LeetCode 官方还给出了一种快速幂的迭代实现，将空间复杂度从O(log n) 降到了 O(1)，思想也非常巧妙，供大家参考：

class Solution:

def myPow(self, x: float, n: int) -&gt; float:

def quickMul(N):

ans = 1.0

# 贡献的初始值为 x

x_contribute = x

# 在对 N 进行二进制拆分的同时计算答案

while N &gt; 0:

if N % 2 == 1:

# 如果 N 二进制表示的最低位为 1，那么需要计入贡献

ans *= x_contribute

# 将贡献不断地平方

x_contribute *= x_contribute

# 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可

N //= 2

return ans

return quickMul(n) if n &gt;= 0 else 1.0 / quickMul(-n)
