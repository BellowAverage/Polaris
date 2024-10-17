
--- 
title:  新年值得练手的100道Python经典练手题，（附详细答案）建议收藏 
tags: []
categories: [] 

---
## 前言

近年来，Python在编程语言界里赚足了风头，无论是受欢迎程度，还是薪资待遇，都非常可观，相应的，Python岗位要求也越来越高，无论你是零基础还是老前辈，在Python面试中都不能轻视。 不打无准备之战，在平时我们就需要多积累，今天就给大家分享一份**100多道Python真题合集**，全是**经典题目，从容易到困难**，非常全面，，供大家参考学习。 题目答案一一对应，**代码齐全可复制**，不仅可当作练习使用，也可以当作面试参考，建议人手一份。

##### **程序001：数字组合**

题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析 遍历全部可能，把有重复的剃掉。

```

total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)

```

简便方法 用itertools中的permutations即可。

```

import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)

```

##### **程序002：“个税计算”**

题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析 分区间计算即可。

```

profit=int(input('Show me the money: '))
bonus=0
thresholds=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(len(thresholds)):
    if profit&lt;=thresholds[i]:
        bonus+=profit*rates[i]
        profit=0
        break
    else:
        bonus+=thresholds[i]*rates[i]
        profit-=thresholds[i]
bonus+=profit*rates[-1]
print(bonus)

```

思路是：最坏的结果是n的平方与(n+1)的平方刚好差168，由于是平方的关系，不可能存在比这更大的间隙。

至于判断是否是完全平方数，最简单的方法是：平方根的值小数为0即可。

结合起来：

```

n=0
while (n+1)**2-n*n&lt;=168:
    n+=1

for i in range((n+1)**2):
    if i**0.5==int(i**0.5) and (i+168)**0.5==int((i+168)**0.5):
        print(i-100) 

```
- **【数据类型】** 不运行程序，说出下方程序运行结果：
```

4.0 == 4
"4.0" == 4
bool("1")
bool("0")
str(32)
int(6.26)
float(32)
float("3.21")
int("434")
int("3.42")
bool(-1)
bool("")
bool(0)
"wrqq" &gt; "acd"
"ttt" == "ttt "
"sd"*3
"wer" + "2322"

```
- **【字符串】** 不用代码，口述下方代码执行结果
```

string="Python is good"

string[1:20]
string[20]
string[3:-4]
string[-10:-3]
string.lower()
string.replace("o","0")
string.startswith("python")
string.split()
len(string)
string[30]
string.replace("",") 

```
- **【简单算法】** 打印杨辉三角。给定一个正整数N，打印杨辉三角的前N行。杨辉三角形态如下：
```
    1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1


```

杨辉三角的每一行第一个和最后一个元素都是1；中间的元素，由上一行的两个元素相加得到；第N行的第index元素，是由第N-1行的第index-1元素和第index相加得到的。
- **【简单算法】** 已知两个列表
```

lst_1 = [1, 2, 3, 4]
lst_2 = ['a', 'b', 'c', 'd']

```

请写算法，将两个列表交叉相乘，生成如下的矩阵

```

['1a', '2a', '3a', '4a'],
['1b', '2b', '3b', '4b'],
['1c', '2c', '3c', '4c'],
['1d', '2d', '3d', '4d']

```
- **【简单算法】** 求三位数组合
这四个数字能组成多少个互不相同且无重复数字的三位数？请逐个输出

```
lst = [3, 6, 2, 7]

```
- **【排序】选择排序**
假设有一个序列，a[0] , a[1] , a[2]…a[n] ，现在对它进行排序。我们先从0这个位置找出最小值，然后将这个最小值与a[0] 交换，然后a[1]到a[n]就是我们接下来要排序的序列。

我们可以从1这个位置到n这个位置找出最小值，然后将这个最小值与a[1]交换，之后a[2]到a[n]就是我们接下来要排序的序列。每一次我们都从序列中找出一个最小值，然后把它与序列的第一个元素交换位置，这样下去，待排序的元素就会越来越少吗，直到最后一个

```
def select_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(min,len(lst)):
            # 寻找min 到len(lst)-1 这个范围内的最⼩小值
            if lst[min] &gt; lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
lst = [2,6,1,8,2,4,9]
select_sort(lst)
print lst

```
- **【中等难度算法】** 将下方给定的字符串中的每个单词逐个翻转。翻转后，空格不能减少，单词之间的空格数量不能发生变化。
```

输入: " the sky is  blue",
输出: "blue  is sky the "

```

如果只是简单的翻转字符串，就过于简单了，因此要求翻转每一个单词，单词还是原来的样子，但是单词所在的位置却发生了翻转，第一个单词变成了倒数第一个单词。字符串是不可变对象，不能直接在字符串上进行翻转，要借助列表（list）进行翻转

**-END-**

<mark>**读者福利：如果大家对Python感兴趣，这套python学习资料一定对你有用**</mark>

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以根据这些资料规划好学习计划和方向。 


<mark>包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习、Python量化交易等习教程。带你从零基础系统性的学好Python！</mark>

## 零基础Python学习资源介绍

① Python所有方向的<mark>学习路线图</mark>，清楚各个方向要学什么东西

② 600多节<mark>Python课程视频</mark>，涵盖必备基础、爬虫和数据分析

③ 100多个<mark>Python实战案例</mark>，含50个超大型项目详解，学习不再是只会理论

④ 20款主流手游迫解 <mark>爬虫手游逆行迫解教程包</mark>

⑤ <mark>爬虫与反爬虫攻防</mark>教程包，含15个大型网站迫解

⑥ <mark>爬虫APP逆向实战</mark>教程包，含45项绝密技术详解

⑦ 超<mark>300本Python电子好书</mark>，从入门到高阶应有尽有

⑧ 华为出品独家<mark>Python漫画教程</mark>，手机也能学习

⑨ 历年互联网企业<mark>Python面试真题</mark>,复习时非常方便

<img src="https://img-blog.csdnimg.cn/7c1055f9bb6e41af9262556bdf20e084.png#pic_center" alt="在这里插入图片描述">

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。<mark>**（全套教程文末领取哈）**</mark> <img src="https://img-blog.csdnimg.cn/9f969354b48f4e3ab0253e89203deca2.png#pic_center" alt="在这里插入图片描述">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。

<img src="https://img-blog.csdnimg.cn/6cf364e7eeb64b0da07021bce5a59ec6.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

## 资料领取

<mark>这份完整版的Python全套学习资料已为大家备好，朋友们如果需要可以微信扫描下方二维码添加，输入"领取资料" 可免费领取全套资料</mark>【<font color="#CC0033" size="3" face="微软雅黑">有什么需要协作的还可以随时联系我</font>】<mark>朋友圈也会不定时的更新最前言python知识。↓↓↓</mark><font color="red" size="3"> **或者**</font> 【】领取
