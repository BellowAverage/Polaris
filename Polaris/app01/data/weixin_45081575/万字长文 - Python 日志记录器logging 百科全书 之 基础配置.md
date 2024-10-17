
--- 
title:  万字长文 - Python 日志记录器logging 百科全书 之 基础配置 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/c1a20e54be504216b38bc7b79ab0b560.webp#pic_center" alt="在这里插入图片描述">

## 万字长文 - Python 日志记录器logging 百科全书 之 基础配置

## 前言

在日常的开发中工作中，日志记录扮演着不可或缺的角色。它不仅能让我们了解应用程序的运行状况，还能帮助我们定位并解决各种问题。
-  最基本的，它记录了应用程序的运行情况，我们可以从日志文件中了解到程序的运行的基本信息； -  其次，当应用程序奔溃时，我们可以从日志文件中快速定位到应用程序崩溃前的状态，帮助我们找出问题所在； -  或者，应用程序的某些功能表现不佳，日志可以帮助我们找到性能瓶颈，从而进行调优。 -  … 
总而言之，日志记录可以帮助我们快速定位并解决程序中的错误，实时监控系统运行状态，及时发现并处理问题。

在这篇文章中，我将介绍 `Python` 的 `logging` 模块，它是一个`Python`标准库。

它可以帮助我们完成应用程序生命周期中的所有的日志记录任务。让我们踏上这个旅程吧！

## 念念碎🎊🎊

本意是分享关于一篇`Python`中的`logging`模块的日志记录功能。

文章标题也都命名好了，就叫 <font color="bluesky"> **《万字长文 - Python 日志记录器logging 百科全书》**</font>，

但是在文章的编写的过程中我发现，单单是关于基础配置已经超10000字数了。

全文写完的话，估计得5w+字数吧，文章太长就不方便查阅啦！

所以我就做了拆分，这里是第一篇。关于`logging`的基础配置！

后面还会有：
- 日志回滚- 高级配置- 日志过滤- 日志处理器- 性能优化
等等知识点，感兴趣的读者朋友们可以一起学习哦！

## 知识点📖📖

|模块|释义
|------
||Python 的日志记录工具，标准库

**导入模块**

```
import logging

```

**文章脉络：**
- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>
## 官方示例

官方示例：

我们先来从一个官方的示例入手，逐步来为读者朋友们介绍`logging`。

**记录日志到文件**

```
import logging

# 基础配置
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# 记录不同级别的日志
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

```

在这个例子中，首先导入了`logging`模块；

并使用`logging.basicConfig`函数来进行基本配置。这是配置日志系统的最简单方式。在这个示例中，指定了三个关键参数：
- `filename='example.log'`：这告诉`logging`模块将日志消息写入到`example.log`文件中。- `encoding='utf-8'`：这确保了即使日志消息包含非ASCII字符（如“Øresund”和“Malmö”）也能被正确记录。- `level=logging.DEBUG`：这设置了日志级别为`DEBUG`，意味着所有级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）的日志都会被记录。
下面是关官方文档对于logging的一些方法的注解：
- 对于简单的日志使用来说日志功能提供了一系列便利的函数。它们是 ，，， 和 。（可以理解为是另一种`print`，也是作用于打印）
<th align="left">你想要执行的任务</th><th align="left">此任务最好的工具</th>
|------
<td align="left">对于命令行或程序的应用，结果显示在控制台。</td><td align="left"></td>
<td align="left">在对程序的普通操作发生时提交事件报告(比如：状态监控和错误调查)</td><td align="left"> 函数(当有诊断目的需要详细输出信息时使用  函数)</td>
<td align="left">提出一个警告信息基于一个特殊的运行时事件</td><td align="left"> 位于代码库中，该事件是可以避免的，需要修改客户端应用以消除告警 不需要修改客户端应用，但是该事件还是需要引起关注</td>
<td align="left">对一个特殊的运行时事件报告错误</td><td align="left">引发异常</td>
<td align="left">报告错误而不引发异常(如在长时间运行中的服务端进程的错误处理)</td><td align="left">,  或  分别适用于特定的错误及应用领域</td>

不出意外的话，你会在`example.log`的日志文件中看到以下日志信息：

<img src="https://img-blog.csdnimg.cn/0f0c0baf574943ae8989cb300d7cd13d.png" alt="在这里插入图片描述">

## 基础配置

>  
 在进行日志记录时候，需要考虑的是如何配置日志。这包括定义日志文件的名称、格式，以及确定记录哪些级别的日志信息等。 


在前面  ，初步接触到了`logging`的基础配置和日志级别，在这里做详细介绍。

### basicConfig

>  
 值得注意的是，`basicConfig()` 在程序运行期间只应被调用一次，通常是在程序的开始处定义。但不管调用多少次，只有第一次的调用会生效，后续的调用将被忽略。 


先来看 **basicConfig(基础配置)**，

**basicConfig** 是`logging`模块的一个方法，下面 `logging.basicConfig()` 函数的主要配置参数及其描述。

|参数|描述|示例值/备注
|------
|`filename`|指定一个文件来保存日志。|`'myapp.log'`
|`filemode`|指定日志文件的打开模式。|`'a'`（追加模式）、`'w'`（写模式）
|`format`|定义日志消息的格式。|`'%(asctime)s - %(levelname)s - %(message)s'`
|`datefmt`|定义时间格式（用于 `format` 中的 `%(asctime)s`）。|`'%Y-%m-%d %H:%M:%S'`
|`style`|决定 `format` 字符串的风格。|`'%'`（默认）、`'{'`、`'$'`
|`level`|设置日志的基本级别。|`logging.INFO`, `logging.DEBUG`, 等
|`stream`|指定日志消息的输出流。|`sys.stdout`, `sys.stderr`
|`handlers`|指定一个或多个日志处理器，而不是使用 `filename` 和 `filemode`。|`[logging.FileHandler('filename'), logging.StreamHandler()]`
|`force`|强制覆盖任何已经存在的日志配置（Python 3.8+）。|`True`、`False`
|`encoding`|指定文件的编码方式（仅当 `filename` 被使用时）。|`'utf-8'`, `'ascii'` 等
|`errors`|指定如何处理编码错误（仅当 `filename` 被使用时）。|`'strict'`, `'replace'`, `'ignore'` 等

一个简单的 `basicConfig` 使用示例可能是这样的：
- 在这个示例中，日志级别被设置为 `INFO`，模式为`W` 写模式(即覆盖)。日志格式包括时间戳、日志级别和消息内容。日志会被写入到 `app.log` 文件中。
```
import logging

# 基础配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='example.log',
    filemode='w',
    errors='ignore')

# 记录不同级别的日志
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

```

修改一下上面的  的代码，将`basicConfig`的配置替换。如果没有意外的话，你会在`example.log`的日志文件中看到以下日志信息：

<img src="https://img-blog.csdnimg.cn/3a5d1997844b48c6bfe29a41d4228e20.png" alt="在这里插入图片描述">

如果你足够细心，你会有以下发现：
- 这里的日志内容值有3行，相比上面的  的日志内容少了1行；- 日志内容带有时间，且内容以 `-` 做分隔；- 非ASCII字符不见了。
这里涉及到三个参数，对应上面的三个变化：
1. 日志级别1. 格式设置1. 错误处理
下面分别来介绍一下这 **三个变化** 和 **三个参数** 。

### 日志级别

>  
 基于日志的内容和重要性，我们通常需要设定不同的日志级别。 


Python的`logging`模块提供了强大的日志记录功能，包括五个日志级别：DEBUG、INFO、WARNING、ERROR和CRITICAL。通过设置不同的日志级别，我们可以控制日志输出的详细程度。

日志功能应以所追踪事件级别或严重性而定。各级别适用性如下（以严重性递增）：
- 这份表格是 **官方文档** 拿下来的，我添加了一列`使用场景`；
`logging`默认的级别是 `WARNING`，意味着只会追踪该级别及以上的事件，除非更改日志配置。

<th align="left">级别</th><th align="left">数值</th><th align="left">含义 / 何时使用</th><th align="left">使用场景</th>
|------
<td align="left">logging.**NOTSET**</td><td align="left">0</td><td align="left">当在日志记录器上设置时，表示将查询上级日志记录器以确定生效的级别。 如果仍被解析为 `NOTSET`，则会记录所有事件。 在处理句柄上设置时，所有事件都将被处理。</td><td align="left">一般不直接使用，用于继承父级日志记录器的级别或允许记录所有事件。</td>
<td align="left">logging.**DEBUG**</td><td align="left">10</td><td align="left">详细的信息，通常只有试图诊断问题的开发人员才会感兴趣。</td><td align="left">用于开发阶段，用于详细追踪事件、变量值，帮助诊断问题。</td>
<td align="left">logging.**INFO**</td><td align="left">20</td><td align="left">确认程序按预期运行。</td><td align="left">用于生产环境，记录常规操作，如程序启动、运行状态或处理流程。</td>
<td align="left">logging.**WARNING**</td><td align="left">30</td><td align="left">表明发生了意外情况，或近期有可能发生问题（例如‘磁盘空间不足’）。 软件仍会按预期工作。</td><td align="left">用于警告可能会影响程序性能但不影响程序继续运行的问题。</td>
<td align="left">logging.**ERROR**</td><td align="left">40</td><td align="left">由于严重的问题，程序的某些功能已经不能正常执行</td><td align="left">用于记录程序运行中出现的错误，这些错误会影响某些功能的执行。</td>
<td align="left">logging.**CRITICAL**</td><td align="left">50</td><td align="left">严重的错误，表明程序已不能继续执行</td><td align="left">用于记录严重错误，如程序崩溃、关键服务失效，需要立即关注的问题。</td>

这些日志级别之间的关系是层级的，也就是说，在设置为某个级别时，会记录该级别以及更高级别的日志。例如，如果日志级别设置为 `WARNING`，则会记录 `WARNING`、`ERROR` 和 `CRITICAL` 级别的消息，但不会记录 `DEBUG` 和 `INFO` 级别的消息。

可以理解为，每个级别都包含了比它更高级别的日志信息，而忽略了比它更低级别的信息。所以，选择合适的日志级别可以帮助你筛选出最关心的信息，而忽略不那么重要的细节。

以下是在日常开发或者生产环境中，对应场景建议使用的日志级别。

|环境|推荐日志级别|理由
|------
|生产环境|`INFO` 或 `WARNING`|关注程序正常运行和潜在问题，`INFO` 记录正常操作，`WARNING` 提示可能的问题但不影响运行。
|测试环境|`DEBUG` 或 `INFO`|`DEBUG` 提供详细信息以诊断问题，`INFO` 提供较少但重要的信息。适用于测试和问题排查。
|日常开发|`DEBUG` 或 `INFO`|`DEBUG` 适用于详细追踪和开发阶段，`INFO` 用于较稳定或需关注主要操作的情况。

以上提供了一个基本的指导，帮助读者朋友们根据不同的应用场景选择合适的日志级别。

然而，具体使用哪个级别还需要根据你的具体需求和项目的复杂度来决定。在实际应用中，需要根据实际情况做出调整。甚至可以在不同阶段动态调整日志级别以满足特定需求。

选择适当的级别有助于确保日志既提供了足够的信息以监控应用程序，又可以避免过多的冗余信息。

<font color="redsky"> **解释：日志内容为什么少了一行？**</font>
- <font color="blueyellow"> 因为  代码中日志级别设置为`INFO`，所以只记录`INFO`、`WARNING`、`ERROR` 和 `CRITICAL` 级别的日志信息，</font>- <font color="blueyellow">  较比  的日志级别少了`DEBUG`，于是内容就少了一行。</font>
### 格式设置

>  
 如果想使用不同的风格，则需要相应地修改 `format` 字符串，并设置 `style` 参数。 


**style**

在 Python 的 `logging` 模块中，`style` 参数用于指定 `format` 字符串的风格。这允许选择不同的字符串格式化方法。有三种风格可供选择：
1.  **`'%'` 风格**：这是默认的格式化风格，使用传统的 printf 风格的格式化字符串。例如：`'%(asctime)s - %(levelname)s - %(message)s'` 1.  **`'{'` 风格**：使用 `str.format()` 方法的格式化字符串。例如：`'{asctime} - {levelname} - {message}'` 1.  **`'$'` 风格**：使用 `string.Template` 风格的格式化字符串。例如：`'${asctime} - ${levelname} - ${message}'` 
根据自己选择的 `style`，我们需要相应地调整 `format` 参数中的字符串，否则会抛出 **ValueError** 异常。

选择哪种风格主要取决于个人偏好以及项目中已有的编码风格。`'%'` 风格是最传统的，而 `'{'` 和 `'$'` 提供了更现代和灵活的字符串格式化选项（但他们记录的内容是一致的）。

示例的配置如下所示：
<li> 使用 `'%'` 风格： <pre><code class="prism language-python">logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    style='%')
</code></pre> </li><li> 使用 `'{'` 风格： <pre><code class="prism language-python">logging.basicConfig(level=logging.INFO,
                    format='{asctime} - {levelname} - {message}',
                    style='{')
</code></pre> </li><li> 使用 `'$'` 风格： <pre><code class="prism language-python">logging.basicConfig(level=logging.INFO,
                    format='${asctime} - ${levelname} - ${message}',
                    style='$')
</code></pre> </li>
在 Python `logging` 模块中，`format` 字符串可以包含多种格式化字段，这些字段用于定义日志消息的具体内容。以下是一些常用的格式化字段，以表格形式展示：

|格式化字段|描述
|------
|`%(name)s`|Logger 的名字（即创建 Logger 实例时指定的名称）
|`%(levelno)s`|日志级别的数值表示（如 10, 20, 30, …）
|`%(levelname)s`|日志级别的文本表示（如 ‘DEBUG’, ‘INFO’, ‘WARNING’, 等）
|`%(pathname)s`|调用日志记录函数的源码文件的全路径
|`%(filename)s`|`pathname` 的文件名部分
|`%(module)s`|`filename` 的模块名部分
|`%(funcName)s`|调用日志记录函数的函数名
|`%(lineno)d`|调用日志记录函数的源代码行号
|`%(asctime)s`|创建日志记录的时间。默认格式为 ‘2023-11-07 09:13:45,896’
|`%(thread)d`|线程ID
|`%(threadName)s`|线程名
|`%(process)d`|进程ID
|`%(message)s`|日志消息本身

我们可以根据需要在 `format` 字符串中组合使用这些字段。例如：
- 这个配置会产生包含时间戳、Logger 名称、日志级别和消息本身的日志记录。
```
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

```

**常用配置：**

在 Python `logging` 中，最常用的 `format` 字段取决于项目的日志需求和个人偏好，以下是一些被频繁使用的字段：
1. **`%(asctime)s`**：显示日志事件发生的时间。这是非常有用的信息，因为它帮助我们知道什么时候发生了什么事件；1. **`%(levelname)s`**：显示日志消息的级别（如 `DEBUG, INFO, WARNING, ERROR, CRITICAL`）。这是不可或缺的；1. **`%(message)s`**：显示日志消息本身。这是日志记录的核心部分，包含了事件或数据的实际描述。1. **`%(name)s`**：显示 Logger 的名字。如果在一个大型应用中使用多个 logger，这可以帮助我们确定哪个 logger 产生了消息。1. **`%(filename)s`** 和 **`%(lineno)d`**：这些字段显示产生日志消息的源文件名和行号。在调试时，它们能帮助我们快速定位问题所在的代码位置。
一个典型的 `format` 配置可能是这样的：

```
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')

```

这个配置提供了日志消息的时间、来源、级别、位置（文件和行号）和具体内容，适用于大多数常规日志记录需求。但具体的配置还是需要根据项目需求和你的具体情况，选择添加或省略某些字段。

<font color="redsky"> **解释：日志内容带有时间**</font>
- <font color="pink">因为代码中使用了 `format='%(asctime)s - %(levelname)s - %(message)s'`</font>
### 错误处理

>  
 指定如何处理编码错误（仅当 `filename` 被使用时生效） 


在 Python 的 `logging` 模块中，`errors` 参数是用于配置日志文件写入时的错误处理策略。这个参数仅在使用 `filename` 参数（即将日志写入到文件）时有效，并且通常与 `encoding` 参数一起使用。`errors` 参数定义了在写入日志文件时如何处理那些无法根据指定的编码（如 UTF-8）编码的字符。

以下是几种常见的 `errors` 参数配置选项及其含义：
1.  **`'strict'`**：这是默认的错误处理方式。如果遇到无法按照指定编码的字符，会引发 `UnicodeEncodeError` 异常，导致日志记录中断； 1.  **`'ignore'`**：忽略无法编码的字符。这意味着那些无法编码的字符将被静默地从日志消息中删除，而不会抛出异常； 1.  **`'replace'`**：用一个替代字符（通常是 `'?'`）来替换无法编码的字符。这种方式可以避免编码错误的异常，同时保留了无法编码字符的占位符，从而使你知道在原始消息中存在某些问题； 1.  **`'backslashreplace'`**：用 Python 的反斜杠转义序列来替换无法编码的字符。这种方式在保持日志可读性的同时，提供了关于原始字符的更多信息； 1.  **`'xmlcharrefreplace'`**：用适合于 XML 和 HTML 的字符引用来替换无法编码的字符。 
例如，如果我们希望在写入日志文件时避免因为编码错误而中断日志记录，可以选择使用 `'replace'` 或 `'ignore'`：

```
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='example.log',
                    filemode='w',
                    encoding='utf-8',
                    errors='replace')

```

在这个例子中，任何无法按照 UTF-8 编码的字符都会被 `'?'` 替换，从而保证日志记录的连续性。这种配置对于多语言环境或处理包含特殊字符的数据时尤其有用。

<font color="redsky"> **解释：非ASCII字符不见了**</font>
- <font color="pinkblack">errors设置为**`ignore`**，则会忽略非ASCII字符</font>
## 示例代码🎈🎈

### 一般

这个示例包括了日志的基本设置，如日志级别、格式、文件名等，以及如何在代码中使用不同级别的日志记录。

在具体的使用时候，我们只需要在应用程序中将对应的logging.debug、logging.info…等方法记录日志即可。

```
import logging

# 基础配置
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 设置日志格式
    datefmt='%Y-%m-%d %H:%M:%S',  # 设置时间格式
    filename='app.log',  # 日志输出到app.log文件
    filemode='w',  # 写入模式
    encoding='utf-8',  # 文件编码
    errors='ignore'  # 忽略编码错误
)

# 记录不同级别的日志
logging.debug('Debug message')  # 通常用于详细的系统诊断信息
logging.info('Info message')  # 通常用于记录程序运行状态或操作
logging.warning('Warning message')  # 用于警告信息，可能的问题
logging.error('Error message')  # 用于记录错误事件
logging.critical('Critical message')  # 用于记录严重的错误事件，可能导致程序终止


```

### 高级

>  
 进一步的，应用程序在运行时候，特别是在复杂的应用程序中，可能无法预见所有可能的错误场景。这个时候，最好的做法是让程序能够优雅地终止或继续运行。 


在下面的示例中：
- `setup_logging` 函数配置了基础的日志记录设置。- `handle_exception` 作为全局异常处理器，用于捕获未被局部 `try-except` 块捕获的异常，并使用 `logging` 记录异常信息。- `my_function` 演示了日志记录的常规用法，包括记录操作开始的信息和捕获处理异常的情况。- 通过 `sys.excepthook` 设置了自定义的全局异常处理函数。
`handle_exception` 作为全局异常处理器，负责捕获并处理整个程序中未被其他 `try-except` 块捕获的异常。函数解释如下：
- 对于所有其他类型的异常，函数使用 `logging.error` 来记录异常信息。`exc_info` 参数被设置为一个包含异常类型、值和回溯信息的元组，这样 `logging` 模块可以记录完整的异常堆栈信息。
这样，即使在 `my_function` 中抛出的除以零异常没有被显式捕获，全局异常处理器也会捕获它，并将相关信息记录到日志文件中。

```
import logging
import sys


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='app.log',
        filemode='w',
        encoding='utf-8',
        errors='ignore'
    )


def handle_exception(exc_type, exc_value, exc_traceback):
    """
    全局异常处理函数，用于捕获并处理所有未被捕获的异常。

    Args:
        exc_type: 异常的类型，例如 ZeroDivisionError
        exc_value: 异常实例，包含异常消息等信息。
        exc_traceback: 一个 traceback 对象，包含异常发生时的调用堆栈信息。

    Returns:

    """
    # 使用 logging 记录异常信息
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def my_function():
    # 潜在的异常操作
    result = 10 / 0
    return result


if __name__ == '__main__':
    setup_logging()
    sys.excepthook = handle_exception
    # 运行示例函数
    my_function()


```

**使用场景和注意事项**

`handle_exception` 作为全局异常处理器，用于捕获那些在程序的其他部分未被明确捕获的异常。在使用这个全局异常处理器时，应注意：
- 它不应替代在函数或方法内部对特定异常的具体处理。对于已知可能发生的异常，应在相应的代码区域内使用 `try-except` 块进行处理。- 这个处理器更适合用于捕获意外异常，记录异常信息，并在可能的情况下让程序能够优雅地终止或继续运行。
## 总结🎞🎞

在这篇文章中，我们介绍了 Python 的 `logging` 模块，这是一个非常强大且灵活的日志记录工具，是 Python 标准库的一部分。通过合理配置和使用 `logging` 模块，我们可以有效地记录程序的运行情况，监控系统状态，并在必要时定位和解决问题。

我们讨论了 `logging` 的基础配置，如 `basicConfig` 方法，以及如何设置日志级别、格式和输出目的地等。我们还探讨了不同日志级别的适用场景，以及如何根据开发环境、测试环境或生产环境选择合适的日志级别。

此外，我们解释了格式化日志消息的不同风格，如 `%` 风格、`{}` 风格和 `$` 风格，并展示了如何根据个人喜好和项目需求选择合适的风格。我们还讨论了 `errors` 参数在处理非 ASCII 字符时的重要性，以及如何配置它以避免编码问题。

总之，合理使用 `logging` 模块能够极大地提升程序的可维护性和可靠性。通过定制化的日志记录策略，我们可以确保在需要时总能获取到足够的信息，以便快速响应和解决任何问题。

## 后话

本次分享到此结束，

see you~~🐱‍🏍🐱‍🏍
