
--- 
title:  使用ChatGPT自动编写Python爬虫脚本 
tags: []
categories: [] 

---
都知道最近ChatGPT聊天机器人爆火，我也想方设法注册了账号，据说后面要收费了。

ChatGPT是一种基于大语言模型的生成式AI，换句话说它可以自动生成类似人类语言的文本，把梳理好的有逻辑的答案呈现在你面前，这完全不同于传统搜索工具。

ChatGPT不光可以回答人文、科学、情感等传统问题，还可以写代码、改bug，程序员可就急了，简直是在抢饭碗，所以网上出现各种ChatGPT让你失业的焦虑言论。

俗话说“百闻不如一见”，我试着让ChatGPT用Python去写爬虫脚本，看它到底行不行？

### **1、爬取知乎上的专栏文章**

提问：

帮我用python写代码爬取这个网站的文章 [https://zhuanlan.zhihu.com/p/595050104]

ChatGPT:

<img src="https://img-blog.csdnimg.cn/5fc4b1abf6744b72bd1971c4b1b24c8f.jpeg#pic_center" alt="在这里插入图片描述">

把给到的代码放进PyCharm中跑一遍，发现没有报错，且打印出了内容。

```
import requests
from bs4 import BeautifulSoup

url = "https://zhuanlan.zhihu.com/p/595050104"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1", class_="Post-Title").text.strip()
body = soup.find("div", class_="Post-RichText").text.strip()

print("Title:", title)
print("Body:", body)


```

<img src="https://img-blog.csdnimg.cn/b968bb846b14445085cec6d021daf00c.jpeg#pic_center" alt="在这里插入图片描述">

虽然说ChatGPT给出的代码可以执行，但它也提到由于爬取的网站会随时变更，也就是HTML会变动，所以代码可能需要调整才能正常工作。

凡是写过爬虫的同学应该都能理解，人工写的爬虫代码也没法一劳永逸，需要随时改。

这一点ChatGPT提示的很有道理。

后来我测试了medium、百家号上的文章，ChatGPT提供的代码形式几乎和上面一致，没法直接执行获取结果，需要微调后才能跑。

### **2. 爬取京东某商品的评论**

为了给ChatGPT增加难度，我试着让它去爬取某电商网站的用户评论

提问：

请用python写代码爬取这个京东商品的所有用户评论 [https://item.jd.com/13652780.html]

ChatGPT:

<img src="https://img-blog.csdnimg.cn/6b617220819e40ba88ab632daf528f3b.jpeg#pic_center" alt="在这里插入图片描述">

可能这个网页是动态页面，ChatGPT提供的方法并不能爬取评论。

我接着问：

爬取的结果是空值怎么办？

ChatGPT:

<img src="https://img-blog.csdnimg.cn/450882a2cf0848c6a90db134dc086a79.jpeg#pic_center" alt="在这里插入图片描述">

ChatGPT提供了3种可能存在的原因，但并没有帮我修改代码。

于是我又问：

还是空值 请帮我重新写代码爬取

ChatGPT:

<img src="https://img-blog.csdnimg.cn/282d6db47a86483e93cd5cc125144a08.jpeg#pic_center" alt="在这里插入图片描述">

这次就牛掰了，它重新用Selenium写了爬虫代码，并告诉我爬取动态网页需要模拟浏览器行为，因此得用selenium技术。

我没有运行去测试代码正确与否，但ChatGPT确实惊艳到我了，能够前后关联对话内容，并给出正确的解决方法。

### **3.继续更多的测试**

上面只是蜻蜓点水的玩玩，ChatGPT就已经吸引到我，

我准备多花时间去测试ChatGPT应对各种爬虫的解决方案，以及它对bug的修复能力。

仅仅从写代码层面看，ChatGPT已经可以媲美中高级程序员的水平了，而且它的知识范畴远超人类最厉害的程序员

ChatGPT能够根据对话生成人想要的内容，这是AI巨大的突破，未来它的应用之广难以想象。

### 关于Python技术储备

学好 Python 不论是就业还是做副业赚钱都不错，但要学会 Python 还是要有一个学习规划。最后大家分享一份全套的 Python 学习资料，给那些想学习 Python 的小伙伴们一点帮助！

**对于0基础小白入门：**

>  
 如果你是零基础小白，想快速入门Python是可以考虑的。 
 一方面是学习时间相对较短，学习内容更全面更集中。 二方面是可以找到适合自己的学习方案 


包括：Python激活码+安装包、Python web开发，Python爬虫，Python数据分析，人工智能、机器学习等习教程。带你从零基础系统性的学好Python！

## 零基础Python学习资源介绍

### 👉Python学习路线汇总👈

Python所有方向的技术点做的整理，形成各个领域的知识点汇总，它的用处就在于，你可以按照上面的知识点去找对应的学习资源，保证自己学得较为全面。**（全套教程文末领取哈）** <img src="https://img-blog.csdnimg.cn/img_convert/673b13641cf2ddf5e18b5c58afd50200.png#pic_center" alt="">

### 👉Python必备开发工具👈

<img src="https://img-blog.csdnimg.cn/img_convert/6be280b059df8debff4a4b52d6a6ad1f.png#pic_center" alt="">

**温馨提示：篇幅有限，已打包文件夹，获取方式在：文末**

### 👉Python学习视频600合集👈

观看零基础学习视频，看视频学习是最快捷也是最有效果的方式，跟着视频中老师的思路，从基础到深入，还是很容易入门的。 <img src="https://img-blog.csdnimg.cn/img_convert/f2a1e9c7368b6ac7d169ab4147b537f4.png#pic_center" alt="">

### 👉实战案例👈

光学理论是没用的，要学会跟着一起敲，要动手实操，才能将自己的所学运用到实际当中去，这时候可以搞点实战案例来学习。 <img src="https://img-blog.csdnimg.cn/68b02d39486d4e4c96b6cb9da7dd54de.png#pic_center" alt="在这里插入图片描述">

### 👉100道Python练习题👈

检查学习结果。<img src="https://img-blog.csdnimg.cn/img_convert/15bc30b75e1de8c9fa2daab3742d4430.png#pic_center" alt="">

### 👉面试刷题👈

<img src="https://img-blog.csdnimg.cn/img_convert/99f6475fb1237ba21e45d55c67bf83f4.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/3360d1bcb588491dac483ff4c30fb05c.png#pic_center" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/49fe592a1ae644c2822a1b4a850724cd.png#pic_center" alt="在这里插入图片描述">

###### 这份完整版的Python全套学习资料已经上传CSDN，朋友们如果需要可以微信扫描下方CSDN官方认证二维码免费领取【`保证100%免费`】

<img src="https://img-blog.csdnimg.cn/1d2a69f2d57e4d1cb444037b17af8607.png" alt="">
