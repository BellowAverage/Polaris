
--- 
title:  命令提示符启动不了mysql，提示发生系统错误 5。拒绝访问。解决办法 
tags: []
categories: [] 

---
### 命令提示符启动不了mysql，提示发生系统错误 5。拒绝访问。

在dos下运行net start mysql 不能启动mysql！提示发生系统错误 5；拒绝访问！ **问题截图如下：**<img src="https://img-blog.csdnimg.cn/6c4b7b2377474a8a8fc8d6fd3c22cbab.png" alt="在这里插入图片描述"> **解决办法：** 首先确定系统环境变量path里面设置了MySQL安装地址中的bin目录地址 <img src="https://img-blog.csdnimg.cn/b2d24b779d7b47aab605677e3dd33a5f.png" alt="在这里插入图片描述"> 然后 　用管理员身份来运行cmd程序：

1.在**开始菜单的搜索框**张收入cmd，然后右键单击，并选择以管理员身份运行；

2.右键单击cmd选择“附到【开始】菜单(U)”;这是就可以到开始菜单上找到cmd了；

<img src="https://img-blog.csdnimg.cn/f176711a76e948efab3ff311f3e9c7f1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/373d441de5a946549cfd1b7b8ac392ee.png" alt="在这里插入图片描述"> 输入mysql -uroot -p;回车 再输入你的数据库密码，就可以操作数据库啦！ <img src="https://img-blog.csdnimg.cn/ea8fd73baa2f4606bf70a414526d7aa0.png" alt="在这里插入图片描述">

到这里就解决啦！有用的话点个赞支持一下再走呗！！！
