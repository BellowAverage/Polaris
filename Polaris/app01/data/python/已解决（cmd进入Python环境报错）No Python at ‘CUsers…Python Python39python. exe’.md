
--- 
title:  已解决（cmd进入Python环境报错）No Python at ‘C:Users…Python Python39python. exe’ 
tags: []
categories: [] 

---
<mark>已解决（cmd进入Python环境报错）No Python at ‘C:\Users…\Python \Python39\python. exe’</mark>



#### 文章目录
- - - - - 


## 报错代码

**粉丝群里面的一个小伙伴提出的问题他重新安装Python后，在cmd控制台输入python却没法进入python环境（当时他心里瞬间凉了一大截，跑来找我求助，然后顺利帮助他解决了，顺便记录一下希望可以帮助到更多遇到这个bug不会解决的小伙伴），报错代码如下：**：

<img src="https://img-blog.csdnimg.cn/17ad363de6ed4dbaae689edb5be617fc.png" alt="在这里插入图片描述">  

**报错信息截图**：

<img src="https://img-blog.csdnimg.cn/41f1539aa36d4d6b906ef1b99ea5dbc7.png" alt="在这里插入图片描述">

## 报错翻译

**报错内容翻译：** 

没有Python ‘C:\Users\Admini strator\AppData\Local\Programs\Py thon\Python39\python。exe’

## 报错原因

**报错原因**： 

他之前用的Python3.9，卸载后安装的Python3.8，虚拟环境保留了旧python环境的配置，导致无法在cmd中使用新的python（已配置路径）。<mark>小伙伴们根据下面的解决方法设置即可解决问题！！！</mark>

## 解决方法

**1. 删除之前Python3.9的所有的虚拟环境文件和路径**

**2. 环境变量中删除之前的配置改成现在的**

**3. 重启电脑**

**以上是此问题报错原因的解决方法，欢迎评论区留言讨论是否能解决，<mark>如果有用欢迎点赞收藏文章谢谢支持，博主才有动力持续记录遇到的问题</mark>！！！**

## 千人全栈VIP答疑群联系博主帮忙解决报错

**由于博主时间精力有限，每天私信人数太多，没办法每个粉丝都及时回复，<font size="4" color="red">所以优先回复VIP粉丝，可以通过订阅限时9.9付费专栏进入千人全栈VIP答疑群，获得优先解答机会（代码指导、远程服务），白嫖80G学习资料大礼包，专栏订阅地址：</font>**
-  **优点**：<mark>作者优先解答机会（代码指导、远程服务），群里大佬众多可以抱团取暖（大厂内推机会），此专栏文章是专门针对零基础和需要进阶提升的同学所准备的一套完整教学，从0到100的不断进阶深入，后续还有实战项目，轻松应对面试！</mark> -  **专栏福利**：<mark>简历指导、招聘内推、每周送实体书、80G全栈学习视频、300本IT电子书：Python、Java、前端、大数据、数据库、算法、爬虫、数据分析、机器学习、面试题库等等</mark> -  **注意**：如果希望得到及时回复，订阅专栏后私信博主进千人VIP答疑群<img src="https://img-blog.csdnimg.cn/b58bb765c2fc4b6abac91c2e433dd06f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9c855cea92904ab5b9575e637bdf5ea4.png" alt="在这里插入图片描述"> 
<img src="https://img-blog.csdnimg.cn/a74f7d5d03234f7c8a635562034442a0.gif#pic_center" alt="在这里插入图片描述">
