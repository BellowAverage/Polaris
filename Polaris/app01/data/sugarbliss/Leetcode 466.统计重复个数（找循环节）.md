
--- 
title:  Leetcode 466.统计重复个数（找循环节） 
tags: []
categories: [] 

---
**题目链接：**

**题意：**由 n 个连接的字符串 s 组成字符串 S，记作 S = [s,n]。例如，["abc",3]=“abcabcabc”。

如果我们可以从 s2 中删除某些字符使其变为 s1，则称字符串 s1 可以从字符串 s2 获得。例如，根据定义，"abc" 可以从 “abdbec” 获得，但不能从 “acbbe” 获得。

现在给你两个非空字符串 s1 和 s2（每个最多 100 个字符长）和两个整数 0 ≤ n1 ≤ 106 和 1 ≤ n2 ≤ 106。现在考虑字符串 S1 和 S2，其中 S1=[s1,n1] 、S2=[s2,n2] 。

请你找出一个可以满足使[S2,M] 从 S1 获得的最大整数 M 。

示例：

输入： s1 ="acb",n1 = 4 s2 ="ab",n2 = 2

返回： 2

**思路： 由于题目中的 n1 和 n2 都很大，因此我们无法真正把 S1 = [s1, n1] 和 S2 = [s2, n2] 都显式地表示出来。由于这两个字符串都是不断循环的，因此我们可以考虑找出 s2 在 S1 中出现的循环节，如果我们找到了循环节，那么我们就可以很快算出 s2 在 S1 中出现了多少次了。**

**首先了解几个数组的含义：**
- vector&lt;int&gt; repeatCnt(105, 0)；repeatCnt[ k ]表示遍历完前k个s1成功匹配了多少个s2，初始化为0.- vector&lt;int&gt; nextIdx(105, -1)；nextIdx[ j ] = k表示遍历完前k个s1，匹配到s2[ j ]这个位置，初始化为-1.
**我们在遍历完第k个s1之后，看看s1想匹配的s2中的字符的在s2中的位置，比如s1=abc，s2=abb,那遍历完第一个s1后，nextIdx[2]=1，在之后的遍历过程中nextidx数组如果在之前出现过，就说明找到了循环节。**

**当nextIdx[j] != -1时，表示出现循环节并且循环节的开始位置为start = nextIdx[j] + 1，那么循环节的起始位置是[start+1,k]（其中k是遍历到第k个s1），那么循环节的长度就是interval = k - start + 1，那么在S1中存在多少个循环节呢？ 就是等于repeat = (n1 - start + 1) / interval，而这些循环节可以贡献多少个成功匹配的s2呢。那就看看每个循环节可以匹配成功多少个s2也就是(repeatCnt[k] - repeatCnt[start-1]) ;（想想为啥是start-1，举个栗子：我们让sum[i]表示前i个数的和，我们要计算区间[i, j]的和，是不是sum[j] - sum[i-1]），循环过程成功匹配s2的个数也就是：patternCnt = (repeatCnt[k] - repeatCnt[start-1]) * repeat;**

**这个时候循环的部分是计算完了，还剩下S1中的头和尾巴匹配的个数没算，因为匹配的是子序列，所以这俩可以合在一起算，头部和尾部s1的个数就是start - 1 + (n1 - start + 1) % interval，成功匹配s2的个数显然就是repeatCnt[start - 1 + (n1 - start + 1) % interval]; 循环部分与两头的个数之和再除以n2即为所求。**

**至此循环节部分算是结束了，但是如果不存在循环节呢？那就更简单了，答案就是：repeatCnt[n1] / n2。**

```
class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        vector&lt;int&gt; repeatCnt(105, 0);//记录遍历完前k个s1成功匹配了多少个s2
        vector&lt;int&gt; nextIdx(105, -1);//记录遍历完s1，匹配到s2哪个位置
        int j = 0, cnt = 0;
        for (int k = 1; k &lt;= n1; ++k) {
            int tag = 0;
            for (int i = 0; i &lt; s1.size(); ++i) {
                if (s1[i] == s2[j]) {
                    ++j;
                    tag = 1;
                    if (j == s2.size()) {  
                        j = 0;
                        ++cnt;//记录成功匹配的个数
                    }
                }
            }
            if(tag == 0)return 0;
            repeatCnt[k] = cnt;
            if(nextIdx[j] != -1){//存在循环节
                int start = nextIdx[j] + 1;//循环节开始的位置
                int interval = k - start + 1;//循环节的长度
                int repeat = (n1 - start + 1) / interval;//循环的次数
                int patternCnt = (repeatCnt[k] - repeatCnt[start-1]) * repeat;//patternCnt表示循环过程中成功匹配了多少个s2（循环节内成功匹配s2的个数乘以循环次数）
                int remainCnt = repeatCnt[start - 1 + (n1 - start + 1) % interval];//中间循环的计算完成，两头的合在一起计算即可。
                return (patternCnt + remainCnt) / n2;
            }
            else{
                nextIdx[j] = k;
            }
           
        }
        return repeatCnt[n1] / n2;//没有循环节的情况
    }
};
```
