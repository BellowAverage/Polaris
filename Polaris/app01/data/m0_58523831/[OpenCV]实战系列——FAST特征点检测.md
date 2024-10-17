
--- 
title:  [OpenCV]实战系列——FAST特征点检测 
tags: []
categories: [] 

---
#### [OpenCV]实战系列——FAST特征点检测
<li> 
  <ul>- - - - - - 
### 0. 前言

[Harris 算子]根据两个垂直方向上的强度变化率给出了角点(或更一般地说，兴趣点)的数学定义。但使用这种定义需要计算图像导数，计算代价较为高昂，特别是兴趣点检测通常只是更复杂算法的先决步骤。 在本中，我们将学习另一个特征点检测[算子] `FAST` (`Features from Accelerated Segment Test`)。其专门设计用于快速检测图像中的兴趣点；[关键点检测]仅基于几个像素的比较。

### 1. FAST 特征点检测

使用 [OpenCV 通用接口]进行特征点检测，能够轻松使用任意特征点检测器。本节将介绍 `FAST` 检测器，顾名思义，其被设计为进行快速计算。

**(1)** 创建一个关键点向量来存储结果：

```
std::vector&lt;cv::KeyPoint&gt; keypoints;

```

**(2)** 创建一个阈值为 `40` 的 FAST 检测器：

```
// FAST 检测器
cv::Ptr&lt;cv::FastFeatureDetector&gt; ptrFAST = new cv::FastFeatureDetector(40);

```

**(3)** 检测加载图像的所有关键点：

```
ptrFAST-&gt;detect(image, keypoints);

```

`OpenCV` 还提供了一个通用函数来在图像上绘制关键点：

```
cv::drawKeypoints(image, keypoints, image, cv::Scalar(255, 255, 255), cv::DrawMatchesFlags::DRAW_OVER_OUTIMG);

```

通过指定绘图标志，将关键点绘制在输入图像上，可以得到以下输出结果：

<img src="https://img-blog.csdnimg.cn/be76f38533a54ed8b66c8604eefb7a69.png#pic_center" alt="FAST特征检测结果"> 当我们将关键点颜色指定为负值时，绘制的每个圆圈将使用不同的随机颜色。 与 `Harris` 角点一样，`FAST` 特征算法源于角点定义，该定义基于特征点周围的图像强度。关键点的检测通过检查以候选点为中心的像素圆进行，如果找到长度大于圆周长 `3/4` 的连续点(弧)，其所有像素都与中心点的强度显着不同，则该候选点为一个关键点。 这是一个可以快速计算的检测过程。此外，在其公式中，该算法使用了一个额外的技巧来进一步加快计算过程。事实上，如果我们首先测试圆上相距 `90` 度的四个点(例如，上、下、右、左)，为了满足检测条件，其中至少三个点都必须比中心像素更亮或更暗，否则，可以立即否定该点，而无需检查圆周上的其他点。这是一个非常高效的检测技巧，因为在实践中，大多数图像点都无法满足此四点检测条件。 要检查像素圆的半径是该方法需要考虑的一个因素，在实践中发现，半径为 `3` 时检测效果较好，效率也更高，此时，需要考虑圆周上的 `16` 个像素： R ≈ [ 16 1 2 15 3 14 4 13 0 5 12 6 11 7 10 9 8 ] R\approx\left[

141312151116101092837456161215314413051261171098

\begin{array}{ccc} &amp; &amp; 16 &amp; 1 &amp; 2 &amp; &amp;\\ &amp; 15 &amp; &amp; &amp; &amp; 3&amp; \\ 14&amp;&amp;&amp;&amp;&amp;&amp;4\\ 13&amp;&amp;&amp;0&amp;&amp;&amp;5\\ 12&amp;&amp;&amp;&amp;&amp;&amp;6\\ &amp; 11 &amp; &amp; &amp; &amp; 7&amp;\\ &amp; &amp; 10 &amp; 9 &amp; 8 &amp; &amp;\\\end{array}\right] R≈ ​141312​1511​1610​109​28​37​456​ ​

在以上示例中，用于预测试的四个点的像素值为 `1`、`5`、`9` 和 `13`，所需满足条件的连续较暗或较亮的像素点数为 `12`。但是，可以观察到通过将连续段的长度减少到 `9`，可以更好的检测到角点在不同图像上的可重复性。这种变体通常称为 `FAST-9` 角点检测器，这也是 `OpenCV` 中所采用的。此外，`OpenCV` 中的 `cv::FASTX` 函数实现了 `FAST` 检测器的另一个变体。 一个像素点的强度必须与中心像素的强度相差指定的量才会被视为满足更暗或更亮的检测条件，相差的量使用函数中的阈值参数指定，阈值越大，检测到的角点就越少。 而对于 `Harris` 特征而言，通常需要对已经检测到的角点进行非极大值抑制。因此，需要定义角点强度度量。也可以考虑以下替代方案，角点强度由中心像素与所识别的连续弧上的像素之间的绝对差之和给出，该算法也可通过直接函数调用实现：

```
cv::FAST(image,     // 输入图像
        keypoints,  // 输出关键点向量
        40,         // 阈值
        false);     // 是否使用非极大值抑制

```

但是，推荐使用 `cv::FeatureDetector` 接口，提高应用程序的灵活性。 `FAST` 特征点检测算法实现了非常快的兴趣点检测，因此，当程序需要效率优先时，应该首选该算法，例如，在实时视觉跟踪或对象识别应用程序中，必须在实时视频流中跟踪或匹配多个特征点。 为了改进特征点的检测，`OpenCV` 提供使用许多类适配器，以更好地控制关键点的提取。

### 2. 自适应特征检测

如果希望更好地控制特征点的数量，可以使用 `cv::FeatureDetector` 类的子类 `cv::DynamicAdaptedFeatureDetector`，其可以指定检测的兴趣点数量，在 `FAST` 特征检测器中用法如下：

```
cv::DynamicAdaptedFeatureDetector fastD(
    new cv::FastAdjuster(40),   // 特征检测器
    150,                        // 最少特征数量
    200,                        // 最大特征数量
    50);                        // 最大迭代次数
fastD-&gt;detect(image, keypoints);

```

然后迭代地检测兴趣点，每次迭代后，检查检测到的兴趣点数量，并相应地调整检测器阈值以产生更多或更少的点；重复此过程，直到检测到的兴趣点数位于指定的区间内。 通过指定最大迭代次数，避免过多检测耗费太多时间。要以通用方式实现此方法，使用的 `cv::FeatureDetector` 类必须实现 `cv::AdjusterAdapter` 接口，该类包括一个 `tooFew` 方法和一个 `tooMany` 方法，这两个方法都会修改检测器的内部阈值以产生更多或更少的关键点；此外，还有一个断言方法，当检测器阈值仍然可以调整时返回 `true`。 虽然可以使用 `cv::DynamicAdaptedFeatureDetector` 类获得适当数量的特征点，但是这需要以降低效率为代价；此外，该类无法保证一定会在指定的迭代次数内获得所需数量的特征点。 可以看到，我们将动态分配对象的地址作为参数传递，以指定适配器类将使用的特征检测器。我们无需手动释放分配的内存来避免内存泄漏，这是因为指针会被转移到 `cv::Ptr&lt;FeatureDetector&gt;` 参数，它会自动释放所指向的对象。 另一个有用的类适配器是 `cv::GridAdaptedFeatureDetector` 类，它会在图像上定义网格，然后，可以限制每个单元格包含的最大元素数量，以将检测到的关键点散布在图像上。在检测图像中的关键点时，通常会在特定纹理区域中看到集中的兴趣点。例如，在以上图像的眼睛周围检测到非常密集的 `FAST` 特征点，通过使用此类适配器可以改进检测结果：

```
cv::GridAdaptedFeatureDetector fastG(
    new cv::FastFeatureDetector(10),   // 特征检测器
    1200,                              // 最大特征点数量
    5,                                 // 网格行数
    2);                                // 网格列数
fastG-&gt;detect(image, keypoints);

```

类适配器通过使用提供的 `cv::FeatureDetector` 对象检测每个单元格上的特征点，还可以指定最大总特征点数，在每个单元格中只保留强度最大的数个点，以免超过指定的最大值。 `cv::PyramidAdaptedFeatureDetector` 适配器可以在图像金字塔上应用特征检测器，结果组合在关键点的输出向量中：

```
cv::PyramidAdaptedFeatureDetector fastP(
    new cv::FastFeatureDetector(60),   // 特征检测器
    3);                                // 金字塔层数
fastP-&gt;detect(image, keypoints);

```

每个点的坐标通过原始图像坐标指定，此外设置 `cv::Keypoint` 类的 `size` 属性，以便在原始分辨率的一半处检测到的点的大小是原始图像中检测到的点的大小的两倍。将 `cv::drawKeypoints` 函数中的 `flag` 参数设为 `cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS`，可以令绘制的半径等于关键点 `size` 属性。

### 3. 完整代码

头文件 (`harrisDetector.h`) 完整代码参考 一节，主函数文件 (`fastCorners.cpp`) 完整代码如下所示：

```
#include &lt;iostream&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;
#include &lt;opencv2/features2d/features2d.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/xfeatures2d.hpp&gt;

#include "harrisDetector.h"

int main() {<!-- -->
    // 读取图像
    cv::Mat image = cv::imread("1.png", 0);
    if (!image.data) return 0;
    cv::transpose(image, image);
    cv::flip(image, image, 0);
    cv::namedWindow("Original");
    cv::imshow("Original",image);
    std::vector&lt;cv::KeyPoint&gt; keypoints;
    // FAST 特征
    image = cv::imread("1.png", 0);
    cv::transpose(image, image);
    cv::flip(image, image, 0);
    keypoints.clear();
    // FAST 检测器
    cv::Ptr&lt;cv::FastFeatureDetector&gt; ptrFAST = cv::FastFeatureDetector::create(40);
    ptrFAST-&gt;detect(image, keypoints);
    cv::drawKeypoints(image, keypoints, image, cv::Scalar(255, 255, 255), cv::DrawMatchesFlags::DRAW_OVER_OUTIMG);
    std::cout &lt;&lt; "Number of keypoints (FAST): " &lt;&lt; keypoints.size() &lt;&lt; std::endl;
    cv::namedWindow("FAST");
    cv::imshow("FAST",image);
    // 未使用非极大值抑制的 FAST 特征
    image = cv::imread("1.png", 0);
    cv::transpose(image, image);
    cv::flip(image, image, 0);
    keypoints.clear();
    ptrFAST-&gt;setNonmaxSuppression(false);
    ptrFAST-&gt;detect(image, keypoints);
    cv::drawKeypoints(image, keypoints, image, cv::Scalar(255, 255, 255), cv::DrawMatchesFlags::DRAW_OVER_OUTIMG);
    cv::namedWindow("FAST Features (all)");
    cv::imshow("FAST Features (all)",image);
    // 读取图像
    image = cv::imread("1.png", 0);
    cv::transpose(image, image);
    cv::flip(image, image, 0);
    int total(100);         // 关键点数量
    int hstep(5), vstep(3); // 4x3 的网格
    int hsize(image.cols/hstep), vsize(image.rows/vstep);
    int subtotal(total/(hstep*vstep));  // 每个网格中的关键点数量
    cv::Mat imageROI;
    std::vector&lt;cv::KeyPoint&gt; gridpoints;
    std::cout &lt;&lt; "Grid of " &lt;&lt; vstep &lt;&lt; " by " &lt;&lt; hstep &lt;&lt; " each of size " &lt;&lt; vsize &lt;&lt; " by " &lt;&lt; hsize &lt;&lt; std::endl;
    // 使用低阈值探测
    ptrFAST-&gt;setThreshold(20);
    // 非极大值抑制
    ptrFAST-&gt;setNonmaxSuppression(true);
    keypoints.clear();
    for (int i=0; i&lt;vstep; i++) {<!-- -->
        for (int j=0; j&lt;hstep; j++) {<!-- -->
            // 在当前网格上创建ROI
            imageROI = image(cv::Rect(j*hsize, i*vsize, hsize, vsize));
            // 在网格中检测关键点
            gridpoints.clear();
            ptrFAST-&gt;detect(imageROI, gridpoints);
            std::cout &lt;&lt; "Number of FAST in grid " &lt;&lt; i &lt;&lt; "," &lt;&lt; j &lt;&lt; ": " &lt;&lt; gridpoints.size() &lt;&lt; std::endl;
            if (gridpoints.size()&gt;subtotal) {<!-- -->
                for (auto it=gridpoints.begin(); it!=gridpoints.end()+subtotal; ++it) {<!-- -->
                    std::cout &lt;&lt; "  " &lt;&lt; it-&gt;response &lt;&lt; std::endl;
                }
            }
            // 获取最强 FAST 特征
            auto itEnd(gridpoints.end());
            if (gridpoints.size()&gt;subtotal) {<!-- -->
                std::nth_element(gridpoints.begin(), 
                                gridpoints.end()+subtotal, 
                                gridpoints.end(),
                                [](cv::KeyPoint&amp; a, cv::KeyPoint&amp; b) {<!-- -->return a.response&gt;b.response;});
                itEnd = gridpoints.begin() + subtotal;
            }
            // 添加到全局关键点向量
            for (auto it=gridpoints.begin(); it!=itEnd; ++it) {<!-- -->
                it-&gt;pt += cv::Point2f(j*hsize, i*vsize);
                keypoints.push_back(*it);
                std::cout &lt;&lt; " " &lt;&lt; it-&gt;response &lt;&lt; std::endl;
            }
        }
    }
    cv::drawKeypoints(image, keypoints, image, cv::Scalar(255, 255, 255), cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    cv::namedWindow("FAST Features (grid)");
    cv::imshow("FAST Features (grid)", image);
    cv::waitKey();
    return 0;
}

```

### 小结

为了解决 `Harris` 角点检测算法计算代价较为高昂的缺点，特征点检测算子 `FAST` (`Features from Accelerated Segment Test`) 被专门设计用于快速检测图像中的角点。本节，我们介绍了如何使用通用接口调用 `OpenCV` 中的 `FAST` 特征点检测算法。

转：https://blog.csdn.net/LOVEmy134611/article/details/128841811
