
--- 
title:  利用txt索引图像路径或直接对目录下的图像进行逐一测试 
tags: []
categories: [] 

---
**1. 利用txt索引图像路径进行逐一测试**

import os

from PIL import Image

**VOCdevkit_path  = 'VOCdevkit'**

**image_ids=open(os.path.join(VOCdevkit_path,"VOC2007/ImageSSegmentation/val.txt"),'r').read().splitlines()  **

**for image_id in image_ids:**

**      image_path = os.path.join(VOCdevkit_path,"VOC2007/JPEGImages/"+image_id+".jpg")**

**      image = Image.open(image_path)       image = deeplab.get_miou_png(image)       image.save(os.path.join(pred_dir, image_id + ".png")))**

**说明：**

**VOCdevkit_path = r'E:\All directions of the project team\语义分割\deeplabv3-plus-pytorch-main\VOCdevkit'**

**image_ids  =open(os.path.join(VOCdevkit_path,"VOC2007/ImageSets/Segmentation/val.txt"),'r').read().splitlines()   # 返回一个list,没有\n**

**image_ids  =open(os.path.join(VOCdevkit_path,"VOC2007/ImageSets/Segmentation/val.txt"),'r').readlines()  # 返回一个list,有\nimage_ids  =open(os.path.join(VOCdevkit_path,"VOC2007/ImageSets/Segmentation/val.txt"),'r').readlines().strip()   # 返回一个list,没有\n**

**2. 目录下的图像进行逐一测试**

**image_ids = os.listdir(VOCdevkit_path)**

**for image_id in image_ids:**

**      image_path = os.path.join(VOCdevkit_path,"VOC2007/JPEGImages/"+image_id+".jpg")**

**      image = Image.open(image_path)       image = deeplab.get_miou_png(image)       image.save(os.path.join(pred_dir, image_id + ".png")))**
