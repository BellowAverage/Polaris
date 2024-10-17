
--- 
title:  第六章 AXU3EGB开发板部署 
tags: []
categories: [] 

---
至第五章，我们部署所需要的文件材料以及环境都准备齐全，开始进行部署工作。

### 开发板部署流程

>  
 流程一共4步。 


需要的材料有：部署需要训练之后的模型权重文件（.h5）、Xilinx Vitis-AI Docker环境、Xilinx Runtime Docker环境。如图18所示：

<img alt="" height="383" src="https://img-blog.csdnimg.cn/direct/1e8fc970a6ee4bcab14ef1c9ea35956b.png" width="544">

图18

#### 第一步：h5-convert-to-pb（本步骤在PC端进行）

<img alt="" height="83" src="https://img-blog.csdnimg.cn/direct/942655d6eff94711bba89ec70e01b79b.png" width="278">

建议新创建一个新的虚拟环境，环境版本如下：

>  
 Python==3.7.6 
 Keras==2.11.0 
 Tensorflow==1.14.0 


在PC端，进入yolov3-keras项目文件夹中，打开yolov3-keras\keras-yolo3-convert2pb\keras2pb.py，如图19所示：

<img alt="" height="311" src="https://img-blog.csdnimg.cn/direct/e63f550a84264f3fafc503d6c7ba0f61.png" width="541">

图19

运行以下命令：

```
python keras2pb.py --input_model=”你的训练权重.h5文件绝对路径” --output_model=”输出.pb文件的绝对路径”
```

得到的.pb文件（该文件在后文中将成为yolov3.pb）如下所示：

<img alt="" height="194" src="https://img-blog.csdnimg.cn/direct/87e6c7c3945d4ddbaef61de7b0ee43d6.png" width="187">

图20



#### 第二步：网络参数的量化校准（Quantization）（本步骤在虚拟机上进行）

<img alt="" height="103" src="https://img-blog.csdnimg.cn/direct/fad303dd846943739b9ea75439a51cf6.png" width="200">

##### **2.1网络结果可视化工具Netron以及打开网络结构图**

安装网络结构可视化工具Netron。命令如下：

```
User:$ sudo apt-get install snapd

User:$ sudo apt-get install snapcraft

User:$ sudo snap install netron
```

三行命令执行完之后，不出意外的情况下Netron工具成功安装好了。



接下来，我们要处理yolov3.pb文件了。

首先，在虚拟机的Vitis-AI-master/AXU3EG/Project/VItis-AI-envirment/Vitis-AI-master/Compile_Tools路径下新建一个你的文件夹（后文中称为voc20），在该文件夹下新建如图21中打钩的文件夹，其他文件先不用管。

<img alt="" height="207" src="https://img-blog.csdnimg.cn/direct/9dd54a4a8769421ba05b84d17ef8494a.png" width="389">

图21

然后，将在PC端转换好的yolov3.pb文件存到虚拟机上述路径下，即存在我们新建的pb_file文件夹中。

<img alt="" height="124" src="https://img-blog.csdnimg.cn/direct/0b8e74a0da7a4972bae073c0a9148b16.png" width="187">

图22

最后，在该路径下打开terminal，执行如下命令：

```
User:$ netron float/yolov3.pb
```

随后，会出现图23的网络结构界面，将此界面保留不要关闭，后续步骤中会使用到。

<img alt="" height="247" src="https://img-blog.csdnimg.cn/direct/cda7e12f4ff048eca022e8a8d510cd60.png" width="189">

图23

##### **2.2执行网络参数量化**

在网络参数量化前，我们需要在Vitis-AI-master/AXU3EG/Project/VItis-AI-envirment/Vitis-AI-master/Compile_Tools路径下新建这三个.txt文件。分别命名为classes_voc20.txt、voc20_test.txt和yolo_anchors_voc20.txt。

<img alt="" height="121" src="https://img-blog.csdnimg.cn/direct/ea243ad119044dcfae805b22f8d98d2c.png" width="175">

图24



###### （1）classes_voc20.txt

该文本文件存放的是检测的类别，在我的例子中voc2012数据集的标签有20个，如图25所示：

<img alt="" height="196" src="https://img-blog.csdnimg.cn/direct/bdae11997d2a40c8b1f81373e93692a1.png" width="347">

图25

###### （2）voc20_test.txt

该文本文件存放的是校准测试数据集的图片名称，我使用的是coco测试数据集中的前1000张图片，如下图所示：

<img alt="" height="314" src="https://img-blog.csdnimg.cn/direct/fc8b847e6f0f4ea59c39317b0cab93b7.png" width="254">

图26

###### （3）yolo_anchors_voc20.txt

该文本文件存放的是yolov3模型三个不同大小尺寸的anchor，使用脚本是可以算出你的训练集适合用哪个大小的anchors，请自行计算按照图27格式填入即可：

<img alt="" height="105" src="https://img-blog.csdnimg.cn/direct/069a0ecce1a947bbb18e684e61948053.png" width="442">

图27

准备完以上步骤后就可以开始网络参数化的步骤啦。





首先，根据第三章（Xilinx Vitis-AI Docker安装）启动Vitis-AI Docker，输入如下命令激活vitis-ai-tensorflow虚拟环境：

```
vitis-ai-docker:$ conda activate vitis-ai-tensorflow
```

<img alt="" height="163" src="https://img-blog.csdnimg.cn/direct/1128cf8ca3d34ee48ad02ad9d5cb6185.png" width="251">

图28

其次，我们需要准备一套校准测试数据集来进行校准，在我的例子中是使用coco数据集中test数据集的前1000张图片（一般使用100到1000张即可），我将其存放在2.1小节提到的Vitis-AI-master/AXU3EG/Project/VItis-AI-envirment/Vitis-AI-master/Compile_Tools路径下的JPEGImages的文件夹中。如下图所示：

<img alt="" height="193" src="https://img-blog.csdnimg.cn/direct/19ac5f3818234c62a9c942c608162918.png" width="218">

图29

然后，我们返回到Vitis-AI-master/Compile_Tools路径下，使用编辑器打开脚本1_tf_quantize.sh。如图30，我们需要根据2.1小节中打开的网络结构图、项目标题（我的是voc20）以及你自定义的.pb文件名字，替换脚本中的红框位置。

<img alt="" height="371" src="https://img-blog.csdnimg.cn/direct/555a5a92e6df4486b955f30232f053ef.png" width="345">

图30

其中，INPUT_NODES为输入节点的名字，如下图的位置：

<img alt="" height="129" src="https://img-blog.csdnimg.cn/direct/bb7632e1568e4fdf9558c1e533c9e6e5.png" width="303">

图31

OUTPUT_NODES为输出节点的名字，yolov3模型中默认三个输出节点，所以你需要在你的网络结构图中找到你的三个输出节点，分别的在下图的例子位置中找到它们的名字：

<img alt="" height="190" src="https://img-blog.csdnimg.cn/direct/e06cd24632f5425d9d5ca7aea38f74cd.png" width="287">

图32

最后，在Vitis-AI-master/Compile_Tools路径下打开terminal，运行如下命令进行量化操作：

```
(vitis-ai-tensorflow) docker:$ source 1_tf_quantize.sh
```

<img alt="" height="87" src="https://img-blog.csdnimg.cn/direct/3943b12574b749c0970e1ca5c08881ac.png" width="459">

图33

随后，在Vitis-AI-master/Compile_Tools/modle/voc20项目路径下会自动生成名为vai_q_output的文件夹，里面存放的文件如下图所示：

<img alt="" height="112" src="https://img-blog.csdnimg.cn/direct/82b22d5124ac4949b37013a5c8000e7f.png" width="293">

图34



#### 第三步：DPU Kernel编译

<img alt="" height="161" src="https://img-blog.csdnimg.cn/direct/39e39a30688244f2830f4be0278e03a8.png" width="173">

（1）首先，检查在

Vitis-AI-master/Compile_Tools/hardware/AXU3EG_DPU_B1600文件夹下是否存在.pcf和.json文件：

<img alt="" height="134" src="https://img-blog.csdnimg.cn/direct/4d39bd2e1a394d35bfcc9ff0073f8d4c.png" width="214">

图35

       使用编辑器打开检查.json文件中的路径是否正确：

<img alt="" height="84" src="https://img-blog.csdnimg.cn/direct/e63b2f1f534b4205ba8a65f4d5064a11.png" width="368">

图36

（2）然后，在Vitis-AI-master/Compile_Tools路径下使用编辑器打开2_vai_compile.sh，替换下图红框处的项目名称：

<img alt="" height="225" src="https://img-blog.csdnimg.cn/direct/8b208e31b45b44e894de4eeb1e9f11be.png" width="301">

图37

随后，在该路径下打开terminal，运行如下命令：

```
(vitis-ai-tensorflow) docker:$ source 2_vai_compile.sh
```

在命令执行完毕后会打印DPU Kernel的相关信息（如图38），并在voc20项目文件夹下自动生成一个名为vai_c_output_AXU3EG_DPU_B1600的文件夹：

<img alt="" height="251" src="https://img-blog.csdnimg.cn/direct/0ba6bbcc241044de9a4c172e8268a5bb.png" width="211">

图38

<img alt="" height="185" src="https://img-blog.csdnimg.cn/direct/fd51d2e27cd54892bab0ff2d5f36f0cf.png" width="414">

图39

（3）我们需要启动Xilinx Runtime Docker（启动方法根据第四章Xilinx Runtime docker安装，<u>安装命令</u>即为<u>启动命令</u>）。

       然后，根据下图红框处替换你的项目名称：

<img alt="" height="458" src="https://img-blog.csdnimg.cn/direct/f8ac18f8e06a4f9ea2b758bf9ac4ccc6.png" width="382">

图40

最后，进入Vitis-AI-master/Compile_Tools路径下，执行下面的命令进行交叉编译：

```
runtime-docker:$ source 3_lib_compiler_runtime.sh
```

在voc20项目文件夹下的vai_c_output_AXU3EG_DPU_B1600文件夹中会自动生成.so文件：

<img alt="" height="119" src="https://img-blog.csdnimg.cn/direct/ebd4898e7c9146e2ab1a9d9175bd5e8f.png" width="154">

图41

#### 第四步：开发板部署

<img alt="" height="152" src="https://img-blog.csdnimg.cn/direct/85d5da60a30246708f3847cef2ca7583.png" width="365">

##### **4.1配置文件的准备**

###### 4.1.1 Xftp工具的连接

将开发板连接键盘、鼠标和显示器，点击主界面中terminal，使用以下命令查看开发板的IP地址并记录下来：

```
ifconfig
```



图42

在PC端上打开Xshell工具，新建会话窗口，名称可以自定义，主机IP地址输入开发板的IP地址，端口号默认为22。点击连接，用户名和密码默认为root。

<img alt="" height="299" id="图片_x0020_8" src="https://img-home.csdnimg.cn/images/20230724024159.png?origin_url=file%3A%2F%2F%2FC%3A%2FUsers%2FNanMao%2FAppData%2FLocal%2FTemp%2Fmsohtmlclip1%2F01%2Fclip_image029.png&amp;pos_id=Za0IT5Uo" width="534">

图43

Xshell工具连接成功后，点击Xftp快捷启动按钮进入开发板的文件管理界面：

<img alt="" height="299" id="图片_x0020_42" src="https://img-home.csdnimg.cn/images/20230724024159.png?origin_url=file%3A%2F%2F%2FC%3A%2FUsers%2FNanMao%2FAppData%2FLocal%2FTemp%2Fmsohtmlclip1%2F01%2Fclip_image030.png&amp;pos_id=1RW2PuKG" width="534">

图44

###### 4.1.2 项目文件夹的准备

新建一个项目名称命名的项目文件夹：tf_yolov3_xxx_deploy。在下文中我以tf_yolov3_voc20_deploy项目为例。

<img alt="" height="144" src="https://img-blog.csdnimg.cn/direct/ab637354061d427fb4dfa3e03130961a.png" width="250">

图45

在tf_yolov3_voc20_deploy项目文件夹添加图46中的文件夹和文件。其中：

（1）libdpumodeltf_yolov3_voc20.so是在上文第三步DPU Kernel编译之后得到的文件，将其拷贝至项目文件夹中。

（2）tf_yolov3_voc20_pic.py和tf_yolov3_voc20_cam.py脚本文件可以从开发板中给的其他例子中拷贝过来，并以项目的名字命名tf_yolov3_xxx_pic.py，如：tf_yolov3_voc20_pic.py。

（3）modellib文件夹也可以从开发板中给的其他例子中拷贝过来，里面的内容不需要修改。

<img alt="" height="115" src="https://img-blog.csdnimg.cn/direct/07ad376b6aae4a0cac74707b3ca05e4d.png" width="414">

图46


<td style="border-color:#000000;width:207.4pt;"> **文件名** </td><td style="border-color:#000000;width:207.4pt;"> **功能** </td>

**功能**
<td style="border-color:#000000;width:207.4pt;"> modellib </td><td style="width:207.4pt;"> dnndk通用依赖库文件夹 </td>

dnndk通用依赖库文件夹
<td style="border-color:#000000;width:207.4pt;"> model_data </td><td style="width:207.4pt;"> Anchor与classes参数文件夹 </td>

Anchor与classes参数文件夹
<td style="border-color:#000000;width:207.4pt;"> output_result </td><td style="width:207.4pt;"> 存放运行yolov3推断后的输出结果 </td>

存放运行yolov3推断后的输出结果
<td style="border-color:#000000;width:207.4pt;"> test_sample </td><td style="width:207.4pt;"> 存放测试图片的文件夹 </td>

存放测试图片的文件夹
<td style="border-color:#000000;width:207.4pt;"> libdpumodeltf_yolov3_voc20.so </td><td style="width:207.4pt;"> 动态链接库，与python应用程序必须在同一个目录 </td>

动态链接库，与python应用程序必须在同一个目录
<td style="border-color:#000000;width:207.4pt;"> tf_yolov3_voc20_pic.py </td><td style="width:207.4pt;"> 运行yolov3的主应用程序（图片输入版本） </td>

运行yolov3的主应用程序（图片输入版本）
<td style="border-color:#000000;width:207.4pt;"> tf_yolov3_voc20_cam.py </td><td style="width:207.4pt;"> 运行yolov3的主应用程序（USB摄像头输入版本） </td>

运行yolov3的主应用程序（USB摄像头输入版本）

##### **4.2数据集的准备**

###### （1）model_data文件夹

在PC端的Vitis-AI-master/AXU3EG/Project/VItis-AI-envirment/Vitis-AI-master/Compile_Tools路径下，将classes_voc20.txt和yolo_anchors_voc20.txt拷贝至开发板的model_data文件夹中。

###### （2）test_sample文件夹

该文件夹存放的是你将要推理的图片文件。在我的例子中还是使用coco测试数据集中的前1000张图片。

在test_sample文件夹下新建一个名为coco的文件夹，将这1000张图片存放到coco文件夹中。

注意：建议在拷贝过去之前，将图片的文件名字按照下图的规则命名！

<img alt="" height="311" src="https://img-blog.csdnimg.cn/direct/721f24799df948188a5b6ba22cbad584.png" width="304">

图47

##### **4.3 执行脚本的准备（tf_yolov3_voc20_pic.py）**

在本说明书中，我只介绍使用图片推理的脚本例子（tf_yolov3_voc20_pic.py），摄像头的例子请各位自行摸索。

（1）我们需要注意TEST_SET为数据集的文件夹名称，我创建的文件夹叫coco，所以列表中我填写的是coco；

（2）INPUT_IMAGE_PATH是coco文件夹的上一级文件夹路径，这里如果你按照我规则创建的文件夹名称和路径的话，是不需要更改的；

（3）OBJECT_TPYE是项目名称，我的例子叫“voc20”；

（4）CLASSES_PATH和ANCHORS_PATH为model_data文件夹中的文件路径，如果你按照我的创建规则，也是不需要更改这个路径的。

<img alt="" height="159" src="https://img-blog.csdnimg.cn/direct/9e1bdcff13484103bd93df21c5fda0cb.png" width="419">

图48

其次，图49中要修改的地方还有CONV_INPUT_NODE、CONV_OUTPUT_NODE1、2和3。这里的名字是根据DPU Kernel编译的输出结果中可以找到的（图50）

<img alt="" height="154" src="https://img-blog.csdnimg.cn/direct/2eec1f8dcf184a0fb66ac2431d4e6bef.png" width="296">

图49

<img alt="" height="207" src="https://img-blog.csdnimg.cn/direct/9860607053c14d74b0428bdc41388db8.png" width="348">

图50

执行完以上的修改替换操作后，就可以给开发板接上鼠标、键盘和显示器进行下一步的测试了！！

##### **4.4 测试**

测试前，需要将开发板的键盘、鼠标和显示器连接上（测试必须在显示器上测试）。

（1）开发板通上电源后，等待主界面显示；

（2）单击启动主界面上的terminal；

（3）使用命令行检查主路径下是否存在我们准备好的项目文件夹以及所需要的文件，根据以下表格进行检查；
<td style="border-color:#000000;width:207.4pt;"> **文件名** </td><td style="border-color:#000000;width:207.4pt;"> **功能** </td>

**功能**
<td style="border-color:#000000;width:207.4pt;"> modellib --- dputils.cpp --- dputils.h --- dputils.py </td><td style="width:207.4pt;"> dnndk通用依赖库文件夹 </td>

--- dputils.cpp

--- dputils.py
<td style="border-color:#000000;width:207.4pt;"> model_data --- classes_voc20.txt --- yolo_anchors_voc20.txt </td><td style="width:207.4pt;"> Anchor与classes参数文件夹 </td>

--- classes_voc20.txt

Anchor与classes参数文件夹
<td style="border-color:#000000;width:207.4pt;"> output_result </td><td style="width:207.4pt;"> 存放运行yolov3推断后的输出结果 </td>

存放运行yolov3推断后的输出结果
<td style="border-color:#000000;width:207.4pt;"> test_sample --- coco ------ 00001.jpg ------ 00002.jpg ------ 00003.jpg ------ 00004.jpg ------ …… </td><td style="width:207.4pt;"> 存放测试图片的文件夹 </td>

--- coco

------ 00002.jpg

------ 00004.jpg

存放测试图片的文件夹
<td style="border-color:#000000;width:207.4pt;"> libdpumodeltf_yolov3_voc20.so </td><td style="width:207.4pt;"> 动态链接库，与python应用程序必须在同一个目录 </td>

动态链接库，与python应用程序必须在同一个目录
<td style="border-color:#000000;width:207.4pt;"> tf_yolov3_voc20_pic.py </td><td style="width:207.4pt;"> 运行yolov3的主应用程序（图片输入版本） </td>

运行yolov3的主应用程序（图片输入版本）
<td style="border-color:#000000;width:207.4pt;"> tf_yolov3_voc20_cam.py </td><td style="width:207.4pt;"> 运行yolov3的主应用程序（USB摄像头输入版本） </td>

运行yolov3的主应用程序（USB摄像头输入版本）

（4）使用命令行进入到项目文件夹路径下，我的例子是：tf_yolov3_voc20_deploy，使用的命令如下：

```
cd tf_yolov3_voc20_deploy
```

（5）使用以下命令执行推理测试，我的例子中，图片推理文件为tf_yolov3_voc20_pic.py，需要执行一下命令：

```
python3 tf_yolov3_voc20_pic.py
```

（6）等待几秒，若显示器显示自动推理的过程，则表示测试成功！！！

今天不学习，明天变垃圾！！！
