
--- 
title:  Python智能家居系统后端源码，基于Django+MQTT+ESP8266的智能家居系统源码 
tags: []
categories: [] 

---
## MyHouse智能家居系统

代码下载地址：

### 环境：

##### 服务器硬件环境：
- 处理器：Intel® Xeon® CPU E5-2680 v4 @ 2.40GHz 1核- 内存：2GB- 硬盘空间：60GB
##### 单片机环境：
- 单片机：ESP8266-12E NodeMCU- 开发环境：Arduino IDE（1.8.19）
##### 软件环境：
- 操作系统：Ubuntu 18.04 LTS- 编程语言：Python（3.7.9）- Web后端框架：django（2.2.0）- 分布式消息队列：Celery（5.1.0）- 反向代理服务器：Nginx（1.14.2）- Web服务器：Gunicorn（20.1.0）- 数据库：MariaDB（10.3）- 缓存：Redis（5.0.14）- MQTT服务器：Mosquitto（1.5.7）- 开发工具：PyCharm、Visual Studio Code
### 安装：
1. 安装nginx服务器：`sudo apt-get install nginx`1. 安装MariaDB数据库：`sudo apt-get install mysql-server`1. 安装python3环境：`sudo apt-get install python3`1. 安装Redis数据库：`sudo apt-get install redis-server`1. 安装MQTT服务器（Mosquitto）：`sudo apt-get install mosquitto`1. 安装web服务器Gunicorn：`pip install gunicorn==20.1.0`1. 安装Django框架：`pip install django==2.2.0`1. 安装消息队列celery：`pip install celery==5.1.0`1. 安装django富文本编辑器：`pip install django-ckeditor==6.1.0`1. 安装django跨域插件：`pip install django-cors-headers==3.7.0`1. 安装django定时任务：`pip install django-crontab==0.7.1`1. 安装redis组件：`pip install redis==3.5.3 django-redis==5.0.0 django-redis-sessions==0.6.2`1. 安装APM组件：`pip install django-silk==4.2.0`1. 安装后台管理组件：`pip install django-simpleui`1. 安装WebSocket支持：`pip install dwebsocket==0.5.12`1. 安装MQTT组件：`pip install paho-mqtt==1.6.1`1. 安装django数据库组件：`pip install MySQL-python`1. 安装全文检索框架： `pip install django-haystack==3.1.1`1. 安装搜索引擎：`pip install whoosh==2.7.4`1. 安装分词库：`pip install jieba`1. 安装其他：`pip install psutil platform requests getpass`
### 项目启动
1. 配置：进入`/MyHouse/settings.py`，更改数据库、缓存、MQTT服务器、后端IP地址、Silk数据存储目录等项目基本信息1. 更改gunicorn配置：进入`gunicorn.conf.py`，更改`accesslog`及`errorlog`路径1. 建立whoosh索引：在项目目录下运行：`python manage.py rebuild_index`1. 更改服务启动脚本：进入`start_myhouse.sh`，更改`celery_log_path`1. 运行服务启动脚本：`bash start_myhouse.sh`
### Redis缓存说明
- db 0: session- db 1: celery- db 2: ip黑名单- db 3: 敏感词- db 4: 用户ws消息- db 5: 客服ws消息- db 6: 注册验证缓存- db 7: 修改验证缓存- db 8:- db 9:- db 10:- db 11:- db 12:- db 13:- db 14:- db 15: 代码下载地址：