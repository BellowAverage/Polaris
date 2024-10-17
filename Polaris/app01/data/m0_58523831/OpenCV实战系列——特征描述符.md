
--- 
title:  OpenCV实战系列——特征描述符 
tags: []
categories: [] 

---
#### OpenCV实战系列——特征描述符
<li> 
  <ul>- - - <li> 
    <ul>- - - 
### 0. 前言

为每个检测到的特征计算位置、方向和比例，比例因子信息可用于定义每个特征点周围的图像窗口的大小。因此，无论特征所属对象的比例如何，定义的邻域都将包含相同的视觉信息。本节将介绍如何使用特征描述符描述兴趣点的邻域，在图像分析中，该邻域中包含的视觉信息可用于表征每个特征点，以区分不同特征点。特征描述符通常是 `N` 维向量，以对光照变化和透视变形的方式描述特征点。通常，可以使用简单的距离度量来比较描述符，例如欧几里得距离。因此，特征描述符是可以用于特征匹配应用程序的强大工具。

### 1. 特征描述符

`cv::Feature2D` 抽象类定义了许多成员函数，用于计算关键点列表的描述符。由于大多数基于特征的方法都包括检测器和描述符组件，因此相关的类包括检测函数(检测兴趣点)和计算函数(计算它们的描述符)，例如 `cv::xfeatures2d::SURF` 和 `cv::xfeature2d::SIFT` 类。接下来，我们创建 `SURF` 特征检测器。

**(1)** 创建 `SURF` 描述符：

```
cv::Ptr&lt;cv::Feature2D&gt; ptrFeature2D = cv::xfeatures2d::SURF::create(2000.0);

```

**(2)** 检测图像中的关键点：

```
ptrFeature2D-&gt;detect(image1, keypoints1);
ptrFeature2D-&gt;detect(image2, keypoints2);

```

**(3)** 对于检测到的每个关键点，提取它们的描述符：

```
cv::Mat descriptors1;
cv::Mat descriptors2;
ptrFeature2D-&gt;compute(image1, keypoints1, descriptors1);
ptrFeature2D-&gt;compute(image2, keypoints2, descriptors2);

```

**(4)** 对于 `SIFT`，只需创建一个 `SIFT` 对象。输出结果是一个 `cv::Mat` 矩阵实例，矩阵的行数等于关键点向量中的元素数量，其中每一行都是一个 `N` 维描述符向量。对于 `SURF` 描述符，它的默认维度为 `64`；而对于 `SIFT`，默认维度为 `128`。该向量表征特征点邻域的强度模式，两个特征点越相似，它们的描述符向量也就越接近，这些描述符将用于关键点间的匹配。

**(5)** 将第一张图像中的每个特征描述符向量与第二张图像中的所有特征描述符进行比较，具有最佳相似度分数的特征点对(即两个描述符向量之间距离最小的特征点对)被保留为该特征的最佳匹配，对第一张图像中的所有特征重复此过程，在 `OpenCV` 中可以使用 `cv::BFMatcher` 类实现此过程，而无需使用双循环：

```
// 构建匹配器
cv::BFMatcher matcher(cv::NORM_L2);
// 匹配两个图像描述子
std::vector&lt;cv::DMatch&gt; matches;
matcher.match(descriptors1, descriptors2, matches);

```

`cv::BFMatcher` 类是 `cv::DescriptorMatcher` 类的子类，其定义了不同匹配策略的通用接口，输出结果为 `cv::DMatch` 实例向量。 使用当前的 `SURF` 的 `Hessian` 阈值，在第一张图像可以得到 `320` 个关键点，第二张图像可以得到 `266` 个关键点。使用蛮力法可以得到 `320` 个匹配，使用 `cv::drawMatches` 类绘制结果如下所示：

<img src="https://img-blog.csdnimg.cn/4ee057cda81c4d83b85d67a5e9960039.png#pic_center" alt="匹配结果"> 可以看出，其中一些匹配正确地将左侧的一个点与其右侧的对应点联系起来。但图中也包含一些错误；这是由于图中人物皮肤纹理具有重复结构，使得一些局部匹配受到干扰。 特征描述符必须对光照、视点和图像噪声的微小变化保持鲁棒性，因此，特征描述符通常基于局部强度差异。 `SURF` 描述符在关键点局部邻域应用以下核：

<img src="https://img-blog.csdnimg.cn/7d5d09155fc346ad92131ca7c7a5b7f1.png#pic_center" alt="SURF 核"> 第一个核测量水平方向上的局部强度差异(指定为 `dx`)，第二个核测量垂直方向上的差异(指定为 `dy`)。用于提取描述符向量的邻域大小一般定义为特征尺度因子的 `20` 倍(即 `20σ`)，然后将该方形区域分成 `4x4` 个较小的方形子区域。对于每个子区域，使用以上核计算结果如下，每个子区域提取四个描述符值： [ ∑ d x ∑ d y ∑ ∣ d x ∣ ∑ ∣ d y ∣ ] \left[ ∑dx∑dy∑|dx|∑|dy|\begin{array}{ccc} \sum dx &amp; \sum dy &amp; \sum |dx| &amp; \sum |dy| \\\end{array}\right] [∑dx​∑dy​∑∣dx∣​∑∣dy∣​] 由于有 `4x4=16` 个子区域，共有 `64` 个描述符值，为了更加重视邻近像素，计算使用以关键点位置为中心的高斯加权 (`σ=3.3`)。 `dx` 和 `dy` 结果也用于估计特征的方向，这些值是在半径为 `6σ` 的圆形邻域内以 `σ` 为间隔计算的(核大小为 `4σ`)。对于给定的方向，将某个角度间隔 (`π/3`) 内的计算结果相加，并将最长矢量方向定义为主导方向。 `SIFT` 是一种更丰富的描述符，它使用图像梯度而非强度差异，它还将每个关键点周围的正方形邻域拆分为 `4x4` 子区域(也可以使用 `8x8` 或 `2x2` 子区域)。在每个区域内，构建了梯度方向的直方图，梯度方向被离散成 `8` 个 `bin`，每个梯度方向 `bin` 与梯度大小成正比。可以用下图进行说明，其中每个星形箭头表示梯度方向的局部直方图：

<img src="https://img-blog.csdnimg.cn/db408d8d235346769cc73e5c1404b9b9.png#pic_center" alt="梯度方向直方图"> 将 `16` 个包含 `8` 个 `bin` 的直方图连接在一起，产生一个 `128` 维的描述符。对于 `SURF`，梯度值由以关键点位置为中心的高斯滤波器加权，以使描述符对定义邻域周边梯度方向的突然变化不那么敏感，然后对最终描述符进行归一化以使距离测量更加一致。 使用 `SURF` 和 `SIFT` 特征和描述符，可以实现尺度不变匹配。下图展示了不同比例的两个图像的 `SURF` 匹配结果(图中显示了 `50` 个最佳匹配)：

<img src="https://img-blog.csdnimg.cn/ac1c7504d33340ffa7d5dc9995e70d18.png#pic_center" alt="SURF 匹配结果">

### 2. 提升匹配集质量

任何匹配算法产生的匹配结果总是包含大量不正确的匹配。接下来，我们介绍三种提高匹配集质量的策略。

#### 2.1 交叉检查匹配

验证获得的匹配的一种简单方法是再次重复相同的过程，但第二次我们将第二幅图像的每个关键点与第一幅图像的关键点进行比较。只有当我们在两个方向上获得相同的关键点对(两个关键点互为最佳匹配)时，才认为匹配是有效的。`cv::BFMatcher` 函数提供了使用此策略的选项，当第二个参数设置为 `true` 时，函数会强制执行交叉检查匹配：

```
cv::BFMatcher matcher(cv::NORM_L2, true);

```

改进后的匹配结果如下图所示(以 `SURF` 特征匹配为例)：

<img src="https://img-blog.csdnimg.cn/a0a615fd08d44dcd82f71ea80d2c5565.png#pic_center" alt="带有交叉验证的匹配结果">

#### 2.2 比率测试

我们已经了解了场景对象中的重复元素会产生不可靠的结果，因为这会在匹配视觉上相似的结构时存在歧义，在这种情况下，一个关键点将与多个关键点匹配。由于选择错误匹配的可能性较高，因此在这种情况下最好拒绝此类匹配。 要使用此策略，我们需要找到每个关键点的两个最佳匹配点，这可以通过使用 `cv::DescriptorMatcher` 类的 `knnMatch` 方法来完成。由于我们只想保留两个最佳匹配，因此指定 `k=2`：

```
std::vector&lt;std::vector&lt;cv::DMatch&gt; &gt; matches2;
matcher.knnMatch(descriptors1, descriptors2, matches2, 2);

```

接下来拒绝所有匹配距离与其次佳匹配相似的匹配。由于 `knnMatch` 输出结果为 `std::vector` 类实例，可以通过循环每个关键点匹配执行比率测试(如果两个匹配的距离相等，则比率为 `1`)：

```
double ratioMax = 0.8;
std::vector&lt;std::vector&lt;cv::DMatch&gt; &gt;::iterator it;
for (it=matches2.begin(); it!=matches2.end(); ++it) {<!-- -->
    if ((*it)[0].distance/(*it)[1].distance &lt; ratioMax) {<!-- -->
        matches.push_back((*it)[0]);
    }
}

```

可以看到匹配由最初的 `320` 对减少到 `29` 对，且其中很大一部分均为正确的匹配：

<img src="https://img-blog.csdnimg.cn/ff0cb2e36913461e9e2aa9bb43a72f1b.png#pic_center" alt="带有比率测试的匹配结果">

#### 2.3 距离阈值

距离阈值策略即拒绝描述符之间的距离过高的匹配项，可以使用 `cv::DescriptorMatcher` 类的 `radiusMatch` 方法完成：

```
float maxDist = 0.2;
matches2.clear();
matcher.radiusMatch(descriptors1, descriptors2, matches2, maxDist);

```

结果同样是一个 `std::vector` 实例，因为该方法将保留距离小于指定阈值的所有匹配项。这意味着给定的关键点在另一幅图像中可能有多个匹配点，而另一些关键点可能没有任何与之关联的匹配项。使用此策略，可以将匹配数量减少至 `25` 对：

<img src="https://img-blog.csdnimg.cn/3cadbacc42b044f8920930db4f54f368.png" alt="带有距离阈值的匹配结果">

### 3. 完整代码

完整代码 `matcher.cpp` 如下所示：

```
#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;
#include &lt;opencv2/features2d/features2d.hpp&gt;
#include &lt;opencv2/objdetect/objdetect.hpp&gt;
#include &lt;opencv2/xfeatures2d.hpp&gt;

int main() {<!-- -->
    // 图像匹配
    // 1. 读取图像
    cv::Mat image1 = cv::imread("1.png", cv::IMREAD_GRAYSCALE);
    cv::Mat image2 = cv::imread("2.png", cv::IMREAD_GRAYSCALE);
    // 2. 定义关键点向量
    std::vector&lt;cv::KeyPoint&gt; keypoints1;
    std::vector&lt;cv::KeyPoint&gt; keypoints2;
    // 3. 定义特征检测器
    // SURF
    cv::Ptr&lt;cv::Feature2D&gt; ptrFeature2D = cv::xfeatures2d::SURF::create(2000.0);
    // SIFT
    // cv::Ptr&lt;cv::Feature2D&gt; ptrFeature2D = cv::xfeatures2d::SIFT::create(74);
    // 4. 关键点检测
    ptrFeature2D-&gt;detect(image1, keypoints1);
    ptrFeature2D-&gt;detect(image2, keypoints2);
    // 绘制特征点
    cv::Mat featureImage;
    cv::drawKeypoints(image1, keypoints1, featureImage, cv::Scalar(255, 255, 255), cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    cv::namedWindow("SURF");
    cv::imshow("SURF",featureImage);
    std::cout &lt;&lt; "Number of SURF keypoints (image 1): " &lt;&lt; keypoints1.size() &lt;&lt; std::endl; 
    std::cout &lt;&lt; "Number of SURF keypoints (image 2): " &lt;&lt; keypoints2.size() &lt;&lt; std::endl;
    // 提取描述子
    cv::Mat descriptors1;
    cv::Mat descriptors2;
    ptrFeature2D-&gt;compute(image1, keypoints1, descriptors1);
    ptrFeature2D-&gt;compute(image2, keypoints2, descriptors2);
    // 构建匹配器
    cv::BFMatcher matcher(cv::NORM_L2);
    // 交叉验证
    // cv::BFMatcher matcher(cv::NORM_L2, true);
    // 匹配两个图像描述子
    std::vector&lt;cv::DMatch&gt; matches;
    matcher.match(descriptors1, descriptors2, matches);
    // 绘制匹配
    cv::Mat imageMatches;
    cv::drawMatches(image1, keypoints1,       // 第一张图像及其关键点
                    image2, keypoints2,         // 第二张图像及其关键点
                    matches,                    // 匹配
                    imageMatches,               // 生成结果
                    cv::Scalar(255, 255, 255),  // 线颜色
                    cv::Scalar(255, 255, 255),  // 点颜色
                    std::vector&lt;char&gt;(),        // 掩码
                    cv::DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS | cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    cv::namedWindow("SURF Matches");
    cv::imshow("SURF Matches",imageMatches);
    std::cout &lt;&lt; "Number of matches: " &lt;&lt; matches.size() &lt;&lt; std::endl;
    // 实施比例测试
    std::vector&lt;std::vector&lt;cv::DMatch&gt; &gt; matches2;
    matcher.knnMatch(descriptors1, descriptors2, matches2, 2);
    matches.clear();
    double ratioMax = 0.8;
    std::vector&lt;std::vector&lt;cv::DMatch&gt; &gt;::iterator it;
    for (it=matches2.begin(); it!=matches2.end(); ++it) {<!-- -->
        if ((*it)[0].distance/(*it)[1].distance &lt; ratioMax) {<!-- -->
            matches.push_back((*it)[0]);
        }
    }
    cv::drawMatches(image1, keypoints1,         // 第一张图像及其关键点
                    image2, keypoints2,         // 第二张图像及其关键点
                    matches,                    // 匹配
                    imageMatches,               // 生成结果
                    cv::Scalar(255, 255, 255),  // 线颜色
                    cv::Scalar(255, 255, 255),  // 点颜色
                    std::vector&lt;char&gt;(),        // 掩码
                    cv::DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS | cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    std::cout &lt;&lt; "Number of matches (after ratio test): " &lt;&lt; matches.size() &lt;&lt; std::endl; 
    cv::namedWindow("SURF Matches (ratio test at 0.6)");
    cv::imshow("SURF Matches (ratio test at 0.6)", imageMatches);
    // 半径匹配
    float maxDist = 0.2;
    matches2.clear();
    matcher.radiusMatch(descriptors1, descriptors2, matches2, maxDist);
    cv::drawMatches(image1, keypoints1,         // 第一张图像及其关键点
                    image2, keypoints2,         // 第二张图像及其关键点
                    matches2,                    // 匹配
                    imageMatches,               // 生成结果
                    cv::Scalar(255, 255, 255),  // 线颜色
                    cv::Scalar(255, 255, 255),  // 点颜色
                    std::vector&lt;std::vector&lt;char&gt; &gt;(), // 掩码
                    cv::DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS | cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    int nmatches = 0;
    for (int i=0; i&lt;matches2.size(); i++) {<!-- -->
        nmatches += matches2[i].size();
    }
    std::cout &lt;&lt; "Number of matches (with max radius): " &lt;&lt; nmatches &lt;&lt; std::endl;
    cv::namedWindow("SURF Matches (with max radius)");
    cv::imshow("SURF Matches (with max radius)", imageMatches);
    // 尺度不变测试
    image1 = cv::imread("1.png", cv::IMREAD_GRAYSCALE);
    image2 = cv::imread("2.png", cv::IMREAD_GRAYSCALE);
    std::cout &lt;&lt; "Number of SIFT keypoints (image 1): " &lt;&lt; keypoints1.size() &lt;&lt; std::endl; 
    std::cout &lt;&lt; "Number of SIFT keypoints (image 2): " &lt;&lt; keypoints2.size() &lt;&lt; std::endl;
    // 提取关键点和描述符
    ptrFeature2D = cv::xfeatures2d::SIFT::create();
    ptrFeature2D-&gt;detectAndCompute(image1, cv::noArray(), keypoints1, descriptors1);
    ptrFeature2D-&gt;detectAndCompute(image2, cv::noArray(), keypoints2, descriptors2);
    // 匹配两张图像描述子
    matcher.match(descriptors1, descriptors2, matches);
    // 提取 50 个最佳匹配
    std::nth_element(matches.begin(),matches.begin()+50,matches.end());
    matches.erase(matches.begin()+50,matches.end());
    cv::drawMatches(image1, keypoints1,       // 第一张图像及其关键点
                    image2, keypoints2,         // 第二张图像及其关键点
                    matches,                    // 匹配
                    imageMatches,               // 生成结果
                    cv::Scalar(255, 255, 255),  // 线颜色
                    cv::Scalar(255, 255, 255),  // 点颜色
                    std::vector&lt;char&gt;(),        // 掩码
                    cv::DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS | cv::DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    cv::namedWindow("Multi-scale SIFT Matches");
    cv::imshow("Multi-scale SIFT Matches",imageMatches);
    std::cout &lt;&lt; "Number of matches: " &lt;&lt; matches.size() &lt;&lt; std::endl; 
    cv::waitKey();
    return 0;
}

```

### 小结

特征描述符是用于特征匹配应用程序的强大工具，本节介绍了如何使用 `SURF` 和 `SIFT` 特征描述符匹配图像特征点，并介绍了三种不同方法改进匹配结果：交叉检查匹配、比率测试和距离阈值。

转载：https://blog.csdn.net/LOVEmy134611/article/details/130188868
