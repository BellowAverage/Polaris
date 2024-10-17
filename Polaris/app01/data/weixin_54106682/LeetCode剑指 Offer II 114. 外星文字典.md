
--- 
title:  LeetCode剑指 Offer II 114. 外星文字典 
tags: []
categories: [] 

---
## **目录**















## 一、题目

现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。

请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。

字符串 s 字典顺序小于 字符串 t 有两种情况：

在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。如果前面 min(s.length, t.length) 字母都相同，那么 s.length &lt; t.length 时，s 的字典顺序也小于 t 。 示例 1：

>  
 输入：words = ["wrt","wrf","er","ett","rftt"] 输出："wertf" 


示例 2：

>  
 输入：words = ["z","x"] 输出："zx" 


示例 3：

>  
 输入：words = ["z","x","z"] 输出："" 解释：不存在合法字母顺序，因此返回 "" 。 


提示：

>  
 1 &lt;= words.length &lt;= 100 1 &lt;= words[i].length &lt;= 100 words[i] 仅由小写英文字母组成 


### **二、解题思路**

**建图+拓扑排序**

使用广度优先搜索实现拓扑排序，则可以正向得到拓扑排序。

首先计算每个节点的入度，只有入度为 0 的节点可能是拓扑排序中最前面的节点。当一个节点加入拓扑排序之后，该节点的所有相邻节点的入度都减 1，表示相邻节点少了一条入边。当一个节点的入度变成 0，则该节点前面的节点都已经加入拓扑排序，该节点也可以加入拓扑排序。

具体做法是，使用队列存储可以加入拓扑排序的节点，初始时将所有入度为 0 的节点入队列。每次将一个节点出队列并加入拓扑排序中，然后将该节点的所有相邻节点的入度都减 1，如果一个相邻节点的入度变成0，则将该相邻节点入队列。重复上述操作，直到队列为空时，广度优先搜索结束。

如果有向图中无环，则每个节点都将加入拓扑排序，因此拓扑排序的长度等于字典中的字母个数。如果有向图中有环，则环中的节点不会加入拓扑排序，因此拓扑排序的长度小于字典中的字母个数。广度优先搜索结束时，判断拓扑排序的长度是否等于字典中的字母个数，即可判断有向图中是否有环。

如果拓扑排序的长度等于字典中的字母个数，则拓扑排序包含字典中的所有字母，返回拓扑排序；

如果拓扑排序的长度小于字典中的字母个数，则有向图中有环，不存在拓扑排序。

```
class Solution {
public:
    //键为字母序较小的字母 值为字母序比键所存储的字母大的字母
    unordered_map&lt;char, vector&lt;char&gt;&gt; edges;
    //键为字母节点 值为该节点所对应的入度
    unordered_map&lt;char, int&gt; indegrees;
    //是否存在合法字母序的标志
    bool valid = true;

    string alienOrder(vector&lt;string&gt;&amp; words) {
        int length = words.size();
        for (auto word : words) {
            int wordLength = word.size();
            for (int j = 0; j &lt; wordLength; j++) {
                char c = word[j];
                //如果该节点没有出现过 则将其存储在map容器的键中
                if (!edges.count(c)) {
                    edges[c] = vector&lt;char&gt;();
                }
            }
        }
        //添加字母序小的指向较大一方的边
        for (int i = 1; i &lt; length &amp;&amp; valid; i++) {
            addEdge(words[i - 1], words[i]);
        }
        if (!valid) {
            return "";
        }
        //广度优先建立队列
        queue&lt;char&gt; qu;
        //遍历图 将入度为0的放入队列
        for (auto it : edges) {
            if (!indegrees.count(it.first)) {
                qu.emplace(it.first);
            }
        }
        string order;
        while (!qu.empty()) {
            char u = qu.front();
            qu.pop();
            order.push_back(u);
            将从队列中取出的节点所指向的节点的入度-1
            for (char v : edges[u]) {
                indegrees[v]--;
                //如果入度为0加入队列
                if (indegrees[v] == 0) {
                    qu.emplace(v);
                }
            }
        }
        //最终从队列取出的节点数等于初始化图中的节点数 则代表序列合法 否则不合法
        return order.size() == edges.size() ? order : "";
    }

    void addEdge(string before, string after) {
        int length1 = before.size(), length2 = after.size();
        int length = min(length1, length2);
        int index = 0;
        while (index &lt; length) {
            char c1 = before[index], c2 = after[index];
            //出现不同字母代表字母序开始出现
            if (c1 != c2) {
                edges[c1].emplace_back(c2);
                indegrees[c2] += 1;
                break;
            }
            index++;
        }
        //如果后一个字符串时前一个字符串的前缀 则不合法
        if (index == length &amp;&amp; length1 &gt; length2) {
            valid = false;
        }
    }
};
```

## 三、知识总结

### 1.C++ STL unordered_map容器用法详解

unordered_map 容器，直译过来就是"无序 map 容器"的意思。所谓“无序”，指的是 unordered_map 容器不会像 map 容器那样对存储的数据进行排序。换句话说，unordered_map 容器和 map 容器仅有一点不同，即 map 容器中存储的数据是有序的，而 unordered_map 容器中是无序的。

unordered_map 容器和 map 容器一样，以键值对（pair类型）的形式存储数据，存储的各个键值对的键互不相同且不允许被修改。但由于 unordered_map 容器底层采用的是哈希表存储结构，该结构本身不具有对数据的排序功能，所以此容器内部不会自行对存储的键值对进行排序。 unordered_map 容器在`&lt;unordered_map&gt;`头文件中，并位于 std 命名空间中。因此，如果想使用该容器，代码中应包含如下语句：

```
#include &lt;unordered_map&gt;
using namespace std;
```

### 2.unordered_map类模板成员方法
|begin()|返回指向容器中第一个键值对的正向迭代器。
|end() |返回指向容器中最后一个键值对之后位置的正向迭代器。
|cbegin()|和 begin() 功能相同，只不过在其基础上增加了 const 属性，即该方法返回的迭代器不能用于修改容器内存储的键值对。
|cend()|和 end() 功能相同，只不过在其基础上，增加了 const 属性，即该方法返回的迭代器不能用于修改容器内存储的键值对。
|empty()|若容器为空，则返回 true；否则 false。
|size()|返回当前容器中存有键值对的个数。
|max_size()|返回容器所能容纳键值对的最大个数，不同的操作系统，其返回值亦不相同。
|operator[key]|该模板类中重载了 [] 运算符，其功能是可以向访问数组中元素那样，只要给定某个键值对的键 key，就可以获取该键对应的值。注意，如果当前容器中没有以 key 为键的键值对，则其会使用该键向当前容器中插入一个新键值对。
|at(key)|返回容器中存储的键 key 对应的值，如果 key 不存在，则会抛出 out_of_range 异常。 
|find(key)|查找以 key 为键的键值对，如果找到，则返回一个指向该键值对的正向迭代器；反之，则返回一个指向容器中最后一个键值对之后位置的迭代器（如果 end() 方法返回的迭代器）。
|count(key)|在容器中查找以 key 键的键值对的个数。
|equal_range(key)|返回一个 pair 对象，其包含 2 个迭代器，用于表明当前容器中键为 key 的键值对所在的范围。
|emplace()|向容器中添加新键值对，效率比 insert() 方法高。
|emplace_hint()|向容器中添加新键值对，效率比 insert() 方法高。
|insert() |向容器中添加新键值对。
|erase()|删除指定键值对。
|clear() |清空容器，即删除容器中存储的所有键值对。
|swap()|交换 2 个 unordered_map 容器存储的键值对，前提是必须保证这 2 个容器的类型完全相等。
|bucket_count()|返回当前容器底层存储键值对时，使用桶（一个线性链表代表一个桶）的数量。
|max_bucket_count()|返回当前系统中，unordered_map 容器底层最多可以使用多少桶。
|bucket_size(n)|返回第 n 个桶中存储键值对的数量。
|bucket(key)|返回以 key 为键的键值对所在桶的编号。
|load_factor()|返回 unordered_map 容器中当前的负载因子。负载因子，指的是的当前容器中存储键值对的数量（size()）和使用桶数（bucket_count()）的比值，即 load_factor() = size() / bucket_count()。
|max_load_factor()|返回或者设置当前 unordered_map 容器的负载因子。
|rehash(n)|将当前容器底层使用桶的数量设置为 n。
|reserve()|将存储桶的数量（也就是 bucket_count() 方法的返回值）设置为至少容纳count个元（不超过最大负载因子）所需的数量，并重新整理容器。
|hash_function()|返回当前容器使用的哈希函数对象。

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;unordered_map&gt;
using namespace std;
int main()
{
    //创建空 umap 容器
    unordered_map&lt;string, string&gt; umap;
    //向 umap 容器添加新键值对
    umap.emplace("a", "1");
    umap.emplace("b", "2");
    umap.emplace("c", "3");

    //输出 umap 存储键值对的数量
    cout &lt;&lt; "umap size = " &lt;&lt; umap.size() &lt;&lt; endl;
    //使用迭代器输出 umap 容器存储的所有键值对
    for (auto iter = umap.begin(); iter != umap.end(); ++iter) {
        cout &lt;&lt; iter-&gt;first &lt;&lt; " " &lt;&lt; iter-&gt;second &lt;&lt; endl;
    }
    return 0;
}
```

### 3.C++map方法

C++中访问容器需要使用，而非下标。

#### c++98

```
    map&lt;string, int&gt;::iterator it;
    for (it = m2.begin(); it != m2.end(); it++) {
        string s = it-&gt;first;
        printf("%s %d\n", s.data(), it-&gt;second);
    }

```

c++11以后

```
for(auto it : map1){
	cout &lt;&lt; it.first &lt;&lt;" "&lt;&lt; it.second &lt;&lt;endl;
}

```

## 四、总结

建图的过程就是确定节点和对应边的过程；

要熟练掌握map容器相关用法 比如遍历操作；

拓扑排序利用广度优先的方法实现，应重点理解出入度。
