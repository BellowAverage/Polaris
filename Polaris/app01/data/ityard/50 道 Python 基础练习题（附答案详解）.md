
--- 
title:  50 道 Python 基础练习题（附答案详解） 
tags: []
categories: [] 

---
>  
  作者：Amo Xiang 
  https://blog.csdn.net/xw1680/article/details/103546693 
 

## 1.两个变量的交换

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 23:30
# @Author  : 我就是任性-Amo
# @FileName: 1.两个变量的交换.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 需求: 完成两个变量值的交换
# 如:a=20,b=30--&gt;a=30,b=20
a = 20
b = 30
print(f"变量交换之前a的值为{a},b的值为{b}")
# 第一种交换变量的方式: 使用第三方临时变量
temp = a  # 先将a值赋值给一个第三变量 存储a的值
a = b  # 将b的值赋值给a
b = temp  # 将temp的值赋值给b temp存储的值其实为原来变量a存储的值
print(f"变量交换之后a的值为{a},b的值为{b}")


# 第二种交换变量的方式: 使用python特有的方式
a, b = b, a
print(f"变量交换之后a的值为{a},b的值为{b}")


# 第三种交换变量的方式: 使用算术运算符的方式
# 总的来说: 无论a,b如何交换 他们的和都是不变的
a = a + b
b = a - b
a = a - b
print(f"变量交换之后a的值为{a},b的值为{b}")


# 第四种交换变量的方式: 使用位运算符的方式
a = a ^ b
b = a ^ b
a = a ^ b
print(f"变量交换之后a的值为{a},b的值为{b}")


# 在java中还可以使用下面这种方式:
# int a = 10;
# int b = 20;
# System.out.println("交换变量前a的值为:" + a + ",b的值为:" + b);
# a = (a + b) - (b = a);
# System.out.println("交换变量后a的值为:" + a + ",b的值为:" + b);

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1SGxkTzRaTUduc3NITU5mcFJlaWJDSE1JU3ZCQlN3aWIyTHNtbDF6VTMzbTZzSmZoMTlPZGI2N2cvNjQw?x-oss-process=image/format,png">

## 2.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 23:47
# @Author  : 我就是任性-Amo
# @FileName: 2.数字1-4组成不同且不重复的三位数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
count = 0  # 计数器
for i in range(1, 5):  # 百位的数字可以是1,2,3,4
    for j in range(1, 5):
        for k in range(1, 5):
            # 百位 十位 个位的数字不重复
            if i != j and i != k and j != k:
                count += 1  # 符合条件计数器就+1
                print(i * 100 + j * 10 + k)  # 打印符合条件的三位数


print(count)  # 打印符合条件的三位数的个数

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1aWFIS2NlTHQyRUtaSUxjTkNmZnZXSmVqTHlMZkdmVFlRemhZbmlidWxnSmpxR0piZm01T09pY1RRLzY0MA?x-oss-process=image/format,png">

## 3.求应发奖金数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 00:04
# @Author  : 我就是任性-Amo
# @FileName: 3.求应发奖金数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 需求: 企业发放的奖金根据利润提成。从键盘输入当月利润I，求应发放奖金总数？
# 利润(i)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%
# 高于100万元时，超过100万元的部分按1%提成


profit = [1000000, 600000, 400000, 200000, 100000, 0]  # 利润
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]  # 利率
bonus = 0  # 奖金
# 键盘录入当月的利润i
i = int(input("&gt;&gt;&gt;:"))


for j in range(6):
    if i &gt; profit[j]:
        bonus += (i - profit[j]) * rate[j]  # 减去基本数 再计算奖金
        i = profit[j]  # 下次计算的利润值
print(bonus)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1ak1IUUh1M2dBaWJ2d2tTTDJpYWxpYUZlV2Y0Sk56T1RpY3hON2d1NlVva2lidlJkWWE4NDUxQWdTZncvNjQw?x-oss-process=image/format,png">

## 4.输入某年某月某日，判断这一天是这一年的第几天？

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 00:39
# @Author  : 我就是任性-Amo
# @FileName: 4.判断用户输入的是这一年的第几天.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 需求:输入某年某月某日，判断这一天是这一年的第几天？
# 思路:以5月20日为例，应该先把前四个月的加起来，然后再加上20天即本年的第几天
# 特殊情况就是: 如果年份为闰年且输入月份大于2时需考虑多加一天


year = int(input("年:"))
month = int(input("月:"))
day = int(input("日:"))
sum_day = 0  # 第几天
leap_year = 0  # 闰年


# 使用元组定义天数
# 如果输入的月份是1月份，则直接计算day即可
# 如果输入的月份是2月份，则要先计算出1月份的天数，即为31天
# 以此类推
# 1  2   3   4   5    6    7    8    9    10   11   12
# 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# 根据输入的月份，计算出前几个月的天数
if 0 &lt; month &lt;= 12:
    sum_day = months[month - 1]
else:
    print("输入的月份有误")
# 判断是否为闰年:
# 1.能被400整除 或者是 2.能被4整除并且不能被100整除
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    # 如果是闰年 则将leap_year变为1
    leap_year = 1


# 判断如果是闰年并且输入的月份大于2则在总的天数上加1
if leap_year == 1 and month &gt; 2:
    sum_day += day + 1
else:
    sum_day += day


print(f"it is the {sum_day}th day.")  # 打印

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1ckdZSDFQVWVqSmNFM1FiV21VdTl5Rk9pYzlvSnM4R25DbE1ZdnhRREJVRFVzWTlVOWM3c0VuZy82NDA?x-oss-process=image/format,png">

## 5.输入三个整数x,y,z，请把这三个数由小到大输出

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 01:06
# @Author  : 我就是任性-Amo
# @FileName: 5.输入三个整数，由小到大输出.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。


# 1.录入数据
x = int(input("&gt;&gt;&gt;:"))
y = int(input("&gt;&gt;&gt;:"))
z = int(input("&gt;&gt;&gt;:"))


# 2.使用列表存储数据并进行排序
num_list = [x, y, z]
num_list.sort()
print(num_list)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1NzNLenRVVU9pYXFKUHJlZVR2c1hOSjNKM2ljVmxYMExmS0ZXMkp5OHVjWWlhV0V1aFNNTHR4M2VnLzY0MA?x-oss-process=image/format,png">

## 6.斐波那契数列

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 01:33
# @Author  : 我就是任性-Amo
# @FileName: 6.斐波那契数列.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目:斐波那契数列
# 程序分析: 斐波那契数列(Fibonacci sequence)，又称黄金分割数列，指的是这样一个数列: 
# 1 1 2 3 5 8 13 21 34 55....




# 第一种方式:使用函数
def fibonacci1(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    print(f"斐波那契数列第{n}项的值为:{a}")




fibonacci1(3)  # 2




# 第二种方式:使用递归
def fibonacci2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)




print(fibonacci2(10))  # 3




# 第三种方式:输出指定个数的斐波那契数列
def fibonacci3(n):
    fibs = [1, 1]
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])  # 列表的最后两个数字相加
    return fibs




print(fibonacci3(10))




# 第四种方式: 使用生成器的方式实现
def fibonacci4(n):
    a = 0
    b = 1
    for i in range(0, n):
        a, b = b, a + b
        yield a
        print("amo~")




f = fibonacci4(4)
print(f)  # &lt;generator object fibonacci4 at 0x101cc63d0&gt;
print(next(f))  # 相当于去调用内置方法__next__ --&gt;1
print(f.__next__())  # 1
print(f.__next__())  # 2
print(f.__next__())  # 3

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1bUxoVDRlTjJXMHJ1MmlidnN5RDVUM3hOWUhUTTBJbTZ5ME1YcEZjNFFaY2haaWEzaFBEeTYxQ0EvNjQw?x-oss-process=image/format,png">

## 7. 将一个列表的数据复制到另一个列表中

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 02:15
# @Author  : 我就是任性-Amo
# @FileName: 7.将一个列表的数据复制到另一个列表中.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




list1 = [1, 2, 3, 4, 5]
print(list1)
# 1.直接使用列表的copy方法
new_list1 = list1.copy()
print(new_list1)
# 2.使用列表的切片
new_list2 = list1[:]
print(new_list2)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1VEVSTldBVUFseVJlaHQzYnV0aWM0aWJNbnp4NlRDUWZsYWlhY3ZiaWF2RU9rODljRkc1bWw2eVY5US82NDA?x-oss-process=image/format,png">

## 8.输出九九乘法表

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 02:20
# @Author  : 我就是任性-Amo
# @FileName: 8.输出 9*9 乘法口诀表.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 分析: 九九乘法表的每一个小的单元类似为: 1 * 1 = 1
# print("1 * 1 = 1")  # 只是里面的1随着行数在不停的变化 而等号后面的结果根据前面的数字动态生成
# print("2 * 1 = 2", end="\t")
# print("2 * 2 = 4")
# print("3 * 1 = 3", end="\t")
# print("3 * 2 = 6", end="\t")
# print("3 * 3 = 9")


# 综上: 发现规律第一个数字从1变化到9 第二个数字最多变化到和第一个数字相等 最后的数字为前两个数字的积


for i in range(1, 10):  # 第一个数字的变化范围
    for j in range(1, i + 1):  # 第二个数字变化的范围
        print(f"{i} * {j} = {i * j}", end="\t")
    # 循环完成之后需要进行换行
    print()

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1aGFBaWNodUFrR1JhYkNHdXVyVk9haWI4TkIwcEE0QnZqTVNzcnZGZGpPT1BoS09lOXJxTUxkSVEvNjQw?x-oss-process=image/format,png">

## 9.判断101-200之间有多少个素数，并输出所有素数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 10:32
# @Author  : 我就是任性-Amo
# @FileName: 9.判断101-200之间有多少个素数，并输出所有素数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目: 判断101-200之间有多少个素数，并输出所有素数。
# 分析:
# 1.数据变化的范围是从101-200 所以需要使用循环
# 2.素数: 只能被1和本身整除的数 所以需要一个变量从1变到本身
# 3.判断: 如果有一个非1和本身的数被整除 则跳出循环 判断下一个数字
# 如果循环完成，都只有1和本身能被整除 说明符合条件 计数器+1


# 定义一个变量为计数器
count = 0
# 第一种方式: 使用while循环实现
i = 101
while i &lt;= 200:
    j = 2
    # 其实这里的话是可以进行优化的 只需要判断数字的一半次数就可以了
    # 因为数字就是等于两个数的乘积 判断了前一个数 后一个数肯定就不用判断了
    # 数字的乘积就是一个小的数字*大的数字 减少循环的次数
    # while j &lt; i:
    while j &lt; i / 2:
        if i % j == 0:
            break
        j += 1
    else:
        count += 1
        print(i)
    i += 1
print(f"The total is {count}")
count = 0
# 第二种方式: 使用for循环改写
for i in range(101, 201):
    # for j in range(2, i):
    for j in range(2, int(i / 2)):  # 优化循环次数
        if i % j == 0:
            break
    else:
        count += 1
        print(i)
print(f"The total is {count}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1bmlhd2ljc0VmM0pCeTJzVGlhc09ZU3o2aWJTZ2dkMEFzRVlpYm5reGx5NFVxRU5DWER6R0hBaEk0dlEvNjQw?x-oss-process=image/format,png">

## 10.打印水仙花数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 10:54
# @Author  : 我就是任性-Amo
# @FileName: 10.打印水仙花数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
# 程序分析:利用for循环控制100-999个数，每个数分解出个位，十位，百位
# 核心: 就是如何获取到每个位上的数字
# 例子: 12345
# 个位: 12345 % 10
# 十位: 12345 // 10 % 10
# 百位: 12345 // 100 % 10
# 千位: 12345 // 1000 % 10
# 万位: 12345 // 10000


# 1.三位数的范围为:100~999 所以需要使用循环
for i in range(100, 1000):
    # 2.根据水仙花数的概念去判断
    ge_wei = i % 10
    shi_wei = i // 10 % 10
    bai_wei = i // 100
    if i == (ge_wei ** 3 + shi_wei ** 3 + bai_wei ** 3):
        print(i)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1WE9HOGVvdWFDanhseTJSN1VpY2VLWXQxa2FJeExTa1VZcGlhcVhvQ1Y1d1JkMVN6cVU2YnJVd1EvNjQw?x-oss-process=image/format,png">

## 11.将一个正整数分解质因数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 11:07
# @Author  : 我就是任性-Amo
# @FileName: 11.将一个正整数分解质因数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 将一个正整数分解质因数。例如:输入90,打印出90=2*3*3*5。
# 程序分析:对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成:
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n&lt;&gt;k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步


# 第一种方式实现: 使用循环
# while True:  # 可以不停的进行录入数据 进行分解质因数
#     num = int(input("&gt;&gt;&gt;:"))
#     print(f"{num}=", end="")
#     while num &gt; 1:  # 如果商小于等于1 则没有必要再进行循环
#         for j in range(2, num + 1):
#             if num % j == 0:
#                 num = int(num / j)
#                 if num == 1:
#                     print(f"{j}", end="")
#                 else:
#                     print(f"{j}*", end="")
#                 break  # 如果有一个满足条件能被整除 这里一定要跳出循环 从2开始再次进行判断
#     print()  # 换行




# 第二种方式实现: 使用递归
def dec_prime_factor(num):
    # 递归终止条件
    if num == 1:
        return []
    else:
        for i in range(2, num + 1):
            # divmod()函数: 返回的是一个元组
            # 元组第一个元素为商，第二个元素为余数
            # merchant: 商 remainder: 余数
            merchant, remainder = divmod(num, i)
            if remainder == 0:
                # 列表的合并 将几个列表中的元素整合到一个列表中
                return [i] + dec_prime_factor(merchant)




while True:
    number = int(input("&gt;&gt;&gt;:"))
    print(f"{number}=", end="")
    prime_list = dec_prime_factor(number)
    # 这里一定要先是用map函数将列表中的每一个数字转换成字符串类型 才能使用join去拼接
    prime_list_str = "*".join(map(str, prime_list))
    print(prime_list_str)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1b0RCWDZRVHplM00zZkZMbGhUaWFxUE5reFFpYldqTEVOVHdyRk5vaWNIT3BtdDRrRFVObVhQTVBnLzY0MA?x-oss-process=image/format,png">

## 12.条件运算符练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:05
# @Author  : 我就是任性-Amo
# @FileName: 12.条件运算符练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 利用条件运算符的嵌套来完成此题:
# 学习成绩&gt;=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示


while True:
    score = int(input("&gt;&gt;&gt;:"))
    # 值1 if 条件表达式 else 值2
    # 条件表达式成立返回值1，否则返回值2
    score_grade = 'A' if score &gt;= 90 else 'B' if 60 &lt;= score &lt;= 89 else 'C'
    print(score_grade)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1OGh0TkoxbUVqM1dCd3BFY05MOUxnODFmc0JZWlgyRkdZS0pMVzZncGhrM3AyT3RmaWJjWDRGUS82NDA?x-oss-process=image/format,png">

## 13.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:18
# @Author  : 我就是任性-Amo
# @FileName: 13.统计字符个数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import re


s = input("请输入一个字符串:").strip()
letters = 0
space = 0
digit = 0
other = 0
# 1.方式1使用for循环 while循环也一样
for i in s:
    if i.isalpha():  # 判断是否是字母
        letters += 1
    elif i.isspace():  # 判断是否是空白字符
        space += 1
    elif i.isdigit():  # 判断是否是数字
        digit += 1
    else:
        other += 1


print(f'char = {letters},space = {space},digit = {digit},others = {other}')


# 2.使用正则表达式
letters = len("".join(re.findall(r"[a-zA-Z]", s)))  # 匹配字母
space = len("".join(re.findall(r"\s+", s)))  # 匹配空白字符
digit = len("".join(re.findall(r"\d+", s)))  # 匹配数字
# 匹配非字母 数字 下划线 此时空白字符也会被匹配到 所以先要将空白字符移除
other_list = re.findall(r"\W", s)
for i in other_list:
    if i.isspace:
        other_list.remove(i)
other = len("".join(other_list))
print(f'char = {letters},space = {space},digit = {digit},others = {other}')

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1SVVSUmlid214TEVlbEVQSEtnTDNicEVsek5MZUVtcFhtT0VpY2FHTTBpYk1YZXZvM0RwbHJKR2tnLzY0MA?x-oss-process=image/format,png">

## 14.求s=a+aa+aaa+aaaa+aa…a的值

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:46
# @Author  : 我就是任性-Amo
# @FileName: 14.求s=a+aa+aaa+aaaa+aa...a的值.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
# 24690


# 1.输入几个数相加以及要相加的数字
num = input("请输入数字:")
count = int(input("请输入相加的个数:"))
get_sum = 0  # 统计和
str_list = []
for i in range(1, count + 1):
    # 将每个元素存入到列表中 用于后面的结果拼接
    str_list.append(str(num * i))
    # 累加
    get_sum += int(num * i)


# 拼接:24690=2+22+222+2222+22222
print(f"{get_sum}={'+'.join(str_list)}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1dzlGeXNWMDcxT1J4b2RLaWJacm9DaWFTYUcxWURWREhRR1lmNVlQZlluTzU0Z0ZwblJXRlpybUEvNjQw?x-oss-process=image/format,png">

## 15.编程找出1000以内的所有完数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:48
# @Author  : 我就是任性-Amo
# @FileName: 15.求完全数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目:一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
for i in range(1, 1000):
    num_list = []
    for k in range(1, i):
        if i % k == 0:
            num_list.append(k)
    if sum(num_list) == i:
        str1 = "+".join(map(str, num_list))
        print(f"{i}={str1}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1c0pZZVI5cWxlNnVKc3pnc2xmMndKNm9iVXZXWDF5eVlIUk5xZlk2VzhCVmlhdFN5UWJNZzJkQS82NDA?x-oss-process=image/format,png">

## 16.自由落体

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:50
# @Author  : 我就是任性-Amo
# @FileName: 16.自由落体练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 一球从100米高度自由落下，每次落地后反跳回原高度的一半
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
tour = []
height = []
hei = 100  # 起始高度
tim = 10  # 次数
for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2(弹到最高点再落下)
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)


print(f"总高度: tour = {sum(tour)}")
print(f"第10次反弹高度: height = {height[-1]}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1WnN0Z2dTaWFycnRSSkcyUWlhZEJJOFRMd05Mb2NBRGRVeVl1TFg1MHdPTFFnaWEwclN3UUlRUHNBLzY0MA?x-oss-process=image/format,png">

## 17.猴子吃桃问题

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:51
# @Author  : 我就是任性-Amo
# @FileName: 17.猴子吃桃.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 猴子吃桃问题:猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，
# 又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


peach = 1  # 定义第10天的桃子数
# 第九天的桃子数=(第十天的桃子数+1)*2
for i in range(10, 1, -1):
    peach = (peach + 1) * 2
    print(f"第{i - 1}天的桃子数量为: {peach}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1WXpCblVsUGFGaWNDZmdna0IyRW1JZVVOd1F0dXlEZmp2QkJXTTdrdXBpYTRqajVnblFDRElsV3cvNjQw?x-oss-process=image/format,png">

## 18.打印菱形

分析：如下图所示<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1dHZzMENaQU9oYktraWIzQnppYVdKblhseU9qeFBoWHFLRnZibXhFcWRETUVCT1FhN1VDaEtNYncvNjQw?x-oss-process=image/format,png">

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:53
# @Author  : 我就是任性-Amo
# @FileName: 18.打印菱形.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 打印菱形
# 简单理解可以理解为一个正等腰三角形和倒等腰三角形组成
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# 1.打印上三角形
for i in range(1, 11, 2):
    print(" " * int((9 - i) // 2) + "*" * i)


# 2.打印下三角形
for j in range(7, 0, -2):
    print(" " * int((9 - j) // 2) + "*" * j)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1SFRBTE01SEk3bnlxOWljclRuQWQ2TkMzbElQcFZVRHhINWJhdG9TbVR1bDRJbmRlZm9mRnNJUS82NDA?x-oss-process=image/format,png">

## 19.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:54
# @Author  : 我就是任性-Amo
# @FileName: 20.求1+2!+3!+...+20!的和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


from functools import reduce


# 题目: 求1+2!+3!+...+20!的和
# 第一种方式: 使用循环
num = int(input("请输入num:"))
get_sum = 0  # 统计和
cheng_ji = 1
for j in range(1, num + 1):
    cheng_ji *= j
    get_sum += cheng_ji
print(f"1+2!+3!+...+{num}!={get_sum}")  # 拼接字符串可以优化


# 第二种方式: 使用高阶函数map
L = range(1, num + 1)




# 定义一个求一个数的阶乘的函数
def operate(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r




s = sum(map(operate, L))
print(f"1+2!+3!+...+{num}!={s}")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1ZmNYNTcwZkUwVmNpYUdHdVhMSXdpYTFqVkliUzJIWGUyQ0JGVmlhem0yTU51a0lrNFJlYzUyU2JBLzY0MA?x-oss-process=image/format,png">

## 21.利用递归方法求5!

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 12:55
# @Author  : 我就是任性-Amo
# @FileName: 21.递归求5的阶乘.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 利用递归方法求5!
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)




print(fact(5))

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1UEw5S2hMcUNzMEw2TldJZVBzbDZmaWFpYm4yRVlSN29SaWNhMnk3SHhJT3pUb3NtZ0JBeWNxZURRLzY0MA?x-oss-process=image/format,png">

## 22.判断一个数是否是回文数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/15 23:48
# @Author  : 我就是任性-Amo
# @FileName: 22.判断一个数字是否是回文数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目: 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
# 思路1: 获取到各个位上的数字 然后按照回文数的概念进行比较
num1 = int(input("&gt;&gt;&gt;:"))
ge_wei = num1 % 10
shi_wei = num1 // 10 % 10
qian_wei = num1 // 1000 % 10
wan_wei = num1 // 10000
if ge_wei == wan_wei and shi_wei == qian_wei:
    print(f"{num1}是回文数")
else:
    print(f"{num1}不是回文数")
# 思路2: 逆序后的数字与原来的数字比较
num2 = input("&gt;&gt;&gt;:")
new_num2 = num2[::-1]
if num2 == new_num2:
    print(f"{num2}是回文数")
else:
    print(f"{num2}不是回文数")
# 思路3: 通过字符串的操作判断个位与万位相同，十位与千位相同
num3 = input("&gt;&gt;&gt;:")
flag = True  # 用来判断是否为回文数
for i in range(int(len(num3) / 2)):
    if num3[i] != num3[-i - 1]:
        flag = False
        break
if flag:
    print(f"{num3}是回文数")
else:
    print(f"{num3}不是回文数")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1VXQzWlh2NE5QY3BxZ2pyNEx5aWNONm93dlNON2p4dVVNNkJIYkVXaWFEY2lhWVpDbUhCbFl6UThRLzY0MA?x-oss-process=image/format,png">

## 23.两个矩阵相加

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 00:11
# @Author  : 我就是任性-Amo
# @FileName: 23.求两个矩阵的和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目:两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
# 程序分析:创建一个新的3行3列的矩阵，使用for迭代并取出X和Y矩阵中对应位置的值，相加后放到新矩阵的对应位置中
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]


Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]


result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]  # 初始化结果


for i in range(len(X)):  # 迭代三次 拿到每一个列表
    for j in range(len(X[0])):  # 拿到列表中的元素
        result[i][j] = X[i][j] + Y[i][j]


for i in result:
    print(i)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1Y0JiWng3RFZzUzBNSVZMMDdseWlhN2ljUmFLZzR5QXpvanhnUDl5dTB4SmxJTDFpY1JDaWFMcE15US82NDA?x-oss-process=image/format,png">

## 24.统计1-100的和

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 00:19
# @Author  : 我就是任性-Amo
# @FileName: 24.统计1-100的和.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 题目:统计1到100 之和。
get_sum = 0
for i in range(1, 101):
    get_sum += i


print("1-100的和为: %d" % get_sum)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1TXhlREZoSUIyUHdVTDMzV3Z1alB0dlZ3SVZjSTZoanNHd1JyTTgyTmo2dWVRU25HbjRkRFB3LzY0MA?x-oss-process=image/format,png">

## 25.三级菜单

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1MlUxdndWYURXc0hIM2liQXlxVGljc3JoVnlPSW54Mk5TNmw0SUpCM0RTaFNBeUh6WXYyS2h5ZHcvNjQw?x-oss-process=image/format,png">

```
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 09:17
# @Author  : 我就是任性-Amo
# @FileName: 02_three_level_menu.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 初始化数据
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


# 使用死循环保持程序可以不停地进行录入 然后根据指定的条件退出循环
current_level = menu  # 当前菜单层
layer_list = []  # 存储之前的菜单层 列表有序
while True:
    for city in current_level:
        print(city)
    choice = input("&gt;&gt;:").strip()  # 去除空白字符
    if choice in current_level:  # 判断选择城市是否在字典中
        layer_list.append(current_level)  # 使用列表存储上层菜单
        current_level = current_level[choice]  # 当前菜单更改为下层菜单
    elif choice == "b":  # 用户输入的为b的时候 表示回退上一层
        if current_level == menu:  # 判断是否是顶层
            print("reach top level")
            continue
        else:
            current_level = layer_list.pop()  # 回退
    elif choice == "q":
        exit("bye~")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1TXFaTFBjY2ViZFF3R2NSVFV2bWliR2xqcGtKTDBVaWNBaWNZWHZmdUpReXJleHdaZHFWaG5taWMzdy82NDA?x-oss-process=image/format,png">

## 26.双色球

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1dmNXdmh1S2pPOVpWajVDdllpYlR5ZzhTV0o4SnVzR3NHeFJ5Y29sVG5SSlhSNVRQMFJnVnJDdy82NDA?x-oss-process=image/format,png">

```
"""
作业：双色球选购
1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
2 确保用户不能重复选择，不能超出范围
3 用户输入有误时有相应的错误提示
4 最后展示用户选择的双色球的号码
"""
# 没有卡输入的内容为空时的情况
print("Welcome to 小猿圈 lottery station")


red_ball_list = []  # 用于存储选中的红球号
blue_ball_list = []  # 用于存储选中的蓝球号
i = 1  # 提示用户输入红球号时候带编号 [1] [2]
j = 1  # 提示用户输入蓝球号时候带编号 [1] [2]


# 用户一直在选 所以采用死循环
while True:
    # 判断红球号是否已经有效选择6次 如果是则开始选篮球号
    if len(red_ball_list) == 6:
        # 篮球号选择有效的2次 则退出循环
        if len(blue_ball_list) == 2:
            break


        blue_ball_str = input("\033[34m["+str(j)+"]select blue ball:"+"\033[0m")
        blue_ball_num = 0  # 初始化值
        # 判断是否输入的内容是否为空或者是输入的是字母
        if blue_ball_str.isdigit():
            blue_ball_num = int(blue_ball_str)
            if 1 &lt;= blue_ball_num &lt;= 16:
                if blue_ball_num not in blue_ball_list:
                    blue_ball_list.append(blue_ball_num)
                    j += 1
                else:
                    print(f"number {blue_ball_num} is already exist in blue ball list")
            else:
                print("only can select n between 1-16")
        else:
            print("only can input num")
    else:
        red_ball_str = input("\033[31m[" + str(i) + "]select red ball" + "\033[0m:")
        if red_ball_str.isdigit():
            red_ball_num = int(red_ball_str)
            if 1 &lt;= red_ball_num &lt;= 32:
                if red_ball_num not in red_ball_list:
                    red_ball_list.append(red_ball_num)
                    i += 1
                else:
                    print(f"number {red_ball_num} is already exist in red ball list")
            else:
                print("only can select n between 1-32")
        else:
            print("only can input num")
print()
print()
print("Red ball:", red_ball_list)
print("Blue ball:", blue_ball_list)
print("Good Luck.")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1d0xBakU4QzJrUjFheVFrUkkzSlF0dllGc2liZWNnTTBhS0xzempZVkdPWGJMaWJTaWJPT2F1aGR3LzY0MA?x-oss-process=image/format,png">

## 27.股票查询接口

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1YTF4U3RsZm04aWJraGNFZWc3dkxhNFNpY0Y3TFBSMnp2TWtLZzdEaWFWY1d0ZDh1b25pYTRNanpSdy82NDA?x-oss-process=image/format,png">

```
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 15:52
# @Author  : 我就是任性-Amo
# @FileName: 03-stock_info_query.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import os


# TODO 1.读取文件 判断文件是否存在 存在则读取 判断文件内容是否为空
if os.path.exists("stock_data.txt"):
    with open("stock_data.txt", "r") as file:
        stock_data = file.readlines()


    # TODO 2.如果读取的数据不为空 则继续进行后续操作
    while stock_data:
        query_info = input("股票查询接口&gt;&gt;:")
        if query_info.count("&lt;") == 1 or query_info.count("&gt;") == 1:
            # TODO 2.1 用户录入数据时录入符号
            symbol = "&gt;" if query_info.find("&lt;") == -1 else "&lt;"  # 指定用户录入时的符号
            name, num_str1 = query_info.split(symbol)  # 按照用户录入的符号进行切割 得到要查找的比较类型以及数字
            if stock_data[0].strip().find(name) != -1:  # 判断
                index = stock_data[0].strip().split(",").index(name)  # 得到类型在列表出现的位置
                print(stock_data[0].strip().split(","))  # 展示
                total_list = []
                for i in range(1, len(stock_data)):
                    temp_list = stock_data[i].strip().split(",")
                    # 根据类型在列表中出现的位置查找对应的其对应的数据
                    num_str2 = temp_list[index].replace("%", "") if temp_list[index].find("%") != -1 else temp_list[
                        index]
                    # 判断表达式 符合条件的往总列表中添加
                    if eval(str(float(num_str2) &gt; float(num_str1))) if symbol == "&gt;" else eval(str(
                            float(num_str2) &lt; float(num_str1))):
                        total_list.append(temp_list)
                for i in total_list:
                    print(i)
                print(f"找到{len(total_list)}条")
        else:
            # TODO 2.2 用户录入数据时没有符号的情况
            name_list = [stock.strip().split(",") for stock in stock_data if
                         stock.strip().split(",")[2].find(query_info) != -1]
            # 展示
            for name in name_list:
                print(name)
            print(f"找到{len(name_list)}条")

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1RFlOZ09sQ0pmZTZPaWFlajV5aWFCbXdNaGVIODU1cWNEVjBsMUlwUU9mSnhKdzFwRlB4SDQ0dkEvNjQw?x-oss-process=image/format,png">

## 28.员工信息管理

```
# -*- coding: utf-8 -*-
# @Time    : 2019/11/16 00:17
# @Author  : 我就是任性-Amo
# @FileName: 04-staffsystem.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import os
import re


filename = "staff_table.txt"  # 定义保存员工信息的文件名
condition_list = ["staff_id", "name", "age", "phone", "dept", "enroll_date"]




def menu():
    # 输出菜单
    print('''
    ╔———————员工信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 添加员工信息                             │
    │   2 删除员工信息                             │
    │   3 修改员工信息                             │
    │   4 查找员工信息                             │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字或↑↓方向键选择菜单          │
    ╚———————————————————————╝
    ''')




def main():
    flag = True  # 控制是否退出系统
    while flag:
        menu()  # 显示菜单
        option = input("请选择&gt;&gt;:")  # 用户选择功能
        # regexp.sub(): 将字符串中的数字提取出来 如果用户输入中含有非数字 则替换成''
        option_str = re.sub('\D', '', option)  # 提取数字
        if option_str in ['0', '1', '2', '3', '4']:
            option_int = int(option_str)
            if option_int == 0:
                flag = False
                print("您已退出员工信息管理系统!!!")
            elif option_int == 1:
                add()  # 添加员工信息
            elif option_int == 2:
                delete()  # 删除员工信息
            elif option_int == 3:
                update()  # 修改员工信息
            elif option_int == 4:
                search()  # 查找员工信息
                # pass




def search():
    flag = True
    while flag:
        operator_list = ["&gt;", "=", "like"]  # 定义三种操作符
        input_info = input("&gt;&gt;&gt;:")  # 用户输入
        operator = [operator for operator in operator_list if operator in input_info][0]  # 获取用户输入的操作符
        d_index = input_info.index("d")  # 查找到第一个d的位置
        from_index = input_info.index("from")  # 查找到from的位置
        where_index = input_info.index("where")  # 查找到where的位置
        operator_index = input_info.index(operator)  # 查找到对应的操作符位置
        find_info = input_info[d_index + 2:from_index - 1]  # 查找的信息 是所有的员工信息 还是员工信息中具体的某一个
        condition_type = input_info[where_index + 6:operator_index - 1]  # 查找条件
        condition_value = input_info[operator_index + len(operator) + 1:]  # 查找条件的值
        if condition_value.find("\"") != -1:
            condition_value = condition_value.replace("\"", "")
        if os.path.exists(filename):
            with open(filename, "r") as file:
                staff_list = file.readlines()
                if staff_list:
                    index = condition_list.index(condition_type)
                    # 不同的操作符进行不同的判断
                    if operator == "&gt;":
                        input_age = int(condition_value)
                        for staff in staff_list:
                            if int(staff.split(",")[index]) &gt; input_age:
                                show(staff, find_info)
                    elif operator == "=":
                        for staff in staff_list:
                            if staff.split(",")[index] == condition_value:
                                show(staff, find_info)
                    elif operator == "like":
                        for staff in staff_list:
                            if staff.split(",")[index].startswith(condition_value):
                                show(staff, find_info)
                    query_info = input("是否继续查找(y/n):")
                    if query_info == "y":
                        flag = True
                    elif query_info == "n":
                        flag = False




def add():
    """
    根据用户输入的信息，添加进入到文本文件中
    :return:
    """
    staff_id = 1  # 员工编号
    staff_list = []
    tel_num = []  # 用来存储文件中所有的电话号码
    tel_num_input = []  # 判断此次用户输入的电话号码是否有重复
    flag = True
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()
        if len(content) &gt; 1:
            staff_id = int(content[-1].strip().split(",")[0]) + 1
            for staff in content[1:]:
                tel_num.append(staff.split(",")[3])
    while flag:
        staff_id_str = str(staff_id) + ","
        staff_info = input("&gt;&gt;&gt;:").strip()
        staff_info = staff_info[staff_info.index("e") + 2:]
        tel_phone = staff_info.split(",")[2]
        # 判断输入的电话号码是否在文件中存在或者是在之前已经输入存储过
        if tel_phone in tel_num_input or tel_phone in tel_num:
            print("你输入的电话号码重复...")
            continue
        tel_num_input.append(tel_phone)
        write_info = "\n" + staff_id_str + staff_info
        staff_list.append(write_info)
        tips = input("是否继续添加(y/n):")
        if tips == "y":
            flag = True
            staff_id += 1
        elif tips == "n":
            flag = False
    save(staff_list)
    print("员工信息添加成功!!!")




def save(staff_list):
    # 1.打开文件
    file = open(filename, "a")
    # 2.写入
    for staff in staff_list:
        file.write(staff)
    # 3.关闭文件
    file.close()




def delete():
    """
    根据用户输入id删除文件中对应的用户信息
    :return:
    """
    flag = True  # 控制是否结束循环
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, "r") as file:
            staff_list = file.readlines()
    while flag:
        search_str = input("&gt;&gt;&gt;:").strip()
        # 查找id
        staff_id = search_str[search_str.index("=") + 2:]
        for staff in staff_list:
            temp = staff.strip().split(",")[0]
            # 如果用户输入id与文件中读取到的id相同 则从大列表中进行移除
            if staff_id == temp:
                staff_list.remove(staff)
            else:
                pass
        # 判断是否继续删除
        tips = input("是否继续删除(y/n):")
        if tips == "y":
            flag = True
        elif tips == "n":
            flag = False
    # 向文件写入内容的时候 将最后一个元素的换行去除
    staff_list[-1] = staff_list[-1].strip()
    with open(filename, "w") as file:
        file.writelines(staff_list)
    print("删除成功!!!")




def update():
    """更新员工信息函数"""
    flag = True  # 控制是否退出更新
    while flag:
        input_info = input("&gt;&gt;&gt;:")  # 用户输入
        # 例子: update staff_table set dept="Market" where dept = "IT"
        set_index = input_info.index("set")
        den_index = input_info.index("=")  # 获取set和第一个=号的索引
        where_index = input_info.index("where")
        rden_index = input_info.rindex("=")  # 获取where和最后一个=的位置
        update_type = input_info[set_index + 4: den_index]  # 定位修改员工的哪个具体信息
        update_value = input_info[den_index + 1:where_index - 1]  # 定位修改员工的值
        condition_type = input_info[where_index + 6:rden_index - 1]  # 定位根据哪个员工的信息去判断
        condition_value = input_info[rden_index + 2:]  # 符合条件的值
        if "\"" in update_type:  # 去掉引号 否则会匹配不成功
            update_type = update_type.replace("\"", "")
        if "\"" in update_value:
            update_value = update_value.replace("\"", "")
        if "\"" in condition_type:
            condition_type = condition_type.replace("\"", "")
        if "\"" in condition_value:
            condition_value = condition_value.replace("\"", "")
        # 读取文件
        if os.path.exists(filename):
            with open(filename, "r") as file:
                staff_list = file.readlines()
                new_staff_list = []
                # 判断文件内容是否为空
                if staff_list:
                    # 根据类型去condition_list查找对应的所以 在根据对应的索引去查找值
                    index1 = condition_list.index(condition_type)
                    index2 = condition_list.index(update_type)
                    for staff in staff_list:
                        staff_info = staff.split(",")
                        # 判断文件中查找出的值是否和用户输入条件值一致
                        if staff_info[index1] == condition_value:
                            staff_info[index2] = update_value
                            new_staff = ",".join(staff_info)
                        else:
                            new_staff = staff
                        # 将符合条件的更改后的员工信息存储到大列表中
                        new_staff_list.append(new_staff)
                    # 写入文件
                    with open(filename, "w") as wfile:
                        wfile.writelines(new_staff_list)
                    print("修改成功")
                    # 是否继续修改
                    choice = input("是否继续修改(y/n):")
                    if choice == "y":
                        flag = True
                    elif choice == "n":
                        flag = False




def show(staff, find_info, con_list=condition_list):
    """
    员工信息显示函数
    :param staff: 员工
    :param find_info: 显示所有员工信息 或者是 显示员工某个具体信息
    :param con_list: condition_list
    :return: None
    """
    if find_info == "*":
        staff_info = staff.split(",")
        print("staff_id " + staff_info[0] + " name " + staff_info[1] + " age " + staff_info[
            2] + " phone " + staff_info[3] + " dept " + staff_info[4] + " enroll_date " +
              staff_info[
                  5].strip())
    else:
        staff_info = staff.split(",")
        find_info_list = find_info.split(",")
        for info in find_info_list:
            print(" " + info + " " + staff_info[con_list.index(info)], end="")
        print()




if __name__ == '__main__':
    main()

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1cEs1Qkl6MlBvMHViUFNJd3JIejRiRG5EU1Q1ZkxuT3NnbklBZjJQUUxWZDdNcXk3aWFWeWlhekEvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1QTF1Z090VGpaOWd5YlRydUN4NFlpY3F4c2JycFVERnBqOENFNGp1akdGbXh2QnJmUEdkQ3J2Zy82NDA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1VDl5eWMzR3BwTjlYOXlMMUZPYWNzU3ZHMHVaTU9kbGdsYXkySk05Y0tTbkp0N3dVS3E2czZRLzY0MA?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1aDhrd3JMU3kwWXdPVEp5dHZyWkUxTkVnOVUySDhuaWJaejJqZ0F0Z2RDQTBQblNFeWlhemJBVHcvNjQw?x-oss-process=image/format,png"><img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1MU5sQXREekFmUWJZdmlhZWFDaWE1RkRsS0VBSzQ2UHlTUm84S21pYUltVjE5RklkamxsVGxwWVRRLzY0MA?x-oss-process=image/format,png">

## 29.网络访问日志

```
# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 00:58
# @Author  : 我就是任性-Amo
# @FileName: network.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import re
import os


file_name = "网站访问日志.txt"




def read_txt(filename):
    """
    读取文件中的数据
    :param filename: 文件名
    :return: 返回文件数据列表
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            log_list = file.readlines()
            if log_list:
                return log_list




def total(filename, name):
    """
    统计文件中所有的pv数，uv数，设备列表等
    :param filename: 需要处理的文本
    :param name: 传入需要返回哪个数据列表
    :return: 根据name 返回对应的列表
    """
    uv_list = []  # 统计所有的uv数量
    pv_list = []  # 统计所有的pv数量
    equipment_list = []  # 统计所有的设备来源
    log_list = read_txt(filename)  # 读取文本中的数据
    for log in log_list:
        # 1.统计本日志文件的总uv
        re_obj1 = re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip())
        if re_obj1:
            uv_list.append(re_obj1.group())
        # 2.将符合的pv追加到列表中
        pv_list.append(log.split("\"")[1])
        # 3.将符合的设备来源添加到列表中
        mozilla_index = log.find("Mozilla/5.0")
        r_index = log.find(")", mozilla_index)
        if mozilla_index != -1 and r_index != -1:
            equipment_list.append(log[mozilla_index: r_index + 1])
    if name == "uv":
        return uv_list
    elif name == "pv":
        return pv_list
    elif name == "equipment":
        return equipment_list




def every_hour(filename):
    """
    列出全天每小时的pv、uv数
    :param filename: 文件名
    :return: 无
    """
    temp_hour = "00"
    count = 0
    log_list = read_txt(filename)
    every_hour_uv = []
    for log in log_list:
        hour = re.search(r"\[.*\]", log).group().split(":")[1]
        value = ""
        if re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip()):
            value = re.match(r"(\d{1,3}\.){3}\d{1,3}", log.strip()).group()
        if temp_hour == hour:
            if value not in every_hour_uv:
                every_hour_uv.append(value)
            count += 1
            if temp_hour == "23" and log == log_list[-1]:
                print(f"全天{temp_hour}~第二天00时间段的uv数量为:{len(every_hour_uv) - 1}", end=" ")
                print(f"pv数量为:{count}")
        else:
            # 因为文件中每一行的数据有些并不是以ip开头 所以就会存在为空
            # 那么第一次为空的时候在列表中是不存在的 所以要减去为空白的一次
            temp = temp_hour
            temp_hour = hour
            print(f"全天{temp}~{temp_hour}时间段的uv数量为:{len(every_hour_uv) - 1}", end=" ")
            print(f"pv数量为:{count}")
            count = 1
            every_hour_uv.clear()
            every_hour_uv.append(value)




def show(filename, name, default=1):
    """
    根据传入的名称 统计指定的值以及其对应的数量 并选择是否排序及个数
    :param default: 结果默认降序排列 并且取出前10个数据
    :param filename: 文件名
    :param name: 统计的名称
    :return: 返回字典 key:为要查询的名称 value:为其对应的数量
    """
    name1_list = total(filename, name)
    # 对数据进行去重
    name1_set = set(name1_list)
    # 定义字典用于返回结果
    name1_dict = {}
    if name == "uv":
        for name1 in name1_set:
            if name1 not in name1_dict:
                name1_dict[name1] = name1_list.count(name1)
    elif name == "pv":
        for pv in name1_set:
            try:
                new_pv = pv.split(" ")[1]
                if new_pv not in name1_dict:
                    name1_dict[new_pv] = name1_list.count(pv)
            except IndexError as e:
                pass
    elif name == "equipment":
        for equipment in name1_set:
            if equipment not in name1_dict:
                name1_dict[equipment] = name1_list.count(equipment)
    top10_name = sorted(name1_dict.items(), key=lambda item: item[1], reverse=True)[:10]
    return top10_name




if __name__ == "__main__":
    print(total(file_name, "uv"))  # 测试统计uv数量
    every_hour(file_name)  # 测试统计一天每小时的uv pv数量
    print(show(file_name, "pv"))  # 测试top10 pv数量

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1OUIydDNXeGpOeElWT2RoNnpRNnVHaHN4QUNjVGtsaFBlN2lhaHVBZ1UwSDd6UWdyWUtvYU92QS82NDA?x-oss-process=image/format,png">

## 30.selenium基本操作流程

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 00:53
# @Author  : 我就是任性-Amo
# @FileName: 25.selenium基本操作流程.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




from selenium import webdriver
import time


# 这里以拉勾网为例子
# 1.准备url和创建浏览器对象
url = "https://www.lagou.com/jobs/list_python?labelWords=&amp;fromSearch=true&amp;suginput="
driver = webdriver.Chrome()
# 2.发送请求
driver.get(url)
# 3.根据实际需求判断是否需要操作滚动条
for j in range(3):
    driver.execute_script("window.scrollBy(0,1000);")
    time.sleep(3)
# 4.解析数据
li_list = driver.find_elements_by_xpath("//ul[@class='item_con_list']//li")
data_list = []
for li in li_list:
    # 职位以及地区
    position = li.find_element_by_xpath(".//h3").text
    address = li.find_element_by_xpath(".//em").text
    # 公司名称
    company_name = li.find_element_by_xpath(".//div[@class='company_name']/a").text
    # 薪资范围 经验及学历要求
    li_b_l = li.find_element_by_xpath(".//div[@class='p_bot']//div[@class='li_b_l']").text.strip()
    # 工作内容
    span_list = li.find_elements_by_xpath("//div[@class='li_b_l']//span[@class='']")
    work = ""
    for k in span_list:
        work += k.text
    # 公司规模
    industry = li.find_element_by_xpath(".//div[@class='industry']").text
    # 公司介绍(福利 团队等等)
    introduce = li.find_element_by_xpath(".//div[@class='li_b_r']").text
    # 5.保存数据 这里为了演示将数据保存到字典中即可
    print({"职位": position, "地区": address, "薪资": li_b_l, "工作内容": work, "公司规模": industry, "公司介绍": introduce})
# 6.翻页 找到下一页的按钮即可
# 7.退出浏览器
driver.quit()

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1Q05PZzZ6VDZoOW42T3hyc1U3YnVNTFVKZjJCVXFZbWFXSXJvNU1aWHRGdWM5Q0JlN3NpYVJGZy82NDA?x-oss-process=image/format,png">

## 31.字典的排序

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 10:05
# @Author  : 我就是任性-Amo
# @FileName: 26.字典的排序.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
"""
sorted函数:
    sorted(iterable, key, reverse), sorted一共有iterable，key，reverse这三个参数
        1.iterable:表示可迭代对象
        2.key:一个函数，用来选取参与比较的元素
        3.reverse:用来指定排序是倒序还是顺序
            reverse=True则是倒序（从大到小），reverse=False则是顺序（从小到大），默认是reverse=False
"""
import operator


# 1.字典按照key排序
my_dict = {'lilee': 25, 'age': 24, 'phone': 12}
print(sorted(my_dict.keys()))
# my_dict.items()返回了三个元素 每个元素都是一个元组 元组中有两个元素
# 第一个元素为key, 第二个元素为value reverse=True降序排列
print(sorted(my_dict.items(), key=lambda item: item[0], reverse=True))


# 2.字典的value值进行排序


# 2.1 key()使用lambda匿名函数取出value值进行排序
print(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))


# 2.2 使用operator的itemgetter进行排序()
print(sorted(my_dict.items(), key=operator.itemgetter(1)))

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1OG1uZmI3OHhlZzY2RmJEMWtmY3dYSTBWdFZrZjkydVhQeGJ3VlJmc0t6Z2Z5eVhzalBraWNPUS82NDA?x-oss-process=image/format,png">

## 32.字符串切片练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 15:20
# @Author  : 我就是任性-Amo
# @FileName: 27.字符串切片练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 定义一个字符串 name = "abcdefg" 使用切片得到以下数据
# 切片的语法: [start_index: end_index: step]
# start_index: 表示起始索引
# end_index: 表示结束索引
# step: 表示步长，步长不能为0，且默认值为1
# 列表元组等也是支持切片的
name = "abcdefg"


# cde
print(name[2:5])
# abcde
print(name[:5])  # 省略start_index，保留end_index，这样会从第一个元素开始，切到end_index - 1的元素为止
# bcdefg
print(name[1:])  # 保留start_index，但省略end_index，这样会从起始索引开始，切到最后一个元素为止
# abcdefg
print(name[:])  # 省略start_index、end_index和step，这样就表示就表示切片整个序列，也就是复制出了一个新的字符串序列
# aceg
print(name[::2])  # 省略start_index、end_index，但保留step，表示对整个序列，按照步长的规则取值
# abcdef
print(name[:-1])
# def
print(name[3:6])
# gfedcba
print(name[::-1])  # 步长为-1表示逆序
# 注意:步长和切片的方向要一致 否则切片失败

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1NUtKOXkwWGNzMUJGVGNxU1lqWllabGxDQ3J1YWVVV1BobG5EckY4Z2lhcndLOVg3ak1kcVZyUS82NDA?x-oss-process=image/format,png">

## 33.字符串方法练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 16:05
# @Author  : 我就是任性-Amo
# @FileName: 28.字符串方法的练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


name = " gouguoQ "
# 移除name变量对应值的两边的空格，并输出移除后的内容
print(name.strip())
# 判断name变量对应的值是否以"go"开头，并输出结果
print(name.startswith("go"))  # False
# 判断name变量对应的值是否以"Q"结尾，并输出结果
print(name.endswith("Q"))
# 将name变量对应的值中的"o"，替换为"p"，并输出结果
print(name.replace("o", "p"))
# 将name变量对应的值根据"o"分割，并输出结果
print(name.split("o"))
# 请问上一题分割之后得到的值是什么类型(可选)
# 上一题分割之后得到的值是列表数据类型
# 将name变量对应的值变大写，并输出结果
print(name.upper())
# 将name变量对应的值变成小写，并输出结果
print(name.lower())
# 请输出name变量对应的值的第二个字符？请输出name变量对应的值的前三个字符.请输出name变量对应值的后2个字符
# 切片
print(name[2:3])
print(name[0:3])
print(name[-2:])
# 请输出name变量中的值"Q的索引的位置
print(name.index("Q"))
# 获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
temp_str = "woaini"
print(temp_str[:-1])
# 利用下划线将列表的每一个元素拼接成字符串  li = ['gou', 'guo', 'qi']
li = ['gou', 'guo', 'qi']
print("_".join(li))

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1aEN3M2lid0I3MDlFNTVpY2c1RkVCQWpTWGVYRm9WWWpjazJMZ0tQZUU4MWlhWG9XYnlvaWJQblo4Zy82NDA?x-oss-process=image/format,png">

## 34.将列表中的数字类型转换为字符串类型

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 16:33
# @Author  : 我就是任性-Amo
# @FileName: 29.将列表中的数字类型转换为字符串类型.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 代码题2: 把[1,2,3,4]转换成"1234"


num_list = [1, 2, 3, 4]
temp_str = "".join(map(str, num_list))
print(temp_str)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1RXY4eUFSMnExSEk3cmNmNnJCRVRpY1FZNUNFVjlzTzhGd0JKbVBqcVVGdVMxM3V6VlZGNEIxdy82NDA?x-oss-process=image/format,png">

## 35.把一个元素全为数字的列表中的所有偶数加1

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 16:44
# @Author  : 我就是任性-Amo
# @FileName: 30.把一个元素全为数字的列表中的所有偶数加1.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 代码题1: 编程实现 把一个元素全为数字的列表中的所有偶数加1
# 思路1: 使用循环
num_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(num_list1)):
    # 判断列表中的每一个元素是否能被2整除
    if num_list1[i] % 2 == 0:
        # 符合该条件的元素+1
        num_list1[i] += 1


print(num_list1)


# 思路2: 使用高阶函数
num_list2 = [100, 101, 102, 103, 104, 105, 106, 107]
new_list = list(map(lambda x: x + 1 if x % 2 == 0 else x, num_list2))
print(new_list)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1bmRaZmlhY2xSS1V0RXo0TmtpY21YbmRDY3FyMzZrcXM2VHNyZUZ5TFBQeTUxa216Q2w3Y1p6UGcvNjQw?x-oss-process=image/format,png">

## 36.统计元组中元素出现的个数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 18:31
# @Author  : 我就是任性-Amo
# @FileName: 31.统计元组中元素出现的个数.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/xw1680




# 代码题:test = ("a", "b", "c", "a", "c")，
# 统计元组中每个元素出现的次数把最终的结果保存到列表中，例如[('a',2),('b',1),('c',2)]。


# 1.使用循环
test = ("a", "b", "c", "a", "c")
temp = []  # 定义一个空列表用于去重 如果使用集合不能保证顺序
for i in test:
    if i not in temp:
        temp.append(i)


# 统计temp列表中每个元素在test中出现的次数 并追加到新列表中
# 使用列表推导式
result = [(i, test.count(i)) for i in temp]
print(result)  # 最后的结果与预期的一致

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1blJCZ3NkNjBLb1daTUFReWliTXo4WjZrd1ViSVpEODRNRUxjMkZVNnZVN3ZvS3ZXdVQ5RldmQS82NDA?x-oss-process=image/format,png">

## 37.循环练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 18:49
# @Author  : 我就是任性-Amo
# @FileName: 32.循环练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 1.使用 while 循环实现输出 1,2,3,4,5,7,8,9,11,12
# 分析:使用while打印1-12 但是跳过了6和10 说明要使用continue
# 使用while的步骤:
# 1.初始值 2.条件判断语句 3.循环体 4.条件控制语句
i = 1
while i &lt;= 12:
    if i == 6 or i == 10:
        i += 1
        continue
    if i == 12:
        print(i, end="")
    else:
        print(i, end=",")
    i += 1
print()
print("***************************")
# 2.使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
j = 100
while j &gt;= 50:
    print(j)
    if j == 50:
        k = 0
        while k &lt;= 50:
            print(k)
            k += 1
    j -= 1
print("***************************")
# 或者直接使用第二种方法:
count = 100
while count &gt; -2:
    if count &gt;= 50:
        print(count)
    else:
        print(49 - count)
    count -= 1
print("***************************")
# 3.使用 while 循环实现输出 1-100 内的所有奇数
m = 1
while m &lt;= 100:
    if m % 2 != 0:
        print(m)
    m += 1
print("***************************")
# 4.使用 while 循环实现输出 1-100 内的所有偶数
n = 1
while n &lt;= 100:
    if n % 2 == 0:
        print(n)
    n += 1
print("***************************")
# 5.使用while循环实现输出2-3+4-5+6…+100 的和
j = 2
get_sum = 0
while j &lt;= 100:
    if j % 2 != 0:
        get_sum -= j
    else:
        get_sum += j
    j += 1


print(get_sum)

```

## 

## 38.打印各种图形

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 23:30
# @Author  : 我就是任性-Amo
# @FileName: 33.打印各种图形.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 1.打印矩形
row = int(input("row:"))  # 控制行数
clo = int(input("clo:"))  # 控制每一列星星的个数
for i in range(row):
    print("*" * clo)


print("------------------------------")


# 2.打印空心矩形
for i in range(row):
    if i == 0 or i == row - 1:
        print("*" * clo)
    else:
        print("*" + " " * (clo - 2) + "*")
print("------------------------------")


# 3.打印等腰直角三角形
for i in range(1, row + 1):
    print("*" * i)
print("------------------------------")


# 4.打印空心等腰直角三角形
for i in range(1, row + 1):
    if i == 1 or i == row:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")


print("------------------------------")


# 5.打印等腰三角形 这里的话自定义有点点问题 以后我空了再说
s = 1  # 定义星星的初始个数
for i in range(row + 1):
    if i &lt; row / 2:
        print(" " * ((row - s) // 2) + "*" * s)
    s += 2


print("------------------------------")


# 6.打印右三角形
for i in range(1, 10):
    if i &gt;= 6:
        print("* " * (10 - i))
    else:
        print("* " * i)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1MUdsM2hTUUNyU3JKRDJHRzFZSWljZ2t1SXdqaWFham9IUzlheXlxOFJzeHZCWVA1N1Z3aWJyN3B3LzY0MA?x-oss-process=image/format,png">

## 39.列表操作

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 00:05
# @Author  : 我就是任性-Amo
# @FileName: 34.列表操作.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 题目: 写代码，有如下列表，按照要求实现每一个功能


li = ["amo", "jerry", "crystal"]
# 1.计算列表长度并输出
print(len(li))
# 2.列表中追加元素"seven"，并输出添加后的列表
li.append("seven")
print(li)
# 请在列表的第1个位置插入元素"Tony"，并输出添加后的列表
li.insert(0, "Tony")
print(li)
# 请修改列表第2个位置的元素为"Kelly"，并输出修改后的列表
li[1] = "Kelly"
print(li)
# 请删除列表中的元素"jerry"，并输出修改后的列表
li.remove("jerry")
print(li)
# 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
del_value = li.pop(1)
print(del_value)
print(li)
# 请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print(li)


li = ["amo", "jerry", "crystal", "paul", "ben"]
print(li)
# 1.请删除列表中的第2至5个元素，并输出删除元素后的列表 这个的话很简单 不进行演示
# 使用列表的切片
# 2.请将列表所有的元素反转，并输出反转后的列表
# 这里的话可以使用切片或者是使用reverse()方法
li.reverse()
print(li)
li = li[::-1]
print(li)
print("--------------------------")
# 请使用for、len、range输出列表的索引
for i in range(len(li)):
    print(i)
print("--------------------------")
# 请使用enumrate输出列表元素和序号（序号从100开始）
for key, value in enumerate(li, 100):
    print(key, value)
print("--------------------------")
# 4.请使用for循环输出列表的所有元素
for ele in li:
    print(ele)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1SEx0ZmlhVmEzTm9PNGljTHh1bVhoN3JpYTdpYXc4RVl2N1g3OGZKQVFjbnVIdU5EN2h0T2EydWljMmcvNjQw?x-oss-process=image/format,png">

## 40.文件操作

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 00:23
# @Author  : 我就是任性-Amo
# @FileName: 35.文件操作.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 1.有名为poetry.txt的文件，其内容如下，请删除第三行
"""
昔人已乘黄鹤去,此地空余黄鹤楼.
黄鹤一去不复返,白云千载空悠悠.
晴川历历汉阳树,芳草萋萋鹦鹉洲.
日暮乡关何处是?烟波江上使人愁.
"""
with open("poetry.txt", 'r', encoding="utf8") as file:
    content = file.readlines()
    content.pop(2)


with open("poetry.txt", "w", encoding="utf8") as file:
    file.writelines(content)


# 2.有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行
"""
pizza,100001
alex,100002
egon,100003
"""
# 如果是这个文本文件的需求都是只删除最后一行的数据的话 则直接可以使用pop()方法
with open("user_info.txt", "r", encoding="utf8") as file:
    content = file.readlines()


for ele in content:
    if ele.split(",")[1] == "100003":
        content.remove(ele)
with open("user_info.txt", "w", encoding="utf8") as file:
    file.writelines(content)

```

## 

## 41.字符串练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:12
# @Author  : 我就是任性-Amo
# @FileName: 36.字符串练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import re


# 代码题1:已知字符串 test = "aAsmr3idd4bgs7Dlsf9eAF",将字符串中的数字取出，生成一个新的字符串
test = "aAsmr3idd4bgs7Dlsf9eAF"
new_str = ""
# 1.使用循环 判断每一个字符是否是数字 如果是则将其进行拼接
for i in test:
    if i.isdigit():
        new_str += i
print(new_str)


# 2.使用正则表达式
new_str = "".join(re.findall(r"\d", test))
print(new_str)


# 代码题2:现有字符串 msg = "hel@#$lo pyt \nhon ni\t hao%$" ，
# 去掉所有不是英文字母的字符，打印结果："清理以后的结果为: hellopythonnihao"


msg = "hel@#$lo pyt \nhon ni\t hao%$"
new_str = ""
# 1.使用循环 判断每一个字符是否是字母 如果是则进行拼接
for i in msg:
    if i.isalpha():
        new_str += i
print(new_str)
# 2.使用正则表达式
new_str = "".join(re.findall("[a-zA-Z]", msg))
print(new_str)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1Z0hGS041ZVppYTMwTXk4bmNOaWFrdXgzWkt0cXR4aWF6aWN4RFBoUWZ4cUU2RWliMnRnU1FGN1lmd3cvNjQw?x-oss-process=image/format,png">

## 42.数据序列综合练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:57
# @Author  : 我就是任性-Amo
# @FileName: 38.数据序列综合操作.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




"""
第一题:
  对数据进行清洗，去除数据中的`空字符串`、`None`、`广告`，只留下单词。
  对留下的单词统计次数 数据见info.txt
"""
# 1.打开文件
f = open("info.txt", encoding="gbk")
# 2.操作文件
content = f.readlines()  # 返回一个列表
total_list = []
# 3.关闭文件
f.close()
for i in content:
    # 1.去除空白行使用strip()方法
    temp_str = i.strip()
    # 2.去除None
    if temp_str == "None":
        pass
    else:
        list1 = temp_str.split("-")
        total_list.extend(list1)
set1 = set(total_list)
dict1 = {}
for i in set1:
    dict1[i] = total_list.count(i)
print(dict1)
print("-------------------------------")


"""
第二题:
url = "http://{}.58.com/zpjianshen/pn{}"
start_url = 'http://{}.58.com/zpjianshen/'
start_urls = []
citys = ['北京', '金华', '上海', '深圳', '广州', '厦门', '武汉', '长沙', '石家庄', '南昌', '青岛', '杭州', '合肥', '南宁', '贵阳', '兰州', '郑州', '哈尔滨']
cityscode = ['bj', 'jh', 'sh', 'sz', 'gz', 'xm', 'wh', 'cs', 'sjz', 'nc', 'qd', 'hz', 'hf', 'nn', 'gy', 'lz', 'zz',
             'hrb']
# 需求：要求将上面的url补充完整
# 格式如下:
# [{'北京':['http://bj.58.com/zpjianshen/pn1',...'http://bj.58.com/zpjianshen/pn30']}, {'金华':['http://jh.58.com/zpjianshen/pn1',...,'http://bj.58.com/zpjianshen/pn30']}]
"""
# 18个演员
# list1 = [{"赵丽颖": []}, {"林志颖": []}]
# 1.定义一个总列表存储所有的字典
total_lit = []
citys = ['北京', '金华', '上海', '深圳', '广州', '厦门', '武汉', '长沙', '石家庄', '南昌', '青岛', '杭州', '合肥', '南宁', '贵阳', '兰州', '郑州', '哈尔滨']
cityscode = ['bj', 'jh', 'sh', 'sz', 'gz', 'xm', 'wh', 'cs', 'sjz', 'nc', 'qd', 'hz', 'hf', 'nn', 'gy', 'lz', 'zz',
             'hrb']
# 2.遍历citys拿到每一个城市的名字
for i in range(len(citys)):
    # 2.1 拿到每一个具体城市的名字
    city = citys[i]
    # 2.2 拿到城市所对应的citycode
    city_code = cityscode[i]
    # 2.3 拼接url
    temp_url = f'http://{city_code}.58.com/zpjianshen/' + "pn{}"
    # 2.4 构造url_list
    url_list = [temp_url.format(i) for i in range(1, 31)]
    # 2.5 往大列表中追加字典元素
    total_lit.append({city: url_list})
for i in total_lit:
    print(i)

```

程序运行结果如下：

```
{'五险一金': 9856, '包吃': 8265, '包住': 14125, '饭补': 3646, '加班补助': 3893, '交通补助': 4745, '话补': 3513, '年底双薪': 7417, '广告': 531, '提供食宿': 7, '周末双休': 6380, '房补': 3511, '餐补': 20}
-------------------------------
{'北京': ['http://bj.58.com/zpjianshen/pn1', 'http://bj.58.com/zpjianshen/pn2', 'http://bj.58.com/zpjianshen/pn3', 'http://bj.58.com/zpjianshen/pn4', 'http://bj.58.com/zpjianshen/pn5', 'http://bj.58.com/zpjianshen/pn6', 'http://bj.58.com/zpjianshen/pn7', 'http://bj.58.com/zpjianshen/pn8', 'http://bj.58.com/zpjianshen/pn9', 'http://bj.58.com/zpjianshen/pn10', 'http://bj.58.com/zpjianshen/pn11', 'http://bj.58.com/zpjianshen/pn12', 'http://bj.58.com/zpjianshen/pn13', 'http://bj.58.com/zpjianshen/pn14', 'http://bj.58.com/zpjianshen/pn15', 'http://bj.58.com/zpjianshen/pn16', 'http://bj.58.com/zpjianshen/pn17', 'http://bj.58.com/zpjianshen/pn18', 'http://bj.58.com/zpjianshen/pn19', 'http://bj.58.com/zpjianshen/pn20', 'http://bj.58.com/zpjianshen/pn21', 'http://bj.58.com/zpjianshen/pn22', 'http://bj.58.com/zpjianshen/pn23', 'http://bj.58.com/zpjianshen/pn24', 'http://bj.58.com/zpjianshen/pn25', 'http://bj.58.com/zpjianshen/pn26', 'http://bj.58.com/zpjianshen/pn27', 'http://bj.58.com/zpjianshen/pn28', 'http://bj.58.com/zpjianshen/pn29', 'http://bj.58.com/zpjianshen/pn30']}
{'金华': ['http://jh.58.com/zpjianshen/pn1', 'http://jh.58.com/zpjianshen/pn2', 'http://jh.58.com/zpjianshen/pn3', 'http://jh.58.com/zpjianshen/pn4', 'http://jh.58.com/zpjianshen/pn5', 'http://jh.58.com/zpjianshen/pn6', 'http://jh.58.com/zpjianshen/pn7', 'http://jh.58.com/zpjianshen/pn8', 'http://jh.58.com/zpjianshen/pn9', 'http://jh.58.com/zpjianshen/pn10', 'http://jh.58.com/zpjianshen/pn11', 'http://jh.58.com/zpjianshen/pn12', 'http://jh.58.com/zpjianshen/pn13', 'http://jh.58.com/zpjianshen/pn14', 'http://jh.58.com/zpjianshen/pn15', 'http://jh.58.com/zpjianshen/pn16', 'http://jh.58.com/zpjianshen/pn17', 'http://jh.58.com/zpjianshen/pn18', 'http://jh.58.com/zpjianshen/pn19', 'http://jh.58.com/zpjianshen/pn20', 'http://jh.58.com/zpjianshen/pn21', 'http://jh.58.com/zpjianshen/pn22', 'http://jh.58.com/zpjianshen/pn23', 'http://jh.58.com/zpjianshen/pn24', 'http://jh.58.com/zpjianshen/pn25', 'http://jh.58.com/zpjianshen/pn26', 'http://jh.58.com/zpjianshen/pn27', 'http://jh.58.com/zpjianshen/pn28', 'http://jh.58.com/zpjianshen/pn29', 'http://jh.58.com/zpjianshen/pn30']}
{'上海': ['http://sh.58.com/zpjianshen/pn1', 'http://sh.58.com/zpjianshen/pn2', 'http://sh.58.com/zpjianshen/pn3', 'http://sh.58.com/zpjianshen/pn4', 'http://sh.58.com/zpjianshen/pn5', 'http://sh.58.com/zpjianshen/pn6', 'http://sh.58.com/zpjianshen/pn7', 'http://sh.58.com/zpjianshen/pn8', 'http://sh.58.com/zpjianshen/pn9', 'http://sh.58.com/zpjianshen/pn10', 'http://sh.58.com/zpjianshen/pn11', 'http://sh.58.com/zpjianshen/pn12', 'http://sh.58.com/zpjianshen/pn13', 'http://sh.58.com/zpjianshen/pn14', 'http://sh.58.com/zpjianshen/pn15', 'http://sh.58.com/zpjianshen/pn16', 'http://sh.58.com/zpjianshen/pn17', 'http://sh.58.com/zpjianshen/pn18', 'http://sh.58.com/zpjianshen/pn19', 'http://sh.58.com/zpjianshen/pn20', 'http://sh.58.com/zpjianshen/pn21', 'http://sh.58.com/zpjianshen/pn22', 'http://sh.58.com/zpjianshen/pn23', 'http://sh.58.com/zpjianshen/pn24', 'http://sh.58.com/zpjianshen/pn25', 'http://sh.58.com/zpjianshen/pn26', 'http://sh.58.com/zpjianshen/pn27', 'http://sh.58.com/zpjianshen/pn28', 'http://sh.58.com/zpjianshen/pn29', 'http://sh.58.com/zpjianshen/pn30']}
{'深圳': ['http://sz.58.com/zpjianshen/pn1', 'http://sz.58.com/zpjianshen/pn2', 'http://sz.58.com/zpjianshen/pn3', 'http://sz.58.com/zpjianshen/pn4', 'http://sz.58.com/zpjianshen/pn5', 'http://sz.58.com/zpjianshen/pn6', 'http://sz.58.com/zpjianshen/pn7', 'http://sz.58.com/zpjianshen/pn8', 'http://sz.58.com/zpjianshen/pn9', 'http://sz.58.com/zpjianshen/pn10', 'http://sz.58.com/zpjianshen/pn11', 'http://sz.58.com/zpjianshen/pn12', 'http://sz.58.com/zpjianshen/pn13', 'http://sz.58.com/zpjianshen/pn14', 'http://sz.58.com/zpjianshen/pn15', 'http://sz.58.com/zpjianshen/pn16', 'http://sz.58.com/zpjianshen/pn17', 'http://sz.58.com/zpjianshen/pn18', 'http://sz.58.com/zpjianshen/pn19', 'http://sz.58.com/zpjianshen/pn20', 'http://sz.58.com/zpjianshen/pn21', 'http://sz.58.com/zpjianshen/pn22', 'http://sz.58.com/zpjianshen/pn23', 'http://sz.58.com/zpjianshen/pn24', 'http://sz.58.com/zpjianshen/pn25', 'http://sz.58.com/zpjianshen/pn26', 'http://sz.58.com/zpjianshen/pn27', 'http://sz.58.com/zpjianshen/pn28', 'http://sz.58.com/zpjianshen/pn29', 'http://sz.58.com/zpjianshen/pn30']}
{'广州': ['http://gz.58.com/zpjianshen/pn1', 'http://gz.58.com/zpjianshen/pn2', 'http://gz.58.com/zpjianshen/pn3', 'http://gz.58.com/zpjianshen/pn4', 'http://gz.58.com/zpjianshen/pn5', 'http://gz.58.com/zpjianshen/pn6', 'http://gz.58.com/zpjianshen/pn7', 'http://gz.58.com/zpjianshen/pn8', 'http://gz.58.com/zpjianshen/pn9', 'http://gz.58.com/zpjianshen/pn10', 'http://gz.58.com/zpjianshen/pn11', 'http://gz.58.com/zpjianshen/pn12', 'http://gz.58.com/zpjianshen/pn13', 'http://gz.58.com/zpjianshen/pn14', 'http://gz.58.com/zpjianshen/pn15', 'http://gz.58.com/zpjianshen/pn16', 'http://gz.58.com/zpjianshen/pn17', 'http://gz.58.com/zpjianshen/pn18', 'http://gz.58.com/zpjianshen/pn19', 'http://gz.58.com/zpjianshen/pn20', 'http://gz.58.com/zpjianshen/pn21', 'http://gz.58.com/zpjianshen/pn22', 'http://gz.58.com/zpjianshen/pn23', 'http://gz.58.com/zpjianshen/pn24', 'http://gz.58.com/zpjianshen/pn25', 'http://gz.58.com/zpjianshen/pn26', 'http://gz.58.com/zpjianshen/pn27', 'http://gz.58.com/zpjianshen/pn28', 'http://gz.58.com/zpjianshen/pn29', 'http://gz.58.com/zpjianshen/pn30']}
{'厦门': ['http://xm.58.com/zpjianshen/pn1', 'http://xm.58.com/zpjianshen/pn2', 'http://xm.58.com/zpjianshen/pn3', 'http://xm.58.com/zpjianshen/pn4', 'http://xm.58.com/zpjianshen/pn5', 'http://xm.58.com/zpjianshen/pn6', 'http://xm.58.com/zpjianshen/pn7', 'http://xm.58.com/zpjianshen/pn8', 'http://xm.58.com/zpjianshen/pn9', 'http://xm.58.com/zpjianshen/pn10', 'http://xm.58.com/zpjianshen/pn11', 'http://xm.58.com/zpjianshen/pn12', 'http://xm.58.com/zpjianshen/pn13', 'http://xm.58.com/zpjianshen/pn14', 'http://xm.58.com/zpjianshen/pn15', 'http://xm.58.com/zpjianshen/pn16', 'http://xm.58.com/zpjianshen/pn17', 'http://xm.58.com/zpjianshen/pn18', 'http://xm.58.com/zpjianshen/pn19', 'http://xm.58.com/zpjianshen/pn20', 'http://xm.58.com/zpjianshen/pn21', 'http://xm.58.com/zpjianshen/pn22', 'http://xm.58.com/zpjianshen/pn23', 'http://xm.58.com/zpjianshen/pn24', 'http://xm.58.com/zpjianshen/pn25', 'http://xm.58.com/zpjianshen/pn26', 'http://xm.58.com/zpjianshen/pn27', 'http://xm.58.com/zpjianshen/pn28', 'http://xm.58.com/zpjianshen/pn29', 'http://xm.58.com/zpjianshen/pn30']}
{'武汉': ['http://wh.58.com/zpjianshen/pn1', 'http://wh.58.com/zpjianshen/pn2', 'http://wh.58.com/zpjianshen/pn3', 'http://wh.58.com/zpjianshen/pn4', 'http://wh.58.com/zpjianshen/pn5', 'http://wh.58.com/zpjianshen/pn6', 'http://wh.58.com/zpjianshen/pn7', 'http://wh.58.com/zpjianshen/pn8', 'http://wh.58.com/zpjianshen/pn9', 'http://wh.58.com/zpjianshen/pn10', 'http://wh.58.com/zpjianshen/pn11', 'http://wh.58.com/zpjianshen/pn12', 'http://wh.58.com/zpjianshen/pn13', 'http://wh.58.com/zpjianshen/pn14', 'http://wh.58.com/zpjianshen/pn15', 'http://wh.58.com/zpjianshen/pn16', 'http://wh.58.com/zpjianshen/pn17', 'http://wh.58.com/zpjianshen/pn18', 'http://wh.58.com/zpjianshen/pn19', 'http://wh.58.com/zpjianshen/pn20', 'http://wh.58.com/zpjianshen/pn21', 'http://wh.58.com/zpjianshen/pn22', 'http://wh.58.com/zpjianshen/pn23', 'http://wh.58.com/zpjianshen/pn24', 'http://wh.58.com/zpjianshen/pn25', 'http://wh.58.com/zpjianshen/pn26', 'http://wh.58.com/zpjianshen/pn27', 'http://wh.58.com/zpjianshen/pn28', 'http://wh.58.com/zpjianshen/pn29', 'http://wh.58.com/zpjianshen/pn30']}
{'长沙': ['http://cs.58.com/zpjianshen/pn1', 'http://cs.58.com/zpjianshen/pn2', 'http://cs.58.com/zpjianshen/pn3', 'http://cs.58.com/zpjianshen/pn4', 'http://cs.58.com/zpjianshen/pn5', 'http://cs.58.com/zpjianshen/pn6', 'http://cs.58.com/zpjianshen/pn7', 'http://cs.58.com/zpjianshen/pn8', 'http://cs.58.com/zpjianshen/pn9', 'http://cs.58.com/zpjianshen/pn10', 'http://cs.58.com/zpjianshen/pn11', 'http://cs.58.com/zpjianshen/pn12', 'http://cs.58.com/zpjianshen/pn13', 'http://cs.58.com/zpjianshen/pn14', 'http://cs.58.com/zpjianshen/pn15', 'http://cs.58.com/zpjianshen/pn16', 'http://cs.58.com/zpjianshen/pn17', 'http://cs.58.com/zpjianshen/pn18', 'http://cs.58.com/zpjianshen/pn19', 'http://cs.58.com/zpjianshen/pn20', 'http://cs.58.com/zpjianshen/pn21', 'http://cs.58.com/zpjianshen/pn22', 'http://cs.58.com/zpjianshen/pn23', 'http://cs.58.com/zpjianshen/pn24', 'http://cs.58.com/zpjianshen/pn25', 'http://cs.58.com/zpjianshen/pn26', 'http://cs.58.com/zpjianshen/pn27', 'http://cs.58.com/zpjianshen/pn28', 'http://cs.58.com/zpjianshen/pn29', 'http://cs.58.com/zpjianshen/pn30']}
{'石家庄': ['http://sjz.58.com/zpjianshen/pn1', 'http://sjz.58.com/zpjianshen/pn2', 'http://sjz.58.com/zpjianshen/pn3', 'http://sjz.58.com/zpjianshen/pn4', 'http://sjz.58.com/zpjianshen/pn5', 'http://sjz.58.com/zpjianshen/pn6', 'http://sjz.58.com/zpjianshen/pn7', 'http://sjz.58.com/zpjianshen/pn8', 'http://sjz.58.com/zpjianshen/pn9', 'http://sjz.58.com/zpjianshen/pn10', 'http://sjz.58.com/zpjianshen/pn11', 'http://sjz.58.com/zpjianshen/pn12', 'http://sjz.58.com/zpjianshen/pn13', 'http://sjz.58.com/zpjianshen/pn14', 'http://sjz.58.com/zpjianshen/pn15', 'http://sjz.58.com/zpjianshen/pn16', 'http://sjz.58.com/zpjianshen/pn17', 'http://sjz.58.com/zpjianshen/pn18', 'http://sjz.58.com/zpjianshen/pn19', 'http://sjz.58.com/zpjianshen/pn20', 'http://sjz.58.com/zpjianshen/pn21', 'http://sjz.58.com/zpjianshen/pn22', 'http://sjz.58.com/zpjianshen/pn23', 'http://sjz.58.com/zpjianshen/pn24', 'http://sjz.58.com/zpjianshen/pn25', 'http://sjz.58.com/zpjianshen/pn26', 'http://sjz.58.com/zpjianshen/pn27', 'http://sjz.58.com/zpjianshen/pn28', 'http://sjz.58.com/zpjianshen/pn29', 'http://sjz.58.com/zpjianshen/pn30']}
{'南昌': ['http://nc.58.com/zpjianshen/pn1', 'http://nc.58.com/zpjianshen/pn2', 'http://nc.58.com/zpjianshen/pn3', 'http://nc.58.com/zpjianshen/pn4', 'http://nc.58.com/zpjianshen/pn5', 'http://nc.58.com/zpjianshen/pn6', 'http://nc.58.com/zpjianshen/pn7', 'http://nc.58.com/zpjianshen/pn8', 'http://nc.58.com/zpjianshen/pn9', 'http://nc.58.com/zpjianshen/pn10', 'http://nc.58.com/zpjianshen/pn11', 'http://nc.58.com/zpjianshen/pn12', 'http://nc.58.com/zpjianshen/pn13', 'http://nc.58.com/zpjianshen/pn14', 'http://nc.58.com/zpjianshen/pn15', 'http://nc.58.com/zpjianshen/pn16', 'http://nc.58.com/zpjianshen/pn17', 'http://nc.58.com/zpjianshen/pn18', 'http://nc.58.com/zpjianshen/pn19', 'http://nc.58.com/zpjianshen/pn20', 'http://nc.58.com/zpjianshen/pn21', 'http://nc.58.com/zpjianshen/pn22', 'http://nc.58.com/zpjianshen/pn23', 'http://nc.58.com/zpjianshen/pn24', 'http://nc.58.com/zpjianshen/pn25', 'http://nc.58.com/zpjianshen/pn26', 'http://nc.58.com/zpjianshen/pn27', 'http://nc.58.com/zpjianshen/pn28', 'http://nc.58.com/zpjianshen/pn29', 'http://nc.58.com/zpjianshen/pn30']}
{'青岛': ['http://qd.58.com/zpjianshen/pn1', 'http://qd.58.com/zpjianshen/pn2', 'http://qd.58.com/zpjianshen/pn3', 'http://qd.58.com/zpjianshen/pn4', 'http://qd.58.com/zpjianshen/pn5', 'http://qd.58.com/zpjianshen/pn6', 'http://qd.58.com/zpjianshen/pn7', 'http://qd.58.com/zpjianshen/pn8', 'http://qd.58.com/zpjianshen/pn9', 'http://qd.58.com/zpjianshen/pn10', 'http://qd.58.com/zpjianshen/pn11', 'http://qd.58.com/zpjianshen/pn12', 'http://qd.58.com/zpjianshen/pn13', 'http://qd.58.com/zpjianshen/pn14', 'http://qd.58.com/zpjianshen/pn15', 'http://qd.58.com/zpjianshen/pn16', 'http://qd.58.com/zpjianshen/pn17', 'http://qd.58.com/zpjianshen/pn18', 'http://qd.58.com/zpjianshen/pn19', 'http://qd.58.com/zpjianshen/pn20', 'http://qd.58.com/zpjianshen/pn21', 'http://qd.58.com/zpjianshen/pn22', 'http://qd.58.com/zpjianshen/pn23', 'http://qd.58.com/zpjianshen/pn24', 'http://qd.58.com/zpjianshen/pn25', 'http://qd.58.com/zpjianshen/pn26', 'http://qd.58.com/zpjianshen/pn27', 'http://qd.58.com/zpjianshen/pn28', 'http://qd.58.com/zpjianshen/pn29', 'http://qd.58.com/zpjianshen/pn30']}
{'杭州': ['http://hz.58.com/zpjianshen/pn1', 'http://hz.58.com/zpjianshen/pn2', 'http://hz.58.com/zpjianshen/pn3', 'http://hz.58.com/zpjianshen/pn4', 'http://hz.58.com/zpjianshen/pn5', 'http://hz.58.com/zpjianshen/pn6', 'http://hz.58.com/zpjianshen/pn7', 'http://hz.58.com/zpjianshen/pn8', 'http://hz.58.com/zpjianshen/pn9', 'http://hz.58.com/zpjianshen/pn10', 'http://hz.58.com/zpjianshen/pn11', 'http://hz.58.com/zpjianshen/pn12', 'http://hz.58.com/zpjianshen/pn13', 'http://hz.58.com/zpjianshen/pn14', 'http://hz.58.com/zpjianshen/pn15', 'http://hz.58.com/zpjianshen/pn16', 'http://hz.58.com/zpjianshen/pn17', 'http://hz.58.com/zpjianshen/pn18', 'http://hz.58.com/zpjianshen/pn19', 'http://hz.58.com/zpjianshen/pn20', 'http://hz.58.com/zpjianshen/pn21', 'http://hz.58.com/zpjianshen/pn22', 'http://hz.58.com/zpjianshen/pn23', 'http://hz.58.com/zpjianshen/pn24', 'http://hz.58.com/zpjianshen/pn25', 'http://hz.58.com/zpjianshen/pn26', 'http://hz.58.com/zpjianshen/pn27', 'http://hz.58.com/zpjianshen/pn28', 'http://hz.58.com/zpjianshen/pn29', 'http://hz.58.com/zpjianshen/pn30']}
{'合肥': ['http://hf.58.com/zpjianshen/pn1', 'http://hf.58.com/zpjianshen/pn2', 'http://hf.58.com/zpjianshen/pn3', 'http://hf.58.com/zpjianshen/pn4', 'http://hf.58.com/zpjianshen/pn5', 'http://hf.58.com/zpjianshen/pn6', 'http://hf.58.com/zpjianshen/pn7', 'http://hf.58.com/zpjianshen/pn8', 'http://hf.58.com/zpjianshen/pn9', 'http://hf.58.com/zpjianshen/pn10', 'http://hf.58.com/zpjianshen/pn11', 'http://hf.58.com/zpjianshen/pn12', 'http://hf.58.com/zpjianshen/pn13', 'http://hf.58.com/zpjianshen/pn14', 'http://hf.58.com/zpjianshen/pn15', 'http://hf.58.com/zpjianshen/pn16', 'http://hf.58.com/zpjianshen/pn17', 'http://hf.58.com/zpjianshen/pn18', 'http://hf.58.com/zpjianshen/pn19', 'http://hf.58.com/zpjianshen/pn20', 'http://hf.58.com/zpjianshen/pn21', 'http://hf.58.com/zpjianshen/pn22', 'http://hf.58.com/zpjianshen/pn23', 'http://hf.58.com/zpjianshen/pn24', 'http://hf.58.com/zpjianshen/pn25', 'http://hf.58.com/zpjianshen/pn26', 'http://hf.58.com/zpjianshen/pn27', 'http://hf.58.com/zpjianshen/pn28', 'http://hf.58.com/zpjianshen/pn29', 'http://hf.58.com/zpjianshen/pn30']}
{'南宁': ['http://nn.58.com/zpjianshen/pn1', 'http://nn.58.com/zpjianshen/pn2', 'http://nn.58.com/zpjianshen/pn3', 'http://nn.58.com/zpjianshen/pn4', 'http://nn.58.com/zpjianshen/pn5', 'http://nn.58.com/zpjianshen/pn6', 'http://nn.58.com/zpjianshen/pn7', 'http://nn.58.com/zpjianshen/pn8', 'http://nn.58.com/zpjianshen/pn9', 'http://nn.58.com/zpjianshen/pn10', 'http://nn.58.com/zpjianshen/pn11', 'http://nn.58.com/zpjianshen/pn12', 'http://nn.58.com/zpjianshen/pn13', 'http://nn.58.com/zpjianshen/pn14', 'http://nn.58.com/zpjianshen/pn15', 'http://nn.58.com/zpjianshen/pn16', 'http://nn.58.com/zpjianshen/pn17', 'http://nn.58.com/zpjianshen/pn18', 'http://nn.58.com/zpjianshen/pn19', 'http://nn.58.com/zpjianshen/pn20', 'http://nn.58.com/zpjianshen/pn21', 'http://nn.58.com/zpjianshen/pn22', 'http://nn.58.com/zpjianshen/pn23', 'http://nn.58.com/zpjianshen/pn24', 'http://nn.58.com/zpjianshen/pn25', 'http://nn.58.com/zpjianshen/pn26', 'http://nn.58.com/zpjianshen/pn27', 'http://nn.58.com/zpjianshen/pn28', 'http://nn.58.com/zpjianshen/pn29', 'http://nn.58.com/zpjianshen/pn30']}
{'贵阳': ['http://gy.58.com/zpjianshen/pn1', 'http://gy.58.com/zpjianshen/pn2', 'http://gy.58.com/zpjianshen/pn3', 'http://gy.58.com/zpjianshen/pn4', 'http://gy.58.com/zpjianshen/pn5', 'http://gy.58.com/zpjianshen/pn6', 'http://gy.58.com/zpjianshen/pn7', 'http://gy.58.com/zpjianshen/pn8', 'http://gy.58.com/zpjianshen/pn9', 'http://gy.58.com/zpjianshen/pn10', 'http://gy.58.com/zpjianshen/pn11', 'http://gy.58.com/zpjianshen/pn12', 'http://gy.58.com/zpjianshen/pn13', 'http://gy.58.com/zpjianshen/pn14', 'http://gy.58.com/zpjianshen/pn15', 'http://gy.58.com/zpjianshen/pn16', 'http://gy.58.com/zpjianshen/pn17', 'http://gy.58.com/zpjianshen/pn18', 'http://gy.58.com/zpjianshen/pn19', 'http://gy.58.com/zpjianshen/pn20', 'http://gy.58.com/zpjianshen/pn21', 'http://gy.58.com/zpjianshen/pn22', 'http://gy.58.com/zpjianshen/pn23', 'http://gy.58.com/zpjianshen/pn24', 'http://gy.58.com/zpjianshen/pn25', 'http://gy.58.com/zpjianshen/pn26', 'http://gy.58.com/zpjianshen/pn27', 'http://gy.58.com/zpjianshen/pn28', 'http://gy.58.com/zpjianshen/pn29', 'http://gy.58.com/zpjianshen/pn30']}
{'兰州': ['http://lz.58.com/zpjianshen/pn1', 'http://lz.58.com/zpjianshen/pn2', 'http://lz.58.com/zpjianshen/pn3', 'http://lz.58.com/zpjianshen/pn4', 'http://lz.58.com/zpjianshen/pn5', 'http://lz.58.com/zpjianshen/pn6', 'http://lz.58.com/zpjianshen/pn7', 'http://lz.58.com/zpjianshen/pn8', 'http://lz.58.com/zpjianshen/pn9', 'http://lz.58.com/zpjianshen/pn10', 'http://lz.58.com/zpjianshen/pn11', 'http://lz.58.com/zpjianshen/pn12', 'http://lz.58.com/zpjianshen/pn13', 'http://lz.58.com/zpjianshen/pn14', 'http://lz.58.com/zpjianshen/pn15', 'http://lz.58.com/zpjianshen/pn16', 'http://lz.58.com/zpjianshen/pn17', 'http://lz.58.com/zpjianshen/pn18', 'http://lz.58.com/zpjianshen/pn19', 'http://lz.58.com/zpjianshen/pn20', 'http://lz.58.com/zpjianshen/pn21', 'http://lz.58.com/zpjianshen/pn22', 'http://lz.58.com/zpjianshen/pn23', 'http://lz.58.com/zpjianshen/pn24', 'http://lz.58.com/zpjianshen/pn25', 'http://lz.58.com/zpjianshen/pn26', 'http://lz.58.com/zpjianshen/pn27', 'http://lz.58.com/zpjianshen/pn28', 'http://lz.58.com/zpjianshen/pn29', 'http://lz.58.com/zpjianshen/pn30']}
{'郑州': ['http://zz.58.com/zpjianshen/pn1', 'http://zz.58.com/zpjianshen/pn2', 'http://zz.58.com/zpjianshen/pn3', 'http://zz.58.com/zpjianshen/pn4', 'http://zz.58.com/zpjianshen/pn5', 'http://zz.58.com/zpjianshen/pn6', 'http://zz.58.com/zpjianshen/pn7', 'http://zz.58.com/zpjianshen/pn8', 'http://zz.58.com/zpjianshen/pn9', 'http://zz.58.com/zpjianshen/pn10', 'http://zz.58.com/zpjianshen/pn11', 'http://zz.58.com/zpjianshen/pn12', 'http://zz.58.com/zpjianshen/pn13', 'http://zz.58.com/zpjianshen/pn14', 'http://zz.58.com/zpjianshen/pn15', 'http://zz.58.com/zpjianshen/pn16', 'http://zz.58.com/zpjianshen/pn17', 'http://zz.58.com/zpjianshen/pn18', 'http://zz.58.com/zpjianshen/pn19', 'http://zz.58.com/zpjianshen/pn20', 'http://zz.58.com/zpjianshen/pn21', 'http://zz.58.com/zpjianshen/pn22', 'http://zz.58.com/zpjianshen/pn23', 'http://zz.58.com/zpjianshen/pn24', 'http://zz.58.com/zpjianshen/pn25', 'http://zz.58.com/zpjianshen/pn26', 'http://zz.58.com/zpjianshen/pn27', 'http://zz.58.com/zpjianshen/pn28', 'http://zz.58.com/zpjianshen/pn29', 'http://zz.58.com/zpjianshen/pn30']}
{'哈尔滨': ['http://hrb.58.com/zpjianshen/pn1', 'http://hrb.58.com/zpjianshen/pn2', 'http://hrb.58.com/zpjianshen/pn3', 'http://hrb.58.com/zpjianshen/pn4', 'http://hrb.58.com/zpjianshen/pn5', 'http://hrb.58.com/zpjianshen/pn6', 'http://hrb.58.com/zpjianshen/pn7', 'http://hrb.58.com/zpjianshen/pn8', 'http://hrb.58.com/zpjianshen/pn9', 'http://hrb.58.com/zpjianshen/pn10', 'http://hrb.58.com/zpjianshen/pn11', 'http://hrb.58.com/zpjianshen/pn12', 'http://hrb.58.com/zpjianshen/pn13', 'http://hrb.58.com/zpjianshen/pn14', 'http://hrb.58.com/zpjianshen/pn15', 'http://hrb.58.com/zpjianshen/pn16', 'http://hrb.58.com/zpjianshen/pn17', 'http://hrb.58.com/zpjianshen/pn18', 'http://hrb.58.com/zpjianshen/pn19', 'http://hrb.58.com/zpjianshen/pn20', 'http://hrb.58.com/zpjianshen/pn21', 'http://hrb.58.com/zpjianshen/pn22', 'http://hrb.58.com/zpjianshen/pn23', 'http://hrb.58.com/zpjianshen/pn24', 'http://hrb.58.com/zpjianshen/pn25', 'http://hrb.58.com/zpjianshen/pn26', 'http://hrb.58.com/zpjianshen/pn27', 'http://hrb.58.com/zpjianshen/pn28', 'http://hrb.58.com/zpjianshen/pn29', 'http://hrb.58.com/zpjianshen/pn30']}

```

## 43.函数基础练习

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:21
# @Author  : 我就是任性-Amo
# @FileName: 37.函数练习.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


# 1.打印图形(函数嵌套)
# 1.1 打印一条横线
# 1.2 打印多条横线
# 2.这里的话是可以使用装饰器进行实现的




def print_line():
    """打印一条横线"""
    print("-------------------")




def print_lines(num):
    """打印多条横线"""
    for i in range(num):
        print_line()




print_line()  # 调用普通函数
print("*******************")
print_lines(4)
print("*******************")




# 2.函数计算(函数嵌套)
# 2.1 求三个数之和
# 2.2 求三个数平均值
def get_sum(a, b, c):
    """求三个数之和"""
    return a + b + c




def get_average(a, b, c):
    return get_sum(a, b, c) / 3




print(get_average(10, 20, 30))
print("*******************")


# 3.定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，
# 需要找出里面所有的"hello"的位置，返回的格式是一个元组，即: (0,10,21,29)
temp_str = "helloworldhellopythonhelloc++hellojava"




def findall(tem_str, find_str):
    """
    tem_str: 查找的字符串
    find_str: 查找的单词
    """
    index = 0
    index_list = []
    while True:
        index = tem_str.find(find_str, index)  # 每次index都在变化 变化的长度就是要查找单词的长度
        if index == -1:
            break
        index_list.append(index)  # 将所有的下标都追加到列表中
        index += len(find_str)
    return tuple(index_list)  # 为了和题目一致 将列表转换为元组




print(findall(temp_str, "hello"))  # 测试在指定的字符串中查找所有的"hello"的下标
# 4.定义一个函数 sum_test 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并打印结果。




print("*******************")




def sum_test(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result




print(sum_test(100))

```

运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1cmt3dm1YNGdaakNReE1iandXQUJVMUZ1SjNYWFZpY1NrS2U0UWFFZ3NHUUxVeTZCRXNleDA1QS82NDA?x-oss-process=image/format,png">

## 44.复制文本文件

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 11:03
# @Author  : 我就是任性-Amo
# @FileName: 39.复制文件.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 1.复制普通文本文件
# filename = input("&gt;&gt;&gt;:")
filename = "1.两个变量的交换.py"
# 一般的话 我们在windows中复制文件 都会在文件名末尾默认添加-副本
new_filename = filename[:filename.rfind(".")] + " - 副本" + filename[filename.rfind("."):]
# 1.打开文件
f1 = open(filename, "r")
f2 = open(new_filename, "w")
# 2.读取文件内容 并将读取的文件写入另一个新的文件中
content = f1.read()
f2.write(content)
# 3.关闭文件
f2.close()
f1.close()


# 2.复制图片
filename = "陈瑶.jpeg"
# 一般的话 我们在windows中复制文件 都会在文件名末尾默认添加-副本
new_filename = filename[:filename.rfind(".")] + " - 副本" + filename[filename.rfind("."):]
# 1.打开文件
f3 = open(filename, "rb")
f4 = open(new_filename, "wb")
# 2.读取文件内容 并将读取的文件写入另一个新的文件中
content = f3.read()
f4.write(content)
# 3.关闭文件
f4.close()
f3.close()

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1OTlkZFNwaGxFVFlkTFJhaWJ1QTBIbWYzSHJjVnM4TGtpYVJpYjhuUllhaWNKMzdzRHl1SlRpY0FBU3cvNjQw?x-oss-process=image/format,png">

## 45.函数参数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 17:32
# @Author  : 我就是任性-Amo
# @FileName: 40.函数参数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680




# 1.函数传参的方式
def test(a, b, c):
    print(a, b, c)




# 1.1 位置传参
test(10, 20, 30)
# 1.2 序列传参数(也是位置传参的一种)
test(*"ABC")  # 使用星号将"ABC"拆解为"A" "B" "C" 然后在按照位置传参的方式去匹配函数的形参
# 1.3 关键字传参
test(a=10, c=30, b=20)  # 根据名字传递参数
# 1.4 双星号字典传参
# 字典的key要和函数行参的名字一致
test(**{"a": "amo", "b": "paul", "c": "jason"})




# 2.函数定义参数的方式
# 2.1 位置形参
def test2(a, b, c):
    pass




# 2.2 缺省参数
# 因为大部分人的国籍都是中国，所以此时我们可以指定默认的参数
# 如果用户有传入实际的国籍 就以用户实际传入的参数为准 否则默认就为中国
def person_info(name, age, nationality="中国"):
    print(name, age, nationality)




person_info("amo", 18)
person_info("奥巴马", 23, "美国")




# 2.3 命名关键字形参
# *标识着这个函数的形参为命名关键字形参 没有其他实际的含义
# 表示着
def test3(*, a, b, c):
    print(a, b, c)  # 命名关键字行参只能是使用关键字传参的方式或者是双星号字典传参的方式




test3(a=10, b=20, c=30)
test3(**{"a": 30, "b": 20, "c": 10})




# 2.4 星号元组形参
# 用于接受多余的位置参数 一般使用*args表示
def test4(*args):
    print(args)




test4(10, 20, 30, 40)  # 将10,20,30,40先打包成一个元组，然后赋值给args
test4(10, 20, *[30, 40, 50])




# 2.5 双星号字典形参
def test5(**kwargs):
    print(kwargs)




test5(a=1, b=2, c=3)  # 将所有的变量作为字典的key,值作为字典的value 然后传递给变量kwargs
test5(**{"name": "amo", "age": 18, "is_male": True})

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1ZWliSEppY3NIWXYyYm1OMHY3MWh1RzFnbU1rS2N0MjAwTUVtTk95aWFnZXk3WEZpY3h4YmJkOUhpYncvNjQw?x-oss-process=image/format,png">

## 46.检索敏感词并描红输出

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 18:51
# @Author  : 我就是任性-Amo
# @FileName: 41.检索敏感词并描红输出.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


"""
需求:敏感词，一般是指带有暴力倾向、不健康的色彩或过度宣传营销的词或用语，也有一些网站根据自身实际情况，
设定一些适用于网站的特殊敏感词。例如在淘宝、京东等平台中，对于商品宣传用语有一定的限定，如"盗版" "水货" "山寨" "领先" "最佳" "最大"和"唯一"
等词语都不能用于产品宣传，否则可能造成商品下架及其他处罚。
为了不让敏感词对企业宣传、营销带来损害，可以使用程序检测敏感词。广告法规定的限制敏感词很多，可以先建立敏感词库，然后对输入的文字进行敏感词检索输出.


本例稍加修改，即可实现如下功能，快来试试吧!
    输入运营文字，实现用星号标注敏感词。
    查找多个文件中的敏感词，可以将敏感词保存到文件中，然后从文件读取敏感词进行检测。
    替换文本或文件中的指定文字并输出替换个数。
"""


word = input("请输入或者拷贝含有敏感词的宣传文字: \n")
sensitive = ["第一", "国家级", "最高级", "最佳", "独一无二", "一流", "仅此一次", "顶级", "顶尖", "尖端", "极品", "极佳", "绝佳", "绝对", "终极", "极致", "首个",
             "首选", "独家", "首发", "首次", "首款", "金牌", "名牌", "王牌", "领袖", "领先", "领导", "缔造者", "巨星", "掌门人", "至尊", "巅峰", "奢侈",
             "资深", "之王", "王者", "冠军"]  # 使用列表建立敏感词库


sensitive_find = []  # 存储查找到的敏感词
new_word = word  # 复制一份用户输入的内容 用来标红
for item in sensitive:
    if word.count(item) &gt; 0:  # 查找每个敏感词汇在用户输入的内容是否出现
        sensitive_find.append(item + ":" + str(word.count(item)) + "次")  # 记录敏感词的出现次数
        new_word = new_word.replace(item, "\033[1;31m" + item + "\033[0m")  # 对敏感词描红输出


print("发现敏感词汇如下:")
for item in sensitive_find:
    print(item)


print("敏感词位置已用星号进行标注: \n" + new_word)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1ZWljSDI4M24zQnVkQ3Nuc3R6NGxKVUIzVVlrTmljZkF0QU5oZENyOHM5WTBrTW1oNG03M21UM2cvNjQw?x-oss-process=image/format,png">

## 47.实现字符串与列表等数据去重

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 19:20
# @Author  : 我就是任性-Amo
# @FileName: 42.实现字符串与列表等数据的去除.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


"""
背景:
随着大数据，云技术等的发展，各行各业每天都会产生海量的大数据，如何让这些大数据逐步为人类创造更多的价值，
为企业所用，已经成为互联网经济的核心发展方向。
由于目前各行各业产生的大数据会有很多重复的数据，影响分析效率，
因此进行大数据分析的第一步，是检测和消除其中的重复数据，通过数据去重，一方面是减少存储空间和网络带宽的占用另一方面可以减少数据分析量。
数据去重又称重复数据删除，是指在一个数据集合中，找出重复的数据并将其删除，只保存唯一的数据单元。
Python主要操作的数据有字符串和列表，该如何在Python中对字符串和列表去重呢?
"""


# 字符串去重的5种方法
# 1.通过for循环遍历字符串去重
name = "王李张李陈王杨张吴周王刘赵黄吴杨"
new_name = ''
for char in name:
    if char not in new_name:  # 如果不在新的字符串中
        new_name += char  # 拼接到新字符串中的末尾


print(new_name)
# 2.通过while循环遍历字符串去重
name = "王李张李陈王杨张吴周王刘赵黄吴杨"
new_name = ''
i = 0
while i &lt;= len(name) - 1:
    if name[i] not in new_name:
        new_name += name[i]
    i += 1
print(new_name)
# 3.使用列表的方法去重
name = "王李张李陈王杨张吴周王刘赵黄吴杨"
new_name = ''
name_set = set(name)  # 对字符串进行去重
print("".join(sorted(name_set, key=name.index)))  # 按照name字符串下标进行排序
# 4.在原字符串中直接删除
name = "王李张李陈王杨张吴周王刘赵黄吴杨"
length = len(name)  # 字符串下标的总长度
for s in name:
    if name[0] in name[1:length]:
        name = name[1:length]
    else:
        name = name[1:length] + name[0]
print(name)  # 这个的话没有按照原来的顺序进行排列 感觉不是太好
# 5.使用fromkeys()方法把字符串转成字典
name = "王李张李陈王杨张吴周王刘赵黄吴杨"
zd = {}.fromkeys(name)
my_list = list(zd.keys())
print("".join(my_list))


# 列表的去重方法
# 定义一个列表:下面的各种方法都将使用该列表作为操作数据
city = ['上海', "广州", "上海", "成都", "上海", "上海", "北京", "上海", "广州", "北京", "上海"]
# 方法1: for循环语句
new_city = []
for item in city:
    if item not in new_city:
        new_city.append(item)
print(new_city)
# 方法2: set()方法 改变原来的顺序
print(list(set(city)))
# 方法3: set()方法 不改变原来数据的顺序
city_set = set(city)
new_city = sorted(city_set, key=city.index)
print(new_city)
# 方法4: count()方法统计并删除，需要先排序(改变原来顺序)
city.sort()
for x in city:
    while city.count(x) &gt; 1:
        del city[city.index(x)]
print(city)


# 方法5: 把列表转成字典
my_list = list({}.fromkeys(city).keys())
print(my_list)

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1UXo1c1R3SkJieVNlZ3M3OElITnZxTFRNN2JEN0lTQjhYUTFIYzZiUjFjZzlRczNmZnhTZDF3LzY0MA?x-oss-process=image/format,png">

## 48.匿名函数lambda

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 20:11
# @Author  : 我就是任性-Amo
# @FileName: 43.lambda表达式.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680


"""
lambda表达式运用场景:
    如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化
语法:
    lambda 参数列表: 表达式
lambda表达式的参数可有可⽆，函数的参数在lambda表达式中完全适⽤
lambda函数能接收任何数量的参数但只能返回⼀个表达式的值
"""
# 1.lambda表达式实现两个数的和
print((lambda x, y: x + y)(100, 200))


# 2.lambda的参数形式
# 2.1 无参数
print((lambda: 100)())
# 2.2 一个参数
print((lambda x: x)("hello amo"))
# 2.3 默认参数
print((lambda a, b, c=100: a + b + c)(10, 20))
# 2.4 可变参数 **args
print((lambda *args: args)(10, 20, 30))  # 这里的可变参数传到lambda之后，返回元组
# 2.5 可变参数 **kwargs
print((lambda **kwargs: kwargs)(name='amo', age=18))


# 3.lambda表达式的运用:
# 3.1 带判断的lambda表达式
print((lambda a, b: a if a &gt; b else b)(1000, 500))
# 3.2 列表数据按字典key的值排序
students = [{'name': 'TOM', 'age': 20},
            {'name': 'ROSE', 'age': 19},
            {'name': 'Jack', 'age': 22}]
# 按name值升序排列
students.sort(key=lambda x: x['name'])
print(students)
# 按name值降序排列
students.sort(key=lambda x: x['name'], reverse=True)
print(students)
# 按age值升序排列
students.sort(key=lambda x: x['age'])
print(students)
# 3.3 当做参数传入高阶函数
num_list = [1, 2, 3, 4, 5, 6, 7]
# 对num_list中的每个数字进行+1
print(list(map(lambda x: x + 1, num_list)))

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1eWdhd3RGa3RFVVAyTVJpYnE2WW50ZEZwTlFIQW1tVUlUd1JGRkduRWVQRXVVQkRnZHFya0VYZy82NDA?x-oss-process=image/format,png">

## 49.使用MD5或SHA1等算法对用户密码进行加密

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 22:42
# @Author  : 我就是任性-Amo
# @FileName: 44.使用md5或sha1等算法对用户密码进行加密.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
import hashlib
import hmac  # 采用哈希算法计算后的MD5加密


"""
问题背景:互联网.上每天都有亿量级别的数据在进行交互，与此同时，我们每天也都会看到
各种各样类似"用户信息泄露""**公司用户密码惨遭破解"的类似新闻。
网络安全在当今的互联网时代越来越重要，而密码安全就是其中最基础的一种保护用户信息的方式，
比如我们登录淘宝、京东，或者自己开发一些项目的时候，通常都会将用户密码加密之后，再进行存储.
"""


# 1.解决方案:
# 使用Python对用户密码进行加密非常简单，因为Python中提供了一个hashlib模块，该模块中提供了常用的加密算法，如MD5、SHA1等等，
# 例如要对输入的密码进行MD5加密，可以使用如下代码:


content = input("请输入要加密的内容:")
# MD5加密(返回32位十六进制字符串)
md5 = hashlib.md5()
md5.update(content.encode("utf8"))
print("MD5加密:" + md5.hexdigest())
# MD5是最常见的加密算法，速度很快，生成结果是固定的128位字节，通常用一个32位的十六进制字符串表示。


# 使用SHA1加密用户密码的方式与MD5类似，代码如下:
content = input("请输入要加密的内容:")
# SHA1加密(返回40位十六进制表示字符串)
sha1 = hashlib.sha1()
sha1.update(content.encode("utf8"))
print("SHA1加密:" + sha1.hexdigest())


# 另外，hashlib模块中还提供了比SHA1更安全的算法，比如SHA256、SHA512等，
# 但是越安全的算法不仅越慢，而且返回结果的长度更长。例如，使用SHA256对用户输入的密码进行加密，代码如下:
content = input("请输入要加密的内容:")
# SHA256加密(返回64位十六进制表示字符串)
sha256 = hashlib.sha256()
sha256.update(content.encode("utf8"))
print("SHA256加密:" + sha256.hexdigest())


# 上面介绍了几种普通的加密算法，但对于黑客来说，他们很容易利用常用口令的MD5或SHA1.值
# 反推出用户的明文密码。因此，为了确保存储的密码不是那些已经被计算出来的固定值，
# 我们可以为.原始密码加一个随机的字符串(key)来实现这个功能，Python中的hmac模块提供了一种Hmac算法,
# 它可以在计算哈希码的过程中，把key值混入计算过程中，这种加密方式更安全，其实现代码如下:
content = input("请输入要加密的内容:")
pwd = content.encode("utf8")
key = 'id'.encode("utf8")
h = hmac.new(key, pwd, digestmod="MD5")
print("更安全的MD5加密:" + h.hexdigest())

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1c3B1Y1hpYzk0bHRIZ2Q3dmZIcGNTZDlIMjNpY3QyNFhFUDlPZHBEOVNpYlVrOGhuc0RBUUg1T1R3LzY0MA?x-oss-process=image/format,png">

## 50.高阶函数

```
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 23:57
# @Author  : 我就是任性-Amo
# @FileName: 45.高阶函数.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/xw1680
from functools import reduce


"""
高阶函数: 高阶函数英文叫Higher-order function
编写高阶函数，就是让函数的参数能够接收别的函数。
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
"""


"""
我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下:
"""
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x ** 2, num_list)))


# 解释说明: map()传入的第一个参数是一个匿名函数
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串:
print(list(map(str, num_list)))


"""
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是:
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
# 例子: 对一个序列求和 注意reduce不是python内置的 在functools模块中
print(reduce(lambda a, b: a + b, [1, 3, 5, 7, 9]))  # 这里的话其实可以直接使用sum()
# 但是如果想把[1, 3, 5, 7, 9]变成13579 高阶函数reduce就可以派上用场了
print(reduce(lambda a, b: a * 10 + b, [1, 3, 5, 7, 9]))
# 第一次:1*10+3 --&gt;13
# 第二次:13*10+5 --&gt;135
# 第三次:135*10+7 --&gt;1357
# 第四次:1357*10+9 --&gt;13579


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入: ['adam', 'LISA', 'barT']，输出: ['Adam', 'Lisa', 'Bart']
print(list(map(lambda x: x.capitalize(), ['adam', 'LISA', 'barT'])))




# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积:
def prod(num_list2):
    return reduce(lambda x, y: x * y, num_list2)




print(prod([3, 5, 7, 9]))


"""
Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
"""
# 在一个list中，删掉偶数，只保留奇数
print(list(filter(lambda x: True if x % 2 != 0 else False, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


"""
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
Python内置的sorted()函数就可以对list进行排序:
"""
print(sorted([36, 5, -12, 9, -21]))  # 默认是升序排列 可以通过reverse来控制
print(sorted([36, 5, -12, 9, -21], reverse=False))  # 默认是升序排列 即reverse=False
print(sorted([36, 5, -12, 9, -21], reverse=True))  # reverse=True 降序排列


"""
此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序:
"""
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))

```

程序运行结果如下：<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9VTGliSGdYSXQzancxazU3eFRhTXZwNmljcEpiUFAwUEM1aWFnRjNuek8wTjY0RWFCM2w4RWEzam9pYkIxZU1ZOUhSSWJzRmlhRnFCekdIZUFPczFCaWFtb0ZpYlEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
