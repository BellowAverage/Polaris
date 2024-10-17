
--- 
title:  【已解决】打开IBM出现Rational Lience Key Error错误（Failed to check out a key for rose_enterprise_windows:） 
tags: []
categories: [] 

---
## 问题：

打开IBM后出现下面弹窗 <img src="https://img-blog.csdnimg.cn/f84805235fdd4688b89c76540eae8f7c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_15,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

## 准备工作：

解决此问题需要用到下面4个文件（下载路径一定要记住呀）： <img src="https://img-blog.csdnimg.cn/929f48c64b634dc29c6094f81d7ac32d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 链接： 提取码：lcca

然后把电脑时间改为2019年之前的一个日期。

## 解决办法：

### 一、将license.dat、 lmgrd.exe 、rational.exe三个文件一起复制到：安装目录\common\ 中

<img src="https://img-blog.csdnimg.cn/be891e0135cc4d459c755723b1d313f3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 二、用记事本打开license.dat文件，进行下面操作

在文中大概中间位置找到： SERVER PC ANY DAEMON rational “D:\ProgrammingSoftware\rationalRosessss\Common\rational.exe” <img src="https://img-blog.csdnimg.cn/f5109d6b8cad4c8bbe67693263eb6fa4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

将其修改为： SERVER 计算机名　ANY DAEMON rational “自己安装的目录\rational.exe” <img src="https://img-blog.csdnimg.cn/4290b1d129974e3d85f1bc8255aec6ec.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 注：搜索计算机名 桌面右键此电脑，点击属性，即可查询计算机名称。 <img src="https://img-blog.csdnimg.cn/abf40fd3ba5a479b8426f41fbb982a50.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 路径复制可用如下简单方式： 先打开common文件夹，然后右键路径中的common，选择复制地址。 <img src="https://img-blog.csdnimg.cn/886d18c30ec9482fa6b4aa52b2e71770.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/42f3ac7628824a93ad8bdbdac245887c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

### 三、将 flexlm.cpl复制到C盘 windows/SysWOW64 下，直接双击打开它

<img src="https://img-blog.csdnimg.cn/3f505dff9e5940c78d3b152b43797221.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 四、在Setup中点击Browse选中复制到common中的lmgrd.exe文件与license.dat文件路径

<img src="https://img-blog.csdnimg.cn/7f532a1ebb0044e4a5321878e47bec6b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 五、回到Control进行操作

点击Start，若出现：Server Started 则表示已经成功！ <img src="https://img-blog.csdnimg.cn/2ee7314fd3854c639d765e43a7fe9932.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 此时，点击Status，若出现：**计算机名：license server UP(MASTER)** 则代表成功！ <img src="https://img-blog.csdnimg.cn/b34fc1cfdde14c5fb39a5736dddc8179.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述"> 确认没问题后，点击确定

### 六、打开IBM Rational License Key Administrator导入刚刚获取的证书

<img src="https://img-blog.csdnimg.cn/1e337a3eadd24b30af3b256f84a45c53.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/ca2ce27751294435983911ce515d79fe.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 七、在Server Name中填写自己电脑名字，点击完成

<img src="https://img-blog.csdnimg.cn/5f798d5b1bce4dabb5f2a6295efcaf87.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

### 八、关闭窗口，打开IBM Rational Rose Enterprise Edition

<img src="https://img-blog.csdnimg.cn/db853cf42afb420383721cea7dbba1a9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_12,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 出现如下界面证明配置成功，可以正常使用啦！ <img src="https://img-blog.csdnimg.cn/de00f61bac1e408e98d66c0ea1c1c061.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5L-X5Lq6TGF5bWFu,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center" alt="在这里插入图片描述">

完结撒花！！！
