
--- 
title:  python如何生成excel图表,python图形界面生成exe 
tags: []
categories: [] 

---
本篇文章给大家谈谈python如何生成excel图表，以及python图形界面生成exe，希望对各位有所帮助，不要忘了收藏本站喔。



<img alt="" height="500" src="https://img-blog.csdnimg.cn/img_convert/4ba4a6fe83ab2b8173ebb84c8d844baf.gif" width="716">

大家都知道，Matplotlib 是众多 Python 可视化包的鼻祖，也是Python最常用的标准可视化库，其功能非常强大，同时也非常复杂，想要搞明白并非易事。但自从Python进入3.0时代以后，pandas的使用变得更加普及，它的身影经常见于市场分析、爬虫、金融分析以及科学计算中。

作为数据分析工具的集大成者，pandas作者曾说，pandas中的可视化功能比plt更加简便和功能强大。实际上，如果是对图表细节有极高要求，那么建议大家使用matplotlib通过底层图表模块进行编码。当然，我们大部分人在工作中是不会有这样变态的要求的，所以一句import pandas as pd就足够应付全部的可视化工作了。下面，我们总结一下PD库的一些使用方法和入门技巧。



#### 一、线型图 

#### 

对于pandas的内置数据类型，Series 和 DataFrame 都有一个用于生成各类 图表 的 plot 方法。 默认情况下， 它们所生成的是线型图。其实Series和DataFrame上的这个功能只是使用`matplotlib`库的`plot()`方法的简单包装实现。参考以下示例代码 -

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))

df.plot()
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzM4NTE4MTEyMl85NzY4Ni5wbmc?x-oss-process=image/format,png">

如果索引由日期组成，则调用`gct().autofmt_xdate()`来格式化`x`轴，如上图所示。

我们可以使用`x`和`y`关键字绘制一列与另一列。







```
s = Series( np. random. randn( 10). cumsum(), index= np. arange( 0, 100, 10))
s. plot()
```



<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWctYmxvZy5jc2RuLm5ldC8yMDE4MDMxNjE4MzkxMzMzOT93YXRlcm1hcmsvMi90ZXh0L0x5OWliRzluTG1OelpHNHVibVYwTDNGeFh6TTVOVEl4TlRVMC9mb250LzVhNkw1TDJUL2ZvbnRzaXplLzQwMC9maWxsL0kwSkJRa0ZDTUE9PS9kaXNzb2x2ZS83MA?x-oss-process=image/format,png">





pandas 的大部分绘图方法都有 一个 可选的ax参数， 它可以是一个 matplotlib 的 subplot 对象。 这使你能够在网格 布局 中 更为灵活地处理 subplot 的位置。 DataFrame的plot 方法会在 一个 subplot 中为各列绘制 一条 线， 并自动创建图例（ 如图所示）：  

```
df = DataFrame( np. random. randn( 10, 4). cumsum( 0), ...: columns=[' A', 'B', 'C', 'D'], index= np. arange( 0, 100, 10)) 

df. plot() 
```

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWctYmxvZy5jc2RuLm5ldC8yMDE4MDMxNjE4NDEyMjE_d2F0ZXJtYXJrLzIvdGV4dC9MeTlpYkc5bkxtTnpaRzR1Ym1WMEwzRnhYek01TlRJeE5UVTAvZm9udC81YTZMNUwyVC9mb250c2l6ZS80MDAvZmlsbC9JMEpCUWtGQ01BPT0vZGlzc29sdmUvNzA?x-oss-process=image/format,png">



#### 



#### 二、柱状图 

#### 

在生成线型图的代码中加上 kind=' bar'（ 垂直柱状图） 或 kind=' barh'（ 水平柱状图） 即可生成柱状图。 这时，Series 和 DataFrame 的索引将会被用 作 X（ bar） 或 （barh）刻度： 

```
In [59]: fig, axes = plt. subplots( 2, 1) 

In [60]: data = Series( np. random. rand( 16), index= list(' abcdefghijklmnop')) 

In [61]: data. plot( kind=' bar', ax= axes[ 0], color=' k', alpha= 0. 7) 

Out[ 61]: &lt; matplotlib. axes. AxesSubplot at 0x4ee7750&gt; 

In [62]: data. plot( kind=' barh', ax= axes[ 1], color=' k', alpha= 0.
```



对于 DataFrame， 柱状 图 会 将 每一 行的 值 分为 一组， 如图 8- 16 所示： 



```
In [63]: df = DataFrame( np. random. rand( 6, 4), ...: index=[' one', 'two', 'three', 'four', 'five', 'six'], ...: columns= pd. Index([' A', 'B', 'C', 'D'], name=' Genus')) 

In [64]: df 

Out[ 64]: 

Genus 

          A         B         C         D 
one 0. 301686 0. 156333 0. 371943 0. 270731 
two 0. 750589 0. 525587 0. 689429 0. 358974 
three 0. 381504 0. 667707 0. 473772 0. 632528 
four 0. 942408 0. 180186 0. 708284 0. 641783 
five 0. 840278 0. 909589 0. 010041 0. 653207 
six 0. 062854 0. 589813 0. 811318 0. 060217 

In [65]: df. plot( kind=' bar')
```

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWctYmxvZy5jc2RuLm5ldC8yMDE4MDMxNjE4NDMzNDMwMz93YXRlcm1hcmsvMi90ZXh0L0x5OWliRzluTG1OelpHNHVibVYwTDNGeFh6TTVOVEl4TlRVMC9mb250LzVhNkw1TDJUL2ZvbnRzaXplLzQwMC9maWxsL0kwSkJRa0ZDTUE9PS9kaXNzb2x2ZS83MA?x-oss-process=image/format,png">











#### 三、条形图

#### 

现在通过创建一个条形图来看看条形图是什么。条形图可以通过以下方式来创建 -

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar()
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzIyMDE4MTEzM18zNTE2NS5wbmc?x-oss-process=image/format,png">

要生成一个堆积条形图，通过指定：pass stacked=True -

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(stacked=True)
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzcyNjE4MTEzNV81MTgxMy5wbmc?x-oss-process=image/format,png">

要获得水平条形图，使用`barh()`方法 -

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

df.plot.barh(stacked=True)
</code>
```

#### 

#### 四、直方图

#### 

可以使用`plot.hist()`方法绘制直方图。我们可以指定`bins`的数量值。

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame({<!-- -->'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.plot.hist(bins=20)
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzM1NDE4MTE0MF83MjAxNy5wbmc?x-oss-process=image/format,png">

要为每列绘制不同的直方图，请使用以下代码 -

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df=pd.DataFrame({<!-- -->'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.hist(bins=20)
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzUzMjE4MTE0Ml82MDkzNy5wbmc?x-oss-process=image/format,png">

#### 

#### 五、箱型图



Boxplot可以绘制调用`Series.box.plot()`和`DataFrame.box.plot()`或`DataFrame.boxplot()`来可视化每列中值的分布。

例如，这里是一个箱形图，表示对`[0,1)`上的统一随机变量的`10`次观察的五次试验。

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box()
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzY5MzE5MTEyOF8yOTYyOC5wbmc?x-oss-process=image/format,png">

#### 

#### 六、块型图



可以使用`Series.plot.area()`或`DataFrame.plot.area()`方法创建区域图形。

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area()
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzkzNjE5MTEzMF8xODk0NS5wbmc?x-oss-process=image/format,png">

#### 

#### 七、散点图



可以使用`DataFrame.plot.scatter()`方法创建散点图。

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzYwNTE5MTEzMV85NjkxOS5wbmc?x-oss-process=image/format,png">

#### 

#### 八、饼状图



饼状图可以使用`DataFrame.plot.pie()`方法创建。

```

<code class="language-python" style="margin-left:0px;">import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True)
</code>
```

执行上面示例代码，得到以下结果 -

<img alt="" class="has" height="246" src="https://imgconvert.csdnimg.cn/aHR0cDovL3d3dy55aWliYWkuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMTcxMS8wNTExLzU3MTE5MTEzMl8yNDMyNC5wbmc?x-oss-process=image/format,png" width="379">

  

#### 参考文章：

[1] 

[2]** Python for Data Analysis，Wes McKinney，public in 2012**
