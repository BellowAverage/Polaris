
--- 
title:  OpenCV实战系列——轮廓检测详解 
tags: []
categories: [] 

---


####  
- <ul><li>- - <ul><li>- - 


### 0. 前言

在领域，轮廓通常指图像中对象边界的一系列点。因此，轮廓通常描述了对象边界的关键信息，包含了有关对象形状的主要信息，该信息可用于形状分析与对象检测和识别。本节中，我们首先介绍如何提取图像中轮廓，然后讲解如何计算轮廓的形状描述符。

### 1. 提取区域轮廓

#### 1.1 轮廓提取

图像通常包含目标对象的表示，图像分析的目标之一是识别和提取这些对象。在/识别应用中，通常需要生成一个二值图像，显示目标物体的位置，提取包含在二值图像中的对象。例如，使用如下二值图像：

<img src="https://img-blog.csdnimg.cn/3d092b8a79824651925924a6a88b6047.png#pic_center" alt="二值图像">

我们可以通过简单的阈值操作获得此图像，然后应用开/闭形态滤波器。本节将介绍如何提取图像中的目标对象，更具体地说，我们将提取图像中的连接部分，即由中的一组连接像素组成的形状。`OpenCV` 提供了一个简单的函数来提取图像的连接部分的轮廓，即 `cv::findContours` 函数。

**(1)** 要使用 `cv::findContours` 函数，我们需要一个点向量存储所有输出轮廓：

```
std::vector&lt;std::vector&lt;cv::Point&gt; &gt; contours;

```

**(2)** 使用 `cv::findContours` 函数检测图像的所有轮廓并将它们保存在轮廓向量中：

```
cv::findContours(image,
        contours,               // 轮廓向量
        cv::RETR_EXTERNAL,      // 检索外部轮廓
        cv::CHAIN_APPROX_NONE); // 检索每个轮廓的所有像素

```

`cv::findContours` 函数的输入是二值图像，输出是一个轮廓向量，每个轮廓由一个 `cv::Point` 对象向量表示，因此输出参数定义为 `std::vector` 对象。此外，还指定了两个标志，第一个表示只需要外部轮廓，即忽略对象中的孔；第二个标志用于指定轮廓的格式，使用 `CV_CHAIN_APPROX_NONE` 选项，向量将列出轮廓中的所有点，使用 `CV_CHAIN_APPROX_SIMPLE` 标志，将仅包含水平、垂直或对角线轮廓的端点，也可以使用其他标志获取更复杂的轮廓链近似表示。使用上示图像，可以得到 `10` 个连通分量。

**(3)** 使用 `OpenCV` 可以非常方便地在一张图片上绘制出连接部分的轮廓：

```
cv::Mat result(image.size(), CV_8U, cv::Scalar(255));
cv::drawContours(result, contours,
                -1,             // 绘制所有轮廓
                cv::Scalar(0),  // 颜色
                2);             // 线宽为2

```

如果此函数的第 `3` 个参数为负值，则绘制所有轮廓，也可以使用正值指定要绘制的轮廓的索引，如下图所示：

<img src="https://img-blog.csdnimg.cn/c30006e6decc4393b0982a758ce3bfd2.png#pic_center" alt="轮廓图像">

轮廓是通过系统地扫描图像直到检测出所有的目标部分，从连接部分上的起点开始，沿着它的轮廓，在其边框上标记像素；完成标记后，在最后一个位置继续扫描，直到找到新的连接部分。

**(4)** 然后可以单独分析识别的连接部分。例如，我们可以通过预估目标对象的预期大小消除一些无效部分，可以使用连接部分周长的最小值和最大值消除无效连接：

```
// 消除所有过短或过长的轮廓
int cmin = 50;
int cmax = 500;
std::vector&lt;std::vector&lt;cv::Point&gt; &gt;::iterator itc = contours.begin();
while (itc!=contours.end()) {<!-- -->
    if (itc!=contours.end()) {<!-- -->
        if (itc-&gt;size()&lt;cmin || itc-&gt;size()&gt;cmax) {<!-- -->
            itc = contours.erase(itc);
        } else {<!-- -->
            ++itc;
        }
    }
}

```

由于 `std::vector` 中的每个消除操作的时间复杂度都是 O ( N ) O(N) O(N)，因此该循环可以进一步进行优化。在原图上绘制轮廓，结果如下图所示：

<img src="https://img-blog.csdnimg.cn/39c8fa75af434b9ab1105cf06f951693.png#pic_center" alt="轮廓绘制">

#### 1.2 复杂轮廓分析

使用简单的标准就能够帮助我们识别图像中所有感兴趣的对象，在更复杂情况下，我们需要对连接部分的属性进行更精细的分析。 使用 `cv::findContours` 函数，还可以通过在函数调用中指定 `CV_RETR_LIST` 标志检测二值图中所有闭合轮廓(包括对象中的孔形轮廓)：

```
cv::findContours(image, contours, cv::RETR_LIST, cv::CHAIN_APPROX_NONE);

```

使用以上函数调用，可以得到以下轮廓：

<img src="https://img-blog.csdnimg.cn/8037b95dc7f34be7b61a60d76f0c4378.png#pic_center" alt="轮廓">

可以看到上图中增加了额外轮廓。也可以将这些轮廓组织成层次结构，主要部分是父组件，其中的孔是其子组件，如果这些孔内还有组件，它们将成为之前子组件的子组件，依此类推，该层次结构可以通过使用 `CV_RETR_TREE` 标志获得：

```
std::vector&lt;cv::Vec4i&gt; hierarchy;
cv::findContours(image,
                contours, // 轮廓向量
                hierarchy, // 分层表示
                CV_RETR_TREE, // 使用树结构检索所有轮廓 
                CV_CHAIN_APPROX_NONE); // 每一轮廓的所有像素

```

在这种情况下，每个轮廓在相同的索引处都有一个对应的层次元素，由四个整数组成。前两个整数提供了同一级别的下一个和前一个轮廓的索引，后两个整数提供该轮廓的第一个子项和父项的索引，负索引表示轮廓列表的结尾。`CV_RETR_CCOMP` 标志类似，但层次结构仅包括两个级别。

### 2. 计算区域形状描述符

连接部分通常对应于图片场景的中某个目标对象，为了识别此对象，或将其与其他图像元素进行比较，我们可能需要进行测量以提取所需特征。在本节中，我们介绍 `OpenCV` 中可用的形状描述符，用于描述轮廓形状。 有多个 `OpenCV` 函数可用作形状描述符，应用这些函数可以提取连接部分。我们使用目标对象相对应的轮廓向量，计算轮廓上( `contours[0]` 到 `contours[3]` )的形状描述符并在轮廓图像(线宽为 `1` )上绘制结果(线宽为 `2`)。

**(1)** `boundingRect` 函数用于计算矩形边框：

```
// 矩形
cv::Rect r0 = cv::boundingRect(contours[0]);
cv::rectangle(result, r0, 0, 2);

```

**(2)** `minEnclosingCircle` 函数用于近似最小包围圆：

```
// 圆形
float radius;
cv::Point2f center;
cv::minEnclosingCircle(contours[1], center, radius);
cv::circle(result, center, static_cast&lt;int&gt;(radius), 0, 2);

```

**(3)** 区域轮廓的多边形近似使用 `approxPolyDP` 函数：

```
// 近似多边形
std::vector&lt;cv::Point&gt; poly;
cv::approxPolyDP(contours[2], poly, 5, true);
cv::polylines(result, poly, true, 0, 2);
std::cout &lt;&lt; "Polygon size: " &lt;&lt; poly.size() &lt;&lt; std::endl;

```

多边形绘制函数 `cv::polylines` 与其他绘图函数类似，第 `3` 个参数为布尔类型用于指示轮廓是否闭合，如果为true，则将最后一个点连接到第一个点。

**(4)** 凸包函数 `convexHull` 是多边形近似的另一种形式：

```
// 凸包
std::vector&lt;cv::Point&gt; hull;
cv::convexHull(contours[3], hull);
cv::polylines(result, hull, true, 0, 2);

```

**(5)** 矩是另一个强大的描述符，可以计算区域内的质心：

```
// 矩
itc = contours.begin();
while (itc!=contours.end()) {<!-- -->
    cv::Moments mom = cv::moments(*itc++);
    cv::circle(result,
                cv::Point(mom.m10/mom.m00, mom.m01/mom.m00),
                2, cv::Scalar(0), 2);
}

```

结果图像如下：

<img src="https://img-blog.csdnimg.cn/ac61f51c330f4e05a173a082637ec039.png#pic_center" alt="形状描述符">

边界框大多数情况下是表示和定位图像中目标对象的最紧凑的方式，其定义为完全包含对象形状的最小尺寸的矩形。边界框的高度和宽度可以指示对象的垂直或水平尺寸，例如，可以使用高宽比来区分汽车和行人；当只需要目标的近似尺寸和位置时，通常使用最小包围圆。 当想要与目标对象形状相似的紧凑的表示时，可以采用多边形近似，通过指定精度参数( `cv::approxPolyDP` 函数中的第 `4` 个参数)指定目标对象形状与近似多边形之间的最大可接受距离，函数返回的 `cv::Point` 的向量对应于多边形的顶点。为了绘制这个多边形，我们需要遍历向量并在它们之间线段将相邻点连接起来。 形状的凸包或凸包络是包含形状的最小凸多边形，可以将其想象为弹性皮筋围在目标对象周围时的形状，凸包轮廓将在对象形状轮廓的凹面位置偏离原始轮廓，这些位置通常称为凸面缺陷，并且可以使用 `OpenCV` 函数 `cv::convexityDefects` 识别这些缺陷，调用方式如下所示：

```
std::vector&lt;cv::Vec4i&gt; defects;
cv::convexityDefects(contours[3], hull, defects);

```

`contour` 和 `hull` 参数分别是原始轮廓和凸包轮廓(均为 `std::vector&lt;cv::Point&gt;` 实例)。输出是由四个整数元素组成的向量，前两个整数是轮廓上的点索引，用于界定缺陷；第三个整数对应凹面内最远的点，最后一个整数对应这个最远点到凸包的距离。 矩是形状结构分析中常用的数学工具，`OpenCV` 定义了一个封装了形状所有计算矩的数据结构，`cv::moments` 函数的返回值就使用这种数据结构，这些矩构成了对物体形状的简洁描述。我们可以使用这个结构中前3个空间矩来获得形状的质心。 也可以使用 `OpenCV` 函数计算结构属性，`cv::minAreaRect` 函数计算最小的封闭旋转矩形；`cv::contourArea` 函数估计轮廓(内部像素数)的面积；`cv::pointPolygonTest` 函数用于确定一个点是在轮廓内部还是外部，而 `cv::matchShapes` 可以测量两个轮廓之间的相似性。我们可以通过组合所有这些属性进行更高级的图像结构分析。

#### 2.1 四边形检测

我们可以利用形态学操作转换后获得的图像提取图像形状，假设，我们使用形态学操作转换图像获得的 `MSER` 结果，然后构建算法检测图像中的四边形分量。假设我们检测以下使用 `MSER` 算法得到的二值图像，检测四边形分量能够帮助我们识别建筑物上的窗户等，为了减少图像中的噪音，我们使用了一些形态滤波器对图像进行预处理：

```
// 创建二值图像
components = components==255;
// 图像开操作
cv::morphologyEx(components, components, cv::MORPH_OPEN, cv::Mat(), cv::Point(-1, -1), 3);

```

接下来，获取轮廓：

```
// 反转图像
cv::Mat componentsInv = 255 - components;
// 获取轮廓和连接部分
cv::findContours(componentsInv, contours, cv::RETR_LIST, cv::CHAIN_APPROX_NONE);

```

最后，遍历所有轮廓并用多边形近似：

```
cv::Mat quadri(components.size(), CV_8U, 255);
std::vector&lt;std::vector&lt;cv::Point&gt; &gt;::iterator it = contours.begin();
while (it!= contours.end()) {<!-- -->
    poly.clear();
    // 使用多边形近似轮廓
    cv::approxPolyDP(*it,poly,5,true);
    // 检测轮廓是否为四边形
    if (poly.size()==4) {<!-- -->
        cv::polylines(quadri, poly, true, 0, 2);
    }

    ++it;
}

```

检测结果如下所示：

<img src="https://img-blog.csdnimg.cn/a4b09cb08333416aac754dbca1c73448.png#pic_center" alt="四边形描述符">

如果想要检测矩形，我们可以测量相邻边之间的角度并消除掉偏差过大(与 `90` 度相比)的四边形。

### 3. 完整代码

完整代码文件 `blobs.cpp` 如下所示：

```
#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;

int main() {<!-- -->
    // 读取二进制图像
    cv::Mat image = cv::imread("binary.png", 0);
    if (!image.data) return 0;
    cv::namedWindow("Binary Image");
    cv::imshow("Binary Image", image);
    // 获取轮廓和连接部分
    std::vector&lt;std::vector&lt;cv::Point&gt; &gt; contours;
    cv::findContours(image,
            contours,               // 轮廓向量
            cv::RETR_EXTERNAL,      // 检索外部轮廓
            cv::CHAIN_APPROX_NONE); // 检索每个轮廓的所有像素
    std::cout &lt;&lt; "Contours: " &lt;&lt; contours.size() &lt;&lt; std::endl;
    std::vector&lt;std::vector&lt;cv::Point&gt; &gt;::const_iterator itContours = contours.begin();
    for (; itContours!=contours.end(); ++itContours) {<!-- -->
        std::cout &lt;&lt; "Size: " &lt;&lt; itContours-&gt;size() &lt;&lt; std::endl;
    }
    // 绘制轮廓
    cv::Mat result(image.size(), CV_8U, cv::Scalar(255));
    cv::drawContours(result, contours,
                    -1,             // 绘制所有轮廓
                    cv::Scalar(0),  // 颜色
                    2);             // 线宽为2
    cv::namedWindow("Contours");
    cv::imshow("Contours", result);
    // 消除所有过短或过长的轮廓
    int cmin = 50;
    int cmax = 500;
    std::vector&lt;std::vector&lt;cv::Point&gt; &gt;::iterator itc = contours.begin();
    while (itc!=contours.end()) {<!-- -->
        if (itc!=contours.end()) {<!-- -->
            if (itc-&gt;size()&lt;cmin || itc-&gt;size()&gt;cmax) {<!-- -->
                itc = contours.erase(itc);
            } else {<!-- -->
                ++itc;
            }
        }
    }
    // 绘制轮廓
    cv::Mat original = cv::imread("2.png");
    cv::drawContours(original, contours, -1, cv::Scalar(0, 0, 255), 2);
    cv::namedWindow("Contours on Animals");
    cv::imshow("Contours on Animals",original);
    result.setTo(cv::Scalar(255));
    cv::drawContours(result, contours, -1, 0, 1);
    image = cv::imread("binary.png", 0);
    // 矩形
    cv::Rect r0 = cv::boundingRect(contours[0]);
    cv::rectangle(result, r0, 0, 2);
    // 圆形
    float radius;
    cv::Point2f center;
    cv::minEnclosingCircle(contours[1], center, radius);
    cv::circle(result, center, static_cast&lt;int&gt;(radius), 0, 2);
    // 近似多边形
    std::vector&lt;cv::Point&gt; poly;
    cv::approxPolyDP(contours[2], poly, 5, true);
    cv::polylines(result, poly, true, 0, 2);
    std::cout &lt;&lt; "Polygon size: " &lt;&lt; poly.size() &lt;&lt; std::endl;
    // 凸包
    std::vector&lt;cv::Point&gt; hull;
    cv::convexHull(contours[3], hull);
    cv::polylines(result, hull, true, 0, 2);
    // std::vector&lt;cv::Vec4i&gt; defects;
    // cv::convexityDefects(contours[3], hull, defects);
    // 矩
    itc = contours.begin();
    while (itc!=contours.end()) {<!-- -->
        cv::Moments mom = cv::moments(*itc++);
        cv::circle(result,
                    cv::Point(mom.m10/mom.m00, mom.m01/mom.m00),
                    2, cv::Scalar(0), 2);
    }
    cv::namedWindow("Some Shape descriptors");
    cv::imshow("Some Shape descriptors", result);
    image = cv::imread("binary.png", 0);
    cv::findContours(image, contours, cv::RETR_LIST, cv::CHAIN_APPROX_NONE);
    result.setTo(255);
    cv::drawContours(result, contours, -1, 0, 2);
    cv::namedWindow("All Contours");
    cv::imshow("All Contours", result);
    // MSER 图像
    cv::Mat components;
    components = cv::imread("mser.png",0);
    // 创建二值图像
    components = components==255;
    // 图像开操作
    cv::morphologyEx(components, components, cv::MORPH_OPEN, cv::Mat(), cv::Point(-1, -1), 3);
    cv::namedWindow("MSER image");
    cv::imshow("MSER image", components);
    contours.clear();
    // 反转图像
    cv::Mat componentsInv = 255 - components;
    // 获取轮廓和连接部分
    cv::findContours(componentsInv, contours, cv::RETR_LIST, cv::CHAIN_APPROX_NONE);
    cv::Mat quadri(components.size(), CV_8U, 255);
    std::vector&lt;std::vector&lt;cv::Point&gt; &gt;::iterator it = contours.begin();
    while (it!= contours.end()) {<!-- -->
        poly.clear();
        // 使用多边形近似轮廓
        cv::approxPolyDP(*it,poly,5,true);
        // 检测轮廓是否为四边形
        if (poly.size()==4) {<!-- -->
            cv::polylines(quadri, poly, true, 0, 2);
        }

        ++it;
    }
    cv::namedWindow("MSER quadrilateral");
    cv::imshow("MSER quadrilateral", quadri);
    cv::waitKey();
    return 0;
}

```

### 小结

在本文中，首先介绍了轮廓的相关概念，然后了解利用 `cv::findContours()` 检测轮廓、`cv::drawContours()` 绘制轮廓，在获取轮廓后，我们可以计算轮廓的形状描述符。

转：https://blog.csdn.net/LOVEmy134611/article/details/128833287?spm=1001.2014.3001.5501
