
--- 
title:  python 三种方式实现截屏（详解+完整代码） 
tags: []
categories: [] 

---
## 一、方法一

```
import numpy as np
from PIL import ImageGrab, Image
import cv2

img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))  # bbox 定义左、上、右和下像素的4元组
print(img.size[1], img.size[0])
img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
print(img)
img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR) # 看评论区有C友说颜色相反，于是加了这一条
cv2.imwrite('screenshot1.jpg', img)
# img = Image.fromarray(img)
# img.save('screenshot1.jpg')
```

## 二、方法二

```
import win32gui
from PyQt5.QtWidgets import QApplication
import sys

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
# print(hwnd_title.items())
for h, t in hwnd_title.items():
    if t != "":
        print(h, t)

# 程序会打印窗口的hwnd和title，有了title就可以进行截图了。
hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot2.jpg")
```

## 三、方法三

```
import pyautogui
import cv2  # https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
import numpy as np
from PIL import Image

img = pyautogui.screenshot(region=[0, 0, 1920, 1080])  # x,y,w,h

# img = Image.fromarray(np.uint8(img))
# img.save('screenshot3.png')
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)  # cvtColor用于在图像中不同的色彩空间进行转换,用于后续处理。
cv2.imwrite('screenshot3.jpg', img)
```

<img alt="" height="1080" src="https://img-blog.csdnimg.cn/ff0949794d2c47ac809b5a0bf6f386f4.png" width="1200">


