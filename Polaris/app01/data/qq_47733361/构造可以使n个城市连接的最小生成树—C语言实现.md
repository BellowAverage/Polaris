
--- 
title:  构造可以使n个城市连接的最小生成树—C语言实现 
tags: []
categories: [] 

---
<mark>补充说明：有些同学反映说输出的内容为空，在这里我统一补充一下，其原因就是文本文档相对路径不对，此时有一种解决办法就是：把fp文件指针的引用路径改为 fp=fopen(".\\textdata.txt",“r”); 前面的“.”表示当前目录，这样就不用非常麻烦的修改路径了，当然使用此方法文本文档与".cpp"文件必须要在同一文件夹中；还有另一种问题就是有些同学的电脑扩展名隐藏了，相对路径中“textdata.txt”的含义为“textdata”为文件名，“.txt”为扩展名，如果此时重命名文本文档为“textdata.txt”表示文件名为“textdata.txt”，扩展名为“.txt”，即此时文本文档的全名为“textdata.txt.txt”，名字不一样，所以引用不成功。大概就是这样，有什么其他问题欢迎大家指正！！！如果对你有帮助就请留下你的点赞与关注吧~</mark>
- 数据结构的课设作业，现在分享给大家，希望能够帮助到大家。 由于要交报告，为了看起来高大上一点，所以也采用了多级菜单的格式，而且Prim算法写了两种方法。哈哈，不多说，看下面。
## 一、题目：

问题描述：给定一个地区的 n 个城市间的距离网，用 Prim 算法或 Kruskal 算 法建立最小生成树，并计算得到的最小生成树的代价。 基本要求：

(1)城市间的距离网采用邻接矩阵表示，邻接矩阵的存储结构定义采用课本中给出的定义，若两个城市之间不存在道路，则将相应边的权值设为自己定义的无穷大值。要求在屏幕上显示得到的最小生成树中包括了哪些城市间的道路，并显示得到的最小生成树的代价。

(2)表示城市间距离网的邻接矩阵（要求至少 6 个城市，10 条边）

(3)最小生成树中包括的边及其权值，并显示得到的最小生成树的代价。

## 二、模块简介

依据程序的功能模块的划分，各模块定义如下： （1）输入功能 模块名：void GreateUDN_M(FILE *fp,MGraph *G); 模块描述：通过此模块可以输入各个城市及城市距离之间的信息。采用文件输入的方式：先把相关数据输入文件中，然后直接从文件中调用，方便快捷。在各个模块整合的过程中，更方便调试。

（2）显示距离网 模块名：void printUDN_M(MGraph G); 模块描述：此模块可以输出距离网的邻接矩阵。邻接矩阵的存储结构定义采用课本中给出的定义，若两个城市之间不 存在道路，则将相应边的权值设为自己定义的无穷大值。

（3）使用Prim算法实现最小生成树 模块名：void MinTree_Prim(MGraph G,VertexType u); void MinTree_Prim2(MGraph G,VertexType u); 模块描述：在屏幕上显示得到的最小生成树中包括了哪些城市间的道路，及道路之间的距离（权值），并显示得到的最小生成树的代价。采用辅助数组的方法（该模块我用了两种方法来写，毕竟这道题比较简单，这样写能多拿点分，哈哈）。

（4）使用Kruskal算法实现最小生成树 模块名：void MinTree_Kruskal(MGraph G); 模块描述：在屏幕上显示得到的最小生成树中包括了哪些城市间的道路，及道路之间的距离（权值），并显示得到的最小生成树的代价。哲理采用并查集的知识来判断两部分是否连通。

（5）得到最先生成树的代价 为了程序简洁，该功能的实现在三、四中同时实现。最先生成树的代价及最小生成树各边权值和。

## 三、代码：

介绍差不多了，下面看代码：

### 1、相关头文件及其他基础信息：

**jichu.h**

```
#include&lt;stdio.h&gt;
#include&lt;windows.h&gt;
#include&lt;process.h&gt;
#include&lt;stdlib.h&gt;
#include&lt;string.h&gt;
#include&lt;limits.h&gt;

#define OK 1
#define TRUE 1
#define FALSE 0
#define ERROR 0

typedef int Status;

```

**smallesttree.h**

```
#include "jichu.h"
#define INFINITY 99999      //无穷,足够大
#define MAX  20             //最大顶点数
#define MAXNUM 1000

typedef int VRType;         //顶点关系类型
typedef char VertexType;    //顶点类型

typedef struct{<!-- -->
	VRType adj;             //权值即城市间的距离
}ArcCell,AdjMatrix[MAX+1][MAX+1];

typedef struct{<!-- -->
	VertexType vexs[MAX+1];  //顶点向量
	AdjMatrix arcs;          //邻接矩阵
	int vexnum,arcnum;       //网的当前顶点数和弧数
}MGraph;

typedef struct{<!-- -->
	VertexType vexadj;       //较早加入边的端点
	VRType lowcost;          //当前边的权值
}Edge;

typedef struct{<!-- -->
	int a,b;                 //端点
	int w;                   //权值
}KEdge;

void GreateUDN_M(FILE *fp,MGraph *G);//调用文件中数据构建无向网，并将邻接矩阵初始化
int Locate_vexM(MGraph G,VertexType u);//定位顶点u的位置
void printUDN_M(MGraph G);//输出距离网的邻接矩阵
int Attention();//输出警告信息
void MinTree_Prim(MGraph G,VertexType u);//使用prim算法从顶点u出发构建最小生成树T，并输出T的各条边
int Minimum(Edge closedge[],int n); //求出T的下个结点，第k结点||返回最小边的端点
void MinTree_Prim2(MGraph G,VertexType u);//使用prim算法从顶点u出发构建最小生成树T，并输出T的各条边
int Minimum2(MGraph G,int start[],int mark[]);//求出T的下个结点，第k结点||返回最小边的端点
void MinTree_Kruskal(MGraph G);//kruskal算法构建最小生成树T，并输出T的各条边
void Sort(KEdge a[],int n);//使用选择排序按权值排序
int Root(int x,int fat[]);//寻找x的根结点
void Unionn(int x,int y,int fat[]);//加入集合，并查集的一部分




void GreateUDN_M(FILE *fp,MGraph *G){<!-- -->
	//调用文件中数据构建无向网，并将邻接矩阵初始化
	int i,j,k;
	VertexType v1,v2;
	VRType w;
	char tem;
	fscanf(fp, "%d", &amp;((*G).vexnum));
	fscanf(fp, "%c", &amp;tem);    //跳过换行符
	fscanf(fp, "%d", &amp;((*G).arcnum));
	fscanf(fp, "%c", &amp;tem);    //跳过换行符
	for(i=1;i&lt;=(*G).vexnum;i++){<!-- -->
		fscanf(fp, "%c", &amp;((*G).vexs[i]));
	}
	(*G).vexs[i]='\0';
	fscanf(fp, "%c", &amp;tem);    //跳过换行符
	for(i=1;i&lt;=(*G).vexnum;i++){<!-- -->    //初始化邻接矩阵
		for(j=1;j&lt;=(*G).vexnum;j++){<!-- -->
			(*G).arcs[i][j].adj=INFINITY;
		}
	}
	for(k=1;k&lt;=(*G).arcnum;k++){<!-- -->    //输入弧信息
		fscanf(fp,"%c%c%d",&amp;v1,&amp;v2,&amp;w);
		fscanf(fp, "%c", &amp;tem);    //跳过空格字符
		i=Locate_vexM(*G,v1);
		j=Locate_vexM(*G,v2);
		(*G).arcs[i][j].adj=w;
		(*G).arcs[j][i].adj=w;     //填充对称点
	}
	printf("\n\n\n调用成功，您可进行其他操作！！！\n");
}

int Attention(){<!-- -->
	int t;
	printf("ATTENTION: \n\n");
	printf("※在使用之前请先确认是否已把使用的数据存入文件中,已存入请输入:1  否则输入:0！！！※\n");
	scanf("%d",&amp;t);
	if(t==0){<!-- -->
		printf("※文件中第一行请输入顶点个数！！！※\n");
		printf("※文件中第二行请输入弧个数！！！  ※\n");
		printf("※文件中第三行请输入顶点集！！！  ※\n");
		printf("※文件中第四行请输入弧的集合！！！※\n");
	}
	return t;
}

int Locate_vexM(MGraph G,VertexType u){<!-- -->
	//定位顶点u的位置
	int i;
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->
		if(G.vexs[i]==u)
			return i;
	}
	return 0;
}

void printUDN_M(MGraph G){<!-- -->//输出距离网的邻接矩阵
	int i,j;
	printf("距离网的邻接矩阵如下:\n\n");
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->    
		for(j=1;j&lt;=G.vexnum;j++){<!-- -->
			if(G.arcs[i][j].adj==INFINITY){<!-- -->
				printf("∞ ");
			}
			else{<!-- -->
				printf("%-2d",G.arcs[i][j].adj);
			}
		}
		printf("\n");
	}
}

void MinTree_Prim(MGraph G,VertexType u){<!-- -->
	//使用prim算法从顶点u出发构建最小生成树T，并输出T的各条边
	int i,j,k,t=1;
	Edge closedge[MAX+1];    //0号单元弃用
	int minprice=0;
	k=Locate_vexM(G,u);
	for(j=1;j&lt;=G.vexnum;j++){<!-- -->//辅助数组初始化
		if(j!=k){<!-- -->
			closedge[j].vexadj=u;
			closedge[j].lowcost=G.arcs[k][j].adj;
		}
	}
	closedge[k].lowcost=0;
	printf("使用prim算法得到的最小生成树的各边及其权值为:\n\n");
	printf("  结点     权值\n");
	for(i=1;i&lt;=G.vexnum-1;i++){<!-- -->  //需要n-1次寻找最小边
		k=Minimum(closedge,G.vexnum);
		printf("%3c--%c%8d\n",closedge[k].vexadj,G.vexs[k],closedge[k].lowcost);
		minprice+=closedge[k].lowcost;
		closedge[k].lowcost=0;
		for(j=1;j&lt;=G.vexnum;j++){<!-- -->  //新顶点并入U后从新选择最小边
			if(G.arcs[k][j].adj&lt;closedge[j].lowcost){<!-- -->
				closedge[j].vexadj=G.vexs[k];
				closedge[j].lowcost=G.arcs[k][j].adj;
			}
		}
	}
	printf("\n\n※使用prim算法得到的最小生成树的代价为: %d ※\n",minprice);
}

int Minimum(Edge closedge[],int n){<!-- -->  
	//求出T的下个结点，第k结点
	//返回最小边的端点
	int i,j;
	int min=INFINITY;
	for(i=1;i&lt;=n;i++){<!-- -->
		if(closedge[i].lowcost!=0){<!-- -->  //从权值不为0的边中找最小权值
			if(closedge[i].lowcost&lt;min){<!-- -->
				min=closedge[i].lowcost;
				j=i;
			}
		}
	}
	return j;
}

void MinTree_Prim2(MGraph G,VertexType u){<!-- -->
	//使用prim算法从顶点u出发构建最小生成树T，并输出T的各条边
	int i,j,k;
	int start[MAX+1];  
	int mark[MAX+1];  //标记该顶点是否加入T中
	int minprice=0;
	k=Locate_vexM(G,u);
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->//初始化
		start[i]=k;
		if(i!=k)
			mark[i]=0;
		else
			mark[i]=1;
	}
	printf("使用prim算法得到的最小生成树的各边及其权值为:\n\n");
	printf("  结点     权值\n");
	for(i=1;i&lt;=G.vexnum-1;i++){<!-- -->
		k=Minimum2(G,start,mark);
		printf("%3c--%c%8d\n",G.vexs[start[k]],G.vexs[k],G.arcs[start[k]][k].adj);
		minprice+=G.arcs[start[k]][k].adj;
		mark[k]=1;  //标记
		for(j=1;j&lt;=G.vexnum;j++){<!-- -->
			if(mark[j]!=1){<!-- -->
				if(G.arcs[k][j].adj&lt;G.arcs[start[j]][j].adj)
					start[j]=k;
			}
		}
	}
	printf("\n\n※使用prim算法得到的最小生成树的代价为: %d ※\n",minprice);
}

int Minimum2(MGraph G,int start[],int mark[]){<!-- -->
	//求出T的下个结点，第k结点
	//返回最小边的端点
	int i,j;
	int min=INFINITY;
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->
		if(mark[i]!=1&amp;&amp;G.arcs[start[i]][i].adj&lt;min){<!-- -->
			min=G.arcs[start[i]][i].adj;
			j=i;
		}
	}
	return j;
}

void MinTree_Kruskal(MGraph G){<!-- -->
	//kruskal算法运用并查集知识
	KEdge h[MAXNUM];     //存储边信息
	int fat[MAX];       //fat[i]存储i的前驱结点
	int x,y;
	int i,j,k=1;
	int has=0;       //已经连接了多少条边
	int minprice=0;
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->        //初始化
		for(j=i;j&lt;=G.vexnum;j++){<!-- -->
			if(G.arcs[i][j].adj!=INFINITY){<!-- -->
				h[k].a=i;
				h[k].b=j;
				h[k].w=G.arcs[i][j].adj;
				k++;
			}
		}
	}
	for(i=1;i&lt;=G.vexnum;i++){<!-- -->//初始化
		fat[i]=i;
	}
	Sort(h,G.arcnum);   //kruskal思想，排序权值
	printf("使用kruskal算法得到的最小生成树的各边及其权值为:\n\n");
	printf("  结点     权值\n");
	for(i=1;i&lt;=G.arcnum;i++){<!-- -->
		if(has==G.vexnum-1)  break;//树的边数等于顶点-1
		x=Root(h[i].a,fat);   //寻找根结点
		y=Root(h[i].b,fat);   //寻找根结点
		if(x!=y){<!-- --> //不在一个集合
			Unionn(x,y,fat);
			printf("%3c--%c%8d\n",G.vexs[h[i].a],G.vexs[h[i].b],h[i].w);
			minprice+=h[i].w;
			has++;
		}
	}
	printf("\n\n※使用kruskal算法得到的最小生成树的代价为: %d ※\n",minprice);
}

void Sort(KEdge h[],int n){<!-- -->
	//按权值排序
	//使用选择排序
	int i,j;
	KEdge temp;   //定义一个KEdeg结构体作为交换中间变量
	for(i=1;i&lt;=n;i++){<!-- -->
		for(j=i+1;j&lt;=n;j++){<!-- -->
			if(h[i].w&gt;h[j].w){<!-- -->  //交换KEdge数据结构类型
				temp=h[i];
			    h[i]=h[j];
				h[j]=temp;
			}
		}
	}
}

int Root(int x,int fat[]){<!-- -->//寻找x的根结点，当一个顶点的根节点是它本身，说明就是根结点
	if(fat[x]!=x)
	    return Root(fat[x],fat);
	else
	    return x;
}

void Unionn(int x,int y,int fat[]){<!-- -->//加入集合，并查集的一部分
	fat[y]=x;
}

```

### 2、主函数：

```
#include "smallesttree.h"
#include "jichu.h"

void main(){<!-- -->
	int x,t=1;
	int flag;
	FILE *fp;
	MGraph G;
	printf("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n");
	printf("★                                                                            ★\n");
	printf("★                  ****************************************                  ★\n");
	printf("★                          /*欢迎使用最小生成树系统*/                        ★\n");
	printf("★                  ****************************************                  ★\n");
	printf("★                                                                            ★\n");
	printf("★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n\n\n");
	flag=Attention();
	if(flag==0){<!-- -->
		printf("\n\n\n※请您先把所需数据输入文件中,谢谢配合！！！");
		system("pause");
		exit(1);
	}
	fp=fopen("D:\\工程\\第二学期课设\\第二学期课设\\textdata.txt","r");
	GreateUDN_M(fp,&amp;G);
	fclose(fp);
	system("pause");
	system("cls");
	while(t){<!-- -->
		printf("     * ******************************************************************** *\n");
		printf("     * ≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌ *\n");
		printf("     * ≌                            *主菜单*                            ≌ *\n");
		printf("     * ≌                                                                ≌ *\n");
		printf("     * ≌                       *1.输出距离网的邻接矩阵                  ≌ *\n");
		printf("     * ≌                       *2.使用prim算法实现最小生成树            ≌ *\n");
		printf("     * ≌                       *3.使用prim算法实现最小生成树(另一种)    ≌ *\n");
		printf("     * ≌                       *4.使用kruskal算法实现最小生成树         ≌ *\n");
		printf("     * ≌                       *0.退出                                  ≌ *\n");
		printf("     * ≌                                                                ≌ *\n");
		printf("     * ≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌≌ *\n");
		printf("     * ******************************************************************** *\n");
		printf("请输入您要进行的操作:");
		scanf("%d",&amp;x);
		switch(x){<!-- -->
		case 1:
			system("cls");
			printUDN_M(G);
			system("pause");
			system("cls");
			break;
		case 2:
			system("cls");
			MinTree_Prim(G,G.vexs[1]);
			system("pause");
			system("cls");
			break;
		case 3:
			system("cls");
			MinTree_Prim2(G,G.vexs[1]);
			system("pause");
			system("cls");
			break;
		case 4:
			system("cls");
			MinTree_Kruskal(G);
			system("pause");
			system("cls");
			break;
		case 0:
			t=0;
			break;
		}
	}
}

```

## 四、运行结果截图：

运行程序后首先进入如下界面： <img src="https://img-blog.csdnimg.cn/20210104202405726.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

这里选择是否已经把顶点与边的信息存入textdata.txt文档中，选择1进入下面界面，否则退出程序： <img src="https://img-blog.csdnimg.cn/20210104202316945.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 选择1输出距离网的邻接矩阵存储表示： <img src="https://img-blog.csdnimg.cn/20210104202504203.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 选择2使用Prim算法实现： <img src="https://img-blog.csdnimg.cn/20210104202557268.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 选择3也是使用Prim算法实现，但这里我使用了与上面不同的方法（为了多混点分，这个毕竟比较简单，hhh）： <img src="https://img-blog.csdnimg.cn/20210104202720132.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 选择4使用Kruskal算法实现： <img src="https://img-blog.csdnimg.cn/20210104202812225.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 最后输入0退出程序： <img src="https://img-blog.csdnimg.cn/20210104202925398.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

**最后给大家展示一下textdata.txt文档内容的输入方式：** 第一行为顶点个数； 第二行为边的个数； 第三行为顶点名称（可修改）； 第四行为边的信息及权值（可修改）。 <img src="https://img-blog.csdnimg.cn/20201123112320873.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20201208123328965.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ3NzMzMzYx,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">
