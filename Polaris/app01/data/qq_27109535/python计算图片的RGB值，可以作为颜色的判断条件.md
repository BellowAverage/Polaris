
--- 
title:  python计算图片的RGB值，可以作为颜色的判断条件 
tags: []
categories: [] 

---
python计算图片的RGB值，可以作为颜色的判断条件

```

import colorsys
import PIL.Image as Image
 
def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count,(r,g,b) in image.getcolors(image.size[0]*image.size[1]):
    # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)[1]
        y = min(abs(r*2104+g*4130+b*802+4096+131072)&gt;&gt;13,235)
        y = (y-16.0)/(235-16)

        #忽略高亮色
        if y &gt; 0.9:
            continue
        score = (saturation+0.1)*count
        if score &gt; max_score:
            max_score = score
            dominant_color = (r,g,b)
    return dominant_color
 

if __name__ == '__main__':
    image = Image.open(r"在此处放入自己的图片路径")
    image = image.convert('RGB')
    print(get_dominant_color(image))

```
