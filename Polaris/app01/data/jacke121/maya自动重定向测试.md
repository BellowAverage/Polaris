
--- 
title:  maya自动重定向测试 
tags: []
categories: [] 

---
**目录**











## Pose-to-Motion: Cross-Domain Motion Retargeting with Pose Prior



### maya导入bvh





### maya python脚本测试

首先打开MAYA，然后点击软件上方，菜单栏上的窗口-&gt;常规编辑器-&gt;脚本编辑器。

在弹出的脚本编辑器的下方，选择python选项卡，然后把下面的案例代码复制粘贴进去。

测试脚本：

```
import maya.OpenMaya as om
import maya.cmds as cmds
import random, time

def arPolyNoise(geoObject, maxDisplacement):
    """Apply noise to the supplied geometry object using the supplied max displacement."""
    # get the dag path for the shapeNode using an API selection list
    selection = om.MSelectionList()
    dagPath = om.MDagPath()
    try:
        selection.add(geoObject)
        selection.getDagPath(0, dagPath)
    except: raise
    # apply noise to the shape's points
    try:        
        # initialize a geometry iterator
        geoIter = om.MItGeometry(dagPath)
        # get the positions of all the vertices in world space
        pArray = om.MPointArray()
        geoIter.allPositions(pArray)
        # displace each of the vertices
        for i in xrange(pArray.length()):
            displacement = om.MVector.one * random.random() * maxDisplacement
            pArray[i].x += displacement.x
            pArray[i].y += displacement.y
            pArray[i].z += displacement.z
        # update the surface of the geometry with the changes
        geoIter.setAllPositions(pArray)
        meshFn = om.MFnMesh(dagPath)
        meshFn.updateSurface()
    except: raise

# start the timer and add the noise
timeStart = time.clock()
# create a sphere and add noise
sphere = cmds.polySphere(radius=1, subdivisionsX=200, subdivisionsY=200)
arPolyNoise(sphere[0], 0.02)
# stop the timer
timeStop = time.clock()
print('Execution time: %s seconds.'%(timeStop-timeStart))
```



### maya python脚本调用





### maya重定向



maya导入bvh需要用插件，效果还没测

两个bvh必须 是T-Pose

是把source的动作拷贝给target

target只要t-pose就行。

关节映射。
