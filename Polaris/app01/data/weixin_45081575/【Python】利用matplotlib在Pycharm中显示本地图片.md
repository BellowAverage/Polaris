
--- 
title:  【Python】利用matplotlib在Pycharm中显示本地图片 
tags: []
categories: [] 

---
## 前言

>  
 近来在做绘图的工作，结果是会导出一张`png`图片，但苦于每次都要点击图片才能查看。为解决这一痛点，遂有此文 


## 图片显示

鄙人有一图，名为 `因果关系图.png` <img src="https://img-blog.csdnimg.cn/a5b3bbaeb0a1407eb80d5bd8b3f3ffef.png#pic_center" alt="因果关系图">

### 显示在Pycharm里面

运行以下代码后，可以看到 图片就显示在 `Pycharm` 中了 <img src="https://img-blog.csdnimg.cn/e0cf44d81b4344b1b5e68c681b8e50f1.png" alt="在这里插入图片描述">

### 显示在Pycharm上面

在 `Pycharm` 的 `Settings` 里面，取消勾选图示的 `Show plots in tool window`，

<img src="https://img-blog.csdnimg.cn/c6caf10b15a3454b87a255ff0888431e.png" alt="因果分析">

再次运行代码，如下所示。
- 图片显示在 `Pycharm` 上方，且可以对显示的图片进行修改~
<img src="https://img-blog.csdnimg.cn/2829ae40ad9f47e98f93632ed1dc950a.png" alt="因果分析">

## 代码

```
# encoding:utf-8

from PIL import Image
import matplotlib.pyplot as plt


def show_img(path: str, ) -&gt; None:
    img = Image.open(fp=path)
    plt.axis('off')  # 不显示坐标轴
    plt.imshow(img)  # 将数据显示为图像，即在二维常规光栅上。
    plt.show()  # 显示图片


if __name__ == '__main__':
    show_img(path='因果关系图.png')

```

## 后话

这样一来，即可解决了 `前言` 处的痛点，妙啊！！！ 本次分享到此结束，谁赞成？谁反对？
