
--- 
title:  用Python实现开心消消乐小游戏 
tags: []
categories: [] 

---
本文之前发过一次，重新整理了一下在本号再发一次。提到开心消消乐这款小游戏，相信大家都不陌生，其曾在 2015 年获得过玩家最喜爱的移动单机游戏奖，受欢迎程度可见一斑，本文我们使用 Python 来做个简单的消消乐小游戏。

### 实现

消消乐的构成主要包括三部分：游戏主体、计分器、计时器，下面来看一下具体实现。

定义一些常量，比如：窗口宽高、网格行列数等，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ1VXMHR1bFFnc2lhQjk2VkVpY2lhc3djaWNQenFOamUwYVBFaWNNQkU1WlhTQmt6bFYya0J0UlVHZkZ3LzY0MA?x-oss-process=image/format,png">

接着创建一个主窗口，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ0hUYjU0N0NXeFBoUjNMckxrSFBPMWh0d0xQNHRVQjZXR2FsVDVtQ2pGSDBpYUhHZzdwN3I2UVEvNjQw?x-oss-process=image/format,png">

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQzNoaWE2SU9uaWM4Tm9uOWlhTU5zTmlhVzNSQ25ST001cklXT1JjREF3N0FWZ24zdWdQQzJWcGd4VUEvNjQw?x-oss-process=image/format,png">

再接着在窗口中画一个 8 x 8 的网格，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3BIY2VlR25pYmlhb3g5TjFhS1dpY1lvaWJTeXZvbzBESG1tRjdKM3RndWZyYzJzb3ZWNGdubFFpYXVRLzY0MA?x-oss-process=image/format,png">

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3VzaWFVT3o2VjYybm1wYTNHUkJkZjZBRXFPOW1mYWlhc3FpY0VIb0FMa0tYMjFOSndHVENEQmljRkEvNjQw?x-oss-process=image/format,png">

再接着在网格中随机放入各种拼图块，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3pTVW41c2hqNmdPUGtKMFNBVFFHY21UT3JxS0Mzek9ZZ3FJWU5nVEtKM1p1Yk5QY2liN2JqRkEvNjQw?x-oss-process=image/format,png">

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ0VxWUdiclNsYThQM1RGbm5MaWNxaWFETGpldDdFaWI4cERTT0xzOFpUNG9YbUJPNmJ0ejJqalJJUS82NDA?x-oss-process=image/format,png">

再接着加入计分器和计时器，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ25TMktpYjhONUxTWFpIb0FEM0hUc2dwUnFOOHd1aWN6TzNmZ1pIbXZadGljV29oZEx6Y2liQllER3cvNjQw?x-oss-process=image/format,png">

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQzhaSjVnSUVzOEhpYmVuemNuaWNBRHNCbEFYMmIxeUp6T2N4Mnp5a3UzUHloWVRlWmlhSE9lanlGdy82NDA?x-oss-process=image/format,png">

当设置的游戏时间用尽时，我们可以生成一些提示信息，代码如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ2ZpYUZGbWo0OFd5UHVqanZueHc3cVFacWJYUmJJYlUybnBpYUVncDRWVjBPbUt5bW5pY09DcGlhREEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ2xrS3RjTnJrRThSY2xkV0RpY2JOaWI2aWE3VHB0NTRJTVVzVGF2aWFNUUVnaGt1Z3NvVlI0UGpNT0EvNjQw?x-oss-process=image/format,png">

看一下效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3JsdHgwa1NjVllKMExVdUFta3hWMUV1cTdpYzVrYXVDSzFzYzJpYmxIQ0l2NFBNbDlwc255MEN3LzY0MA?x-oss-process=image/format,png">

说完了游戏图形化界面相关的部分，我们再看一下游戏的主要处理逻辑。

我们通过鼠标来操纵拼图块，因此程序需要检查有无拼图块被选中，代码实现如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ2RSS0pLSmVRVHlEUkdpYzViSGVJSnFqY1RzeU8zYVY2RHpjZ3BHZ3VTVWliREQ1RDVwS3RKNHB3LzY0MA?x-oss-process=image/format,png">

我们需要将鼠标连续选择的拼图块进行位置交换，代码实现如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ2licHN3eGV4Zk1od0hwSXkxQWJuaWJacEZjdm9tdDRuWUh2ZVFESzVodzFkdDVPbzloOFY5b2hnLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3B6NWRiUzNnMktmWVZpY2pPazRuaG9LcTFzZlZJUlZudW9qUnV1ZUhYYlBoS3Q5MXk2YWlhY1VBLzY0MA?x-oss-process=image/format,png">

每一次交换拼图块时，我们需要判断是否有连续一样的三个及以上拼图块，代码实现如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ2VaOEQ0YUxIUWZGMUl5aWFtRWU2TVk2RFYwVHRCMGljNnJ5TXI0ZnJCanpWMVJhbkdscWYwUGliZy82NDA?x-oss-process=image/format,png">

当出现三个及以上拼图块时，需要将这些拼图块消除，代码实现如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ0puYU5iVmdnVXJPY1BtQ0lqbVgyZUVjRzJNbUVNYUEycXRoRlNoZ3dZbFFURjh3MWpPZ0xZdy82NDA?x-oss-process=image/format,png">

将匹配的拼图块消除之后，我们还需要随机生成新的拼图块，代码实现如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3E4dUdFTGliZ3pjTXA4TkpHallBcGJjejNPTXJUYzRpYk0ya2xNcmM3aWJEY2RlSWFRZ0xLclVuQS82NDA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQ3E0Q0ppYWJGYmVQdXNlOVN6Q0JVWElKaWNnSFVpY2xyUlZPVkRmSlB0bXNGb2VPRjdpYmVSNzBUTkEvNjQw?x-oss-process=image/format,png">

之后反复执行这个过程，直至耗尽游戏时间，游戏结束。

最后，我们动态看一下游戏效果。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcHo2VHVrbXk5WVFuWDl6VkU0Q1JJQzhHUkg3d1J2eXMwVER6S1JaVm90SnFSZ1pxaWJYQkhEU0drdlhhQlI2T1FwUnAzQThPbEJxZUEvNjQw?x-oss-process=image/format,png">

### 总结

本文我们使用 Python 实现了一个简单的消消乐游戏，有兴趣的可以对游戏做进一步扩展，比如增加关卡等。

源码在公号**Python小二**后台回复**210111**获取。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫描关注，查看更多内容
