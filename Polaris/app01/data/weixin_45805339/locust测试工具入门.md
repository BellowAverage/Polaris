
--- 
title:  locust测试工具入门 
tags: []
categories: [] 

---
### 1.python3环境安装

locust基于python开发，需要依赖python环境，大部分Linux发行版系统都会自带python，Ubuntu18.04自带python2.7和python3.6.9(建议使用python3) 如纯净版系统可参照下面链接进行安装：

 pyhton3安装python包需要用pip3工具，安装工具指令：

```
sudo apt install python3-pip

```

pip3默认从外网下载，所以速度会很慢。有时候下载超时，导致下载失败，建议将pip3下载镜像源改为国内镜像源，配置地址如下：



### 2.locust工具安装

locust工具安装非常简单，使用pip3工具安装，指令如下：

```
pip3 install locust
# 可指定版本：
pip3 install locust==2.1.0
# 查看版本
locust -V

```

### 3.locust使用

#### 简单用例：

详细代码可参照locust_request_test.py文件

```
class UdeskUser(HttpUser):
    wait_time = between(1, 2)

    @events.init.add_listener
    def on_locust_init(environment, **kwargs):
        """
        初始化参数，多用于分布式等环境
        :param kwargs:
        :return:
        """

    def on_start(self):
        """
        可用于用户登录测试
        :return:
        """
        print("初试化数据，只执行一次")
        # self.client.post("/login", json={"username":"admin@udesk.cn", "password":"admin"})

    def on_stop(self):
        """
        程序被杀死时调用
        :return:
        """
        print("实例用户被被杀死")

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("A new test is starting")

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print("A new test is ending")

    @task
    def post_query(self):
        """
        POST查询接口请求测试，@task(1)表示所有测试接口中所占比重为1
        :return:
        """

    @tag("tag2")
    @task(10)
    def post_query_2(self):
        response = self.client.post("/v2/robot/query", json={<!-- -->"robot_id": "222", "query": "北京大学怎么走？", })
        # print("response:{}".format(response.text))
        self.parse_robot_query_post_result(response.content)

    def parse_robot_query_post_result(self, bytes_data):
        """
        解析查询响应的json数据
        :param bytes_data:
        :return:
        """


    def get_query_dict(self):
        """
        获取查询问答字典
        :return:
        """

```

#### 启动locust测试工具

```
# 命令行执行
locust -f locust_request_test.py --host http://120.78.15.109:17555
# locust_request_test.py 为测试功能代码脚本，--host 指定测试服务的ip:port

```

也可以在locust.conf 中配置启动参数

```
# 指定测试脚本
locustfile = /Users/wuhao/Desktop/locust_request_test_project/locust_request_test.py
# 指定待测试服务器host
host = http://120.78.15.109:17555
# 指定非测试任务
exclude-tags = tag2
# 指定log地址
logfile = /Users/wuhao/Desktop/locust_request_test_project/log/locust.log

```

命令行指令：

```
locust --config=./locust.conf
# ./locust.conf 配置文件路径

```

### 4.web_UI扩展

locust支持web_ui扩展功能，详细代码可参照locust_request_test.py文件 简单用例如下：

```
# web_ui 拓展开发
stats = {<!-- -->}
response_list = []
path = os.path.dirname(os.path.abspath(__file__))
extend = Blueprint(
    "extend",
    "extend_web_ui",
    static_folder=f"{<!-- -->path}/static/",
    static_url_path="/static/",
    template_folder=f"{<!-- -->path}/templates/",
)


@events.init.add_listener
def locust_init(environment, **kwargs):
    """
    我们得找个地方储存数据。
    在主节点上，统计数据将包含所有成功测试的汇总和，而在工作节点上，
    这将是自上次统计报告发送到主节点以来的成功测试的总和
    """

def on_request(request_type, name, response_time, response_length, exception, context, response, **kwargs):
    """
    Event handler that get triggered on every request
    :param request_type:
    :param name:
    :param response_time:
    :param response_length:
    :param exception:
    :param context:
    :param kwargs:
    :return:
    """

@events.reset_stats.add_listener
def on_reset_stats():
    """
    Event handler that get triggered on click of web UI Reset Stats button
    """
    global stats
    stats = {<!-- -->}

```

### 5.查询接口压力测试目录结构

```
# locust_request_test_project 目录结构 
├── common
│   ├── __init__.py
│   ├── auth.py
│   └── config.py
├── locust.conf
├── locust_request_test.py
├── log
│   └── locust.log
├── query.txt
├── requirements
│   └── requirements.txt
├── static
│   └── extend.js
└── templates
    └── extend.html
# common 公共基础包
# locust.conf 配置文件
# log 日志文件
# requirements python需求包
# locust_request_test.py 测试脚本文件
# static web_ui扩展 静态文件（包括.js文件等）
# templates 前端页面文件

```

### 6.帮助文档


