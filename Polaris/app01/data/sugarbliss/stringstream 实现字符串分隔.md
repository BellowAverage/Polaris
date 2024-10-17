
--- 
title:  stringstream 实现字符串分隔 
tags: []
categories: [] 

---
>  
 <h4>**stringstream默认分割空格、tab、回车换行 **</h4> 


```
#include &lt;bits/stdc++.h&gt;
using namespace std;
int main()
{
    string s1, s2;
    s1 = "Those who cannot remember the past are condemned to repeat it";
    stringstream ss(s1);
    while(ss &gt;&gt; s2)
        cout &lt;&lt; s2 &lt;&lt; endl;
}
/*
输出：
Those
who
cannot
remember
the
past
are
condemned
to
repeat
it
*/

```

>  
 <h4 id="利用指定字符分割字符串">利用指定字符分割字符串</h4> 


```
#include &lt;bits/stdc++.h&gt;
using namespace std;
int main()
{
    string s1, s2;
    s1 = "Those*who*cannot*remember*the*past*are*condemned*to*repeat*it";
    stringstream ss(s1);
    while(getline(ss, s2, '*'))
        cout &lt;&lt; s2 &lt;&lt; endl;
}
/*
输出：
Those
who
cannot
remember
the
past
are
condemned
to
repeat
it
*/

```

 
