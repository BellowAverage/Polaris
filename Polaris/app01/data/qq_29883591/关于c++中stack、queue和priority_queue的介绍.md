
--- 
title:  关于c++中stack、queue和priority_queue的介绍 
tags: []
categories: [] 

---
        在c++中除了一些顺序容器外，标准库中还定义了三个容器适配器：stack、queue和priority_queue。适配器是标准库中的一个通用概念。容器、迭代器和函数本质上都是适配器。本质上，一个适配器是一种机制，能使某种事物的行为看起来像另外一种事物一样。一个容器适配器接受一种已有的容器类型，使其行为看起来像一种不同的类型。例如，stack适配器接受一个顺序容器（除array和rorward_list外），并使其操作起来像一个stack一样。

下面是所有容器适配器都支持的操作和类型

size_type     一种类型，足以保存当前类型的最大对象的大小

value_type      元素类型

container_type    实现适配器的底层容器类型

A  a;           创建一个名为a的空适配器

A  a(c);      创建一个名为a的适配器，带有容器c的一个拷贝

关系运算符     每个适配器都支持所有关系运算符：==、!=、&lt;、&lt;=、&gt;、和&gt;=这些运算符返回底层容器的比较结果

a.empty()       若a包含容纳和元素，返回false，否则返回true 

a.size()           返回a中元素的个数

swap(a,b)      交换a和b的内容，a和b必须有相同类型，包括底层容器类型也比必须相同

a.swap(b)

对于适配器的构造有两种方式：一种是用默认构造函数创建一个空对象，另一种是接收一个容器作为参数进行拷贝初始化。

例如：deque&lt;int&gt;   myDeque;

            ............//假设经过一些操作后myDeque中已经有了一些元素

            stack&lt;int&gt;   myStack(myDeque);      // 将myDeque中的元素拷贝到myStack中

 默认情况下，stack和queue是基于deque实现的，priority_queue是在vector之上实现的。

当然也可以在创建一个适配器时通过将一个命名的顺序容器作为第二个类型参数，来重载默认容器类型。

例如：stack&lt;int,vector&lt;int&gt; &gt;   str_stk1;    //在vector上实现的空栈，也就是说此时的栈的数据存放是以vector为底层的

            stack&lt;int,vector&lt;int&gt; &gt;    str_stk2(vec)      //vec是一个存放了int型数据的一个vector容器，此时str_stk2对vec进行拷贝初始化的

 

上面是结合c++ primer中的相关解释进行一些小的铺垫，下面正式进入主题。

1、stack栈

     stack类型是定义在头文件&lt;stack&gt;中的一种数据结构，在使用时我们只需要将头文件包含进自己创建的cpp文件中即可

 定义一个栈：stack&lt;value_type&gt;   stk;     //value_type指代栈中元素类型，可以是int、string等

栈的操作如下：

stk.pop()       删除栈顶元素，但不返回栈顶的元素

stk.top()        返回栈顶的元素，但不会将栈顶元素弹出

push(item)       将item元素的副本压入栈顶，该元素通过拷贝或移动而来。

stk.emplace(arg)    将arg放置在stk中，作用相当于push

size()            返回栈中元素的个数

empty()        判断栈是否为空，若栈为空，返回false，否则返回true

swap(stk1)      将stk和stk1中元素互换，此操作并不会真正交换他们的元素，只是交换了两个容器的内部数据结构，可以用指针的思想类比理解

swap(stk1,stk2)      此函数是非成员版本的函数，功能和成员版本的swap相同

下面的程序是对stack的用法的一个展示：



```
int main()
{
	stack&lt;int&gt; stk1;    //定义一个空栈
	stack&lt;int&gt; stk2;
	stk1.push(2);       //向栈中添加元素
	stk1.push(9);
	stk1.emplace(3);
	stk1.emplace(39);
	stk2.push(3);
	stk2.push(4);
	stk2.swap(stk1);    //交换两个栈中的元素
	while(!stk1.empty())    //当栈不为空时，继续循环
	{
		cout &lt;&lt; stk1.top() &lt;&lt; endl;    //输出栈顶元素
		stk1.pop();        //将栈顶元素弹出
	}
	while(stk2.size())     //当栈中元素个数不为0时，继续循环
	{
		cout &lt;&lt; stk2.top() &lt;&lt; endl;
		stk2.pop();
	}
	return 0;

}
```



 

 1、queue队列  

       queue队列是c++标准库中一个重要的数据结构，其主要特性就是先进先出，就相当于我们日常生活中的排队买东西，先到的人先被服务，后到的人要排到队尾。

       首先queue定义在头文件&lt;queue&gt;中，使用时要将头文件包含进去。

定义一个队列：queue&lt;value_type&gt;    q;

q.pop()      删除queue的队头元素

q.front()    返回队列的队头元素，但不删除该元素

q.back()    返回队列的队尾元素，但不删除该元素

q.push(arg)      将元素arg插入到队列的队尾

q.emplace(arg)    将元素arg放置到队列的尾部，作用和push一样

q.size()     返回队列中元素的个数

q.empty()    当队列为空时返回true，否则返回false

q.swap(q1)      交换q和q1中的元素，方法和stack中一样，并不会真正使用拷贝形式进行交换，只是交换底层的数据结构

swap(q,q1)      非成员函数，和成员函数swap一样

下面的程序是对queue的一个小测试：



```
#include&lt;iostream&gt;
using namespace std;
#include&lt;queue&gt;

int main()
{
	queue&lt;int&gt; q;      //定义一个空的队列
	for(int i=0;i&lt;10;i++)
	{
	     q.push(i);       //将i插入到队尾
	}
	q.emplace(32);     //将32放置到队尾
	cout &lt;&lt; q.size() &lt;&lt; endl;    //输出队列中元素的个数
	while(!q.empty())     //当队列不为空时，继续循环
	{
		cout &lt;&lt; q.front() &lt;&lt; endl;    //输出队列中的首元素
		q.pop();      //将元素从队尾删除
	}
	return 0;
}
```



3、priority_queue优先队列

      作为队列的一个延伸，优先队列同样是一种很有用的数据结构，它包含在头文件&lt;queue&gt;中。

      优先队列是一种重要的数据结构，它是由二项队列编写而成的，可以以log（n）的效率查找一个队列中最大值或最小值（最大值和最小值是由你选择创建的优先队列的性质决定的），这在很多场合可以派上很大的用处，例如prim算法如果结合优先队列可以产生出很好的效果。

priority_queue的模板生命是带有三个参数的：priority_queue&lt;type,container,function&gt;，

其中，type是数据的类型，container为实现优先队列的底层容器，function为元素间的比较方式，其中container要求必须是数组形式实现的容器，如vector，deque，而不能是

list。在c++标准库中，默认情况下是以vector为容器，以operator&lt;为比较方式，所以在只使用第一个参数时，优先队列默认是一个最大堆，每次输出的堆顶元素是此时堆中的最大元素。

定义一个默认的优先队列：priority_queue&lt;int&gt;   temp;



temp.pop()      删除priority_queue的队头元素

temp.top()       返回priority_queue优先队列中队头元素，但不删除该元素

temp.push(arg)      将元素arg插入到优先队列中

temp.emplace(arg)    将元素arg放置到优先队列中，作用和push一样

temp.size()     返回优先队列中元素的个数

temp.empty()    当优先队列为空时返回true，否则返回false

temp.swap(temp1)      交换temp和temp1中的元素,并不会真正使用拷贝形式进行交换，只是交换底层的数据结构

swap(temp,temp1)      非成员函数，和成员函数swap一样

下面是一个使用系统提供的数据类型的优先队列的例子：

此程序使用默认参数构造一个大顶堆的例子



```
#include&lt;iostream&gt;
#include&lt;random&gt;
using namespace std;
#include&lt;queue&gt;

int main()
{
	priority_queue&lt;int,vector&lt;int&gt;,greater&lt;int&gt; &gt; myQueue;   //构造一个空的优先队列,此优先队列是一个小顶堆
	uniform_int_distribution&lt;unsigned&gt; u(0,100);    //用于在0到100之间生成均匀分布的随机数
	default_random_engine e;     //定义一个随机数引擎
	int value;
	for(int i=0;i&lt;10;i++)
	{
		value=u(e);
		cout &lt;&lt; value &lt;&lt; " ";
		myQueue.push(value);    //将生成的随机数放入到队列中
	}
	cout &lt;&lt; endl;
	while(!myQueue.empty())    //此循环将会按照升序输出优先队列中的元素
	{
		cout &lt;&lt; myQueue.top() &lt;&lt; " ";    //输出队列中最小的元素
		myQueue.pop();
	}
	cout &lt;&lt; endl;
	return 0;
}
```

如果想创造一个小顶堆，则需要将三个参数都带进去

只需将上面的优先队列的声明改变一下便可得到以下程序 

```
#include&lt;queue&gt;

int main()
{
	priority_queue&lt;int&gt; myQueue;   //构造一个空的优先队列（此优先队列默认为大顶堆）
	uniform_int_distribution&lt;unsigned&gt; u(0,100);    //用于在0到100之间生成均匀分布的随机数
	default_random_engine e;     //定义一个随机数引擎
	int value;
	for(int i=0;i&lt;10;i++)
	{
		value=u(e);
		cout &lt;&lt; value &lt;&lt; " ";
		myQueue.push(value);    //将生成的随机数放入到队列中
	}
	cout &lt;&lt; endl;
	while(!myQueue.empty())    //此循环将会按照降序输出优先队列中的元素
	{
		cout &lt;&lt; myQueue.top() &lt;&lt; " ";    //输出队列中最大的元素
		myQueue.pop();
	}
	cout &lt;&lt; endl;
	return 0;
}
```

下面是重载&lt;、&gt;的一个简单的例子：

```
#include&lt;iostream&gt;
#include&lt;random&gt;
using namespace std;
#include&lt;queue&gt;

class node
{
public:
	node(int x=0,int y=0):m_x(x),m_y(y){}
	friend bool operator&lt;(const node &amp;n1,const node &amp;n2)    //重载&lt;运算符是用于大顶堆
	{
		return n1.m_x&lt;n2.m_x;
	}
	friend bool operator&gt;(const node &amp;n1,const node &amp;n2)    //重载&gt;运算符是用于小顶堆
	{
		return n1.m_x&gt;n2.m_x;
	}
	friend ostream &amp;operator&lt;&lt;(ostream &amp;out,const node &amp;n)
	{
		cout &lt;&lt; "(" &lt;&lt; n.m_x &lt;&lt; ","&lt;&lt; n.m_y &lt;&lt; ")";
		return out;
	}
private:
	int m_x,m_y;
};
int main()
{
	priority_queue&lt;node,vector&lt;node&gt;,greater&lt;node&gt; &gt; myQueue;
	uniform_int_distribution&lt;unsigned&gt; u(0,100);
	default_random_engine e;
	int value1,value2;
	for(int i=0;i&lt;10;i++)
	{
		value1=u(e);
		value2=u(e);
		cout &lt;&lt; "(" &lt;&lt; value1 &lt;&lt; ","&lt;&lt; value2 &lt;&lt; ")";
		myQueue.push(node(value1,value2));
	}
	cout &lt;&lt; endl;
	while(!myQueue.empty())
	{
		cout &lt;&lt; myQueue.top() &lt;&lt; " ";
		myQueue.pop();
	}
	cout &lt;&lt; endl;
	return 0;
}
```

下面修改一下上面的例子，展示一个仿写函数的例子：



```
#include&lt;iostream&gt;
#include&lt;random&gt;
using namespace std;
#include&lt;queue&gt;

class node
{
public:
	node(int x = 0, int y = 0) :m_x(x), m_y(y) {}
	int get_x()const { return m_x; }
	friend ostream &amp;operator&lt;&lt;(ostream &amp;out, const node &amp;n)
	{
		cout &lt;&lt; "(" &lt;&lt; n.m_x &lt;&lt; "," &lt;&lt; n.m_y &lt;&lt; ")";
		return out;
	}
private:
	int m_x, m_y;
};
struct cmp     //定义一个函数对象
{
	bool operator()(const node &amp;n1, const node &amp;n2)  //重载函数运算符()
	{
		return n1.get_x()&gt;n2.get_x();
	}
};
int main()
{
	priority_queue&lt;node, vector&lt;node&gt;, cmp&gt; myQueue;
	uniform_int_distribution&lt;unsigned&gt; u(0, 100);
	default_random_engine e;
	int value1, value2;
	for (int i = 0; i&lt;10; i++)
	{
		value1 = u(e);
		value2 = u(e);
		cout &lt;&lt; "(" &lt;&lt; value1 &lt;&lt; "," &lt;&lt; value2 &lt;&lt; ")";
		myQueue.push(node(value1, value2));
	}
	cout &lt;&lt; endl;
	while (!myQueue.empty())
	{
		cout &lt;&lt; myQueue.top() &lt;&lt; " ";
		myQueue.pop();
	}
	cout &lt;&lt; endl;
	return 0;
}
```



上面的例子是将优先队列中的第三个参数用一个函数对象替代，以作为优先队列中数据比较的依据。

下面补充说明一下函数对象的知识：

      在c++中，可以像对待其他运算符一样对待函数调用运算符()；这个运算符也可以重载。()运算符能够返回任何类型，可以使用任何数量的参数，但和赋值运算符一样，该运算符只能重载为成员函数。包含函数调用运算符定义的对象称为函数对象。函数对象也是对象，只是它们的行为表现得像函数而已。当调用函数对象时，其参数是函数调用运算符的参数。

    




