
--- 
title:  LODGE 学习笔记 
tags: []
categories: [] 

---
**目录**



















### 高斯喷洒预测：

noise为空，输入只有cond，6*256*35

```
    def render_sample(self, shape, cond, normalizer, epoch, render_out, fk_out=None, name=None, sound=True, mode="normal", noise=None, constraint=None, sound_folder="ood_sliced", start_point=None, render=True, genre=None, # do_normalize=False,
    ):
        if isinstance(shape, tuple):
            if mode == "inpaint":
                func_class = self.inpaint_loop
            elif mode == "inpaint_soft":
                func_class = self.inpaint_soft_loop
            elif mode == "inpaint_soft_ddim":
                func_class = self.inpaint_soft_ddim
            elif mode == "normal":
                func_class = self.ddim_sample
            elif mode == "long":
                func_class = self.long_ddim_sample
            else:
                assert False, "Unrecognized inference mode"
            samples = (func_class(shape, cond, genre, noise=noise, constraint=constraint, start_point=start_point, ).detach().cpu())
```



每隔20次预测1次，扩散50次，x是随机数输入，迭代后更新x值，网络输出就是x。

```
  for time, time_next, weight in tqdm(time_pairs, desc='sampling loop time step'):
            time_cond = torch.full((batch,), time, device=device, dtype=torch.long)
            pred_noise, x_start, *_ = self.model_predictions(x, cond, genre, time_cond, weight=weight, clip_x_start=self.clip_denoised)
```



### pytorch_lightning版本问题

安装最新的版本2.0.0以上，会有不兼容的问题

安装1.9.3和以下，也会报参数错误。

测试ok

pip install pytorch-lightning==1.9.4

```
    def loss(self, x, cond, genre_id, t_override=None, isgen=False):
        batch_size = len(x)
        if t_override is None:
            t = torch.randint(0, self.n_timestep, (batch_size,), device=x.device).long()
        else:
            t = torch.full((batch_size,), t_override, device=x.device).long()
        return self.p_losses(x, cond, genre_id, t, isgen)

    def forward(self, x, cond, genre_id=None, t_override=None, isgen=False):
        return self.loss(x, cond, genre_id, t_override, isgen)
```

### 训练加载数据



```
    def __getitem__(self, index):
        motion_index = self.motion_index[index]
        music_index = self.music_index[index]
        motion = self.motion[motion_index:motion_index+self.seq_len]
        music = self.music[music_index:music_index+self.seq_len]
        genre = self.genre_list[index]

        return motion, music, genre
```



#### SMPLX_Skeleton

```
        self.smplx_fk = SMPLX_Skeleton(Jpath='/data2/lrh/project/dance/Lodge/lodge_pub/data/smplx_neu_J_1.npy', device=cfg.DEVICE)  # debug 这里的DEVICE？


        if features.shape[2] == 315:
            trans, rot6d = torch.split(features, (3, features.shape[2] - 3), dim=2)  # 前4维是foot contact
            b, s, c = rot6d.shape
            local_q_156 = ax_from_6v(rot6d.reshape(b, s, -1, 6))
            joints = self.smplx_fk.forward(local_q_156, trans)
            joints = joints.view(b, s, 55, 3)
            return joints
```



#### motion处理

```
       for name in tqdm(self.datalist):
            name = name + ".npy"
            if name[:-4] in ignor_list:
                continue
            motion = np.load(os.path.join(self.motion_dir, name))

            if dataname == "AISTPP":
                motion = motion[::2]
            music = np.load(os.path.join(self.music_dir, name))

            min_all_len = min(motion.shape[0], music.shape[0])
            motion = motion[:min_all_len]
          
  
            if motion.shape[-1] == 319 and args.FINEDANCE.nfeats ==139:
                motion = motion[:,:139]
            elif motion.shape[-1] == 139:
                pass
            else:
                print("motion.shape", motion.shape)
```


