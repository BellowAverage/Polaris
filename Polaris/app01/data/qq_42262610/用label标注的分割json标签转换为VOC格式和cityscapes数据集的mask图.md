
--- 
title:  用label标注的分割json标签转换为VOC格式和cityscapes数据集的mask图 
tags: []
categories: [] 

---
```
import base64
import json
import os
import os.path as osp
import numpy as np
import PIL.Image
from labelme import utils

'''
用labelme标注的分割标签json文件生成8位的mask图(使用具VOC格式数据集和cityscapes数据集)

制作自己的语义分割数据集需要注意以下几点：
1、我使用的labelme版本是3.16.7，建议使用该版本的labelme，有些版本的labelme会发生错误，
   具体错误为：Too many dimensions: 3 &gt; 2
   安装方式为命令行sudo pip install labelme==3.16.7
2、此处生成的标签图是8位彩色图，与视频中看起来的数据集格式不太一样。
   虽然看起来是彩图，但事实上只有8位，此时每个像素点的值就是这个像素点所属的种类。
   所以其实和视频中VOC数据集的格式一样。因此这样制作出来的数据集是可以正常使用的。也是正常的。
'''

if __name__ == '__main__':
    jpgs_path   = "datasets/JPEGImages"           # 图片路径
    pngs_path   = "datasets/SegmentationClass"    # mask路径
    classes     = ["_background_","cat"]          # 标签的类别（根据自己数据集的类别填写）
    
    count = os.listdir("./datasets/before/")      # 该路径存放图片及对应的json标签
    for i in rang
```
