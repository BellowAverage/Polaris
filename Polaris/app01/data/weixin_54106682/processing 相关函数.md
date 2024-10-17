
--- 
title:  processing 相关函数 
tags: []
categories: [] 

---
#### vertex函数

①description

所有形状都是通过连接一系列顶点来构建的。vertex（）用于指定点、线、三角形、四边形和多边形的顶点坐标。它只在beginShape（）和endShape（）函数中使用。

使用z参数在三维中绘制顶点需要将P3D参数与大小结合起来，如上例所示。

此函数还用于将纹理映射到几何体上。texture（）函数声明要应用于几何体的纹理，u和v坐标集定义了该纹理到表单的映射。默认情况下，u和v使用的坐标是根据图像的像素大小指定的，但可以使用textureMode（）更改此关系。

②example

```
// Drawing vertices in 3D requires P3D
// as a parameter to size()
size(400, 400, P3D);
//beginShape(POINTS)只绘制点
beginShape(POINTS);
//点的大小 注释掉默认为0 即画布上不显示
strokeWeight(25);
//点的坐标有三维 x,y,z
vertex(120, 80, -100);
vertex(340, 80, -200);
vertex(340, 300, -200);
vertex(120, 300, -200);
endShape();
```

运行效果如图所示

```
size(400, 400, P3D);
PImage img = loadImage("D:\\compression\\image\\1.png");
noStroke();
beginShape();
texture(img);
// "laDefense.jpg" is 700 x 700 pixels in size so
// the values 0 and 400 are used for the
// parameters "u" and "v" to map it directly
// to the vertex points
// 将load的图片的像素0,0点映射到400X400画布的40,80像素点
vertex(40, 80, 0, 0);
// 将load的图片的像素700,0点映射到400X400画布的320,20像素点
vertex(320, 20, 700, 0);
// 将load的图片的像素700,700点映射到400X400画布的380,360像素点
vertex(380, 360, 700, 700);
// 将load的图片的像素0,700点映射到400X400画布的160,380像素点
vertex(160, 380, 0, 700);
endShape();
```

运行效果:

#### textureMode()函数

①description

设置纹理贴图的坐标空间。默认模式是IMAGE，它指的是图像的实际坐标。NORMAL是指范围从0到1的值的归一化空间。此功能仅适用于P2D和P3D渲染器。

使用IMAGE，如果图像为100 x 200像素，则将图像映射到四边形的整个大小将需要点（0,0）（100，0）（100，200）（0，200）。NORMAL中的相同映射为（0,0）（1,0）（1,1）（0,1）。

```
size(400, 400, P3D);
noStroke();
PImage img = loadImage("D:\\compression\\image\\1.png");
//模式为NORMAL
textureMode(NORMAL);
beginShape();
texture(img);
vertex(40, 80, 0, 0);
vertex(320, 20, 1, 0);
vertex(380, 360, 1, 1);
vertex(160, 380, 0, 1);
endShape();
```

```
size(400, 400, P3D);
noStroke();
PImage img = loadImage("shells.jpg");
//模式为IMAGE
textureMode(IMAGE);
beginShape();
texture(img);
vertex(40, 80, 0, 0);
vertex(320, 20, 400, 0);
vertex(380, 360, 400, 400);
vertex(160, 380, 0, 400);
endShape();
```

运行效果:


