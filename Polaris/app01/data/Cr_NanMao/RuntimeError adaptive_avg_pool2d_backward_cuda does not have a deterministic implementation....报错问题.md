
--- 
title:  RuntimeError: adaptive_avg_pool2d_backward_cuda does not have a deterministic implementation....报错问题 
tags: []
categories: [] 

---
在训练yolov8模型，加入CA注意力机制时，运行train.py出现

>  
 RuntimeError: adaptive_avg_pool2d_backward_cuda does not have a deterministic implementation, but you set 'torch.use_deterministic_algorithms(True)'. You can turn off determinism just for this operation, or you can use the 'warn_only=True' option, if that's acceptable for your application. You can also file an issue at https://github.com/pytorch/pytorch/issues to help us prioritize adding deterministic support for this operation. 


解决方法：

定位报错位置后，在该函数前加上

```
torch.use_deterministic_algorithms(False)
```


