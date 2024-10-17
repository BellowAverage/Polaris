
--- 
title:  numpy转为图片并保存 
tags: []
categories: [] 

---
```
from PIL import Image
bg_img1 = cv2.cvtColor(bg_img1, cv2.COLOR_BGR2RGB)
bg_img1 = Image.fromarray(np.uint8(bg_img1))
bg_img1.save('compose.jpg')
```


