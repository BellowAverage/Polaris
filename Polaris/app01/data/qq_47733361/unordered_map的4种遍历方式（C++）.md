
--- 
title:  unordered_map的4种遍历方式（C++） 
tags: []
categories: [] 

---
#### c++ unordered_map4种遍历方式

此处我通过移到LeetCode上的一道题来演示unordered_map的用法： 首先看一下题目题解：

```
int longestPalindrome(string s) {<!-- -->
   unordered_map&lt;char, int&gt; map;
    int ans = 0;
    int flag = 0;
    for(int i = 0; i &lt; s.size(); i++){<!-- -->
        map[s[i]]++;
    }
    for(auto [_, v] : map){<!-- -->
        if(v % 2 == 0){<!-- -->
            ans += v;
        } else{<!-- -->
            flag = 1;
            ans += v - 1;
        }
    }
    if(flag == 1){<!-- -->
        ans += 1;
    }
    return ans;
}

```

这里定义了一个unordered_map：

```
for(int i = 0; i &lt; s.size(); i++){<!-- -->
	map[s[i]]++;
}

```

##### 方式一：值传递遍历

```
for(pair&lt;char, int&gt; kv : map){<!-- -->
	cout &lt;&lt; kv.first &lt;&lt; kv.second &lt;&lt; endl;
}

```

可以使用aotu取代pair&lt;char, int&gt;:

```
for(auto kv : map){<!-- -->
	cout &lt;&lt; kv.first &lt;&lt; kv.second &lt;&lt; endl;
}

```

##### 方式二：引用传递遍历

此处需要**添加const**

```
for(const pair&lt;char, int&gt;&amp; kv : map){<!-- -->
	cout &lt;&lt; kv.first &lt;&lt; kv.second &lt;&lt; endl;
}

for(pair&lt;const char, int&gt;&amp; kv : map){<!-- -->
	cout &lt;&lt; kv.first &lt;&lt; kv.second &lt;&lt; endl;
}

```

可以使用aotu取代pair&lt;char, int&gt;:

```
for(auto&amp; kv : map){<!-- -->
	cout &lt;&lt; kv.first &lt;&lt; kv.second &lt;&lt; endl;
}

```

##### 方式三：使用迭代器遍历

```
for(unordered_map&lt;char, int&gt;::iterator it = map.begin(); it != map.end(); it++){<!-- -->
	cout &lt;&lt; it-&gt;first &lt;&lt; it-&gt;second &lt;&lt; endl;
}

```

使用迭代器的话auto会更简洁：

```
for(auto it = map.begin(); it != map.end(); it++){<!-- -->
	cout &lt;&lt; it-&gt;first &lt;&lt; it-&gt;second &lt;&lt; endl;
}

```

##### 方式四：结构化绑定(c++17特性)

值传递：

```
for(auto [k,v] : map){<!-- -->
	cout &lt;&lt; k &lt;&lt; v &lt;&lt; endl;
}

```

引用传递：

```
for(auto&amp; [k,v] : map){<!-- -->
	cout &lt;&lt; k &lt;&lt; v &lt;&lt; endl;
}

```

```
for(auto&amp; [_,v] : map){<!-- -->
	cout &lt;&lt; v &lt;&lt; endl;
}

```

```
for(auto&amp; [k,_] : map){<!-- -->
	cout &lt;&lt; k &lt;&lt; endl;
}

```
