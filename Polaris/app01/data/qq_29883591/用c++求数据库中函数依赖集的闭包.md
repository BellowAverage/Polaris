
--- 
title:  用c++求数据库中函数依赖集的闭包 
tags: []
categories: [] 

---
      由于数据库作业要求用程序求一个函数依赖集中属性集的闭包和此依赖集的闭包，便用c++写了这个程序，刚好在这分享给大家，代码写得丑，望大家勿喷。

首先我们将求闭包具体化，即建立在下面的规则下：

1. 由用户输入函数依赖，当用户输入End时，表示所有依赖都输入完毕。(即函数依赖是由用户自己定的，程序中不能假定某个具体的依赖)。

2. 函数依赖的形式是AB--&gt;C, A--&gt;BE这样的形式，为了简单起见，我们假定所有的属性都是用英文的大写字母表示，由A到Z。（提示，你可以让用户先输入依赖左边的属性，   然后再输入依赖右边的属性，用来表示A--&gt;B这样的形式）

3. 用户输入完毕所有的依赖后，显示“请输入属性集求闭包”的提示，当用户输入1个或者多个属性时，求出对应的闭包。（如，用户输入A，则显示A+的值， 用户输入AB则求   出AB+的值。显示完毕后，再次显示“请输入属性集求闭包”，让用户继续输入属性，直到用户输入END后程序结束。

    这样，在上述规则的约束下，我们便可以将求闭包的算法具体化了。

下面我先简述一下此算法的规则：

    在此算法中，我们会首先求出各个单一属性的闭包，这样的话，我们就得到了两组属性（泛化地说），将左边看成一组，将右边看成另一组，然后对左边的属性集进行排列组合，产生所有的可能情况，然后对左边的每个组合相对应的右边的属性的集合也进行排列组合，最后得出所有的函数依赖，也就是要求的函数依赖集的闭包。

当然，这样说的话可能会有点难懂，下面我用一个简短的例子进行解说：

例：A-&gt;B,B-&gt;C，求此函数依赖集的闭包

解：（1）首先求出各个单一属性的闭包：（A)+ = ABC，（B)+ = BC，（C)+ = C，其中（A)+表示属性A的闭包。

    （2）求出左边属性的排列组合并求出相对应右边属性的集合

      A：ABC， B：BC， C：C， AB：ABC， AC：ABC， BC：BC， ABC：ABC

     （3）对（2）中求出的组合中，再对右边的属性集合进行排列组合

      A：A，B，C，AB,BC,AC,ABC

      B：B,C,BC

      C:C

      AB:A，B，C，AB,BC,AC,ABC

      AC:A，B，C，AB,BC,AC,ABC

      BC:B,C,BC

      ABC:A，B，C，AB,BC,AC,ABC

      (4)只需要将（3）中的结果输出就好

      例如左边为B时，得到的是B-&gt;B,B-&gt;C,B-&gt;BC（在我们的程序中是将B-&gt;NULL这种类型保留了的，当然你也可以根据自己的需求选择需不需要输出这个）

闲话不多说了，下面直接上代码：

```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;string&gt;
#include&lt;set&gt;
#include&lt;algorithm&gt;
using namespace std;

//定义一个结构体，用于表示函数依赖
struct Node   
{
	string m_left;   //存放函数依赖的左边属性集
	string m_right;  //用于存放函数依赖集的右边属性集
	Node(const string &amp;left,const string &amp;right):m_left(left),m_right(right){}
};

//定义一个函数依赖集的类
class FunSet    
{
public:
	FunSet(vector&lt;Node&gt; s=vector&lt;Node&gt;()):m_set(s){}
	void pushFun(const Node &amp;n)
	{
		m_set.push_back(n);
	}
	string attrClosure(const string &amp;attr);
	void closure();
	bool contains(const string &amp;attrSet,const string attr);  
private:
	vector&lt;Node&gt; m_set;     //用于存放所有的函数依赖的集合
	void print(string attrs,int n,int sum,const string &amp;leftAttrs);
	void calculateAttrs(vector&lt;pair&lt;char,string&gt; &gt; attrClosures,int n);

};
/*
此函数是递归函数，用于将左边属性对应的右边属性集中的所有可能情况输出
*/
void FunSet::print(string attrs,int n,int sum,const string &amp;leftAttrs)
{
		
	if(n&gt;=sum)
	{
		cout &lt;&lt; leftAttrs &lt;&lt; "-&gt;";
		int num=0;
		for(int i=0;i&lt;n;i++)
		{
			if(attrs[i]!=NULL)
				cout &lt;&lt; attrs[i];
			else
				num++;
		}
		if(num==n)
			cout &lt;&lt; "NULL";
		cout &lt;&lt; endl;
		return ;
	}
	print(attrs,n+1,sum,leftAttrs);  //此时是attrs中下标为n处的值为真的属性
	attrs[n]=NULL;       //将attrs属性集中下标为n处的属性置为NULL
	print(attrs,n+1,sum,leftAttrs);  
}

/*
此递归函数用于将左边属性集的所有组合情况找出来
利用的规则是分别找出左边属性集的所有可能排列，在找出相对应的右边属性集的所有可能排列
此过程中用到了二进制位的思想，即将每个属性为看成要么选中，要么不选，不选时置为NULL，然后进行递归
*/
void FunSet::calculateAttrs(vector&lt;pair&lt;char,string&gt; &gt; attrClosures,int n)
{
	if(n&gt;=attrClosures.size())
	{
		int count=0;      //用于记录左边属性集中NULL的个数
		string leftAttrs;  //用于存放左边的属性
		string rightAttrs;  //用于存放左边属性的闭包
		for(int i=0;i&lt;n;i++)
		{
			if(attrClosures[i].first!=NULL)
				    leftAttrs+=attrClosures[i].first;      
			else
				count++;
			rightAttrs+=attrClosures[i].second;
		}
		if(count==n)
			return ;
		//下面三行代码用于取出rightAttrs中重复的属性
		sort(rightAttrs.begin(),rightAttrs.end());
		auto end_unique=unique(rightAttrs.begin(),rightAttrs.end());
		rightAttrs.erase(end_unique,rightAttrs.end());

		int num=rightAttrs.size();
		print(rightAttrs,0,num,leftAttrs);
		return ;
	}
	calculateAttrs(attrClosures,n+1);
	attrClosures[n].first=NULL;
	attrClosures[n].second=string();
	calculateAttrs(attrClosures,n+1);
}

/*
此函数用于判断attr中的所有字符是否出现在attrSet中，如果是则返回true，否则返回false
*/
bool FunSet::contains(const string &amp;attrSet,const string attr)
{
	bool result=true;
	for(int i=0;i&lt;attr.size();i++)
	{
		int num=attrSet.find(attr[i]);
		if(num&lt;0)
		{
			result=false;
			break;
		}
	}
	return result;
}
/*
此函数用于求属性集的闭包
*/
string FunSet::attrClosure(const string &amp;attr)
{
	int size=-1;
	string result=attr;      //将要求的属性放在结果集中
	while(attr.size()!=size)   //当发现属性的闭包不会再改变时，就说明已经求得结果了
	{
		size=result.size();
		for(int i=0;i&lt;m_set.size();i++)
		{
			bool flag=contains(result,m_set[i].m_left);   //判断函数依赖的左边是否在求得的闭包中
			if(flag)                                      //若在，则更新闭包，否则判断下一个
				result=result+m_set[i].m_right;
		}
	}
	sort(result.begin(),result.end());
	auto end_unique=unique(result.begin(),result.end());
	result.erase(end_unique,result.end());
	return result;
}

/*
此函数用于求函数依赖集的闭包
*/
void FunSet::closure()
{
	set&lt;char&gt; attrsSet;    //利用set集合中元素不会重复的规则过滤属性集中重复的属性
	
	//下面的for循环是遍历所有函数依赖中左边属性和右边属性以得到所有属性的一个集合
	for(int i=0;i&lt;m_set.size();i++)
	{
		int index=m_set[i].m_left.size();
		for(int j=0;j&lt;index;j++)
		{
			attrsSet.insert(m_set[i].m_left[j]);
		}
		index=m_set[i].m_right.size();
		for(int j=0;j&lt;index;j++)
		{
			attrsSet.insert(m_set[i].m_right[j]);
		}
	}
	vector&lt;pair&lt;char,string&gt; &gt; attrClosures;  //attrClosures用来存放各个单一属性对应的闭包
	for(auto it=attrsSet.begin();it!=attrsSet.end();++it)
	{
		string attr;
		attr=attr+*it;
		attrClosures.push_back(pair&lt;char,string&gt;(*it,attrClosure(attr)));
	}
	calculateAttrs(attrClosures,0);
}

int main()
{
	string left,right;
	FunSet funset;
	cout &lt;&lt; "输入函数依赖时，函数依赖的左边和右边用空格隔开,输入END结束" &lt;&lt; endl;
	while(true)
	{
		cout &lt;&lt; "请输入：" ;
		cin &gt;&gt; left;
		if(left=="END")
		   break;
		else
			cin &gt;&gt; right;
		funset.pushFun(Node(left,right));
	}
	string attrs;
	int choice;
	while(true)
	{
	    cout &lt;&lt; "请输入属性集求闭包：" &lt;&lt; endl;
		cin &gt;&gt; attrs;
		cout &lt;&lt; attrs &lt;&lt; "+:"&lt;&lt; endl;
		cout &lt;&lt; funset.attrClosure(attrs) &lt;&lt; endl;
		cout &lt;&lt; "是否继续求属性集的闭包？ 输入1代表继续，输入0待表结束" &lt;&lt; endl;
		cout &lt;&lt; "请输入您的选择：";
		while(true)
		{
		    cin &gt;&gt; choice;
			if(choice&lt;0||choice&gt;1)
			{
				cout &lt;&lt; "**********您的输入有误！*******" &lt;&lt; endl;
				cout &lt;&lt; "请重新输入：";
			}
			else 
				break;
		}
		if(choice==0)
			break;
	}
	cout &lt;&lt; "您输入的函数依赖的闭包F+是：" &lt;&lt; endl;
	funset.closure();
	return 0;
}

```



    

 

 

 

      
