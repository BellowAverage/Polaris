
--- 
title:  FineDance pkl渲染 
tags: []
categories: [] 

---


### FineDance pkl渲染代码

如果是75，也可以渲染

给定wav路径，可以渲染mp4

```
import pickle
import numpy as np
import torch
import cv2
import os
# os.environ["PYOPENGL_PLATFORM"] = "osmesa"
from tqdm import tqdm
from smplx import SMPL, SMPLX, SMPLH
import pyrender
import trimesh
import subprocess
import pickle
from pytorch3d.transforms import (axis_angle_to_matrix, matrix_to_axis_angle,
                                  matrix_to_quaternion, matrix_to_rotation_6d,
                                  quaternion_to_matrix, rotation_6d_to_matrix)

import sys
sys.path.append('.')
import argparse


def quat_to_6v(q):
    assert q.shape[-1] == 4
    mat = quaternion_to_matrix(q)
    mat = matrix_to_rotation_6d(mat)
    return mat


def quat_from_6v(q):
    assert q.shape[-1] == 6
    mat = rotation_6d_to_matrix(q)
    quat = matrix_to_quaternion(mat)
    return quat


def ax_to_6v(q)
```
