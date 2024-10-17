
--- 
title:  【超详细】C++ vector 详解 + 例题，这一篇就够了 
tags: []
categories: [] 

---
>  
 没人会在意你努力的过程， 他们只会看你最后站在什么位置！在繁华中自律，在落魄中自愈！！！ 


### 写在前面：

本文是对C++中的vector容器进行一个知识总结，其中包含了对vector向量的各种操作；除此之外，本文还对每一个内置函数，如erase()、assign()等函数设置了解释程序用来演示本函数用法；错误展示也在本文中有所涉猎；最后学完知识点后，本文最后有例题，可以进行学习验证与刷题巩固！！！ 

>  
 向量（Vector）是一个封装了动态大小数组的顺序容器（Sequence Container）。跟任意其它类型容器一样，它能够存放各种类型的对象。可以简单的认为，向量是一个能够存放任意类型的动态数组。 


### 一、头文件

使用 vector 之前需要添加**头文件**：

```
#include &lt;vector&gt;

```

### 二、容器特性

##### 1.顺序序列

顺序容器中的元素按照严格的线性顺序排序。可以通过元素在序列中的位置访问对应的元素。

##### 2.动态数组

支持对序列中的任意元素进行快速直接访问，甚至可以通过指针算述进行该操作。提供了在序列末尾相对快速地添加/删除元素的操作。

##### 3.能够感知内存分配器的（Allocator-aware）

容器使用一个内存分配器对象来动态地处理它的存储需求。

### 三、vector数组初始化

尖括号为元素类型名，它可以是任何合法的数据类型，下面我全用int举例。

##### 1、定义空向量

```
vector&lt;int&gt; a;  //相当于空数组

```

##### 2、定义具有10个整型元素的向量

```
vector&lt;int&gt; a(10); //相当于a[10]

```

##### 3、定义具有10个整型元素的向量，且赋予每个元素初值为1

```
vector&lt;int&gt; a(10,1); //相当于a[10] = {1}

```

##### 4、定义与向量b具有相同值的向量a

```
vector&lt;int&gt; a(b); //将向量b赋值给向量a，即向量a等于向量b

```

###### 5、将向量b中下标0-2（共三个）的元素赋值给a

```
//第一个数据是起始地址，第二个数据是结束地址（不包括），第二个数据就是你要截取的长度加1
vector&lt;int&gt; a(b.begin(), b.begin()+3); 

```

##### 6、从数组中获得初值

```
int b[7] = {<!-- -->1,2,3,4,5,6,7}; //定义整形数组

vector&lt;int&gt; a(b, b+7）; //将数组b赋值给a，第一个数据是起始地址，第二个数据是结束地址（不包括）

```

##### 7、二维数组初始化

```
vector&lt;vector&lt;int&gt;&gt; a;  //初始化为int型二维数组，相当于int a[][]

```

### 四、vector 对象常用内置函数

首先定义两个vector向量，进行下面函数演示：

```
vector&lt;int&gt; a, b;

```

##### 1、assign() 函数：可对已定义好的vector向量进行赋值

```
//将b的下标为0-2的元素赋值给向量a
a.assign(b.begin(), b.begin()+3);

//使向量a变为长度为4且值为2
a.assign(4,2);

```

测试用例：

```
int main(){<!-- -->
	a.assign(5, 3);
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	a.assign(4, 2);
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	return 0;
} 

//输出：
3 3 3 3 3
2 2 2 2

```

##### 2、back() 函数

```
a.back();  //返回a的最后一个元素

```

##### 3、front() 函数

```
a.front();  //返回a的第一个元素

```

##### 4、取向量a中第i个数据

```
a[i]; //返回a的第i元素,当且仅当a存在

```

##### 5、clear() 函数

```
a.clear(); //清空a中的元素

```

##### 6、empty() 函数

```
a.empty(); //判断向量a是否为空，若为空空则返回true，非空则返回false

```

##### 7、push_back() 函数

```
a.push_back(5); //在向量a的最后插入一个元素，其值为5

```

##### 8、pop_back() 函数

```
a.pop_back(); //删除a向量的最后一个元素

```

测试用例：

```
int main(){<!-- -->
	a.push_back(1);
	a.push_back(2);
	a.push_back(3);
	a.push_back(4);
	a.push_back(5);
	cout &lt;&lt; "使用push_back压入函数后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl &lt;&lt; endl;
	cout &lt;&lt; "使用pop_back删除函数后：";
	a.pop_back(); 
	a.pop_back();
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	return 0;
} 

//输出：
使用push_back压入函数后：1 2 3 4 5
使用pop_back删除函数后：1 2 3

```

##### 9、erase() 函数

erase可以删去容器中指定位置的元素，容器的size（大小）会改变，但是容器的容量不变。

```
//删除a向量中全部元素
a.erase(a.begin(), a.end());

//删除a向量中下标0-2共三个元素
a.erase(a.begin(), a.begin()+3);

```

测试程序：

```
int main(){<!-- -->
	for(int i = 1; i &lt; 5; i++) a.push_back(i); //输入数据
	cout &lt;&lt; "使用erase删除前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	a.erase(a.begin(), a.begin() + 3);
	cout &lt;&lt; "使用erase删除后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	return 0;
} 

//输出：
使用erase删除前：1 2 3 4 5
使用erase删除后：4 5

```

##### 10、insert() 函数

```
//在a向量第二个元素（下标从0开始）后插入 8
a.insert(a.begin()+2, 8);

//在a向量的第二个元素（下标从0开始）后插入3个数，其值都为5
a.insert(a.begin()+1, 3, 8);

//b为数组，在a的第一个元素（从第0个元素算起）的位置插入b的第三个元素到第5个元素（不包括b+6）
a.insert(a.begin()+1, b+3, b+6);

```

测试用例：

```
void fun(){<!-- -->
	a.clear(); //清空a 
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	b.assign(10, 6); //对b输入数据 
}

int main(){<!-- -->
	fun(); 
	cout &lt;&lt; "使用insert插入前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	a.insert(a.begin() + 2, 8);
	cout &lt;&lt; "使用insert插入后：" ;
	for(int i = 0; i &lt; a.size(); i++) cout &lt;&lt; a[i] &lt;&lt; " ";
	cout &lt;&lt; endl &lt;&lt; endl;
	
	fun(); 
	cout &lt;&lt; "使用insert插入前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	a.insert(a.begin() + 2, 3, 8);
	cout &lt;&lt; "使用insert插入后：" ;
	for(int i = 0; i &lt; a.size(); i++) cout &lt;&lt; a[i] &lt;&lt; " ";
	cout &lt;&lt; endl &lt;&lt; endl;
	
	fun(); 
	cout &lt;&lt; "使用insert插入前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	a.insert(a.begin() + 2, b.begin()+3, b.begin()+6);
	cout &lt;&lt; "使用insert插入后：" ;
	for(int i = 0; i &lt; a.size(); i++) cout &lt;&lt; a[i] &lt;&lt; " ";
	cout &lt;&lt; endl;
	
	return 0;
} 

//输出：
使用insert插入前：1 2 3 4 5
使用insert插入后：1 2 8 3 4 5

使用insert插入前：1 2 3 4 5
使用insert插入后：1 2 8 8 8 3 4 5

使用insert插入前：1 2 3 4 5
使用insert插入后：1 2 6 6 6 3 4 5

```

##### 11、size() 函数

```
a.size(); //返回向量a中元素的个数

```

##### 12、capacity() 函数

capacity是指在发生realloc（动态分配）前能允许的最大元素数，即预分配的内存空间。

```
a.capacity(); //返回a在内存中总共可以容纳的元素个数

```

测试用例：

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	cout &lt;&lt; "a向量值：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;
	cout &lt;&lt; "a.size = " &lt;&lt; a.size() &lt;&lt; endl;
	
	cout &lt;&lt; "a.capacity = " &lt;&lt; a.capacity();
	
	return 0;
} 

//输出
a向量值：1 2 3 4 5
a.size = 5
a.capacity = 8

```

##### 13、resize() 函数

```
//将a的现有元素个数调整至10个，多则删，少则补，其值随机
a.resize(10);

//将a的现有元素个数调整至10个，多则删，少则补，其值为2
a.resize(10, 2);

```

测试用例：

```
void fun(){<!-- -->
	a.clear(); //清空a 
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	b.assign(10, 6); //对b输入数据 
}

int main(){<!-- -->
	fun();
	cout &lt;&lt; "使用resize前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl; 
	a.resize(10);
	cout &lt;&lt; "使用a.resize(10)后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl;
	fun(); 
	a.resize(10, 2);
	cout &lt;&lt; "使用a.resize(10, 2)后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	return 0;
} 


//输出：
使用resize前：1 2 3 4 5

使用a.resize(10)后：1 2 3 4 5 0 0 0 0 0

使用a.resize(10, 2)后：1 2 3 4 5 2 2 2 2 2

```

##### 14、reserve() 函数

```
a.reserve(100); //将a的容量扩充至100

```

##### 15、swap() 函数

```
a.swap(b); //b为向量，将a中的元素和b中的元素整体交换

```

##### 16、两个向量比较操作

```
a == b; //相等
a &gt; b; //大于
a &gt;= b; 大于等于
a &lt; b; //小于
a &lt;= b; //小于等于
a != b; //不等于

```

### 五、几个常用的操作函数

使用下面函数进行简单操作时，需要带有头文件：

```
#include&lt;algorithm&gt;

```

##### 1、sort() 函数

```
sort(a.begin(), a.end()); //对向量a进行从小到大排序

```

若你还想了解更多**sort函数**的内容，请看这篇文章：

测试用例：

```
int main(){<!-- -->
	for(int i = 5; i &gt;= 0; i--) a.push_back(i); //对a输入数据
	cout &lt;&lt; "使用sort前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl; 
	sort(a.begin(), a.end());
	cout &lt;&lt; "使用sort后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	return 0;
} 

输出：
使用sort前：5 4 3 2 1 0
使用sort后：0 1 2 3 4 5

```

##### 2、reverse() 函数

```
//对a中的元素从a.begin()（包括它）到a.end()（不包括它）的元素倒置，但不排列
reverse(a.begin(), a.end()); //如a中元素为1,3,2,4,倒置后为4,2,3,1

```

测试用例：

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	cout &lt;&lt; "使用reverse前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl; 
	reverse(a.begin(), a.end());
	cout &lt;&lt; "使用reverse后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	return 0;
} 

输出：
使用reverse前：1 2 3 4 5
使用reverse后：5 4 3 2 1

```

##### 3、copy() 函数

```
//把a中的从a.begin()（包括它）到a.end()（不包括它）的元素复制到b中，从b.begin()+1的位置（包括它）开始复制，覆盖掉原有元素
copy(a.begin(), a.end(), b.begin()+1);

```

测试用例：

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	b.assign(10, 6); //对b输入数据 
	
	cout &lt;&lt; "使用copy前向量b为：" ; 
	for(int i = 0; i &lt; b.size(); i++){<!-- -->
		cout &lt;&lt; b[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl; 
	copy(a.begin(), a.end(), b.begin()+2);
	cout &lt;&lt; "使用copy后向量b为：";
	for(int i = 0; i &lt; b.size(); i++){<!-- -->
		cout &lt;&lt; b[i] &lt;&lt; " ";
	}
	
	return 0;
} 

//输出：
使用copy前向量b为：6 6 6 6 6 6 6 6 6 6

使用copy后向量b为：6 6 1 2 3 4 5 6 6 6

```

##### 4、find() 函数

```
//在a中的从a.begin()（包括它）到a.end()（不包括它）的元素中查找10，
//若存在返回其在向量中的下标，不存在则返回end()，即向量最后一个元素下标加一
find(a.begin(), a.end(), 4);

```

测试用例：

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	cout &lt;&lt; "使用find前：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	cout &lt;&lt; endl &lt;&lt; endl; 
	
	cout &lt;&lt; "使用find后返回值index = ";
	cout &lt;&lt; find(a.begin(), a.end(), 4) - a.begin() &lt;&lt; endl;
	
	return 0;
}

//输出：
使用find前：1 2 3 4 5

使用find后返回值index = 3

```

### 六、遍历向量

##### 1、使用下标进行遍历

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	
	cout &lt;&lt; "遍历向量a：" ; 
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	
	return 0;
} 

//输出：
遍历向量a：1 2 3 4 5

```

##### 2、通过迭代器进行遍历

```
int main(){<!-- -->
	for(int i = 1; i &lt;= 5; i++) a.push_back(i); //对a输入数据
	
	cout &lt;&lt; "遍历向量a：" ; 
	for(vector&lt;int&gt;::iterator it = a.begin(); it != a.end(); it++){<!-- -->
		cout &lt;&lt; *it &lt;&lt; " ";
	}
	
	return 0;
} 

//输出：
遍历向量a：1 2 3 4 5

```

### 七、对向量添加元素的几种方式

##### 1、使用push_back() 函数

```
int main(){<!-- -->
	a.push_back(1);
	a.push_back(2);
	a.push_back(3);
	a.push_back(4);
	a.push_back(5);
	cout &lt;&lt; "使用push_back压入函数后：";
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	}
	return 0;
} 

//输出：
使用push_back压入函数后：1 2 3 4 5

```

##### 2、从数组或现有向量中添加

```
int main(){<!-- -->
	int num[6] = {<!-- -->1, 2, 3, 4, 5, 6};
	for(int i = 0; i &lt; 6; i++) a.push_back(num[i]);
	for(int i = 0; i &lt; a.size(); i++){<!-- -->
		cout &lt;&lt; a[i] &lt;&lt; " ";
	} 
	return 0;
} 

//输出：
遍历向量a：1 2 3 4 5

```

### 八、在赋值时一个常犯的错误与注意

1、在使用内置函数时，一定要注意第二个参数范围不包括end()。

2、下标只能用来获取已经存在的元素，so下面使用方法是错误的。

```
for(int i=0; i&lt;10; i++){<!-- -->
	a[i] = i;    //应使用a.push_back(i)
}

```

### 九、例题

这里为了清楚方便一些，我就只放AC代码啦，题目放链接，学了上面的内容，下面就开始通过刷题巩固上面知识吧！！！^ - ^

（一些做过LeetCode中题的朋友应该知道，LeetCode中只需提交其定义的函数就好了，他自带主函数，若有需要主函数的朋友可以在下面评论，我会在看到后第一时间回复）

1、

**AC代码：**

```
vector&lt;int&gt; twoSum(vector&lt;int&gt;&amp; numbers, int target) {<!-- -->
	vector&lt;int&gt; a;
	int n = numbers.size();
	for(int i = 0, j = n - 1; i &lt; j;){<!-- -->
		if(numbers[i] + numbers[j] == target){<!-- -->
			a.push_back(i+1);
			a.push_back(j+1);
			return a;
		}else if(numbers[i] + numbers[j] &gt; target){<!-- -->
			j--;
		}else{<!-- -->
			i++;
		}
	}
}

```

2、

**AC代码：**

```
vector&lt;int&gt; sortedSquares(vector&lt;int&gt;&amp; nums) {<!-- -->
	vector&lt;int&gt; a;
	for(int i = 0; i &lt; nums.size(); i++){<!-- -->
		int temp = pow(nums[i], 2);
		a.push_back(temp);
	}
	sort(a.begin(), a.end());
	return a;
}


```

3、

**AC代码：**

```
void moveZeroes(vector&lt;int&gt;&amp; nums) {<!-- -->
	int n = nums.size(), t = 0;
	for(int i = 0; i &lt; n; i++){<!-- -->
		if(nums[i] == 0) t++;
	}
	remove(nums.begin(),nums.end(),0);
	nums.erase(nums.begin() + (n - t), nums.end());
	while(t--){<!-- -->
		nums.push_back(0);
	}
}

```

4、

本题介绍使用了vector向量的二维数组定义方法！

**AC代码**

```
struct xy{<!-- -->  //存位置
    int x;
    int y;
}node, top;

vector&lt;vector&lt;int&gt;&gt; updateMatrix(vector&lt;vector&lt;int&gt;&gt;&amp; mat) {<!-- -->
    int n = mat.size(), m = mat[0].size(); 
    vector&lt;vector&lt;int&gt;&gt; a(n, vector&lt;int&gt; (m));  //记录变换后的数组
    vector&lt;vector&lt;int&gt;&gt; book(n, vector&lt;int&gt; (m)); //标记是否被访问
    int tx[4] = {<!-- -->0, 1, 0, -1};  //进行方向上的操作
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    queue&lt;xy&gt; q;
    
    for(int i = 0; i &lt; n; i++){<!-- -->  //先将所有0填入数组
        for(int j = 0; j &lt; m; j++){<!-- -->
            if(mat[i][j] == 0){<!-- -->
                node.x = i;
                node.y = j;
                q.push(node);
                book[i][j] = 1;
            }
        }
    }
    
    while(!q.empty()){<!-- -->  //bfs模板
        top = q.front();
        q.pop();
        
        for(int t = 0; t &lt; 4; t++){<!-- -->
            int x1 = top.x + tx[t];
            int y1 = top.y + ty[t];
            
            if(x1 &gt;= 0 &amp;&amp; x1 &lt; n &amp;&amp; y1 &gt;=0 &amp;&amp; y1 &lt; m &amp;&amp; !book[x1][y1]){<!-- -->
                a[x1][y1] = a[top.x][top.y] + 1;
                node.x = x1;
                node.y = y1;
                q.push(node);
                book[x1][y1] = 1;
            }
        }
    }
    return a;
}


```

5、

本题介绍使用了vector向量的二维数组定义方法！

**AC代码：**

```
struct xy{<!-- -->  //记录结点
    int x;
    int y;
}node, top;

int orangesRotting(vector&lt;vector&lt;int&gt;&gt;&amp; grid) {<!-- -->
    int m = grid.size(), n = grid[0].size();
    vector&lt;vector&lt;int&gt;&gt; book(m, vector&lt;int&gt; (n)); //标记是否被访问
    int ans = 0, cnt = 0; // cnt统计好橘子的个数 
    int tx[4] = {<!-- -->0, 1, 0, -1};
    int ty[4] = {<!-- -->-1, 0, 1, 0};
    queue&lt;xy&gt; q;
    
    for(int i = 0; i &lt; m; i++){<!-- --> //将所有坏橘子放入队列
        for(int j = 0; j &lt; n; j++){<!-- -->
            if(grid[i][j] == 2){<!-- -->
                node.x = i;
                node.y = j;
                q.push(node);
                book[i][j] = 1;
            }else if(grid[i][j] == 1){<!-- -->
                cnt++;
            }
        }
    }
    
    while(!q.empty() &amp;&amp; cnt &gt; 0){<!-- -->
        int size = q.size();
        int cnt1 = 0;
        ans++;
        
        for(int i = 0; i &lt; size; i++){<!-- --> //层次遍历
            top = q.front();
            q.pop();
            
            for(int t = 0; t &lt; 4; t++){<!-- --> //访问四个方向
                int x1 = top.x + tx[t];
                int y1 = top.y + ty[t];
                
                if(x1 &gt;= 0 &amp;&amp; x1 &lt; m &amp;&amp; y1 &gt;=0 &amp;&amp; y1 &lt; n &amp;&amp; !book[x1][y1]){<!-- -->
                    if(grid[x1][y1] == 1){<!-- -->
                        grid[x1][y1] = 2; 
                        node.x = x1;
                        node.y = y1;
                        q.push(node);
                        book[x1][y1] = 1;
                        cnt1++;
                    }
                }
            }
        }
        cnt -= cnt1;
    }
    if(cnt != 0) return -1;
 else return ans;
}


```

6、

本题使用vector实现DFS算法中的组合问题！！

**AC代码：**

```
vector&lt;vector&lt;int&gt;&gt; a; //存储排列数据
vector&lt;int&gt; b; // 存储每次的排列数据 

void DFS(int cur, int n, int k){<!-- -->
    if(cur == k){<!-- -->
        a.push_back(b);
        return ; 
    }
    
    for(int i = 1; i &lt;= n; i++){<!-- -->
        int temp;
        if(cur &gt; 0) temp = b.back();  //返回b数组的最后一个元素
        if((cur == 0) || (cur &gt; 0 &amp;&amp; i &gt; temp)){<!-- -->
            b.push_back(i);
            DFS(cur + 1, n, k);
            b.pop_back();
        }
    }
}

vector&lt;vector&lt;int&gt;&gt; combine(int n, int k) {<!-- -->
    DFS(0, n, k);
    return a;
}


```
1. https://blog.csdn.net/u013575812/article/details/511711351. https://blog.csdn.net/qq_31858735/article/details/826231101. 百度百科