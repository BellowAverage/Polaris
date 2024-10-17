
--- 
title:  bvh转smplx 
tags: []
categories: [] 

---


### 方法1：



#### 依赖项：

pip install bvh

加了没有节点的判断： 

```
import sys
import numpy as np
from bvh import Bvh
from scipy.spatial.transform import Rotation as R
import pdb
import math


# 提供的关节映射信息
JOINT_MAP = {
    # 'BVH joint name': 'SMPLX joint index'
    'Hips': 0,
    'LeftUpLeg': 1,
    'RightUpLeg': 2,
    'Spine': 3,
    'LeftLeg': 4,
    'RightLeg': 5,
    'Spine1': 6,
    'LeftFoot': 7,
    'RightFoot': 8,
    'Spine2': 9,
    'LeftForeFoot': 10,
 
```
