
--- 
title:  3d姿态可视化 npz格式 
tags: []
categories: [] 

---
**目录**







### 效果图

<img alt="" height="464" src="https://img-blog.csdnimg.cn/direct/bc638e331c024d8abeced5594d36e77f.png" width="467">

### 可视化代码

```
import os
import time

import numpy as np
from PyQt5 import QtOpenGL, QtWidgets, QtCore, QtGui
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import argparse

from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QPixmap, QMouseEvent, QImage, QPainter, QColor, QFont
from PyQt5.QtWidgets import QSplitter, QLabel, QWidget,
```
