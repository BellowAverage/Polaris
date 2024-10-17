
--- 
title:  【OpenGL ES】渲染管线 
tags: []
categories: [] 

---
##### 1 前言

[渲染管线]是指图形渲染流程，涉及到的概念非常多，主要包含图元、片段、光栅化、空间、变换、裁剪、着色器、片段测试、混合等。渲染管线主体流程如下：

<img src="https://img-blog.csdnimg.cn/b6ecd2a072a24b26a0f590dfaa6b2237.png" alt="">

为方便读者理解渲染管线，本文将先介绍顶点数据、图元与片段、空间与变换、等渲染管线基础概念，再介绍渲染管线、片段测试、混合等内容。

##### 2 顶点数据

模型的顶点数据主要属性有位置坐标、纹理坐标、法线向量、颜色等，OpenGL ES 接收的顶点序列是按照图元类型有序组织的，通过 glVertexAttribPointer 函数输入顶点数据，如下：

```
void glVertexAttribPointer(    int index, // 顶点属性的索引值, 如: 位置属性索引为0, 颜色属性索引为1    int size, // 每个顶点在待设置属性下的数组大小, 如: 位置用三维坐标表示, 则size为3; 颜色用rgba表示, 则size为4    int type, // 顶点属性的数据类型, 如: GLES30.GL_FLOAT    boolean normalized, // 当被访问时, 固定点数据值是否应该被归一化    int stride, // 连续顶点属性之间的偏移量, 0表示紧密排列在一起的    Buffer pointer // 顶点属性序列)

```

##### 3 图元与片段

三维空间中的物体，都由点线面构成。由于三点共面（四点不一定共面），因此组成面的最小元素是三角形，如下是 Unity3D 中的标准模型，可以看到这些模型都是由一系列三角形网格构成。

<img src="https://img-blog.csdnimg.cn/ed54e5eb17714f4d9c56a1233c9511fa.png" alt="">
- 图元：组成模型的基本元素称为图元，主要有点、线、三角形；- 片段：图元经插值，使其内部与屏幕中的像素点一一对应，映射后的像素点的集合称为片段；- 光栅化：由图元经插值得到片段的过程称为光栅化；
<img src="https://img-blog.csdnimg.cn/b8eae5fa21df465e821ae62db9d029de.png" alt="">

对于线段类型图元，输入顶点序列 abcdef，根据图元类型，组装成的线段如下：

<img src="https://img-blog.csdnimg.cn/9bd24eaa76eb48aca0fb381c84b48187.png" alt="">

对于三角形类型图元，输入顶点序列 abcdef，根据图元类型，组装成的三角形如下：

<img src="https://img-blog.csdnimg.cn/f42569fcace14005baa8f193b64a60cf.png" alt="">

图元使用详见 →。

##### 4 空间与变换

如下图，**近平面**和**远平面**间棱台称为**视锥体**，表示可见区域范围，视锥体以外的空间将被裁剪丢弃，视锥体内的模型通过透视变换投影到近平面上，近平面上得到的平面图形就是屏幕上要显示的模型的图形。

<img src="https://img-blog.csdnimg.cn/92dd8311ce774f72a3af1d7371b76a3d.png" alt="">

```
     空间及变换如下，MVP矩阵变换详见→[MVP矩阵变换](https://zhyan8.blog.csdn.net/article/details/120818853 "MVP矩阵变换")，透视变换详见→[透视变换原理](https://zhyan8.blog.csdn.net/article/details/123539785 "透视变换原理")。

```

<img src="https://img-blog.csdnimg.cn/88433417d10c4129be5731f7a6fc6f6b.png" alt="">

**1）空间**
- 模型空间：模型的出厂空间，为方便建模使用的局部空间，一般以模型的中心为原点；- 世界空间：场景空间，为方便摆放各个模型的位置及朝向而定义的全局空间，一般以场景中心为原点；- 观察空间：以相机位置为原点的世界空间；- 裁剪空间：进行透视分割，并剔除视锥体外面的顶点，根据 x, y, z 的值是否在 [-1, 1] 之间判断是否淘汰顶点；- 设备空间：近平面空间，以近平面中心为原点，值域：[-1, 1]；- 屏幕空间：以屏幕左上角为原点。
**2）变换**
- 模型变换：对模型施加的变换，主要包含平移、旋转、缩放变换；- 观察变换：对坐标轴施加的变换，坐标轴由一组基向量变换到另一组基向量上，属于相似变换+平移变换；- 投影变换：投影分为正交投影和透视投影，透视投影需要经过透视变换和透视分割两个步骤（）；- 透视分割：也叫透视除法，将 [x, y, z, w] 映射到 [x/w, y/w, z/w, 1]；- 视口变换：根据视口（Viewport）大小，将近平面上的点映射到屏幕上，属于缩放变换。
##### 5 着色器
- 顶点着色器：对顶点的位置坐标进行 ；- 片段着色器：对像素点的颜色属性进行计算，纹理贴图、光照计算、阴影计算都可以在此阶段完成。
OpenGL ES 1.x 为固定渲染管线，2.x 之后支持可编程渲染管线，使用 GLSL 语言编程，语法详见→。

##### 6 渲染管线

渲染管线是指：将模型的顶点序列、颜色系列、纹理序列、法线序列等数据输入到 OpenGL ES 中，到输出屏幕，这个阶段数据所经历的流程。渲染管线总体流程如下：

<img src="https://img-blog.csdnimg.cn/206b9a764dc24f0d8781b61b11d1279c.png" alt="">
- 裁剪：进行透视分割，并剔除视锥体外面的顶点，根据 x, y, z 的值是否在 [-1, 1] 之间判断是否淘汰顶点；- 屏幕映射：根据视口（Viewport）大小，将近平面上的点映射到屏幕上- 图元装配：根据输入顶点序列和和图元类型（mode）组装图元；- 光栅化：对图元内部进行插值，使其与屏幕中的像素一一对应；- 裁剪测试：指定一个矩形的剪裁区域，当启用剪裁测试后，只有在这个区域之内的像素才能被绘制，其它像素被丢弃；- Alpha 测试：检查片段的 Alpha 值，只有 Alpha 值满足条件的片段才会进行绘制；- 模板测试：在模板缓冲区中为每个像素保存了一个 “模板值” ，当像素需要进行模板测试时，将缓冲区中模板值与该像素的模板值进行比较，符合条件的通过测试，不符合条件的则被丢弃，不进行绘制；- 深度测试：在深度缓冲区中为每个像素保存了一个 “深度值”（顶点到相机的距离），当像素需要进行深度测试时，将缓冲区中深度值与该像素的深度值进行比较，符合条件的通过测试，并覆盖缓冲区中深度值，不符合条件的则被丢弃，不进行绘制；- 混合：在物体遮挡场景下，未开启混合时，前面的物体会遮住后面物体；开启混合后，根据物体的色光三元色和透明度进行混合。
补充：只有开启模板测试时，才会尝试修改像素的模板值，模板测试被关闭时，在像素被绘制时也不会修改像素的模板值；无论是否开启深度测试，在像素被绘制时都会修改像素的深度值。

##### 7 片段测试

片段测试包含裁剪测试、Alpha 测试、模板测试。OpenGL ES 会对每个即将绘制的像素进行以上四种测试，每个像素只有通过一项测试后才会进入下一项测试，而只有通过所有测试的像素才会被绘制，没有通过测试的像素会被丢弃掉，不进行绘制。每种测试都可以单独的开启或者关闭，如果某项测试被关闭，则认为所有像素都可以顺利通过该项测试。

**1）裁剪测试** 指定一个矩形的剪裁区域，当启用剪裁测试后，只有在这个区域之内的像素才能被绘制，其它像素被丢弃。

```
glEnable(GL_SCISSOR_TEST); // 启用剪裁测试glDisable(GL_SCISSOR_TEST); // 禁用剪裁测试glScissor(x, y, width, height); // 指定一个位置在(x, y)，宽度为width，高度为height的剪裁窗口

```

注意：OpenGL ES 窗口坐标是以左下角为 (0, 0)，右上角为 (width, height)。

视口变换也可以将像素只绘制到某一个特定的矩形区域内，但视口变换是将所有内容缩放到合适的大小后，放到一个矩形的区域内；而剪裁测试不会进行缩放，超出矩形范围的像素直接忽略掉。

**2）Alpha 测试** 检查片段的 Alpha 值，只有 Alpha 值满足条件的片段才会进行绘制。

```
glEnable(GL_ALPHA_TEST); // 启用Alpha测试glDisable(GL_ALPHA_TEST); // 禁用Alpha测试glAlphaFunc(GL_GREATER, 0.5f); // 大于0.5通过Alpha测试

```

glAlphaFunc 第一个参数取值如下：

```
GL_ALWAYS //始终通过，默认情况GL_NEVER // 始终不通过GL_GREATER // 大于设定值则通过GL_LESS // 小于设定值则通过GL_EQUAL // 等于设定值则通过GL_GEQUAL // 大于等于设定值则通过GL_LEQUAL // 小于等于设定值则通过GL_NOTEQUAL // 不等于设定值则通过

```

**3）模板测试** 在模板缓冲区中为每个像素保存了一个 “模板值” ，当像素需要进行模板测试时，将缓冲区中模板值与该像素的模板值进行比较，符合条件的通过测试，不符合条件的则被丢弃，不进行绘制。

```
glEnable(GL_STENCIL_TEST); // 启用模板测试glDisable(GL_STENCIL_TEST); // 禁用模板测试glStencilFunc(GL_LESS, 3, mask); // 小于3则通过, 第一个参数取值同Alpha测试glClear(GL_STENCIL_BUFFER_BIT); // 复位模板值glClearStencil(); // 指定复位后的模板值

```

说明：mask 表示只比较 mask 中二进制为 1 的位，例如：某个像素模板值为 5（二进制 101），mask 的二进制值为 00000011，则只需较最后两位，5 的二进制最后两位为 01，小于 3，因此会通过测试。

使用 glStencilOp 函数可以指定每个像素的 “模板值” 会根据模板测试的结果和深度测试的结果而进行改变，如下：

```
// fail: 模板测试未通过时该如何变化;// zfail: 模板测试通过，但深度测试未通过时该如何变化;// zpass: 模板测试和深度测试均通过时该如何变化;// 如果没有起用模板测试，则认为模板测试总是通过；如果没有启用深度测试，则认为深度测试总是通过glStencilOp(fail, zfail, zpass); 

```

fail、zfail、zpass 取值如下：

```
GL_KEEP // 不改变, 默认值GL_ZERO // 回零GL_REPLACE // 使用测试条件中的设定值来代替当前模板值GL_INCR // 增加1，但如果已经是最大值, 则保持不变GL_INCR_WRAP // 增加1, 但如果已经是最大值, 则从零重新开始GL_DECR // 减少1, 但如果已经是零, 则保持不变GL_DECR_WRAP // 减少1, 但如果已经是零, 则重新设置为最大值GL_INVERT // 按位取反

```

使用剪裁测试可以把绘制区域限制在一个矩形的区域内，但如果需要把绘制区域限制在一个不规则的区域内，则需要使用模板测试。如：绘制一个池塘以及周围的树木，然后绘制树木在池塘中的倒影。为了保证倒影被正确的限制在池塘水面，可以使用模板测试。具体的步骤如下：

```
glDisable(GL_STENCIL_TEST); // 禁用模板测试draw_ground_trees(); // 绘制地面和树木-------------------------------------------------------------glEnable(GL_STENCIL_TEST); // 开启模板测试glClear(GL_STENCIL_BUFFER_BIT); // 设置所有像素的模板值为0glStencilFunc(GL_ALWAYS, 1, 1); // 设置模板测试总是通过glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE); // 池塘水面的像素的模板值修改为1，而其它地方像素的模板值为0draw_pond_surface(); // 绘制池塘水面-------------------------------------------------------------glStencilFunc(GL_EQUAL, 1, 1); // 设置模板值等于1时才通过模板测试glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP); // 通过模板测试后不修改模板值draw_reflection(); // 绘制倒影

```

**4）深度测试** 在深度缓冲区中为每个像素保存了一个 “深度值”（顶点到相机的距离），当像素需要进行深度测试时，将缓冲区中深度值与该像素的深度值进行比较，符合条件的通过测试，并覆盖缓冲区中深度值，不符合条件的则被丢弃，不进行绘制。

```
glEnable(GL_DEPTH_TEST); //启用深度测试glDisable(GL_DEPTH_TEST); // 禁用深度测试glDepthMask(GL_TRUE); // 开启深度缓冲区写入glDepthMask(GL_FALSE); // 禁用深度缓冲区写入glDepthFunc(GL_LESS); // 深度小于缓冲区则通过测试, 默认值是GL_LESS, 取值同Alpha测试

```

##### 8 混合

在物体遮挡场景下，未开启混合时，前面的物体会遮住后面物体；开启混合后，根据物体的色光三元色和透明度进行混合。 读者可以在 网站查看不同混合设置的混合效果，网站页面如下：

<img src="https://img-blog.csdnimg.cn/5b8632aa5367431493be5a4f2cc7477e.png" alt="">

**1）混合函数**

```
glEnable(GL_BLEND); //启用混合效果glDisable(GL_BLEND); //禁用混合效果// 设置混合因子, srcfactor: 源混合因子, destfactor: 目标混合因子void glBlendFunc(GLenum srcfactor, GLenum destfactor);// // 设置混合因子, srcRGB: 源rgb混合因子, destRGB: 目标rgb混合因子, srcalpha: 源alpha混合因子, destalpha: 目标alpha混合因子void glBlendFuncSeparate(GLenum srcRGB, GLenum destRGB, GLenum srcalpha, GLenum destalpha);// 设置混合方程: add、subtract、reverse_subtract、min、maxvoid glBlendEquation(GLenum mode);

```

示例如下：

```
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE, GL_ZERO);glBlendEquation(GL_FUNC_ADD);glBlendEquationSeparate(GL_FUNC_ADD, GL_FUNC_ADD);

```

**2）混合因子**

```
// 源颜色为: (sR, sG, sB, sA), 目标颜色为: (dR, dG, dB, dA)GL_ZERO // (0, 0, 0, 0)GL_ONE // (1, 1, 1, 1)GL_SRC_COLOR // (sR, sG, sB, sA)GL_DST_COLOR // (dR, dG, dB, dA)GL_ONE_MINUS_SRC_COLOR // (1, 1, 1, 1) - (sR, sG, sB, sA)GL_ONE_MINUS_DST_COLOR // (1, 1, 1, 1) - (dR, dG, dB, dA)GL_SRC_ALPHA // (1, 1, 1, 1) * sAGL_DST_ALPHA // (1, 1, 1, 1) * dAGL_ONE_MINUS_SRC_ALPHA // (1, 1, 1, 1) * (1-sA)GL_ONE_MINUS_DST_ALPHA // (1, 1, 1, 1) * (1-dA)GL_SRC_ALPHA_STATURATE // (1, 1, 1, 1) * min(sA, 1-dA)

```

说明：混合因子将作为 glBlendFunc、glBlendFuncSeparate 函数的入参。

**3）混合方程**

混合方程用于确定 srcFactor * srcRGBA（结果记为 S） 与 destFactor * destRGBA（结果记为 D）之间通过什么运算确定最终的混合颜色。

```
GL_FUNC_ADD // S + DGL_FUNC_SUBTRACT // S - DGL_FUNC_REVERSE_SUBTRACT // D - SGL_MIN // min(S, D)GL_MAX // max(S, D)

```
