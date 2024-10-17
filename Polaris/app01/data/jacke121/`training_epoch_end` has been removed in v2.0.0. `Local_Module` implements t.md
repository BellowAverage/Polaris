
--- 
title:  `training_epoch_end` has been removed in v2.0.0. `Local_Module` implements t 
tags: []
categories: [] 

---


`training_epoch_end` has been removed in v2.0.0. `Local_Module` implements t



RuntimeError: Training with multiple optimizers is only supported with manual optimization. Remove the `optimizer_idx` argument from `training_step`, set `self.automatic_optimization = False` and access your optimizers in `training_step` with `opt1, opt2, ... = self.optimizers()`.  

原因：pytorch-lightning 版本有点高了，切换低版本

测试ok

pip install pytorch-lightning==1.9.4
