
--- 
title:  Python人员信息管理系统（当期末作业） 
tags: []
categories: [] 

---
### 1. 涉及模块
- datetime- os- random- sys- PyQt5
2. 运行效果

<img height="651" width="1067" src="https://img-blog.csdnimg.cn/img_convert/f2aa4ebcd13b43571a93c774b95ce5ca.png" alt="f2aa4ebcd13b43571a93c774b95ce5ca.png">

支持功能：
- 添加信息- 修改信息- 删除信息- 查询信息- 文件存储数据，每次运行都会加载显示之前的信息
### 3.部分源码

```
# 创建字体对象，用来对要显示的文字进行设定
font = QtGui.QFont()
font.setFamily("黑体")
font.setPointSize(12)


# 姓名
label_name = QLabel(self)
label_name.setGeometry(40, 30, 54, 16)
label_name.setText("姓名：")
label_name.setFont(font)
self.line_edit_name = QLineEdit(self)
self.line_edit_name.setGeometry(90, 30, 141, 20)


# 性别
label_gender = QLabel(self)
label_gender.setGeometry(270, 30, 54, 16)
label_gender.setFont(font)
label_gender.setText("性别：")
self.line_edit_gender = QComboBox(self)
self.line_edit_gender.setGeometry(340, 30, 201, 20)
self.line_edit_gender.addItems(['男', '女'])


# 身份证
label_id = QLabel(self)
label_id.setGeometry(580, 30, 54, 16)
label_id.setFont(font)
label_id.setText("身份证：")
self.line_edit_id = QLineEdit(self)
self.line_edit_id.setGeometry(660, 30, 221, 20)


# 地址
label_addr = QLabel(self)
label_addr.setGeometry(40, 110, 54, 16)
label_addr.setFont(font)
label_addr.setText("地址：")
self.line_edit_addr = QLineEdit(self)
self.line_edit_addr.setGeometry(92, 110, 141, 20)


# 电话
label_phone = QLabel(self)
label_phone.setGeometry(270, 70, 54, 16)
label_phone.setFont(font)
label_phone.setText("电话:")
self.line_edit_phone = QLineEdit(self)
self.line_edit_phone.setGeometry(340, 70, 201, 20)
```

完整代码已经打包整理好了，有需要的小伙伴可以**关注下方视频号**私信**人员**免费获取~

代码免费获取方式（点击上方视频后点圆形头像点**关注**后**私信**关键字**人员**，未关注的可能不会发哦<img src="https://img-blog.csdnimg.cn/img_convert/2143dbed9d6500a4fdfafa5dbd7cc5c2.png" alt="2143dbed9d6500a4fdfafa5dbd7cc5c2.png">，已经关注的直接私信即可~）

<img src="https://img-blog.csdnimg.cn/img_convert/234edc0b9d4e0f224ad5bf6810b576fe.png" alt="234edc0b9d4e0f224ad5bf6810b576fe.png">

<img src="https://img-blog.csdnimg.cn/img_convert/2dc7125cffca71d43b08cda1501e799d.png" alt="2dc7125cffca71d43b08cda1501e799d.png">

推荐阅读  点击标题可跳转
- - - - - - - - - 
<img src="https://img-blog.csdnimg.cn/img_convert/00a604457b6d68b6fa44e5cb0c9a4894.gif" alt="00a604457b6d68b6fa44e5cb0c9a4894.gif">
