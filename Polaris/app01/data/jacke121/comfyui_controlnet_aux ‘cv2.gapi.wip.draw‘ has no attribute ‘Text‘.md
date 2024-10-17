
--- 
title:  comfyui_controlnet_aux ‘cv2.gapi.wip.draw‘ has no attribute ‘Text‘ 
tags: []
categories: [] 

---


comfyui_controlnet_aux 引用时报错：

import cv2

'cv2.gapi.wip.draw' has no attribute 'Text'

**目录**









### 方法1：

把comfyui_controlnet_aux改名为：

aComfyUI_Controlnet_Aux

这个库调用排名第1个库就不报错了，

### 方法2：

pip install opencv-python==4.7.0.72
