
--- 
title:  matplotlib.animation 3d姿态动画 
tags: []
categories: [] 

---
**目录**









### 演示效果：

<img alt="" height="346" src="https://img-blog.csdnimg.cn/direct/e5e349f8ff8945d2becfc112e8acd9de.png" width="373">

### 演示代码：

```
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 定义人体关键点之间的连接关系
connections = [
    (0, 1),  # 头部到颈部
    (1, 2), (2, 3), (3, 4),  # 右臂
    (1, 5), (5, 6), (6, 7),  # 左臂
    (1, 8),  # 颈部到身体中心
    (8, 9), (9, 10), (10, 11),  # 右腿
    (8, 12), (12, 13), (13, 14),  # 左腿
    (11, 15),  # 右脚到右脚尖
    (14, 16),  # 左脚到左脚尖
]


map_boneInfo = {
# 骨骼名称       父骨骼名称        子骨骼名称    序号       初始位置
"BoneRoot":   ["RootNode",     "",          0,        np.array([  0,  0,0])],
"Hip":        ["BoneRoot",     "",          1,        np.array([  0, 80,0])],
"r_hip":      ["Hip",          "r_knee",    2,        np.array([-10, 80,0])],
"r_knee":     ["r_hip",        "r_foot",    3,        np.array([-10, 40,0])],
"r_foot":     ["r_knee",       "",          4,        np.array([-10,  0,0])],
"l_hip":      ["Hip",          "l_knee",    5,        np.array([ 10, 80,0])],
"l_knee":     ["l_hip",        "l_foot",    6,        np.array([ 10, 40,0])],
"l_foot":     ["l_knee",       "",          7,        np.array([ 10,  0,0])],
"spine":      ["Hip",          "thorax",    8,        np.array([  0,110,0])],
"thorax":     ["spine",        "",          9,        np.array([  0,140,0])],
"neck":       ["thorax",       "head",     10,        np.array([  0,150,0])],
"head":       ["neck",         "",         11,        np.array([  0,160,0])],
"l_shoulder": ["thorax",       "l_elbow",  12,        np.array([ 15,140,0])],
"l_elbow":    ["l_shoulder",   "l_wrist",  13,        np.array([ 50,140,0])],
"l_wrist":    ["l_elbow",      "",         14,        np.array([ 85,140,0])],
"r_shoulder": ["thorax",       "r_elbow",  15,        np.array([-15,140,0])],
"r_elbow":    ["r_shoulder",   "r_wrist",  16,        np.array([-50,140,0])],
"r_wrist":    ["r_elbow",      "",         17,        np.array([-85,140,0])],
}

init_poses=[]

map_initTRS = {}
map_initTRS["BoneRoot"] = np.array([[0,0,0],[0,0,0],[1,1,1]],dtype=float)
for index,i in enumerate(map_boneInfo.keys()):
    if i == "BoneRoot":
        continue
    trans = - map_boneInfo[i][3] + map_boneInfo[map_boneInfo[i][0]][3]

    init_poses.append(map_boneInfo[i][3]/60.0)
    rotate = [0,0,0]
    scale = [1,1,1]
    map_initTRS[i] = np.array([trans, rotate, scale], dtype=float)


# 更新姿态以模拟行走动作
def update_pose(frame, pose, lines):
    # 在x轴上前进，并在y轴上轻微左右摆动以模拟行走的平衡动作
    pose[:, 0] += 0.01  # 向前移动
    pose[:, 1] =pose[:, 1]+ np.sin(frame / 10.0) * 0.02  # 左右摆动
    # 更新线段以连接关键点
    for line, (i, j) in zip(lines, connections):
        line.set_data([pose[i, 0], pose[j, 0]], [pose[i, 1], pose[j, 1]])
        line.set_3d_properties([pose[i, 2], pose[j, 2]])
    return lines

# 创建动画
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 设置坐标轴的显示范围
ax.set_xlim((0, 5))
ax.set_ylim((-1, 1))
ax.set_zlim((0, 3))

def init_pose():
    pose = np.zeros((17, 3))  # 17个关键点，每个有x, y, z坐标

    # 设置头部和颈部位置
    pose[0, 2], pose[1, 2] = 1.8, 1.6  # z轴上的高度

    # 设置右臂位置（水平伸展）
    pose[2, :] = [0, -0.3, 1.5]  # 右肩
    pose[3, :] = [0, -0.7, 1.5]  # 右肘
    pose[4, :] = [0, -1.0, 1.5]  # 右手

    # 设置左臂位置（水平伸展）
    pose[5, :] = [0, 0.3, 1.5]  # 左肩
    pose[6, :] = [0, 0.7, 1.5]  # 左肘
    pose[7, :] = [0, 1.0, 1.5]  # 左手

    # 设置躯干中心位置
    pose[8, 2] = 1.2  # z轴上的高度

    # 设置腿部位置（站立）
    pose[9, :] = [0, -0.2, 1.0]  # 右髋
    pose[10, :] = [0, -0.2, 0.2]  # 右膝
    pose[11, :] = [0, -0.2, -0.5]  # 右脚

    pose[12, :] = [0, 0.2, 1.0]  # 左髋
    pose[13, :] = [0, 0.2, 0.2]  # 左膝
    pose[14, :] = [0, 0.2, -0.5]  # 左脚

    # 脚尖位置（在T姿势中通常不需要特别调整）
    pose[15, :] = [0, -0.2, -1]  # 右脚尖
    pose[16, :] = [0, 0.2, -1]  # 左脚尖

    return pose

# pose = np.asarray(init_poses).astype(np.float32)
pose = init_pose()
lines = [ax.plot([pose[s, 0], pose[e, 0]], [pose[s, 1], pose[e, 1]], [pose[s, 2], pose[e, 2]])[0] for s, e in connections]

ani = FuncAnimation(fig, update_pose, frames=np.arange(0, 200), fargs=(pose, lines), interval=50)

plt.show()
```

### 保存为gif

```
ani.save('1111.gif', writer='pillow', fps=60)

writergif = animation.PillowWriter(fps=30)
ani.save('2222.gif', writer = writergif)
plt.show()
```


