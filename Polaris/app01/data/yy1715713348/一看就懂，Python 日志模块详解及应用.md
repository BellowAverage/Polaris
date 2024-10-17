
--- 
title:  一看就懂，Python 日志模块详解及应用 
tags: []
categories: [] 

---
### 日志概述

**百度百科的日志概述**：

Windows网络操作系统都设计有各种各样的日志文件，如应用程序日志，安全日志、系统日志、Scheduler服务日志、FTP日志、WWW日志、DNS服务器日志等等，这些根据你的系统开启的服务的不同而有所不同。我们在系统上进行一些操作时，这些日志文件通常会记录下我们操作的一些相关内容，这些内容对系统安全工作人员相当有用。比如说有人对系统进行了IPC探测，系统就会在安全日志里迅速地记下探测者探测时所用的IP、时间、用户名等，用FTP探测后，就会在FTP日志中记下IP、时间、探测所用的用户名等。

**我映像中的日志**：

查看日志是开发人员日常获取信息、排查异常、发现问题的最好途径，日志记录中通常会标记有异常产生的原因、发生时间、具体错误行数等信息，这极大的节省了我们的排查时间，无形中提高了编码效率。

### 日志分类

我们可以按照输出终端进行分类，也可以按照日志级别进行分类。输出终端指的是将日志在控制台输出显示和将日志存入文件；日志级别指的是 Debug、Info、WARNING、ERROR以及CRITICAL等严重等级进行划分。

### Python 的 logging

logging提供了一组便利的日志函数，它们分别是：debug()、 info()、 warning()、 error() 和 critical()。logging函数根据它们用来跟踪的事件的级别或严重程度来命名。标准级别及其适用性描述如下（以严重程度递增排序）：

<img src="https://img-blog.csdnimg.cn/img_convert/ab9a9a25b612796f5af597e5363abe72.png" alt="">

每个级别对应的数字值为 CRITICAL：50，ERROR：40，WARNING：30，INFO：20，DEBUG：10，NOTSET：0。 Python 中日志的默认等级是 WARNING，DEBUG 和 INFO 级别的日志将不会得到显示，在 logging 中更改设置。

### 日志输出

#### 输出到控制台

使用 logging 在控制台打印日志，这里我们用 Pycharm 编辑器来观察：

```
import logging


logging.debug('崔庆才丨静觅、韦世东丨奎因')
logging.warning('邀请你关注微信公众号【进击的 Coder】')
logging.info('和大佬一起coding、共同进步') 

```

<img src="https://img-blog.csdnimg.cn/img_convert/5d370282803bf34d4158300c53ad62ab.png" alt="">

从上图运行的结果来看，的确只显示了 WARNING 级别的信息，验证了上面的观点。同时也在控制台输出了日志内容，默认情况下 Python 中使用 logging 模块中的函数打印日志，日志只会在控制台输出，而不会保存到日文件。

**有什么办法可以改变默认的日志级别呢？**

当然是有的，logging 中提供了 basicConfig 让使用者可以适时调节默认日志级别，我们可以将上面的代码改为：

```
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('崔庆才丨静觅、韦世东丨奎因')
logging.warning('邀请你关注微信公众号【进击的 Coder】')
logging.info('和大佬一起coding、共同进步') 

```

<img src="https://img-blog.csdnimg.cn/img_convert/1826faa2d1073599e4d420c2898b8b18.png" alt="">

在 basicConfig 中设定 level 参数的级别即可。

思考：如果设定级别为 ，那 DEBUG 信息能够显示么？

#### 保存到文件

刚才演示了如何在控制台输出日志内容，并且自由设定日志的级别，那现在就来看看如何将日志保存到文件。依旧是强大的 basicConfig，我们再将上面的代码改为：

```
import logging

logging.basicConfig(level=logging.DEBUG, filename='coder.log', filemode='a')
logging.debug('崔庆才丨静觅、韦世东丨奎因')
logging.warning('邀请你关注微信公众号【进击的 Coder】')
logging.info('和大佬一起coding、共同进步') 

```

<img src="https://img-blog.csdnimg.cn/img_convert/21fd615482bb821ed0c5c485dfb2220d.png" alt="">

在配置中填写 filename （指定文件名） 和 filemode （文件写入方式），控制台的日志输出就不见了，那么 coder.log 会生成么？

<img src="https://img-blog.csdnimg.cn/img_convert/98032e3d5bb45739118c828256a22605.png" alt="">

在 .py 文件的同级目录生成了名为 coder.log 的日志。

通过简单的代码设置，我们就完成了日志文件在控制台和文件中的输出。那既在控制台显示又能保存到文件中呢？

### 强大的 logging

logging所提供的模块级别的日志记录函数是对logging日志系统相关类的封装

logging 模块提供了两种记录日志的方式：
- 使用logging提供的模块级别的函数- 使用Logging日志系统的四大组件
这里提到的级别函数就是上面所用的 DEBGE、ERROR 等级别，而四大组件则是指 loggers、handlers、filters 和 formatters 这几个组件，下图简单明了的阐述了它们各自的作用：

<img src="https://img-blog.csdnimg.cn/img_convert/60e134aaddc86e5e9d73f15c1f621f2a.png" alt="">

日志器（logger）是入口，真正工作的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

#### 四大组件

下面介绍下与logging四大组件相关的类：Logger, Handler, Filter, Formatter。

<img src="https://img-blog.csdnimg.cn/img_convert/a0361d3c69fdd6daa910c40328a7be39.png" alt="">

**Logger类**

Logger 对象有3个工作要做：

```
1）向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
2）基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
3）将日志消息传送给所有感兴趣的日志handlers。 

```

Logger对象最常用的方法分为两类：配置方法 和 消息发送方法

最常用的配置方法如下：

<img src="https://img-blog.csdnimg.cn/img_convert/0d09d9477410fcde481ef7f196596e58.png" alt="">

关于Logger.setLevel()方法的说明：

内建等级中，级别最低的是DEBUG，级别最高的是CRITICAL。例如setLevel()，此时函数参数为INFO，那么该logger将只会处理INFO、WARNING、ERROR和CRITICAL级别的日志，而DEBUG级别的消息将会被忽略/丢弃。

logger对象配置完成后，可以使用下面的方法来创建日志记录：

<img src="https://img-blog.csdnimg.cn/img_convert/56fbd3c38dc7d7bbdcd843e9e9fde5f2.png" alt="">

那么，怎样得到一个Logger对象呢？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，但是我们通常都是用第二种方式–logging.getLogger()方法。

logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为’root’。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。

```
关于logger的层级结构与有效等级的说明：

    logger的名称是一个以'.'分割的层级结构，每个'.'后面的logger都是'.'前面的logger的children，例如，有一个名称为 foo 的logger，其它名称分别为 foo.bar, foo.bar.baz 和 foo.bam都是 foo 的后代。
    logger有一个"有效等级（effective level）"的概念。如果一个logger上没有被明确设置一个level，那么该logger就是使用它parent的level;如果它的parent也没有明确设置level则继续向上查找parent的parent的有效level，依次类推，直到找到个一个明确设置了level的祖先为止。需要说明的是，root logger总是会有一个明确的level设置（默认为 WARNING）。当决定是否去处理一个已发生的事件时，logger的有效等级将会被用来决定是否将该事件传递给该logger的handlers进行处理。
    child loggers在完成对日志消息的处理后，默认会将日志消息传递给与它们的祖先loggers相关的handlers。因此，我们不必为一个应用程序中所使用的所有loggers定义和配置handlers，只需要为一个顶层的logger配置handlers，然后按照需要创建child loggers就可足够了。我们也可以通过将一个logger的propagate属性设置为False来关闭这种传递机制。 

```

**Handler**

Handler对象的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）。Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。比如，一个应用程序可能想要实现以下几个日志需求：

```
1）把所有日志都发送到一个日志文件中；
2）把所有严重级别大于等于error的日志发送到stdout（标准输出）；
3）把所有严重级别为critical的日志发送到一个email邮件地址。
这种场景就需要3个不同的handlers，每个handler复杂发送一个特定严重级别的日志到一个特定的位置。 

```

一个handler中只有非常少数的方法是需要应用开发人员去关心的。对于使用内建handler对象的应用开发人员来说，似乎唯一相关的handler方法就是下面这几个配置方法：

<img src="https://img-blog.csdnimg.cn/img_convert/7002f9fd58362800c907a6ab69499fc7.png" alt="">

需要说明的是，应用程序代码不应该直接实例化和使用Handler实例。因为Handler是一个基类，它只定义了素有handlers都应该有的接口，同时提供了一些子类可以直接使用或覆盖的默认行为。下面是一些常用的Handler：

<img src="https://img-blog.csdnimg.cn/img_convert/3cab523c7222b5c3cd5eb6485d49519c.png" alt="">

**Formater**

Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。

Formatter类的构造方法定义如下：

```
logging.Formatter.__init__(fmt=None, datefmt=None, style='%') 

```

该构造方法接收3个可选参数：
- fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值- datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"- style：Python 3.2新增的参数，可取值为 ‘%’, ‘{‘和 ‘$’，如果不指定该参数则默认使用’%’
**Filter**

Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。该类定义如下：

```
class logging.Filter(name='')
    filter(record) 

```

比如，一个filter实例化时传递的name参数值为’A.B’，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志记录通过过滤：‘A.B’，‘A.B,C’，‘A.B.C.D’，‘A.B.D’，而名称为’’, 'B.A.B’的loggers产生的日志则会被过滤掉。如果name的值为空字符串，则允许所有的日志事件通过过滤。

filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值为非0表示可以通过过滤。

```
说明：

    如果有需要，也可以在filter(record)方法内部改变该record，比如添加、删除或修改一些属性。
    我们还可以通过filter做一些统计工作，比如可以计算下被一个特殊的logger或handler所处理的record数量等。 

```

### 实战演练

上面文绉绉的说了(复制/粘贴)那么多，现在应该动手实践了。

**现在我需要既将日志输出到控制台、又能将日志保存到文件，我应该怎么办？**

利用刚才所学的知识，我们可以构思一下：

<img src="https://img-blog.csdnimg.cn/img_convert/e807054b7a97d13c7a53da90fd73df75.png" alt="">

看起来好像也不难，挺简单的样子，但是实际如此吗？

在实际的工作或应用中，我们或许还需要指定文件存放路径、用随机数作为日志文件名、显示具体的信息输出代码行数、日志信息输出日期和日志写入方式等内容。再构思一下：

<img src="https://img-blog.csdnimg.cn/img_convert/96b42179c02f2a260d91d48671a7cd3b.png" alt="">

具体代码如下：

```
import os
import logging
import uuid
from logging import Handler, FileHandler, StreamHandler


class PathFileHandler(FileHandler):
    def __init__(self, path, filename, mode='a', encoding=None, delay=False):

        filename = os.fspath(filename)
        if not os.path.exists(path):
            os.mkdir(path)
        self.baseFilename = os.path.join(path, filename)
        self.mode = mode
        self.encoding = encoding
        self.delay = delay
        if delay:
            Handler.__init__(self)
            self.stream = None
        else:
            StreamHandler.__init__(self, self._open())


class Loggers(object):
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING,
        'error': logging.ERROR, 'critical': logging.CRITICAL
    }

    def __init__(self, filename='{uid}.log'.format(uid=uuid.uuid4()), level='info', log_dir='log',
                 fmt='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        abspath = os.path.dirname(os.path.abspath(__file__))
        self.directory = os.path.join(abspath, log_dir)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        stream_handler = logging.StreamHandler()  # 往屏幕上输出
        stream_handler.setFormatter(format_str)
        file_handler = PathFileHandler(path=self.directory, filename=filename, mode='a')
        file_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


if __name__ == "__main__":
    txt = "关注公众号【进击的 Coder】，回复『日志代码』可以领取文章中完整的代码以及流程图"
    log = Loggers(level='debug')
    log.logger.info(4)
    log.logger.info(5)
    log.logger.info(txt) 

```

文件保存后运行，运行结果如下图所示：

<img src="https://img-blog.csdnimg.cn/img_convert/ffbc11dcf7b564e48ded955b39f32761.png" alt="">

日志确实在控制台输出了，再来看一下目录内是否生成有指定的文件和文件夹：

<img src="https://img-blog.csdnimg.cn/img_convert/0f590be871e0644f71a4dd067db2ec51.png" alt="">

文件打开后可以看到里面输出的内容：

<img src="https://img-blog.csdnimg.cn/img_convert/e4a2c96f7a870b7b696b0732f3751bf9.png" alt="">

**正确的学习方式是什么**

是一步步的看着文章介绍，等待博主结论？

是拿着代码运行，跑一遍？都不是 而是有一份资料

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### **网络安全行业特点**

1、就业薪资非常高，涨薪快 2021年猎聘网发布网络安全行业就业薪资行业最高人均33.77万！

2、人才缺口大，就业机会多

2019年9月18日《中华人民共和国中央人民政府》官方网站发表：我国网络空间安全人才 需求140万人，而全国各大学校每年培养的人员不到1.5W人。猎聘网《2021年上半年网络安全报告》预测2027年网安人才需求300W，现在从事网络安全行业的从业人员只有10W人。

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
