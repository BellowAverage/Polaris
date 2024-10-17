
--- 
title:  torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
tags: []
categories: [] 

---


torch.distributed.elastic.multiprocessing.errors.ChildFailedError:



原因：torch的cu版本与使用的CUDA版本不一致。

解决方案：因为我的CUDA是11.6，所以运行下方（需注意cu版本要低于nvidia-smi里的CUDA版本）：



```
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
```

查了一下cuda 11.8



另一种方法：



修改finetune_qlora_ds.sh，设置GPUS_PER_NODE与可使用GPU数相同

GPUS_PER_NODE=2





torch.distributedtorch.distributed…DistBackendErrorDistBackendError: : NCCL error in: …/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1275, internal error, NCCL version 2.14.3

这个不知道什么原因，然后解决方法是 增加环境变量NCCL_SOCKET_IFNAME=eth2
