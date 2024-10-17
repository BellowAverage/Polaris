
--- 
title:  数据结构与算法（c++）--拓扑排序 
tags: []
categories: [] 

---
        这次来说一下拓扑排序的东西，仍是基于自己看的资料进行整理的（《数据结构与算法分析c++描述》这本书真的好，强烈推荐）。

        拓扑排序是对有向无环图的顶点的一种排序，它使得如果存在一条从Vi到Vj的路径，那么在排序的时候Vj将会出现在Vi的后面。举个例子说，对于有向边（Vi，Vj）而言，在排序的时候，无论如何进行排序选择，最终Vi必定出现在Vj的前面，所以说，拓扑排序的图必须是无环图，试想一下，如果存在一个环的话，那么久必定会出现两个顶点v和w，v先于w的同时w又先于v，这肯定是不可能的。

        下面举一个例子，如下图所示：

<img src="https://img-blog.csdn.net/20170416170409111?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 

        对于上图所示的的有向无环图中，v1,v2,v5,v4,v3,v7,v6和v1,v2,v5,v4,v7,v3,v6都是拓扑排序。由此可以看出，排序不必是唯一的，任何合理的排序都是可以的。

一个简单的求拓扑排序的算法是先找到任意一个没有入边（没有入边的意思是这个顶点没有其他的顶点指向它，即没有指向它的边存在）的顶点，然后显示出该顶点，并将它和它的边一起从图中删除。然后，对图中的其余任何部分应用同样的方法处理。

书上提供了一个简单的伪代码，如下：



```
void Graph::topsort()
{
	for(int counter=0;counter&lt;NUM_VERTICES;counter++)
	{
		Vertex v=findNewVertexOfIndegreeZero();
		if(v==NOT_A_VERTEX)
		{
			throw CycleFoundException();
		}
		v.topNum=counter;
		for each vertex w adjacent to v
			w.indegree--;
	}
}
```



下面给出一个处理的代码：



```
#include&lt;iostream&gt;
using namespace std;
#include&lt;vector&gt;
#include&lt;string&gt;
#include&lt;list&gt;
#include&lt;queue&gt;
#include&lt;climits&gt;
#include&lt;algorithm&gt;

template &lt;typename vertexNametype,typename weight&gt;
class ALGraph
{
private:
	template &lt;typename weight&gt;
	struct Edge
	{
		int nDestVertex;   //邻接顶点编号
		weight edgeWeight;  //边权重
		Edge *pNextEdge;   //下一条边
		Edge(int d,weight w,Edge&lt;weight&gt; *p=NULL):nDestVertex(d),edgeWeight(w),pNextEdge(p){}
	};
	template &lt;typename vertexNametype,typename weight&gt;
	struct Vertex
	{
		vertexNametype vertexName;   //顶点名
		Edge&lt;weight&gt; *pAdjEdges;   //邻接边链表
		Vertex( const vertexNametype &amp;name=vertexNametype(),Edge&lt;weight&gt; *p=NULL):vertexName(name),pAdjEdges(p){}
	};
public:
	explicit ALGraph():m_vertexArray(NULL){}
	~ALGraph()
	{
		for(auto it=m_vertexArray.begin();it!=m_vertexArray.end();++it)
		{
			Edge&lt;weight&gt; *p=it-&gt;pAdjEdges;
			while(NULL!=p)
			{
				it-&gt;pAdjEdges=p-&gt;pNextEdge;
				delete p;
				p=it-&gt;pAdjEdges;
			}
		}
		if(!m_vertexArray.empty())
			m_vertexArray.clear();
	}
	bool insertAVertex(const vertexNametype &amp;vertexName)  //插入节点
	{
		int index=getVertexIndex(vertexName);
		if(-1!=index)
		{
			cerr &lt;&lt; "点" &lt;&lt; vertexName &lt;&lt; "已经存在" &lt;&lt; endl;
			return false;
		}
		Vertex&lt;vertexNametype,weight&gt; vertexInstance(vertexName);
		m_vertexArray.push_back(vertexInstance);
		return true;
	}
	bool insertAEdge(const vertexNametype &amp;vertexName1,const vertexNametype &amp;vertexName2,const weight &amp;edgeWeight=1)  //插入边
	{
		int index1=getVertexIndex(vertexName1);
		if(-1==index1)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName1 &lt;&lt; endl;
			return false;
		}
		int index2=getVertexIndex(vertexName2);
		if(-1==index2)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName2 &lt;&lt; endl;
			return false;
		}
		Edge&lt;weight&gt; *p=m_vertexArray[index1].pAdjEdges;
		while(p!=NULL&amp;&amp;p-&gt;nDestVertex!=index2)
		{
			p=p-&gt;pNextEdge;
		}
		if(NULL==p)
		{
			p=new Edge&lt;weight&gt;(index2,edgeWeight,m_vertexArray[index1].pAdjEdges); 
			m_vertexArray[index1].pAdjEdges=p;     //将p插入到链表开始处
			return true; 
		}
		if(p-&gt;nDestVertex==index2)
		{
			Edge&lt;weight&gt; *q=p;
			p=new Edge&lt;weight&gt;(index2,edgeWeight,q-&gt;pNextEdge);
			q-&gt;pNextEdge=p;
			return true;
		}
		return false;
	}
	bool edgeExist(const vertexNametype &amp;vertexName1,const vertexNametype &amp;vertexName2) const  //判断便是否存在
	{
		int index1=getVertexIndex(vertexName1);
		if(-1==index1)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName1 &lt;&lt; endl;
			return false;
		}
		int index2=getVertexIndex(vertexName2);
		if(-1==index2)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName2 &lt;&lt; endl;
			return false;
		}
		Edge&lt;weight&gt; *p=m_vertexArray[index1].pAdjEdges;
		while(p!=NULL&amp;&amp;p-&gt;nDestVertex!=index2)
		{
			p=p-&gt;pNextEdge;
		}
		if(NULL=p)
		{
			cerr &lt;&lt; "不存在" &lt;&lt; endl;
			return false;
		}
		if(p-&gt;nDestVertex==index2)
		{
			cout &lt;&lt; "存在" &lt;&lt; endl;
			cout &lt;&lt; vertexName1 &lt;&lt; "：" ;
			while(p!=NULL&amp;&amp;p-&gt;nDestVertex==index2)
			{
				cout &lt;&lt; "(" &lt;&lt; vertexName1 &lt;&lt; "，" &lt;&lt; vertexName2 &lt;&lt; "，" &lt;&lt; p-&gt;edgeWeight &lt;&lt; ")" ;
				p=p-&gt;pNextEdge;
			}
			cout &lt;&lt; endl;
			return true;
		}
	}
	void printVertexAdjEdges(const vertexNametype &amp;vertexName) const     //输出邻接表
	{
		int index=getVertexIndex(vertexName);
		if(-1==index)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName &lt;&lt; endl;
			return ;
		}
		Edge&lt;weight&gt; *p=m_vertexArray[index].pAdjEdges;
		cout &lt;&lt; vertexName &lt;&lt; "：" ;
		while(p!=NULL)
		{
			cout &lt;&lt; "(" &lt;&lt; vertexName &lt;&lt; "，" &lt;&lt; getData(p-&gt;pNextEdge) &lt;&lt; p-&gt;edgeWeight &lt;&lt; ")" ;
		}
		cout &lt;&lt; endl;
	}
	bool removeAEdge(const vertexNametype &amp;vertexName1,const vertexNametype &amp;vertexName2,const weight &amp;edgeWeight)     //删除边
	{
		int index1=getVertexIndex(vertexName1);
		if(-1==index1)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName1 &lt;&lt; endl;
			return false;
		}
		int index2=getVertexIndex(vertexName2);
		if(-1==index2)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName2 &lt;&lt; endl;
			return false;
		}
		Edge&lt;weight&gt; *p=m_vertexArray[index1].pAdjEdges;
		Edge&lt;weight&gt; *q=NULL;
		while(p!=NULL&amp;&amp;p-&gt;nDestVertex!=index2)
		{
			q=p;     //用q记下将要删除的边的前面的边
			p=p-&gt;pNextEdge;
		}
		if(NULL==p)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName1 &lt;&lt; "到" &lt;&lt; vertexName2 &lt;&lt; "的点" &lt;&lt; endl;
			return false;
		}
		while(p!=NULL&amp;&amp;edgeWeight!=p-&gt;edgeWeight&amp;&amp;p-&gt;nDestVertex==index2)
		{
			q=p;
			p=p-&gt;pNextEdge;
		}
		if(p-&gt;nDestVertex!=index2)
		{
			cerr &lt;&lt; "不存在点" &lt;&lt; vertexName1 &lt;&lt; "到" &lt;&lt; vertexName2 &lt;&lt; "的点" &lt;&lt; endl;
			return false;
		}
		if(NULL==q)
			m_vertexArray[index1].pAdjEdges=p-&gt;pNextEdge;
		else
		    q-&gt;pNextEdge=p-&gt;pNextEdge;
		delete p;
		return true;
	}
	int getVertexIndex(const vertexNametype &amp;vertexName) const  //获取顶点索引
	{
		for(int i=0;i&lt;m_vertexArray.size();i++)
		{
			if(vertexName==getData(i))
				return i;
		}
		return -1;

	}
	int getVertexNumber() const  //获取顶点数
	{
		return m_vertexArray.size();
	}

	friend ostream &amp;operator&lt;&lt;(ostream &amp;out,const ALGraph&lt;vertexNametype,weight&gt; &amp;graphInstance)
	{
		int vertexNum=graphInstance.getVertexNumber();
		out &lt;&lt; "这个图有" &lt;&lt; vertexNum &lt;&lt; "个点" &lt;&lt; endl;
		for(int i=0;i&lt;vertexNum;i++)
		{
			vertexNametype vertexName=graphInstance.getData(i);
			out &lt;&lt; vertexName &lt;&lt; "：" ;
			Edge&lt;weight&gt; *p=graphInstance.m_vertexArray[i].pAdjEdges;
			while(NULL!=p)
			{
			    out &lt;&lt; "(" &lt;&lt; vertexName &lt;&lt; "," &lt;&lt; graphInstance.getData(p-&gt;nDestVertex) &lt;&lt; "," &lt;&lt; p-&gt;edgeWeight &lt;&lt; ")";
				p=p-&gt;pNextEdge;
			}
			out &lt;&lt; endl;
		}
		return out;
	}

	 list&lt;vertexNametype&gt; topologicialSort() const
	 {
		 list&lt;vertexNametype&gt; vertexList;
		 vector&lt;int&gt; indegree(m_vertexArray.size(),0);
		 queue&lt;Vertex&lt;vertexNametype,weight&gt; &gt; zeroIndegree;
		 for(int i=0;i&lt;m_vertexArray.size();i++)
		 {
			 Edge&lt;weight&gt; *p=m_vertexArray[i].pAdjEdges;
			 while(NULL!=p)
			 {
				 ++indegree[p-&gt;nDestVertex];
				 p=p-&gt;pNextEdge;
			 }
		 }
		 for(int i=0;i&lt;m_vertexArray.size();i++)
		 {
			 if(0==indegree[i])
				 zeroIndegree.push(m_vertexArray[i]);
		 }
		 while(!zeroIndegree.empty())
		 {
			   Vertex&lt;vertexNametype,weight&gt; v=zeroIndegree.front();
			   zeroIndegree.pop();
			   vertexList.push_back(v.vertexName);
			   Edge&lt;weight&gt; *p=v.pAdjEdges;
			   while(NULL!=p)
			   {
				   if(--indegree[p-&gt;nDestVertex]==0)
					   zeroIndegree.push(m_vertexArray[p-&gt;nDestVertex]);
				   p=p-&gt;pNextEdge;
			   }
		 }
		 if(vertexList.size()&lt;m_vertexArray.size())
		 {
			 cerr &lt;&lt; "此图有环，无法进行拓扑排序" &lt;&lt; endl;
			 exit(EXIT_FAILURE);
		 }
		 return vertexList;
	 }

	 void printPath(const vertexNametype &amp;beginVertex,const vertexNametype &amp;endVertex,const vector&lt;int&gt; prev)
	 {
		 int beginIndex=getVertexIndex(beginVertex);
		 int endIndex=getVertexIndex(endVertex);
		 printPath(beginIndex,endIndex,prev);
	 }


private:
	vector&lt;Vertex&lt;vertexNametype,weight&gt; &gt; m_vertexArray;
	vertexNametype getData(int index) const  //取顶获点名
	{
		return m_vertexArray[index].vertexName;
	}
	void printPath(int beginIndex,int endIndex,const vector&lt;int&gt; prev)
	{
		 if(beginIndex!=endIndex)
			 printPath(beginIndex,prev[endIndex],prev);
		 cout &lt;&lt; m_vertexArray[endIndex].vertexName &lt;&lt; " " ;
	}
	Edge&lt;weight&gt; *getEdge(int begin,int end)
	{
		Edge&lt;weight&gt; *p=m_vertexArray[begin].pAdjEdges;
		while(NULL!=p)
		{
			if(p-&gt;nDestVertex==end)
				break;
			p=p-&gt;pNextEdge;
		}
		return p;
	}
};

int main()
{
	ALGraph&lt;string,int&gt; graph;
	graph.insertAVertex("v1");
	graph.insertAVertex("v2");
	graph.insertAVertex("v3");
	graph.insertAVertex("v4");
	graph.insertAVertex("v5");
	graph.insertAVertex("v6");
	graph.insertAVertex("v7");
	graph.insertAEdge("v1","v2");
	graph.insertAEdge("v1","v4");
	graph.insertAEdge("v1","v3");
	graph.insertAEdge("v2","v4");
	graph.insertAEdge("v2","v5");
	graph.insertAEdge("v3","v6");
	graph.insertAEdge("v4","v7");
	graph.insertAEdge("v4","v6");
	graph.insertAEdge("v4","v3");
	graph.insertAEdge("v5","v7");
	graph.insertAEdge("v7","v6");
	cout &lt;&lt; graph &lt;&lt; endl;
	list&lt;string&gt; result=graph.topologicialSort();
	cout &lt;&lt; "拓扑排序的结果为："&lt;&lt; endl;
	for(auto it=result.begin();it!=result.end();++it)
		cout &lt;&lt; *it &lt;&lt; " " ;
	cout &lt;&lt; endl;
	return 0;
}


```



        对于上面的代码可能看起来会有点多啊，其实我们在平时解题的时候，很多情况下不会用到这么复杂的，原因之一就是类的运用啊，因为一旦使用了类，不可避免的就会产生很多的代码，尤其是在进行各种方法之间的优化的时候。在这个程序中，我使用了邻接表的方法对图进行处理的，在很多情况下也可以使用矩阵的方法进行处理，这两种方法各有优劣，分别对应于稀疏和稠密类型的图很有效果，这里因为是基于c++的嘛，就给出了一个运用类进行构造的例子，并且采用邻接表进行，相对来说矩阵方法更加简单易写，这里就不给出了。

        至于代码量而言，其实如果仅仅是写这一个算法的话，确实是有点小题大做了，毕竟就一个那么简答的算法实现，没有必要搞个300多行出来，太吓人了吧，其实这是为了其它算法铺路的，在后续的博客中会看到，这些都是通用的东西，所以这个类模型可以把很多种算法整合到一起，而共用很多的代码，后面会继续看到。

        好了，这次就这么多了。 <img src="https://img-blog.csdn.net/20170416192730937?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt=""> 
