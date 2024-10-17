
--- 
title:  NVIDIA Jetson xavier/Linux python36 linux_aarch64系统安装tensorflow、torch、torchvision 
tags: []
categories: [] 

---
**1. 安装tensorflow** 参考网址：https://forums.developer.nvidia.com/t/official-tensorflow-for-jetson-agx-xavier

**sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran**

**sudo apt-get install python3-pip**

**sudo pip3 install -U pip**

**sudo pip3 install Cython**

**sudo pip3 install -U pip testresources setuptools numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11**

**sudo pip3 install tensorflow-1.15.2+nv20.4-cp36-cp36m-linux_aarch64.whl**  

**2.安装pytorch**

torch的安装：**sudo apt-get install libopenblas-dev**

**sudo pip3 install torch-1.7.0-cp36-cp36m-linux_aarch64.whl**

torchvision安装：

参考https://blog.csdn.net/weixin_41010198/article/details/109855435 https://blog.csdn.net/u013171226/article/details/107680337

**sudo apt-get install libjpeg-dev zlib1g-dev**

**git clone --branch v0.8.1 https://github.com/pytorch/vision torchvision**

**cd torchvision sudo python3 setup.py install**  
