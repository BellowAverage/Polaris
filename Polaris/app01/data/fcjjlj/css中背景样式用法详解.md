
--- 
title:  css中背景样式用法详解 
tags: []
categories: [] 

---
### css中背景样式分别如下：

background-color： #999999； //元素du的背景色 background-image : url(“path/bgFile.gif”); //设置背景图像和指定图片所在位置 background-repeat : repeat-x | repeat-y | repeat | no-repeat; //设置重复方式 background-attachment : fixed | scroll; //设置背景图片的固定方式 background-position : X轴坐标,Y轴坐标[top,bottom,center,left,right,20px,10%]; //设置背景的左上角位置,坐标可以是以百分比或固定单位

background 可以用这个属性把前面几个综合起来进行简写, background 各个值的次序依次如下： background-color | background-image | background-repeat | background-attachment | background-position

### 例如:

.bg01{<!-- --> background-color: #FFCC66; background-image: url(“path/bgFile.gif”); background-repeat: no-repeat; background-attachment: fixed; background-position: left top;}

###### 上面可以简写为:

###### .bg01{background:#FFCC66 url(“path/bgFile.gif”) no-repeat fixed left top; }
