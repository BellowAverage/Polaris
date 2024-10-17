
--- 
title:  c++中sort等算法中比较操作的规则 
tags: []
categories: [] 

---
对于c++中，标准库中提供的算法很多，这些算法（如sort等）都会有自己默认的对关键字的处理规则，这些都是适用于关键字符合要求的情况，而如果我们待处理的关键字是自己自定义的类的时候，这个时候就需要我们自己定义其中的处理规则，下面以sort为例：

对于sort这种排序的算法，c++中默认的比较操作是&lt;运算符，用来处理非降序的排序要求。这些算法中提供的操作必须在关键字类型上定义一个严格弱序。可以将严格所需看做“小于等于”，虽然实际上定义的操作可能是一个复杂的函数，但是无论如何，这个比较函数必须具备如下的基本性质：

（1）两个关键字不能同时“小于等于”对方；如果k1“小于等于”k2，那么k2决不能“小于等于”k1。

（2）如果k1“小于等于”k2，且k2“小于等于”k3，那么k1必须“小于等于”k3.

（3）如果存在两个关键字，任何一个都不“小于等于”另一个，那我们称这两个关键字是“等价的”。如果k1“等价于”k2，且k2“等价于”k3，那么k1必须“等价于”k3。

在上面的规则中提到的“小于等于”是严格弱序的说法，千万不要和我们平时使用的“&lt;=”符号混淆了，这是一个很大的误区，下面举个例子。



```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;algorithm&gt;
#include&lt;string&gt;
using namespace std;

class Node
{
public:
	Node(int score,int age,string name):m_score(score),m_age(age),m_name(name){}
	int getScore() { return m_score;  }
	int getScore() const { return m_score; }
	friend ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node);
private:
	int m_score;
	int m_age;
	string m_name;
};
ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node)
{
	out &lt;&lt; "score:" &lt;&lt; node.m_score &lt;&lt; "	age:" &lt;&lt; node.m_age &lt;&lt; "		" 
		&lt;&lt; node.m_name;
	return out;
}
bool compare(const Node &amp;node1, const Node &amp;node2)
{
	return node1.getScore() &lt; node2.getScore();
}

int main()
{
	Node node1 = { 32,30,"liu" };
	Node node2 = { 90,23,"hu" };
	Node node3 = { 67,32,"ki" };
	Node node4 = { 78,45,"arr" };
	vector&lt;Node&gt; vec;
	vec.push_back(node1);
	vec.push_back(node2);
	vec.push_back(node3);
	vec.push_back(node4);
	sort(vec.begin(), vec.end(), compare);
	for (auto itr = vec.begin(); itr != vec.end(); itr++)
	{
		cout &lt;&lt; *itr &lt;&lt; endl;
	}
	return 0;
}
```



检验如下：

（1）不存在数k1，k2，满足k1&lt;k2,k2&lt;k1，这两个式子中只有一个可以成立，满足条件1

（2）对于数k1，k2，k3而言，当k1&lt;k2，k2&lt;k3时，则必有k1&lt;k3，满足条件2

（3）对于条件3，显而易见任何对于数k1，k2而言，当k1和k2相等的时候，k1&lt;k2和k2&lt;k1都是不成立，k1和k2是等价的，满足条件3。

如果我们将compare函数中的“&lt;”符号改成“&lt;=”号的时候，如下所示：

```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;algorithm&gt;
#include&lt;string&gt;
using namespace std;

class Node
{
public:
	Node(int score,int age,string name):m_score(score),m_age(age),m_name(name){}
	int getScore() { return m_score;  }
	int getScore() const { return m_score; }
	friend ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node);
private:
	int m_score;
	int m_age;
	string m_name;
};
ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node)
{
	out &lt;&lt; "score:" &lt;&lt; node.m_score &lt;&lt; "	age:" &lt;&lt; node.m_age &lt;&lt; "		" 
		&lt;&lt; node.m_name;
	return out;
}
bool compare(const Node &amp;node1, const Node &amp;node2)
{
	return node1.getScore() &lt;= node2.getScore();
}

int main()
{
	Node node1 = { 32,30,"liu" };
	Node node2 = { 90,23,"hu" };
	Node node3 = { 67,32,"ki" };
	Node node4 = { 78,45,"arr" };
	vector&lt;Node&gt; vec;
	vec.push_back(node1);
	vec.push_back(node2);
	vec.push_back(node3);
	vec.push_back(node4);

	sort(vec.begin(), vec.end(), compare);
	for (auto itr = vec.begin(); itr != vec.end(); itr++)
	{
		cout &lt;&lt; *itr &lt;&lt; endl;
	}
	return 0;
}
```



检验如下：

（1）当k1&lt;=k2的时候，k2&lt;=k1是成立的，显然不符合我们的要求1。



（2）对于数k1，k2，k3而言，当k1&lt;=k2，k2&lt;=k3时，则必有k1&lt;=k3，满足条件2

（3）对于条件3，显而易见任何对于数k1，k2而言，k1&lt;=k2和k2&lt;=k1都是成立的，显然条件3也不符合。

从上面的检验可以发现什么问题？是不是有种恍然大悟的感觉，一切的焦点都落在了“=”上，这也就可以解释为什么我们上面的程序对于“&lt;=”同样没有出错，这不是说用“&lt;=”没有错误，而是我们的测试数据没能检验出这个错误，这是因为在我们的数据中没有分数相等的数据，那就永远不会触发这个错误，现在让我们一起见证这个问题，很简单，我们插入一个分数相同的数据，代码如下：



```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;algorithm&gt;
#include&lt;string&gt;
using namespace std;

class Node
{
public:
	Node(int score,int age,string name):m_score(score),m_age(age),m_name(name){}
	int getScore() { return m_score;  }
	int getScore() const { return m_score; }
	friend ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node);
private:
	int m_score;
	int m_age;
	string m_name;
};
ostream &amp;operator&lt;&lt;(ostream &amp;out, const Node &amp;node)
{
	out &lt;&lt; "score:" &lt;&lt; node.m_score &lt;&lt; "	age:" &lt;&lt; node.m_age &lt;&lt; "		" 
		&lt;&lt; node.m_name;
	return out;
}
bool compare(const Node &amp;node1, const Node &amp;node2)
{
	return node1.getScore() &lt;= node2.getScore();
}

int main()
{
	Node node1 = { 32,30,"liu" };
	Node node2 = { 90,23,"hu" };
	Node node3 = { 67,32,"ki" };
	Node node4 = { 78,45,"arr" };
	Node node5 = { 78,45,"dkk" };
	vector&lt;Node&gt; vec;
	vec.push_back(node1);
	vec.push_back(node2);
	vec.push_back(node3);
	vec.push_back(node4);

	sort(vec.begin(), vec.end(), compare);
	for (auto itr = vec.begin(); itr != vec.end(); itr++)
	{
		cout &lt;&lt; *itr &lt;&lt; endl;
	}
	return 0;
}
```



                                   <img src="https://img-blog.csdn.net/20170405232606057?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">

开个玩笑啊，写了这么多文字，给大家养养眼。

        下面是真正的结果：

<img src="https://img-blog.csdn.net/20170405232706535?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">

这里面提示的是invalid comparator，意思是不合法的比较符，说明我们的“&lt;=”是不合法的，这也正是我们平时编程时比较容易忽略和犯错的地方，特此和大家分享一下。  

 
