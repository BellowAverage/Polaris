
--- 
title:  OSError: /media/yons/BE81566485C8329A/Anaconda/Installation_package/enter/envs/nanmao/lib/python3.7/ 
tags: []
categories: [] 

---
安装某个包时，**报错：**

OSError: /media/yons/BE81566485C8329A/Anaconda/Installation_package/enter/envs/nanmao/lib/python3.7/site-packages/torch/lib/../../nvidia/cublas/lib/libcublas.so.11: undefined symbol: cublasLtGetStatusString, version libcublasLt.so.11

<img alt="" height="240" src="https://img-blog.csdnimg.cn/direct/1473133a1b21416ebb1ba766ae7d418c.png" width="1200">



解决方案：

在虚拟环境中找到以下文件夹：

>  
 /media/yons/BE81566485C8329A/Anaconda/Installation_package/enter/envs/nanmao/lib/python3.7/site-packages/nvidia 


将该文件夹删除即可解决该报错问题。
