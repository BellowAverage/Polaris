
--- 
title:  基于Qt、C++的毕业设计课设数学绘图工具（平面图、图表、立体图绘制-附下载链接） 
tags: []
categories: [] 

---
### 基于Qt、C++的毕业设计课设数学绘图工具（平面图、图表、立体图绘制）

**介绍** 这是我的毕业设计，基于Qt Creator 4.11.1，c++语言。 效果图如下  <img src="https://img-blog.csdnimg.cn/2bf7ed569e9c478caa178df0ec02ad2e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/b0e631479a7041d48c55d5c54f8713ac.png" alt="在这里插入图片描述">

**使用说明** **1. 二维函数绘制** 开始界面： <img src="https://img-blog.csdnimg.cn/cad372a2dcc84be085a8a071609189e2.png" alt="在这里插入图片描述"> **函数设置、输入界面：**

<img src="https://img-blog.csdnimg.cn/c4f1fb6ba7d34d32b980ae8f56b592d9.png" alt="在这里插入图片描述"> **使用细节** 目前仅支持一元方程，如y=x^2,x=y+1 用户 最开始只能选择输入x或y，其他符号均无法输入 ；输入x或y后=号自动补全，删除=号会连同左边的未知数一同删除 特定位置**号会自动补全 括号的输入很重要 ！若要输入 x的二分之一次方 ，应为 y=x^(1/2) x和y轴的最大范围为[-100,100] **2. 数据图表绘制** 以柱状图为例： <img src="https://img-blog.csdnimg.cn/153821c128f447f79b67ffebedfdc232.png" alt="在这里插入图片描述"> **使用细节** 可直接在表格中进行数据输入、名字更改 该输入数据的格子中若输入非数字或未输入，则会 识别成0 使用 清空 功能，不改变表格行列数，只更改格子中的内容 饼图的孔洞大小输入限制在[0,100]， 超出范围无法输入 拟合曲线目前只能绘制多项式拟合 拟合图中， 因double类型数据只显示小数点后6位，若计算出的某系数类似于0.0000001，则会识别成0，影响拟合图像的绘制，因此需要根据实际情况改变数据比例或者拟合阶数 使用excel导入数据，名字需要自行输入，不可空缺 excel导入，只导入数据，不导入名字，并且excel中数据的摆放应于表格中各类数据的摆放一致，类似于下图（柱状图），否则无法绘制预期效果 <img src="https://img-blog.csdnimg.cn/6e6e3542d95f41c58df4c26e86112ba9.png" alt="在这里插入图片描述"> 3. 三维函数绘制 开始界面： <img src="https://img-blog.csdnimg.cn/6da3036925da47009001cfec7126623f.png" alt="在这里插入图片描述"> **使用细节** 用户输入的未知数只能为x和y，可缺少其中之一，但是不能全部缺少或者使用其他字母 未设置**号自动补全，用户需要自行注意输入 显示的坐标中y和z位置互换 **类的介绍** <img src="https://img-blog.csdnimg.cn/eeb74fb1946f4840be47cae247a10ada.png" alt="在这里插入图片描述"> **二维函数绘图结构设计** <img src="https://img-blog.csdnimg.cn/4ad19e91ccc045c5b66b6873418b69e0.png" alt="在这里插入图片描述"> **所用相关知识** <img src="https://img-blog.csdnimg.cn/5033992c7bcc4ad68f5a86cd72419633.png" alt="在这里插入图片描述"> 效果图 二维 <img src="https://img-blog.csdnimg.cn/428932ce390e44659b1025ce6c6eb390.png" alt="在这里插入图片描述"> 柱状图 <img src="https://img-blog.csdnimg.cn/e1da2388b3c843738f5dd9ae02572151.png" alt="在这里插入图片描述"> 曲线图 <img src="https://img-blog.csdnimg.cn/b666148db537446abab6f5202aa8d566.png" alt="在这里插入图片描述"> 饼图 <img src="https://img-blog.csdnimg.cn/0350aab8fcd74c829e7a4e86e7e2261a.png" alt="在这里插入图片描述"> 拟合曲线 <img src="https://img-blog.csdnimg.cn/1b171d2097a5458b8de2bb1d3995d5e4.png" alt="在这里插入图片描述"> 三维 <img src="https://img-blog.csdnimg.cn/04347ce4a01e4df2b1d1c92340c3b476.png" alt="在这里插入图片描述"> 
