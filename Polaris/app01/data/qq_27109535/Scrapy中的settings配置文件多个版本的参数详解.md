
--- 
title:  Scrapy中的settings配置文件多个版本的参数详解 
tags: []
categories: [] 

---
Scrapy中的settings配置文件多个版本的参数详解

```
# -*- coding: utf-8 -*-
 
# Scrapy settings for demo1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
 
BOT_NAME = 'demo1'   #Scrapy项目的名字,这将用来构造默认 User-Agent,同时也用来log,当您使用 startproject 命令创建项目时其也被自动赋值。
 
SPIDER_MODULES = ['demo1.spiders']   #Scrapy搜索spider的模块列表 默认: [xxx.spiders]
NEWSPIDER_MODULE = 'demo1.spiders'   #使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'
 
 
#爬取的默认User-Agent，除非被覆盖
#USER_AGENT = 'demo1 (+http://www.yourdomain.com)'
 
#如果启用,Scrapy将会采用 robots.txt策略
ROBOTSTXT_OBEY = True
 
#Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
#CONCURRENT_REQUESTS = 32
 
#为同一网站的请求配置延迟（默认值：0）
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs  
#DOWNLOAD_DELAY = 3   下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
 
    
#下载延迟设置只有一个有效
#CONCURRENT_REQUESTS_PER_DOMAIN = 16   对单个网站进行并发请求的最大值。
#CONCURRENT_REQUESTS_PER_IP = 16       对单个IP进行并发请求的最大值。如果非0,则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。
 
#禁用Cookie（默认情况下启用）
#COOKIES_ENABLED = False
 
#禁用Telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False 
 
#覆盖默认请求标头：
#DEFAULT_REQUEST_HEADERS = {
   <!-- -->
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
 
#启用或禁用蜘蛛中间件
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
   <!-- -->
#    'demo1.middlewares.Demo1SpiderMiddleware': 543,
#}
 
#启用或禁用下载器中间件
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
   <!-- -->
#    'demo1.middlewares.MyCustomDownloaderMiddleware': 543,
#}
 
#启用或禁用扩展程序
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
   <!-- -->
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}
 
#配置项目管道
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
   <!-- -->
#    'demo1.pipelines.Demo1Pipeline': 300,
#}
 
#启用和配置AutoThrottle扩展（默认情况下禁用）
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
 
#初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
 
#在高延迟的情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
 
 
#Scrapy请求的平均数量应该并行发送每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
 
#启用显示所收到的每个响应的调节统计信息：
#AUTOTHROTTLE_DEBUG = False
 
#启用和配置HTTP缓存（默认情况下禁用）
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
 

```

解释几个参数：

```
ROBOTSTXT_OBEY = True-----------是否遵守robots.txt

CONCURRENT_REQUESTS = 16-----------开启线程数量，默认16

AUTOTHROTTLE_START_DELAY = 3-----------开始下载时限速并延迟时间

AUTOTHROTTLE_MAX_DELAY = 60-----------高并发请求时最大延迟时间

最底下的几个：是否启用在本地缓存，如果开启会优先读取本地缓存，从而加快爬取速度，视情况而定

HTTPCACHE_ENABLED = True

HTTPCACHE_EXPIRATION_SECS = 0

HTTPCACHE_DIR = 'httpcache'

HTTPCACHE_IGNORE_HTTP_CODES = []

HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

以上几个可以视项目需要开启，但是有两个参数最好每次都开启，而每次都是项目文件手动开启不免有些麻烦，最好是项目创建后就自动开启


#DEFAULT_REQUEST_HEADERS = {
   <!-- -->
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

```

```
# scrapy默认深度优先, 如果想换成广度优先..添加下面代码.
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue
SCHEDULER_ORDER = ‘BFO’

# 增加全局并发数
CONCURRENT_REQUESTS = 100

# LOG_FILE = 'spider_name.log' # 最好为爬虫名称
LOG_FILE = BOT_NAME + '_' + time.strftime("%Y%m%d", time.localtime()) + '.log'

# 日志等级
LOG_LEVEL = 'INFO'

# 是否启用日志（创建日志后，不需开启，进行配置）
LOG_ENABLED = True # （默认为True，启用日志）

# 日志编码
LOG_ENCODING = 'utf-8'

# 如果是True ，进程当中，所有标准输出（包括错误）将会被重定向到log中;例如：在爬虫代码中的 print（）
LOG_STDOUT = False # 默认为False

# 如果使用自定义cookie就把COOKIES_ENABLED设置为True
# 如果使用settings的cookie就把COOKIES_ENABLED设置为False

#Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
#CONCURRENT_REQUESTS = 32

#为同一网站的请求配置延迟（默认值：0）
#DOWNLOAD_DELAY = 3 下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
#下载延迟设置只有一个有效

#CONCURRENT_REQUESTS_PER_DOMAIN = 16 对单个网站进行并发请求的最大值。
#CONCURRENT_REQUESTS_PER_IP = 16  对单个IP进行并发请求的最大值。如果非0,则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。
#覆盖默认请求标头：  不包含cookie
#DEFAULT_REQUEST_HEADERS = {
   <!-- -->
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language': 'en',
#}

#启用或禁用蜘蛛中间件
#SPIDER_MIDDLEWARES = {
   <!-- -->
# 'demo1.middlewares.Demo1SpiderMiddleware': 543,
#}

#启用或禁用下载器中间件
#DOWNLOADER_MIDDLEWARES = {
   <!-- -->
# 'demo1.middlewares.MyCustomDownloaderMiddleware': 543,
#}

#启用或禁用扩展程序
#EXTENSIONS = {
   <!-- -->
# 'scrapy.extensions.telnet.TelnetConsole': None,
#}

#配置项目管道
#ITEM_PIPELINES = {
   <!-- -->
# 'demo1.pipelines.Demo1Pipeline': 300,
#}

#启用和配置AutoThrottle扩展（默认情况下禁用）
#AUTOTHROTTLE_ENABLED = True

#初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5 


#在高延迟的情况下设置的最大下载延迟

#AUTOTHROTTLE_MAX_DELAY = 60

#Scrapy请求的平均数量应该并行发送每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

#启用显示所收到的每个响应的调节统计信息：
#AUTOTHROTTLE_DEBUG = False

#启用和配置HTTP缓存（默认情况下禁用）
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


```

```
-- coding: utf-8 --
Scrapy settings for step8_king project
For simplicity, this file contains only settings considered important or
commonly used. You can find more settings consulting the documentation:
http://doc.scrapy.org/en/latest/topics/settings.html
http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
1. 爬虫名称
BOT_NAME = ‘step8_king’

2. 爬虫应用路径
SPIDER_MODULES = [‘step8_king.spiders’]
NEWSPIDER_MODULE = ‘step8_king.spiders’

Crawl responsibly by identifying yourself (and your website) on the user-agent
3. 客户端 user-agent请求头
USER_AGENT = ‘step8_king (+http://www.yourdomain.com)’
Obey robots.txt rules
4. 禁止爬虫配置
ROBOTSTXT_OBEY = False
Configure maximum concurrent requests performed by Scrapy (default: 16)
5. 并发请求数
CONCURRENT_REQUESTS = 4
Configure a delay for requests for the same website (default: 0)
See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
See also autothrottle settings and docs
6. 延迟下载秒数
DOWNLOAD_DELAY = 2
The download delay setting will honor only one of:
7. 单域名访问并发数，并且延迟下次秒数也应用在每个域名
CONCURRENT_REQUESTS_PER_DOMAIN = 2
单IP访问并发数，如果有值则忽略：CONCURRENT_REQUESTS_PER_DOMAIN，并且延迟下次秒数也应用在每个IP
CONCURRENT_REQUESTS_PER_IP = 3
Disable cookies (enabled by default)
8. 是否支持cookie，cookiejar进行操作cookie
COOKIES_ENABLED = True
COOKIES_DEBUG = True
Disable Telnet Console (enabled by default)

```
