
--- 
title:  flask实现文件简易服务器，可根据链接上传下载 
tags: []
categories: [] 

---
flask实现文件简易服务器，可根据链接上传下载

```
# -*- encoding: utf-8 -*-
from flask import send_file, request
from gevent import pywsgi
from flask import Flask
import sys
import os
import time

sys.path.append('../..')

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    """接受前端传送过来的文件"""
    file_obj = request.files.get("file")
    # print(file_obj)
    if file_obj is None:
        return "文件上传为空"

    # 直接使用文件上传对象保存
    time_str = time.strftime("%Y%m%d_%H%M%S")
    path = os.getcwd() + '\\download\\' + time_str + file_obj.filename
    print(path)
    file_obj.save(path)
    return "文件上传成功\n"


@app.route('/download')
def download():
    """
    简单的文件服务器
    提供文件下载服务
    浏览器下载：示例：文件1.TXT的下载链接：http://127.0.0.1:10011/download?file_name=1.txt
    linux下载：示例：文件1.TXT的下载链接：curl -# -o 1.txt http://127.0.0.1:10011/download?file_name=1.txt
    :return:
    """
    file_name = request.args.get('file_name')
    path = os.getcwd() + '/files/%s' % file_name
    return send_file(path)


if __name__ == "__main__":
    print('启动成功，端口9090')
    server = pywsgi.WSGIServer(('0.0.0.0', 9090), app)
    server.serve_forever()


```
