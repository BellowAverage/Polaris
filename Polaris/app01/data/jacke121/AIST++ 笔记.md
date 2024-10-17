
--- 
title:  AIST++ 笔记 
tags: []
categories: [] 

---
**目录**







### 开源项目地址



有提取特征，可视化的



### pkl转空间坐标xyz 代码

```
"""Demo code for running visualizer."""
import os
import pickle

import numpy as np
from absl import app
from absl import flags
from aist_plusplus.loader import AISTDataset
from aist_plusplus.visualizer import plot_on_video
from smplx import SMPL
import torch

FLAGS = flags.FLAGS
flags.DEFINE_string('anno_dir', '/home/ruilongli/data/AIST++/', 'input local dictionary for AIST++ annotations.')
flags.DEFINE_string('video_dir', '/home/ruilongli/data/AIST/videos/10M/', 'input local dictionary for AIST Dance Videos.')
flags.DEFINE_string('smpl_dir', r'E:\assets\smpl_model/smpl', 'input local dictionary that stores SMPL data.')
flags.DEFINE_string('video_name', 'gBR_sBM_c01_d04_mBR0_ch01', 'input video name to be visualized.')
flags.DEFINE_string('save_dir', './', 'output local dictionary that stores AIST++ visualization.')
flags.DEFINE_enum('mode', 'SMPL', ['2D', '3D', 'SMPL', 'SMPLMesh'], 'visualize 3D or 2D keypoints, or SMPL joints on image plane.')


def main(_):
    # Parsing data info.
    # aist_dataset = AISTDataset(FLAGS.anno_dir)
    # video_path = os.path.join(FLAGS.video_dir, f'{FLAGS.video_name}.mp4')
    # seq_name, view = AISTDataset.get_seq_name(FLAGS.video_name)
    view_idx = 0#AISTDataset.VIEWS.index(view)
    file_path=r"E:\airuhuo_slice0.pkl"
    if FLAGS.mode == 'SMPL':  # SMPL joints

        with open(file_path, "rb") as f:
            poses = pickle.load(f)
            if "smpl_poses" in poses:
                rots = poses["smpl_poses"]  # (N, 72)
                smpl_poses = rots.reshape(-1, 24 * 3)  # (N, 24, 3)
            elif "poses" in poses:
                rots = poses["poses"]
            elif "pos" in poses:
                rots = poses["q"]  # (N, 72)
                smpl_poses = rots.reshape(-1, 24 , 3)  # (N, 24, 3)
                smpl_trans = poses['pos']  # (N, 3)
            else:
                rots = poses["pred_thetas"]  # (N, 72)
                smpl_poses = rots.reshape(-1, 22*3)  # (N, 24, 3)

        smpl_scaling = poses.get('smpl_scaling',[1])
        smpl_scaling=np.asarray(smpl_scaling)
        # smpl_trans = poses['smpl_trans']  # (N, 3)

        # smpl_poses, smpl_scaling, smpl_trans = AISTDataset.load_motion(motion_dir, seq_name)
        smpl = SMPL(model_path=FLAGS.smpl_dir, gender='MALE', batch_size=1)
        keypoints3d = smpl.forward(global_orient=torch.from_numpy(smpl_poses[:, 0:1]).float(), body_pose=torch.from_numpy(smpl_poses[:, 1:]).float(), transl=torch.from_numpy(smpl_trans).float(), scaling=torch.from_numpy(smpl_scaling.reshape(1, 1)).float(), ).joints.detach().numpy()

        vals = keypoints3d*10
        out_path="0328.npz"
        print('save frames', vals.shape[0], file_path)
        np.savez_compressed(out_path, joints_3d={"data": vals})

        nframes, njoints, _ = keypoints3d.shape
        # env_name = aist_dataset.mapping_seq2env[seq_name]
        # cgroup = AISTDataset.load_camera_group(aist_dataset.camera_dir, env_name)
        # keypoints2d = cgroup.project(keypoints3d)
        # keypoints2d = keypoints2d.reshape(9, nframes, njoints, 2)[view_idx]

    elif FLAGS.mode == 'SMPLMesh':  # SMPL Mesh
        import trimesh  # install by `pip install trimesh`
        import vedo  # install by `pip install vedo`
        smpl_poses, smpl_scaling, smpl_trans = AISTDataset.load_motion(aist_dataset.motion_dir, seq_name)
        smpl = SMPL(model_path=FLAGS.smpl_dir, gender='MALE', batch_size=1)
        vertices = smpl.forward(global_orient=torch.from_numpy(smpl_poses[:, 0:1]).float(), body_pose=torch.from_numpy(smpl_poses[:, 1:]).float(), transl=torch.from_numpy(smpl_trans).float(), scaling=torch.from_numpy(smpl_scaling.reshape(1, 1)).float(), ).vertices.detach().numpy()[0]  # first frame
        faces = smpl.faces
        mesh = trimesh.Trimesh(vertices, faces)
        mesh.visual.face_colors = [200, 200, 250, 100]

        keypoints3d = AISTDataset.load_keypoint3d(aist_dataset.keypoint3d_dir, seq_name, use_optim=True)
        pts = vedo.Points(keypoints3d[0], r=20)  # first frame

        vedo.show(mesh, pts, interactive=True)
        exit()

if __name__ == '__main__':
    app.run(main)

```


