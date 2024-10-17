
--- 
title:  数据结构（c++）--map划分词典的相似单词 
tags: []
categories: [] 

---
        这次分享一下看到的一个map对于相似单词的划分的示例。

        首先，我们需要一个存放了很多单词的字典，在上一篇博客中，我已经做好了相关的处理 ，可以参考。

        下面我们切入正题。

         在我们所用过的英文单词中，许多单词都和其它的单词是相似的，而这些往往记忆起来是特别头疼的，大家都懂的。例如，对于单词wine，替换第一个字母，可以有dine、fine、line、mine、pine、vine等。替换第三个字母，就有了wide、wife、wipe、wire等。替换第四个字母，就有了wind、wing、wink、wins等。于是，通过这些变换，我们就得到了15个不同的单词（当然，还可以得到更多的单词）。现在我们想做的就是，为字典中的每一个单词都量身定做一个“集合”，这些集合的构成元素就是通过变换某一个位置的字母所能得到的“合法”的单词。

       下面来让看一下字典中单词长度的大致分布：



```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;map&gt;
#include&lt;string&gt;
#include&lt;fstream&gt;
#include&lt;iomanip&gt;

using namespace std;

/*
此函数用于从文件中获取单词并存储到向量中
*/
vector&lt;string&gt; getWords(const string &amp;path)
{
	ifstream input(path);
	vector&lt;string&gt; words;
	if (!input)
	{
		cerr &lt;&lt; "无法打开文件" &lt;&lt; endl;
		exit(EXIT_FAILURE);
	}
	string word;
	while (input &gt;&gt; word)
	{
		words.push_back(word);
	}
	return words;
}

int main()
{
	string path = "D://newfile.txt";     //文件的路径可以自行修改
	vector&lt;string&gt; words = getWords(path);
	cout &lt;&lt; "文件的大小为：" &lt;&lt; words.size() &lt;&lt; endl;
	map&lt;int, vector&lt;string&gt; &gt; wordsMap;
	for (int i = 0; i &lt; words.size(); i++)
	{
		wordsMap[words[i].size()].push_back(words[i]);
	}
	cout &lt;&lt; "单词的字母个数" &lt;&lt; "\t对应的单词的个数" &lt;&lt; endl;
	for (auto itr = wordsMap.begin(); itr != wordsMap.end(); ++itr)
	{
		cout &lt;&lt; left &lt;&lt; setw(10)&lt;&lt; itr-&gt;first &lt;&lt; right &lt;&lt; setw(10) &lt;&lt; itr-&gt;second.size() &lt;&lt; endl;
	}
	return 0;
}
```



<img src="https://img-blog.csdn.net/20170812172801764?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">

        从上图可以看出单词的大致分布情况。事实上，哪些最具有可变性的是有3、4、5个字母的单词，而较长的单词却消耗最多的时间。

        首先，我们先来说一下几个基础的模块：

（1）读取文件中单词的模块，我们交个函数getWords来实现，这在上面的程序中已经展现过了。

（2）判断两个单词是不是相似（只有一个位置的字母不同），函数为oneCharOff。

（3）输出函数printHighChangebles，用于输出最终的结果。

（4）对字典中的所有单词进行“相似”判断的函数computeAdjacentWords（有三个版本）。

       下面先看检测两个单词是否只有一个字母不同的函数：



```
/*
此函数用于比较两个单词是否是只有一个位置的字母不同
*/
bool oneCharOff(const string &amp;word1, const string &amp;word2)
{
	if (word1.size() != word2.size())
		return false;
	int diffs = 0;
	for (int i = 0; i &lt; word1.size(); i++)
	{
		if (word1[i] != word2[i])
			if (++diffs &gt; 1)
				return false;
	}
	return diffs == 1;
} 

```

```
void printHighChangeables(const map&lt; string, vector&lt;string&gt; &gt; &amp;adjWords, int minWords = 15)
{
	map&lt;string, vector&lt;string&gt; &gt;::const_iterator itr;
	for (itr = adjWords.begin(); itr != adjWords.end(); ++itr)
	{
		const pair&lt;string, vector&lt;string&gt; &gt; &amp;entry = *itr;
		const vector&lt;string&gt; &amp;words = entry.second;
		if (words.size() &gt;= minWords)
		{
			cout &lt;&lt; entry.first &lt;&lt; "(" &lt;&lt; words.size() &lt;&lt; "):";
			for (int i = 0; i &lt; words.size(); i++)
			{
				cout &lt;&lt; " " &lt;&lt; words[i];
			}
			cout &lt;&lt; endl;
		}
	}
}
```





```
//====================Timer类的定义=========================
class Timer
{
public:
	Timer();
	double elapsed_time();  //消逝，时间过去
	void reset();
private:
	clock_t start_time;
};
Timer::Timer()
{
	start_time = clock();
}
double Timer::elapsed_time()
{
	clock_t end_time = clock();
	return ((double)(end_time - start_time)) / ((double)CLK_TCK);
}
void Timer::reset()
{
	start_time = clock();
}
//======================Timer类定义结束=====================
```





##### 方法一：

```
/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	for (int i = 0; i &lt; words.size(); i++)
	{
		for (int j = i + 1; j &lt; words.size(); j++)
		{
			if (oneCharOff(words[i], words[j]))
			{
				adjWords[words[i]].push_back(words[j]);
				adjWords[words[j]].push_back(words[i]);
			}
		}
	}
	return adjWords;
}
```

```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;map&gt;
#include&lt;string&gt;
#include&lt;fstream&gt;
#include&lt;ctime&gt;
#include&lt;iomanip&gt;

using namespace std;


//====================Timer类的定义=========================
class Timer
{
public:
	Timer();
	double elapsed_time();  //消逝，时间过去
	void reset();
private:
	clock_t start_time;
};
Timer::Timer()
{
	start_time = clock();
}
double Timer::elapsed_time()
{
	clock_t end_time = clock();
	return ((double)(end_time - start_time)) / ((double)CLK_TCK);
}
void Timer::reset()
{
	start_time = clock();
}
//======================Timer类定义结束=====================

void printHighChangeables(const map&lt; string, vector&lt;string&gt; &gt; &amp;adjWords, int minWords = 15)
{
	map&lt;string, vector&lt;string&gt; &gt;::const_iterator itr;
	for (itr = adjWords.begin(); itr != adjWords.end(); ++itr)
	{
		const pair&lt;string, vector&lt;string&gt; &gt; &amp;entry = *itr;
		const vector&lt;string&gt; &amp;words = entry.second;
		if (words.size() &gt;= minWords)
		{
			cout &lt;&lt; entry.first &lt;&lt; "(" &lt;&lt; words.size() &lt;&lt; "):";
			for (int i = 0; i &lt; words.size(); i++)
			{
				cout &lt;&lt; " " &lt;&lt; words[i];
			}
			cout &lt;&lt; endl;
		}
	}
}

/*
此函数用于比较两个单词是否是只有一个位置的字母不同
*/
bool oneCharOff(const string &amp;word1, const string &amp;word2)
{
	if (word1.size() != word2.size())
		return false;
	int diffs = 0;
	for (int i = 0; i &lt; word1.size(); i++)
	{
		if (word1[i] != word2[i])
			if (++diffs &gt; 1)
				return false;
	}
	return diffs == 1;
}

/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	for (int i = 0; i &lt; words.size(); i++)
	{
		for (int j = i + 1; j &lt; words.size(); j++)
		{
			if (oneCharOff(words[i], words[j]))
			{
				adjWords[words[i]].push_back(words[j]);
				adjWords[words[j]].push_back(words[i]);
			}
		}
	}
	return adjWords;
}

/*
此函数用于从文件中获取单词并存储到向量中
*/
vector&lt;string&gt; getWords(const string &amp;path)
{
	ifstream input(path);
	vector&lt;string&gt; words;
	if (!input)
	{
		cerr &lt;&lt; "无法打开文件" &lt;&lt; endl;
		exit(EXIT_FAILURE);
	}
	string word;
	while (input &gt;&gt; word)
	{
		words.push_back(word);
	}
	return words;
}

int main()
{
	string path = "D://newfile.txt";     //文件的路径可以自行修改
	vector&lt;string&gt; words = getWords(path);
	cout &lt;&lt; "文件的大小为：" &lt;&lt; words.size() &lt;&lt; endl;
	Timer time;
	map&lt;string, vector&lt;string&gt; &gt; adjWords=computeAdjacentWords(words);
	printHighChangeables(adjWords,3);
	cout &lt;&lt; "时间为：" &lt;&lt; time.elapsed_time() &lt;&lt; endl;
	return 0;
}
```



          从上图看可以看出，这个程序的效率是底下的，共用了1887.01秒。

##### 方法二：

         对单词按照个数进行分组，这样的话在比较的时候，我们就可以避免不同长度的单词之间的比较（当然就无可避免的要多使用一部分的空间了），先来看程序，看效果，之后我们再来说原理：



```
/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	map&lt;int, vector&lt;string&gt; &gt; wordsByLength;
	for (int i = 0; i &lt; words.size(); i++)
	{
		wordsByLength[words[i].size()].push_back(words[i]);
	}
	for (auto itr = wordsByLength.begin(); itr != wordsByLength.end(); ++itr)
	{
		const vector&lt;string&gt; &amp;groupsWords = itr-&gt;second;
		for (int i = 0; i &lt; groupsWords.size(); i++)
		{
			for (int j = i + 1; j &lt; groupsWords.size(); j++)
			{
				if (oneCharOff(groupsWords[i], groupsWords[j]))
				{
					adjWords[groupsWords[i]].push_back(groupsWords[j]);
					adjWords[groupsWords[j]].push_back(groupsWords[i]);
				}
			}
		}
	}
	return adjWords;
}
```





```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;map&gt;
#include&lt;string&gt;
#include&lt;fstream&gt;
#include&lt;ctime&gt;
#include&lt;iomanip&gt;

using namespace std;


//====================Timer类的定义=========================
class Timer
{
public:
	Timer();
	double elapsed_time();  //消逝，时间过去
	void reset();
private:
	clock_t start_time;
};
Timer::Timer()
{
	start_time = clock();
}
double Timer::elapsed_time()
{
	clock_t end_time = clock();
	return ((double)(end_time - start_time)) / ((double)CLK_TCK);
}
void Timer::reset()
{
	start_time = clock();
}
//======================Timer类定义结束=====================

void printHighChangeables(const map&lt; string, vector&lt;string&gt; &gt; &amp;adjWords, int minWords = 15)
{
	map&lt;string, vector&lt;string&gt; &gt;::const_iterator itr;
	for (itr = adjWords.begin(); itr != adjWords.end(); ++itr)
	{
		const pair&lt;string, vector&lt;string&gt; &gt; &amp;entry = *itr;
		const vector&lt;string&gt; &amp;words = entry.second;
		if (words.size() &gt;= minWords)
		{
			cout &lt;&lt; entry.first &lt;&lt; "(" &lt;&lt; words.size() &lt;&lt; "):";
			for (int i = 0; i &lt; words.size(); i++)
			{
				cout &lt;&lt; " " &lt;&lt; words[i];
			}
			cout &lt;&lt; endl;
		}
	}
}

/*
此函数用于比较两个单词是否是只有一个位置的字母不同
*/
bool oneCharOff(const string &amp;word1, const string &amp;word2)
{
	if (word1.size() != word2.size())
		return false;
	int diffs = 0;
	for (int i = 0; i &lt; word1.size(); i++)
	{
		if (word1[i] != word2[i])
			if (++diffs &gt; 1)
				return false;
	}
	return diffs == 1;
}

/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	map&lt;int, vector&lt;string&gt; &gt; wordsByLength;
	for (int i = 0; i &lt; words.size(); i++)
	{
		wordsByLength[words[i].size()].push_back(words[i]);
	}
	for (auto itr = wordsByLength.begin(); itr != wordsByLength.end(); ++itr)
	{
		const vector&lt;string&gt; &amp;groupsWords = itr-&gt;second;
		for (int i = 0; i &lt; groupsWords.size(); i++)
		{
			for (int j = i + 1; j &lt; groupsWords.size(); j++)
			{
				if (oneCharOff(groupsWords[i], groupsWords[j]))
				{
					adjWords[groupsWords[i]].push_back(groupsWords[j]);
					adjWords[groupsWords[j]].push_back(groupsWords[i]);
				}
			}
		}
	}
	return adjWords;
}


/*
此函数用于从文件中获取单词并存储到向量中
*/
vector&lt;string&gt; getWords(const string &amp;path)
{
	ifstream input(path);
	vector&lt;string&gt; words;
	if (!input)
	{
		cerr &lt;&lt; "无法打开文件" &lt;&lt; endl;
		exit(EXIT_FAILURE);
	}
	string word;
	while (input &gt;&gt; word)
	{
		words.push_back(word);
	}
	return words;
}

int main()
{
	string path = "D://newfile.txt";     //文件的路径可以自行修改
	vector&lt;string&gt; words = getWords(path);
	cout &lt;&lt; "文件的大小为：" &lt;&lt; words.size() &lt;&lt; endl;
	Timer time;
	map&lt;string, vector&lt;string&gt; &gt; adjWords=computeAdjacentWords(words);
	printHighChangeables(adjWords,3);
	cout &lt;&lt; "时间为：" &lt;&lt; time.elapsed_time() &lt;&lt; endl;
	return 0;
}
```



<img src="https://img-blog.csdn.net/20170812191929835?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMjk4ODM1OTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="">         这个程序的执行结果为321.098，这个时间是方法一种结果1887.01的1/6左右，这是什么原因呢？这就分组带来的好处，减少了比对的次数。简单来说一下，假设我们有n个单词，那么相对于 第一种方法而言，这些单词要进行t1=n*(n-1)/2次的比较，而对于方法二呢，我们就是将n进行了分组，假设分为了k组，分别为m1，m2，.......，mk，则n=m1+m2+...+mk，那么比较的次数为t2=m1*(m1-1)/2+m2*(m2-1)/2+....+mk*(mk-1)/2，t1-t2=[(n²-(m1²+m2²+...+mk²)]/2，将n=m1+m2+....+mk代入化简，由于结果比较繁杂，这里就不进行展开了，有兴趣的可以自己化简下，显然是t1比t2大的，特别是当m1=m2=....=mk时，这个时候我们是可以取到极值的，t2约为t1的1/k，这个在数学中有相关的定理可以佐证。所以，分组为我们带来了显著的好处。

##### 方法三：

```
/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	map&lt;int, vector&lt;string&gt; &gt; wordsByLength;

    //分组
	for (int i = 0; i &lt; words.size(); i++)
	{
		wordsByLength[words[i].size()].push_back(words[i]);
	}
	
	//遍历单词表中的每一组
	for (auto itr = wordsByLength.begin(); itr != wordsByLength.end(); ++itr)
	{
		const vector&lt;string&gt; &amp;groupsWords = itr-&gt;second;
		int groupNum = itr-&gt;first;

		//处理每一组中的单词的各个字母
		for (int i = 0; i &lt; groupNum; i++)
		{
			map&lt;string, vector&lt;string&gt; &gt; repToWord;

			//处理该组中的所有单词
			for (int j = 0; j &lt; groupsWords.size(); j++)
			{
				string rep = groupsWords[j];
				rep.erase(i, 1);    //删除第i个位置的字母
				repToWord[rep].push_back(groupsWords[j]);  //只有第i个字母不同的单词会被放在一起
			}

			//处理第i个位置中的单词组成的map
			for (auto itr2 = repToWord.begin(); itr2 != repToWord.end(); ++itr2)
			{
				const vector&lt;string&gt; &amp;clique = itr2-&gt;second;
				if (clique.size() &gt;= 2)   //说明有两个以上的单词相似
				{
					for (int i = 0; i &lt; clique.size(); i++)
					{
						for (int j = i+1; j &lt; clique.size(); j++)
						{
							adjWords[clique[i]].push_back(clique[j]);
							adjWords[clique[j]].push_back(clique[i]);
						}
					}
				}
			}
		}

	}
	return adjWords;
}
```

```
#include&lt;iostream&gt;
#include&lt;vector&gt;
#include&lt;map&gt;
#include&lt;string&gt;
#include&lt;fstream&gt;
#include&lt;ctime&gt;
#include&lt;iomanip&gt;

using namespace std;


//====================Timer类的定义=========================
class Timer
{
public:
	Timer();
	double elapsed_time();  //消逝，时间过去
	void reset();
private:
	clock_t start_time;
};
Timer::Timer()
{
	start_time = clock();
}
double Timer::elapsed_time()
{
	clock_t end_time = clock();
	return ((double)(end_time - start_time)) / ((double)CLK_TCK);
}
void Timer::reset()
{
	start_time = clock();
}
//======================Timer类定义结束=====================

void printHighChangeables(const map&lt; string, vector&lt;string&gt; &gt; &amp;adjWords, int minWords = 15)
{
	map&lt;string, vector&lt;string&gt; &gt;::const_iterator itr;
	for (itr = adjWords.begin(); itr != adjWords.end(); ++itr)
	{
		const pair&lt;string, vector&lt;string&gt; &gt; &amp;entry = *itr;
		const vector&lt;string&gt; &amp;words = entry.second;
		if (words.size() &gt;= minWords)
		{
			cout &lt;&lt; entry.first &lt;&lt; "(" &lt;&lt; words.size() &lt;&lt; "):";
			for (int i = 0; i &lt; words.size(); i++)
			{
				cout &lt;&lt; " " &lt;&lt; words[i];
			}
			cout &lt;&lt; endl;
		}
	}
}

/*
此函数用于比较两个单词是否是只有一个位置的字母不同
*/
bool oneCharOff(const string &amp;word1, const string &amp;word2)
{
	if (word1.size() != word2.size())
		return false;
	int diffs = 0;
	for (int i = 0; i &lt; word1.size(); i++)
	{
		if (word1[i] != word2[i])
			if (++diffs &gt; 1)
				return false;
	}
	return diffs == 1;
}


/*
此函数数用于计算字典中各个单词通过变动一个字母所能得到的单词的集合
*/
map&lt;string, vector&lt;string&gt; &gt; computeAdjacentWords(const vector&lt;string&gt; &amp;words)
{
	map&lt;string, vector&lt;string&gt; &gt; adjWords;
	map&lt;int, vector&lt;string&gt; &gt; wordsByLength;

    //分组
	for (int i = 0; i &lt; words.size(); i++)
	{
		wordsByLength[words[i].size()].push_back(words[i]);
	}
	
	//遍历单词表中的每一组
	for (auto itr = wordsByLength.begin(); itr != wordsByLength.end(); ++itr)
	{
		const vector&lt;string&gt; &amp;groupsWords = itr-&gt;second;
		int groupNum = itr-&gt;first;

		//处理每一组中的单词的各个字母
		for (int i = 0; i &lt; groupNum; i++)
		{
			map&lt;string, vector&lt;string&gt; &gt; repToWord;

			//处理该组中的所有单词
			for (int j = 0; j &lt; groupsWords.size(); j++)
			{
				string rep = groupsWords[j];
				rep.erase(i, 1);    //删除第i个位置的字母
				repToWord[rep].push_back(groupsWords[j]);  //只有第i个字母不同的单词会被放在一起
			}

			//处理第i个位置中的单词组成的map
			for (auto itr2 = repToWord.begin(); itr2 != repToWord.end(); ++itr2)
			{
				const vector&lt;string&gt; &amp;clique = itr2-&gt;second;
				if (clique.size() &gt;= 2)   //说明有两个以上的单词相似
				{
					for (int i = 0; i &lt; clique.size(); i++)
					{
						for (int j = i+1; j &lt; clique.size(); j++)
						{
							adjWords[clique[i]].push_back(clique[j]);
							adjWords[clique[j]].push_back(clique[i]);
						}
					}
				}
			}
		}

	}
	return adjWords;
}

/*
此函数用于从文件中获取单词并存储到向量中
*/
vector&lt;string&gt; getWords(const string &amp;path)
{
	ifstream input(path);
	vector&lt;string&gt; words;
	if (!input)
	{
		cerr &lt;&lt; "无法打开文件" &lt;&lt; endl;
		exit(EXIT_FAILURE);
	}
	string word;
	while (input &gt;&gt; word)
	{
		words.push_back(word);
	}
	return words;
}

int main()
{
	string path = "D://newfile.txt";     //文件的路径可以自行修改
	vector&lt;string&gt; words = getWords(path);
	cout &lt;&lt; "文件的大小为：" &lt;&lt; words.size() &lt;&lt; endl;
	Timer time;
	map&lt;string, vector&lt;string&gt; &gt; adjWords=computeAdjacentWords(words);
	printHighChangeables(adjWords,3);
	cout &lt;&lt; "时间为：" &lt;&lt; time.elapsed_time() &lt;&lt; endl;
	return 0;
}



```

```
int main()
{
	string path = "D://newfile.txt";     //文件的路径可以自行修改
	vector&lt;string&gt; words = getWords(path);
	cout &lt;&lt; "文件的大小为：" &lt;&lt; words.size() &lt;&lt; endl;
	Timer time;
	map&lt;string, vector&lt;string&gt; &gt; adjWords=computeAdjacentWords(words);
	cout &lt;&lt; "时间为：" &lt;&lt; time.elapsed_time() &lt;&lt; endl;
	printHighChangeables(adjWords,3);
	return 0;
}
```

 
