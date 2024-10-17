
--- 
title:  BVH2SMPL 实战笔记 
tags: []
categories: [] 

---
**目录**











BVH2SMPL-main



### 渲染npy

rendering.py

```
   self.npy_path = npy_path
        self.motions = np.load(self.npy_path)
        self.rot2xyz = Rotation2xy
```
