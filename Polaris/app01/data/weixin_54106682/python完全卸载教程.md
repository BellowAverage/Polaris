
--- 
title:  python完全卸载教程 
tags: []
categories: [] 

---
最近出于python3.10版本过于新，出现一些不适配的情况，决定卸载该版本的python。接下来一起来看看卸载教程吧~

### **软件卸载**

有三种方式。

**方式一：**如果对应版本安装包还在的话，运行这个安装包，会出现如下页面。

<img alt="" height="820" src="https://img-blog.csdnimg.cn/6b235801907042fbbfe8fcac0acc0631.png" width="1200">

 直接选择 uninstall 即可进行 python 的卸载了。

**方式二：**在设置-&gt;应用-&gt;应用和功能中，找到 python 相关选项，也可以进行卸载（包括 python 环境和 python 启动器）

<img alt="" height="1200" src="https://img-blog.csdnimg.cn/f7fb52d66e4e4440a2f7c1accf79debe.png" width="1200">

** 方式三：**在控制面板（按 ​`WIN+R`​ 打开运行，输入 ​`control`​ 点击确定进入）中找到程序下的卸载程序，找到对应的 python 选项（与第二种方式一样）。右键选择卸载接口卸载 python 环境。

<img alt="" height="1189" src="https://img-blog.csdnimg.cn/014e274175f1492ca43b492fb73726e8.png" width="1200">

### **删除相关文件夹**

首先前往 python 安装路径下查看有没有 python 文件夹（一般卸载后就没有了）。

然后前往用户文件夹下的 \​`AppData\Local\Programs\Python`​ 文件夹，这个文件夹存放 python 的 pip 安装的第三方库，如果不需要之前安装的第三方库，可以将这个文件夹删除。

最后，在用户文件夹下的 ​`\AppData\Local\pip`​ 文件夹也需要卸载（这个文件夹存放 pip 的缓存）。

### **小结**

将上面的步骤做完之后，python 就算是被彻底卸载了。如果只是为了更换更新的 python 版本的话，建议不要清除 pip 模块存放的文件夹。这样更新后就可以不用去重新安装第三方库了。


