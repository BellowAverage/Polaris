
--- 
title:  FineDance：细粒度编舞3D数据集 学习笔记 
tags: []
categories: [] 

---
**目录**











FineDance：细粒度编舞数据集用于 3D 全身舞蹈生成



### 关于数据集

目前，最流行的 3D 编舞数据集是 AIST++ [24]，它提供 5 小时的舞蹈，但没有手部动作。AIST++通过多视角视频进行重构。因此，由于重建误差，生成的3D舞蹈动作与真实动作之间不可避免地存在偏差

FineDance 是最大的音乐-舞蹈配对数据集，拥有最多的舞蹈流派

### 创新点

提出一个 Genre&amp;Coherent aware 检索模块。此外，我们提出了一种新的指标，称为流派匹配分数

最近的方法采用了生成网络，如VAE[37]、GAN[33]、归一化流网络[44]、扩散[42]。但他们只关注身体部位，而忽略了手部动作，导致不自然或单调的手部动作，即使用注释良好的身体和手部标签进行训练。此外，基于生成的方法受到网络长期建模能力的限制，使其难以生成长期的舞蹈序列。

因此，我们提出了FineNet，一个两阶段的生成合成网络，解决了以前舞蹈生成方法的局限性。在第一阶段，我们提出了一个基于扩散的全身舞蹈生成网络（FDGN）。FDGN的关键是设计两个专家网络，专门用于生成身体和手部动作，并使用Refine Net将它们协调组装。在第二阶段，我们提出了一个类型与连贯感知检索模块（GCRM）这确保了舞蹈片段的连贯性



长时：生成长期的新运动具有挑战性，因为神经网络往往会随着时间的推移而累积错误。为了解决这些问题，我们提出了FineNet，它包括一个基于扩散的全身多样化舞蹈生成网络（FDGN）和一个流派和连贯感知检索模块（GCRM）。FDGN专注于创造具有表现力的动作的细节舞蹈，而GCRM则考虑舞蹈的整体编排。FineNet巧妙地结合了生成和合成方法，使它们互补，就像人类编舞的过程一样。此外，FineNet允许通过在初始时间步选择不同的舞蹈片段来生成多个不同的舞蹈片段。此功能为用户提供了广泛的创意可能性。

我们方法的整体框架如图3所示。首先，将输入音乐 X 拆分为 4 秒的片段 {X}，不重叠，N 是给定音乐的片段数。对于每个 X，我们使用 Librosa 工具箱 [30] 提取时间特征 ̄X∈ R 和 mel-spectrogram 图像 eX∈ R，其中 T 是剪辑的时间长度，Cis 通道维度。W 和 H 分别是图像的宽度和高度，3 表示 RGB 通道数。FineNet在每个时间步生成并检索最佳舞蹈片段，



在 FDGN 中，我们构建了 3 个 MLP 层来编码音乐和身体特征。我们使用变压器层作为身体/手专家网络的骨干。细化网络由一维卷积层和可学习的权重参数组成。总纪元、学习率和批处理大小设置为 200、2e、2048。在 GCRM 中，α、β分别设置为 1.0 和 0.5。评估指标。（1）FID评分。Fr'echet成立



### 数据处理：

标签motion数据集，312维，转成smplx格式数据集，319维。





#### motion可视化代码

 

```
import argparse
import os
from pathlib import Path
import smplx, pickle
import torch
import sys

from pytorch3d.transforms import rotation_6d_to_matrix, matrix_to_quaternion
from tqdm import tqdm
import glob
import numpy as np

sys.path.append(os.getcwd()) 
from dataset.quaternion import ax_to_6v, ax_from_6v
from dataset.preprocess import Normalizer, vectorize_many

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


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

def motion_feats_extract(inputs_dir, outputs_dir):
    device = "cuda:0"
    print("extracting")
    raw_fps = 30
    data_fps = 30
    data_fps &lt;= raw_fps
    os.makedirs(outputs_dir,exist_ok=True)
    # All motion is retargeted to this standard model.

    motions = sorted(glob.glob(os.path.join(inputs_dir, "*.npy")))
    for motion in tqdm(motions):
        name = os.path.splitext(os.path.basename(motion))[0].split(".")[0]
        print("name is", name)
        data = np.load(motion, allow_pickle=True)
        print(data.shape)
        pos = data[:,:3]   # length, c
        q = data[:,3:]
        root_pos = torch.Tensor(pos).to(device) # T, 3
        length = root_pos.shape[0]
        local_q_rot6d = torch.Tensor(q).to(device)    # T, 312
        print("local_q_rot6d", local_q_rot6d.shape)
        local_q = local_q_rot6d.reshape(length, 52, 6).clone()

        mat = rotation_6d_to_matrix(local_q)
        quaternions=matrix_to_quaternion(mat)

        norms = torch.norm(quaternions[..., 1:], p=2, dim=-1, keepdim=True)
        half_angles = torch.atan2(norms, quaternions[..., :1])
        angles = 2 * half_angles
        eps = 1e-6
        small_angles = angles.abs() &lt; eps
        sin_half_angles_over_angles = torch.empty_like(angles)

        sin_half_angles_over_angles[~small_angles] = (torch.sin(half_angles[~small_angles]) / angles[~small_angles])

        sin_half_angles_over_angles[small_angles] = (0.5 - (angles[small_angles] * angles[small_angles]) / 48)

        # 这里返回规范化的旋转轴向量
        rotation_axis_normalized = quaternions[..., 1:] / sin_half_angles_over_angles

        # norms = torch.norm(quaternions[..., 1:], p=2, dim=-1, keepdim=True)
        # half_angles = torch.atan2(norms, quaternions[..., :1])
        # angles = 2 * half_angles
        # eps = 1e-6
        # small_angles = angles.abs() &lt; eps
        # sin_half_angles_over_angles = torch.empty_like(angles)
        # sin_half_angles_over_angles[~small_angles] = (torch.sin(half_angles[~small_angles]) / angles[~small_angles])
        # # for x small, sin(x/2) is about x/2 - (x/2)^3/6
        # # so sin(x/2)/x is about 1/2 - (x*x)/48
        # sin_half_angles_over_angles[small_angles] = (0.5 - (angles[small_angles] * angles[small_angles]) / 48)
        # local_q= quaternions[..., 1:] / sin_half_angles_over_angles


        # local_q = ax_from_6v(local_q).view(length, 156)           # T, 156

        rotation_axis_normalized=rotation_axis_normalized.cpu().numpy()*10
        def update_pose(frame, pose,lines):

            pose=rotation_axis_normalized[frame]
            # pose[:, 1] = pose[:, 1] + np.sin(frame / 10.0) * 0.02  # 左右摆动
            # 更新线段以连接关键点
            for line, (i, j) in zip(lines, connections):
                line.set_data([pose[i, 0], pose[j, 0]], [pose[i, 1], pose[j, 1]])
                line.set_3d_properties([pose[i, 2], pose[j, 2]])
            return lines

        # 创建动画
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # 设置坐标轴的显示范围
        ax.set_xlim((0, 10))
        ax.set_ylim((-6, 6))
        ax.set_zlim((-5, 20))

        # pose = np.asarray(init_poses).astype(np.float32)
        pose = rotation_axis_normalized[0]
        lines = [ax.plot([pose[s, 0], pose[e, 0]], [pose[s, 1], pose[e, 1]], [pose[s, 2], pose[e, 2]])[0] for s, e in connections]

        ani = FuncAnimation(fig, update_pose, frames=np.arange(0, rotation_axis_normalized.shape[0]), fargs=(pose,lines), interval=20)

        plt.show()

        


if __name__ == "__main__":

    in_dir=r"E:\迅雷下载\data\finedance\motion"
    out_dir=r"E:\迅雷下载\data\finedance\/motion_fea319"

    motion_feats_extract(in_dir, out_dir)
```


