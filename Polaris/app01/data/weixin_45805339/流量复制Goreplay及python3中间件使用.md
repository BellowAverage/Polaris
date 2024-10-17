
--- 
title:  流量复制Goreplay及python3中间件使用 
tags: []
categories: [] 

---
### 1 简介

#### 1.1 说明

GoReplay 是一个开源网络监控工具，可以记录您的实时流量并将其用于阴影、负载测试、监控和详细分析。线上环境需要迁移流量，我们应该确定流量切换过去后没有问题，即确保新的环境是OK的。那么我们借助goreplay工具就会很方便，不会担心影响线上的用户也能模拟线上流量测试。 随着应用程序的增长，测试它所需的工作量也呈指数增长。GoReplay 为您提供了重用现有流量进行测试的简单想法，这使得它非常强大。我们最先进的技术允许您分析和记录您的应用程序流量而不影响它。这消除了将第三方组件置于关键路径中所带来的风险。 GoReplay 增强了您对代码部署、配置和基础架构更改的信心。 GoReplay 提供了一种独特的阴影方法。GoReplay 不是代理，而是在后台侦听网络接口上的流量，无需更改生产基础架构，只需在与服务相同的机器上运行 GoReplay 守护程序。 <img src="https://img-blog.csdnimg.cn/2377420519cf4b92be46d5b57e15ce3e.png" alt="在这里插入图片描述">

#### 1.2 goreplay安装

从下载最新的二进制文件或自行编译。

#### 1.3 源码地址及说明文档



### 2 使用说明

```
sudo ./gor --input-raw :16888  --input-raw-track-response  --output-http "http://10.13.118.203:17555"  --output-http-track-response --middleware "python3 middleware.py" --http-allow-url "/v2/robot/query" --http-allow-url "/v2/robot/input_hint" --http-allow-url "/v1/robot/intention"
"""
注：
--input-raw :16888 origin 服务器端口

--input-raw-track-response 将origin 服务器响应结果输出显示

--output-http "http://192.168.1.1:17555"  replay 服务器URL地址

--output-http-track-response 将replay 服务器响应结果输出显示

--middleware "python3 middleware.py" 启动中间件脚本

--http-allow-url "/v2/robot/query"  允许引流的URL（目前只允许："/v2/robot/query" ，"/v2/robot/input_hint"，"/v1/robot/intention"三个URL）
"""

```

### 3 中间件脚本

本文采用python脚本，python3简单易懂，上手快，开发效率高。大大节约的开发成本。

#### 3.1 安装依赖

我们使用最新的gor库

```
pip install gor -i https://pypi.tuna.tsinghua.edu.cn/simple #清华镜像源

```

#### 3.2 中间件编写

简单粗暴直接上代码：

```
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
from gor.middleware import AsyncioGor
from logging import handlers

# Used to find end of the Headers section
EMPTY_LINE = b'\r\n\r\n'


class Logger(object):
    level_relations = {<!-- -->
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='debug', backCount=10, w='D', i=1,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.NullHandler()  # 不往屏幕上输出日志
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        self.logger.addHandler(sh)  # 把对象加到logger里

        fh = handlers.TimedRotatingFileHandler(filename=filename, when=w, interval=i,
                                               backupCount=backCount)  # 按照文件大小分割日志文件
        fh.setLevel(self.level_relations.get(level))
        fh.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(fh)


log = Logger("middleware.log", level='info')


def print_ok(msg):
    """
    Logging to STDERR as STDOUT and STDIN used for data transfer
    @type msg: str or byte string
    @param msg: Message to log to STDERR
    """
    try:
        msg = "\033[0;32m" + str(msg) + " \033[1;31;0m" + "\n"
    except:
        pass
    sys.stderr.write(msg)
    sys.stderr.flush()


def print_info(msg):
    """
    Logging to STDERR as STDOUT and STDIN used for data transfer
    @type msg: str or byte string
    @param msg: Message to log to STDERR
    """
    try:
        msg = str(msg) + "\n"
    except:
        pass
    sys.stderr.write(msg)
    sys.stderr.flush()


def print_warn(msg):
    """
    Logging to STDERR as STDOUT and STDIN used for data transfer
    @type msg: str or byte string
    @param msg: Message to log to STDERR
    """
    try:
        msg = "\033[0;33m" + str(msg) + " \033[1;31;0m" + "\n"
    except:
        pass
    sys.stderr.write(msg)
    sys.stderr.flush()


def print_error(msg):
    """
    Logging to STDERR as STDOUT and STDIN used for data transfer
    @type msg: str or byte string
    @param msg: Message to log to STDERR
    """
    try:
        msg = "\033[0;31m" + str(msg) + " \033[1;31;0m" + "\n"
    except:
        pass
    sys.stderr.write(msg)
    sys.stderr.flush()


def on_request(proxy, msg, **kwargs):
    """
    param proxy: AsyncioGor实例化对象
    param msg: 请求信息
    param kwargs: 包含:id ,请求信息，URL等信息的字典
    return None
    """
    try:
        robot_list = ["664"]
        url = msg.http.split("POST ")[-1].split(" HTTP/1.1")[0]
        robot_id = msg.http.split('"robot_id":"')[-1].split('","')[0]
        # print_warn("robot_id:%s" % robot_id)
        if robot_id not in robot_list:
            return
        if url == "/v2/robot/input_hint" or url == "/v2/robot/query" or url == "/v1/robot/intention":
            proxy.on('response', on_response, idx=msg.id, req=msg, url=url)
        else:
            # print_warn("URL:[%s]不在监控范围内!" % url)
            return
    except Exception as e:
        print_error(e)
        log.logger.error(e)


def on_response(proxy, msg, **kwargs):
    """
    param proxy: AsyncioGor实例化对象
    param msg: 请求信息
    param kwargs: 包含:id ,请求信息，URL等信息的字典
    return None
    """
    try:
        proxy.on('replay', on_replay,
                 idx=kwargs['req'].id, req=kwargs['req'], resp=msg, url=kwargs["url"])
    except Exception as e:
        print_error(e)
        log.logger.error(e)


def on_replay(proxy, msg, **kwargs):
    """
    param proxy: AsyncioGor实例化对象
    param msg: 请求信息
    param kwargs: 包含:id ,请求信息，URL等信息的字典
    return None
    """
    try:
        parse_message = proxy.http_status(msg.http)
        replay_body = proxy.http_body(msg.http)
        resp_status = proxy.http_status(kwargs['resp'].http)
        resp_body = proxy.http_body(kwargs['resp'].http)
        url = kwargs["url"]
        print_info("#" * 50)
        request_body = kwargs['req'].http.split(
            "Accept-Encoding: gzip,deflate\r\n\r\n")[1]
        print_warn("URL: %s" % url)
        print_info("request body: %s" % request_body)
        print_warn("replay response: %s\norigin response: %s" %
                   (replay_body, resp_body))

        if parse_message == resp_status:
            if replay_body != resp_body:
                replay_body = eval(replay_body.replace(
                    ':,', ':"",').replace('null', '[]'))
                resp_body = eval(resp_body.replace(
                    ':,', ':"",').replace('null', '[]'))
                if url == "/v2/robot/input_hint":
                    check_hint_input(request_body, replay_body, resp_body)
                elif url == "/v2/robot/query":
                    check_query(request_body, replay_body, resp_body)
                elif url == "/v1/robot/intention":
                    check_intention(request_body, replay_body, resp_body)
            else:
                replay_response_ok()
        else:
            replay_response_error(request_body, replay_body, resp_body)
    except Exception as e:
        print_error(e)
        log.logger.error(e)


def check_hint_input(request_info, replay_body, resp_body):
    """
    param request_info: 请求信息
    param replay_body: replay 服务器响应结果
    param resp_body: origin 服务器相应结果
    return None
    """
    if replay_body["results"].get("hint_list") and len(replay_body["results"]["hint_list"]) &gt; 0:
        replay_response_warn(request_info, replay_body, resp_body)
    else:
        replay_response_error(request_info, replay_body, resp_body)


def check_query(request_info, replay_body, resp_body):
    """
    param request_info: 请求信息
    param replay_body: replay 服务器响应结果
    param resp_body: origin 服务器相应结果
    return None
    """
    pass # 校验逻辑可自己补充


def check_intention(request_info, replay_body, resp_body):
    """
    param request_info: 请求信息
    param replay_body: replay 服务器响应结果
    param resp_body: origin 服务器相应结果
    return None
    """
    if replay_body["results"].get("intention_list") and len(replay_body["results"]["intention_list"]) &gt; 0:
        replay_response_ok()
    else:
        replay_response_error(request_info, replay_body, resp_body)


def replay_response_warn(request_info, replay_body, resp_body):
    """
    param request_info: 请求信息
    param replay_body: replay 服务器响应结果
    param resp_body: origin 服务器相应结果
    return None
    """
    print_warn('please check replay body and response body\n')
    # log.logger.warning("#" * 50)
    log.logger.warning('please check replay body and response body\n')
    log.logger.warning("#request body#:%s #replay resqponse#:%s #origin response#:%s" %
                       (request_info, replay_body, resp_body))
    log.logger.info("#" * 50)
    print_info("#" * 50)
    print_info("\n\n\n")


def replay_response_ok():
    print_ok('replay body is same as response body\n')
    print_info("#" * 50)
    print_info("\n\n\n")


def replay_response_error(request_info, replay_body, resp_body):
    """
    param request_info: 请求信息
    param replay_body: replay 服务器响应结果
    param resp_body: origin 服务器相应结果
    return None
    """
    print_error('replay body diffs from response body\n')
    # log.logger.error("#" * 50)
    log.logger.error('replay body diffs from response body\n')
    log.logger.error("#request body#:%s #replay resqponse#:%s #origin response#:%s" %
                     (request_info, replay_body, resp_body))
    log.logger.info("#" * 50)
    print_info("#" * 50)
    print_info("\n\n\n")


if __name__ == '__main__':
    proxy = AsyncioGor()
    proxy.on('request', on_request)
    proxy.run()


```

#### 3.3 python3中间件官方文档


