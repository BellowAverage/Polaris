
--- 
title:  [ 环境搭建篇 ] Windows 安装 go 环境并配置环境变量(附go.1.20.2安装包) 
tags: []
categories: [] 

---
>  
 这里安装的是 Go 语言最新版本，也就是 go.1.20.2 版本为例，操作系统为 Windows10 操作系统。 


>  
 <h2>🍬 博主介绍</h2> 
 👨‍🎓 博主介绍：大家好，我是  ，很高兴认识大家~ ✨主攻领域：【渗透领域】【数据通信】 【通讯安全】 【web安全】【面试分析】 🎉点赞➕评论➕收藏 == 养成习惯（一键三连）😋 🎉欢迎关注💗一起学习👍一起讨论⭐️一起进步📝文末有彩蛋 🙏作者水平有限，欢迎各位大佬指点，相互学习进步！ 




#### 文章目录
- - - 


## 1.下载go环境

```
https://golang.google.cn/dl/

```

<img src="https://img-blog.csdnimg.cn/2678eee7ce1843a3b111d182e5db2646.png" alt="在这里插入图片描述">

>  
 解压后得到如下文件夹 


<img src="https://img-blog.csdnimg.cn/9000da4ec5c94a91941569e8af45cd67.png" alt="在这里插入图片描述">

## 2. 配置环境变量

>  
 得到完整的 Go 环境之后，需要配置 Go 的环境变量，右击此电脑-&gt;属性-&gt;高级系统设置-&gt;环境变量，打开环境变量设置窗口。 


<img src="https://img-blog.csdnimg.cn/ab1318a94d844f4da4d4c073f65399ad.png" alt="在这里插入图片描述">

>  
 需要新建两个环境变量配置，一个是 GOROOT ，这个就是 Go 环境所在目录的配置。另一个是 GOPATH ，这个是 Go 项目的工作目录，你以后开发的代码就写在这个文件夹中。 


>  
 为了使所有的计算机用户都可以使用 Go 环境，我们就在系统变量之中配置。点击系统变量下的新建，在变量名一栏输入 GOROOT ，在变量值一栏输入 你解压文件所在的目录D:\路径\go。 最后点击确定，就将 GOROOT 新建完毕。 


<img src="https://img-blog.csdnimg.cn/dae77271d18b41619031e21892f98453.png" alt="在这里插入图片描述">

>  
 GOPATH和GOROOT的配置略有不同，我建议配置两个GOPATH目录，第一个用于放 Go 语言的第三方包，第二个用于放自己的开发代码。我们来新建GOPATH。点击系统变量下的新建，在变量名一栏输入GOPATH，在变量值一栏输入任意两个目录，中间用英文分号隔开。 


```
D:\路径\go\library;D:\路径\go\workspace

```

>  
 最后点击确定，就将GOPATH新建完毕。 


<img src="https://img-blog.csdnimg.cn/52aff31c82594a13aa551b6aa8291f07.png" alt="在这里插入图片描述">

>  
 然后将新建的GOROOT配置到path这个环境变量中去，在系统变量中找到path，点击编辑-&gt;新建，输入%GOROOT%\bin，点击确定。并将所有母窗口的确定全部点下，确保环境变量生效。 


<img src="https://img-blog.csdnimg.cn/a35b5aa8c4054ddfabf0104dbeec4548.png" alt="在这里插入图片描述">

>  
 最后一步，验证环境是否安装成功，windows+R 输入 cmd 打开终端，输入go version，如果输出如下图所示，则安装成功。 


```
go version

```

<img src="https://img-blog.csdnimg.cn/959e1ed65a0141f280718d7aa509a7d3.png" alt="在这里插入图片描述">
