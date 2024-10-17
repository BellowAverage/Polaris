
--- 
title:  Python 日志记录器logging 百科全书 之 日志回滚 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/c1a20e54be504216b38bc7b79ab0b560.webp#pic_center#pic_center" alt="在这里插入图片描述">

## Python 日志记录器logging 百科全书 之 日志回滚

## 前言

在之前的文章中，我们学习了关于`Python`日志记录的`基础配置`。

本文将深入探讨`Python`中的日志回滚机制，这是一种高效管理日志文件的方法，特别适用于长时间运行或高流量的应用。

## 知识点📖📖

|模块|释义
|------
||`Python` 的日志记录工具，标准库
|`RotatingFileHandler`|基于文件大小进行日志回滚的处理器。
|`TimedRotatingFileHandler`|基于时间间隔进行日志回滚的处理器。

**导入模块**

```
import logging
from logging.handlers import (RotatingFileHandler, TimedRotatingFileHandler)


```

**文章脉络：**
- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>
## 日志回滚

在`Python`中，日志回滚通常通过`logging.handlers`模块中的`RotatingFileHandler`或`TimedRotatingFileHandler`实现。
- **RotatingFileHandler**: 当日志文件达到指定大小时，自动“回滚”日志文件，即创建一个新的日志文件，并将旧文件保留为备份。- **TimedRotatingFileHandler**: 根据时间间隔回滚日志文件，可以是每秒、每分钟、每小时或每天等。
### 概念

>  
 通过灵活地使用Logger和多个Handler，可以构建一个强大而灵活的日志系统，它可以同时满足日志记录的多样化需求，如日志的级别、格式、输出目的地等，从而为应用程序的监控和故障排查提供强有力的支持。 


**Logger（日志记录器）**
- **Logger**是日志系统的入口。应用程序通过Logger实例来记录日志。- **功能**：Logger负责捕获日志消息并将它们分发给所有附加的Handler。- **日志级别**：Logger可以设置日志级别，以决定要处理哪些级别的日志消息。
**Handler（日志处理器）**
- **Handler**负责将日志消息发送到指定的目的地，这个目的地可以是文件、控制台、网络等。- **类型**：包括但不限于`StreamHandler`（控制台输出）、`FileHandler`（写入文件）、`RotatingFileHandler`（基于文件大小回滚的文件写入）、`TimedRotatingFileHandler`（基于时间间隔回滚的文件写入）等。- **独立配置**：每个Handler可以有自己的日志级别和格式设置（通过Formatter）。这允许不同的Handler以不同的方式处理相同的日志消息。
**多处理器配置**
- **灵活性**：一个Logger可以附加多个Handler，每个Handler可以独立配置，增加了日志系统的灵活性和可定制性。- **举例**：例如配置一个Logger，使其同时将日志消息输出到控制台（使用`StreamHandler`）和文件（使用`FileHandler`或`RotatingFileHandler`）。- **级别和格式的多样性**：不同的Handler可以设置不同的日志级别和格式。例如对于调试目的，在控制台上输出所有级别的日志，而在文件中只记录警告或更高级别的日志。
### 步骤

>  
 值得注意的是，这里的设置日志级别和日志格式，与前文的`basicConfig`是不一样滴~，细看下文！！！ 


设置日志回滚的步骤如下：
1. **创建日志记录器（Logger）**：实例化一个日志记录器，为日志消息提供一个捕获和分发的入口点；1. **创建日志格式（Formatter）**：创建一个`Formatter`对象，指定日志消息的格式；1. **实例化日志处理器（Handler）**：根据需要选择适当的处理器，例如`FileHandler`、`RotatingFileHandler`等；1. **添加处理器（Handler）到记录器（Logger）**：最后，将这些处理器添加到日志记录器（Logger）；1. **记录日志**：使用配置好的日志记录器来记录消息1. **（可选）清理旧日志文件**
#### 1. 创建日志记录器（Logger）
- 实例化一个日志记录器，为日志消息提供一个捕获和分发的入口点。- 命名可随意，如不传入，默认返回 `root logger`
```
logger = logging.getLogger(name="my_application_logger")
logger.setLevel(logging.INFO)

```

#### 2. 创建日志格式（Formatter）
- 创建一个`Formatter`对象，定义日志消息的输出格式。这可以包括时间戳、日志级别、消息等。
```
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

```

#### 3. 实例化日志处理器（Handler）

根据需要选择适当的处理器，

**对于基于文件大小的回滚**：
- 创建一个`RotatingFileHandler`，设置最大文件大小和备份文件数量。
```
rotating_handler = RotatingFileHandler("my_log.log", maxBytes=1024*1024, backupCount=5)
rotating_handler.setFormatter(formatter)

```

**对于基于时间的回滚**：
- 创建一个`TimedRotatingFileHandler`，设置回滚时间（如午夜）、间隔和备份文件数量。
```
timed_handler = TimedRotatingFileHandler("my_log.log", when="midnight", interval=1, backupCount=7)
timed_handler.setFormatter(formatter)

```

#### 4. 添加处理器（Handler）到记录器（Logger）
- 将配置好的处理器添加到日志记录器。这使得日志消息可以按照处理器的配置被处理和输出。- 同时添加多个`日志处理器` 也没任何问题~
```
logger.addHandler(rotating_handler)
logger.addHandler(timed_handler)

```

#### 5. 记录日志
- 使用配置好的日志记录器来记录消息。根据记录器和处理器的配置，日志消息将按照指定的方式被处理和存储。
```
logger.info("This is a test log message.")

```

#### 6. (可选) 清理旧日志文件
- 定期清理旧的日志文件是维护日志系统的一部分。可以编写脚本或使用工具来自动删除过时的日志文件，以释放磁盘空间。
```
import os
import glob
import time

log_dir = '/logs'
# 查找目录中所有扩展名为.log的文件
log_files = glob.glob(os.path.join(log_dir, '*.log'))

for log_file in log_files:
    # 检查文件的最后修改日期
    # 判断文件的最后修改时间是否早于当前时间7天（7 * 24 * 3600秒）
    if os.path.getmtime(log_file) &lt; (time.time() - 7 * 24 * 3600):
        os.remove(log_file)


```

### RotatingFileHandler

`RotatingFileHandler`是用于基于文件大小的日志回滚。当日志文件达到指定大小时，它会自动 `回滚` 日志文件。

**主要参数**：
1. **filename**：日志文件的名称。1. **mode**：文件的打开模式。默认是 `'a'`，表示追加模式。其他常见模式包括 `'w'`（写模式，每次启动时覆盖文件）。1. **maxBytes**：日志文件的最大字节数。当文件大小超过这个值时，会创建一个新文件。如`app.log.1`, `app.log.2` …1. **backupCount**：保留的备份文件数量。比如，如果设置为5，则除了原始日志文件外，还会有5个备份文件。1. **encoding**（可选）：文件的编码方式，同`basicConfig`。1. **delay**（可选）：如果设置为True，则直到第一次调用`emit()`方法时才会创建文件。即直到日志系统实际写入消息时才创建文件，避免创建空日志文件1. **errors**：指定如何处理编码错误，同`basicConfig`。
**示例代码**

```
import logging
from logging.handlers import RotatingFileHandler

# 创建日志记录器，设置日志级别为INFO
logger = logging.getLogger("my_app_logger")
logger.setLevel(logging.INFO)

# 创建 RotatingFileHandler
# 设置文件最大大小为1MB，最多保留3个备份
handler = RotatingFileHandler("./logs/app.log", maxBytes=1024*1024, backupCount=3)
handler.setLevel(logging.INFO)

# 创建日志格式并设置给处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(handler)

# 记录一些示例日志
for i in range(1000):
    logger.info(f"This is log message {<!-- -->i}")
    

```

### TimedRotatingFileHandler

`TimedRotatingFileHandler`用于基于时间的日志回滚。根据指定的时间间隔回滚日志文件。

**主要参数**：
1. **filename**：日志文件的名称。1. **when**：时间间隔的类型。常见值有`'S'`（秒），`'M'`（分钟），`'H'`（小时），`'D'`（天），`'W0'-'W6'`（周一至周日），`'midnight'`（每天午夜）。1. **interval**：回滚之间的时间间隔。与`when`参数一起使用。例如，`when='H'`和`interval=6`表示每6小时回滚一次日志文件。1. **backupCount**：保留的备份文件数量。比如，如果设置为5，则除了原始日志文件外，还会有5个备份文件。1. **encoding**（可选）：文件的编码方式，同`basicConfig`。1. **delay**（可选）：如果设置为True，则直到第一次调用`emit()`方法时才会创建文件。即直到日志系统实际写入消息时才创建文件，避免创建空日志文件1. **utc**：如果设置为`True`，则时间间隔的计算基于UTC时间。默认为`False`，基于本地时间。1. **atTime**（可选）：如果`when`设置为`'midnight'`，这个参数可以用来指定回滚发生的具体时间。1. **errors**：指定如何处理编码错误，同`basicConfig`。
**示例代码**

```
import logging
from logging.handlers import TimedRotatingFileHandler

# 创建日志记录器，设置日志级别为INFO
logger = logging.getLogger("my_app_logger")
logger.setLevel(logging.INFO)

# 创建 TimedRotatingFileHandler
# 设置每天午夜回滚一次日志，保留最多7个备份
handler = TimedRotatingFileHandler("./logs/app.log", when="midnight", interval=1, backupCount=7)
handler.setLevel(logging.INFO)

# 创建日志格式并设置给处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(handler)

# 记录一些示例日志
for i in range(1000):
    logger.info(f"This is log message {<!-- -->i}")
    

```

### 应用场景

|日志处理器|应用场景|优势
|------
|**RotatingFileHandler**|- 日志活动频繁但数据量可预测的环境- 控制日志文件大小，避免单个文件过大|- 防止日志文件过大，便于文件传输和查看- 适合稳定的日志输出环境
|**TimedRotatingFileHandler**|- 需要按时间周期归档日志的情况- 定期审查或归档日志，如审计和系统监控|- 根据时间自动组织日志文件- 便于日志的定期查找和分析

## 总结🐓🐓

本文详细探讨了`Python`中的日志回滚机制，包括`RotatingFileHandler`和`TimedRotatingFileHandler`两种关键的日志处理器。这些处理器不仅增强了日志系统的灵活性，还大大简化了日志管理，特别适用于长时间运行或高流量的应用。

日志回滚是一种高效的日志管理技术，能够自动控制日志文件的大小和生命周期。通过正确使用`RotatingFileHandler`和`TimedRotatingFileHandler`，我们可以为应用程序提供稳定、可靠的日志记录机制，保障应用程序的健康运行。

## 后话

本次分享到此结束，

see you~🐱‍🏍🐱‍🏍
