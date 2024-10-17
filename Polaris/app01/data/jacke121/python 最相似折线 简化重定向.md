
--- 
title:  python 最相似折线 简化重定向 
tags: []
categories: [] 

---
**目录**





效果：

<img alt="" height="425" src="https://img-blog.csdnimg.cn/direct/0884dfd920ed40bc9f57704fe65cb007.png" width="486">



### 计算两个相似折现

```
import numpy as np
from scipy.optimize import minimize
import cv2

# 定义一个函数来计算两个骨骼之间的距离总和
def similarity(angles):
    # 重构骨骼 B
    skeleton_B = [start_point_B]
    for i, angle in enumerate(angles):
        direction = np.array([np.cos(angle), np.sin(angle), 0])
        new_joint = skeleton_B[-1] + direction * joint_lengths_B[i]
        skeleton_B.append(new_joint)
    skeleton_B = np.array(s
```
