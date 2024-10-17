
--- 
title:  数据结构与算法（c++）--prim算法 
tags: []
categories: [] 

---
        刚好这次又遇到了prim算法，就做了下整理（可以参考《数据结构与算法分析c++描述》这本书，个人而言，很经典），并把以前写的代码也整理了一下，做下分享，同时也加深下自己的理解。

        prim算法是解决最小生成树问题的一个很好的算法。此算法是是将点集合中的点一步步加到树中，在每一步中，都要把一个节点当作根本并往上加边，这样也就把相关联的顶点增加到树上了。这样说有点枯燥和难以理解，下面借用一个例子进行详细讲解：

（1）如下图所示，是一个无向图，所有点的点集为S={v1,v2,v3,v4,v5,v6,v7}，带加入点的集合G={}：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410200623875?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（2）首先，我们将这个图的所有边先隐藏掉，这里我们选择点“v1”作为起点，此时点集G为{v1}，接下来的规则是在后续的步骤中，在G中的点和S-G中的点的边中选择最短的 边添加进去，此时情况如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410200708305?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（3）在“v1”的所有邻接点中找到路径长度最短的一个，即“v4”，此时两点点长度为1，将“v1”和“v4”连接起来，此时点集G为{v1，v4}，如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410200937161?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（4）在点集{v1，v4}中找到与v1、v4临接的点中边的长度最短的一个，即点v2（其实v4也是可以的，这里我们就选择v2），此时点集G为{v1，v2，v4}，如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410201330806?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（5）按照（2）中提到的规则应该将点v3添加到G中，此时G为{v1,v2,v3,v4}，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410201951363?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（6）此时选择将点v7添加到G中，则G={v1,v2,v3,v4,v7}，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410202258915?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（7）此时选择将点v6添加到G中，则G={v1,v2,v3,v4,v6,v7}，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410202049130?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（8）最后将点v5添加到G中，则G={v1,v2,v3,v4,v5,v6,v7}，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170410202458917?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

        从上面的示例中可以可以看出，在prim算法中，我们可以对每一个顶点保留值dv和Pv以及一个指标，表示该顶点是known还是unknown。在这里，dv是连接到已知顶点的最短边的权，则Pv则是导致dv改变的最后的顶点。在每个阶段，prim算法将会选择一个顶点v，它在所有的unknown顶点中具有最小的dv，同时算法将声明s（s是与v相连的这个拥有最小dv的另一个点，注意这个点s一定是known的）到v的最短路径是known的。在这个顶点v被选择之后，对于每一个与v邻接的且是unknown的点w，dw=min(dw,Cw,v)。其中Cw,v代表此时点w和v直接的距离。

        对于上面的例子，下面我们用表来刻画相应的转化状态：

（1）表的初始状态如下：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411222121237?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（2）选取点v1，同时更新v2、v3、v4，结果如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411222338547?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（3）通过比较可知，此时v4的dv最小，故选取点v4，同时更新与v4邻接的点（其中v1除外，因为v1已经是known），在这里主要需要注意的是v3的值，在更新的时候明显Cv3,v4&lt;Cv1,v3，所以更新v3处的值，如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411224135118?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（4）此时在比较中，会发现v2和v3的值是一样的，那么这里就选取v2（当然，选取v3也是可以的），然后按照相应的规则进行更新，如下图所示：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411224224000?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（5）此时选择v3，并进行相应的更新，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411224356970?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（6）此时选择v7，并进行相应的更新，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411224741266?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（7）此时选择v6，并进行相应的更新，如下图：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411224855097?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

（7）最优将v5置为true，结束：

<img alt="" class="has" src="https://img-blog.csdn.net/20170411225004878?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">

        对于上述的算法描述过程，对于v，dv，pv，known这些变量的表示方法，可以根据不同的需要进行调整。

        对于prim算法，由于是在无向图上进行的，因此当编写代码的时候要记住把每一条边都放到两个邻接表中。在不用堆时，运行时间为O（|v|^2），它对于稠密的图来说是最优的。使用二叉堆时，运行时间是O(|E|log|V|)，对于稀疏的图是一个好的界。

        下面给出一个具体的实现，在实现中我采用了优先队列进行求解（二叉堆的一种具体形式），代码如下：

 

```
#include&lt;iostream&gt;
using namespace std;
#include&lt;vector&gt;
#include&lt;string&gt;
#include&lt;list&gt;
#include&lt;queue&gt;

struct node   //为了便于prim算法
	{
		int vertexNum;
		int key;
		node(int num=0,int k=INT_MAX):vertexNum(num),key(k){}
		friend bool operator&lt;(const node &amp;n1,const node &amp;n2)
		{
			return n1.key&lt;n2.key;
		}
		friend bool operator&gt;(const node &amp;n1,const node &amp;n2)
		{
			return n1.key&gt;n2.key;
		}
	};
struct edgeNode
{
	int oneVertex;
	int otherVertex;
	int edgeWeight;
	edgeNode(int oneNum=0,int otherNum=0,int eWeight=0):oneVertex(oneNum),otherVertex(otherNum),edgeWeight(eWeight){}
	friend bool operator&gt;(const edgeNode &amp;edge1,const edgeNode &amp;edge2)
	{
		return edge1.edgeWeight&gt;edge2.edgeWeight;
	}
};
class UDGraph
{
	struct Edge
	{
		int nDestVertex;
		int edgeWeight;
		Edge(int num,int weight):
		nDestVertex(num),edgeWeight(weight){}
	};
private:
	struct vertex
	{
		string vertexName;
		list&lt;Edge&gt; adjEdges;
		vertex(const string &amp;name=NULL,list&lt;Edge&gt; adj=list&lt;Edge&gt;()):vertexName(name),adjEdges(adj){}
	};
public:
	UDGraph():m_vertexList(NULL){}
	~UDGraph()
	{
		for(int i=0;i&lt;m_vertexList.size();i++)
		{
			m_vertexList[i].adjEdges.clear();
		}
		m_vertexList.clear();
	}
	bool insertVertex(const string &amp;v)
	{
		int index=getVertexIndex(v);
		if(-1!=index)
			return false;
		m_vertexList.push_back(vertex(v));
	}
	bool insertEdge(const string &amp;v1,const string &amp;v2,int weight=0)
	{
		int index1=getVertexIndex(v1);
		int index2=getVertexIndex(v2);
		if(-1==index1)
			return false;
		if(-1==index2)
			return false;
		m_vertexList[index1].adjEdges.push_back(Edge(index2,weight));
		m_vertexList[index2].adjEdges.push_back(Edge(index1,weight));
		return true;
	}
	int getVertexNum() const
	{
		return m_vertexList.size();
	}
	bool removeEdge(const string &amp;v1,const string &amp;v2)
	{
		int index1=getVertexIndex(v1);
		int index2=getVertexIndex(v2);
		if(-1==index1)
			return false;
		if(-1==index2)
			return false;
		auto itr1=m_vertexList[index1].adjEdges.begin();
		auto itr2=m_vertexList[index2].adjEdges.begin();
		bool flag1=false,flag2=false;
		for(;itr1!=m_vertexList[index1].adjEdges.end();++itr1)
		{
			if(itr1-&gt;nDestVertex==index2)
			{
				m_vertexList[index1].adjEdges.erase(itr1);
				flag1=true;
				break;
			}
		}
		for(;itr2!=m_vertexList[index2].adjEdges.end();++itr2)
		{
			if(itr2-&gt;nDestVertex==index1)
			{
				m_vertexList[index1].adjEdges.erase(itr2);
				flag2=true;
				break;
			}
		}
		return flag1&amp;&amp;flag2;
	}
	void Prim(const string &amp;v,vector&lt;int&gt; &amp;prev,vector&lt;node&gt; &amp;node_vec)
	{
		priority_queue&lt;node,vector&lt;node&gt;,greater&lt;node&gt; &gt; nodeQueue;
	    node_vec.resize(m_vertexList.size());
		for(int i=0;i&lt;node_vec.size();i++)
		{
			node_vec[i].vertexNum=i;
			node_vec[i].key=INT_MAX;
		}
		int beginIndex=getVertexIndex(v);
		node_vec[beginIndex].key=0;
		vector&lt;bool&gt; visited(m_vertexList.size(),false);
		prev.assign(m_vertexList.size(),-1);
		visited[beginIndex]=true;
		nodeQueue.push(node_vec[beginIndex]);
		while(!nodeQueue.empty())
		{
			node vertexNode=nodeQueue.top();
			nodeQueue.pop();
			/*if(visited[vertexNode.vertexNum])
				continue;*/
			visited[vertexNode.vertexNum]=true;
			list&lt;Edge&gt; edgeList=m_vertexList[vertexNode.vertexNum].adjEdges;
			for(auto it=edgeList.begin();it!=edgeList.end();++it)
			{
				if(!visited[it-&gt;nDestVertex]&amp;&amp;it-&gt;edgeWeight&lt;node_vec[it-&gt;nDestVertex].key)
				{
					prev[it-&gt;nDestVertex]=vertexNode.vertexNum;
					node_vec[it-&gt;nDestVertex].key=it-&gt;edgeWeight;
					node_vec[it-&gt;nDestVertex].vertexNum=it-&gt;nDestVertex;
					nodeQueue.push(node_vec[it-&gt;nDestVertex]);
				}
			}
		}
	}
	void printPathResult(const vector&lt;int&gt; &amp;prev) const
	{
		for(int i=1;i&lt;prev.size();i++)
		{
			cout &lt;&lt; "(" &lt;&lt; getName(i) &lt;&lt; "," &lt;&lt; getName(prev[i]) &lt;&lt; ")" &lt;&lt; endl;
		}
	}
	int PrimWeightResult(const vector&lt;node&gt; &amp;node_vec) const
	{
		int edgeSum=0;
		for(int i=0;i&lt;node_vec.size();i++)
			edgeSum+=node_vec[i].key;
		return edgeSum;
	}

	void setTreeNode(const string &amp;name)
	{
		treeNode=getVertexIndex(name);
	}
private:
	vector&lt;vertex&gt; m_vertexList;
	static int counter;  //用来为深度优先搜索时为点排序号
	static int treeNodeNum;   //记录根节点的分支个数
	static int treeNode;   //记录根节点的编号
	int getVertexIndex(const string &amp;name) const
	{
		for(int i=0;i&lt;m_vertexList.size();i++)
		{
			if(name==m_vertexList[i].vertexName)
				return i;
		}
		return -1;
	}
	string getName(int index) const 
	{
		return m_vertexList[index].vertexName;
	}
	bool compare(const node &amp;n1,const node &amp;n2)
	{
		return n1.key&lt;n2.key;
	}
	priority_queue&lt;edgeNode,vector&lt;edgeNode&gt;,greater&lt;edgeNode&gt; &gt; getEdgeNodes() const 
	{
		priority_queue&lt;edgeNode,vector&lt;edgeNode&gt;,greater&lt;edgeNode&gt; &gt; edgeQueue;
		vector&lt;int&gt; visit1(m_vertexList.size(),false);
		vector&lt;int&gt; visit2(m_vertexList.size(),false);
		for(int index=0;index&lt;m_vertexList.size();index++)
		{
			list&lt;Edge&gt; adjList=m_vertexList[index].adjEdges;
			for(auto it=adjList.begin();it!=adjList.end();++it)
			{
				if(visit1[index]&amp;&amp;visit2[it-&gt;nDestVertex])
					continue;
				else
				{
					edgeQueue.push(edgeNode(index,it-&gt;nDestVertex,it-&gt;edgeWeight));
				}
			}
			visit1[index]=true;
			visit2[index]=true;
		}
		return edgeQueue;
	}
	int find(const vector&lt;int&gt; &amp;prev,int x) const
	{
		if(prev[x]&lt;0)
			return x;
		else
			return find(prev,prev[x]);
	}
	void unionSets(vector&lt;int&gt; &amp;prev,int root1,int root2)
	{
		prev[root1]=root2;
	}

};
int UDGraph::counter=1;
int UDGraph::treeNodeNum=0;
int UDGraph::treeNode=0;
int main()
{
	UDGraph graph;
	graph.insertVertex("v1");
	graph.insertVertex("v2");
	graph.insertVertex("v3");
	graph.insertVertex("v4");
	graph.insertVertex("v5");
	graph.insertVertex("v6");
	graph.insertVertex("v7");
	graph.insertEdge("v1","v2",2);
	graph.insertEdge("v1","v3",4);
	graph.insertEdge("v1","v4",1);
	graph.insertEdge("v2","v4",3);
	graph.insertEdge("v2","v5",10);
	graph.insertEdge("v3","v6",5);
	graph.insertEdge("v3","v4",2);
	graph.insertEdge("v4","v5",7);
	graph.insertEdge("v4","v6",8);
	graph.insertEdge("v4","v7",4);
	graph.insertEdge("v5","v7",6);
	graph.insertEdge("v6","v7",1);
	vector&lt;int&gt; prev;
	vector&lt;node&gt; node_vec;
	vector&lt;int&gt; dist;
	graph.Prim("v1",prev,node_vec);
	graph.printPathResult(prev);
	int edgeSum=graph.PrimWeightResult(node_vec);
	cout &lt;&lt; "最小生成树的路径权重之和为：" &lt;&lt; edgeSum &lt;&lt; endl;

	return 0;
}

```

好了，这次就分享这么多了。

 

<img alt="" class="has" src="https://img-blog.csdn.net/20170411230622199?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center">
