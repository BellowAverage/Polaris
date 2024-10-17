
--- 
title:  用Python做一个游戏辅助脚本，完整编程思路分享 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/aa146fc1198cb175abef56cfee13abbb.png">

一、说明

简述：本文将以4399小游戏《 宠物连连看经典版2 》作为测试案例，通过识别小图标，模拟鼠标点击，快速完成配对。对于有兴趣学习游戏脚本的同学有一定的帮助。

运行环境：Win10/Python3.5。

主要模块：win32gui（识别窗口、窗口置顶等操作）、PIL（屏幕截图）、numpy（创建矩阵）、operator（比较值）、pymouse（模拟鼠标点击）。

注意点：

1、如果安装pymouse不成功或者运行报错，可以考虑先通过whl 安装pyHook、然后再通过pip安装pyuserinput。

2、如果报错 [ImportError: No module named 'windows' ]，可以修改__init__.py相应的行 为 windows =&gt; pymouse.windows。

本文主要参考：https://baijiahao.baidu.com/s?id=1618385402903335091&amp;wfr=spider&amp;for=pc。

二、开发前景（随便唠叨一哈，可跳过）

游戏辅助脚本在当前环境也算是比较流行了，对于经常玩游戏人来说，适当的游戏辅助还是很有帮助的，让计算机做一些繁琐乏味的操作。当然还有更加高大上的其他操作，这里就不赘述了。对于游戏辅助脚本，能想到基本有以下两种：一是读取游戏在内存中的数据，理想的话可以做到更改游戏一些基本属性，原理和很多的外挂或破解游戏类似；二是模拟用户用户行为，模拟鼠标点击、键盘操作等。当然，由于本人从未涉及游戏辅助脚本这一领域，出于个人兴趣，学习研究一下，本文例子则是第二种，主要还是模拟用户行为，让程序代替用户操作。

三、开发流程

先看看程序运行图吧：

<img src="https://img-blog.csdnimg.cn/img_convert/f3fe23b1b0e81f6c908249602e28bcd8.gif">

浏览器打开游戏窗口（单个一个窗口），游戏界面如下图所示，游戏主要界面截图需要两个坐标（左上角坐标和右下角坐标）来确定，原点一般是屏幕左上角，不确定坐标点值的同学，可以全屏截图，用编辑图片软件查看坐标值。获取窗口句柄，这里就是浏览器标题栏的标题了（右键-查看源代码-title，加上软件名）比如：“宠物连连看经典2,宠物连连看经典版2小游戏,4399小游戏 www.4399.com - Google Chrome“。获取窗口句柄就可以开始了。

总体开发思路：截取游戏主图 ---&gt; 分割成小图 ---&gt; 对比每个小图，对比图片相识度，编号存入矩阵 ---&gt; 对矩阵进行可连计算 ---&gt; 模拟点击。

<img src="https://img-blog.csdnimg.cn/img_convert/76905b4a83607bd2bbce08ec1d23275a.png">

3.1、获取窗口句柄，把窗口置顶

python可以使用win32gui模块调用Windows API实现对窗口的操作，使用FindWindow()方法可以获取窗口的句柄（handle），需要传入两个参数，第一个为父窗口句柄（这里填0即可），第二个参数是窗口的名称（标签title - Google Chrome）。获取句柄之后然后通过SetForegroundWindows() 设置窗口在前面，这里传入游戏窗口的举报即可，代码如下：

<img src="https://img-blog.csdnimg.cn/img_convert/c2bfe7c2cf0c9c8d8acf93c0fc79237b.png">

3. 2、截取游戏界面，分割图标，图片比较

这里需要花费一些时间来校验程序，如果截取的图片不好，则会影响后续操作，所以比较主要的是确认游戏左上角和右下角这两个坐标值，以及每个小图标的宽高。如下图所示，先截取整个游戏界面图，然后分割小图标，接着对每个图标进行比较，然后以编号代替图标存入矩阵（这里的编号矩阵和游戏图不一致，原理一样）。

<img src="https://img-blog.csdnimg.cn/img_convert/9fd5bc7e2d892ebb912875bd59d1f05f.png">

根据初始化设定的左上角和右下角两个坐标，使用ImageGrab.grab()方法进行截图，传入一个元组即可，然后对这个大图进行分割，切割成一个个小图标存入到images_list数组中。

<img src="https://img-blog.csdnimg.cn/img_convert/932c0519bc88688ddb1b455d7e0fbff1.png">

通过上面代码切割的小图标，转成数字矩阵，如果图标已经存入image_type_list则返回这个索引，如果不存在，则在追加进去，然后当前长度就是这个新加入图标的编号，代码如下所示：

<img src="https://img-blog.csdnimg.cn/img_convert/777f239d0f00532a9a4af9d05ac77049.png">

上面的getIndex就是对比图片，判断图标是否出现过（是否已存在image_type_list中，没出现则追加进去），这里使用汉明距离判断两个图片的相识度，设置阀值10，当小于阀值则认为是同一个图片，具体代码如下：

<img src="https://img-blog.csdnimg.cn/img_convert/a6fade27303721e50778c0ab3532fa4e.png">

四、程序核心-图标连接算法（路径寻找）

这里仅对算法代码进行简单分析，如果对程序不好理解，可以留言，后续可以图文分析。

通过上面的开发流程，基本获取如下这样的矩阵，只要比较两个编号相同的值进行可连路径寻找，如果找到即进行模拟点击操作。这里简单介绍下游戏规则：8行乘12列游戏图标区域，外围的0其实表示寻找路径的时候可以通过，例如坐标（1, 1）可以与（1,10）进行连接、（7, 1）和（7,2）进行连接。

<img src="https://img-blog.csdnimg.cn/img_convert/faafe37775f876b0131d8ada3ec64dbe.png">

算法的思路：路径的寻找首先是寻找一个坐标的横向竖向可以直接相连的坐标集合，比如坐标p1（1,1）这样的集合有[ （0,1）, （1,0） ]，另外一个坐标p2（1,10）的可连集合为[ （0,10） ]，然后再对p1和p2的可连坐标集合进行比较，如果集合中坐标也有可连，则表示p1和p2可连，很明显，（0,1）和（0,10）为同一行且可连，这样就表示p1和p2两点存在可连路径了，代码如下所示：

简单分析下代码实现过程：在isReachable()传入两个需要比较的坐标值，然后分别获取两个点横竖向（isRowConnect()、isColConnect()）可以连接的坐标集合，最后再对集合进行遍历比较是否存在可连的，如果存在则表示传入的两个坐标是可以连接的。

<img src="https://img-blog.csdnimg.cn/img_convert/a7a3595d8667d78469c7f217f76e5b9f.png">

<img src="https://img-blog.csdnimg.cn/img_convert/7059681c0b35d5fef3ffeb164b196e69.png">

五、开发总结

学习这样一个游戏辅助脚本，对于个人培养编程兴趣也是有很多帮助的，在工作之余不失为一个好的消遣方式，以后会多向这些方向研究学习。本案例仅仅是截图、比较图片和模拟鼠标点击，我觉得还可以更加强大，而且还不局限于游戏这样一个领域，相信大家应该见过自动发QQ消息的软件吧，我觉得这完全可以做。还有很多模拟操作可以实现：鼠标滚轮，左右键、键盘输入等。

六、附件-源码

注意：源码仅供学习，转发注明出处，谢谢！

```
1 # -*- coding:utf-8 -*-
 2
 3 import win32gui
 4 import time
 5 from PIL import ImageGrab, Image
 6 import numpy as np
 7 import operator
 8 from pymouse import PyMouse
 9
 10
 11 class GameAssist:
 12
 13 def __init__(self, wdname):
 14 """初始化"""
 15
 16 # 取得窗口句柄
 17 self.hwnd = win32gui.FindWindow(0, wdname)
 18 if not self.hwnd:
 19 print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname )
 20 exit()
 21
 22 # 窗口显示最前面
 23 win32gui.SetForegroundWindow(self.hwnd)
 24
 25 # 小图标编号矩阵
 26 self.im2num_arr = []
 27
 28 # 主截图的左上角坐标和右下角坐标
 29 self.scree_left_and_right_point = (299, 251, 768, 564)
 30 # 小图标宽高
 31 self.im_width = 39
 32
 33 # PyMouse对象，鼠标点击
 34 self.mouse = PyMouse()
 35
 36 def screenshot(self):
 37 """屏幕截图"""
 38
 39 # 1、用grab函数截图，参数为左上角和右下角左标
 40 # image = ImageGrab.grab((417, 257, 885, 569))
 41 image = ImageGrab.grab(self.scree_left_and_right_point)
 42
 43 # 2、分切小图
 44 # exit()
 45 image_list = {}
 46 offset = self.im_width # 39
 47
 48 # 8行12列
 49 for x in range(8):
 50 image_list[x] = {}
 51 for y in range(12):
 52 # print("show",x, y)
 53 # exit()
 54 top = x * offset
 55 left = y * offset
 56 right = (y + 1) * offset
 57 bottom = (x + 1) * offset
 58
 59 # 用crop函数切割成小图标，参数为图标的左上角和右下角左边
 60 im = image.crop((left, top, right, bottom))
 61 # 将切割好的图标存入对应的位置
 62 image_list[x][y] = im
 63
 64 return image_list
 65
 66 def image2num(self, image_list):
 67 """将图标矩阵转换成数字矩阵"""
 68
 69 # 1、创建全零矩阵和空的一维数组
 70 arr = np.zeros((10, 14), dtype=np.int32) # 以数字代替图片
 71 image_type_list = []
 72
 73 # 2、识别出不同的图片，将图片矩阵转换成数字矩阵
 74 for i in range(len(image_list)):
 75 for j in range(len(image_list[0])):
 76 im = image_list[i][j]
 77
 78 # 验证当前图标是否已存入
 79 index = self.getIndex(im, image_type_list)
 80
 81 # 不存在image_type_list
 82 if index &lt; 0:
 83 image_type_list.append(im)
 84 arr[i + 1][j + 1] = len(image_type_list)
 85 else:
 86 arr[i + 1][j + 1] = index + 1
 87
 88 print("图标数：", len(image_type_list))
 89
 90 self.im2num_arr = arr
 91 return arr
 92
 93 # 检查数组中是否有图标,如果有则返回索引下表
 94 def getIndex(self,im, im_list):
 95 for i in range(len(im_list)):
 96 if self.isMatch(im, im_list[i]):
 97 return i
 98
 99 return -1
100
101 # 汉明距离判断两个图标是否一样
102 def isMatch(self, im1, im2):
103
104 # 缩小图标，转成灰度
105 image1 = im1.resize((20, 20), Image.ANTIALIAS).convert("L")
106 image2 = im2.resize((20, 20), Image.ANTIALIAS).convert("L")
107
108 # 将灰度图标转成01串,即系二进制数据
109 pixels1 = list(image1.getdata())
110 pixels2 = list(image2.getdata())
111
112 avg1 = sum(pixels1) / len(pixels1)
113 avg2 = sum(pixels2) / len(pixels2)
114 hash1 = "".join(map(lambda p: "1" if p &gt; avg1 else "0", pixels1))
115 hash2 = "".join(map(lambda p: "1" if p &gt; avg2 else "0", pixels2))
116
117 # 统计两个01串不同数字的个数
118 match = sum(map(operator.ne, hash1, hash2))
119
120 # 阀值设为10
121 return match &lt; 10
122
123 # 判断矩阵是否全为0
124 def isAllZero(self, arr):
125 for i in range(1, 9):
126 for j in range(1, 13):
127 if arr[i][j] != 0:
128 return False
129 return True
130
131 # 是否为同行或同列且可连
132 def isReachable(self, x1, y1, x2, y2):
133 # 1、先判断值是否相同
134 if self.im2num_arr[x1][y1] != self.im2num_arr[x2][y2]:
135 return False
136
137 # 1、分别获取两个坐标同行或同列可连的坐标数组
138 list1 = self.getDirectConnectList(x1, y1)
139 list2 = self.getDirectConnectList(x2, y2)
140 # print(x1, y1, list1)
141 # print(x2, y2, list2)
142
143 # exit()
144
145 # 2、比较坐标数组中是否可连
146 for x1, y1 in list1:
147 for x2, y2 in list2:
148 if self.isDirectConnect(x1, y1, x2, y2):
149 return True
150 return False
151
152 # 获取同行或同列可连的坐标数组
153 def getDirectConnectList(self, x, y):
154
155 plist = []
156 for px in range(0, 10):
157 for py in range(0, 14):
158 # 获取同行或同列且为0的坐标
159 if self.im2num_arr[px][py] == 0 and self.isDirectConnect(x, y, px, py):
160 plist.append([px, py])
161
162 return plist
163
164 # 是否为同行或同列且可连
165 def isDirectConnect(self, x1, y1, x2, y2):
166 # 1、位置完全相同
167 if x1 == x2 and y1 == y2:
168 return False
169
170 # 2、行列都不同的
171 if x1 != x2 and y1 != y2:
172 return False
173
174 # 3、同行
175 if x1 == x2 and self.isRowConnect(x1, y1, y2):
176 return True
177
178 # 4、同列
179 if y1 == y2 and self.isColConnect(y1, x1, x2):
180 return True
181
182 return False
183
184 # 判断同行是否可连
185 def isRowConnect(self, x, y1, y2):
186 minY = min(y1, y2)
187 maxY = max(y1, y2)
188
189 # 相邻直接可连
190 if maxY - minY == 1:
191 return True
192
193 # 判断两个坐标之间是否全为0
194 for y0 in range(minY + 1, maxY):
195 if self.im2num_arr[x][y0] != 0:
196 return False
197 return True
198
199 # 判断同列是否可连
200 def isColConnect(self, y, x1, x2):
201 minX = min(x1, x2)
202 maxX = max(x1, x2)
203
204 # 相邻直接可连
205 if maxX - minX == 1:
206 return True
207
208 # 判断两个坐标之间是否全为0
209 for x0 in range(minX + 1, maxX):
210 if self.im2num_arr[x0][y] != 0:
211 return False
212 return True
213
214 # 点击事件并设置数组为0
215 def clickAndSetZero(self, x1, y1, x2, y2):
216 # print("click", x1, y1, x2, y2)
217
218 # (299, 251, 768, 564)
219 # 原理：左上角图标中点 + 偏移量
220 p1_x = int(self.scree_left_and_right_point[0] + (y1 - 1)*self.im_width + (self.im_width / 2))
221 p1_y = int(self.scree_left_and_right_point[1] + (x1 - 1)*self.im_width + (self.im_width / 2))
222
223 p2_x = int(self.scree_left_and_right_point[0] + (y2 - 1)*self.im_width + (self.im_width / 2))
224 p2_y = int(self.scree_left_and_right_point[1] + (x2 - 1)*self.im_width + (self.im_width / 2))
225
226 time.sleep(0.2)
227 self.mouse.click(p1_x, p1_y)
228 time.sleep(0.2)
229 self.mouse.click(p2_x, p2_y)
230
231 # 设置矩阵值为0
232 self.im2num_arr[x1][y1] = 0
233 self.im2num_arr[x2][y2] = 0
234
235 print("消除：(%d, %d) (%d, %d)" % (x1, y1, x2, y2))
236 # exit()
237
238 # 程序入口、控制中心
239 def start(self):
240
241 # 1、先截取游戏区域大图，然后分切每个小图
242 image_list = self.screenshot()
243
244 # 2、识别小图标，收集编号
245 self.image2num(image_list)
246
247 print(self.im2num_arr)
248
249 # 3、遍历查找可以相连的坐标
250 while not self.isAllZero(self.im2num_arr):
251 for x1 in range(1, 9):
252 for y1 in range(1, 13):
253 if self.im2num_arr[x1][y1] == 0:
254 continue
255
256 for x2 in range(1, 9):
257 for y2 in range(1, 13):
258 # 跳过为0 或者同一个
259 if self.im2num_arr[x2][y2] == 0 or (x1 == x2 and y1 == y2):
260 continue
261 if self.isReachable(x1, y1, x2, y2):
262 self.clickAndSetZero(x1, y1, x2, y2)
263
264
265 if __name__ == "__main__":
266 # wdname 为连连看窗口的名称，必须写完整
267 wdname = u'宠物连连看经典版2,宠物连连看经典版2小游戏,4399小游戏 www.4399.com - Google Chrome'
268
269 demo = GameAssist(wdname)
270 demo.start()
GameAssist.py
```

<img src="https://img-blog.csdnimg.cn/img_convert/115a732fc46e67e2e108921c9a87aa5d.png">

**长按识别上方二维码**加我个人微信，

备注**666**免费领取电子书
