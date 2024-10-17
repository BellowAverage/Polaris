
--- 
title:  Flask 实现文件上传和下载（简单但实用） 
tags: []
categories: [] 

---
### 目录结构和代码 

```
root@master ~/w/upload# ll
total 4.0K
drwxr-xr-x. 3 root root  21 Jul  2 17:32 static/
drwxr-xr-x. 2 root root  25 Jul  5 17:40 templates/
-rw-r--r--. 1 root root 819 Jul  5 09:55 upload.py


root@master ~/workspace# tree upload/
upload/
|-- static
|   `-- uploads
|-- templates
|   `-- upload.html
`-- upload.py

3 directories, 2 files

```

upload.html

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;upload:&lt;/h1&gt;
    &lt;form action="" enctype='multipart/form-data' method='POST'&gt;
        &lt;input type="file" name="file"&gt;
        &lt;input type="submit" value="upload"&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;

```

upload.py

```
# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static/uploads', f.filename)
        f.save(upload_path)
        print('uploading ...')
    return render_template('upload.html')

@app.route('/download')
def download():
    dir_path = "/root/"
    filename = "test.sh"
    print('downloading ...')
    return send_from_directory(dir_path, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

```

### 上传和下载测试 

启动服务(默认端口是 5000)：

```
root@master ~/w/upload# python3 upload.py
 * Serving Flask app "upload" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 332-961-513

```

选择上传文件（**如果页面打不开，可以先用 systemctl stop firewalld 命令关闭防火墙或者开放指定端口**）：

<img alt="" height="216" src="https://img-blog.csdnimg.cn/20210705174431652.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="814">

点击上传（上传后自动下载了测试文件 test.sh）： 

<img alt="" height="654" src="https://img-blog.csdnimg.cn/20210705174727874.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1RvbW9ycm93QW5kVHV0dXJl,size_16,color_FFFFFF,t_70" width="1200">

上传成功：

<img alt="" height="89" src="https://img-blog.csdnimg.cn/20210705174832556.png" width="908">
