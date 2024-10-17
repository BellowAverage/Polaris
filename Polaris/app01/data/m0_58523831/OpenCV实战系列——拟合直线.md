
--- 
title:  OpenCV实战系列——拟合直线 
tags: []
categories: [] 

---
#### OpenCV实战——拟合直线
<li> 
  <ul>- - - - 
### 0. 前言

在某些应用中，不仅要检测图像中的线条，还要准确估计线条的位置和方向。本节将介绍如何找到最适合给定点集的线。

### 1. 直线拟合

首先要做的是识别图像中可能沿直线对齐的点，可以使用检测到的线段。使用 `cv::HoughLinesP` 检测到的线段 `lines` 包含在向量 `std::vector&lt;cv::Vec4i&gt;` 中。

**(1)** 要提取可能的点集，比如说，第 `1` 条线段，我们可以在黑色图像上绘制一条白线，并将其与用于检测线条的 `Canny` 轮廓图像相交：

```
int n = 0;
// 提取探测到的第一条线段的轮廓像素
cv::Mat oneline(image.size(), CV_8U, cv::Scalar(0));
cv::line(oneline, cv::Point(li[n][0], li[n][1]), cv::Point(li[n][2], li[n][3]), cv::Scalar(255), 3);
cv::bitwise_and(contours, oneline, oneline);

```

以上代码可以获得只包含可以与指定线关联的点，为了引入一些公差，我们绘制了一条一定粗细的线(线宽为 `3`)，因此，在定义的邻域内的所有点可以都被接受。结果如下图所示(为了便于观察，反转图像像素值)：

<img src="https://img-blog.csdnimg.cn/7aa478e49ff44911a5bbb57a8b3456d2.png#pic_center" alt="线关联的点"> **(2)** 通过双循环将这个集合中点的坐标插入到 `cv::Point` 函数的 `std::vector` 中(也可以使用浮点坐标，即 `cv::Point2f`)：

```
std::vector&lt;cv::Point&gt; points;
//  迭代像素以获得所有点位置
for (int y=0; y&lt;oneline.rows; y++) {<!-- -->
    uchar* rowPtr = oneline.ptr&lt;uchar&gt;(y);
    for (int x=0; x&lt;oneline.cols; x++) {<!-- -->
        if (rowPtr[x]) {<!-- -->
            points.push_back(cv::Point(x, y));
        }
    }
}

```

**(3)** 通过调用 `cv::fitLine` 函数很容易找到最佳拟合线段：

```
// 拟合直线
cv::Vec4f line;
cv::fitLine(points, line, cv::DIST_L2, 0, 0.01, 0.01);

```

以上代码以单位方向向量( `cv::Vec4f` 的前两个值)和线上一个点的坐标( `cv::Vec4f` 的后两个值)的形式提供线段方程的参数。对于示例结果，方向向量为 `(0.83, 0.55)`，点坐标的值为 `(366.1, 289.1)`。`cv::fitLine` 函数的最后两个参数用于指定所需线段参数的精度。

**(4)** 线段方程可以用于计算某些属性，作为说明，我们可以在图像上绘制拟合的线。例如，绘制一个长度为 `100` 像素、宽度为 `3` 像素的黑色线段：

```
int x0 = line[2];
int y0 = line[3];
int x1 = x0+100*line[0];
int y1 = y1+100*line[1];
// 绘制直线
cv::line(image, cv::Point(x0, y0), cv::Point(x1, y1), 0, 2);

```

绘制结果如下图所示：

<img src="https://img-blog.csdnimg.cn/01ff07e0287a4e189d44e5e32a4d92e8.png#pic_center" alt="拟合直线"> 将一组点拟合为一条线是数学中的一个经典问题，`cv::fitLine` 函数通过最小化每个点到直线的距离总和来拟合直线。 可以使用不同的距离函数，欧几里得距离( `CV_DIST_L2` ) 是最容易计算的距离，其对应于标准最小二乘线拟合。当点集中包含异常值(即不属于该线的点)时，可以选择其他异常点影响较小的距离函数。最小化基于 `M` 估计技术，该技术迭代地解决加权最小二乘问题，其权重与距离直线的距离成反比。 使用 `cv::fitLine` 函数，还可以将一组 `3D` 点集拟合为一条直线，此时，输入是一组 `cv::Point3i` 或 `cv::Point3f` 类型数据，输出类型为 `std::Vec6f`。`cv::fitEllipse` 函数可以将一组 `2D` 点拟合为椭圆，其返回一个旋转矩形( `cv::RotatedRect` 实例)，椭圆内接于该矩形内：

```
cv::RotatedRect rrect= cv::fitEllipse(cv::Mat(points));
cv::ellipse(image,rrect,cv::Scalar(0));

```

`cv::ellipse` 函数用来绘制计算出的椭圆函数图像。

### 2. 完整代码

库文件 `linefinder.h` 和 `edgedetector.h` 可以参考一节，主函数 `fitLine.cpp` 代码如下所示：

```
#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;opencv2/core/core.hpp&gt;
#include &lt;opencv2/imgproc/imgproc.hpp&gt;
#include &lt;opencv2/highgui/highgui.hpp&gt;
#include "linefinder.h"
#include "edgedetector.h"

#define PI 3.1415926

int main() {<!-- -->
    // 读取输入图像
    cv::Mat image = cv::imread("road.jpg", 0);
    if (!image.data) return 0;
    cv::namedWindow("Original Image");
    cv::imshow("Original Image", image);
    // 计算 Sobel
    EdgeDetector ed;
    ed.computeSobel(image);
    cv::namedWindow("Sobel (orientation)");
    cv::imshow("Sobel (orientation)", ed.getSobelOrientationImage());
    cv::imwrite("ori.png", ed.getSobelOrientationImage());
    // 低阈值 Sobel
    cv::namedWindow("Sobel (low threshold)");
    cv::imshow("Sobel (low threshold)", ed.getBinaryMap(125));
    // 高阈值 Sobel
    cv::namedWindow("Sobel (high threshold)");
    cv::imshow("Sobel (high threshold)", ed.getBinaryMap(350));
    // 应用 Canny 算法
    cv::Mat contours;
    cv::Canny(image,    // 灰度图像
            contours,   // 输出图像
            125,        // 低阈值
            350);       // 高阈值
    cv::namedWindow("Canny Contours");
    cv::imshow("Canny Contours", 255-contours);
    // 霍夫变换
    std::vector&lt;cv::Vec2f&gt; lines;
    cv::HoughLines(contours, lines, 1, PI/180, 50);
    // 绘制检测结果
    cv::Mat result(contours.rows, contours.cols, CV_8U, cv::Scalar(255));
    image.copyTo(result);
    std::cout &lt;&lt; "Lines detected: " &lt;&lt; lines.size() &lt;&lt; std::endl;
    std::vector&lt;cv::Vec2f&gt;::const_iterator it = lines.begin();
    while (it!=lines.end()) {<!-- -->
        float rho = (*it)[0];
        float theta = (*it)[1];
        if (theta &lt; PI/4. || theta &gt; 3.*PI/4.) {<!-- -->    // 竖线
            // 直线与图像第一行交点
            cv::Point pt1(rho/cos(theta), 0);
            // 直线与图像最后一行交点
            cv::Point pt2((rho-result.rows*sin(theta))/cos(theta), result.rows);
            cv::line(result, pt1, pt2, cv::Scalar(255), 1);
        } else {<!-- -->        // 横线
            // 直线与图像第一列交点
            cv::Point pt1(0, rho/sin(theta));
            // 直线与图像最后一列交点
            cv::Point pt2(result.cols, (rho-result.cols*cos(theta))/sin(theta));
            cv::line(result, pt1, pt2, cv::Scalar(255), 1);
        }
        std::cout &lt;&lt; "line: (" &lt;&lt; rho &lt;&lt; "," &lt;&lt; theta &lt;&lt; ")" &lt;&lt; std::endl;
        ++it;
    }
    cv::namedWindow("Lines with Hough");
    cv::imshow("Lines with Hough", result);
    // 创建 LineFinder 实例
    LineFinder ld;
    // 设置概率霍夫变换
    ld.setLineLengthAndGap(100, 20);
    ld.setMinVote(60);
    // 直线检测
    std::vector&lt;cv::Vec4i&gt; li = ld.findLines(contours);
    ld.drawDetectedLines(image);
    cv::namedWindow("Lines with HoughP");
    cv::imshow("Lines with HoughP", image);
    std::vector&lt;cv::Vec4i&gt;::const_iterator it2 = li.begin();
    while (it2 != li.end()) {<!-- -->
        std::cout &lt;&lt; "(" &lt;&lt; (*it2)[0] &lt;&lt; ", " &lt;&lt; 
                (*it2)[1] &lt;&lt; ") - (" &lt;&lt; (*it2)[2] &lt;&lt; 
                ", " &lt;&lt; (*it2)[3] &lt;&lt; ")" &lt;&lt; std::endl;
        ++it2;
    }
    image = cv::imread("road.jpg", 0);
    int n = 0;
    cv::line(image, cv::Point(li[n][0], li[n][1]), cv::Point(li[n][2], li[n][3]), cv::Scalar(255), 5);
    cv::namedWindow("One line of the Image");
    cv::imshow("One line of the Image", image);
    // 提取探测到的第一条线段的轮廓像素
    cv::Mat oneline(image.size(), CV_8U, cv::Scalar(0));
    cv::line(oneline, cv::Point(li[n][0], li[n][1]), cv::Point(li[n][2], li[n][3]), cv::Scalar(255), 3);
    cv::bitwise_and(contours, oneline, oneline);
    cv::namedWindow("One line");
    cv::imshow("One line", 255-oneline);
    std::vector&lt;cv::Point&gt; points;
    //  迭代像素以获得所有点位置
    for (int y=0; y&lt;oneline.rows; y++) {<!-- -->
        uchar* rowPtr = oneline.ptr&lt;uchar&gt;(y);
        for (int x=0; x&lt;oneline.cols; x++) {<!-- -->
            if (rowPtr[x]) {<!-- -->
                points.push_back(cv::Point(x, y));
            }
        }
    }
    // 拟合直线
    cv::Vec4f line;
    cv::fitLine(points, line, cv::DIST_L2, 0, 0.01, 0.01);
    std::cout &lt;&lt; "line: (" &lt;&lt; line[0] &lt;&lt; ", " &lt;&lt; line[1] &lt;&lt; 
            ") (" &lt;&lt; line[2] &lt;&lt; ", " &lt;&lt; line[3] &lt;&lt; std::endl;
    // 直线上的点
    int x0 = line[2];
    int y0 = line[3];
    int x1 = x0+100*line[0];
    int y1 = y0+100*line[1];
    image = cv::imread("road.jpg", 0);
    // 绘制直线
    cv::line(image, cv::Point(x0, y0), cv::Point(x1, y1), 0, 2);
    cv::namedWindow("Fitted line");
    cv::imshow("Fitted line", image);
    cv::waitKey();
    return 0;
}

```

转：https://blog.csdn.net/LOVEmy134611/article/details/128808279?spm=1001.2014.3001.5501
