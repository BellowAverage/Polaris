
--- 
title:  Python实现手势识别 
tags: []
categories: [] 

---
>  
  作者：露露核桃露  
  https://blog.csdn.net/qq_45874897/article/details/105516981 
 

网上搜到了一些关于手势处理的实验，我在这儿简单的实现一下，主要运用的知识就是opencv，python基本语法，图像处理基础知识。最终实现结果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9VTGliSGdYSXQzandvU2xVWm1zQTJvQ1p3Yk5EQmljdEFTaWE1emxhWG42RUxrNVVkTW42cVlFY0NnbkZYRHh1NTMyNEM0UFdsMm1pYUM0T3d4SmZWNVQxaWFBLzY0MA?x-oss-process=image/format,png">

## 获取视频（摄像头）

这部分没啥说的，就是获取摄像头。

```
cap = cv2.VideoCapture("C:/Users/lenovo/Videos/1.mp4")#读取文件
#cap = cv2.VideoCapture(0)#读取摄像头
while(True):
    ret, frame = cap.read()    key = cv2.waitKey(50) &amp; 0xFF
    if key == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()



```

## 肤色检测

这里使用的是椭圆肤色检测模型

在RGB空间里人脸的肤色受亮度影响相当大，所以肤色点很难从非肤色点中分离出来，也就是说在此空间经过处理后，肤色点是离散的点，中间嵌有很多非肤色，这为肤色区域标定(人脸标定、眼睛等)带来了难题。如果把RGB转为YCrCb空间的话，可以忽略Y(亮度)的影响，因为该空间受亮度影响很小，肤色会产生很好的类聚。这样就把三维的空间将为二维的CrCb，肤色点会形成一定得形状，如：人脸的话会看到一个人脸的区域，手臂的话会看到一条手臂的形态。

```
def A(img):


    YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) #转换至YCrCb空间
    (y,cr,cb) = cv2.split(YCrCb) #拆分出Y,Cr,Cb值
    cr1 = cv2.GaussianBlur(cr, (5,5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Ostu处理
    res = cv2.bitwise_and(img,img, mask = skin)
    return res

```

## 轮廓处理

轮廓处理的话主要用到两个函数，cv2.findContours和cv2.drawContours，这两个函数的使用使用方法很容易搜到就不说了，这部分主要的问题是提取到的轮廓有很多个，但是我们只需要手的轮廓，所以我们要用sorted函数找到最大的轮廓。

```
def B(img):


    #binaryimg = cv2.Canny(Laplacian, 50, 200) #二值化，canny检测
    h = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #寻找轮廓
    contour = h[0]
    contour = sorted(contour, key = cv2.contourArea, reverse=True)#已轮廓区域面积进行排序
    #contourmax = contour[0][:, 0, :]#保留区域面积最大的轮廓点坐标
    bg = np.ones(dst.shape, np.uint8) *255#创建白色幕布
    ret = cv2.drawContours(bg,contour[0],-1,(0,0,0),3) #绘制黑色轮廓
    return ret

```

## 全部代码

```
""" 从视频读取帧保存为图片"""
import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/lenovo/Videos/1.mp4")#读取文件
#cap = cv2.VideoCapture(0)#读取摄像头


#皮肤检测
def A(img):


    YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) #转换至YCrCb空间
    (y,cr,cb) = cv2.split(YCrCb) #拆分出Y,Cr,Cb值
    cr1 = cv2.GaussianBlur(cr, (5,5), 0)
    _, skin = cv2.threshold(cr1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Ostu处理
    res = cv2.bitwise_and(img,img, mask = skin)
    return res


def B(img):


    #binaryimg = cv2.Canny(Laplacian, 50, 200) #二值化，canny检测
    h = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #寻找轮廓
    contour = h[0]
    contour = sorted(contour, key = cv2.contourArea, reverse=True)#已轮廓区域面积进行排序
    #contourmax = contour[0][:, 0, :]#保留区域面积最大的轮廓点坐标
    bg = np.ones(dst.shape, np.uint8) *255#创建白色幕布
    ret = cv2.drawContours(bg,contour[0],-1,(0,0,0),3) #绘制黑色轮廓
    return ret




while(True):


    ret, frame = cap.read()
    #下面三行可以根据自己的电脑进行调节
    src = cv2.resize(frame,(400,350), interpolation=cv2.INTER_CUBIC)#窗口大小
    cv2.rectangle(src, (90, 60), (300, 300 ), (0, 255, 0))#框出截取位置
    roi = src[60:300 , 90:300]  # 获取手势框图


    res = A(roi)  # 进行肤色检测
    cv2.imshow("0",roi)


    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    dst = cv2.Laplacian(gray, cv2.CV_16S, ksize = 3)
    Laplacian = cv2.convertScaleAbs(dst)


    contour = B(Laplacian)#轮廓处理
    cv2.imshow("2",contour)


    key = cv2.waitKey(50) &amp; 0xFF
    if key == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

```

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">
