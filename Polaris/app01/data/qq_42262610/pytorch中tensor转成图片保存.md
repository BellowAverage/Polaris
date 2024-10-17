
--- 
title:  pytorch中tensor转成图片保存 
tags: []
categories: [] 

---
```
image_tensor为带有devices：cuda的三维tensor

image_numpy = image_tensor[0].cpu().float().numpy()  # convert it into a numpy array
image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0  # post-processing: tranpose and scaling
image_pil = Image.fromarray(image_numpy)
image_pil.save(image_path)
```


