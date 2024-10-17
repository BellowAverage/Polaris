
--- 
title:  用ChatGPT生成Excel公式，太方便了 
tags: []
categories: [] 

---
来源丨机器之心

ChatGPT 自去年 11 月 30 日 OpenAI 重磅推出以来，这款 AI 聊天机器人迅速成为 AI 界的「当红炸子鸡」。一经发布，不少网友更是痴迷到通宵熬夜和它对话聊天，就为了探究 ChatGPT 的应用天花板在哪里，经过试探不少人发现，ChatGPT 似乎像个全能战士，可以聊天、写代码、修改 bug、做智能音箱、写神经网络……

但是！作为一名资深打工者，平时工作中 Word、PPT、Excel 等必不可少，要是能将 ChatGPT 整合进这些应用软件简直不要太开心。这方面微软已经在紧锣密鼓的进行了。

微软的动作到底有多迅速，我们一时半会还猜不出来，但是已经有人坐不住了，**这位名叫 PyCoach 的 AI 爱好者开始用 ChatGPT 写 Excel 公式，工作效率妥妥提高 10 倍**。

<img src="https://img-blog.csdnimg.cn/img_convert/d584d45f0bd3d1d5ced91ba764891c47.png" alt="d584d45f0bd3d1d5ced91ba764891c47.png">

PyCoach 表示，我们需要做的是创建有效提示，从而使得 ChatGPT 可以生成 Excel 公式和宏。

使用过 ChatGPT 的人都知道，提示占据非常重要的位置。而 Word，Excel、PPT 这办公三大件中，当属 Excel 最难搞，想要熟练掌握它，需要记住很多公式。但是使用提示就简单多了，和 ChatGPT 聊聊天就能解决问题。

<img src="https://img-blog.csdnimg.cn/img_convert/332d600569e4a2cd1ff73e18d9030b4b.png" alt="332d600569e4a2cd1ff73e18d9030b4b.png">

下面我们看看 PyCoach 是如何实现的。

**使用 ChatGPT 完成 Excel 公式**

首先你需要创建一个账户，注册成功后得到如下界面：

<img src="https://img-blog.csdnimg.cn/img_convert/a3f0fbf4cb5524b1f75eb52ee10f1a75.png" alt="a3f0fbf4cb5524b1f75eb52ee10f1a75.png">

创建账户地址：https://chat.openai.com/auth/login

接下来是使用 ChatGPT 完成 Excel 公式。在使用 Excel 时，我们常常会利用其自带的计算函数，包括数据库函数、日期与时间函数、统计函数等。这些函数分别有自己的名称和格式，调用时需要按照规定格式准确输入参数，这给 Excel 用户带来了一些使用负担。

但是现在，我们用自然语言「告诉」ChatGPT 要计算的内容就可以了。我们以下面这张全年收入支出数据表为例，假设我们是 Excel 新手，不知道如何将 Expenses 列的值相加。

<img src="https://img-blog.csdnimg.cn/img_convert/5bc111607fedf7253f49d83a32222cc2.png" alt="5bc111607fedf7253f49d83a32222cc2.png">

**SUM**

在这种情况下（当我们想要对一些数据进行求和），我们只需要告诉 ChatGPT 要对哪些数据求和，它就会输出一个已经代入实际参数的公式。例如：

<img src="https://img-blog.csdnimg.cn/img_convert/438965ce2f48b3dfa186340780e533eb.png" alt="438965ce2f48b3dfa186340780e533eb.png">

ChatGPT 就像是一个精通 Excel 的小助手，我们把它写好的公式放到 B14 单元格里就能得到 B2 到 B13 单元格里数据的和。

有时，我们对一个 Excel 表格有多个问题，这时我们也可以对 ChatGPT 连续提问。例如对于上面的收入支出数据表，想知道 1. 月支出超过 100000 美元的次数；2. 未支付的费用总计多少，我们就可以询问 ChatGPT 获得计算公式：

**COUNTIF**

这一步是计算月支出超过 100000 美元的次数：

<img src="https://img-blog.csdnimg.cn/img_convert/af50bb7fb599ac4f8d7f1e5e5a9ab099.png" alt="af50bb7fb599ac4f8d7f1e5e5a9ab099.png">

**SUMIF**

这一步是对「已支付」状态栏中标记为「否（No）」的费用求和：

<img src="https://img-blog.csdnimg.cn/img_convert/15d2ea4ea8c7dceeb3b42b0798b4e453.png" alt="15d2ea4ea8c7dceeb3b42b0798b4e453.png">

特别是对于一些复杂的函数，如果我们记不清其参数格式，就可以让 ChatGPT 帮忙写出正确格式，例如 VLOOKUP：

<img src="https://img-blog.csdnimg.cn/img_convert/63d4f249216d96c56ab543b79f9e76a5.png" alt="63d4f249216d96c56ab543b79f9e76a5.png">

**提取数据**

接下来挑战任务升级。假设我们有下面的电话号码列表，我们想要额外的区号（area code），即前面括号内容。

<img src="https://img-blog.csdnimg.cn/img_convert/3f706e55c7fa4ad5a2ee9bf3570fdae3.png" alt="3f706e55c7fa4ad5a2ee9bf3570fdae3.png">

向 ChatGPT 描述此任务：

<img src="https://img-blog.csdnimg.cn/img_convert/25e019d1cfac550463bfa24514d93afb.png" alt="25e019d1cfac550463bfa24514d93afb.png">

下面是 ChatGPT 生成的公式：

```
=MID (A1,FIND ("(",A1)+1,FIND (")",A1)-FIND ("(",A1)-1)
```

我们唯一要做的修改就是用 A2 替换 A1，然后就可以得出结果！

<img src="https://img-blog.csdnimg.cn/img_convert/ab2cae219905e58e00ee4e4bff56425b.png" alt="ab2cae219905e58e00ee4e4bff56425b.png">

**计算唯一值**

接下来我们数一下列 B 中有多少唯一的区号（area codes）。如下图所示，ChatGPT 生成了非常复杂的公式，但这些公式不起作用。究其原因，可能是 ChatGPT 记住了对话中的每一个细节。我们可以试着提问一个一般性的问题来解决：

<img src="https://img-blog.csdnimg.cn/img_convert/63c5b15e9d6a1e00b9fbc0faa3654ae7.png" alt="63c5b15e9d6a1e00b9fbc0faa3654ae7.png">

ChatGPT 生成的公式如下

```
=SUMPRODUCT (1/COUNTIF (range, range))
```

如果加上区号所在的范围，公式又变成如下方式：

```
=SUMPRODUCT (1/COUNTIF (B2:B9, B2:B9))
```

**使用 ChatGPT 创建宏**

接下来让我们尝试使用 VBA 创建一个简单的宏，按 tab 名对 sheet 进行排序。

<img src="https://img-blog.csdnimg.cn/img_convert/f87e44034879cf808980dd72f52bc68a.png" alt="f87e44034879cf808980dd72f52bc68a.png">

由上图可得，ChatGPT 出现了错误，这时我们需要向 ChatGPT 描述错误，并进行 debug。

<img src="https://img-blog.csdnimg.cn/img_convert/1602b9e0ad14cba8225aa50f41ac642d.png" alt="1602b9e0ad14cba8225aa50f41ac642d.png">

一番调试后，ChatGPT 完成了工作，但没有达到预期。除此以外，ChatGPT 通过 tab 名对 sheets 进行排序，它将其中一个 tab 名更改为 temp。

以上就是 PyCoach 对 ChatGPT 的探索，可以看出 ChatGPT 还是很有帮助的，还在为写 Excel 公式头疼的小伙伴，可以试一试了。

**原文链接：**

**https://artificialcorner.com/10x-your-productivity-in-excel-with-chatgpt-6f9536e46d7e**
- - - - - 