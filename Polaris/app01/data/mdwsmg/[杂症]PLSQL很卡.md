
--- 
title:  [杂症]PLSQL很卡 
tags: []
categories: [] 

---
## PLSQL症状如下：
- 1、PLSQL隔段时间没用再执行语句时会很卡- 2、就是很卡，干啥都卡
## 目前网上的方法汇总如下：
-  1、Tools &gt;&gt; Preferesnces &gt;&gt; Oracle &gt;&gt; Connection 打开自动连接 勾选检查连接、勾选所有会话，设置成功后点击应用，然后点击确定会退出首选项，然后再点进来检查一遍。 <img src="https://img-blog.csdnimg.cn/75e4cad7f175416fb9de5c8d4027c068.png" alt="在这里插入图片描述"> -  2、在Other选项中，关闭更新与消息，还是点击应用然后确定，再进来检查 <img src="https://img-blog.csdnimg.cn/b304f236bd1f4ed6948f4339ec9ce841.png" alt="在这里插入图片描述"> -  3、开启PLSQL管理员模式 右键程序，选择属性，然后选择“以管理员模式”启动 <img src="https://img-blog.csdnimg.cn/75a235ddae9b485894462e23e8d032b9.png" alt="在这里插入图片描述"> 