
--- 
title:  bvh 保存指定列 
tags: []
categories: [] 

---
**目录**







### bvh_tool.py

```
import re
import numpy as np

channelmap = {
    'Xrotation': 'x',
    'Yrotation': 'y',
    'Zrotation': 'z'
}

channelmap_inv = {
    'x': 'Xrotation',
    'y': 'Yrotation',
    'z': 'Zrotation',
}

ordermap = {
    'x': 0,
    'y': 1,
    'z': 2,
}

def load(filename:str, order:str=None) -&gt; dict:
    """Loads a BVH file.
    
    Args:
        filename (str): Path to the BVH file.
        order (str): The order of the rotation channels. (i.e."xyz")
    
    Returns:
       
```
