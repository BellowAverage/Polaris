
--- 
title:  这15个好用的Python库，你都用过吗？ 
tags: []
categories: [] 

---
>  
  作者：Erik van Baaren 
  译者：数据黑客  
  https://medium.com/tech-explained/top-15-python-packages-you-must-try-c6a877ed3cd0 
 

为什么我喜欢Python？对于初学者来说，这是一种简单易学的编程语言，另一个原因：大量开箱即用的第三方库，正是23万个由用户提供的软件包使得Python真正强大和流行。

在本文中，我挑选了15个最有用的软件包，介绍它们的功能和特点。

### 1. Dash

Dash是比较新的软件包，它是用纯Python构建数据可视化app的理想选择，因此特别适合处理数据的任何人。Dash是Flask，Plotly.js和React.js的混合体。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpicm9aYlRvVlhkMWlha21yOXNXZWxhaEVtVzhzZFFQOW85dk1xNkU1VTNOY3l5WWRyY2dTTnlBLzY0MA?x-oss-process=image/format,png">

### 2. Pygame

Pygame是SDL多媒体库的Python装饰器，SDL(Simple DirectMedia Layer)是一个跨平台开发库，旨在提供对以下内容的低级接口：
- 音频- 键盘- 鼠标- 游戏杆- 基于OpenGL和Direct3D的图形硬件
Pygame具有高度的可移植性，几乎可以在所有平台和操作系统上运行。尽管它具有完善的游戏引擎，但您也可以使用此库直接从Python脚本播放MP3文件。

### 3. Pillow

Pillow专门用于处理图像，您可以使用该库创建缩略图，在文件格式之间转换，旋转，应用滤镜，显示图像等等。如果您需要对许多图像执行批量操作，这是理想的选择。

为了快速了解它，看以下代码示例（加载并渲染图片）：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGppYVdnODZPSHJweWJyTWZVdEpoNkFQenVzbzNDUmE3YWVjQTlNdXU4cTdQNUEzUE1NMEU3aGliUS82NDA?x-oss-process=image/format,png">

### 4. Colorama

Colorama允许你在终端使用颜色，非常适合Python脚本，文档简短而有趣，可以在Colorama PyPI页面上找到。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGo0MGNIUHNxM0ZuRHRpYkJmZXJmaWNYZjRmQ1VmVGVrcDkwYlpSaWI1MHk1UnNDUHZFb1VZMFlkaWF3LzY0MA?x-oss-process=image/format,png">

### 5. JmesPath

在Python中使用JSON非常容易，因为JSON在Python字典上的映射非常好。此外，Python带有自己出色的json库，用于解析和创建JSON。对我来说，这是它最好的功能之一。如果我需要使用JSON，可以考虑使用Python。

JMESPath使Python处理JSON更加容易，它允许您明确的地指定如何从JSON文档中提取元素。以下是一些基本示例，可让您对它的功能有所了解：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpwdnVwUFZEbE40ajYwMFNlR0h5NzN5NlR2QmptUDJMUjN2VGxrY1k0VERXV1N3aWFFTjE4b293LzY0MA?x-oss-process=image/format,png">

### 6. Requests

Requests建立在世界上下载量最大的Python库urllib3上，它令Web请求变得非常简单，功能强大且用途广泛。

以下代码示例说明requests的使用是多么简单。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpDTTlndVlSQXU0TXJMRlJwanEyN01hV0JtMnpCTExOemNpY3dnSUp1Yk9rdVNmWGlidGljRDVCMkEvNjQw?x-oss-process=image/format,png">

Requests可以完成您能想到的所有高级工作，例如：
- 认证- 使用cookie- 执行POST，PUT，DELETE等- 使用自定义证书- 使用会话Session- 使用代理
### 7. Simplejson

Python中的本地json模块有什么问题？没有！实际上，Python的json是simplejson。意思是，Python采用了simplejson的一个版本，并将其合并到每个发行版中。但是使用simplejson具有一些优点：
- 它适用于更多Python版本。- 它比Python随附的版本更新频率更高。- 它具有用C编写的（可选）部分，因此非常快速。
由于这些事实，您经常会在使用JSON的脚本中看到以下内容：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpqdGNMN1hDRG93bXRHWU05SFhPelF6dHdqcE8yMGh4UWJycll5Q0hLMkxFU1A1SmtWWXRVbEEvNjQw?x-oss-process=image/format,png">

我将只使用默认的json，除非您特别需要：
- 速度- 标准库中没有的东西
Simplejson比json快很多，因为它用C实现一些关键部分。除非您正在处理数百万个JSON文件，否则您不会对这种速度感兴趣。

### 8. Emoji

Emoji库非常有意思，但并非每个人都喜欢表情包，分析视角媒体数据时，Emoji包非常有用。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGprbURYaWN1aGljYkRJNGxreXl2dm9BRFZlaDg5SGpEdTFDTmFqU2RpYzJucWppYjE2S29MTGliUHlrQS82NDA?x-oss-process=image/format,png">

以下是简单的代码示例：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpUVGx3UWlieWlibHdWaWNiZ28xczROT2F6R2J3ZFA2aGhGcnpCWkxCblZGTGxEckh4YWNIUUM1aWJRLzY0MA?x-oss-process=image/format,png">

### 9. Chardet

您可以使用chardet模块来检测文件或数据流的字符集。例如，这在分析大量随机文本时很有用。但是，当您不知道字符集是什么时，也可以在处理远程下载的数据时使用它。

### 10. Python-dateutil

python-dateutil模块提供了对标准datetime模块的强大扩展。我的经验是，常规的Python日期时间功能在哪里结束，而python-dateutil就出现了。

您可以使用此库做很多很棒的事情。我将这些示例限制为我发现特别有用的示例：模糊分析日志文件中的日期，例如：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpNN1J3TlNndXo4ZDN6aHB1aEVJNFg3VlFhSldRenBUb2xUSll6TjRoenBhTnZWMUdOcDFPWmcvNjQw?x-oss-process=image/format,png">

有关更多功能，请参见完整文档，例如：
- 计算相对增量（下个月，明年，下周一，该月的最后一周等）和两个给定日期对象之间的相对增量。- 使用iCalendar规范的超集，根据重复规则计算日期。- tzfile文件（/ etc / localtime，/ usr / share / zoneinfo等）的时区（tzinfo）实现，TZ环境字符串（所有已知格式），iCalendar格式文件，给定范围（在相对增量的帮助下），本地计算机 时区，固定偏移时区，UTC时区和基于Windows注册表的时区。- 基于奥尔森数据库的内部最新世界时区信息。- 使用Western，Orthodox或Julian算法计算任意一年的复活节周日日期。
### 11. 进度条：progress和tqdm

这里有点作弊，因为这是两个包，但忽略其中之一是不公平的。

您可以创建自己的进度条，这也许很有趣，但是使用progress或tqdm程序包更快，更不容易出错。

progress

借助这个软件包，您可以轻松创建进度条：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpLY216MW53RzJNRFdrbjA2QTVhMUpzZDJqaWNVaWFtakNZZWprcmp3YlhjRlRvZDNpYVY2Z2dUeXcvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpkbGdia2Nhd25VY0dPNEpzOEJNbVByelVXbE44NG5JQnZUbG1xbUtpY1NtYThhMEJwUXBoSnRBLzY0MA?x-oss-process=image/format,png">

tqdm

tqdm的功能大致相同，但似乎是最新的。首先以gif动画形式进行一些演示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpGRVVNSDBMQmR5OWVLRXJSY1Y1MmtpYncyVGR4ZzB0QnVsb2FpY1BjTVo2Zk1VM0VtbGJONlU0Zy82NDA?x-oss-process=image/format,png">

### 12. IPython

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGppY2ZKNHJSQmY2S1ZDSzAwbnFCV2hnRTVxMzM4elVyb0xPWVdmUGhGa1VpYUNSTzlXSlVIbldoQS82NDA?x-oss-process=image/format,png">

我确定您知道Python的交互式外壳，这是运行Python的好方法。但是您也知道IPython shell吗？如果您经常使用交互式外壳程序，但您不了解IPython，则应该检查一下！

增强的IPython shell提供的一些功能包括：
- 全面的对象自省。- 输入历史记录，跨会话持续存在。- 在具有自动生成的引用的会话期间缓存输出结果。- 制表符补全，默认情况下支持python变量和关键字，文件名和函数关键字的补全。- “魔术”命令，用于控制环境并执行许多与IPython或操作系统相关的任务。- 会话记录和重新加载。- 对pdb调试器和Python分析器的集成访问。- IPython的一个鲜为人知的功能：它的体系结构还允许并行和分布式计算。
IPython是Jupyter Notebook的核心，它是一个开放源代码Web应用程序，可让您创建和共享包含实时代码，方程式，可视化效果和叙述文本的文档。

### 13. Homeassistant

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy95MFNCdXhmTGhhbnJYdEg4VUhiS0hBT0NpY25SdHZBMGpxcnkyZWljRTF1MTZUMmRCZDVCU3BXaWFQVkdXUUJhejU3ZlRTR093Y2w3VlpwY2MzU242clRaZy82NDA?x-oss-process=image/format,png">

我喜欢家庭自动化。这对我来说是一种嗜好，但我至今仍对此深表歉意，因为它现在控制着我们房屋的大部分。我使用Home Assistant将房子中的所有系统捆绑在一起。尽管它确实是一个完整的应用程序，但是您也可以将其安装为Python PyPI软件包。
- 我们的大多数灯具都是自动化的，百叶窗也是如此。- 我监视我们的天然气用量，电力用量和产量（太阳能电池板）。- 我可以跟踪大多数电话的位置，并在进入一个区域时开始操作，例如当我回家时打开车库灯。- 它还可以控制我们所有的娱乐系统，例如三星电视和Sonos扬声器。- 它能够自动发现网络上的大多数设备，因此上手起来非常容易。
我已经每天使用Home Assistant已有3年了，它仍处于测试阶段，但这是我尝试过的所有平台中最好的平台。它能够集成和控制各种设备和协议，并且都是免费和开源的。

如果您有兴趣将房屋自动化，请确保有机会！如果您想了解更多，请访问他们的官方网站。如果可以，请将其安装在Raspberry Pi上。到目前为止，这是最简单，最安全的入门方法。我将其安装在Docker容器内功能更强大的服务器上。

### 14. Flask

Flask是我的入门库，用于创建快速的Web服务或简单的网站。这是一个微框架，这意味着Flask旨在使核心保持简单但可扩展。有700多个官方和社区扩展。

如果您知道自己将开发一个大型的Web应用程序，则可能需要研究一个更完整的框架。该类别中最受欢迎的是Django。

### 15. BeautifulSoup

如果您从网站上提取了一些HTML，则需要对其进行解析以获取实际所需的内容。Beautiful Soup是一个Python库，用于从HTML和XML文件中提取数据。它提供了导航，搜索和修改解析树的简单方法。它非常强大，即使损坏了，也能够处理各种HTML。相信我，HTML经常被破坏，所以这是一个非常强大的功能。

它的一些主要功能：
- Beautiful Soup会自动将传入文档转换为Unicode，将传出文档转换为UTF-8。您无需考虑编码。- Beautiful Soup位于流行的Python解析器（如lxml和html5lib）的顶部，使您可以尝试不同的解析策略或提高灵活性。- BeautifulSoup会解析您提供的任何内容，并为您做遍历树的工作。您可以将其告诉“查找所有链接”，或“查找带有粗体的表格标题，然后给我该文字。”
```
&lt; END &gt;


```
