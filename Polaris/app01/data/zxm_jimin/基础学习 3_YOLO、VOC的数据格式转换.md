
--- 
title:  基础学习 3_YOLO、VOC的数据格式转换 
tags: []
categories: [] 

---
**主要参考：**  

## YOLO数据格式说明

<img src="https://img-blog.csdnimg.cn/ba8f9d067d6f46ce8ce017d1261e9470.png" alt="在这里插入图片描述"> yolo标注格式保存在.txt文件中，一共5个数据，用空格隔开，举例说明如下图所示：<img src="https://img-blog.csdnimg.cn/05c273b3102140bc87ef7f86dc963ac3.png" alt="在这里插入图片描述">

## 数据格式转换

假设图像的宽和高（真实宽高）分别为 w、h，bbox的左上角坐标为(x1, y2)，右下角坐标为(x2, y2)，则可求得bbox`中心坐标(x', y')`为：

```
x' = x1 + (x2 - x1)/2 = (x1 + x2)/2
y' = y1 + (y2 - y1)/2 = (y1 + y2)/2

```

设yolo的5个数据分别为：`label, x', y', w', h'`，则 `VOC——&gt;YOLO` 有对应关系：

```
x' = (x1 + x2) / 2 / w = (x1 + x2) / (2w) 
y' = (y1 + y2) / 2 / h = (y1 + y2) / (2h) 
w' = (x2 - x1) / w
h' = (y2 - y1) / h

```

`YOLO——&gt;VOC` 有对应关系：

```
x1 = w * x' - 0.5 * w * w' = w * ( x' - 0.5 * w' )
y1 = h * y' - 0.5 * h * h' = h * ( x' - 0.5 * h' )

x2 = w * x' + 0.5 * w * w'= w * ( x' + 0.5 * w' )
y2 = h * y' + 0.5* h * h' = h * ( x' + 0.5 * h' )

```

## 代码实现：

具体栗子可以移步我的另一篇博客：

### xywh2xyxy.py（VOC、YOLO格式转换）

这部分是从Yolov5官方开源的代码中 截取一部分出来的 更详细说明可以参考

```
import cv2
import numpy as np
import pandas as pd
import pkg_resources as pkg
import torch
import torchvision
import yaml


def clip_coords(boxes, shape):
    # Clip bounding xyxy bounding boxes to image shape (height, width)
    '''
    将boxes的坐标(x1y1x2y2左上角右下角)限定在图像的尺寸(img_shapehw)内，防止出界。
    这个函数会用在下面的xyxy2xywhn、save_one_boxd等函数中，很重要，必须掌握
    '''
    if isinstance(boxes, torch.Tensor):  # faster individually
        boxes[:, 0].clamp_(0, shape[1])  # x1
        boxes[:, 1].clamp_(0, shape[0])  # y1
        boxes[:, 2].clamp_(0, shape[1])  # x2
        boxes[:, 3].clamp_(0, shape[0])  # y2
    else:  # np.array (faster grouped)
        boxes[:, [0, 2]] = boxes[:, [0, 2]].clip(0, shape[1])  # x1, x2
        boxes[:, [1, 3]] = boxes[:, [1, 3]].clip(0, shape[0])  # y1, y2


def xyxy2xywh(x):
    # Convert nx4 boxes from [x1, y1, x2, y2] to [x, y, w, h] where xy1=top-left, xy2=bottom-right
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = (x[:, 0] + x[:, 2]) / 2  # x center
    y[:, 1] = (x[:, 1] + x[:, 3]) / 2  # y center
    y[:, 2] = x[:, 2] - x[:, 0]  # width
    y[:, 3] = x[:, 3] - x[:, 1]  # height
    return y


def xywh2xyxy(x):
    # Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y


def xywhn2xyxy(x, w=640, h=640, padw=0, padh=0):
    # Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y


def xyxy2xywhn(x, w=640, h=640, clip=False, eps=0.0):
    # Convert nx4 boxes from [x1, y1, x2, y2] to [x, y, w, h] normalized where xy1=top-left, xy2=bottom-right
    if clip:
        clip_coords(x, (h - eps, w - eps))  # warning: inplace clip
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = ((x[:, 0] + x[:, 2]) / 2) / w  # x center
    y[:, 1] = ((x[:, 1] + x[:, 3]) / 2) / h  # y center
    y[:, 2] = (x[:, 2] - x[:, 0]) / w  # width
    y[:, 3] = (x[:, 3] - x[:, 1]) / h  # height
    return y


def xyn2xy(x, w=640, h=640, padw=0, padh=0):
    # Convert normalized segments into pixel segments, shape (n,2)
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[:, 0] = w * x[:, 0] + padw  # top left x
    y[:, 1] = h * x[:, 1] + padh  # top left y
    return y

```
