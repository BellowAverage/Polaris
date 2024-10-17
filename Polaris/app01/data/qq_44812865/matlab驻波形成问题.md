
--- 
title:  matlab驻波形成问题 
tags: []
categories: [] 

---
### 模拟驻波形成：但是频率只能是pi的整数倍，分数倍会出现异常。

```
clear all;
xm=5;
x=0:0.01:xm;
u1=0.1*cos((2*pi)*x+pi/4);
u2=u1;
% u2=0.4*cos((pi/4)*x+(pi/6));
u=u1+u2;
figure
h=plot(x,u,'r','LineWidth',2);
axis([0,5,-0.4,0.4]) ;
grid on                                %加网格
fs=16;                                 %字体大小
% xlabel('\itx/\lambda','FontSize',fs)   %x标签
% ylabel('\itu/A','FontSize',fs)         %y标签   
% title('驻波的形成','FontSize',fs)      %标题
hold on;
h1=plot(x,u1,'b','LineWidth',2)        %右行波句柄
h2=plot(x,u2,'k','LineWidth',2)       %左行波句
% ht1=text(1,max(u1)+0.01,'\rightarrow','FontSize',fs);%显示向右的箭头
% ht2=text(1,max(u2)+0.02,'\leftarrow','FontSize',fs);%显示向右的箭头
while 1
    u1=[u1(end),u1(1:end-1)];        %倒数第二个元素移到第一个
    u2=[u2(2:end),u2(1)];              
```
