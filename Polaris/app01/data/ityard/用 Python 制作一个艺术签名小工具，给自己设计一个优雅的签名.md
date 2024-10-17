
--- 
title:  用 Python 制作一个艺术签名小工具，给自己设计一个优雅的签名 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20200602194354844.png" alt=""> 生活中有很多场景都需要我们签字（签名），如果是一些不重要的场景，我们的签名好坏基本无所谓了，但如果是一些比较重要的场景，如果我们的签名比较差的话，就有可能给别人留下不太好的印象了，俗话说字如其人嘛，本文我们使用 Python 来制作一个艺术签名小工具，给自己设计一个优雅的签名。

实现的基本原理为：我们根据艺术签名网站生成签名的规则，模拟对于请求生成签名，然后将其显示在 tkinter 生成的 GUI 窗口中。

我们选择的艺术签名网站地址为 `http://www.uustv.com/`，打开后如下图所示： <img src="https://img-blog.csdnimg.cn/20200602194442234.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 我们接着按 F12 打开开发者工具并选择 Network，然后输入一个名字，再点`马上给我设计`按钮，我们可以看到生成签名发送的请求如下所示： <img src="https://img-blog.csdnimg.cn/20200602194458303.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70" alt=""> 现在我们就可以根据其生成签名了，实现代码如下所示：

```
url = 'http://www.uustv.com/'
name = enter.get()
if not name:
	messagebox.showinfo('提示：', '请输入您的名字')
else:
	data = {<!-- -->
		'word': name,
		'sizes': 50,
		# 'fonts': 'jfcs.ttf',  # 个性签
		# 'fonts': 'qmt.ttf',  # 连笔签
		# 'fonts': 'bzcs.ttf',  # 潇洒签
		# 'fonts': 'lfc.ttf',  # 草体签
		# 'fonts': 'haku.ttf',  # 合文签
		# 'fonts': 'zql.ttf',  # 商务签
		'fonts': 'yqk.ttf',  # 可爱签
		'fontcolor': '#000000'
	}
	result = requests.post(url, data=data)
	result.encoding = 'utf-8'
	html = result.text
	reg = '&lt;div class="tu"&gt;.*?&lt;img src="(.*?)"/&gt;&lt;/div&gt;'
	img_path = re.findall(reg, html)
	# 图片完整路径
	img_url = url + img_path[0]
	# 获取图片内容
	response = requests.get(img_url).content
	f = open('{}.gif'.format(name), 'wb')
	# 写入
	f.write(response)
	# 把图片放到窗口上，显示图片
	bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
	label = Label(root, image=bm)
	label.bm = bm
	# 绘图
	label.grid(row=2, columnspan=2)

```

然后我们再将签名显示在 tkinter 的 GUI 窗口上即可，实现代码如下所示：

```
# 创建窗口
root = Tk()
# 标题
root.title('签名设计')
# 窗口大小
root.geometry('600x300')
# 窗口的初始位置
root.geometry('+400+200')
# 标签的控件
label = Label(root, text='输入名字', font=('宋体', 16), fg='blue')
label.grid()
# 输入框
enter = Entry(root, font=('宋体', 16))
# 设置输入框的位置
enter.grid(row=0, column=1)
# 按钮
button = Button(root, text='设计签名', font=('宋体', 16), command=sign)
# 设置按钮的位置
button.grid(row=1, column=0)
# 显示窗口
root.mainloop()

```

以商务签为例，我们来看一下效果： <img src="https://img-blog.csdnimg.cn/20200602194515208.gif" alt=""> 是不是有内味了。

>  
 作者：程序员野客 公号：Python小二 链接： 

