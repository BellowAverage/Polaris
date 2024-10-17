
--- 
title:  VScode配置Python开发环境 
tags: []
categories: [] 

---
打开vscode，选择扩展商店，搜索python,点击安装

<img alt="" height="413" src="https://img-blog.csdnimg.cn/39aeecbe3c0842d896334a5c3248ee3f.png" width="271">

 点击    文件——首选项——设置，点击右上角的“打开设置(json)”，打开配置文件 Settings.json 

<img alt="" height="785" src="https://img-blog.csdnimg.cn/d9a5ee10314b448cb2f52f37fa8c96c7.png" width="587">

<img alt="" height="641" src="https://img-blog.csdnimg.cn/786bc52318aa40c6b823f26b29b01509.png" width="987">



输入一下内容,D:\\lyf\\python\\data\\Python-2.7.9\\python.exe是我的安装路径，选择自己的就行

{<!-- -->

    "python.defaultInterpreterPath": "D:\\lyf\\python\\data\\Python-2.7.9\\python.exe",     "python.linting.flake8Enabled": true,     "python.formatting.provider": "yapf",     "python.linting.flake8Args": ["--max-line-length=248"],     "python.linting.pylamaEnabled": false

}

<img alt="" height="277" src="https://img-blog.csdnimg.cn/2bff2cb8c481436788bc91b1752321b2.png" width="788"> 

 到这里就配置好了，接下来，我们来测试一下

新建一个py后缀的文件，比如  test.py

在这个文件里面输入：   print ("hello world")

<img alt="" height="177" src="https://img-blog.csdnimg.cn/af85e5cb50ce47a684961b26eee1caed.png" width="534">

保存并运行，在终端输入  python test.py    运行test.py

<img alt="" height="320" src="https://img-blog.csdnimg.cn/99e2489884ed47bea1fb7160fc30b0a8.png" width="987"> 

 

出现以上结果即配置完成

 
