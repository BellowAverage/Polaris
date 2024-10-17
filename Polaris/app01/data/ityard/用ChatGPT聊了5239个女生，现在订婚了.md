
--- 
title:  用ChatGPT聊了5239个女生，现在订婚了 
tags: []
categories: [] 

---
**来源：机器之心 | 编辑：陈萍、杜伟、泽南**

有事 AI 它是真上啊。

「我向一位女生求婚，ChatGPT 已经和她交流了一年。为了走到这一步，AI 已经尝试了和 5239 名女生进行过沟通……」

<img src="https://img-blog.csdnimg.cn/img_convert/e9ca372c695b89fc2b17ddd7a718bf5b.jpeg" alt="e9ca372c695b89fc2b17ddd7a718bf5b.jpeg">

**来源：https://twitter.com/biblikz/status/1752335415812501757**

最近几天，社交网络上人们正在轮番向一位俄罗斯小哥送去祝福。

23 岁的 Aleksandr Zhadan 是一名 AI 开发者，也是社交平台 TenChat 的一名产品经理。

**故事是这样开始的：**

GPT 除了搜索之外，还可以在配对后写入。这样在 50 次自动执行中，他可以获得 18 次配对。GPT 在没有 Aleksandr 的干预下根据以下 prompt 与人交流：你是一个男生，第一次和女生说话。你的任务是：邀请她约会，但不是马上。

最开始进展并不顺利，GPT-3 的约会和 DM 游戏能力很弱。Aleksandr 对它进行了改进，加入了记忆、微调和示例。为了找到最相关的女生，他通过 torchvision 在 Tinder 网络版中使用了照片识别，并根据自己的滑动进行训练。这样一来，GPT 几乎总是能正确地选择合适的女生。

随着使用 ChatGPT 和 GPT-4 API，AI 变得越来越强大了，它们可以执行几十次对话、配对、安排约会。就这样经过一年的 AI 聊天，Aleksandr 找到了自己想要携手一生的 Karina—— 善解人意、开朗活泼、善良、独立。

最终，Aleksandr 向 Karina 求婚了。

羡煞旁人之余，质疑声也有。有人认为这个故事是「AI 生成的」。

<img src="https://img-blog.csdnimg.cn/img_convert/4e07803d292b7555220433667b0ecdc7.png" alt="4e07803d292b7555220433667b0ecdc7.png">

**图源：https://twitter.com/Darkolorin/status/1753135894750458268**

也有社区对 Aleksandr 做了一个小研究，认为他很可能只是在炒作，并指出他此前用 ChatGPT 撰写大学毕业论文并获得文凭，所以非常习惯「炒作浪潮」。

<img src="https://img-blog.csdnimg.cn/img_convert/f18fbecc83c0e60b758a1befd908fa7e.png" alt="f18fbecc83c0e60b758a1befd908fa7e.png">

**图源：https://twitter.com/literallydenis/status/1753177433073664236**

去年 2 月，Alexandr 用 ChatGPT 写论文的事还被媒体报道过。

<img src="https://img-blog.csdnimg.cn/img_convert/0c3eb8be81b195224baf2caa5a6b87ae.jpeg" alt="0c3eb8be81b195224baf2caa5a6b87ae.jpeg">

Aleksandr 在俄罗斯国立人文大学进行了现代组织管理的学位论文答辩，在这名学生的故事引起公众广泛关注后，该大学还召集他进行了演讲。

**用 ChatGPT 找女友，需要几步？**

随着这位俄罗斯小哥的「事迹」越来越火，大家伙当然想知道怎么才能像他一样用 ChatGPT 找到人生的另一半。

今日，一位推特博主详细分享了 Aleksandr 如何一步步找到自己的意中人。

<img src="https://img-blog.csdnimg.cn/img_convert/8cb63341b3bde54a084abea2e34f7b07.png" alt="8cb63341b3bde54a084abea2e34f7b07.png">

**图源：https://twitter.com/8teAPi/status/1754535819493405036**

相比线下相亲，用 AI 找女友还是蛮简单的。Aleksandr Zhadan 将这个过程分为两步：
- 第一步是找女孩；- 第二步是和她聊天。
**找女孩阶段**：当 Aleksandr 在 Tinder 上找女孩时，他使用网略爬虫获取图像，最开始 Aleksandr 倾向于那些在 Tinder 上的照片超过两张的女孩。在迭代过程中，Aleksandr 训练了一个图像相似性模型，该模型能够找到与他喜欢的女孩相似的女孩照片。

<img src="https://img-blog.csdnimg.cn/img_convert/b24d88a963efaf91ee5da6d40768f41e.gif" alt="b24d88a963efaf91ee5da6d40768f41e.gif">

**在聊天阶段**：GPT-3 会主动开启对话，这个阶段给 GPT-3 的提示语是「你是个男生，第一次和这个女孩说话。你的任务不是立刻、马上要求对方干什么，而是邀请那个女孩来一次约会。」

Aleksandr 表示一开始 GPT-3 表现非常糟糕，经常忘记对话，并且由于机器人无法访问 Telegram，因此他失去了一半的潜在约会机会。更糟糕的是，机器人承诺约会时会送鲜花或巧克力…… 而真正线下约会时却没有这个环节，因而被投诉了。

<img src="https://img-blog.csdnimg.cn/img_convert/1af69d5aaa4ad0c1be768574c4c419bb.png" alt="1af69d5aaa4ad0c1be768574c4c419bb.png">

第一代约会机器人（ Datebot V1）的战报：
- 匹配了 353 个女孩的 Tinder 档案；- 总共聊了 160 次（约占匹配人数的 45%）；- 有 12 次约会（占聊天次数的 7.5%）。
面对这一结果，Aleksandr 并没有灰心，和朋友继续升级这个机器人，因此第二代机器人（Datebot V2）出现了，这次，Aleksandr 他们采用：
- GPT-4 进行聊天；- 每个聊天机器人都有一个记忆，包含最简单约会问题的背景故事；- 从 Tinderbot 切换到 Telegrambot 进行消息传递；- 集成 Google 日历，用于设置日期；- 对收到的消息进行人工循环验证。
<img src="https://img-blog.csdnimg.cn/img_convert/821b8fb92cd0b7137cec8e42e70e038f.png" alt="821b8fb92cd0b7137cec8e42e70e038f.png">

第二代机器人的结果：
- GPT-4 幻觉降至零；- 匹配了 4886 条 Tinder 个人资料；- 无数约会，Aleksandr 用「多到吓人」来形容。
<img src="https://img-blog.csdnimg.cn/img_convert/20762cacc5da6945d1a39f084a14ca61.png" alt="20762cacc5da6945d1a39f084a14ca61.png">

接下来，Aleksandr 有过很多次约会，最多的时候还和 4 个女孩周旋，直到一位名叫 Karina 的女孩出现。

在结识了 Karina 之后，Aleksandr 专门推出了第三代机器人（Datebot V3）：它被设置成只会与 Karina 聊天。

给 Datebot V3 的提示是「与 Karina 保持良好的关系，告诉我是否有什么负面的事情需要注意，或者是否需要回答问题。」

<img src="https://img-blog.csdnimg.cn/img_convert/32c68b9b0375ef8525ed5179d167ceb5.png" alt="32c68b9b0375ef8525ed5179d167ceb5.png">

在此期间，Aleksandr 还利用剩下的人脉还建立了一个新的推荐工作的副项目：
- Aleksandr 在俄罗斯就业门户网站上发现了愿意为推荐员工付费的职位空缺；- Aleksandr 将与女孩的对话与潜在的工作相匹配；- 出售 GPT-4 形成的联系人 / 关系；- 成功安排 8 名员工并获得报酬。
<img src="https://img-blog.csdnimg.cn/img_convert/92b37fee2d42ef05e2082c9441016a7c.png" alt="92b37fee2d42ef05e2082c9441016a7c.png">

随着关系的深入，Datebot V3 告诉 Aleksandr 应该与 Karina 结婚，机器人不仅提出了求婚建议，还帮忙策划了一场浪漫的求婚行动。

<img src="https://img-blog.csdnimg.cn/img_convert/c489bc14140367021eda4515b2931c0f.png" alt="c489bc14140367021eda4515b2931c0f.png">

<img src="https://img-blog.csdnimg.cn/img_convert/e795b49034f53dbaf9457a927ca97751.png" alt="e795b49034f53dbaf9457a927ca97751.png">

最终 他耗费 120 小时打造的机器人帮他找到了女友。他 表示调用 GPT API 花费 1432 美元、餐厅约会花费 200 卢布，但他的副项目帮他赚了 526 卢布，现在 他 已经向女友求婚了。

<img src="https://img-blog.csdnimg.cn/img_convert/9a073c4bc2e7cbab11637f82a432fa38.png" alt="9a073c4bc2e7cbab11637f82a432fa38.png">

总而言之，这是一个有点肆无忌惮但又温馨的故事。

虽然 Karina 一直并不知道 ChatGPT 在她与 Aleksandr 的交往中扮演的角色。当他们向婚姻登记处提交申请时，她第一次发现了这件事，不过反应很平静。他们也将于今年 8 月完婚。
- - - - - - - 