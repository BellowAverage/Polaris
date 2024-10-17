
--- 
title:  torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL. 
tags: []
categories: [] 

---


pytorch 单机多卡训练报错



 torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1207, internal error, NCCL version 2.14.3 ncclInternalError: Internal check failed.



原因还未知



查看nccl是否可用

```
import torch
print(torch.distributed.is_nccl_available())
```


