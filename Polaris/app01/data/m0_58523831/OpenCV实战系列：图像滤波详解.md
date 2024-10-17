
--- 
title:  OpenCV实战系列：图像滤波详解 
tags: []
categories: [] 

---
#### OpenCV实战（12）——图像滤波详解
<li> 
  <ul>- - - - <li> 
    <ul>- - 
### 0. 前言

滤波是信号和中的基本任务之一，其旨在有选择地提取图像的某些特征，可以用于在给定应用程序的上下文中传达重要信息，例如，去除图像中的噪声、提取所需的视觉特征、图像重采样等。图像滤波起源于信号系统理论，本节将介绍一些与滤波相关的重要概念，并展示如何在图像处理应用程序中使用滤波器。

### 1. 频域分析

首先，我们先简要说明频域分析 (`frequency domain analysis`) 的概念。不同图像具有不同的灰度分布，可以用图像的灰度分布作为表征图像的一种方式，但同时，还存在另一种分析图像的观点。观察图像中的灰度变化，可以发现，某些图像包含强度几乎恒定的大面积区域(例如，蓝天)，而某些图像上的灰度强度变化很快(例如，拥挤的街道)。因此，可以用图像中的变化频率作为表征图像的另一种方式，这种方式被称为频域，而通过观察图像的灰度分布来表征图像的方式则被称为空间域。 频域分析将图像从最低频率到最高频率分解为其频率内容，图像强度缓慢变化的区域仅包含低频，而高频是由强度的快速变化产生的。有多种用于计算图像的频率内容的变换，例如傅立叶变换或余弦变换。需要注意的是，由于图像是二维平面，因此频率由垂直频率(垂直方向的变化)和水平频率(水平方向的变化)组成。 在频域分析中，滤波器是一种放大图像某些频带同时减少其他频带的操作。因此，低通滤波器 (`low-pass filters`) 是消除图像高频成分的滤波器，而高通滤波器 (`high-pass filters`) 消除图像的低频成分。本节将介绍一些在图像处理中经常使用的滤波器，并展示将它们应用于图像时的效果。

### 2. 低通滤波器

在本节中，我们将介绍一些基本的低通滤波器。我们已经了解了低通滤波器的目标是减少图像变化的幅度，实现此目标的一种简单方法是将每个像素替换为其周围像素的平均值，通过这种方式，快速的强度变化将变得平滑，从而被更平缓的过渡所取代。`cv::blur` 函数通过将每个像素替换为其矩形邻域上的平均像素值来平滑图像。

**(1)** 使用 `5x5` 的矩形作为滤波器调用平滑模糊函数，将像素值替换为其邻域的平均值：

```
cv::blur(image, result, cv::Size(5, 5));

```

这种滤波器也称为盒式滤波器 (`box filter`)，我们使用 `5x5` 滤波器来调用 `cv::blur()` 函数，以使滤波器的效果更加明显。

<img src="https://img-blog.csdnimg.cn/a3d24bc3294141978dd7d439215fd395.png#pic_center" alt="原始图像">

对上图应用滤波器可以得带以下结果：

<img src="https://img-blog.csdnimg.cn/5b9426106b26412b8867c4bb571b26de.png#pic_center" alt="均值滤波器">

**(2)** 有时，我们可能更加关注像素邻域中较近的像素，此时我们可以使用加权平均值，邻居中靠近中心的像素比外围像素具有更大的权重。可以通过使用诸如高斯函数(钟形函数)的加权方案实现，`OpenCV` 中使用 `cv::GaussianBlur` 函数实现此滤波器：

```
cv::GaussianBlur(image, result, cv::Size(5, 5), 1.5);

```

滤波结果如下图所示：

<img src="https://img-blog.csdnimg.cn/5e769e0bd529433b87385dae57432585.png#pic_center" alt="高斯滤波器">

如果滤波时用相邻像素的加权总和替换像素，则称该滤波器是线性的。均值滤波器就是一种线性滤波器，使用矩形邻域中所有像素的总和除以该邻域的大小后(以获得平均值)替换像素，这等价于在像素邻域中将每个像素乘以 `1/n` 并求和(其中 `n` 表示邻域大小)，滤波器的不同权重可以使用矩阵表示，该矩阵包含与邻域中的每个像素位置相关联的乘法因子，矩阵的中心元素对应于当前应用滤波器的像素。这种矩阵也被称为核或掩码，`3x3` 均值滤波器的核如下：

[ 1 9 1 9 1 9 1 9 1 9 1 9 1 9 1 9 1 9 ] \left[

191919191919191919191919191919191919

\begin{array}{ccc} \frac 1 9 &amp; \frac 1 9 &amp; \frac 1 9\\ \frac 1 9 &amp; \frac 1 9 &amp; \frac 1 9\\ \frac 1 9 &amp; \frac 1 9 &amp; \frac 1 9\\\end{array}\right] ​91​91​91​​91​91​91​​91​91​91​​ ​

`cv::boxFilter` 函数使用核元素全为 `1` 的核执行图像滤波，它类似于均值滤波器，但并未对求和结果计算均值。应用线性滤波器，在图像的每个像素上移动滤波器核并将每个对应的像素乘以其相关的权重，在数学上，这个操作称为卷积 (`convolution`)，数学表达式如下：

I o u t ( x , y ) = ∑ i ∑ j I i n ( x − i , y − j ) K ( i , j ) I_{out}(x,y)=\sum_i\sum_jI_{in}(x-i,y-j)K(i,j) Iout​(x,y)=i∑​j∑​Iin​(x−i,y−j)K(i,j)

上式中的二重求和将 ( x , y ) (x,y) (x,y) 处的当前像素与核 K K K 的中心对齐，假设其中心坐标为 ( 0 , 0 ) (0,0) (0,0)。查看生成的输出图像，可以观察到低通滤波器可以用于模糊或平滑图像，这是因为该滤波器会衰减图像中物体边缘快速变化产生的高频分量。 在高斯滤波器中，像素权重与其距中心像素的距离成正比。一维高斯函数表达式如下：

G ( x ) = A e − x 2 2 σ 2 G(x)=Ae^{\frac {-x^2} {2\sigma ^2}} G(x)=Ae2σ2−x2​

使用归一化系数 A A A 确保像素权重总和为 `1`， σ σ σ (`sigma`) 值控制高斯函数的宽度，该值越大，函数越平坦。例如，如果计算区间 `[-4, 4]` 的一维高斯滤波器的系数， σ = 0.5 σ = 0.5 σ=0.5，可以得到以下系数：

```
0.5 = [9.96126e-15 1.19795e-08 0.000263865 0.106451 0.786571 0.106451 0.000263865 1.19795e-08 9.96126e-15]

```

而当系数 σ = 1.5 σ=1.5 σ=1.5 时，系数如下：

```
1.5 = [0.00761442 0.036075 0.109586 0.213445 0.26656 0.213445 0.109586 0.036075 0.00761442]

```

这些值可以通过使用相应的 σ σ σ 值调用 `cv::getGaussianKernel` 函数获得：

```
cv::Mat gauss= cv::getGaussianKernel(9, sigma,CV_32F);

```

高斯函数的对称钟形使其成为滤波的良好选择：

<img src="https://img-blog.csdnimg.cn/09094ee768da40339ff1fddeb0e582c4.png#pic_center" alt="高斯函数">

离中心越远的像素权重越低，这使得像素间的过渡更平滑，而在简单的均值滤波器中，距离中心较远的像素会导致平均值的突变，从频率角度分析，这意味着均值滤波器不会去除所有高频分量。 要在图像上应用 `2D` 高斯滤波器，可以首先在图像横坐标方向上应用 `1D` 高斯滤波器(用于衰减水平频率)，然后在图像纵坐标方向上应用另一个 `1D` 高斯滤波器(用于衰减垂直频率)。这是由于高斯滤波器是一个可分离滤波器，可分离滤波器意味着二维滤波器可以分解为两个一维滤波器，调用 `cv::sepFilter2D` 函数可以实现可分离滤波器的分离。也可以使用 `cv::filter2D` 函数直接应用二维核，一般来说，可分离滤波器比不可分离滤波器的计算速度更快，因为前者需要较少的乘法运算。 使用 `cv::GaussianBlur()` 函数需要提供滤波器中系数的数量(系数数量为奇数)作为函数的第 `3` 个参数，第 `4` 个参数 σ σ σ 指定所用高斯滤波器函数；也可以仅设置 σ σ σ 的值，且设置滤波器尺寸为 `0`，此时 `OpenCV` 可以自行确定适当的系数数量；或者可以仅设置滤波器尺寸，将 σ σ σ 值设置为 `0`，此时 `OpenCV` 将自行确定最适合给定尺寸的 σ σ σ 值。

### 3. 图像下采样

调整图像尺寸大小也称 (`resampled`)，是一种常见的图像处理操作。减小图像大小的过程通常称为下采样 (`downsampling`)，而增加其大小的过程称为上采样 (`upsampling`)。执行这些操作的挑战在于确保尽可能保留图像的视觉质量。为了实现这一目标，通常使用低通滤波器 (`low-pass filters`)。 最简单的减小图像尺寸的方法是消除图像的某些列和行，但生成的图像质量并不好。下图通过通过简单地保留每 `4` 列(行)中的 `1` 列(行)而令原始图像大小缩小了 `4` 倍，可以看到图像质量大幅下降。为了便于观察图像的缺陷，我们通过放大像素显示来缩放图像：

<img src="https://img-blog.csdnimg.cn/019e745452a2408391c3a8937f91e6c7.png#pic_center" alt="图像缩放">

可以看到图像质量有明显下降。例如，在图像的纹理部分(例如皮肤)上可以看到锯齿状扭曲。这些伪影是由空间混叠 (`spatial aliasing`) 现象引起的，当试图在一幅尺寸较小而无法包含高频分量的图像中显示高频分量时，会出现此问题，较小的图像(即像素较少的图像)无法像高分辨率图像那样表现出精细的纹理和锐利的边缘。由于图像中的精细细节对应于高频部分，我们需要在缩小图像尺寸之前消除图像中的高频分量，我们可以使用低通滤波器来完成。

#### 3.1 使用低通滤波器下采样图像

**(1)** 要在不添加伪影的情况下将图像的大小缩小为原来的 `1/4`，必须先对原始图像应用低通滤波器，然后再丢弃图像中相应的像素列和行：

```
// 首先消除高频分量后缩放图像
cv::GaussianBlur(image, image, cv::Size(11, 11), 1.75);
cv::Mat reduced2(image.rows/4, image.cols/4, CV_8U);
for (int i=0; i&lt;reduced2.rows; i++) {<!-- -->
    for (int j=0; j&lt;reduced2.cols; j++) {<!-- -->
        reduced2.at&lt;uchar&gt;(i, j) = image.at&lt;uchar&gt;(i*4, j*4);
    }
}

```

生成的图像如下图所示：

<img src="https://img-blog.csdnimg.cn/85dc6fbfc256437cbe1f821f31876de1.png#pic_center" alt="低通滤波后缩放图像">

图像中丢失了一部分精细细节，但总体而言，图像的视觉质量比直接丢弃像素更好。为了避免混叠效应，图像在缩小尺寸之前必须进行低通滤波，消除较小图像中无法表示的高频分量。这一理论通常被称为 `Nyquist-Shannon` 定理，简单而言，该理论证明了，如果将图像下采样为原来的 `1/2`，那么可表示频率的带宽也会减少 `1/2`。 使用 `OpenCV` 函数 `cv::pyrDown` 可以执行图像缩小操作：

```
cv::Mat reducedImage; 
cv::pyrDown(image,reducedImage); 

```

以上函数使用 `5x5` 高斯滤波器对图像进行低通处理，然后将其缩小 `2` 倍，而函数 `cv::pyrUp` 则用于执行图像放大操作，上采样是通过在每行和列像素间插入 `0` 值，然后应用 `5x5` 高斯滤波器完成的。显然，如果在缩小图像后再放大，图像无法准确的恢复为原始图像，在缩小尺寸过程中丢失的图像细节无法恢复。 `cv::pyrDown` 和 `cv::pyrUp` 函数可以用于创建图像金字塔，图像金字塔一个由同一图像的不同尺寸堆叠组成的数据结构(可以自定义尺寸的缩减因子)，通常用于进行高效的图像分析。例如，如果想检测图像中的一个物体，可以先在金字塔顶部的小尺寸图像上完成检测，定位到目标物体后，可以通过移动到金字塔底部来细化搜索高分辨率版本的图像。 更通用的 `cv::resize` 函数可以指定所需的结果图像大小，只需通过指定新尺寸进行调用：

```
cv::Mat resizedImage;
cv::resize(image, resizedImage, cv::Size(image.cols/4, image.rows/4)); 

```

还可以指定比例因子调整图像大小，此时，指定一个空的 `cv::Size` 实例作为参数，然后传入比例因子：

```
cv::resize(image, resizedImage, cv::Size(), 1.0/4.0, 1.0/4.0); 

```

`cv::resize` 函数的最后一个参数用于选择要在重采样过程中使用的插值方法。

#### 3.2 内插像素值

当图像按缩放因子调整大小时，需要执行一些像素插值，以便在现有像素之间填充新像素值。执行插值的最基本方法是使用最近邻策略，每个新像素都被赋值为原始图像中与其最接近像素的值。在图像上采样时，这意味着新图像的多个像素将从相同的原始像素接收值。例如，我们使用最近邻插值(插值标志 `cv::INTER_NEAREST` )将缩小后的图像重新放大 `3` 倍：

```
cv::resize(reduced, newImage, cv::Size(), 3, 3, cv::INTER_NEAREST);

```

结果如下图所示：

<img src="https://img-blog.csdnimg.cn/58c09d3daca04a09b9496d92f7e02a74.png#pic_center" alt="图像缩放">

在这种情况下，插值相当于将每个像素的尺寸大小扩大为原来的 `3` 倍，为了获取更好的图像质量，我们可以通过组合几个相邻像素的值计算新的像素值，例如，我们可以通过考虑周围的四个像素线性插入新的像素值：

<img src="https://img-blog.csdnimg.cn/77d3c3f93c634b96a14c57fef29c398a.png#pic_center" alt="插值">

首先在添加的像素的左侧和右侧垂直插入两个像素值，然后，这两个插值像素(上图中灰色圆形)用于查找插值位置所需的像素值。这种双线性插值方案是 `cv::resize` 使用的默认方法，可以由标志 `cv::INTER_LINEAR` 显式指定：

```
cv::resize(reduced2, newImage, cv::Size(), 4, 4, cv::INTER_LINEAR);

```

结果如下图所示：

<img src="https://img-blog.csdnimg.cn/bb0eedc80bf0470ca43d51e723ce5bf5.png#pic_center" alt="双线性插值">

也可以使用双三次插值以产生更好的结果，双三次插值使用 `4x4` 像素邻域执行插值，但由于该方法使用更多像素并使用三次项计算，因此它比双线性插值速度更慢。

### 4. 中值滤波器

上一小节中，我们已经介绍了线性滤波器的概念，此外，非线性滤波器也可以用于图像处理，中值滤波器就是一个非线性滤波器，中值滤波器对于消除椒盐噪声特别有效。

<img src="https://img-blog.csdnimg.cn/42fe1cebe5e444d28f5a99953f3a1b44.png#pic_center" alt="椒盐噪声">

**(1)** 中值滤波函数的调用方式与其他滤波器类似，例如，使用核大小为 `5` 的 `cv::medianBlur` 函数：

```
cv::medianBlur(image, result, 5);

```

生成的图像如下图所示：

<img src="https://img-blog.csdnimg.cn/9df7ee6fda4948fc8100b211925ea934.png#pic_center" alt="中值滤波">

由于中值滤波器不是线性滤波器，因此不能用核矩阵表示。但它也需要对像素的邻域进行操作以确定输出像素值。中值滤波器将计算当前像素及其邻域的中值，然后将当前像素替换为中值(一组变量值按大小顺序排列起来，形成一个数列，处于变量数列中间位置的变量值就称为中值，或称中位数)。 这也解释了中值滤波器在消除椒盐噪声方面的有效性：当给定像素邻域中存在异常黑色或白色像素时，它永远不会为中值(它是最大值或最小值)，因此它总是被相邻值替换。相比之下，简单的均值滤波器会受到此类噪声的极大影响，如下图所示，使用均值滤波处理包含椒盐噪声的图像：

<img src="https://img-blog.csdnimg.cn/7a987ae75f2a4cd9a8ca30bfd103d7e4.png#pic_center" alt="均值滤波">

显然，噪声像素会改变相邻像素的平均值，即使噪声被均值滤波器所模糊，它仍然是可见的。 中值滤波器还具有保留边缘锐度的优点。但是，它会清除均匀区域中的纹理(例如，背景中的树木)。中值滤波器常用于在照片编辑软件工具中创建特殊效果，例如使用中值滤波器生成卡通化图像。

### 5. 完整代码

完整代码 (`filters.cpp`) 如下所示：

```
#include &lt;iostream&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;

int main() {<!-- -->
    // 读取输入图像
    cv::Mat image = cv::imread("1.png", 0);
    if (!image.data) return 0;
    cv::namedWindow("Original Image");
    cv::imshow("Original Image", image);
    // 使用均值滤波器模糊图像
    cv::Mat result;
    cv::blur(image, result, cv::Size(5, 5));
    cv::namedWindow("Mean filtered Image");
    cv::imshow("Mean filtered Image", result);
    // 使用 9x9 均值滤波器模糊图像
    cv::blur(image, result, cv::Size(9, 9));
    cv::namedWindow("Mean filtered Image (9x9)");
    cv::imshow("Mean filtered Image (9x9)", result);
    // 高斯滤波
    cv::GaussianBlur(image, result, cv::Size(5, 5), 1.5);
    cv::namedWindow("Gaussian filtered Image");
    cv::imshow("Gaussian filtered Image", result);
    cv::GaussianBlur(image, result, cv::Size(9, 9), 1.7);
    cv::namedWindow("Gaussian filtered Image (9x9)");
    cv::imshow("Gaussian filtered Image (9x9)", result);
    // 获取高斯核
    cv::Mat gauss = cv::getGaussianKernel(9, 1.5, CV_32F);
    // 显示核值
    cv::Mat_&lt;float&gt;::const_iterator it = gauss.begin&lt;float&gt;();
    cv::Mat_&lt;float&gt;::const_iterator itend = gauss.end&lt;float&gt;();
    std::cout &lt;&lt; "1.5 = [";
    for ( ; it!= itend; ++it) {<!-- -->
        std::cout &lt;&lt; *it &lt;&lt; " ";
    }
    std::cout &lt;&lt; "]" &lt;&lt; std::endl;
    // 获取高斯核 (sigmma=0.5)
    gauss = cv::getGaussianKernel(9, 0.5, CV_32F);
    it= gauss.begin&lt;float&gt;();  
    itend= gauss.end&lt;float&gt;();  
    std::cout &lt;&lt; "0.5 = [";
    for ( ; it!= itend; ++it) {<!-- -->
        std::cout &lt;&lt; *it &lt;&lt; " ";
    }
    std::cout &lt;&lt; "]" &lt;&lt; std::endl;
    // 获取高斯核 (sigmma=2.5)
    gauss = cv::getGaussianKernel(9, 2.5, CV_32F);
    it= gauss.begin&lt;float&gt;();  
    itend= gauss.end&lt;float&gt;();  
    std::cout &lt;&lt; "2.5 = [";
    for ( ; it!= itend; ++it) {<!-- -->
        std::cout &lt;&lt; *it &lt;&lt; " ";
    }
    std::cout &lt;&lt; "]" &lt;&lt; std::endl;
    // 获取高斯核 (9个元素)
    gauss = cv::getGaussianKernel(9, -1, CV_32F);
    it= gauss.begin&lt;float&gt;();  
    itend= gauss.end&lt;float&gt;();  
    std::cout &lt;&lt; "9 = [";
    for ( ; it!= itend; ++it) {<!-- -->
        std::cout &lt;&lt; *it &lt;&lt; " ";
    }
    std::cout &lt;&lt; "]" &lt;&lt; std::endl;
    // 获取微分核 (2.5)
    cv::Mat kx, ky;
    cv::getDerivKernels(kx, ky, 2, 2, 7, true);
    cv::Mat_&lt;float&gt;::const_iterator kit= kx.begin&lt;float&gt;();  
    cv::Mat_&lt;float&gt;::const_iterator kitend= kx.end&lt;float&gt;();  
    std::cout &lt;&lt; "[";
    for ( ; kit!= kitend; ++kit) {<!-- -->
        std::cout &lt;&lt; *kit &lt;&lt; " ";
    }
    std::cout &lt;&lt; "]" &lt;&lt; std::endl;
    // 读取带有椒盐噪声的图像
    image = cv::imread("noisy_img.png", 0);
    if (!image.data) return 0;
    cv::namedWindow("S&amp;P Image");
    cv::imshow("S&amp;P Image",image);
    // 使用均值滤波
    cv::blur(image, result, cv::Size(5, 5));
    cv::namedWindow("Mean filtered S&amp;P Image");
    cv::imshow("Mean filtered S&amp;P Image",result);
    // 使用中值滤波
    cv::medianBlur(image, result, 5);
    cv::namedWindow("Median filtered Image");
    cv::imshow("Median filtered Image",result);
    // 将图像缩小为原来的 1/4 (错误方式)
    image = cv::imread("1.png", 0);
    cv::Mat reduced(image.rows/4, image.cols/4, CV_8U);
    for (int i=0; i&lt;reduced.rows; i++) {<!-- -->
        for (int j=0; j&lt;reduced.cols; j++) {<!-- -->
            reduced.at&lt;uchar&gt;(i, j) = image.at&lt;uchar&gt;(i*4, j*4);
        }
    }
    cv::namedWindow("Badly reduced Image");
    cv::imshow("Badly reduced Image", reduced);
    cv::resize(reduced, reduced, cv::Size(), 4, 4, cv::INTER_NEAREST);
    cv::namedWindow("Badly reduced");
	cv::imshow("Badly reduced", reduced);
	cv::imwrite("badlyreducedimage.png", reduced);
    // 首先消除高频分量后缩放图像
    cv::GaussianBlur(image, image, cv::Size(11, 11), 1.75);
    cv::Mat reduced2(image.rows/4, image.cols/4, CV_8U);
    for (int i=0; i&lt;reduced2.rows; i++) {<!-- -->
        for (int j=0; j&lt;reduced2.cols; j++) {<!-- -->
            reduced2.at&lt;uchar&gt;(i, j) = image.at&lt;uchar&gt;(i*4, j*4);
        }
    }
    cv::namedWindow("Reduced Image, original size");
    cv::imshow("Reduced Image, original size", reduced2);
    cv::imwrite("reducedimage.png", reduced2);
    // 使用最近邻算法缩放图像
    cv::Mat newImage;
    cv::resize(reduced2, newImage, cv::Size(), 4, 4, cv::INTER_NEAREST);
    cv::namedWindow("Reduced Image");
    cv::imshow("Reduced Image",newImage);
    // 使用双线性插值缩放图像
    cv::resize(reduced2, newImage, cv::Size(), 4, 4, cv::INTER_LINEAR);
    cv::namedWindow("Bilinear resizing");
	cv::imshow("Bilinear resizing", newImage);
    // 创建图像金字塔
    cv::Mat pyramid(image.rows, 
            image.cols+image.cols/2+image.cols/4+image.cols/8,
            CV_8U, cv::Scalar(255));
    image.copyTo(pyramid(cv::Rect(0, 0, image.cols, image.rows)));
    cv::pyrDown(image, reduced);
    reduced.copyTo(pyramid(cv::Rect(image.cols, image.rows/2,
                                image.cols/2, image.rows/2)));
    cv::pyrDown(reduced, reduced2);
    reduced2.copyTo(pyramid(cv::Rect(image.cols+image.cols/2, 
                                image.rows-image.rows/4,
                                image.cols/4, image.rows/4)));
    cv::pyrDown(reduced2, reduced);
    reduced.copyTo(pyramid(cv::Rect(image.cols+image.cols/2+image.cols/4,
                                image.rows-image.rows/8,
                                image.cols/8, image.rows/8)));
    cv::namedWindow("Pyramid of images");
    cv::imshow("Pyramid of images", pyramid);
    cv::waitKey();
    return 0;
}

```

### 小结

图像滤波，即在尽量保留图像细节特征的条件下对目标图像的噪声进行抑制，通常可以用作图像预处理操作，低通滤波器 (`low-pass filters`) 是消除图像高频成分的滤波器，而高通滤波器 (`high-pass filters`) 消除图像的低频成分。本节，我们介绍了频域分析的基本概念，并且介绍了常见的低通滤波器，同时介绍了常用的图像下采样方法，并展示了如何在图像处理应用程序中使用滤波器。

转：https://blog.csdn.net/LOVEmy134611/article/details/128781377
