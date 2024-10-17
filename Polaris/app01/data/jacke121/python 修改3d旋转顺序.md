
--- 
title:  python 修改3d旋转顺序 
tags: []
categories: [] 

---
**目录**









### 旋转和角度计算

```
import numpy as np
from scipy.spatial.transform import Rotation as R

def rotate_vector(vector, axis='x',angle=90, order='zxy', new_order=
```
