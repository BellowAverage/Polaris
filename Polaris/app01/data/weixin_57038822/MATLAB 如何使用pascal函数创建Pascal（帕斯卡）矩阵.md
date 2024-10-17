
--- 
title:  MATLAB 如何使用pascal函数创建Pascal（帕斯卡）矩阵 
tags: []
categories: [] 

---
****MATLAB 如何使用pascal函数创建Pascal（帕斯卡）矩阵****

语法说明：

Y=pascal(n)：生成n阶Pascal矩阵，其元素由Pascal三角形（杨辉三角）组成，其逆矩阵的所有元素均为整数。

Y=pascal(n,1)：对n阶Pascal矩阵做Cholesky分解，取其下三角的分解形式，再按列的序号取符号，就得到了Y。

Y= pascal(n,2)：对Pascal(n,1)顺时针旋转90 度，如果n 为偶数，则矩阵中的元素取原来的相反数。

功能介绍：

生成Pascal矩阵，该矩阵为对称阵，由Pascal三角形构成。Pascal三角形是二项式展开系数构成的三角形。

eg:生成4阶Pascal矩阵，以及其Cholesky下三角分解形式。

```
d=pascal(4)　　　　% 生成4阶Pascal矩阵

```

<img src="https://img-blog.csdnimg.cn/b35817fe25b8428faa71e2a7375ae248.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_12,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">

```
t = chol(d, 'lower')　　%对Pascal矩阵做holesky分解

```

<img src="https://img-blog.csdnimg.cn/3b1ceb467f7443e2aa4ebfe0678dac28.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_11,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">

```
d11 = t .* repmat([1,-1,1,-1],4,1)

```

<img src="https://img-blog.csdnimg.cn/a44e257118244131a951a4a3065f8a3e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_14,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">

```
d12 = -rot90(d11,-1)

```

<img src="https://img-blog.csdnimg.cn/a35c990d03d043828591427fd210ca8e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_14,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">

```
d1=pascal(4,1)　　　　　% 第二种调用形式

```

<img src="https://img-blog.csdnimg.cn/096c478d350a4121878beb75ee2baee8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_16,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">

```
d2 = pascal(4,2)　　　　% 第三种调用形式

```

<img src="https://img-blog.csdnimg.cn/2b7f90d0492d4cb4831d777a1f2d3b94.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAamVmZiBvbmU=,size_18,color_FFFFFF,t_70,g_se,x_16" alt="请添加图片描述">
