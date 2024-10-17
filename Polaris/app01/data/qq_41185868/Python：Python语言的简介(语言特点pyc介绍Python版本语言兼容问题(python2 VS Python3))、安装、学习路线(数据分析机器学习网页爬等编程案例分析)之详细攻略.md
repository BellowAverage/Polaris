
--- 
title:  Python：Python语言的简介(语言特点/pyc介绍/Python版本语言兼容问题(python2 VS Python3))、安装、学习路线(数据分析/机器学习/网页爬等编程案例分析)之详细攻略 
tags: []
categories: [] 

---
Python：Python语言的简介(语言特点/pyc介绍/Python版本语言兼容问题(python2 VS Python3))、安装、学习路线(数据分析/机器学习/网页爬等编程案例分析)之详细攻略





**目录**











































































































## **Python语言的简介**

        自从20世纪90年代初Python语言诞生至今，它已被逐渐广泛应用于系统管理任务的处理和Web编程。由荷兰人Guido van Rossum(感恩节时无聊而发明的)于1989年发明，第一个公开发行版发行于1991年。Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议。         Python的创始人为Guido van Rossum。1989年圣诞节期间，在阿姆斯特丹，Guido为了打发圣诞节的无趣，决心开发一个新的脚本解释程序，作为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧《蒙提.派森干的飞行马戏团》（Monty Python's Flying Circus）。         Python已经成为最受欢迎的程序设计语言之一。自从2004年以后，python的使用率呈线性增长。2011年1月，它被TIOBE编程语言排行榜评为2010年度语言。          2018年3月，该语言作者在邮件列表上宣布Python 2.7将于2020年1月1日终止支持。用户如果想要在这个日期之后继续得到与Python 2.7有关的支持，则需要付费给商业供应商。

        Python，可以学到面向对象的编程思维，运用模块进行编程，是一种面向对象的解释型计算机程序设计语言。         Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。         由于Python语言的简洁性、易读性以及可扩展性，在国外用Python做科学计算的研究机构日益增多，一些知名大学已经采用Python来教授程序设计课程。例如卡耐基梅隆大学的编程基础、麻省理工学院的计算机科学及编程导论就使用Python语言讲授。众多开源的科学计算软件包都提供了Python的调用接口，例如著名的计算机视觉库OpenCV、三维可视化库VTK、医学图像处理库ITK。         而Python专用的科学计算扩展库就更多了，例如如下3个十分经典的科学计算扩展库：NumPy、SciPy和matplotlib，它们分别为Python提供了快速数组处理、数值运算以及绘图功能。因此Python语言及其众多的扩展库所构成的开发环境十分适合工程技术、科研人员处理实验数据、制作图表，甚至开发科学计算应用程序。         Python语法简洁清晰，Python语言的特点如下所示： &gt;&gt;  **Python 是一种解释型语言**： 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。 &gt;&gt;  **Python 是交互式语言**： 这意味着，您可以在一个Python提示符，直接互动执行写你的程序。 &gt;&gt;  **Python 是面向对象语言**: 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。 &gt;&gt; ** Python 是初学者的语言**：Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

**官方地址**：**官方文档**：



### **1、Python的应用领域**

        目前业内几乎所有大中型互联网企业都在使用Python，如：Youtube、Dropbox、BT、Google、Yahoo!、Facebook、NASA、Quora（中国知乎）、豆瓣、知乎、百度、腾讯、汽车之家、美团等。         互联网公司广泛使用Python来做的事一般有：自动化运维、自动化测试、大数据分析、网络爬虫、Web 等。主流的应用如下所示：**科学计算、数值计算： 图像处理： 机器学习： 数据分析： 网络爬虫： 网络服务、网页开发： 可视化界面GUI开发：**





### **2、Python**语法**特点、对比其它语言**

#### 2.1、Python语法特点

(1)、Python对大小写敏感； (2)、Python默认每行本身作为语法的结束，故每行需要顶格(不能缩进)写代码，不像Java和其他语言，需要分号作为结束。它强制用空白符(white space)作为语句缩进，一般而言，每缩进一次，使用4个空白字符。 (3)、Python是属于“动态类型语言”的编程语言，所谓动态，是指变量的类型是根据情况自动决定的。Python不像C、C++、Java等不需要提前声明变量类型，这点类似Matlab语言。不需变量声明，直接赋值，只有赋值后才可使用；变量名不能为Python内置的关键字。 (4)、python虽然运算的慢，但是开发效率高，一行python可能替代100行C++或、Java代码。



#### 2.2、Python语言**对比其它语言**

<img alt="" height="302" src="https://img-blog.csdnimg.cn/d2087bccd02d4fc59359a3693f7a203b.png" width="302">

        Python 等动态类型语言一般比C 和C++ 等静态类型语言（编译型语言）运算速度慢。实际上，如果是运算量大的处理对象，用C/C++ 写程序更好。为此，当Python 中追求性能时，人们会用C/C++ 来实现处理的内容。Python 则承担“中间人”的角色，负责调用那些用C/C++ 写的程序。比如在NumPy 中，主要的处理也都是通过C 或C++ 实现。
<td style="vertical-align:top;width:83px;"> **<strong>数据分析相关的语言**</strong> </td><td style="vertical-align:top;width:549px;"> 做数据分析、科学计算等离不开工具、语言的使用，目前最流行的数据语言，无非是MATLAB，R语言，Python这三种语言。 python可以调用matlab库。当然matlab也能调用python库。 对于科学运算来说，python语言本身包含的包并不能匹敌matlab，但是当python搭配numpy, scipy, matplotlib等等第三方包的时候，从编程的角度来说与matlab没有什么区别。更重要的是，现在python可以使用的第三方包越来越多了，几乎无所不包。这使得python几乎可以应付任何任务，比如web开发、爬虫、深度学习等等。相对而言，matlab则局限于仅仅完成科学计算任务。 </td>

做数据分析、科学计算等离不开工具、语言的使用，目前最流行的数据语言，无非是MATLAB，R语言，Python这三种语言。 python可以调用matlab库。当然matlab也能调用python库。
<td style="vertical-align:top;width:83px;"> ****<strong><em>Matlab****</em></strong> </td><td style="vertical-align:top;width:549px;"> Python相对于Matlab最大的优势免费。 python易学、易读、易维护，处理速度也比R语言要快，无需把数据库切割； python势头猛，众多大公司需要，市场前景广阔；而MATLAB语言比较局限，专注于工程和科学计算方面，而且MATLAB价格贵，免费版或盗版都只能玩玩学习用； python具有丰富的扩展库，这个是其他两个不能比的；长期来看，Python的科学计算生态会比Matlab好。 </td>

Python相对于Matlab最大的优势免费。

python势头猛，众多大公司需要，市场前景广阔；而MATLAB语言比较局限，专注于工程和科学计算方面，而且MATLAB价格贵，免费版或盗版都只能玩玩学习用；
<td style="vertical-align:top;width:83px;"> ****<strong><em>C/C++/Java****</em></strong> </td><td style="vertical-align:top;width:549px;">  Python这门语言是由C开发而来。  Python/Ruby能让你用少的多的多的代码写出相同的程序。有人计算过，Python或Ruby写出的程序的代码行数只相当于相对应的Java代码的行数的五分之一。如果没有绝对的必要，为什么要花这么多时间写出这么多的代码呢？而且，有人说，一个优秀的程序员能维护的代码量最多是2万行。这不区分用的语言究竟是汇编，C还是Python/Ruby/PHP/Lisp。所以，如果你用Python/Ruby写，你一个人干的，不管是干什么，如果换用Java/C/C++，那都需要一个5人的小团队来干。 </td>

 Python这门语言是由C开发而来。 
<td style="vertical-align:top;width:83px;"> ****<strong><em>VB/PHP****</em></strong> </td><td style="vertical-align:top;width:549px;"> 跟PHP/VB相比，Python/Ruby的是一种从设计上讲比它们好的不知多少倍的语言。PHP和VB分别是在开发网站和桌面应用程序上非常流行的语言。它们流行的原因是非常的易学。不懂计算机的人也很容易的上手。如果你用这些语言开发过大型的项目，你就会发现这些语言的设计是如此的糟糕。是朋友，他就不会劝你使用PHP/VB。 </td>

跟PHP/VB相比，Python/Ruby的是一种从设计上讲比它们好的不知多少倍的语言。PHP和VB分别是在开发网站和桌面应用程序上非常流行的语言。它们流行的原因是非常的易学。不懂计算机的人也很容易的上手。如果你用这些语言开发过大型的项目，你就会发现这些语言的设计是如此的糟糕。是朋友，他就不会劝你使用PHP/VB。
<td style="vertical-align:top;width:83px;"> ****<strong><em>Lisp/Scala/****</em></strong> ****<strong><em>Haskell****</em></strong> ****<strong><em>/Closure/Erlang****</em></strong> </td><td style="vertical-align:top;width:549px;"> Python/Ruby跟它们比起来显得相当的“主流”。确实，这些语言每种都有其很酷的特征，对于高级编程人员，了解这些语言能给他们对编程的思考带来实际的提升。但这些应该在你以后的职业生涯中才去决定学哪一两种。对于现在，Python/Ruby是在语言功能和实际运用之间平衡后的更好的选择。 </td>

****<strong><em>Haskell****</em></strong>

Python/Ruby跟它们比起来显得相当的“主流”。确实，这些语言每种都有其很酷的特征，对于高级编程人员，了解这些语言能给他们对编程的思考带来实际的提升。但这些应该在你以后的职业生涯中才去决定学哪一两种。对于现在，Python/Ruby是在语言功能和实际运用之间平衡后的更好的选择。
<td style="vertical-align:top;width:83px;"> ****<strong><em>Perl****</em></strong> </td><td style="vertical-align:top;width:549px;"> Python和Ruby都受恩于Perl，在这两种语言异军突起前，Perl是最好、最大的一种动态语言。但现在，Perl已是明日黄花，越来越多的人转向Ruby/Python。我感觉Perl的面向对象机制有点做作，很不好用。通常认为，Perl一种比较难学的语言，因为它提供你了太多不同的方法去完成同一个任务，它的语法有点像密码，非常不直观 — 除非你对它掌握的非常好。总之，我感觉Perl是一种对于学生来说不是很合适的语言—除非你有特殊的理由去学它(例如，你有很多正则表达式要处理，这是Perl的闪光点)。 </td>

Python和Ruby都受恩于Perl，在这两种语言异军突起前，Perl是最好、最大的一种动态语言。但现在，Perl已是明日黄花，越来越多的人转向Ruby/Python。我感觉Perl的面向对象机制有点做作，很不好用。通常认为，Perl一种比较难学的语言，因为它提供你了太多不同的方法去完成同一个任务，它的语法有点像密码，非常不直观 — 除非你对它掌握的非常好。总之，我感觉Perl是一种对于学生来说不是很合适的语言—除非你有特殊的理由去学它(例如，你有很多正则表达式要处理，这是Perl的闪光点)。
<td style="vertical-align:top;width:83px;"> ****<strong><em>sh/sed/awk/bash****</em></strong> </td><td style="vertical-align:top;width:549px;"> 如果你使用Linux/Unix，你可能需要做一些shell编程，甚至会编写一些不小的程序。但是，对于这些语言，一旦程序达到一定的行数，事情就会开始变得让你痛苦不堪，你最好是用Python去做这些事情。当然，做这种事情，Perl是最好的选择，Python排第二。(Ruby对于系统shell脚本不是很合适)。 </td>

如果你使用Linux/Unix，你可能需要做一些shell编程，甚至会编写一些不小的程序。但是，对于这些语言，一旦程序达到一定的行数，事情就会开始变得让你痛苦不堪，你最好是用Python去做这些事情。当然，做这种事情，Perl是最好的选择，Python排第二。(Ruby对于系统shell脚本不是很合适)。





### **3、Python版本语言兼容问题(python2 VS Python3)**

#### **(1)、Python 3 与 Python 2 有很大的区别**

1)、python编程需要格外注意python2和python3，因为python3并不兼容ython2。 2)、Python 3默认使用的就是utf-8编码。所以，对于使用的是Python 3 的情况，就不需要sys.setdefaultencoding("utf-8")这段代码， 最重要的是，Python 3 的 sys 库里面已经没有 setdefaultencoding() 函数了。



#### **(2)、****Python 2用法VS Python 3用法**
<td style="vertical-align:top;width:150.7pt;"> **<strong>Python2**</strong> </td><td style="vertical-align:top;width:209.4pt;"> **<strong>Python3**</strong> </td>

**<strong>Python3**</strong>
<td style="vertical-align:top;width:150.7pt;"> print clf  </td><td style="vertical-align:top;width:209.4pt;"> print (clf) 输出要加() </td>

print (clf)
<td style="vertical-align:top;width:150.7pt;"> import cPickle </td><td style="vertical-align:top;width:209.4pt;"> import pickle python2有cPickle，但是在python3下，是没有cPickle的； **<strong>解决办法**</strong>：将cPickle改为pickle即可 </td>

import pickle

**<strong>解决办法**</strong>：将cPickle改为pickle即可
<td style="vertical-align:top;width:150.7pt;"> a=[2,.0] print (clf.predict(a)) </td><td style="vertical-align:top;width:209.4pt;"> a=[2,.0] print (clf.predict([a])) 对与数组等要加[] </td>

print (clf.predict(a))

print (clf.predict([a]))
<td style="vertical-align:top;width:150.7pt;"> clf = GridSearchCV(SVC(kernel=**'****<u><u>rbf</u></u>****'**, class_weight=**'auto'**), param_grid)   </td><td style="vertical-align:top;width:209.4pt;"> clf = GridSearchCV(SVC(kernel=**'****<u><u>rbf</u></u>****'**, class_weight=**'balanced'**), param_grid)   #auto改为balanced #建立分类器模型，GridSearchCV函数(图像处理即选择<u><u>rbf</u></u>作为核函数，权重自自动的，上行定义好的格子似的矩阵) </td>



 #auto改为balanced
<td style="vertical-align:top;width:150.7pt;"> xPredict =  [90,2,0,0,1] print (**"predict:"**) </td><td style="vertical-align:top;width:209.4pt;"> xPredict =  [[90,2,0,0,1]] print (**"predict:"**) </td>

print (**"predict:"**)

print (**"predict:"**)
<td style="vertical-align:top;width:150.7pt;">  </td><td style="vertical-align:top;width:209.4pt;"> import sys import importlib importlib.reload(sys) </td>

import sys

importlib.reload(sys)





### **4、****<strong>pyc等文件简介**</strong>

执行Python代码时，如果导入了其他的 .py 文件，那么，执行过程中会自动生成一个与其同名的 .pyc 文件，该文件就是Python解释器编译之后产生的字节码。







## **Python****语言IDE的安装**

**<strong>Python Interpreter编译器**</strong>：是Python的编译器，核心模块，是将所有Python代码的语言转为系统理解的程序，然后执行。

<img alt="" height="35" src="https://img-blog.csdnimg.cn/3b9e9ad6fd8e494e93c7477b9641f22d.png" width="572">





### **1、****<strong>Windows系统下安装Python的IDE**</strong>

#### **<strong>T1**</strong>**<strong>、安装IDLE(Python官网下载时自带的IDLE)软件编程**</strong>

<img alt="" height="205" src="https://img-blog.csdnimg.cn/20190220161858234.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTg1ODY4,size_16,color_FFFFFF,t_70" width="565">

          安装Python解释器环境时会附带的IDE，安装时切记勾选Add Python 3.6 to PATH，系统会自动帮我们设置电脑环境变量。安装Python时，会自动带有Python自带的IDE即IDLE(IDLE是一个python shell，但是该IDLE的工作界面比较简单)。 (1)、**<strong>Python Shell**</strong>类似Matlab的命令窗口(Shellku框内会输出结果)，新建的编辑器类似Matlab的脚本窗口。 (2)、help(input)   # 利用Python内部帮助文档了解该关键词。
<td style="vertical-align:top;width:71.95pt;"> **<strong>上边菜单栏**</strong> </td><td colspan="2" style="vertical-align:top;width:243px;"> <img alt="" height="43" src="https://img-blog.csdnimg.cn/71216c4bd82444a484032e50445c82c1.png" width="331"> <img alt="" height="46" src="https://img-blog.csdnimg.cn/bf74410aefc1424f87b918413a3e9953.png" width="332"> </td>

<img alt="" height="46" src="https://img-blog.csdnimg.cn/bf74410aefc1424f87b918413a3e9953.png" width="332">
<td style="vertical-align:top;width:71.95pt;"> **<strong>File**</strong> </td><td style="vertical-align:top;width:270px;"> **<strong>New File**</strong>：新建一个File，即编辑(不同于shell内)， **<strong>Save：**</strong> </td><td style="vertical-align:top;width:285px;">  </td>

**<strong>New File**</strong>：新建一个File，即编辑(不同于shell内)，


<td rowspan="3" style="vertical-align:top;width:71.95pt;"> **<strong>Edit**</strong> </td><td style="vertical-align:top;width:270px;"> **<strong>Undo、Redo：**</strong> </td><td rowspan="3" style="vertical-align:top;width:285px;"> <img alt="" height="253" src="https://img-blog.csdnimg.cn/d6ed9aab69f641a68b276e44342debf8.png" width="175"> </td>

**<strong>Undo、Redo：**</strong>
<td style="vertical-align:top;width:270px;"> **<strong>Cut、Copy、Paste：**</strong> </td>
<td style="vertical-align:top;width:270px;"> **<strong>Find、Find Again：**</strong> **<strong>Replace：**</strong> **<strong>设置编码：**</strong>切记要打开不同的文件设置相同的编码，主文件和需要调用的文件都为utf8或GBK的模式， </td>

**<strong>Replace：**</strong>
<td rowspan="3" style="vertical-align:top;width:71.95pt;"> **<strong>Shell**</strong> </td><td style="vertical-align:top;width:270px;">  </td><td rowspan="3" style="vertical-align:top;width:285px;"> <img alt="" height="92" src="https://img-blog.csdnimg.cn/f6ec3a4a5aa34d12908bd754c4307938.png" width="196"> </td>


<td style="vertical-align:top;width:270px;">  </td>
<td style="vertical-align:top;width:270px;">  </td>
<td rowspan="2" style="vertical-align:top;width:71.95pt;"> **<strong>Debug**</strong> </td><td style="vertical-align:top;width:270px;"> Go to File/Line </td><td rowspan="2" style="vertical-align:top;width:285px;"> <img alt="" height="112" src="https://img-blog.csdnimg.cn/98bee36b98fe4853b64296fe53bfa361.png" width="186"> </td>

Go to File/Line
<td style="vertical-align:top;width:270px;"> DebuggerStack Viewer Auto-open Stack Viewer   </td>


<td rowspan="4" style="vertical-align:top;width:71.95pt;"> **<strong>Format**</strong> </td><td style="vertical-align:top;width:270px;"> lndent Region Ctrl+] Dedent Region  Ctrl+[ </td><td rowspan="4" style="vertical-align:top;width:285px;"> <img alt="" height="215" src="https://img-blog.csdnimg.cn/c305ab27bba94cab9b7145ad9fdf262b.png" width="201">  </td>

lndent Region Ctrl+]

<img alt="" height="215" src="https://img-blog.csdnimg.cn/c305ab27bba94cab9b7145ad9fdf262b.png" width="201">
<td style="vertical-align:top;width:270px;"> Comment Out Region  Alt+3 Uncomment Region  Alt+4 Tabify Region    Alt+5 Untabify Region   Alt+6 </td>
<td style="vertical-align:top;width:270px;"> Toggle Tabs     Alt+T New Indent Width    Alt+U </td>
<td style="vertical-align:top;width:270px;"> Format ParagraphAlt+Q Strip Trailing Whitespace </td>
<td style="vertical-align:top;width:71.95pt;"> **<strong>Run**</strong> </td><td style="vertical-align:top;width:270px;"> **<strong>Python Shell：**</strong> **<strong>Check Module模块：**</strong> **<strong>Run Module F5：**</strong>点击即可运行程序 </td><td style="vertical-align:top;width:59px;"> <img alt="" height="73" src="https://img-blog.csdnimg.cn/ba8f9052e18a4f55a492bec4cc872a34.png" width="137"> </td>

**<strong>Python Shell：**</strong>

**<strong>Run Module F5：**</strong>点击即可运行程序
<td style="vertical-align:top;width:71.95pt;"> **<strong>Options**</strong> </td><td style="vertical-align:top;width:270px;"> **<strong>Configure IDLE：**</strong> **<strong>Code Context：**</strong> </td><td style="vertical-align:top;width:59px;"> <img alt="" height="62" src="https://img-blog.csdnimg.cn/c683eda4f3084697a33ff3147ffefcaf.png" width="122"> </td>

**<strong>Configure IDLE：**</strong>

<img alt="" height="62" src="https://img-blog.csdnimg.cn/c683eda4f3084697a33ff3147ffefcaf.png" width="122">



#### **T2、在****<strong>Windows系统**</strong>**的dos内执行python代码**

<img alt="" height="327" src="https://img-blog.csdnimg.cn/6ed5c1a99a364175ac916227b5c09119.png" width="630">

          需要先将下载后的Python Interpreter编译器配置(告诉)给Win系统，即在Win系统环境变量中加入Python Interpreter编译器的路径位置，然后在dos内编写Python代码前，先进入Python环境，即输入python，然后继续输入Python代码。

```
python --version    #查看已经安装的python版本
python                   #进入pythonb编译环境，可以直接输入进行计算
```



<img alt="" height="125" src="https://img-blog.csdnimg.cn/ae2230d2a37a4b8ca34d81ae5d960608.png" width="660">

<img alt="" height="133" src="https://img-blog.csdnimg.cn/20190313164127178.png" width="661">





#### **<strong>T3**</strong>**<strong>、利用MyEclipse软件的PyDev插件实现Python编程**</strong>

          PyDev是Eclips的插件，用户可以完全利用 Eclipse 来进行 Python 应用程序的开发和调试。这个能够将 Eclipse当作 Python IDE 的项目就是 PyDev。           前提必须已安装IDLE(Python)软件，即上一个步骤， 第一步，下载MyEclipse软件。 第二步，下载PyDev插件，利用MyEclipse软件内置下载器，输入下载PyDev插件的网址，如右图，一步步安装即可完成。 第三步，将Python编辑器配置到MyEclipse软件的PyDev插件中，在首选项内找到PyDev添加已经安装好了的Python编辑器即可。 第四步，新建Python软件，New&gt; Others，选择PyDev&gt;PyDev Project，然后新建*.py文件即可，

<img alt="" height="287" src="https://img-blog.csdnimg.cn/d015a39eadcf4e7bb2a796151315038d.png" width="409">

 <img alt="" height="384" src="https://img-blog.csdnimg.cn/60e1c2dfbec04131bb3518f6e56e6b3d.png" width="675">

#### T4、IPython，一款基于web端的IDE

      IPython是一款notebook风格的，并且基于浏览器的解释器环境。一般在安装Anaconda的同时就会附带。对于想快速搭建运行环境并且实践。推荐使用这款集成开发环境。原因在于Anaconda的一键式安装可以帮助使用者一次性配置好所有本书需要的工具包以及IPython解释器环境。同时IPython还提供了非常方便的互联网发布功能，可以随时随地利用互联网维护、更新以及交流Python源代码。

#### Py之ipython：Python库之ipython的简介、安装、使用方法详细攻略





#### T5、Pycharm

      这是一款功能强劲的商业软件，同时也提供免费的社区版本，对于已经熟悉Python编程的专业人士而言，使用这款软件无疑会如虎添翼。其优秀的智能代码提示功能，免去了大家记忆大量Python编程关键词函数以及工具包名称等的麻烦。

#### Python的IDE之PyCharm：PyCharm的简介、安装、入门、使用方法之详细攻略









### **2、****<strong>Linux系统下自带Python的IDE**</strong>

         **<strong>一般Linux系统**</strong>无需安装python，原装Python环境，比如**<strong>ubuntu14.04LTS版本**</strong>自带python。

#### **(1)、从IDLE启动Python**

         IDLE是一个Python Shell类似Windows的cmd窗口，shell的意思是外壳，即通过键入文本与与程序交互的途径



### 3、python下载各种库的方法

#### T1、利用pip的方法



```
pip install pyaudio
```



#### T2、利用conda的方法



```
conda install pyaudio
```







### **4****、python与GPU和CUDA**

         要用GPU图形处理器运算(因为CPU太慢无法达到深度学习的要求)，所编写出的程序于是就可以在支持CUDA™的处理器上以超高性能运行。CUDA是显卡厂商推出的运算平台。CUDA是一种由NVIDIA推出的通用架构，该架构使能够解决复杂的计算问题。









## **Python****语言的系统命令**

### **1、Python编程语言学习：python语言中快速查询python自带模块&amp;函数的用法及其属性方法、如何查询某个函数&amp;关键词的用法、输出一个类或者实例化对象的所有属性和方法名之详细攻略**









### **2、****Python常使用的各种符号**

#**<strong> 单行注释**</strong>：# 单行注释

**"""**** ****<strong>多行注释**</strong>：**""" ****多行内容，****被注释内容****"""**

换行符****<strong>\n****</strong>、字符串是****<strong>%s****</strong>、整数****<strong>%d****</strong>、浮点数****<strong>%f****</strong>



#### **Computer：字符编码(ASCII编码/GBK编码/BASE64编码/UTF-8编码)的简介、案例应用(python中的编码格式及常见编码问题详解)之详细攻略**





## **Python****语言的学习路线**

### **1、Python语言基础学习路线**

**<strong>容器**</strong>：数据的封装**<strong>函数**</strong>：语句的封装**<strong>类**</strong>：方法和属性的封装**<strong>模块**</strong>：模块就是程序**<strong>Python的乐高积木**</strong>：函数、对象、模块

#### **Python语言学习：Python语言学习之python包/库package的简介(模块的封装/模块路径搜索/模块导入方法/案例应用)、使用方法、管理工具之详细攻略**





#### **Python语言学习：Python语言学习之数据类型/变量/字符串/操作符/转义符的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之列表/元祖/字典/集合的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之函数(定义&amp;调用函数/常用内置函数如filter&amp;map/内嵌函数/闭包/匿名函数如lambda&amp;map)的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之逻辑控制语句(if语句&amp;for语句&amp;while语句&amp;range语句&amp;with语句)的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之迭代/递归/OS输入输出/错误&amp;异常处理的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之面向对象编程OO(继承&amp;封装&amp;多态)/类&amp;方法/装饰器的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之文件读取&amp;写入/操作系统(OS模块详解)的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之容器(列表&amp;元组&amp;字典&amp;集合)简介、特点/意义/经验总结及容器魔法方法(定义可变&amp;不可变容器的协议)的简介、案例应用之详细攻**





#### **Python语言学习：Python语言学习之硬件交互应用(arduino、树莓派等)相关的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之程序打包发布(exe/msi等)&amp;如何将自己的Python项目(自定义程序代码库)发布到PyPI全流程的简介、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之编程语言基础案例综合应用集合(输入带*号的密码/与用户交/根据分数判断优良差/提取txt文档中两人对话内容等)之详细攻略**





#### **Python语言学习：Python语言学习之正则表达式相关(re正则表达式库)的简介、常用函数、案例应用之详细攻略**





#### **Python语言学习：Python语言学习之GUI图形用户界面编程(tkinter/wxPython/PyGTK/PySide/Kivy/easygui/PyQt等)的简介、案例应用之详细攻略**









### **2、python与人工智能**

#### AI之DS/CV/NLP：Python与人工智能相关的库/框架(机器学习常用库、数据科学常用库、深度学习常用库、计算机视觉常用库、自然语言处理常用库)的简介、案例应用之详细攻略





持续更新中……





### **3、Python与网页爬虫**

#### **3.1、网络爬虫/反爬虫技术相关介绍**

#### **Python语言学习：Python语言学习之网络爬虫/反爬虫技术相关的简介、案例应用之详细攻略**



#### python之crawler：基于气象局所有城市代码数据爬天气官网数据利用pickle和urllib库实现交互输入城市获取天气预报详情案例代码实现





#### **3.2、与网页相关的包requests**

         提供很多网页抓取和相关函数，先在dos内输入命令行pip install requests进行下载完成即可

<img alt="" height="247" src="https://img-blog.csdnimg.cn/c48593f3cd524e838343f43a39c0d1ec.png" width="554">

         验证先输入python进入环境，再输入import requests即可。

import requestsr = requests.get(**'http://www.jason-niu.com'**)  #抓取网页内容返回给r,print(r.url)                 #抓取网页地址print(r.encoding)       #抓取网页编码print(r.text)                #抓取网页源码






















