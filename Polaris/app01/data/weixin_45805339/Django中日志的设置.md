
--- 
title:  Django中日志的设置 
tags: []
categories: [] 

---
## python 的日志级别

DEBUG:⽤于调试目的底层系统信息； INFO:一般系统信息; WARNING:描述已发⽣的小问题的信息； ERROR:描述已发生的主要问题的信息； CRITICAL:描述已发生的严重问题的信息。

## ⽇志⽣成器的配置⽅方法:

创建py⽂件，写入:

```
import logging
# 创建⽇日志记录器器
logger = logging.getLogger('django')
# 输出⽇日志 
logger.debug('测试logging模块debug') 
logger.info('测试logging模块info') 
logger.error('测试logging模块error')

```

## 在settings中配置⽇日志设置

现在⼯程文件⾥创建logs文件 问题: logs⽂件⽬录需求被Git仓库记录和管理。 当把 *.log 都忽略掉后，logs文件⽬录为空。 但是，Git是不允许提交一个空的目录到版本库上的。 解决: 在空文件目录中建立⼀个.gitkeep⽂件，然后即可提交。

```
LOGGING = {<!-- -->
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {<!-- -->  # 日志信息显示的格式
        'verbose': {<!-- -->
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {<!-- -->
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {<!-- -->  # 对日志进行过滤
        'require_debug_true': {<!-- -->  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {<!-- -->  # 日志处理方法
        'console': {<!-- -->  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {<!-- -->  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/meiduo.log'),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {<!-- -->  # 日志器
        'django': {<!-- -->  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

```
