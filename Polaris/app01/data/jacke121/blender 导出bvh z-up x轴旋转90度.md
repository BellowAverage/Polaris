
--- 
title:  blender 导出bvh z-up x轴旋转90度 
tags: []
categories: [] 

---


**目录**







### blender导出bvh 轴向是 z-up，x 轴逆时针旋转了 90 度，和缩放不对的问题





博文解决了fbx格式d轴旋转90度的问题，bvh的没有解决





### bvh导出：

先绕x轴 顺时针旋转90度，再导出，还没试



import bpy

import math # 选中的对象

obj = bpy.context.active_object # 绕X轴旋转90度（π/2弧度）

obj.rotation_euler[0] += math.radians(90) 
