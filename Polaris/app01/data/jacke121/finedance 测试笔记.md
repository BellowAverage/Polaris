
--- 
title:  finedance 测试笔记 
tags: []
categories: [] 

---
**目录**



















### 网络创新点

#### 引入了一个细粒度的舞蹈数据集

我们引入了一个细粒度的舞蹈数据集（FineDance）。它包括从 346 对歌曲和舞蹈中收集的超过 14.6 小时的数据，由专业舞者和动作捕捉系统创建，该系统具有准确的身体和手部动作





### 依赖库：

```
import glob
import os,sys
from functools import cmp_to_key
from pathlib import Path

# import jukemirlib
import numpy as np
import torch
from tqdm import tqdm

from args import FineDance_parse_test_opt
from train_seq import EDGE
from dataset.FineDance_dataset import get_train_test_list

# test_list = ["063", "132", "143", "036", "098", "198", "130", "012", "211", "193", "179", "065", "137", "161", "092", "120", "037", "109", "204", "144"]


def test(opt):
    # split = get_train_test_dict(opt.datasplit)
    train_list, test_list, ignore_list = get_train_test_list(opt.datasplit)
    for file in os.listdir(music_dir):
        if file[:3] in ignore_list:
            continue
        if not file[:3] in test_list:
            continue

        file_name = file[:-4]
        music_fea = np.load(os.path.join(music_dir, file))
        music_fea = torch.from_numpy(music_fea).cuda().unsqueeze(0)
        music_fea = music_fea.repeat(count, 1, 1)
        all_filenames = [file_name]*count

        # directory for optionally saving the dances for eval
        fk_out = None
        if opt.save_motions:
            fk_out = opt.motion_save_dir
            os.makedirs(fk_out,exist_ok=True)

        model = EDGE(opt, opt.feature_type, opt.checkpoint)
        model.eval()
        
        data_tuple = None, music_fea, all_filenames
        model.render_sample(
                data_tuple, "test", opt.render_dir, render_count=10, mode='normal', fk_out=fk_out, render=not opt.no_render
            )
        print("Done")
     

if __name__ == "__main__":
    test_list = ["063", "144"]

    data_dir=r'E:\迅雷下载/'
    music_dir = data_dir+"data/finedance/div_by_time/music_npy_120"
    count = 10

    opt = FineDance_parse_test_opt()
    test(opt)

# python test.py --save_motions

```

#### general_all.py改进

### 模型EDGE

模型原来输入长度是120，改为240后，预训练不能用了。

```
        model = SeqModel(
            nfeats=repr_dim,
            seq_len=horizon,
            latent_dim=512,
            ff_size=1024,
            num_layers=8,
            num_heads=8,
            dropout=0.1,
            cond_feature_dim=feature_dim,
            activation=F.gelu,
        )
        if opt.nfeats == 139 or opt.nfeats == 135:
            smplx_fk = SMPLSkeleton(device=self.accelerator.device)
        else:
            smplx_fk = SMPLX_Skeleton(device=self.accelerator.device, batch=512000)
        diffusion = GaussianDiffusion(
            model,
            opt,
            horizon,
            repr_dim,
            smplx_model = smplx_fk,
            schedule="cosine",
            n_timestep=1000,
            predict_epsilon=False,
            loss_type="l2",
            use_p2=False,
            cond_drop_prob=0.25,
            guidance_weight=2,
            do_normalize = opt.do_normalize
        )

        print(
            "Model has {} parameters".format(sum(y.numel() for y in model.parameters()))
        )

        self.model = self.accelerator.prepare(model)    
```



### 数据格式 smplx 学习笔记：


