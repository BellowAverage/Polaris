
--- 
title:  python-展示图片，鼠标点击图片选择图片，并保存结果到xlsx 
tags: []
categories: [] 

---
```
import cv2 
import numpy as np 
import os
import pandas as pd

results = []
width = 0
def ButtonDown(event, x, y , flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #如果是只需要选择是合成图更好(1)，和谐后更好(2)
        # if x &lt; width // 2 : # 点击左图
        #     results.append(1)
        # else: #点击右图
        #     results.append(2)

        #如果是选择合成图更好(1)，差不多好(2)，和谐后更好(3)
        if x &lt; width // 3:        # 点击左图左侧
            results.append(1)
        elif x &gt; (width // 3)*2:  #点击右图右侧
            results.append(2)
        else:                     #点击拼图的中间部分
            results.append(0)
dataroot = " " # 图片目录
img_file_list = " " # 图片名目录（txt）
with open(img_file_list, "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        img = cv2.imread(os.path.join(dataroot,line))
        height, width = img.shape[:2]
        resize_img = cv2.resize(img, (width//2, height//2))
        width = width // 2
        cv2.namedWindow("image")
        cv2.imshow("image", resize_img)
        cv2.setMouseCallback("image", ButtonDown)
        cv2.waitKey(0)
        dataframe = pd.DataFrame(results)
        dataframe.to_excel(" ") #保存的xlsx路径
```


