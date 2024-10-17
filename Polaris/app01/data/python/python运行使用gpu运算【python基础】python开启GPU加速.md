
--- 
title:  python运行使用gpu运算【python基础】python开启GPU加速 
tags: []
categories: [] 

---
1.首先需要确认是否成功安装cuda，代码见图一；打印结果如图二所示。

<img alt="" height="240" src="https://img-blog.csdnimg.cn/8c89ead376a34ac888cb61ede8251cc5.png" width="543">

 图一

 

<img alt="" height="137" src="https://img-blog.csdnimg.cn/eab1930265d54701b285e6858dcc4dda.png" width="651">

图二 

2.如果未安装成功可以自行搜索，不麻烦；安装成功后需要分三步设置使用GPU，以简单的softmax分类器为例：

a.导入os模块

b.将模型放进GPU中运算。

<img alt="" height="199" src="https://img-blog.csdnimg.cn/d7b97115397a4485859bf2a6fcfc18cc.png" width="785">

 c.更改训练、测试两个步骤，使用GPU运算。

<img alt="" height="278" src="https://img-blog.csdnimg.cn/f26ab52269904a1f90c8ebf746570b64.png" width="726">

<img alt="" height="294" src="https://img-blog.csdnimg.cn/f3d289233b94446fa7671d867c86c6c2.png" width="715"> 

 


