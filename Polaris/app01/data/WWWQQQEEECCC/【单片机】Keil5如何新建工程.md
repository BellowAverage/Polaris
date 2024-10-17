
--- 
title:  【单片机】Keil5如何新建工程 
tags: []
categories: [] 

---
>  
 ✌ 作者简介：神奇的汪同学，一名在读的电子信息工程专业大学生. 📑 个人主页： 📫 如果文章知识点有错误的地方，请指正！和大家一起学习，一起进步👀 🔥 如果感觉博主的文章还不错的话，还请不吝👍关注、点赞、收藏三连支持👍一下博主哦！ 


## 新建工程

在桌面新建一个文件夹（总文件夹），命名可以随意 如：**Keil Project**。 <img src="https://img-blog.csdnimg.cn/bd9c79efa3004c169a09d7c43e057c79.bmp#pic_center" alt="在这里插入图片描述"> 然后双击打开Keil5，点击**Project**。 <img src="https://img-blog.csdnimg.cn/04015deb0cbd48108b5be1989c957d07.bmp#pic_center" alt="在这里插入图片描述">然后再点**New Project**。 <img src="https://img-blog.csdnimg.cn/9145fdd658ef4327843fe77a2bbfff8a.png#pic_center" alt="在这里插入图片描述"> 在桌面选择刚刚新建的文件夹**Keil Project**。 <img src="https://img-blog.csdnimg.cn/887131cc09a5468ea145953f4b2fa070.bmp#pic_center" alt="在这里插入图片描述">右击新建文件夹即，项目文件夹名称： **点亮一个LED**。 <img src="https://img-blog.csdnimg.cn/ebe3c095c1764dfaa39cf7ebed71b1bd.png#pic_center" alt="在这里插入图片描述"> 点击刚刚新建的 **点亮一个LED**文件夹。<img src="https://img-blog.csdnimg.cn/7cd503cd613146eb8103b2933fb8a753.bmp#pic_center" alt="在这里插入图片描述"> 选择刚刚新建的**点亮一个LED文件夹**，**填Project**，然后点击保存。 <img src="https://img-blog.csdnimg.cn/94b5a0486b2e474d8519f27fc94bc574.bmp#pic_center" alt="在这里插入图片描述"> 然后选择 **STC MCU**。 <img src="https://img-blog.csdnimg.cn/2b30ead685d44450823f3daf80c9e17b.png#pic_center" alt="在这里插入图片描述"> 在下面的搜索框搜索**STC89C52RC**，选择**STC89C52RC**，点击OK。**（这里是选择芯片的型号）** <img src="https://img-blog.csdnimg.cn/b9ebb8fc13ba4d1491553eb39bc278fb.bmp#pic_center" alt="在这里插入图片描述"> 在 **Source Group1** 上面右击 ，然后点击**Add New Item to Group**。 <img src="https://img-blog.csdnimg.cn/71c02eb65a774b1aa0ce8273aa62a653.png" alt="请添加图片描述"> 选择**C文件**，下面填 **main**。 <img src="https://img-blog.csdnimg.cn/2dc9a4a8f25445aa80d5f2e8afeee808.png#pic_center" alt="在这里插入图片描述"> 把基本框架敲进去，**Ctrl+S保存**。 <img src="https://img-blog.csdnimg.cn/f8d4d6cb11c4445b8fef47446c888cbf.bmp#pic_center" alt="在这里插入图片描述">

要把代码植入(烧录)单片机里肯定不是只有C文件那么简单，我们需要点击左上角的类似魔法棒的图案，在弹出的界面上**选择Output**，勾选**Create HEX File，点击OK** <img src="https://img-blog.csdnimg.cn/933b9c2bd36f469aa2e10a07b17d66ac.bmp#pic_center" alt="在这里插入图片描述">**再次编译，并保存** <img src="https://img-blog.csdnimg.cn/b9159676719846248d40fc00068dbd6e.bmp#pic_center" alt="在这里插入图片描述"> 这个hex文件就是我们所需的文件，**在51开发板上烧录代码时需要用对应的软件把hex下载进单片机里，这里不涉及该方面内容。** <img src="https://img-blog.csdnimg.cn/59bfaf1e14b248ac9bf2ffc3ac60362c.bmp#pic_center" alt="在这里插入图片描述">

如果觉得博主的这篇文章不错的话麻烦给博主一个三连。你的三连就是对我最大的支持。这句话感觉好耳熟啊(doge)
