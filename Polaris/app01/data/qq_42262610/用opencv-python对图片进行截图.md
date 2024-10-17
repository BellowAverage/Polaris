
--- 
title:  用opencv-python对图片进行截图 
tags: []
categories: [] 

---
方法一：

# import os # import cv2 # img_input_path = 'image/1.jpg' # filename = img_input_path.split("/")[-1].split(".")[0] # image = cv2.imread(img_input_path)

# region = image[int(520):int(1580), int(338):int(713)] # [338, 520, 713, 1580]

# cv2.imwrite('image/' + filename + '_0.jpg', region)

方法二：

from PIL import Image

x0 = max(int(x1-(x2-x1)*0.05),0)

x00= min(int(x2+(x2-x1)*0.05),w)

y0= max(int(y1-(y2-y1)*0.05),0)

y0= min(int(y1+(y2-y1)*0.05),h)



img = Image.open(img_path)

img = img.convert('RGB')

region = img.crop((x0,y0,x00,y00))

region.save(save_path+filemane+"_0.jpg", quality=95)


