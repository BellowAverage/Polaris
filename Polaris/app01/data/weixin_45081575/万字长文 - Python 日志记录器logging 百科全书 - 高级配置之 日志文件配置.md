
--- 
title:  万字长文 - Python 日志记录器logging 百科全书 - 高级配置之 日志文件配置 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/028756c9e83645fb92b1b441a14653f1.png" alt="在这里插入图片描述">

## 万字长文 - Python 日志记录器logging 百科全书 - 高级配置之 日志文件配置

## 前言

在 `Python` 的`logging`模块中，它不仅提供了基础的日志功能，还拥有一系列高级配置选项来满足复杂应用的日志管理需求。

说到`logging` 模块的高级配置，必须提及`日志分层`、`logging.config配置`、`日志异步操作`等关键功能。它们每一项都为开发者提供了强大的调试和监控环境，对于构建可维护和高效的日志系统至关重要。

在接下来的三篇`logging高级配置` 文章中，我将为读者朋友们介绍 `Python` 的 `logging` 模块中的三个高级配置的具体应用：`日志分层`、`logging.config` 以及 `日志异步操作`，探讨它们如何优化日志处理流程，并提升应用的整体性能。

本文将聚焦于 `logging` 模块中的`日志文件配置`概念，探讨如何通过配置文件灵活定义和调整日志记录器的行为。我们将详细解析如何利用配置文件来设置日志级别、格式、输出目的地等，以构建一个既灵活又可扩展的日志系统。

## 知识点📖📖

|模块|释义
|------
||`Python` 的日志记录工具，标准库
|`logging.config`|日志文件配置函数
||

**导入模块**

```
import logging
import logging.config


```

**文章脉络：**
- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>- <font color="bluegreenred">**点击直达：**</font>
## 理解文件配置 logging.config

>  
 `logging.config` 专门用于配置日志系统。它提供了灵活的配置方式，支持多种配置方法，包括基于文件的配置（如 `INI` 、`JSON` 和 `YAML`文件等）。 


### 作用和应用场景

`logging.config` 模块的主要作用是提供一种标准化、灵活的方法来配置 `Python` 应用程序中的日志记录。通过使用这个模块，开发者可以轻松定义日志的级别、格式、输出目标（如文件、控制台、网络服务等）以及其他高级功能，比如日志轮转和过滤。

它适用于各种规模的 `Python` 应用程序，从小型脚本到大型系统。在复杂的系统中，`logging.config` 可以立大功，因为它可以帮助管理和控制多个日志记录器和处理器。

下面是`logging.config`中常用的方法及其作用：

|方法名|作用
|------
|`dictConfig(config_dict)`|使用字典配置日志记录器。
|`fileConfig(fname, defaults=None, disable_existing_loggers=True)`|从配置文件加载日志配置。
|`listen(port=DEFAULT_LOGGING_CONFIG_PORT)`|监听远程日志配置的更改。
|`stopListening()`|停止监听远程日志配置的更改。

下面只介绍关于 `dictConfig` 和 `fileConfig`，因为`listen`不常用。

### ⚠️⚠️注意点

>  
 建议使用`dictConfig`，而不是 `fileConfig`。 


先说结论，
- `fileConfig` 在某些方面（不支持`filters`，需要额外配置）显得不够灵活，适用于简单的日志配置需求。- `dictConfig` 提供了更高的灵活性和更全面的配置选项，更适合复杂的日志配置需求。
`logging.config.dictConfig `较比 `logging.config.fileConfig` 可谓是遥遥领先！！
- `dictConfig` 支持` JSON` 和 `YAML`格式，支持所有日志配置功能，可以更灵活地表示复杂的配置结构，包括过滤器、多个处理器和记录器等。- `fileConfig` 支持 `INI` 格式的文件，这种格式相对简单，在表达能力上不如 `JSON` 或 `YAML` 强。不支持直接在配置文件中定义过滤器，只适合简单的日志配置需求。
### logging.config.dictConfig

>  
 配置字典，支持字典，` JSON` 和 `YAML`格式。 


无论使用哪种格式，它们的主要区别在于数据格式和可读性。选择更加符合自己的开发习惯的即可。

**JSON**:
- 格式更严格（例如，必须使用双引号，不能有注释）。- 在多数编程环境中广泛支持。- 可能更适合那些习惯于编程和处理结构化数据的用户。
**YAML**:
- 可读性更好，容错性更好（例如，可以使用注释，对引号不敏感）。- 适合配置文件，因为它更易于读写，特别是对于较长或复杂的配置。- 需要额外的库来解析（`Python` 中需要安装 `PyYAML`）。
下面将使用 `dict()` 字典进行介绍（因为方便），`JSON` 和`YAML`格式自行学习~

**方法：**

```
logging.config.dictConfig(config)

```

#### 基本示例

>  
 下面是一个使用 `logging.config.dictConfig` 的简单示例，这个示例配置了基本的日志记录功能，只包含一个将日志信息输出到控制台的处理器（handler） 

- 定义了一个名为 `console` 的处理器，它使用 `logging.StreamHandler` 将日志信息输出到控制台（标准输出）。- 设置了一个简单的日志格式，包括时间戳、日志级别和日志消息。- 配置了根日志记录器，将其日志级别设置为 `INFO`，这意味着只有 `INFO` 级别及以上（如 `WARNING`, `ERROR`, `CRITICAL`）的日志会被处理。- 使用 `dictConfig` 函数应用这个配置。
**示例代码**

```
import logging
from logging.config import dictConfig

# 日志配置字典
log_config = {<!-- -->
    'version': 1,
    'handlers': {<!-- -->
        'console': {<!-- -->  # 定义一个名为 "console" 的处理器
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'  # 使用标准输出
        }
    },
    'formatters': {<!-- -->
        'simple': {<!-- -->  # 定义一个简单的格式器
            'format': '%(asctime)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'root': {<!-- -->  # 配置根日志记录器
        'level': 'INFO',
        'handlers': ['console']
    }
}

# 应用日志配置
dictConfig(log_config)

# 获取日志记录器
logger = logging.getLogger()

# 记录一些日志
logger.info("这是一个信息级别的日志")
logger.warning("这是一个警告级别的日志")


```

#### 参数详解

>  
 下面的每一个参数都不是独立的，最终它们结合起来，便是一份完整的`logging.config.dictConfig` 的日志文件配置。 


以下是 `logging.config.dictConfig` 方法中各个参数的整理：

|参数名|类型|必需|描述
|------
|`version`|int|必需|唯一一个必选项，必须设置为 1，表示配置字典的版本。
|`formatters`|dict|可选|定义日志的格式，键是格式器的名称，值是格式器的配置字典。
|`filters`|dict|可选|定义过滤器，用于过滤日志记录。键是过滤器的名称，值是过滤器的配置字典。
|`handlers`|dict|可选|定义处理程序，决定日志如何输出。键是处理程序的名称，值是处理程序的配置字典。
|`loggers`|dict|可选|定义记录器，用于生成日志记录。键是记录器的名称，值是记录器的配置字典。
|`root`|dict|可选|定义根记录器的配置，包含日志级别和处理程序列表。
|`incremental`|bool|可选|默认`False`，用于指定是否应该增量地应用配置。
|`disable_existing_loggers`|bool|可选|默认`True`，用于指定是否禁用所有已存在的记录器。

##### **1. version**

>  
 应设为代表架构版本的整数值。 目前唯一有效的值是 1。 

- 唯一一个必选项，必须设置为 1，表示配置字典的版本。
```
logg_config = {<!-- -->
    'version': 1
}

```

##### **2. formatters**

>  
 对应的值是一个字典，其中每个键是一个格式器 ID 而每个值则是一个描述如何配置相应 `Formatter` 实例的字典 


以下是 `formatters` 字典中全部的参数：
- **format**： 定义日志消息的格式。这是一个字符串，可以包含各种日志记录属性的占位符，如 `%(levelname)s`, `%(message)s`, `%(asctime)s` 等。- **datefmt**： 定义日期和时间的格式。这是一个字符串，用于格式化日志记录中的时间戳，例如 `%Y-%m-%d %H:%M:%S`。- **style**：指定`format`字符串的格式化风格。Python标准库的日志模块支持三种风格：‘%’（默认）、‘{‘和’$’。- **validate**：布尔值，指定是否对 format 字符串进行验证。默认为 `True`。- **class**： 指定自定义的格式器类。这是可选的，仅当需要使用不是标准的`logging.Formatter`的格式器时使用。
**示例代码：**
- 包含两个格式器，`simple` 和 `complex`，分别指定了 `format` 、`style` 等
```
log_config = {<!-- -->
    'version': 1,
    'formatters': {<!-- -->
        'simple': {<!-- -->
            'format': '%(levelname)s - %(asctime)s - %(name)s - %(message)s',
            'style ': '%',  # 默认值
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'complex': {<!-- -->
            'format': '{levelname} - {asctime} - {name} - {message}',
            'style': '{'
        }
    }
}

```

##### **3. filters**

>  
 这里可以结合这篇文章食用： 


对应的值将是一个字典，其中每个键是一个过滤器 ID 而每个值则是一个描述如何配置相应 Filter 实例的字典。

配置日志记录的过滤器，一般过滤器需要绑定到处理器中，所以需要结合下面的`handlees` 使用。
- **name**：字符串，过滤器名称- **()**：字符串，过滤器的类命，用于指定日志系统使用哪个过滤器，如`logging.Filter`，也可以是自定义过滤器类的路径。- **param**：可选，如果过滤类有需要，则可传递。
**无param参数：**
- 自定义过滤器`CommonFilter`，`console_filter`指定的过滤器类路径为 `CommonFilter`（`__main__`需要更改为自定义过滤器的路径
```
import logging


# 自定义过滤器 - 控制台使用
class CommonFilter(logging.Filter):
    def filter(self, record):
        # 过滤掉包含敏感信息的日志
        return "敏感信息" not in record.getMessage()

    
log_config = {<!-- -->
    'version': 1,
    'filters': {<!-- -->
        'console_filter': {<!-- -->
            '()': '__main__.CommonFilter'
        }
    }
}

```

**有param参数：**
- 携带参数
```
import logging


# 自定义过滤器 - 控制台使用
class CommonFilter(logging.Filter):
    def __init__(self, param1=None, param2=None):
        super().__init__()
        self.param1 = param1
        self.param2 = param2

    def filter(self, record):
        # 过滤掉包含敏感信息的日志
        return "敏感信息" not in record.getMessage()


log_config = {<!-- -->
    'version': 1,
    'filters': {<!-- -->
        'console_filter': {<!-- -->
            '()': '__main__.CommonFilter',
            'param1': "value1",
            'param2': "value2"
        }
    }
}


```

##### **4. handlers**

对应的值将是一个字典，其中每个键是一个处理器 ID 而每个值则是一个描述如何配置相应 Handler 实例的字典。

|参数名|类型|必需|描述
|------
|`class`|string|必需|处理器的类名，例如 `logging.StreamHandler` 或 `logging.handlers.FileHandler`
|`level`|string|可选|处理器的日志级别，例如 ‘DEBUG’、‘INFO’、‘WARNING’、‘ERROR’ 或 ‘CRITICAL’。默认为 ‘NOTSET’
|`formatter`|string|可选|处理器使用的格式化器的名称，通常与 formatters 字典中的一个格式化器名称对应
|`filename`|string|可选|只有在处理器类型为 `FileHandler` 时才适用。指定写入日志的文件名
|`mode`|string|可选|只有在处理器类型为 `FileHandler` 时才适用。指定文件的打开模式，默认为 `a`
|`encoding`|string|可选|只有在处理器类型为 `FileHandler` 时才适用。指定文件的编码，默认为 None
|`delay`|bool|可选|只有在处理器类型为 `FileHandler` 时才适用。指定文件创建的时机
|`stream`|string|可选|只有在处理器类型为 `StreamHandler` 时才适用。指定输出流，例如 `ext://sys.stdout`，默认为`sys.stderr`
|`filters`|list|可选|指定一个或多个过滤器的名称列表，用于过滤要发送到处理器的日志消息

**代码**

>  
 一般来说，需要将日志处理器（`Handler`）添加到日志记录器（`Logger`）中才能使用。 

- 包含两个处理器`console` 和 `file`，分别设置了`class`， `formatter`， `level`,等，注意 `FileHandler` 和 `StreamHandler` 所接受的参数有所不同！
```
log_config = {<!-- -->
    'version': 1,
    'handlers': {<!-- -->
        'console': {<!-- -->
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG',
            'filters': ['common_filter'],
            'stream': 'ext://sys.stdin',
        },
        'file': {<!-- -->
            'class': 'logging.FileHandler',
            'formatter': 'complex',
            'level': 'DEBUG',
            'filters': ['common_filter'],
            'filename': 'app.log',
            'mode': 'a',
            'encoding': 'utf-8',
        }
    }
}

```

##### 5. loggers

其中每个键是一个日志记录器名称，而每个值则是一个描述如何配置相应 `Logger `实例的字典。每个日志记录器可以接受以下参数：
- `level` (可选)。字符串，日志记录器的级别。- `propagate` (可选)。 布尔值，日志记录器的传播设置。- `filters` (可选)。 由日志记录器对应过滤器的 ID 组成的列表。- `handlers` (可选)。 由日志记录器对应处理器的 ID 组成的列表。
**代码**
- 配置这里就不解释了，在前的文章都有介绍~
```
log_config = {<!-- -->
    'version': 1,
    'loggers': {<!-- -->
        'common_logger': {<!-- -->
            'level': 'DEBUG',
            'filters': ['common_filter'],
            'handlers': ['console'],
        },
        'common_logger.file': {<!-- -->
            'level': 'WARNING',
            'propagate': False,
            'filters': ['common_filter'],
            'handlers': ['console', 'file'],
        }
    }
}


```

##### 6. root

根日志记录器对应的配置。 配置的处理方式将与所有日志记录器一致，除了 `propagate` 设置将不可用之外。

一般情况下，不需要显式设置根日志记录器（`root logger`），我们只需要设置自定义的子记录器`Logger`即可。

如果我们的应用可能会使用默认的日志记录器（即直接通过 `logging.getLogger()` 获取的记录器），那么配置根日志记录器是有意义的，因为它定义了这些记录器的默认行为。根记录器的目的是提供一个全局的、基本的日志配置，为了保持简单和明确，通常不会涉及过于复杂的参数设置。

置根日志记录器的 `root` 部分包含以下参数：
1.  `level` (可选)：设置根日志记录器的日志级别。 1.  `handlers`（可选）：指定一个处理器列表，这些处理器会被附加到根日志记录器。这些处理器控制日志信息的输出方式和位置。 1.  `propagate` (可选)：不常用于 `root`， 对于非根日志记录器，这个布尔值指定日志信息是否向上传播到父记录器。但对于根记录器本身，这个设置通常不适用或忽略，因为根记录器是层级的顶端。 
**示例代码**
- 指定跟日志记录器的`level`，`handlers`，`filters`等
```
log_config = {<!-- -->
    'version': 1,
    'root': {<!-- -->
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
        'filters': ['common_filter']
    }
}

```

##### 7. incremental

>  
 配置是否要被解读为在现有配置上新增。 该值默认为 `False`. 

-  当 `incremental=True` 时，这意味着正在进行增量更新。只有在配置字典中显式修改的部分会被更新，而其他的配置将保持不变； -  当不使用 `incremental=True`，并且提供了一个新的配置字典给 `dictConfig`，那么整个日志配置将被这个新的配置字典替换（被覆盖）。 
使用 `incremental=True` 的主要作用是允许对日志配置进行部分更新，！！！值得注意的是
- 系统将完全忽略任何 `formatters` 和 `filters` 条目，并仅会处理 `handlers` 条目中的 `level` 设置，以及 `loggers` 和 `root` 条目中的 `level` 和 `propagate` 设置。
###### 应用场景

假设小菜维护一个在生产环境中运行的Web服务，该服务正常情况下仅记录 `INFO` 级别以上的日志。但是，当遇到某些特定问题时，小菜可能需要临时增加日志的详细程度，以便能更好地分析和调试问题。例如，小菜可能想要将某个模块的日志级别从 `INFO` 提升到 `DEBUG` 来获得更多信息。

###### 示例代码

>  
 在不重写整个日志配置的情况下动态调整日志配置，仅更新了日志级别。这对于生产环境中的问题诊断和调试会有用。 

1. **初始日志配置**：最初，小菜的日志配置设置为仅记录 `INFO` 级别及以上的日志。1. **检测到特定问题**：当系统检测到特定问题（可能是通过错误计数、特定类型的请求或其他指标）时，小菜想动态调整相关模块的日志级别以捕获更详细的信息。1. **应用增量更新**：此时，小菜可以使用 `incremental=True` 来更新特定日志记录器的配置，而不影响其他配置。
```
import logging
from logging.config import dictConfig
import time

# 初始配置，记录 INFO 级别及以上的日志
initial_config = {<!-- -->
    'version': 1,
    'handlers': {<!-- -->
        'console': {<!-- -->
            'class': 'logging.StreamHandler',
            'level': 'DEBUG'
        }
    },
    'root': {<!-- -->
        'level': 'INFO',
        'handlers': ['console'],
    }
}
dictConfig(initial_config)

logger = logging.getLogger()

# 模拟应用程序运行
for i in range(5):
    if i == 3:
        # 当出现特定条件时，提升日志级别到 DEBUG
        incremental_config = {<!-- -->
            'version': 1,
            'incremental': True,
            'root': {<!-- -->
                'level': 'DEBUG'
            }
        }
        dictConfig(incremental_config)
        logger.debug("日志级别已提升至 DEBUG")

    logger.debug(f"详细的调试信息 {<!-- -->i}")
    logger.info(f"一般的信息 {<!-- -->i}")
    time.sleep(1)


```

##### 8. disable_existing_loggers

>  
 是否要禁用任何现有的非根日志记录器。形参默认为 `True`。这个选项的作用主要是控制新的日志配置是否会影响到现有的日志记录器。 

- 当 `disable_existing_loggers` 设置为 `True` 时，它的作用是关闭（禁用）之前创建的所有日志记录器，除非它们在新的日志配置中明确定义。- 当 `disable_existing_loggers` 设置为 `False` 时，它的作用是忽略之前创建的日志记录器，不会关闭它们，除非在新的日志配置中明确定义。
如果希望保留现有记录器的配置，并且不希望新的配置覆盖它们，通常会将 `disable_existing_loggers` 设置为 `False`。

如果想要在新的配置中重新定义所有记录器的配置，则不必理会，因为 `disable_existing_loggers` 默认为 `True`。

```
log_config = {<!-- -->
    'version': 1,
    'disable_existing_loggers': False
}

```

#### 🧐使用JSON

**log_config.json**

```
{<!-- -->
    "version": 1,
    "formatters": {<!-- -->
        "simple": {<!-- -->
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        }
    },
    "handlers": {<!-- -->
        "console": {<!-- -->
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG"
        }
    },
    "root": {<!-- -->
        "level": "INFO",
        "handlers": ["console"]
    }
}

```

**代码**

```
import logging
import logging.config
import json

# 从 JSON 文件加载配置
with open('log_config.json', 'r') as file:
    config = json.load(file)
    logging.config.dictConfig(config)

# 获取日志记录器
logger = logging.getLogger()

```

#### 🎈使用YAML

>  
 整体来看，确实需要比 `YAML` 确实会比 `JSON` 更加简单和容易阅读。 


配置与上面的 **使用 JSON** 同款。

**log_config.yaml**

```
version: 1	# 如需要则添加注释
formatters:
  simple:
    format: "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    level: DEBUG
root:
  level: INFO
  handlers: [console]

```

首先需要安装 `PyYAML`

```
pip install pyyaml

```

**代码**

```
import logging
import logging.config
import yaml

# 从 YAML 文件加载配置
with open('log_config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    logging.config.dictConfig(config)

# 获取日志记录器
logger = logging.getLogger()

```

### logging.config.fileConfig

>  
 配置文件，支持`INI` 文件 


⚠️⚠️⚠️**不支持过滤器**

⚠️⚠️⚠️**不支持过滤器**

⚠️⚠️⚠️**不支持过滤器**

**方法：**

```
logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)

```

这里只做基本介绍，不深入。因为它不够友好。

#### 参数详解

以下是 `logging.config.fileConfig` 函数的参数整理：

|参数名称|类型|必需|描述
|------
|`fname`|str|必须|配置文件的路径。这个文件包含了日志配置的信息。
|`defaults`|dict|可选|配置文件中使用的变量的默认值。
|`disable_existing_loggers`|bool|可选|决定是否禁用在调用 `fileConfig` 之前已经存在的日志记录器。默认为 `True`。
|`encoding`|str|可选|用于指定配置文件的编码方式。

#### 必需的字段

在 `logging.config.fileConfig` 中使用的 `INI` 文件中，有几个必需的字段来确保至少基本的日志配置能够工作。以下是一个最简单的示例，其中包含了必需的基础字段。
- `[loggers]`：至少需要列出需要配置的日志记录器。- `[handlers]`：至少需要定义一个处理器。- `[formatters]`：至少需要定义一个格式器。- `[logger_&lt;logger_name&gt;]`：为每个需要配置的记录器定义具体配置。- `[handler_&lt;handler_name&gt;]`：为每个处理器定义具体配置。- `[formatter_&lt;formatter_name&gt;]`：为每个格式器定义具体配置。
#### 基础示例 INI 文件

**log_config.ini**
- 这个配置定义了一个根日志记录器 `root`，它的日志级别为 `INFO`。- 有一个处理器 `consoleHandler`，它将日志输出到标准输出（控制台），同时也设置为 `INFO` 级别。- 有一个格式器 `simpleFormatter`，它定义了日志的显示格式。
```
[loggers]
keys=root

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=INFO
handlers=consoleHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S

```

#### 示例代码

代码通过 `fileConfig` 加载 INI 文件中的配置，然后使用 `getLogger` 创建一个日志记录器。此记录器将根据 `INI` 文件中定义的配置处理日志消息。

```
import logging
import logging.config

logging.config.fileConfig('log_config.ini')

# 创建日志记录器
logger = logging.getLogger()

# 记录消息
logger.info("这是一个信息级别的日志")
logger.debug("这条调试消息不会显示，因为日志级别设置为 INFO")


```

#### 特别处理：添加filters

```
import logging
import logging.config


# 自定义过滤器
class CommonFilter(logging.Filter):
    def filter(self, record):
        # 过滤掉包含敏感信息的日志
        return "敏感信息" not in record.getMessage()
    

logging.config.fileConfig('log_config.ini')

# 创建日志记录器
logger = logging.getLogger()
# 添加过滤器
logger.addFilter(CommonFilter())

# 记录消息
logger.info("这是一个信息级别的日志")
logger.debug("这条调试消息不会显示，因为日志级别设置为 INFO")

```

## 实际案例

以下的代码来自
- 
里的 **示例代码**，将他修改成本文所介绍的 **logging.config 高级配置**。

```
import logging
import logging.config
import requests
import sys


class RemoteLogHandler(logging.Handler):
    """自定义远程处理器"""

    def __init__(self, remote_url):
        super().__init__()
        self.remote_url = remote_url
        self.error_logger = logging.getLogger('error')
        # self.setFormatter(formatter)

    def emit(self, record):
        # 发送日志记录到远程服务器
        log_entry = self.format(record)  # 格式化日志记录
        try:
            response = requests.post(self.remote_url, data=log_entry)
            response.raise_for_status()
        except Exception as e:
            record.msg = f"Original message: {<!-- -->record.msg}, Failed to send log to remote: {<!-- -->str(e)}"
            print('error_logger 等级是 ', self.error_logger.level)
            self.error_logger.handle(record)


log_config = {<!-- -->
    'version': 1,
    'formatters': {<!-- -->
        'simple': {<!-- -->
            'format': '%(levelname)-7s - %(asctime)s - %(name)s - %(message)s'
        }
    },
    'handlers': {<!-- -->
        'file_global': {<!-- -->
            '()': 'logging.FileHandler',
            'filename': 'ecommerce_global.log',
            'level': 'DEBUG',
            'formatter': 'simple',
            'delay': True
        },
        'file_error': {<!-- -->
            '()': 'logging.FileHandler',
            'filename': 'error.log',
            'level': 'ERROR',
            'formatter': 'simple',
            'delay': True
        },
        'file_order': {<!-- -->
            '()': 'logging.FileHandler',
            'filename': 'orders.log',
            'level': 'WARNING',
            'formatter': 'simple',
            'delay': True
        },
        'file_payment': {<!-- -->
            '()': 'logging.FileHandler',
            'filename': 'payments.log',
            'level': 'ERROR',
            'formatter': 'simple',
            'delay': True
        },
        'stream': {<!-- -->
            '()': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'simple'
        },
        'remote': {<!-- -->
            '()': '__main__.RemoteLogHandler',
            'remote_url': 'http://127.0.0.1:5000/submit_log',
        }
    },
    'loggers': {<!-- -->
        'ecommerce': {<!-- -->
            'handlers': ['file_global', 'stream'],
            'level': 'DEBUG'
        },
        'ecommerce.orders': {<!-- -->
            'handlers': ['file_order', 'remote'],
            'level': 'INFO',
            'propagate': False
        },
        'ecommerce.payments': {<!-- -->
            'handlers': ['file_payment', 'remote'],
            'level': 'WARNING',
            'propagate': False
        },
        'error': {<!-- -->
            'handlers': ['file_error'],
            'level': 'WARNING',
        }
    }
}

if __name__ == '__main__':
    logging.config.dictConfig(log_config)

    # 使用日志记录器
    global_logger = logging.getLogger('ecommerce')
    order_logger = logging.getLogger('ecommerce.orders')
    payment_logger = logging.getLogger('ecommerce.payments')
    # 日志测试
    global_logger.info('Global logger configured')
    order_logger.warning('Order logger configured')
    payment_logger.error('Payment logger configured')


```

## 总结🎈🎈

本文全面介绍了`Python` 中`logging`模块的高级文件配置技巧，重点讨论了`dictConfig`和`fileConfig`两种配置方法。

通过`dictConfig`，开发者可以灵活地使用字典、`JSON` 或 `YAML` 格式来设置日志级别、格式和处理器，

而`fileConfig`则提供了对INI格式配置文件的支持。尽管`fileConfig`在功能上有所限制，但它仍适用于简单的配置需求。

文章通过实例和注意事项，指导读者如何选择和应用这些配置方法，以优化日志处理流程并提升应用性能。

总的来说，这篇文章可以帮助读者朋友们深入了解如何使用 `logging.config` 进行日志文件配置。进而帮助读者建立一个高效、可维护的日志系统。

## 后话

本次分享到此结束，

see you~~✨✨
