
--- 
title:  【python】python新闻内容zhua取分析词云可视化（源码）【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>【python】python新闻内容获取分析词云可视化（源码）【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- -  
   </li>- </ul> 
  
  


## 一、设计要求

通过对`搜狐新闻网页`的内容进行获取和处理，提取其中的中文文本信息。然后利用正则表达式去除非中文字符，使用`jieba`库进行中文分词，并过滤停用词。接着统计各词语的词频并按照词频降序排序，最后输出词频最高的前50个词汇。同时，根据词频生成词云图，展示文本数据的可视化结果。

网站的内容如下：

<img src="https://img-blog.csdnimg.cn/direct/b91606c858dc42598f506dbcde10d3ba.png" alt="在这里插入图片描述">

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 


主要功能实现如下：

>  
 - 使用 `requests` 库发送请求并获取指定网页的内容。- 使用 `BeautifulSoup` 库解析网页内容，提取文本信息。- 使用正则表达式去除非中文字符，只保留中文文本内容。- 使用 `jieba` 进行中文分词。- 过滤停用词（如’的’、‘和’、'是’等），并对分词结果进行处理。- 统计分词后各词语的词频，显示柱状图。- 对词频进行降序排序，并输出词频最高的前50个词。- 指定中文字体文件路径，生成词云图。- 显示生成的词云图。 


## 二、功能展示

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 


### 2.1. zhua取内容

<img src="https://img-blog.csdnimg.cn/direct/2d41dacb07444f4e84658784df97c155.png" alt="在这里插入图片描述">

### 2.2. 词频统计

```
工作: 10
报告: 10
发展: 10
政府: 8
生态环境: 5
一年: 5
江苏: 4
全文: 3
十三届: 3
全国人大: 3
五次: 3
会议: 3
新华社: 3
经济社会: 3
任务: 3
主要: 3
目标: 3
增长: 3
改善: 3
实施: 3
江苏省: 3
来源: 2
李克强: 2
总理: 2
代表: 2
国务院: 2
回顾: 2
二年: 2
总体: 2
要求: 2
政策: 2
取向: 2
三年: 2
指出: 2
统筹: 2
全年: 2
十四五: 2
今年: 2
左右: 2
城镇: 2
新增: 2
就业: 2
以上: 2
控制: 2
经济: 2
基本: 2
保持: 2
持续: 2
着力: 2
创新: 2

```

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 


使用柱状图展示词频前10名的字段。柱状图如下：

<img src="https://img-blog.csdnimg.cn/direct/c38304ac98f24a7796dc44bb22b8ecad.png" alt="在这里插入图片描述">

### 2.3. 词云展示

<img src="https://img-blog.csdnimg.cn/direct/04b9b61190ab4d7b8337d2dd8bd4dfae.png" alt="在这里插入图片描述">

## 三、代码分析

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 

<li> **导入所需的库：** <pre><code class="prism language-python">import requests
from bs4 import BeautifulSoup
import jieba
import matplotlib.pyplot as plt
import re
</code></pre> 代码导入了执行任务所需的库： 
  1. `requests`：用于向网页发送HTTP请求。1. `BeautifulSoup`：从`bs4`库，用于解析HTML和XML文档。1. `jieba`：一个中文分词库，用于处理中文文本。1. `matplotlib.pyplot`：用于数据可视化。1. `re`：正则表达式库，用于文本处理。 </li><li> **获取网页内容：** <pre><code class="prism language-python">url = "源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
</code></pre> 用`requests`库获取指定URL的内容，然后使用`BeautifulSoup`解析HTML文档。 </li><li> **提取和处理文本内容：** <pre><code class="prism language-python">text_content = soup.get_text()
text_content = re.sub(r"源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。", "", text_content)
</code></pre> `soup.get_text()`从HTML中提取所有文本。接着用正则表达式删除非中文字符。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻抓取分析 ” 获取。👈👈👈 
  </blockquote> </li><li> **分词和过滤停用词：** <pre><code class="prism language-python">words = jieba.cut(text_content)
stop_words = set(['的', '和', '是', '在', '了', '等'])
</code></pre> 使用`jieba.cut`进行分词，然后过滤掉一些常见的停用词和单字词。 </li><li> **词频统计：** <pre><code class="prism language-python">word_freq = {<!-- -->}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
</code></pre> 对分词后的词进行频率统计，记录每个词出现的次数。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻抓取分析 ” 获取。👈👈👈 
  </blockquote> </li><li> **选取前50个高频词汇：** <pre><code class="prism language-python">源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。
</code></pre> 将词频字典按频率降序排序，并选取前50个高频词。 </li><li> **绘制柱状图：** <pre><code class="prism language-python">words, freqs = zip(*sorted_word_freq)
plt.figure(figsize=(10, 6))
plt.bar(words, freqs)
plt.xlabel('词语')
plt.ylabel('词频')
plt.xticks(rotation=45)
plt.title('Top 10 Words Frequency Bar Chart')
plt.show()
</code></pre> 使用matplotlib绘制柱状图，展示这十个词及其频率。 </li><li> **绘制词云图：** 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 
  </blockquote> <pre><code class="prism language-cpp">
# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
</code></pre> </li>
>  
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻抓取分析 ” 获取。👈👈👈 
  

总体来说，这段代码通过抓取网页内容，提取中文文本，进行分词和词频统计，最后以柱状图的形式展现出最常见的10个词汇。这是一个结合了网络爬虫、自然语言处理和数据可视化的实用脚本。

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 新闻分析 ” 获取。👈👈👈 

