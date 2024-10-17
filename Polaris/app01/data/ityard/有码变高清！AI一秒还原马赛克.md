
--- 
title:  有码变高清！AI一秒还原马赛克 
tags: []
categories: [] 

---
像素不够，后期修图来凑？

在知乎搜索低像素修图，结果求助帖多到刷不完，而且从PS技巧、插件神器到各类修图App教程多到眼花缭乱，重点是效果不知道会怎么样。

不过，近日杜克大学（Duke University）研究团队开发了一款AI修图黑科技PULSE，可以解决所有低像素烦恼。据说它能够将图像原始分辨率放大64倍，任何渣画质都可以秒变高清、逼真图像，甚至被打了马赛克的人脸图像，毛孔、皱纹，头发也都能被清晰还原。

1

**马赛克秒变高清人像**

PULSE是一种新型超分辨率算法，它通过潜在空间探索对照片采样，可以将16x16像素的低分辨率（Low Resolution，简称LR）放大到1024x1024像素的高分辨率（High Resolution，简称HR），在几秒内增加了64倍，而传统方法最多只能放大8倍。

先来看一组示例，修图界最难处理的LR大头照，经过PULSE也可以秒变高清、细腻的图像。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1JHd0lwcUd2SzBscVZjVFFUaWI4cWdoaWF2U1htMXF3bzlpY3pIbWljckdweWhxdEN4cFRpYzJtVUFidy82NDA?x-oss-process=image/format,png">

更重要的是，PULSE可以定位面部的关键特征，以更高分辨率生成一组类似的细节。图中尽管头像被打上了马赛克，PULSE也可以自行“想象”出诸如眉毛、睫毛、头发、脸型等面部细节，形成高清、逼真人像。

不过，过度虚化产生的人像只是一种虚拟的新面孔，事实上它并不存在。正因如此，这项技术不能用于身份识别。比如监控摄像头拍摄的失焦、无法辨别的图片，不能通过PULSE还原成真实存在的人像。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1JqU3ppY1pTRjdIUmFacXVKZzhMRkZvWXhkTjdmWVhibmREMG40b1loaWNBWDJySGZkeFhyR2gzZy82NDA?x-oss-process=image/format,png">

一位杜克大学研究小组的计算机科学家Cynthia Rudin说“此前从来没有如此超高分辨率的图像被制作出来，它能够产生不存在的新面孔，而且看起来很真实”。

同时，她补充到，这项研究所采取的技术可以广泛应用于医学、显微镜、天文学，以及卫星图像等领域。另外，该研究团队已将论文已经发表至预印论文库arVix，同时被IEEE国际计算机视觉与模式识别会议（CVPR 2020）收录。

2

**“缩减损失”，超越常规修图法**

对于一个LR图像，传统将HR分辨率部分匹配给LR图像而获取超高分辨率（SR）的方式，往往会导致HR图像出现感光度差、不平滑，画面失真的情况。

在本次研究中，杜克大学研究团队开拓了一种新思路，提出新型超分辨率算法PULSE，它不是遍历LR图像来慢慢添加细节，而是发现与HR相对应的LR，通过“缩减损失”的方式得到SR图像。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1JDOHAyOWZVWld1TjR3bkVtU0dGNTRhWVhveExnMWduNHJFbzJmbE1XQzJ1REFmZHRpYWsxcGd3LzY0MA?x-oss-process=image/format,png">

原始LR(第一行),PULSE输出HR（中间行）,HR对应的LR(最后一行)

PULSE使用了生成对抗网络（GAN），它是一种训练模型，顾名思义，通过对抗博弈的方式来进行目标训练。其主要结构包括一个生成器（Generator）和一个鉴别器（Discriminator），在同一组照片训练中，一个负责训练接收到的图像并输出，一个负责接收该输出，并检验其是否足够逼真。

以下是与原图对比后的试验结果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1J1U1U5dzg2djRYZEJpY1RCMlk1bFpPRXJocXI3UkFVa2ljOGF5bWEzSmRaRWZkTWlibXY2aWFqZ1lBLzY0MA?x-oss-process=image/format,png">

图中，第一行为原图，第二行为通过“缩减损失”得到的HR所对应的LR，而第三行经过PULSE得到的HR，可以看出，尽管与原图还存在细微的差别，但还原度已经非常高。

论文中表明，为了检验PULSE在SR方面的优势，杜克大学研究团队采用4种不同的图像缩放方法与其进行了比较研究。本次研究利用CelebA HQ数据集中的1440张图像，以x8，x64的比例因子，对LR面部图像，尤其是眼部、唇部以及头发等细节之处进行了试验。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1I2YXYwOHVIZjZOc2pLZldHUnlLSE5oWURUaWEzdTRWY21jb1p2SjRNVTRCWkVhenhDbnRlZkpnLzY0MA?x-oss-process=image/format,png">

PULSE呈现出了明显的优势，尤其是在X64分辨率下，模糊头像被完全还原，尤其是在眼唇等细节之处，其他方法几乎达不到这样的效果。

另外，针对测试结果，研究人员采用感知超分辨率常见的MOS测试方式，邀请五位评分者对图像结果进行了1-5的打分，结果显示，HR源高清图像分辨率得分为3.74，而PULSE达到了3.60，仅差0.14，可以说几乎达到了真实的高质量图像的水平。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9ZamhtYmJrZFY2dTBLcjdTaWJOYzRoTGhTeDZyakFOc1JBVnR4aWNWcGFGc0RpYUJLSDBFRUUxYzMwTFd4cFV1NDNJcngxSTNVRVZsUHhjWVdvWVFXbUlEdy82NDA?x-oss-process=image/format,png">

不过，研究人员也承认PULSE还不是很完美。它产生的高分辨率图像与专业原图像相比还有一定的差别。但随着技术和工具的改进，这项技术会被一点点的完善。

现在研究团队已经将PULSE发布到Github开源平台，而且收割了569科颗星星。有修图烦恼的朋友可以安装体验一下~（Github地址：https://github.com/adamian98/pulse）

引用链接：
- http://pulse.cs.duke.edu/- https://www.gizmodo.co.uk/2020/06/researchers-have-created-a-tool-that-can-perfectly-depixelate-faces/- https://www.rt.com/news/492091-ai-tech-undo-pixelation/
>  
  作者 | 贝爽 
  转自：雷锋网（**leiphone-sz**） 
  论文地址：**https://urlify.cn/ABJRFf** 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
