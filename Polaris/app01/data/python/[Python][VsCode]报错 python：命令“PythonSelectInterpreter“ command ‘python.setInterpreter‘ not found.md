
--- 
title:  [Python][VsCode]报错 python：命令“Python:Select:Interpreter“ command ‘python.setInterpreter‘ not found 
tags: []
categories: [] 

---
## 错误情况：

在使用ctrl+shift+P后使用Python:Select:Interpreter切换解释器出错

报错如下

<img alt="" height="157" src="https://img-blog.csdnimg.cn/265cc12eb1d24d99b936c0d0c46a2aa5.png" width="683">

##  解决方案：

在左侧扩展栏目<img alt="" height="50" src="https://img-blog.csdnimg.cn/4e852ca503324831af6c61feda4567df.png" width="51">中搜索@workspaceUnsupported 

发现python在限制在受限模式下

<img alt="" height="388" src="https://img-blog.csdnimg.cn/077e41f5a1a24cf6822eea931dcd996f.png" width="296">

 点击蓝圈中选项

<img alt="" height="91" src="https://img-blog.csdnimg.cn/a0ed2e2df34e4b2382d796def464d4ee.png" width="291">

 然后选择信任，问题解决

<img alt="" height="494" src="https://img-blog.csdnimg.cn/05be748e2f0144bfa3e99894ec4e3c03.png" width="416">

 

 

 





 
