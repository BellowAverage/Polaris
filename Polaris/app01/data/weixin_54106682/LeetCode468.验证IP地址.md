
--- 
title:  LeetCode468.验证IP地址 
tags: []
categories: [] 

---
**目录**















**一、题目**

`给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。`

`有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 &lt;= xi &lt;= 255 且 xi 不能包含 前导零。例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。`

`一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:`

`1 &lt;= xi.length &lt;= 4 xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。 在 xi 中允许前导零。 例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。`

` `

`示例 1：`

`输入：queryIP = "172.16.254.1" 输出："IPv4" 解释：有效的 IPv4 地址，返回 "IPv4" 示例 2：`

`输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334" 输出："IPv6" 解释：有效的 IPv6 地址，返回 "IPv6" 示例 3：`

`输入：queryIP = "256.256.256.256" 输出："Neither" 解释：既不是 IPv4 地址，又不是 IPv6 地址  `

`提示：`

`queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。`

`来源：力扣（LeetCode） 链接：`

## 二、题目解析

我们首先查找给定的字符串queryIP 中是否包含符号 ‘.’。如果包含，那么我们需要判断其是否为 IPv4 地址；如果不包含，我们则判断其是否为 IPv6 地址。

对于 IPv4 地址而言，它包含 4 个部分，用 ‘.’ 隔开。因此我们可以存储相邻两个 ‘.’ 出现的位置 last 和cur，如图所示，last和cur刚好把每个字段框住（当考虑首个部分时，last=−1；当考虑最后一个部分时，cur=n，其中 n 是字符串的长度），我们需要判断：

它的长度是否在 [1, 3]之间；

它是否只包含数字；

它的值是否在 [0,255] 之间；

它是否不包含前导零。

对于 IPv6 地址而言，它包含 8 个部分，用 ':' 隔开。同样地，我们可以存储相邻两个‘:’ 出现的位置 last 和cur，我们需要判断：

它的长度是否在 [1,4] 之间；

它是否只包含数字，或者 a-f，或者 A-F；

除了上述情况以外，如果我们无法找到对应数量的部分，那么给定的字符串也不是一个有效的 IP 地址。

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/807258b4844e49289957bf3377bc3a1d.png" width="1200">

## 三、题目代码

```
class Solution {
public:
    string validIPAddress(string queryIP) {
        if(queryIP.find('.')!=string::npos){
            //Ipv4
            int last=-1;
            int cur;
            for(int i=0;i&lt;4;i++)
            {
                cur=(i==3)?queryIP.size():queryIP.find('.',last+1);
                //当i等于3时，说明此时遍历已到达第四个字段，last+1之后的下标已经没有'.'；
                //因此为了将第四个字段框住，cur的取值应为字符串的长度
                if(cur==string::npos){
                    return "Neither";
                }
                if((cur-last-1&lt;1)||(cur-last-1&gt;3))
                {
                    return "Neither";
                }
                int addr=0;
                for(int j=last+1;j&lt;cur;j++)
                {
                    if(!isdigit(queryIP[j]))
                    {
                        return "Neither";
                    }
                    addr=addr*10+(queryIP[j]-'0');
                }
                if(addr&gt;255)
                {
                    return "Neither";
                }
                if(addr&gt;0 &amp;&amp; queryIP[last+1]=='0')
                {
                    return "Neither";
                }
                if(addr==0 &amp;&amp; cur-last-1&gt;1)
                {
                    return "Neither";
                }
                last=cur;
            }
            return "IPv4";
        }
        else{
            //IPv6
            int last=-1;
            int cur;
            for(int i=0;i&lt;8;i++)
            {
                cur=(i==7)?queryIP.size():queryIP.find(':',last+1);
                if(cur==string::npos){
                    return "Neither";
                }
                if((cur-last-1&lt;1)||(cur-last-1&gt;4))
                {
                    return "Neither";
                }
                for(int j=last+1;j&lt;cur;j++)
                {
                    if(!isdigit(queryIP[j]) &amp;&amp; !('a'&lt;=tolower(queryIP[j]) &amp;&amp; tolower(queryIP[j])&lt;='f'))
                    {
                        return "Neither";
                    }
                }
                last=cur;
            }
            return "IPv6";
        }
    }
};
```

<img alt="" height="280" src="https://img-blog.csdnimg.cn/30a51f1d822b4d4d852c7624347dcddc.png" width="985">



## **四、知识点汇总**

### **1.单引号和双引号的区别**

单引号是字符型， 双引号是字符串型 单引号引起的一个字符实际上代表一个整数。 双引号引起的字符串，代表的却是一个指向无名数组起始字符的指针。该数组会被双引号之间的字符以及一个额外的二进制为零的字符 ‘\0’ 初始化。

"a"和’a’的区别，前者是字符串，后者是字符。

实际上 ”a" 是 “a\0”，以’\0’结尾。而‘a’单单表示a这个字符。

```
string s='zhangxinguan';//error
string s="zhangxinguan";//right

```

### 2.find的用法

string中find()返回值是字母在母串中的位置（下标记录），如果没有找到，那么会返回一个特别的标记npos。（返回值可以看成是一个int型的数）

可以测试一下npos值的大小，没有固定值

**string::npos**参数 —— npos 是一个常数，用来表示不存在的位置

```
cout&lt;&lt;s.npos&lt;&lt;endl;
```

<img alt="" height="45" src="https://img-blog.csdnimg.cn/c7176020903b4f4f99483ff624e26cc2.png" width="337">

```
#include &lt;iostream&gt;

using namespace std;

int main()
{
    string s="zhangxinguau";
    //cin&gt;&gt;s;
    string::size_type position;
    position = s.find('g');
    //string对象的索引也应为size_type类型
    if(position!=s.npos)
    {
        cout&lt;&lt;"position is:"&lt;&lt;position&lt;&lt;endl;
    }
    else{
        cout &lt;&lt; "Not Found!" &lt;&lt; endl;
    }
    return 0;
}

```

## <img alt="" height="118" src="https://img-blog.csdnimg.cn/de1aa2dba69f4da7a543c67672ca6164.png" width="694">

 返回子串出现在母串中的首次出现的位置，和最后一次出现的位置。

```
#include &lt;iostream&gt;

using namespace std;

int main()
{
    string s="zhangxinguau";
    //cin&gt;&gt;s;
    string::size_type position;
    string flag = "g";
    position = s.find_first_of(flag);
    cout&lt;&lt;"s.find_first_of(flag) is :"&lt;&lt;position&lt;&lt;endl;
    position = s.find_last_of(flag);
    cout&lt;&lt;"s.find_last_of(flag) is :"&lt;&lt;position&lt;&lt;endl;
    return 0;
}

```

<img alt="" height="187" src="https://img-blog.csdnimg.cn/5564a85ed8aa4b4a9cbd8956aa247cd5.png" width="923">

## **五、总结**

题目本身没用到什么算法，主要考察对题目的理解程度，以及对应不符合的条件进行依次判断，在做题时，需要仔细不要漏掉某个判断条件;另外做题时，不要被题目的长度吓住，依次分析即可。
