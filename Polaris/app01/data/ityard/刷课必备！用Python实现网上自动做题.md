
--- 
title:  刷课必备！用Python实现网上自动做题 
tags: []
categories: [] 

---
来源：blog.csdn.net/XM67_/article/details/132641455

```
👉 Python练手必备
👉 Python毕设实战项目
👉 Python爬虫实战必备
👉 30款Python小游戏附源码

👉 Python清理微信单向好友神器
```

### 前言

开学少不了老师会布置一些 软件上面的作业，今天教大家用python制作自动答题脚本，100%准确率哦~喜欢的同学记得关注、收藏哦~

### 环境使用
- Python3.8- Pycharm
### 模块使用
- import requests —&gt; 数据请求模块 pip install requests- import parsel —&gt; 数据解析模块 pip install parsel- from selenium import webdriver —&gt; 自动测试模块 pip install selenium==3.141.0
### 实现思路

##### 1.打开考试网站

selenium --&gt; 浏览器驱动 --&gt; 操作浏览器 &lt;模拟人的行为做操作浏览器&gt;

##### 2.获取答案

获取答案网站链接 获取问题以及答案内容

##### 3.对比题目以及答案，选出正确答案

获取问题答案选项 和正确的答案进行对比 如果正确答案和选择答案一致, 那就进行点击

##### 4.进行点击答题

### 最终效果

### 

<img src="https://img-blog.csdnimg.cn/img_convert/46ca472e3d05fe18452b3c6433a59d19.gif" alt="46ca472e3d05fe18452b3c6433a59d19.gif">

##### 导入模块

<img src="https://img-blog.csdnimg.cn/img_convert/bea846140c37dea9edbe698e432dc86c.png" alt="bea846140c37dea9edbe698e432dc86c.png">

##### 打开浏览器 webdriver.Chrome(‘驱动路径’)
- 1.驱动和代码放在一起- 2.驱动文件和python安装目录放在一起
<img src="https://img-blog.csdnimg.cn/img_convert/d3650c536dfaaee7d6403b9dcaa0556a.png" alt="d3650c536dfaaee7d6403b9dcaa0556a.png">

##### 输入网址

<img src="https://img-blog.csdnimg.cn/img_convert/0725c17731f20076c860dd424d8ed331.png" alt="0725c17731f20076c860dd424d8ed331.png">

##### 获取问题及答案

<img src="https://img-blog.csdnimg.cn/img_convert/6f05b39c8ccdc142e924429071579a49.png" alt="6f05b39c8ccdc142e924429071579a49.png">

##### 点击判断

<img src="https://img-blog.csdnimg.cn/img_convert/2033e8c1ae73eef20b162cbe17030e9d.png" alt="2033e8c1ae73eef20b162cbe17030e9d.png">

##### 点击提交试卷

如果过快,可能程序还没找到元素 &lt;网页还没加载元素出来, 你就直接点了, 可能报错&gt;

<img src="https://img-blog.csdnimg.cn/img_convert/aa9434c5a85f06b8238e2c08a785c34e.png" alt="aa9434c5a85f06b8238e2c08a785c34e.png">
