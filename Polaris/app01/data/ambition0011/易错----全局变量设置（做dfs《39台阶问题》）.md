
--- 
title:  易错----全局变量设置（做dfs《39台阶问题》） 
tags: []
categories: [] 

---
### 将步数设为全局变量（出错）

```
#include&lt;iostream&gt;
using namespace std;
int ans=0;
int t=0;
void dfs(int step)
{
	if(step==0&amp;&amp;t%2==0)
	ans++;
	if(step&gt;0)
	{
		t++;
		dfs(step-1);
		dfs(step-2); 
	}
}
int main()
{
	dfs(39);
	cout&lt;&lt;ans;
	return 0;
}

```

<img src="https://img-blog.csdnimg.cn/20210328151018925.png" alt="输出跟下面比少了一个">

### 步数设为每次递归的局部变量

```
#include&lt;iostream&gt;
using namespace std;
int ans=0;
void dfs(int step,int t)
{
	if(step==0&amp;&amp;t%2==0)
	ans++;
	if(step&gt;0)
	{
		dfs(step-1,t+1);//走一阶，步数加一 
		dfs(step-2,t+1); //走两阶，步数加一 
	}
}
int main()
{
	dfs(39,0);
	cout&lt;&lt;ans;
	return 0;
}

```

<img src="https://img-blog.csdnimg.cn/20210328151411863.png" alt="在这里插入图片描述">

### 分析原因

<img src="https://img-blog.csdnimg.cn/20210328153019298.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2FtYml0aW9uMDAxMQ==,size_16,color_FFFFFF,t_70" alt="">

但不知道为何只差一，如果这种原理的话应该差好多才对呀 我带入了45看结果也是差一（巧死算了），分析了一下，可能是整体的t都相当于加了1，除了第一个之外，于是阴差阳错后面的没变，就第一个偶数的时候误判（不一定对）

### 有想明白的评论告诉我蟹蟹😄
