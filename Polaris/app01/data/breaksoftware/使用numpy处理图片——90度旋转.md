
--- 
title:  使用numpy处理图片——90度旋转 
tags: []
categories: [] 

---


#### 大纲
- - - <ul><li>


在一文中，我们介绍了如何将图片旋转的方法。本文将使用更简单的方法旋转图片90度。

## 左旋转90度

```
import numpy as np
import PIL.Image as Image

data = np.array(Image.open('the_starry_night.jpg'))

# left 90
rot90LeftWithOne = np.rot90(data, 1)

rot90LeftWithOneImg = Image.fromarray(rot90LeftWithOne)
rot90LeftWithOneImg.save('rot90leftone.png')

```

rot90第二个参数传递1，表示向左旋转90度1一次。

<img src="https://img-blog.csdnimg.cn/direct/187ba3fa0b8f4648bac80af9d623991d.png#pic_center" alt="在这里插入图片描述">

## 向右旋转90

向右旋转90度，可以理解成向左旋转3次90度。

```
rot90RightWithThree = np.rot90(data, 3)

rot90RightWithThreeImg = Image.fromarray(rot90RightWithThree)
rot90RightWithThreeImg.save('rot90rightthree.png')

```

或者直接给rot90传递-1，表示向右旋转90度。

```
rot90RightWithMinusOne = np.rot90(data, -1)

rot90RightWithMinusOneImg = Image.fromarray(rot90RightWithMinusOne)
rot90RightWithMinusOneImg.save('rot90rightminusone.png')

```

或者将轴转置旋转

```
rot90RightWithAOnexes = np.rot90(data, 1, axes=(1,0))

rot90RightWithAOnexesImg = Image.fromarray(rot90RightWithAOnexes)
rot90RightWithAOnexesImg.save('rot90rightaonexes.png')

```

<img src="https://img-blog.csdnimg.cn/direct/03996a56b6f440dba43236647d656efc.png#pic_center" alt="在这里插入图片描述">

### 旋转180度

向左旋转2次90度和向右旋转2次90度，都可以达到旋转180度的目的。

```
rot180WithLeftTwice = np.rot90(data, 2)

rot180WithLeftTwiceImg = Image.fromarray(rot180WithLeftTwice)
rot180WithLeftTwiceImg.save('rot180lefttwice.png')

```

```
rot180WithRightMinusTwo = np.rot90(data, -2)

rot180WithRightMinusTwoImg = Image.fromarray(rot180WithRightMinusTwo)
rot180WithRightMinusTwoImg.save('rot180rightminustwo.png')

```

<img src="https://img-blog.csdnimg.cn/direct/ac648204ee454e7ab8dbfaea6c88ac18.png#pic_center" alt="在这里插入图片描述">

## 代码地址


