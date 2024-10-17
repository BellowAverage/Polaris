
--- 
title:  gunicorn+flask配置服务 
tags: []
categories: [] 

---
gunicorn的作用是：作为负载均衡和并发的控制

通过gunicorn启动flask

```
gunicorn main:app
// -w 并发数
gunicorn -w 4 -b 0.0.0.0:8080 main:app
// 通过配置文件读入
gunicorn --config gunicorn.conf main:app

```

来控制多线程的并发数

Flask

```
# main.pyfrom flask import Flask
# 获取程序的句柄，推荐服务的名字是app，作为程序的入口
app = Flask(__name__)

# 安装装饰器，当用户发送命令的时候可以输入数据
@app.route('/')
def index():
	# 返回的内容返回给用户
    return 'hello world'

def main():
    app.run(debug=True)

# 如果用gunicorn的话，那么必须这么写不然的话，会提示找不到
if __name__ == '__main__':
	# debug在测试是可以，正式不能开，不然会泄密堆栈信息
    app.run(debug=True, host='0.0.0.0', port=1111)

```

其余的都是看技术文档的各种api，比较简单

包括：
- cookies和session的配置
测试本地命令：

F12，然后点击报文，能看到各种Network。

测试的话，需要知道这么几个：
- 状态值，200成功， 500运行时错误，404找不到，403权限不够- 请求常见的是post和get。