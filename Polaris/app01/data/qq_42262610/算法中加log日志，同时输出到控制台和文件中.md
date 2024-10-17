
--- 
title:  算法中加log日志，同时输出到控制台和文件中 
tags: []
categories: [] 

---
 该文件名为common_log.py

```
#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging

import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import colorlog

log_level = {
    "logger_handler": logging.DEBUG,
    "file_handler": logging.DEBUG,
    "console_handle": logging.DEBUG,
    "base": logging.DEBUG,
}
log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

default_formats = {
    'color_format': '%(log_color)s%(asctime)s|%(name)s|%(filename)s|[line:%(lineno)d]|%(levelname)s|[MSG]: %(message)s',
    'log_format': '%(asctime)s|%(name)s-%(filename)s|[line:%(lineno)d]|%(levelname)s|[MSG]: %(message)s'
}


class Log(object):
    def __init__(self, logger=None, log_cate='gujia', level=logging.DEBUG):
        # Step 1: create logger
        # logging.basicConfig(level=log_level["base"])  # 0928: print info iteratively , modified by zja
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(log_level["base"])

        self.log_path = "/home/hisense/gujia_0.1.7/logs"
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        self.log_name = os.path.join(self.log_path, log_cate + '.log')

        # Step 2: File Handler
        # # fh = logging.FileHandler(self.log_name, 'a')  # 追加模式 这个是python2的
        # file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        # file_handler.setLevel(log_level["file_handler"])
        # formatter = logging.Formatter(default_formats["log_format"], datefmt='%a, %d %b %Y %H:%M:%S')
        # file_handler.setFormatter(formatter)
        # logger_handler = RotatingFileHandler(filename=self.log_path, maxBytes=1 * 1024 * 1024, backupCount=3,encoding='utf-8')
        logger_handler = TimedRotatingFileHandler(self.log_name, when='D')
        logger_handler.setLevel(log_level["logger_handler"])
        logger_formatter = logging.Formatter(default_formats["log_format"])
        logger_handler.setFormatter(logger_formatter)

        # Step 3: Console/Stream handler
        console_handle = logging.StreamHandler()
        console_handle.setLevel(log_level["console_handle"])
        console_formatter = colorlog.ColoredFormatter(default_formats["color_format"], log_colors=log_colors_config)
        console_handle.setFormatter(console_formatter)

        # Step 4: 给logger添加handler  避免日志输出重复问题
        if not self.logger.handlers:
            self.logger.addHandler(console_handle)
            self.logger.addHandler(logger_handler)
            # Print multi-times
            # self.logger.removeHandler(console_handle)
            # self.logger.removeHandler(logger_handler)

        console_handle.close()
        logger_handler.close()

    def get_log(self):
        return self.logger


if __name__ == "__main__":
    log = Log(__name__).get_log()

    log.debug("这是debug信息")
    log.info("这是日志信息")
    log.warning("这是警告信息")
    log.error("这是错误日志信息")
    log.critical("这是严重级别信息")

```

下面是运行代码

```
from common_log import Log
import time
log = Log(__name__).get_log()

def add():
    try:
        time1_1 = time.time()
        b = 1
        c = 1
        a = b + c
        time1_2 = time.time()
        log.info("读取图像耗时:{}".format(time1_2 - time1_1))
    except BaseException as e:
        log.error('{}'.format(e))
    finally:
        return a

A = add()
```

1.每个函数必须写try...expect.....finally，把log.error()写在
