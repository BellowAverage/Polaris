
--- 
title:  OpenCV实战系列：高通滤波器及其应用 
tags: []
categories: [] 

---
#### OpenCV实战系列：高通滤波器及其应用
<li> 
  <ul>- - <li> 
    <ul>- - - - - - 
### 0. 前言

在中，滤波器是一种放大图像某些频带同时减少其他频带的操作，低通滤波器 (`low-pass filters`) 是消除图像高频成分的滤波器，而高通滤波器 (`high-pass filters`) 消除图像的低频成分。在一节中，已经介绍了[低通滤波器]的实现以及应用，在本节中，我们介绍另一类重要的滤波器，即高通滤波器。

### 1. 检测图像边缘

在一节中，我们已经介绍了如何使用核矩阵进行线性滤波，使用低通滤波器通过去除或衰减图像高频分量来模糊图像。在本节中，我们将执行相反的变换，即放大图像的高频内容，介绍高通滤波器用于执行边缘检测。

#### 1.2 Sobel 滤波器

本节主要介绍 `Sobel` 滤波器，它也被称为定向滤波器，因为它仅影响垂直或水平图像频率，具体取决于使用的滤波器核。

**(1)** 要在水平方向应用 `Sobel` 算子，使用以下参数调用函数：

```
cv::Mat sobelX;
cv::Sobel(image,        // 输入
        sobelX,         // 输出
        CV_8U,          // 图像类型
        1, 0,           // 核
        3,              // 核大小
        0.4, 128);      // 缩放和偏移因子

```

**(2)** 垂直滤波与水平滤波类似，可以通过使用以下方式实现：

```
cv::Sobel(image, sobelY, CV_8U, 0, 1, 3, 0.4, 128);

```

生成的输出用 `8` 位图像 (`CV_8U`) 表示。水平 `Sobel` 算子操作结果如下所示：

<img src="https://img-blog.csdnimg.cn/10ff863bafa143f782dcbfec4d59033b.png#pic_center" alt="水平 Sobel">

`Sobel` 算子的核包含正值和负值，`Sobel` 滤波器的结果通常用 `16` 位有符号整数图像 (`CV_16S`) 计算，为了使结果可显示为 `8` 位图像，我们使用如下表示：使用零值对应于灰度级 `128`，负值由较暗的像素表示，而正值由较亮的像素表示。垂直 `Sobel` 算子操作结果如下所示：

<img src="https://img-blog.csdnimg.cn/532a2483447c46cb917abbf15794722f.png#pic_center" alt="请添加图片描述">

以上图像类似于照片编辑软件中的浮雕效果，实际上，浮雕图像转换通常基于方向滤镜完成。

**(3)** 然后将以上两个结果(垂直和水平 `Sobel` )进行组合，以获得 `Sobel` 滤波器的范数结果：

```
// 计算 Sobel 范数
cv::Sobel(image, sobelX, CV_16S, 1, 0);
cv::Sobel(image, sobelY, CV_16S, 0, 1);
cv::Mat sobel;
sobel = abs(sobelX) + abs(sobelY);

```

**(4)** 使用 `convertTo` 方法的缩放参数可以在图像中显示 `Sobel` 范数结果，得到的图像中使用零值表示白色像素，而较大的值用于表示灰色阴影：

```
double sobmin, sobmax;
cv::minMaxLoc(sobel, &amp;sobmin, &amp;sobmax);
// 转换为 8 位图像
cv::Mat sobelImage;
sobel.convertTo(sobelImage, CV_8U, -255./sobmax, 255)

```

<img src="https://img-blog.csdnimg.cn/d9f65b10e3364b7faada9f6d57b14ccc.png#pic_center" alt="Sobel 滤波器">

从上图中可以看出 `Sobel` 算子被称为边缘检测器的原因，对该图像进行阈值处理，可以获得图像轮廓的二值图：

```
// 对 Sobel 范数应用阈值
cv::Mat sobelThresholded;
cv::threshold(sobelImage, sobelThresholded, 225, 255, cv::THRESH_BINARY);

```

<img src="https://img-blog.csdnimg.cn/d012802de39f4140a571b4072d0c9539.png#pic_center" alt="边缘检测">

`Sobel` 算子是一个经典的边缘检测线性滤波器，它基于简单的 `3x3` 核，垂直和水平核分别具有以下结构：

[ − 1 0 1 − 2 0 2 − 1 0 1 ] [ − 1 − 2 − 1 0 0 0 1 2 1 ] \left[

−1−2−1000121−101−202−101

\begin{array}{ccc} -1 &amp; 0 &amp; 1\\ -2 &amp; 0 &amp; 2\\ -1 &amp; 0 &amp; 1\\\end{array}\right] \left[

−101−202−101−1−2−1000121

\begin{array}{ccc} -1 &amp; -2 &amp; -1\\ 0 &amp; 0 &amp; 0\\ 1 &amp; 2 &amp; 1\\\end{array}\right] ​−1−2−1​000​121​ ​ ​−101​−202​−101​ ​

如果我们将图像视为一个二维函数，那么 `Sobel` 算子就可以看作是图像在垂直和水平方向上的变化的度量。在数学中，这种度量称为梯度，定义为由函数在两个正交方向上的一阶导数构成的二维向量： g r a d ( I ) = [ ∂ I ∂ x , ∂ I ∂ y ] T grad(I)=[\frac {\partial I} {\partial x},\frac {\partial I} {\partial y}]^T grad(I)=[∂x∂I​,∂y∂I​]T 因此，`Sobel` 算子在水平和垂直方向上计算图像梯度的近似值，对目标像素周围的窗口进行操作，以减少噪声的影响。`cv::Sobel` 函数计算图像与 `Sobel` 核的卷积结果，其完整调用形式如下：

```
cv::Sobel(image,            // 输入
        sobel,              // 输出
        image_depth,        // 图像类型
        xorder, yorder,     // 指定核
        kernel_size,        // 核尺寸
        alpha, beta);       // 缩放和偏移

```

我们可以将结果写入无符号字符、有符号整数或浮点图像，如果结果落在图像像素域之外，将应用饱和运算。最后两个参数用于将结果存储在图像中之前将结果缩放(乘以) `alpha` 并添加偏移量 `beta`，在上一节生成的图像中，`Sobel` 值 `0` 由中灰度级 `128` 表示；每个 `Sobel` 掩码对应一个方向的导数，因此，使用两个参数来指定应用的内核：`x` 和 `y` 方向的导数阶数，例如，通过为 `xorder` 和 `yorder` 参数指定 `1` 和 `0` 来使用水平 `Sobel` 核，将而指定 `0` 和 `1` 则使用垂直 `Sobel` 核，我们也可以使用其他组合，但这两种是最常用的组合(二阶导数将在下一节中介绍)；最后，也可以使用其他尺寸的核，例如，值 `1`、`3`、`5` 和 `7`，大小为 `1` 的核对应于一维 `Sobel` 滤波器( `1x3` 或 `3x1`)。 由于梯度是一个二维向量，它包含一个范数和一个方向，梯度向量的范数表示梯度变化的幅度，它通常使用欧几里得范数(也称为 `L2` 范数)计算： ∣ g r a d ( I ) ∣ = ( ∂ I ∂ x ) 2 + ( ∂ I ∂ y ) 2 |grad(I)|=\sqrt {(\frac {\partial I} {\partial x})^2+(\frac {\partial I} {\partial y})^2} ∣grad(I)∣=(∂x∂I​)2+(∂y∂I​)2 ​ 然而，在图像处理中，梯度范数通常使用 `L1` 范数计算(绝对值之和)，它可以以更低的计算成本得到接近 `L2` 范数的计算结果：

```
sobel= abs(sobelX)+abs(sobelY);

```

梯度向量总是指向变化最陡峭的方向，对于图像而言，这意味着梯度方向会与边缘正交，从较暗的方向指向较亮的方向，梯度方向可以使用以下公式计算： a t a n ( g r a d ( I ) ) atan(grad(I)) atan(grad(I)) 大多数情况下，对于边缘检测，只需要计算范数。但是，如果同时需要范数和方向，可以使用以下 `OpenCV` 函数：

```
cv::Sobel(image, sobelX, CV_32F, 1, 0);
cv::Sobel(image, sobelY, CV_32F, 0, 1);
// 计算梯度的 L2 范数和方向
cv::Mat norm, dir;
cv::cartToPolar(sobelX, sobelY, norm, dir);

```

默认情况下，方向以弧度计算，需添加 `true` 作为附加参数将弧度制转换为角度值。 通过在梯度幅度上应用阈值，可以获得二值边缘图像，其关键在于设置合适的阈值。如果阈值太低，会保留太多(粗)边缘，而如果阈值太高，则会得到较多断边。例如下图是使用较高阈值得到的二值边缘图像：

<img src="https://img-blog.csdnimg.cn/3c27e4f48e51404a8bc233e93b3ee77d.png#pic_center" alt="使用较高阈值得到的二值边缘图像">

可以使用滞后阈值技术获得合适的阈值。也可以在应用微分滤波器之前应用高斯平滑滤波器，能够降低噪声影响。接下来，我们将介绍一些其他梯度算子。

#### 1.2 梯度算子

为了估计像素位置的梯度，`Prewitt` 算子使用以下矩阵核： [ − 1 0 1 − 1 0 1 − 1 0 1 ] [ − 1 − 1 − 1 0 0 0 1 1 1 ] \left[

−1−1−1000111−101−101−101

\begin{array}{ccc} -1 &amp; 0 &amp; 1\\ -1 &amp; 0 &amp; 1\\ -1 &amp; 0 &amp; 1\\\end{array}\right] \left[

−101−101−101−1−1−1000111

\begin{array}{ccc} -1 &amp; -1 &amp; -1\\ 0 &amp; 0 &amp; 0\\ 1 &amp; 1 &amp; 1\\\end{array}\right] ​−1−1−1​000​111​ ​ ​−101​−101​−101​ ​ `Roberts` 算子基于简单的 `2x2` 矩阵核： [ 1 0 0 − 1 ] [ 0 1 − 1 0 ] \left[

100−1100−1

\begin{array}{ccc} 1 &amp; 0\\ 0 &amp; -1\\\end{array}\right] \left[

0−11001−10

\begin{array}{ccc} 0 &amp; 1\\ -1 &amp; 0\\\end{array}\right] [10​0−1​][0−1​10​] 当需要更准确地估计梯度方向时，应当首选 `Scharr` 算子： [ − 3 0 3 − 10 0 10 − 3 0 3 ] [ − 3 − 10 − 3 0 0 0 1 1 1 ] \left[

−3−10−30003103−303−10010−303

\begin{array}{ccc} -3 &amp; 0 &amp; 3\\ -10 &amp; 0 &amp; 10\\ -3 &amp; 0 &amp; 3\\\end{array}\right] \left[

−301−1001−301−3−10−3000111

\begin{array}{ccc} -3 &amp; -10 &amp; -3\\ 0 &amp; 0 &amp; 0\\ 1 &amp; 1 &amp; 1\\\end{array}\right] ​−3−10−3​000​3103​ ​ ​−301​−1001​−301​ ​ 通过使用 `CV_SCHAR` 参数调用 `cv::Sobel` 函数，可以使用 `Scharr` 核：

```
cv::Sobel(image,sobelX,CV_16S,1,0, CV_SCHARR);

```

或者，可以调用 `cv::Scharr` 函数得到相同的结果：

```
cv::Scharr(image,scharrX,CV_16S,1,0,3);

```

以上这些方向滤波器都可以用于计算图像函数的一阶导数，因此，在滤波器方向存在大幅度变化的区域会得到较高值，而平坦区域得到较低值。基于此，我们通常使用高通滤波器计算图像导数。

#### 1.3 高斯导数

微分滤波器是高通滤波器，因此，它们倾向于放大图像中的噪声和具有高对比度的小细节。为了减少这些高频元素的影响，最好在应用微分滤波器之前先平滑图像，我们可以组合这两个步骤得到一个平滑核。我们已经知道图像与滤波器的卷积可以表示为项总和，根据项总和的导数等于项的导数总和这一性质，我们可以不将求导应用于平滑后的结果，而是可以首先对核求导，然后将其与图像进行卷积。由于高斯核是连续可导的，因此是一个合适的选择，使用不同的核大小调用 `cv::sobel` 函数，函数将计算具有不同 `σ` 值的高斯核导数。例如，如果我们在 `x` 方向上选择 `7x7 Sobel` 滤波器(即 `kernel_size=7`)，则可以得到以下结果：

<img src="https://img-blog.csdnimg.cn/92dd375e17b948d0b69a13ab81630188.png#pic_center" alt="7x7 滤波"> 如果将此图像与之前结果图像进行比较，可以看到许多精细的细节已被删除，更加强调重要的边缘。这可以视为一个带通滤波器，高斯滤波器去除低频部分，`Sobel` 滤波器去除高频部分。

### 2. 图像拉普拉斯算子

#### 2.1 拉普拉斯算子

拉普拉斯算子是另一种基于图像导数计算的高通线性滤波器，它通过计算二阶导数来测量图像函数的曲率。 `OpenCV` 函数 `cv::Laplacian` 用于计算图像的拉普拉斯算子，与 `cv::Sobel` 函数非常相似。它同样使用函数 `cv::getDerivKernels` 来获取其核矩阵，唯一的区别是没有导数阶参数，因为根据定义是拉普拉斯算子是二阶导数。

**(1)** 对于拉普拉斯算子，我们创建一个简单的类来封装相关操作：

```
class LaplacianZC {<!-- -->
    private:
        cv::Mat laplace;
        // 拉普拉斯核尺寸
        int aperture;
    public:
        LaplacianZC() : aperture(3) {<!-- -->}
        void setAperture(int a) {<!-- -->
            aperture = a;
        }
        int getAperture() const {<!-- -->
            return aperture;
        }
        cv::Mat computeLaplacian(const cv::Mat&amp; image) {<!-- -->
            // 计算拉普拉斯
            cv::Laplacian(image, laplace, CV_32F, aperture);
            return laplace;
        }

```

**(2)** 此处拉普拉斯算子的计算是在浮点图像上完成的。为了获得结果的图像，我们需要重新对其进行缩放，重新缩放基于拉普拉斯最大绝对值，其中为值 `0` 分配的灰度值强度为 `128`：

```
// 使用 8 位图像展示拉普拉斯结果
cv::Mat getLaplacianImage(double scale=-1.0) {<!-- -->
    if (scale&lt;0) {<!-- -->
        double lapmin, lapmax;
        cv::minMaxLoc(laplace, &amp;lapmin, &amp;lapmax);
        scale = 127/std::max(-lapmin, lapmax);
    }
    cv::Mat laplaceImage;
    laplace.convertTo(laplaceImage, CV_8U, scale, 128);
    return laplaceImage;
}

```

**(3)** 使用 `LaplacianZC` 类，使用 `7x7` 核计算拉普拉斯图像：

```
// 使用 LaplacianZC 计算拉普拉斯
LaplacianZC laplacian;
laplacian.setAperture(7);
cv::Mat flap = laplacian.computeLaplacian(image);
double lapmin, lapmax;
cv::minMaxLoc(flap, &amp;lapmin, &amp;lapmax);
laplace = laplacian.getLaplacianImage();

```

生成的图像如下图所示：

<img src="https://img-blog.csdnimg.cn/9c1cf64ccb4f4cb4b586f0c09ec3f6e3.png#pic_center" alt="拉普拉斯图像"> 形式上，二维函数的拉普拉斯算子定义为其二阶导数之和： l a p l a c i a n ( I ) = ( ∂ I ∂ x ) 2 + ( ∂ I ∂ y ) 2 laplacian(I)=\sqrt {(\frac {\partial I} {\partial x})^2+(\frac {\partial I} {\partial y})^2} laplacian(I)=(∂x∂I​)2+(∂y∂I​)2 ​ 在简单形式中，可以用以下 `3x3` 核来近似： [ 0 1 0 1 − 4 1 0 1 0 ] \left[

0101−410100101−41010

\begin{array}{ccc} 0 &amp; 1 &amp; 0\\ 1 &amp; -4 &amp; 1\\ 0 &amp; 1 &amp; 0\\\end{array}\right] ​010​1−41​010​ ​ 与 `Sobel` 算子一样，可以使用更大的核来计算拉普拉斯算子，并且由于该算子对图像噪声更加敏感，因此最好使用更大的核，除非更加追求计算效率。由于这些较大的核是使用高斯函数的二阶导数计算的，因此相应的算子通常称为高斯拉普拉斯算子 (`Laplacian of Gaussian`, `LoG`)，拉普拉斯算子的核值总和为 `0`，这确保了拉普拉斯算子在强度恒定的区域为零。实际上，由于拉普拉斯算子用于测量图像函数的曲率，因此在平坦区域它应该等于 `0`。 乍一看，拉普拉斯算子的效果可能难以解释。从核的定义来看，孤立的像素值(即与其相邻像素具有较大差异的值)都会被算子放大。这是算子对噪声高度敏感的结果；接下来，观察图像中边缘周围的拉普拉斯值，图像中边缘的存在是不同灰度强度区域之间快速过渡的结果，随着图像函数沿边缘的变化(例如，由从暗到亮的过渡引起))，可以观察到灰度提升必然意味着从正曲率逐渐过渡(当强度值开始上升时)到负曲率(当强度即将达到其顶峰时)，因此，正负拉普拉斯值之间的过渡构成了边缘存在的良好指标，或者说边缘位于拉普拉斯函数的正负值交叉处。我们通过在测试图像的一个小窗口中查看拉普拉斯算子的值来证明这一想法，选择观察图像中人物头发区域，在下图中绘制边界框以显示此感兴趣区域 (`region of interest`, `ROI`) 的确切位置：

<img src="https://img-blog.csdnimg.cn/26e101d47bbc419183ab6a76660d74b3.png#pic_center" alt="感兴趣区域">

查看此窗口内的 `Laplacian` 值( `7x7` 核)，可以得到以下结果：

<img src="https://img-blog.csdnimg.cn/e57ac5128b024d16a4d213dd2f2f5e3f.png#pic_center" alt="拉普拉斯值">

如图所示，如果连接拉普拉斯算子的正负交叉点(位于不同符号的像素之间)，可以得到一条与图像中边缘相对应的曲线。在上图中，我们沿着正负交叉点绘制虚线，这意味着，我们甚至可以以亚像素精度检测图像边缘。 连接拉普拉斯图像中的正负交叉曲线是一项复杂任务，但也可以使用简化的算法来检测近似的交叉位置：首先将拉普拉斯算子的阈值设置为 `0`，以得到正值和负值之间的分区，两个分区之间的轮廓则对应于交叉点。因此，我们使用形态学操作来提取这些轮廓，即从 `Laplacian` 图像中减去膨胀图像生成二值图像：

```
// 获取二值图像
cv::Mat getZeroCrossings(cv::Mat laplace) {<!-- -->
    // 阈值为 0
    cv::Mat signImage;
    cv::threshold(laplace, signImage, 0, 255, cv::THRESH_BINARY);
    // 将图像转换为 CV_8U 类型
    cv::Mat binary;
    signImage.convertTo(binary, CV_8U);
    // 膨胀二值图像
    cv::Mat dilated;
    cv::dilate(binary, dilated, cv::Mat());
    return dilated-binary;
}

```

程序运行结果如下所示：

<img src="https://img-blog.csdnimg.cn/e8ceaac90fb04159a992e0e213ce8145.png#pic_center" alt="拉普拉斯正负交叉点"> 可以看到，拉普拉斯算子能够检测所有边缘，无论是强边缘还是弱边缘。由于拉普拉斯算子对噪声非常敏感，因此，其中一些边缘是由于压缩伪影造成的，这解释了为什么此算子会检测到如此多的边缘。在实践中，拉普拉斯算子可以与其他算子结合使用来检测边缘，此外，拉普拉斯算子和其他二阶算子可以用于检测多尺度兴趣点。 拉普拉斯算子是一种高通滤波器，可以通过使用低通滤波器的组合得到近似结果。

#### 2.2 使用拉普拉斯算子增强图像的对比度

可以通过从图像中减去其拉普拉斯算子来增强图像的对比度，正如我们在操作像素中使用邻居访问扫描图像的方法中进行的操作，其核如下所示： [ 0 1 0 1 − 5 1 0 1 0 ] \left[

0101−510100101−51010

\begin{array}{ccc} 0 &amp; 1 &amp; 0\\ 1 &amp; -5 &amp; 1\\ 0 &amp; 1 &amp; 0\\\end{array}\right] ​010​1−51​010​ ​

#### 2.3 高斯差

高斯滤波器可以从图像中提取低频，且高斯滤波器滤波的频率范围取决于参数 `σ`，该参数控制滤波器的宽度。如果我们减去由两个不同带宽的高斯滤波器对图像进行滤波所产生的两个图像，那么生成的图像将由能保留较高频率的滤波器组成，此操作称为高斯差分 (`Difference of Gaussians`, `DoG`)：

```
cv::GaussianBlur(image, gauss20, cv::Size(), 2.0);
cv::GaussianBlur(image, gauss22, cv::Size(), 2.2);
// 计算 DoG
cv::subtract(gauss22, gauss20, dog, cv::Mat(), CV_32F);
// 显示 DoG 正负交叉点
zeros = laplacian.getZeroCrossings(dog);

```

此外，我们还可以计算 `DoG` 算子的交叉点，得到以下结果：

<img src="https://img-blog.csdnimg.cn/c855639b815845a19dc8787e7ff853ac.png#pic_center" alt="DoG">

可以证明，通过正确选择 `σ` 值，`DoG` 算子可以近似 `LoG` 滤波器的结果。此外，如果根据 `σ 值递增序列中的连续对值计算一系列高斯差分，可以获得图像的尺度空间表示，这种多尺度表示在尺度不变的图像特征检测等方面应用广泛。

### 3. 完整代码

头文件 (`laplacianZC.h`) 完整代码如下：

```
#if !defined LAPLACEZC
#define LAPLACEZ

#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;

class LaplacianZC {<!-- -->
    private:
        cv::Mat laplace;
        // 拉普拉斯核尺寸
        int aperture;
    public:
        LaplacianZC() : aperture(3) {<!-- -->}
        void setAperture(int a) {<!-- -->
            aperture = a;
        }
        int getAperture() const {<!-- -->
            return aperture;
        }
        cv::Mat computeLaplacian(const cv::Mat&amp; image) {<!-- -->
            // 计算拉普拉斯
            cv::Laplacian(image, laplace, CV_32F, aperture);
            return laplace;
        }
        // 使用 8 位图像展示拉普拉斯结果
        cv::Mat getLaplacianImage(double scale=-1.0) {<!-- -->
            if (scale&lt;0) {<!-- -->
                double lapmin, lapmax;
                cv::minMaxLoc(laplace, &amp;lapmin, &amp;lapmax);
                scale = 127/std::max(-lapmin, lapmax);
            }
            cv::Mat laplaceImage;
            laplace.convertTo(laplaceImage, CV_8U, scale, 128);
            return laplaceImage;
        }
        // 获取二值图像
        cv::Mat getZeroCrossings(cv::Mat laplace) {<!-- -->
            // 阈值为 0
            cv::Mat signImage;
            cv::threshold(laplace, signImage, 0, 255, cv::THRESH_BINARY);
            // 将图像转换为 CV_8U 类型
            cv::Mat binary;
            signImage.convertTo(binary, CV_8U);
            // 膨胀二值图像
            cv::Mat dilated;
            cv::dilate(binary, dilated, cv::Mat());
            return dilated-binary;
        }
};

#endif

```

主函数文件 (`derivatives.cpp`) 完整代码如下所示：

```
#include &lt;iostream&gt;
#include &lt;iomanip&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;
#include "laplacianZC.h"

int main() {<!-- -->
    // 读取图像
    cv::Mat image = cv::imread("3.png", 0);
    if (!image.data) return 0;
    cv::namedWindow("Original Image");
    cv::imshow("Original Image",image);
    // 计算 Sobel x 方向导数
    cv::Mat sobelX;
    cv::Sobel(image,        // 输入
            sobelX,         // 输出
            CV_8U,          // 图像类型
            1, 0,           // 核
            3,              // 核大小
            0.4, 128);      // 缩放和偏移因子
    cv::namedWindow("Sobel X Image");
    cv::imshow("Sobel X Image", sobelX);
    // 计算 Sobel y 方向导数
    cv::Mat sobelY;
    cv::Sobel(image, sobelY, CV_8U, 0, 1, 3, 0.4, 128);
    cv::namedWindow("Sobel Y Image");
    cv::imshow("Sobel Y Image",sobelY);
    // 计算 Sobel 范数
    cv::Sobel(image, sobelX, CV_16S, 1, 0);
    cv::Sobel(image, sobelY, CV_16S, 0, 1);
    cv::Mat sobel;
    sobel = abs(sobelX) + abs(sobelY);
    double sobmin, sobmax;
    cv::minMaxLoc(sobel, &amp;sobmin, &amp;sobmax);
    std::cout &lt;&lt; "sobel value range: " &lt;&lt; sobmin &lt;&lt; " " &lt;&lt; sobmax &lt;&lt; std::endl;
    // 计算 Sobel x 方向导数 (7x7)
    cv::Sobel(image, sobelX, CV_8U, 1, 0, 7, 0.001, 128);
    cv::namedWindow("Sobel X Image (7x7)");
    cv::imshow("Sobel X Image (7x7)", sobelX);
    // 打印窗口像素
    for (int i=0; i&lt;12; i++) {<!-- -->
        for (int j=0; j&lt;12; j++) {<!-- -->
            std::cout &lt;&lt; std::setw(5) &lt;&lt; 
                    static_cast&lt;int&gt;(sobel.at&lt;short&gt;(i+79, j+125)) &lt;&lt; " ";
        }
        std::cout &lt;&lt; std::endl;
    }
    std::cout &lt;&lt; std::endl &lt;&lt; std::endl &lt;&lt; std::endl;
    // 转换为 8 位图像
    cv::Mat sobelImage;
    sobel.convertTo(sobelImage, CV_8U, -255./sobmax, 255);
    cv::namedWindow("Sobel Image");
    cv::imshow("Sobel Image",sobelImage);
    // 对 Sobel 范数应用阈值
    cv::Mat sobelThresholded;
    cv::threshold(sobelImage, sobelThresholded, 225, 255, cv::THRESH_BINARY);
    cv::namedWindow("Binary Sobel Image (low)");
    cv::imshow("Binary Sobel Image (low)", sobelThresholded);
    cv::threshold(sobelImage, sobelThresholded, 190, 255, cv::THRESH_BINARY);
    cv::namedWindow("Binary Sobel Image (high)");
    cv::imshow("Binary Sobel Image (high)", sobelThresholded);
    // 计算 3x3 拉普拉斯算子
    cv::Mat laplace;
    cv::Laplacian(image, laplace, CV_8U, 1, 1, 128);
    cv::namedWindow("Laplacian Image");
    cv::imshow("Laplacian Image",laplace);
    int cx(238), cy(90);
    int dx(12), dy(12);
    // 提取较小窗口
    cv::Mat window(image, cv::Rect(cx, cy, dx, dy));
    cv::namedWindow("Image window");
    cv::imshow("Image window", window);
    cv::imwrite("window.png", window);
    // 使用 LaplacianZC 计算拉普拉斯
    LaplacianZC laplacian;
    laplacian.setAperture(7);
    cv::Mat flap = laplacian.computeLaplacian(image);
    double lapmin, lapmax;
    cv::minMaxLoc(flap, &amp;lapmin, &amp;lapmax);
    laplace = laplacian.getLaplacianImage();
    cv::namedWindow("Laplacian Image (7x7)");
    cv::imshow("Laplacian Image (7x7)", laplace);
    // 打印图像值
    std::cout &lt;&lt; std::endl;
    std::cout &lt;&lt; "Image values: " &lt;&lt; std::endl &lt;&lt; std::endl;
    for (int i=0; i&lt;dx; i++) {<!-- -->
        for (int j=0; j&lt;dy; j++) {<!-- -->
            std::cout &lt;&lt; std::setw(5) &lt;&lt;
                    static_cast&lt;int&gt;(image.at&lt;uchar&gt;(i+cy, j+cx)) &lt;&lt; " ";
        }
        std::cout &lt;&lt; std::endl;
    }
    std::cout &lt;&lt; std::endl;
    // 打印拉普拉斯值
    std::cout &lt;&lt; "Laplacian value range=[" &lt;&lt; lapmin &lt;&lt; "," &lt;&lt; lapmax &lt;&lt; "]";
    std::cout &lt;&lt; std::endl &lt;&lt; std::endl;
    for (int i=0; i&lt;dx; i++) {<!-- -->
        for (int j=0; j&lt;dy; j++) {<!-- -->
            std::cout &lt;&lt; std::setw(5) &lt;&lt; 
                    static_cast&lt;int&gt;(flap.at&lt;float&gt;(i+cy, j+cx)/100) &lt;&lt; " ";
        }
        std::cout &lt;&lt; std::endl;
    }
    std::cout &lt;&lt; std::endl;
    // 计算并显示正负交叉点
    cv::Mat zeros;
    zeros = laplacian.getZeroCrossings(flap);
    cv::namedWindow("Zero-crossings");
    cv::imshow("Zero-crossings", 255-zeros);
    // 打印窗口像素值
    std::cout &lt;&lt; "Zero values: " &lt;&lt; std::endl &lt;&lt; std::endl;
    for (int i=0; i&lt;dx; i++) {<!-- -->
        for (int j=0; j&lt;dy; j++) {<!-- -->
            std::cout &lt;&lt; std::setw(2) &lt;&lt; 
                    static_cast&lt;int&gt;(zeros.at&lt;uchar&gt;(i + cy, j + cx))/255 &lt;&lt; " ";
        }
        std::cout &lt;&lt; std::endl;
    }
    // 图像上采样和下采样
    cv::Mat reduced, rescaled;
    cv::pyrDown(image, reduced);
    cv::pyrUp(reduced, rescaled);
    cv::namedWindow("Rescaled Image");
    cv::imshow("Rescaled Image",rescaled);
    // 计算 DoG 金字塔
    cv::Mat dog;
    cv::subtract(rescaled, image, dog, cv::Mat(), CV_16S);
    cv::Mat dogImage;
    dog.convertTo(dogImage, CV_8U, 1.0, 128);
    cv::namedWindow("DoG Image (from pyrdown/pyrup)");
    cv::imshow("DoG Image (from pyrdown/pyrup)",dogImage);
    // 应用两次高斯滤波
    cv::Mat gauss05;
    cv::Mat gauss15;
    cv::GaussianBlur(image, gauss05, cv::Size(), 0.5);
    cv::GaussianBlur(image, gauss15, cv::Size(), 1.5);
    // 计算 DoG
    cv::subtract(gauss15, gauss05, dog, cv::Mat(), CV_16S);
    dog.convertTo(dogImage, CV_8U, 2.0, 128);
    cv::namedWindow("DoG Image");
    cv::imshow("DoG Image",dogImage);
    // 应用两次高斯滤波
    cv::Mat gauss20;
    cv::Mat gauss22;
    cv::GaussianBlur(image, gauss20, cv::Size(), 2.0);
    cv::GaussianBlur(image, gauss22, cv::Size(), 2.2);
    // 计算 DoG
    cv::subtract(gauss22, gauss20, dog, cv::Mat(), CV_32F);
    dog.convertTo(dogImage, CV_8U, 10.0, 128);
    cv::namedWindow("DoG Image (2)");
    cv::imshow("DoG Image (2)",dogImage);
    // 显示 DoG 正负交叉点
    zeros = laplacian.getZeroCrossings(dog);
    cv::namedWindow("Zero-crossings of DoG");
	cv::imshow("Zero-crossings of DoG", 255-zeros);
    cv::rectangle(image, cv::Rect(cx, cy, dx, dy), cv::Scalar(255, 255, 255));
    cv::namedWindow("Original Image with window");
    cv::imshow("Original Image with window", image);
    cv::waitKey();
    return 0;
}

```

### 小结

在信号处理领域，高通滤波器指的是允许高于某一阈值的频率信息通过，过滤掉低于这一阈值的频率信息，从而大大衰减低频率的一种滤波器。在图像处理中，高通滤波器 (`high-pass filters`) 用于消除图像的低频成分，获取图像边缘。本节中，介绍了高通滤波器的基本概念，并利用高通滤波器实现了图像边缘检测。

转：https://blog.csdn.net/LOVEmy134611/article/details/128794797
