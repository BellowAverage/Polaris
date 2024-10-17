
--- 
title:  道路车辆检测_红色车辆检测_matlab实现 
tags: []
categories: [] 

---
**目标：** 实现跨摄像头的车辆追踪。 **方法：** 1、运动目标检测 2、颜色识别： 采用简单的提取颜色分量的方式，检测到基础颜色（R、G、B），这三种颜色的车辆，与我们预先给定的车辆截图相对比，进而可以得到当前运动车辆是否为同色车辆。

代码还不完善，这里提供改善思路： 1、可以通过框选车辆的长宽比的不同来判断其是小汽车、公交车、摩托车等。 2、可以进一步提取轮廓信息和车牌信息进行比对。

代码备注的很详细

```
%fileName='D:\workspace\Matlab workspace\数字图像处理\char2\char2_test\jmucorridor.avi';
fileName='D:\workspace\Matlab workspace\数字图像处理\char2\char2_test\Sample4.mp4';
obj=VideoReader(fileName);
numFrames=obj.NumberOfFrames;
f=read(obj,300);
a=0.01;
for i=10:300
   frame=read(obj,i);
   b=frame;
   b=(1-a)*b+a*f;
    o=frame-f;
    ogray=f-b;
%     
%         
    %%
img = ogray;  
% get binary image  
gray_img = rgb2gray(img);  
T = graythresh(gray_img);  
bw_img = im2bw(gray_img, T);  

bw_img=medfilt2(bw_img,[9,9]);  

% find the largest connected region  
img_reg = regionprops(bw_img,  'area', 'boundingbox');  
areas = [img_reg.Area];  
rects = cat(1,  img_reg.BoundingBox);  

% show all the largest connected region  
figure(1),  
imshow(frame);
for i = 1:size(rects, 1)  
    if( rects(i,3)&gt;20||rects(i,4)&gt;20)
    rectangle('position', rects(i, ：), 'EdgeColor', 'r');   %此处冒号用了中文字符，运行时要改成英文的
    end
end  

%%
% g=o;
% dd1=(g(:,:,1)&lt;=255&amp;g(:,:,1)&gt;=240&amp;g(:,:,2)&lt;=230&amp;g(:,:,2)&gt;=205&amp;g(:,:,3)&lt;=45&amp;g(:,:,3)&gt;=30);
% %由RGB颜色范围抠图 结果为逻辑矩阵（只包含0与1）
% [m,n]=size(dd1);
% z=zeros(m,n);
% image(cat(3,dd1,z,z))

%%
 x=imread('2.jpg');%读取彩图
[m,n,d]=size(x);
y=uint8(x);%转为uint8数据类型，计算图像像素
level=0;%设置阈值


%提取红分量，不满足阈值的变为白色
for i=1:m
    for j=1:n
        if((x(i,j,1)-x(i,j,2)&gt;level)&amp;&amp;(x(i,j,1)-x(i,j,3)&gt;level))
            y(i,j,1)=x(i,j,1);
            y(i,j,2)=x(i,j,2);
            y(i,j,3)=x(i,j,3);
        else
            b(i,j,1)=255;
            y(i,j,2)=255;
            y(i,j,3)=255;
        end
    end
end
% subplot(2,2,2);imshow(y);title('提取红分量后');%显示提取红分量后的图
sum1=sum(sum(y(:,:,1)));
%%
x1=o;
[m,n,d]=size(x1);
y1=uint8(x1);%转为uint8数据类型，计算图像像素
% imshow(y1);
level=0;%设置阈值
% figure(5);
% subplot(2,2,1);imshow(x1);title('原图');%显示原图

%提取红分量，不满足阈值的变为白色
for i=1:m
    for j=1:n
        if((x1(i,j,1)-x1(i,j,2)&gt;level)&amp;&amp;(x1(i,j,1)-x1(i,j,3)&gt;level))
            y1(i,j,1)=x1(i,j,1);
            y1(i,j,2)=x1(i,j,2);
            y1(i,j,3)=x1(i,j,3);
        else b(i,j,1)=255;
            y1(i,j,2)=255;
            y1(i,j,3)=255;
        end
    end
end

%subplot(2,2,2);imshow(y1);title('提取红分量后');%显示提取红分量后的图
sum11=sum(sum(y1(:,:,1)));
flag=0;
if(sum11&gt;0.5*sum1)
    flag=1;
end
figure(3);
if(flag==1)
    imshow(o);
    for i = 1:size(rects, 1)  
    if( rects(i,3)&gt;30||rects(i,4)&gt;30)
    rectangle('position', rects(i, ：), 'EdgeColor', 'r'); %此处冒号用了中文字符，运行时要改成英文的
    end
end  
end
end

subplot(2,2,1),imshow(f);
subplot(2,2,2),imshow(b);
subplot(2,2,3),imshow(o);

```

本文为原创。 转载请注明出处。

代码下载： 
