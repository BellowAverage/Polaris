
--- 
title:  Python人脸识别签到考勤系统 
tags: []
categories: [] 

---
### 前言

本项目为IOT实验室人员签到考勤设计，系统实现功能：
- 人员人脸识别并完成签到/签退- 考勤时间计算- 保存考勤数据为CSV格式（Excel表格）
PS：本系统2D人脸识别，节约了繁琐的人脸识别训练部分，简洁快捷

该项目为测试版，正式版会加入更多的功能，持续更新中..... 测试版项目地址我会放到结尾

#### 项目效果图

###### 登陆界面

###### 主界面展示图：

###### 签到功能展示

<img src="https://img-blog.csdnimg.cn/img_convert/a91a16a41fd8b163b52a9c4353dc486b.png" alt="a91a16a41fd8b163b52a9c4353dc486b.png"><img src="https://img-blog.csdnimg.cn/img_convert/8361772531169f8bffb4b7c6141d924f.png" alt="8361772531169f8bffb4b7c6141d924f.png">

###### 签退功能展示

###### 后台签到数据记录

###### 是否签到/退判断

### 项目环境

核心环境：
- OpenCV-Python     4.5.5.64- face_recognition 1.30- face_recognition_model   0.3.0- dlib 19.23.1
UI窗体界面:
- PyQt5                        5.15.4- pyqt5-plugins                5.15.4.2.2- PyQt5-Qt5                    5.15.2- PyQt5-sip                    12.10.1- pyqt5-tools                  5.15.4.3.2
#### 编译器

Pycham 2021.1.3<img src="https://img-blog.csdnimg.cn/img_convert/b07c9a28f77dea8ca273baefcc5b392d.png" alt="b07c9a28f77dea8ca273baefcc5b392d.png">

```
**Python版本 3.9.12**
```

<img src="https://img-blog.csdnimg.cn/img_convert/0cbc663eea323cbe129d8a764aaa5961.png" alt="0cbc663eea323cbe129d8a764aaa5961.png">Anaconda<img src="https://img-blog.csdnimg.cn/img_convert/7f428bdb07a5bf2639af9ff1c32d0747.png" alt="7f428bdb07a5bf2639af9ff1c32d0747.png">

###### 辅助开发QT-designer

<img src="https://img-blog.csdnimg.cn/img_convert/0a6b4be1b8c07e24e498b60c3a457589.png" alt="0a6b4be1b8c07e24e498b60c3a457589.png"><img src="https://img-blog.csdnimg.cn/img_convert/39595fd5809ec8bc15220841a7157a83.png" alt="39595fd5809ec8bc15220841a7157a83.png">

###### 项目配置

### 代码部分

###### 核心代码

**「MainWindow.py」****UI文件加载：**

```
class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)       ##加载QTUI文件

        self.runButton.clicked.connect(self.runSlot)

        self._new_window = None
        self.Videocapture_ = None
```

**摄像头调用：**

```
def refreshAll(self):
        print("当前调用人俩检测摄像头编号（0为笔记本内置摄像头，1为USB外置摄像头）：")
        self.Videocapture_ = "0"
```

**「OutWindow.py」****获取当前系统时间**

```
class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        loadUi("./outputwindow.ui", self)   ##加载输出窗体UI

        ##datetime 时间模块
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')  ##时间格式
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

        self.image = None
```

**签到时间计算**

```
def ElapseList(self,name):
        with open('Attendance.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 2

            Time1 = datetime.datetime.now()
            Time2 = datetime.datetime.now()
            for row in csv_reader:
                for field in row:
                    if field in row:
                        if field == 'Clock In':
                            if row[0] == name:
                                Time1 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList1.append(Time1)
                        if field == 'Clock Out':
                            if row[0] == name:
                                Time2 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList2.append(Time2)
```

**人脸识别部分**

```
## 人脸识别部分
        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            name = "unknown"    ##未知人脸识别为unknown
            best_match_index = np.argmin(face_dis)
            if match[best_match_index]:
                name = class_names[best_match_index].upper()
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            mark_attendance(name)

        return frame
```

**签到数据保存与判断**

```
## csv表格保存数据
        def mark_attendance(name):
            """
            :param name: 人脸识别部分
            :return:
            """
            if self.ClockInButton.isChecked():
                self.ClockInButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                        if (name != 'unknown'):         ##签到判断：是否为已经识别人脸
                            buttonReply = QMessageBox.question(self, '欢迎 ' + name, '开始签到' ,
                                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                            if buttonReply == QMessageBox.Yes:

                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},Clock In')
                                self.ClockInButton.setChecked(False)

                                self.NameLabel.setText(name)
                                self.StatusLabel.setText('签到')
                                self.HoursLabel.setText('开始签到计时中')
                                self.MinLabel.setText('')

                                self.Time1 = datetime.datetime.now()
                                self.ClockInButton.setEnabled(True)
                            else:
                                print('签到操作失败')
                                self.ClockInButton.setEnabled(True)
            elif self.ClockOutButton.isChecked():
                self.ClockOutButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                        if (name != 'unknown'):
                            buttonReply = QMessageBox.question(self, '嗨呀 ' + name, '确认签退?',
                                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                            if buttonReply == QMessageBox.Yes:
                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},Clock Out')
                                self.ClockOutButton.setChecked(False)

                                self.NameLabel.setText(name)
                                self.StatusLabel.setText('签退')
                                self.Time2 = datetime.datetime.now()

                                self.ElapseList(name)
                                self.TimeList2.append(datetime.datetime.now())
                                CheckInTime = self.TimeList1[-1]
                                CheckOutTime = self.TimeList2[-1]
                                self.ElapseHours = (CheckOutTime - CheckInTime)
                                self.MinLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60)%60) + 'm')
                                self.HoursLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60**2)) + 'h')
                                self.ClockOutButton.setEnabled(True)
                            else:
                                print('签退操作失败')
                                self.ClockOutButton.setEnabled(True)
```

###### 项目目录结构

### 后记
- 因为本系统没有进行人脸训练建立模型，系统误识别率较高，安全性较低- 系统优化较差，摄像头捕捉帧数较低（8-9），后台占有高，CPU利用率较高- 数据保存CSV格式，安全性较低
#### 正式版改进
- 加入TensorFlow深度学习，提高系统人脸识别安全性与准确性- 加入MySQL数据库，对签到数据进行更安全保护，不易被修改- 美化优化UI设计
源码在公众号**Python小二**后台回复**考勤签到**获取~

推荐阅读  点击标题可跳转
- - - - - - - - 
```
点分享

点点赞

点在看
```
