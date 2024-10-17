
--- 
title:  VS2022安装Python开发环境 
tags: []
categories: [] 

---
#### 1 前言

对习惯使用VS2022，VS2019……编辑和调试C\C++\C#的同学来说，能不能在VS2022中开发和调测Python程序呢？答案是肯定的。如果您已经会在VS20XX中编辑调测Python程序，或者习惯使用Pycharm等IDE开发调测Python程序，那么可以忽略本文。

2 安装支持Python

下来我们开始主题。

比如在我的电脑上，已经安装了VS2022社区版，现在想在其上安装支持Python。

在VS2022的启动界面，打开Python组件安装界面，如下图

<img alt="" height="405" src="https://img-blog.csdnimg.cn/084971d75879419a89b4df1fca4606a5.png" width="611">

<img alt="" height="407" src="https://img-blog.csdnimg.cn/cb5428f9f293401b90c2998d7f3535e9.png" width="613">

勾选Python组件，安装。

<img alt="" height="328" src="https://img-blog.csdnimg.cn/0e68eeeffac640abb28111b27d47701c.png" width="612">

<img alt="" height="273" src="https://img-blog.csdnimg.cn/6cd7242591fe402d9cb9b4cfc65d4d87.png" width="610">

安装完成后，就可以在VS2022中，像创建C/C++一样，创建Python工程了

项目类型，选择Python。

<img alt="" height="405" src="https://img-blog.csdnimg.cn/7c668635944b4fd68a6b8e5127ae7f31.png" width="611">

选择您想创建的Python项目：

<img alt="" height="406" src="https://img-blog.csdnimg.cn/575899337c1f440f8e0252871079c6a8.png" width="611">

#### 3 示例

下边我们用Python实现裴波那契数列，来感受一下Python的魅力，代码如下

```
import time

def fun_bis(num):                                   #裴波那契函数
	result = [0, 1]
	for i in range(num-2):
		result.append(result[-2]+result[-1])
	return result

def main():
	result = fun_bis(20)
	fobj = open('result.txt', 'w+')                 #打开文本文件result.txt
	for i, num in enumerate(result):                #循环打印和保存数列数据
		print("index %d is %d" % (i, num))
		fobj.write("index %d is %d \n" % (i, num))
		time.sleep(1)                               #间隔1秒钟

if __name__ == '__main__':
	main()

```

内容比较简单：自动生成前20个裴波那契数列，输出打印在控制台，并将结果保存到当前路径下result.txt文件里。

VS代码视图截图

<img alt="" height="313" src="https://img-blog.csdnimg.cn/2207b24601204f56bcede5f0f8cf6d8d.png" width="677">

运行效果图

<img alt="" height="399" src="https://img-blog.csdnimg.cn/94fd31485604456086b16c927203be29.png" width="672">

<img alt="" height="404" src="https://img-blog.csdnimg.cn/54c89989603444c79f3b475fd07657a3.png" width="671">
