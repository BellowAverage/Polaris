
--- 
title:  女同桌找我要表情包，还好我会Python，分分钟给她下载几十个G... 
tags: []
categories: [] 

---
起因呢，这昨晚女同桌跟我说电脑有点卡，喊我去宿舍给她装个新系统，装系统就装系统吧，结果又说新系统表情包都没保存~

我当时就有点生气，真当我是万能的呢？

于是我直接就用Python给她爬了几十个G，完事扭头就走，任她怎么喊我也没用！

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/5780d601c352adcecc6ad7bed2aebc1a.png">

### 一、准备工作

使用的环境
- python3.8 | Anaconda- pycharm
使用的模块
- requests 第三方模块 需要手动安装- re 内置模块不需要安装
win+r 输入cmd ，确定后新窗口输入 pip install requests 即可安装成功。

插件安装

xpath helper扩展工具包

安装步骤：找助理老师获取xpath helper扩展工具包（注意：不要解压）

》》 打开Google浏览器 --&gt; 更多工具 --&gt; 扩展程序 --&gt; 打开开发者模式 --&gt; 把xpath helper扩展工具包直接拖入 --&gt; 刷新

使用方法：快捷键 ctrl+shift+X

思路流程

1、分析数据来源

第一页:https://fabiaoqing.com/biaoqing/lists/page/1.html

多页 —&gt; 第一页 --&gt; 一个

2、实现代码
- 发送请求,第一页数据- 获取数据- 解析数据,表情- 保存数据
### 二、效果展示

部分效果展示

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/00912ea6355c18eccd0f126f48a69d67.png">

### 三、代码解析

1、发送请求

第一页数据

2、获取数据

网页源代码

re 找规律

3、解析数据

.*? 精准匹配数据

4、保存数据
