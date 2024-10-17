
--- 
title:  Ubuntu下Vim的常用操作命令——vi编辑器常用命令 
tags: []
categories: [] 

---
使用Linux（Ubuntu）下自带的Vim编辑器对bashrc等配置文本进行修改时，在terminal中敲入：

```
sudo vi ~/.bashrc
=====（或者）========
vi ~/.bashrc
```

 【以下为几个常用命令】

i：光标后键入insert

I：光标前键入

a：新建一行开始键入

x：删除光标后的字符

ESC：退出编辑状态，进入Vim命令行状态；

q：ESC之后，先敲出冒号“：”，再跟上“q”，表示退出；后面再多接一个叹号“!”表示强制退出；

wq：ESC之后，先敲出冒号“：”，再跟上“wq”，表示保存并退出；后面再多接一个叹号“!”表示强制保存后退出；
