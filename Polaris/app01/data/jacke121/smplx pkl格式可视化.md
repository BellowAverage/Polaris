
--- 
title:  smplx pkl格式可视化 
tags: []
categories: [] 

---


<img alt="" height="386" src="https://img-blog.csdnimg.cn/direct/3c91c9283f204f5c951562f54478b3ee.png" width="367">

### smplx pkl格式可视化

```
import glob
import os
import pickle

import torch
import numpy as np

from smplpytorch.pytorch.smpl_layer import SMPL_Layer
from display_utils import display_model, display_model_continuous

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def draw_skeleton(joints3D, kintree_table, ax=None, with_numbers=True):
    if ax is None:
        fig = plt.figure(frameon=False)
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = ax

    colors = []
    left_right_mid = ['r', 'g', 'b']
    kintree_colors = [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1]
    for c in kintree_colors:
        colors &amp;
```
