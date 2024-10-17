
--- 
title:  用 Python 写一个颜值测试小工具 
tags: []
categories: [] 

---
我们知道现在有一些利用照片来测试颜值的网站或软件，其实使用 Python 就可以实现这一功能，本文我们使用 Python 来写一个颜值测试小工具。

### 简介

要实现颜值测试功能，大致有两种方式：一种是自己编写检测功能，另一种是借助第三方接口来实现检测功能，比如：百度云接口，为了方便，本文我们采用百度云接口，接口的注册这里就不说了，如果不太清楚注册流程的话，可以参考一下我之前写的车牌识别这篇文章：`https://blog.csdn.net/ityard/article/details/105673451`。

我们需要用到的 Python 库主要包括：pillow、baidu-aip、tkinter，安装使用 `pip install pillow/baidu-aip/tkinter` 即可。

### 实现

首先，我们来看一下如何利用照片通过百度云接口获取性别、年龄、颜值信息，代码实现如下所示：

```
APP_ID = '自己的APP_ID'
API_KEY = '自己的API_KEY'
SECRET_KEY = '自己的SECRET_KEY'
face = AipFace(APP_ID, API_KEY, SECRET_KEY)
image_type = 'BASE64'
options = {<!-- -->'face_field': 'age,gender,beauty'}

def get_file_base64(file_path):
  with open(file_path, 'rb') as fr:
    content = base64.b64encode(fr.read())
    return content.decode('utf8')

def get_score(file_path):
  # 脸部识别分数
  result = face.detect(get_file_base64(file_path), image_type, options)
  # print(result)
  age = result['result']['face_list'][0]['age']
  beauty = result['result']['face_list'][0]['beauty']
  gender = result['result']['face_list'][0]['gender']['type']
  return age, beauty, gender

```

这里我们使用 tkinter 创建 GUI 来进行照片选取和接口调用的操作，下面看一下代码的主要实现。

首先，我们创建一个窗口，代码实现如下：

```
root = tk.Tk()
# 设置窗口大小
root.geometry('700x450')
# 为窗口添加标题
root.title('颜值测试工具')
# 设置背景色
canvas = tk.Canvas(root,
          width=700,
          height=450,
          bg='#EEE8AA')
canvas.pack()

```

我们接着向窗口中添加两个按钮，一个用来选择照片，另一个用来调用接口，代码实现如下：

```
# 照片选择按钮
  tk.Button(self.root, text='选择照片', font=('华文行楷', 16), command=self.show_img).place(x=40, y=180)
  # 颜值测试按钮
  tk.Button(self.root, text='查看颜值', font=('华文行楷', 16), command=self.set_score).place(x=40, y=280)

```

我们还需要创建三个输入框来显示接口返回的性别、年龄和颜值信息，代码实现如下：

```
tk.Label(self.root, text='性别', bg='#EEE8AA', fg='#0AB0D5', font=('华文行楷', 20)).place(x=500, y=150)
self.text1 = tk.Text(self.root, width=10, height=2)
tk.Label(self.root, text='年龄', bg='#EEE8AA', fg='#0AB0D5', font=('华文行楷', 20)).place(x=500, y=260)
self.text2 = tk.Text(self.root, width=10, height=2)
tk.Label(self.root, text='颜值', bg='#EEE8AA', fg='#0AB0D5', font=('华文行楷', 20)).place(x=500, y=360)
self.text3 = tk.Text(self.root, width=10, height=2)
# 填装文字
self.text1.place(x=580, y=150)
self.text2.place(x=580, y=260)
self.text3.place(x=580, y=360)

```

看一下实现效果：

<img src="https://img-blog.csdnimg.cn/20201107084842886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt=""> 原文链接：

源码在公号 **Python小二** 后台回复 **200613** 获取。
