
--- 
title:  序列变换（map+priority_queue） 
tags: []
categories: [] 

---
>  
 题目：给出一个序列，里面的元素相同，我们要得到元素各不相同的序列，进行这样的操作：令 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 为序列重复的最小数字，你需要删除序列左数第一个 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 并把第二个 <img alt="x" class="mathcode" src="https://private.codecogs.com/gif.latex?x"> 换成 <img alt="2*x" class="mathcode" src="https://private.codecogs.com/gif.latex?2*x">。例如原来是<img alt="[2,2,1,1,1]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B2%2C2%2C1%2C1%2C1%5D">，一次变换为<img alt="[2,2,2,1]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B2%2C2%2C2%2C1%5D">，两次变为<img alt="[4,2,1]" class="mathcode" src="https://private.codecogs.com/gif.latex?%5B4%2C2%2C1%5D">变换结束。 
 输入一个n接下来是序列的n个数字，输出最终变换的结果（最终的结果序列唯一）。 
 输入样例1： 
 3 
 5 4 5 
 输出样例1： 
 4 10 


思路：<img alt="map" class="mathcode" src="https://private.codecogs.com/gif.latex?map"> 存每一个数字的下标，并将下标从小到大排序，所以 <img alt="map" class="mathcode" src="https://private.codecogs.com/gif.latex?map"> 里的 <img alt="val" class="mathcode" src="https://private.codecogs.com/gif.latex?val"> 放优先队列即可

```
#include &lt;iostream&gt;
#include &lt;queue&gt;
#include &lt;map&gt;

using namespace std;
const int N = 1e5 + 7;
int a[N], ans[N];
priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; q;
map&lt;int, priority_queue&lt;int, vector&lt;int&gt;, greater&lt;int&gt;&gt; &gt; mp;

int main() {
    int n; cin &gt;&gt; n;
    for (int i = 0 ; i &lt; n; ++i) {
        cin &gt;&gt; a[i];
        mp[a[i]].emplace(i);
	}
	
    for (int i = 0; i &lt; n; ++i) {
        q.emplace(a[i]);
    }

    while (!q.empty()) {
        int x = q.top();
        q.pop();
        
        while (mp[x].size() &gt; 1) {
            mp[x].pop();
            int id = mp[x].top();
            a[id] *= 2;
            if (!mp.count(a[id])) {
                q.emplace(a[id]);
            }
            mp[a[id]].emplace(id);
            mp[x].pop();
        }
        if (mp[x].size() == 1) {
            ans[mp[x].top()] = x;
        }
    }

    for (int i = 0; i &lt; n; ++i) {
        if (ans[i]) {
            cout &lt;&lt; ans[i] &lt;&lt; " ";
        }
    }
    cout &lt;&lt; endl;
}

```

 
