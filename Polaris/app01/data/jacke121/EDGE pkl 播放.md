
--- 
title:  EDGE pkl 播放 
tags: []
categories: [] 

---
**目录**





### EDGE pkl 播放 python代码：



```

import os
import pickle
from pathlib import Path
from tempfile import TemporaryDirectory

import librosa as lr
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import torch
from matplotlib import cm
from matplotlib.colors import ListedColormap
from pytorch3d.transforms import (axis_angle_to_quaternion, quaternion_apply, quaternion_multiply)
from tqdm import tqdm

plt.rcParams['animation.ffmpeg_path'] = r'E:\迅雷下载\assets\ffmpeg-6.0-amd64-static\ffmpe
```
