
--- 
title:  一文入门 Tableau 
tags: []
categories: [] 

---
>  
  作者：Roar 
  https://zhuanlan.zhihu.com/p/71502618 
 

原谅我标题党了，今天利用难得的周末，我利用Tableau做了一个简单的入门。

既然是入门肯定会有很多深入的知识我不是很懂，不过没关系，以后如果有机会接触的话，在慢慢在工作中学呗。

不过可能会有朋友会说，你不是可以敲代码得到相应的可视化图形的吗？为什么还要用Tableau这种专业的数据分析软件呢？

那么我觉得得先认识一下什么是Tableau？

为什么是Tableau？

首先来介绍一下Tableau是什么？

有人可能会说我用excel做的数据透视表也做得很好啊，为什么要用Tableau这种死贵死贵（好像也没有特别贵)的软件呢？话说在国内有什么软件没有破解版呢？

因为我不是老板，所以就不从成本这个角度去谈，我是一个数据分析爱好者，而且也是一个图形爱好者，特别喜欢看到那些很炫酷的图形，有可能这些图形都没什么用，但是酷就行了，哈哈哈。确实Tableau能够绘制出很多炫酷的图形，比如

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdHd0anQ5cVNrVXBUVTlNSzNXZ2FaT0JpYnFreVlpYzFZWkJ4ZFY1R1BpYUJpY29UZGljdmJrQ1U0N2NnLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFhUVGFZNlJTN2Fob3V2enlPZk9NQkNMdkdLTGliU2Juam9IY2drU2hhd0hzTGlhamtwWE14RHdnLzY0MA?x-oss-process=image/format,png">

哇偶还是一个动图，是不是很炫酷。

ps：（上面的图形都是来源于网络，如果侵权立马删除）

在开始学习之前，我想先做一个思维导图来说明学习Tableau的顺序，以及想通过这篇文做到什么。得到什么。

**一、简单的认识Tableau**

我觉得学习任何一个软件？可以称Tableau为软件对吧，都会先对界面有一个基本的认识。

我使用的10.5版的Tableau，我不知道最新版本有没有什么特别好用的功能的增加

我也不免俗，先介绍一下主界面

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdHZhVG5LcDU1N1BXQ24yaWN1T0NNMXpQZUNpYVc0OElMWlVJdGliSGtFVnVSdDdkdWx3Q05zTTVVUS82NDA?x-oss-process=image/format,png">Tableau的开始页面

可以看到开始界面包含3个部分：连接，打开，探索。

首先介绍连接：连接可以直接连接文件：图中也有很多的可以连接的文件类型，这就是Tableau好用的地方，可以直接连接Excel，文本，JSON，Access数据库，PDF，空间文件

紧接着还可以连接到服务器，这个就更强大了，基本可以和目前市面上流行的服务器都能连接起来

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdEVxdjRLZXIwaFlBTTM2RUwwY2IzT25oYXFpYVBXSEdzeGo1ZWFFT2tCa0xZaWNpY1dUdFB3REI5QS82NDA?x-oss-process=image/format,png">这个是可以连接的服务器

现在主流的数据库MySQL,Oracle,Hadoop,MongoDB等都可以连接。

认识了连接以后，再来看一下打开，打开点击以后

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdEFMckRLY1ZQaWMyTTRUSVdtVlM1N1lhVmRYMFV2WjhIb1FybTd6Z3hIdWlhMllqeFRTNkVnbE13LzY0MA?x-oss-process=image/format,png">

可以看到打开工作簿直接转到了可以使用的工作簿，也就是之前保存的Tableau文件。

而最后一个探索，则是这个软件的良心的地方，有很最基础的入门视频，手把手教你入门。

当然少不了软件的更新，以及一些广告。

下面我们看一下下一个界面，数据源界面

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGliWXZWMEJjaFRjMWNKb3cySDh2a2plMmtkcjNaRnNpYlZkaWNIaWN5cVpWdmFuNU9TcnA3QXE3aEEvNjQw?x-oss-process=image/format,png">

这里我们连接一个数据（超市数据集），来更好地说明。可以看到上面通常分为3个主要区域，左侧窗格，画布和网格。

**左侧窗格**：显示连接的数据库，服务器，和数据库中的表

**画布：**这里可以连接一个或者多个数据集

**网格：** 可以查看数据源中的字段，和前1000行的数据。还可以对数据源做一般的修改，如排序，隐藏字段，创建字段，以及设置别名等。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdHRSTTJaQ0s0RWQ3VkREVWJpYk5XeVdFbUQxWGpTS1oxc2hpY21TVE1ZYjYxa1ZFanZMOWZmaDNnLzY0MA?x-oss-process=image/format,png">

**工作簿界面：**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFRnQzBqak1aRW83bFpUSE5SaWIxOHp6WVBuM25yTU5zYU9kb2tFMmFTVWxpYmJYakQyaWFDeTNNQS82NDA?x-oss-process=image/format,png">实际操作最多的界面

我们来看一下这个界面都有些什么呢？

首先可以看到左侧有一个维度和度量区域。

那么维度和度量分别代表什么意思呢？维度：在初次连接数据源的时候Tableau自动将包含离散分类信息的信息字段分配给维度，比如字符串和日期，当然维度也是可以转换为度量的

度量：Tableau会把包含定量数值的信息的字段分配给度量。

由于这个界面是以后经常用的界面，所以一些后续的一些介绍，我会在最后一步实际操作中予以介绍。

好的，到这里就把Tableau的基本界面介绍完了，下面进行第二步

**二** 、**Tableau支持的数据类型**

Tableau支持字符串，日期/日期时间，数字和布尔数据类型。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdDlVSUM1Z2I4UWpSTTFuRGZZOE5LdDBETzVIV29TWU5UcUV4QjFRNXFwOTBoczlWaG52Q0dpYncvNjQw?x-oss-process=image/format,png">

这里就以刚刚的数据集为例，这里标中的Abc代表的是文本值。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFFGZVZLc3B3MXNVUmU0clFHS0xjaWNVNmpNRDdpYVVNczNwUjFIQk9zWndVVzU4amljZVZJcmxjdy82NDA?x-oss-process=image/format,png">

上图中标记的类似于日历的图标就是日期，

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdEY4SEJoTlRGR0tsTjRmQU9KVzlpYk1rZTZVMklIWEhLWWliUXo1cmNlRXh6bFg0YjdZNGY4VFFBLzY0MA?x-oss-process=image/format,png">

而这个图形中的类似于＃代表的是数字值。

还有一种这个图里没有T|F这个就是常用的布尔值（仅限于关系数据源）

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdG9KT0JVSXdjV0prczNRWGdaQlRFOE9UWm9QZEQ4N0cwOWEwMFNzZWJrM1RJVUJrQURwNTZ2Zy82NDA?x-oss-process=image/format,png">

而上面的这个地球图表代表的是地理值（用于地图）

而如果要更改数据类型就是上面的几个操作，把数据类型改一下就好。

**三、 运算符及优先级**

Tableau支持的运算符有，算术运算符，逻辑运算符，比较运算符

**1 算术运算符**

+（加法）：用于数字表示数字相加，用于字符串表示串联，用于日期，可以将天数和日期相加。比如：'abc'+'def'='abcdef',#April 15,2004#+15=#April 30,2004#

- （减法）：同样的，用于数字表示相减，用于表达式时表示求反，用于日期，可以用于从日期中减去天数

*（乘法）：用于数字表示乘法，例如，5*4=20

/（除法）：用于数字表示除法，例如 20/4=5

%（取余）：此运算符算数字余数，5%4=1

^（乘方）：此符号等同于POWER函数，用于计算数字的指定次幂，比如 6^3=216

**2 逻辑运算符**
1. **AND** 逻辑运算且，两侧必须使用表达式或布尔值1. OR 逻辑运算或，两侧必须使用表达式或布尔值1. NOT 逻辑运算否，此运算符可用于对另一个布尔值或表达式取反
**3 比较运算符**

Tableau有很丰富的比较运算符，有==或=，&gt;,&lt;,&gt;=,&lt;=,!=等用来比较两个数字、日期、或者字符串。（ps：这个难道不是每一个编程语言里面都有的）

优先级问题：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGhOdmF5V1dwbVJQeTNnMmZLZmU4VmNQMXdoWUp0a0NtNlZYcWtMMnhqRFBIZW1oTzBkelpEZy82NDA?x-oss-process=image/format,png">

运算符优先级图形实例

**四、Tableau的基础函数**

就像Excel一样，Tableau也支持函数，而且这些函数和Excel的函数有都很像。

常见的函数
1. 数字函数
ABS(number):绝对值函数，如：ABS(-7)=7

CEILING(number）：向上取整函数,如：CEILING(3.1415)=4

FLOOR(number):向下取整函数,如：FLOOR(3.1415)=3

MIN(number，number）/MAX(number，number）这个就不用说了吧

POWER(number，number）在刚刚介绍^的时候也说过，这是一个乘方函数

SIGN(number)；这个要注意以下，这个的名字是符号函数，也就是说当数字为负时返回-1，数字为零时返回为0，数字为正时返回为1

ZN(expression）：如果表达式不为NULL，就返回表达式，如果是NULL，就返回零

2.字符串函数

学过编程语言的应该都知道，常见的字符串函数应该包含，查找，转换大小，替换，以及判断某个元素是否在字符串中。

那么我们就来看几个常用的字符串

Contains(string,substring):如果给定字符串包含指定字符串就返回True

FIND(string,substring，[start]）:返回字符在string的索引的位置，如果没有就返回0,如果设置了起始位置，就会跳过start位置前面的字符；

例如FIND("Calculation","alcu")=2、

FINDTH(string,substring,occurance)：返回指定第n个字符串的位置，其中n由occurance来定，如：FINDTH("Calculation","a",2)=7

LEFT(string,number):返回最左侧一定数量的字符

LEN(string）：求字符串的长度

REPLACE(string，substring,replacement):在string中搜索substring，然后把substring替换为repalcement，如果没找到就保持不变

SPLIT(string,delimiter,tokennumber):这个有点类似于excel中的分列，以及python读取文件时用到的参数splt

3.日期函数

Tableau也同样提供了很多的日期函数，许多日期函数使用date_part这是一个常量字符串函数。

日期的函数，特别多，包含日期的加、减、转换等

DATEADD(date_part,increment,date):返回increment和date按照date__part格式相加的值

DATEDIFF(date_part,date1,date2)：返回date1和date2按照date_part的差值_

DATEPARSE(format,string)：看了我之前写过的文章的朋友应该看到format和parse都很熟悉了吧，这个就是格式的转换，比如：DATEPARSE("dd.MMMM.yyyy"，"15.April.2004")=#April15,2004#

NOW(),TODAY(),YEAR(date)这个就不用说了吧。

4.类型转换函数

在学习函数的这一章的时候，我有一个想法，就是从这一点来说每个编程语言，以及这种应用软件都是万物本根，就是无论什么语言，都会有这些基本的操作，而且这些基本的操作都是大同小异的，数据类型，基本函数，等也是如此

类型转换就是通过特定的函数把某个数据转换为特定的数据类型；

有哪些数据类型，就应该有几个类型转换函数

STR(),DATE(),DATETIME(),INT(),FLOAT()

5.逻辑函数

主要有

CASE WHEN 语句

```
CASE expression WHEN value1 THEN return1 WHEN value2 THEN return2……ELSE
default return END

```

IIF语句

```
IIF(test,then,else,[unknown])

```

IIF语句和excel常用的if语句很相似

IF test THEN value END /IF test THEN value ELSE else END

这个语句就是和我们常见的编程语言里面里用到的语句很相似了，这个就是IF/ELSE 语句，当然还有多重的if嵌套

6.聚合函数

就是一些常用的聚合函数，比如AVG,COUNT,MAX,MEDIAN,MIN,PERCENTILE等

其实Tableau还有很多其他的函数，比如表计算函数，以及特殊的数据库函数，但是既然是入门就没必要那么深究，而且深究下去可能这一篇文要写好几万字了。

下面我们开始实操

**五、Tableau的基本操作**

5.1 创建工作表

有三种方法：1点击左上角的工作表，然后点击新建工作表

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGxqaWJZM0dmT1hvMWdGbDVCU0lQc1BaazNmbDRnTlo4QjUxcTdhOHZ2OWZQVE5YTks5VkVjMmcvNjQw?x-oss-process=image/format,png">最笨的一种方法

5.2点击左下角的图中的小图表，可以直接新建

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdEFhaEZBV0xKYWZDU2FLUkpCcFVHNVo4dUFKYktXa1VBQXJXaWFQMVVWa3lpYTlmYXhTMlRQalN3LzY0MA?x-oss-process=image/format,png">图中箭头指向的位置

5.3 点击左上角的图表下面图形中红色方框标出来的地方

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFVSaWNkaWJMcXE1aWJOYkF3cXE2THJsY2h0OEVQUk1RZ0VPTVVkY1UyWjVBM3J4Rnkxb2g1aWJvWWcvNjQw?x-oss-process=image/format,png">图中方框的位置

5.4 快捷键 ctrl + m

导出工作表

如需导出工作表，直接点击需要导出的表，然后选择导出

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdERMbnp0ekRSb1JNVTVzRXIwOUlmZW1OaWJsRlVxa3d0NUhrT1ZxbUlqN2VxSEhlMUQ4d1FJQkEvNjQw?x-oss-process=image/format,png">

用Tableau创建各种图形

虽然有各种图形，但是最基础的也就那些，对于Tableau这种专门的可视化软件来说，绘制图形是非常方便的

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFd4SFN4aWNreVNPajMya1pIM0JZdERxZVY5T29aSnFxeVpFRHQ1dlhuUzMzelk2VGlhZE9ZeGliQS82NDA?x-oss-process=image/format,png">

智能显示

就像excel中会有很多推荐的图表，Tableau中有一个智能显示，如上图所示，这里会智能推荐你一些可以使用的图表，只需要点击智能显示就能选择当前加入的数据维度和度量可以使用的图形。由于这里非常的方便，我就不再赘述了

**六、Tableau的一些高级操作**

高级的操作：比如表计算，创建字段，创建函数，聚合计算，缺失值处理。

我们来看一下各自的操作

6.1 表计算

这里使用的数据是Tableau自带的超市数据集

点击视图中的数量这一度量，添加表计算

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdE5ldko4T3B6dFVoRDFaY25iZFY2bUhnZVhwWFBXaWIxOWhsT3VYR2h6QXptd1d1b1FIVVVQbXcvNjQw?x-oss-process=image/format,png">

第一步

在计算类型这里选择总额百分比

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGljT1JRMVZoYlRMRmdQMUdCM3BGTU5NUlhDeVU4UEVzUld5bVRNUmdXVEZPblg3NGtOZHhPNUEvNjQw?x-oss-process=image/format,png">

最终的结果

在计算类型中主要有8种
1. 差异：显示绝对变化1. 百分比差异：显示变化率1. 百分比：显示为其他指定值的百分比1. 总额百分比：以总额百分比的形式显示值1. 排序：以数字形式对值进行排名1. 百分位：计算百分位数1. 汇总：显示累积总额1. 移动计算：消除短期波动以确定长期趋势
6.2 创建字段

顾名思义就是用一定的计算来获得新的度量。

如下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdDhvdVVBaWFlVXFpYmtTVUR5SFFNY1FpYXNISk5vUHhWbmRFWGJDU3ZpY1M2ZGJpY0ZWd0lzWWV0ellRLzY0MA?x-oss-process=image/format,png">

创建字段的过程

这里我使用了销售总额/销售总数量，也就是平均单价

6.3 创建参数

在分析过程种，往往需要从”计算字段“中创建新参数。

创建成功以后会显示在参数下拉表中。

6.4 聚合计算

使用聚合函数对数据进行各种聚合操作。

这里我首先创造一个利润率的计算字段

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdE5zUkJNb0JRZWZBeWhPaWNURFpKS1p2MURrenZXaWIwYlpJNkoyaWNyQ1FDbnh0UWROcHluYWhJdy82NDA?x-oss-process=image/format,png">可以看到使用了很简单的两个函数

然后添加度量名称，利润率到列中，制造商到行中

以订单日期月来做筛选

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGJoWFRRaWNJOVUzRlRSRWJWbFRRSUI3RFZ4VzE2R2VkZW9jdDlpYkJ2aWNpY0d3d28yNjcyMW5BcXcvNjQw?x-oss-process=image/format,png">按照利润从大到小排列

6.4 缺失值处理

对于缺失值，Tableau会在视图中显示。有一个隐藏显示器，可以选择保留特殊值指示器。

**七、一个实际操作**

这里我使用Tableau自带的数据集--超市。

我将使用这个数据集完成网上超市运营分析，我将从客户，配送，销售，利润，退货等五个维度，以及预测分析，所有的现有数据都是为了更好地预测未来。

客户分析将围绕各省市的交易次数，各省市利润额，客户散点图，客户交易量排名4个方面进行

7.1 各省市的交易次数

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGM3Ulp3V2FpYjExMEtQZGd1MEU1MldtS3Q2S2M1MkFORXpvWm9ob01MRENBZDZPTHVFZTFvZXcvNjQw?x-oss-process=image/format,png">通过设置以及操作以后得到的图形

操作步骤
1. 把维度（生成）拖到行功能区，经度（生成）放到列功能区，1. 把_**类别****放到标记卡的****颜色**_中1. 把_**记录数****放到标记卡的****大小**_ 中1. 把省/自治区放到标记卡的详细信息中1. 把订单日期放到筛选器上，并选择显示筛选器1. 把类别放到筛选器上，并选择显示筛选器1. 把标记卡中选择为饼图
7.2 各省市的利润

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdGhDNFRpYUJwS0lTRllXaWJ5YWhDWHJIRmxUaWFZckNkRmljbGlibHdvdEdnUTI4NmljNEcxVE53MFI5QS82NDA?x-oss-process=image/format,png">各省市的利润

操作步骤如下
1. 把类别放在列功能区，省/自治区放在行功能区1. 把利润放在标价卡的颜色中1. 把利润放在标记卡的文本中1. 把订单日期放到筛选器中，并选择显示筛选器
7.3 客户散点图

由于时间原因我就不把具体的操作步骤写出来了。因为现在已经是深夜了。。。

在这里要说一声抱歉了

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdFMwaG1KVzRZTzR4bWljang3dTVGRHVWM0l1YXpkYTZpY29OS0kzYjlURXpmeW5NT0hxelpOZHVRLzY0MA?x-oss-process=image/format,png">客户散点图

7.4 客户交易量排名

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcWI5TlR4QzJsZEdVSjI3RkxmTzAzdHcyZXJuaWNQWWQxdGliUlZVQXhyZ05XZEdEaWEzUEdtWHMzQlVsaEpEbHdnVkIzYkdrbmhpY2ZPS1EvNjQw?x-oss-process=image/format,png">

以上就是客户分析的部分

由于写到这里已经是12点钟了，明天还要上班，就先到此为止了。

明天我会把后边的部分补上，而且会用自己的数据集在做一个训练！

如果你觉得这篇文章还不错，期待能为我点个赞！

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

分享或在看是对我最大的支持
