
--- 
title:  第一章 AXU3EBG开发板系统安装 
tags: []
categories: [] 

---
### 一、开发板驱动安装

（1）连接开发板后，在计算机管理界面的端口列表中会显示一个新设备。（下图是我已经安装步骤2驱动软件后的显示名称）

<img alt="" height="571" src="https://img-blog.csdnimg.cn/direct/5e8cea22900148e48fb0f76038d84580.jpeg" width="795">

图1 计算机管理界面截图

（2）接下来需要安装驱动软件（附件1 CP2102 USB转串口驱动程序.zip），双击.exe文件进行驱动安装（64位电脑系统选择x64，32位电脑系统选择x86）。安装后会显示设备COM3。

<img alt="" height="506" src="https://img-blog.csdnimg.cn/direct/113f3ac591644636949689f2e3a76e62.png" width="877">

图2 CP2102 USB转串口驱动程序文件夹截图

### 二、开发板Petalinux系统镜像烧录

#### **1. BalenaEtcher工具下载**

搜索BalenaEtcher进入官网，点击下载。

<img alt="" height="374" src="https://img-blog.csdnimg.cn/direct/6624301611054a59a2577bc7fda6a9e5.png" width="473">

图3 BalenaEtcher进入官网截图

#### **2. 开发板镜像系统烧录**

打开BalenaEtcher。

首先，点击“从文件烧录”，选择sd_card.img（附件2 SD_card.zip）；

 链接：https://pan.baidu.com/s/1VEG0nFxXQmw6in1Mh2WYvA  提取码：fpga  复制这段内容打开「百度网盘APP 即可获取」

其次，点击 “选择目标磁盘”，选择你连接在本地主机（以下简称“**PC****端**”）上的sd卡；

最后，点击“现在烧录！”。

等待提示烧录成功。

<img alt="" height="336" src="https://img-blog.csdnimg.cn/direct/495256d0e5ee44f3b01279f0e37eb6cf.png" width="533">

图4 BalenaEtcher界面截图

#### **3. 开发板DNNDK工具安装**

首先，将烧录好镜像系统的sd插到开发板上，连接好键盘、鼠标、显示器和网线，并通上开发板的电源；

其次，打开开发板端terminal，使用ifconfig命令查看开发板的ip地址，显示如图5所示。命令如下：

```
sh-5.0# ifconfig
```

<img alt="" height="248" src="https://img-blog.csdnimg.cn/direct/cca27e84759b4a1eaaedb65bbecd521c.png" width="499">

图5 开发板端terminal截图

再次，打开PC端的Xshell软件进行连接，主机地址对应开发板的inet addr:192.168.1.156。随后打开Xftp连接开发板，并将Alinx_DNN文件夹（附件3 Alinx_DNN.zip）复制到开发板上，文件夹中文件用于下一步测试环节中。

最后，在Xshell连接上开发板后，进入到Alinx_DNN文件夹路径下，找到DNNDK压缩包，解压并安装，命令步骤如下：

```
(ALINX-BOARD) sh-5.0# cd Alinx_DNN

(ALINX-BOARD) sh-5.0# tar -xzvf vitis-ai_v1.2_dnndk.tar.gz

(ALINX-BOARD) sh-5.0# cd vitis-ai_v1.2_dnndk

(ALINX-BOARD) sh-5.0# ./install.sh
```

#### **4. 开发板运行测试（整个过程需要连接键盘鼠标显示器）**

以车辆检测为例（tf_yolov3_vehicle_deploy）

首先，检查Alinux_DNN\tf_yolov3_vehicle_deploy文件夹路径下文件是否完全，如图6；

<img alt="" height="256" src="https://img-blog.csdnimg.cn/direct/08d86a9a8cec4b43bb4c0faaed38d99d.png" width="656">

图6 

其次，在开发板terminal中进入到Alinux_DNN\tf_yolov3_vehicle_deploy文件夹路径下，并运行图片（或摄像头）版本，推断完成后会自动保存在路径output_result/中；

①图片组输入版本

```
(AXU3EG) sh-5.0# python3 tf_yolov3_voc_pic.py
```

②摄像头输入版本

```
(AXU3EG) sh-5.0# python3 tf_yolov3_voc_cam.py
```

注：使用S键在本地目录保存截图并退出。直接退出使用ESC键。

<img alt="" height="348" src="https://img-blog.csdnimg.cn/direct/358a39f0bcdd4bdcb09125f409d55c2c.png" width="622">

图7

最后，检查路径output_result/中是否保存了检测之后的结果，如果有结果说明开发板系统安装完成！！

今天不学习，明天变垃圾！！！
