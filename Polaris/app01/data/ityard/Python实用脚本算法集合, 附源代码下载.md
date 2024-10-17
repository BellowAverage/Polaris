
--- 
title:  Python实用脚本/算法集合, 附源代码下载 
tags: []
categories: [] 

---
学习编程、学习Python最好的方式就是练习，哪怕是新手，只要不断地敲代码输出，肯定会有神效。

Python的练手项目很多，特别是Github上，建议不管新手、老司机都去看看。

这里推荐给大家两个Github上练习的项目，**算法仓库-algorithms**和**脚本仓库-Python master**。

后文会有相应源代码集打包下载，给需要的小伙伴。

### algorithms算法仓库

首先来看看算法仓库-algorithms。

这里面集合众多核心算法的Python实现，比如排序、图计算、回溯、队列、流计算、堆、搜索、压缩等等。

<img src="https://img-blog.csdnimg.cn/img_convert/1921827330533d9f8ab142177f0c12ca.png" alt="1921827330533d9f8ab142177f0c12ca.png">

该仓库支持第三方库安装，在python中进行调用，非常方便。

首先使用pip进行安装：

```
pip3 install algorithms
```

然后导入相关模块进行调用，比如sort模块里的merge_sort归并排序算法。

```
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

个人感觉这个仓库里的算法很齐全，适合做练习，小伙伴们可以试试。

所有算法脚本**已经打包好，获取步骤如下：**

1，点击下方公众号 **数据STUDIO** 名片

2，关注 **数据STUDIO**后，在消息后台回复 **b**

**▲点击关注「数据STUDIO」回复<strong><strong><strong>b**</strong></strong></strong>

**<strong><strong><strong><strong>另外，@公众号：<strong>数据STUDIO** 还为大家整理和筛选了大量火爆全网的Python数据科学学习资料，全部资料按需自助**免费获取！直接点击👇链接：  **</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>

### **Python脚本仓库**

另外还有一个很好的练手项目，脚本仓库-Python master。

这个项目收集了作者平时工作用到的几千个实用小脚本，作者虽然不是程序员，但他这种用代码解决问题的习惯会极大的提升效率，也会迸发出更多的创新思维。

我觉得这样的代码每个人都可以写出来，只要慢慢积累多练习就可以。

举一个简单的例子，作者写了一个创建二维码的脚本，可以自动将url转化为二维码。

```
import pyqrcode
import png
from pyqrcode import QRCode

# Text which is to be converted to QR code
print("Enter text to convert")
s = input(": ")
# Name of QR code png file
print("Enter image name to save")
n = input(": ")
# Adding extension as .pnf
d = n + ".png"
# Creating QR code
url = pyqrcode.create(s)
# Saving QR code as  a png file
url.show()
url.png(d, scale=6)
```

除此之外，该仓库中还有很多这样实用的脚本文件。

所有算法脚本**已经打包好，获取步骤如下：**

1，点击下方公众号 **数据STUDIO** 名片

2，关注 **数据STUDIO**后，在消息后台回复 **d**

**▲点击关注「数据STUDIO」回复<strong><strong><strong>d**</strong></strong></strong>

**<strong><strong><strong><strong>另外，@公众号：<strong>数据STUDIO** 还为大家整理和筛选了大量火爆全网的Python数据科学学习资料，全部资料按需自助**免费获取！直接点击👇链接：  **</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>

接下来，展示一些更多的代码案例，供大家参考。

#### 从图片中截取文字

```
# extract text from a img and its coordinates using the pytesseract module
import cv2
import pytesseract

# You need to add tesseract binary dependency to system variable for this to work

img = cv2.imread("img.png")
# We need to convert the img into RGB format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hI, wI, k = img.shape
print(pytesseract.image_to_string(img))
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(" ")
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hI - y), (w, hI - h), (0, 0, 255), 0.2)

cv2.imshow("img", img)
cv2.waitKey(0)
```

#### 判断闰年

```
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(input("Enter the year here: "))
print(is_leap(year))
```

#### 打印图片分辨率

```
def jpeg_res(filename):
   """"This function prints the resolution of the jpeg image file passed into it"""

   # open image for reading in binary mode
   with open(filename,'rb') as img_file:

       # height of image (in 2 bytes) is at 164th position
       img_file.seek(163)

       # read the 2 bytes
       a = img_file.read(2)

       # calculate height
       height = (a[0] &lt;&lt; 8) + a[1]

       # next 2 bytes is width
       a = img_file.read(2)

       # calculate width
       width = (a[0] &lt;&lt; 8) + a[1]

   print("The resolution of the image is",width,"x",height)

jpeg_res("img1.jpg")
```

#### 排序算法-桶排序

```
def bucket_sort(arr):
    ''' Bucket Sort
        Complexity: O(n^2)
        The complexity is dominated by nextSort
    '''
    # The number of buckets and make buckets
    num_buckets = len(arr)
    buckets = [[] for bucket in range(num_buckets)]
    # Assign values into bucket_sort
    for value in arr:
        index = value * num_buckets // (max(arr) + 1)
        buckets[index].append(value)
    # Sort
    sorted_list = []
    for i in range(num_buckets):
        sorted_list.extend(next_sort(buckets[i]))
    return sorted_list

def next_sort(arr):
    # We will use insertion sort here.
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] &gt; key and j &gt;= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
```

#### 机器学习-最近邻插值法

```
import math

def distance(x,y):
    """[summary]
    HELPER-FUNCTION
    calculates the (eulidean) distance between vector x and y.

    Arguments:
        x {[tuple]} -- [vector]
        y {[tuple]} -- [vector]
    """
    assert len(x) == len(y), "The vector must have same length"
    result = ()
    sum = 0
    for i in range(len(x)):
        result += (x[i] -y[i],)
    for component in result:
        sum += component**2
    return math.sqrt(sum)

def nearest_neighbor(x, tSet):
    """[summary]
    Implements the nearest neighbor algorithm

    Arguments:
        x {[tupel]} -- [vector]
        tSet {[dict]} -- [training set]

    Returns:
        [type] -- [result of the AND-function]
    """
    assert isinstance(x, tuple) and isinstance(tSet, dict)
    current_key = ()
    min_d = float('inf')
    for key in tSet:
        d = distance(x, key)
        if d &lt; min_d:
            min_d = d
            current_key = key
    return tSet[current_key]
```

#### 符串解码编码

```
# Implement the encode and decode methods.

def encode(strs):
    """Encodes a list of strings to a single string.
    :type strs: List[str]
    :rtype: str
    """
    res = ''
    for string in strs.split():
        res += str(len(string)) + ":" + string
    return res

def decode(s):
    """Decodes a single string to a list of strings.
    :type s: str
    :rtype: List[str]
    """
    strs = []
    i = 0
    while i &lt; len(s):
        index = s.find(":", i)
        size = int(s[i:index])
        strs.append(s[index+1: index+1+size])
        i = index+1+size
    return strs
```

#### 直方分布

```
def get_histogram(input_list: list) -&gt; dict:
    """
    Get histogram representation
    :param input_list: list with different and unordered values
    :return histogram: dict with histogram of input_list
    """
    # Create dict to store histogram
    histogram = {}
    # For each list value, add one to the respective histogram dict position
    for i in input_list:
        histogram[i] = histogram.get(i, 0) + 1
    return histogram
```

个人感觉这两个仓库里的算法和脚本很齐全，适合做练习，小伙伴们可以试试。

所有算法脚本**已经打包好，获取步骤如下：**

1，点击下方公众号 **数据STUDIO** 名片

2，关注 **数据STUDIO**后，在消息后台回复 **b **或者** d**

**▲点击关注「数据STUDIO」回复<strong><strong><strong>b **</strong></strong></strong>**或者****<strong><strong><strong> d**</strong></strong></strong>

**<strong><strong><strong><strong>另外，@公众号：<strong>数据STUDIO** 还为大家整理和筛选了大量火爆全网的Python数据科学学习资料，全部资料按需自助**免费获取！直接点击👇链接：  **</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>

**<strong><strong><strong><strong>**</strong></strong></strong></strong>
