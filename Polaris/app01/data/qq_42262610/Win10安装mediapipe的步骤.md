
--- 
title:  Win10安装mediapipe的步骤 
tags: []
categories: [] 

---
我之前想自己安装mediapipe包进行人体检测的学习，但整了好几个月都不行，这次终于让我整好了，我的python版本为python = 3.7.1。

注意，不要直接用pip install mediapipe 进行安装，我之前这样安装的，mediapipe安装好了，但是所需要的opencv-contrib-python安装失败。

一、安装mediapipe
1. 首先安装opencv-contrib-python
pip install opencv-contrib-python -i ，但安装失败，

在中下载对应的版本，我下载的是opencv_contrib_python-3.4.10.35-cp37-cp37m-win_amd64.whl

然后再pycharm的控制端输入，必须把opencv_contrib_python-3.4.10.35-cp37-cp37m-win_amd64.whl放在你终端对应的路径，之后运行

pip install opencv_contrib_python-4.5.5.62-cp36-abi3-win_amd64.whl

就安装好了。
1. 安装mediapipe
pip install mediapipe

经过这两步mediapipe就安装好了

二、其他的报错

TypeError: create_bool(): incompatible function arguments. 

The following argument types are supported: 

 1. (arg0: bool) -&gt; mediapipe.python._framework_bindings.packet.Packet

那么这个问题就是你所使用的发生了变动，可能是添加了新的功能**，需要减少或者添加参数**，而我的原因就是由于mediapipe更新之后对于mediapipe.solutions.pose.Pose类的调用需要添加一个参数enable_segmentation






