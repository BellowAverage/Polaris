
--- 
title:  100个python代码大全 
tags: []
categories: [] 

---
###  前言

我记得刚开始接触编程的时候，觉得太难了。也很好奇，写代码的那些人也太厉害了吧？全是英文的，他们的英文水平一定很好吧？他们是怎么记住这么多代码格式的？而且错了一个标点符号，整个程序都会有影响。一个程序几千行，错一个标点符号都不行这也太难了吧？带着新手的灵魂拷问，作为从业单片机编程10年的开发者，我来为大家拨开云雾。看完以后你就会明白，其实他们也没那么厉害！即便你是初中文凭，也照样能编程。对于python语言来说，要记得东西其实不多，基本就是几个常用语句加一些关键字而已。你所看到的那些几千甚至上万行的代码，都是用这些语句和关键词来重复编写的。只是他们逻辑功能不一样，另外的那些英文，都是程序员自己起的，比如说一些变量的名字，函数的名字。如果你喜欢你定义成abc都可以，只不过为了程序大了以后为了方便阅读和维护，我们一般起跟要实现的功能相同的英文缩写代替。比如说我要存储一个电压值，那你可以定义一个变量，名字叫VoltageValue,或者这两个词的缩写VoltVal。所以，大家不要把这个想得这么神秘和高大上。

### 1、for循环中的else条件

这是一个for-else方法，循环遍历列表时使用else语句。

下面举个例子，比如我们想检查一个列表中是否包含奇数。

那么可以通过for循环，遍历查找。

```
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")

```

### 2、数字求和

```
# -*- coding: UTF-8 -*-
# Filename : test.py
# author by : www.runoob.com
# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)
# 显示计算结果
print('数字 {0} 和 {1} 相加结果为：{2}'.format(num1, num2, sum))

```

执行以上代码输出结果为：

```
输入第一个数字：1.5
输入第二个数字：2.5
数字 1.5 和 2.5 相加结果为：4.0

```

### 3、

```
# -*- coding: UTF-8 -*-
# Filename : test.py
# author by : www.runoob.com
# 生成 0 ~ 9 之间的随机数
# 导入 random(随机数) 模块
import random
print(random.randint(0,9))
执行以上代码输出结果为：
4
以上实例我们使用了 random 模块的 randint() 函数来生成随机数，你每次执行后都返回不同的数字（0 到 9），该函数的语法为：
random.randint(a,b)

```
- 、将列表中的所有元素作为参数传递给函数
我们可以使用 * 号，提取列表中所有的元素

```
my_list = [1, 2, 3, 4]

print(my_list)  # [1, 2, 3, 4]
print(*my_list)  # 1 2 3 4

```

如此便可以将列表中的所有元素，作为参数传递给函数

```
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")

```

### 5、获取列表的所有中间元素

```
_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)  # [2, 3, 4, 5, 6, 7]

```

### 6、使用一行代码赋值多个变量

```
one, two, three, four = 1, 2, 3, 4

```

### 7、Python清空列表

```
RUNOOB = [6, 0, 4, 1]
print('清空前:', RUNOOB)
RUNOOB.clear()
print('清空后:', RUNOOB)
以上实例输出结果为：
清空前: [6, 0, 4, 1]
清空后: []

```

### 8、通过Enum枚举同一标签或一系列常量的集合

枚举是绑定到唯一的常量值的一组符号名称(成员)。

在枚举中，成员可以通过身份进行比较，枚举本身可以迭代。

```
from enum import Enum


class Status(Enum):
    NO_STATUS = -1
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


print(Status.IN_PROGRESS.name)  # IN_PROGRESS
print(Status.COMPLETED.value)  # 2

```
- 9、重复字符串
```
name = "Banana"
print(name * 4)  # BananaBananaBananaBanana

```

### 10、计算每个月天数

```
#!/usr/bin/python3
# author by : www.runoob.com
import calendar
monthRange = calendar.monthrange(2016,9)
print(monthRange)
执行以上代码输出结果为：
(3, 30)
输出的是一个元组，第一个元素是所查月份的第一天对应的是星期几（0-6），
第二个元素是这个月的天数。以上实例输出的意思为 2016 年 9 月份的第一
天是星期四，该月总共有 30 天。

```

### 11、输出指定范围内的素数

```
# 输出指定范围内的素数
# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
for num in range(lower,upper + 1):
# 素数大于 1
if num &gt; 1:
for i in range(2,num):
if (num % i) == 0:
break
else:
print(num)
执行以上程序，输出结果为：
$ python3 test.py
输入区间最小值: 1
输入区间最大值: 100

```

### 12、计算两数差值

```
def subtract(a, b):
    return a - b


print((subtract(1, 3)))  # -2
print((subtract(3, 1)))  # 2

```

上面的这个方法，需要考虑数值的先后顺序。

```
def subtract(a, b):
    return a - b


print((subtract(a=1, b=3)))  # -2
print((subtract(b=3, a=1)))  # -2

```

使用命名参数，安排顺序，这样就不会出错了。

### 13、奇数移到偶数前

已知线性表（a1,a2,…,an）按顺序结构存储且每个元素为不相等的整数。设计把所有奇数移动到所有偶数前边的算法（要求时间最少，辅助空间最少）。 对于 L，从左向右找到偶数 L.data[i]，从右向左找到奇数 L.data[j]，将两者交换。 循环这个过程直到 i 大于 j 为止。对应的算法如下： 时间复杂度O(n)，空间复杂度O(1)

```
void move(SqList &amp;L)
{
    int i=0,j=L.length-1,k;
    ElemType temp;
    while(i&lt;j)
    {
        //奇数从前向后找
        while(L.data[i]%2==1)
          i++;//指向奇数
        //偶数从后往前找
        while(L.data[j]%2==0)
          j--;//指向偶数
        if(i&lt;j)//奇数在偶数前面
        {
            temp=L.data[i];
            L.data[i]=L.data[j];
            L.data[j]=temp;
        }
    }
}

```



### 14、顺序表元素逆置

设计一个高效算法，将顺序表 L 中所有元素逆置，要求算法的空间复杂度为 O(1)。 扫描顺序表 L 的前半部分元素，对于元素 L.data[i],将其与后半部分对应元素 L.data[L.length-i-1]进行交换。对应的算法如下:

```
void reverse(SqList &amp;L)
{
    int i;
    ElemType x;
    //只扫描前半部分
    for(i=0;i=L.length/2;i++)
    {
        x=L.data[i];
        //L.data[i]后半部分对应元素为L.data[L.length-i-1]
        /*
        角标 0 1 2 3 4 5 6
        元素 a b c d e f g
        长度 length=7
        L.data[0]=L.data[L.length-0-1]=L.data[7-1-0]=L.data[6]
        */
        L.data[i]=L.data[L.length-i-1];
        L.data[L.length-i-1]=x;
    }
}

```

### 15、删除顺序表最小值元素

从顺序表中删除具有最小值的元素（假设唯一）并由函数返回被删除元素的 值。空出的位置由最后一个元素填补。 搜素整个顺序表，查找最小值元素并记在其位置，搜索结束后用最后一个元素填 补空出的原最小值元素的位置。

```
bool Delete_Min(SqList &amp;L,ElemType &amp;value)
{
    //表长为0不成立
    if(L.length==0)
       return false;
    //假设第一个元素为最小值
    value=L.data[0];
    //记录最小值元素下标
    int pos=0;
    int i;
    //从第二个元素开始比较
    for(i=1;i&lt;L.length;i++)
    {
        if(L.data[i]&lt;value)
        {
            value=L.data[i];
            pos=i;
        }
    }
    //删除位置的元素用最后一个元素取代
    L.data[pos]=L.data[length-1];
    //表长减一
    L.length--;
    return true;
}

```

**16、删除值在x~y之间的所有数据**

设计一个算法，从一给定的顺序表 L 中删除元素值在 x 到 y(x≤y)之间的所有元素， 要求以较高的效率来实现，空间复杂度为 O(1)。 本题是上述题目的变形。可以采用上述解法一的方法，只是将 L.data[i] == x 的条件改成 L.data[i] &gt;= x &amp;&amp; L.data[i] &lt;= y。

```
void del_xy(SqList &amp;L, ElemType x, ElemType y)
{
    int i;
    int k=0;
    for(i=0;i&lt;L.length;i++)
    {
        if(L.data[i]&gt;=x&amp;&amp;L.data[j]&lt;=y)
        {
            L.data[k]=L.data[i];
            k++;
        }
    }
    L.length=k;
}

```

**方法二：**

```
void del_xy(SqList &amp;L,ElemType x, ElemType y)
{
    int i=0,k=0;
    while(i&lt;L.length)
    {
        if(L.data[i]&gt;=x&amp;&amp;L.data[i]&lt;=y)
           k++;
        else
           L.data[i-k]=L.data[i];
    }
    L.length=L.length-k;
}

```

### 17、打印九九乘法表

打印我们小时候背诵用的九九乘法表

```
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0b2aa2db58d546229ae76f9439850581.png#pic_center">​

**读者福利：知道你对python感兴趣，便准备了这套python学习资料**

###  关于Python技术储备

>  
 学好 Python 不论是就业还是做赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！ 


### ** 关于Python技术储备**

 学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**一、Python所有方向的学习路线** 刚开始学习python，如果你连完整的学习步骤都没有规划好，基本不可能学会python。他把Python所有方向路线做了整理，形成各个领域的知识点汇总。<img alt="1d124212c9c146be837b8335f249888f.png" src="https://img-blog.csdnimg.cn/1d124212c9c146be837b8335f249888f.png">**二、入门学习视频** 我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。<img alt="2db26fa6ab0644fc8cce1896129b6517.png" src="https://img-blog.csdnimg.cn/2db26fa6ab0644fc8cce1896129b6517.png">**三、学习软件** 工欲善其事必先利其器。学习Python常用的开发软件都在这里了，给大家节省了很多时间。 **<img alt="21c0db7cda7e437f982c15bcdb69c7f8.png" src="https://img-blog.csdnimg.cn/21c0db7cda7e437f982c15bcdb69c7f8.png">**四、全套PDF电子书** 书籍的好处就在于权威和体系健全，刚开始学习的时候你可以只看视频或者听某个人讲课，但等你学完之后，你觉得你掌握了，这时候建议还是得去看一下书籍，看权威技术书籍也是每个程序员必经之路。<img alt="7184d856a8bd40d1a9d3b0ddf8b0a3ed.png" src="https://img-blog.csdnimg.cn/7184d856a8bd40d1a9d3b0ddf8b0a3ed.png">**五、、实战案例** 光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。<img alt="d0191cb2d04c41db881ab8611df0194a.png" src="https://img-blog.csdnimg.cn/d0191cb2d04c41db881ab8611df0194a.png">**六、面试资料** 我们学习Python必然是为了找到高薪的工作，下面这些面试题是来自阿里、腾讯、字节等一线互联网大厂最新的面试资料，并且有阿里大佬给出了权威的解答，刷完这一套面资料相信大家都能找到满意的工作。<img alt="af949dd0c26a49fba02d027e8b455eeb.png" src="https://img-blog.csdnimg.cn/af949dd0c26a49fba02d027e8b455eeb.png"><img alt="7e46fa54bb88437caf334f2ee9a0534b.png" src="https://img-blog.csdnimg.cn/7e46fa54bb88437caf334f2ee9a0534b.png">



因**因链接常被和谐，可戳安全链接：**

##### **👉**

 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/e93788c6df1c918a3cf7bffec011e68f.png">
