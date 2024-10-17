
--- 
title:  LeetCode473. 火柴拼正方形 
tags: []
categories: [] 

---
## 

**目录**















## 一、题目

你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

<img alt="" height="221" src="https://img-blog.csdnimg.cn/c0d4fd65e3ff46edb04d5629129d9cd1.png" width="233">

示例 1:

>  
 输入: matchsticks = [1,1,2,2,2] 输出: true 解释: 能拼成一个边长为2的正方形，每边两根火柴。 


示例 2:

>  
 输入: matchsticks = [3,3,3,3,4] 输出: false 解释: 不能用所有火柴拼成一个正方形。 


提示:

>  
 1 &lt;= matchsticks.length &lt;= 15 1 &lt;= matchsticks[i] &lt;= 108 


## 二、解题思路

首先计算所有火柴的总长度totallen，如果totallen 不是 4 的倍数，那么不可能拼成正方形，返回false。当totallen 是 44 的倍数时，每条边的边长为 totallen/4,用 edges 来记录 4 条边已经放入的火柴总长度。对于第 index 火柴，尝试把它放入其中一条边内且满足放入后该边的火柴总长度不超过len，然后继续枚举第 index+1 根火柴的放置情况，如果所有火柴都已经被放置，那么说明可以拼成正方形。

为了减少搜索量，需要对火柴长度从大到小进行排序。

### 

```
class Solution {
public:
    bool dfs(int index,vector&lt;int&gt;&amp; matchsticks,vector&lt;int&gt;&amp; edges,int len){
        //递归结束条件
        if(index==matchsticks.size())
        {
            return true;
        }
        for(int i=0;i&lt;edges.size();i++){
            edges[i]+=matchsticks[index];
            if(edges[i]&lt;=len &amp;&amp; dfs(index+1,matchsticks,edges,len)){
                return true;
            }
            edges[i]-=matchsticks[index];
        }
        return false;
    }
    bool makesquare(vector&lt;int&gt;&amp; matchsticks) {
        int index=0;
        int totallen=accumulate(matchsticks.begin(),matchsticks.end(),0);
        int len=totallen/4;
        if((totallen%4)!=0){
            return false;
        }
        vector&lt;int&gt; edges(4);
        //降序排序
        sort(matchsticks.begin(),matchsticks.end(),std::greater&lt;int&gt;());
        if(dfs(index,matchsticks,edges,len)){
            return true;
        }
        else{
            return false;
        }
    }
};
```

## 三、知识总结

### 1.C++ sort()排序函数用法详解

该函数专门用来对容器或普通数组中指定范围内的元素进行排序，排序规则默认以元素值的大小做升序排序，除此之外我们也可以选择标准库提供的其它排序规则（比如`std::greater&lt;T&gt;`降序排序规则），甚至还可以自定义排序规则。

sort() 函数是基于快速排序实现的

sort() 函数受到底层实现方式的限制，它仅适用于普通数组和部分类型的容器。换句话说，只有普通数组和具备以下条件的容器，才能使用 sort() 函数：
1. 容器支持的迭代器类型必须为随机访问迭代器。这意味着，sort() 只对 array、vector、deque 这 3 个容器提供支持。1. 如果对容器中指定区域的元素做默认升序排序，则元素类型必须支持`&lt;`小于运算符；同样，如果选用标准库提供的其它排序规则，元素类型也必须支持该规则底层实现所用的比较运算符；1. sort() 函数在实现排序时，需要交换容器中元素的存储位置。这种情况下，如果容器中存储的是自定义的类对象，则该类的内部必须提供移动构造函数和移动赋值运算符。
对于指定区域内值相等的元素，sort() 函数无法保证它们的相对位置不发生改变。

sort() 函数位于`&lt;algorithm&gt;`头文件中，因此在使用该函数前，程序中应包含如下语句：

```
#include &lt;algorithm&gt;
```

sort() 函数有 2 种用法，其语法格式分别为：

```
//对 [first, last) 区域内的元素做默认的升序排序
void sort (RandomAccessIterator first, RandomAccessIterator last);
//按照指定的 comp 排序规则，对 [first, last) 区域内的元素进行排序
void sort (RandomAccessIterator first, RandomAccessIterator last, Compare comp);
```

举例:

```
#include &lt;iostream&gt;     // std::cout
#include &lt;algorithm&gt;    // std::sort
#include &lt;vector&gt;       // std::vector
//以普通函数的方式实现自定义排序规则
bool mycomp(int i, int j) {
    return (i &lt; j);
}
//以函数对象的方式实现自定义排序规则
class mycomp2 {
public:
    bool operator() (int i, int j) {
        return (i &lt; j);
    }
};

int main() {
    std::vector&lt;int&gt; myvector{ 32, 71, 12, 45, 26, 80, 53, 33 };
    //调用第一种语法格式，对 32、71、12、45 进行排序
    std::sort(myvector.begin(), myvector.begin() + 4); //(12 32 45 71) 26 80 53 33
    //调用第二种语法格式，利用STL标准库提供的其它比较规则（比如 greater&lt;T&gt;）进行排序
    std::sort(myvector.begin(), myvector.begin() + 4, std::greater&lt;int&gt;()); //(71 45 32 12) 26 80 53 33
   
    //调用第二种语法格式，通过自定义比较规则进行排序
    std::sort(myvector.begin(), myvector.end(), mycomp2());//12 26 32 33 45 53 71 80
    //输出 myvector 容器中的元素
    for (std::vector&lt;int&gt;::iterator it = myvector.begin(); it != myvector.end(); ++it) {
        std::cout &lt;&lt; *it &lt;&lt; ' ';
    }
    return 0;
}
```

该函数实现排序的平均时间复杂度为`N*log2N`（其中 N 为指定区域 [first, last) 中 last 和 first 的距离）。

### 2.accumulate()函数

accumulate带有三个形参：头两个形参指定要累加的元素范围，第三个形参则是累加的初值。 accumulate函数将它的一个内部变量设置为指定的初始值，然后在此初值上累加输入范围内所有元素的值。accumulate算法返回累加的结果，其返回类型就是其第三个实参的类型。 可以使用accumulate把string型的vector容器中的元素连接起来：

```
string sum = accumulate(v.begin() , v.end() , string(" "));
```

但是对于自定义数据类型，我们就需要自己动手写一个回调函数来实现自定义数据的处理，然后让它作为accumulate()的第四个参数；

```
#include &lt;vector&gt;
#include &lt;string&gt;
using namespace std;
 
struct Grade
{
	string name;
	int grade;
};
 
int main()
{
	Grade subject[3] = {
		{ "English", 80 },
		{ "Biology", 70 },
		{ "History", 90 }
	};
 
	int sum = accumulate(subject, subject + 3, 0, [](int a, Grade b){return a + b.grade; });
	cout &lt;&lt; sum &lt;&lt; endl;
 
	system("pause");
	return 0;
}
```

## 四、总结

编写递归函数时，必须告诉他何时停止递归。

每个递归函数都有两部分：基线条件和递归条件。递归条件指的是函数调用自己，而基线条件则指函数不再调用自己，从而避免形成无限循环。


