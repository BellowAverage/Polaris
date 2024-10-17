
--- 
title:  卧槽！只是pip安装输错字母，就中了挖矿病毒 
tags: []
categories: [] 

---
>  
  晓查 发自 凹非寺  
  量子位 报道 | 公众号 QbitAI 
 

用PyPI包管理工具安装python软件很方便，但你今后要三思而后行了。

当输入这样一句命令后：

```
pip install openvc

```

你也许并未发现异常，仔细一看可能才会察觉自己刚刚手抖，把opencv输错了。

但此时安装命令已经开始运行了，因为openvc其实也是一个真实存在的软件包，不过却是个恶意软件包。

<img src="https://img-blog.csdnimg.cn/img_convert/54a2750aaab6b6fb1ac32cd28b6538ab.png">

最近，安全公司Sonatype发现，很多恶意软件都伪装成常见的PyPI包，往往只差几个字母。

随着加密货币的火爆，黑客们开始把挖矿软件植入其中。如果用户手打pip安装命令手滑一下，自己的电脑就可能变成“矿机”。

### PyPI里的挖矿软件

常用的绘图工具包**matplotlib**首当其冲。PyPI今年有多个与之类似的恶意软件包，如**mplatlib**、**maratlib**（记住这个软件包名称）等等。

这类“李鬼”共有7种之多，都是一个叫做**nedog123**的用户上传到PyPI。其中像maratlib还是今年4月份发布的。

<img src="https://img-blog.csdnimg.cn/img_convert/ee7f9b7d5263bc8906db18853c0d311f.png">

这一组恶意软件以“maratlib”为核心，其他软件都是把它作为依赖项，比如“learninglib”就是这种情况：

<img src="https://img-blog.csdnimg.cn/img_convert/83c03e82f648d264e6c33a4b2f2255bc.png">

这代码还算是比较“直白”的，有些恶意软件将依赖项稍微隐藏了一下，比如“mplatlib”：

<img src="https://img-blog.csdnimg.cn/img_convert/b44d2d5507d239d16f97dd1fd30d9c02.png">

它把依赖项伪装成“LKEK”，从第47行代码可以看出LKEK就是maratlib。

接着Sonatype的安全工程师又对maratlib 1.0安装包进行了分析，发现它已经伪装得很深了，使用一般工具已经很难分析这些代码里到底藏了什么。

<img src="https://img-blog.csdnimg.cn/img_convert/aa7e71e22aa522e519d73e13506a5dc6.png">

他只好把版本倒回0.6，这个版本的maratlib没有对代码做伪装，它会从GitHub下载和运行Bash脚本代码：

<img src="https://img-blog.csdnimg.cn/img_convert/4dc7d48191f7e80175b953700209a680.png">

但服务bash脚本的网址抛出404错误，说明这个地址已经被GitHub删除,或者被黑客nedog123废弃不用。

经过更深的挖掘，这名安全工程师发现，黑客将代码迁移到了“Marat Nedogimov”和“maratoff”用户名下。

<img src="https://img-blog.csdnimg.cn/img_convert/84723a225ea5b51b3c563976ce331cb7.png">

这个aza2.sh脚本会下载一个名为“Ubqminer”的挖矿软件，而上图中那一长串字符就是黑客的数字钱包地址。

至此，案件已经告破。好消息是，PyPI已经删除了这些恶意软件包。

但是，据Sonatype公司统计，这7个李鬼软件已经总共被下载超过**5000次**。

### 恶意PyPI包防不胜防

这次发现的maratlib，可能只是PyPI恶意软件包的冰山一角。PyPI包管理工具的问题一直为用户所诟病。

今年2月，有人将CUDA加速包CuPy换成了恶意软件。还有一位白帽黑客发现，只要向公共库上传PyPI软件包，就能轻易替换掉私有化的同名软件包，大大增加了科技公司中毒风险。

<img src="https://img-blog.csdnimg.cn/img_convert/e87b93085335c31ad82a2a6473e682f0.png">

###### **△** 每月PyPI恶意软件包数量

###### ****

早在2016年，就有人用相似名称的方法发布PyPI恶意软件包，骗过了1.7万名程序员，导致这个恶意程序被运行了4.5万次，甚至连美国军方都中招了。

### 使用pip请谨慎

那么，我们如何预防被安装恶意的PyPI软件包？

你以为只要认真检查安装命令就行了？No！

由于PyPI绝大部分软件包都是第三方编写和维护的，这体现了开源的优势，但也埋下了审核不严的危险种子。

如今，很多软件都需要安装依赖项，个人不可能一一检查，甚至大公司也做不到。有时候一个软件里写了上百个依赖项，根本没法审查代码。

最好的办法就是监控setup.py的行为，在安装不太放心的软件包时，可以在容器中通过pip安装包，同时收集系统调用和网络流量，来分析其是否有恶意行为。

最后再提醒一下大家，不仅pip命令有风险，使用npm、gem等软件包安装命令也可能中毒，一定要对来源不明的软件包仔细核查。

参考链接：[1]https://blog.sonatype.com/sonatype-catches-new-pypi-cryptomining-malware-via-automated-detection[2]https://arstechnica.com/gadgets/2021/06/counterfeit-pypi-packages-with-5000-downloads-installed-cryptominers/[3]https://www.freebuf.com/articles/web/254820.html[4]https://github.com/rsc-dev/pypi_malware

<img src="https://img-blog.csdnimg.cn/img_convert/45396afdc9fc0d7ed175acc51f56c5b3.png">
