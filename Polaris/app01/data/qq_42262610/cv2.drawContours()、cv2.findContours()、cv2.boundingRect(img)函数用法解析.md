
--- 
title:  cv2.drawContours()、cv2.findContours()、cv2.boundingRect(img)函数用法解析 
tags: []
categories: [] 

---
**cv2.drawContours()函数的功能是绘制轮廓**，输入变量如下：

cv2.drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None) 第一个参数image表示目标图像， 第二个参数contours表示输入的轮廓组，每一组轮廓由点vector构成， 第三个参数contourIdx指明画第几个轮廓，如果该参数为负值，则画全部轮廓， 第四个参数color为轮廓的颜色， 第五个参数thickness为轮廓的线宽，如果为负值或CV_FILLED表示填充轮廓内部， 第六个参数lineType为线型， 第七个参数为轮廓结构信息， 第八个参数为maxLevel**一般用该函数前需要使用`cv2.fineContours()`先寻找外轮廓**，函数输入变量如下：`contours, hierarchy`

`image：参数是寻找轮廓的图像； mode：参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）： cv2.RETR_EXTERNAL：表示只检测外轮廓 cv2.RETR_LIST：检测的轮廓不建立等级关系 cv2.RETR_CCOMP：建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。 cv2.RETR_TREE：建立一个等级树结构的轮廓。 method：轮廓的近似办法： cv2.CHAIN_APPROX_NONE：存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1 cv2.CHAIN_APPROX_SIMPLE：压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息 cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS：使用teh-Chinl chain近似算法`

`返回值： contour：轮廓本身 hierarchy：每条轮廓对应的属性，其中的元素个数和轮廓个数相同，每个轮廓contours[i]对应4个hierarchy元素hierarchy[i][0] ~hierarchy[i][3]，分别表示后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号，如果没有对应项，则该值为负数。` 注意：cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的，再转成二值图。

import cv2 as cv mask1 = image.copy() mask2 = image.copy() area = [] #灰度化并直方图均衡化 equalHist = EqualHist(image) #中值滤波 src_gray = cv.blur(equalHist, (5,5)) #canny边缘检测 canny_output = cv.Canny(src_gray, 0,130) #二值化 ret, binary = cv.threshold(canny_output,0,130,cv.THRESH_BINARY | cv.THRESH_OTSU) #形态学变换 kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 矩形结构 close_img = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=2) #寻找外轮廓 contours, hierarchy = cv.findContours(close_img , cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # 找到最大的轮廓 for k in range(len(contours)):     area.append(cv.contourArea(contours[k])) max_idx = np.argmax(np.array(area)) #用于返回一个numpy数组中最大值的索引值 #最大轮廓面积计算 area_black = cv.contourArea(contours[max_idx]) # Draw contours result=cv.drawContours(mask1, contours,max_idx, (0,255,0), 3) cv.imshow("",result)**cv2.boundingRect(img)  矩形边框（Bounding Rectangle）是说，用一个最小的矩形，把找到的形状包起来。**

这个函数很简单，img是一个二值图，也就是它的参数；

返回四个值，分别是x，y，w，h；

x，y是矩阵左上点的坐标，w，h是矩阵的宽和高

然后利用**cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)**画出**矩形**

参数解释

第一个参数：img是原图

第二个参数：（x，y）是矩阵的左上点坐标

第三个参数：（x+w，y+h）是矩阵的右下点坐标

第四个参数：（0,255,0）是画线对应的rgb颜色

第五个参数：2是所画的线的宽度
