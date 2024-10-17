
--- 
title:  detecrton2、detectron+win10——个人配置经验 
tags: []
categories: [] 

---
主要参考博客：

配置时间：2021.11.12 以下是我亲测有效的使用 RTX 3060 的各部分安装版本 电脑系统：window 10 python版本：3.6.13 pytorch版本：1.8.0 CUDA版本：11.2 cuDNN版本：8.2.0.53

以下是我个人安装教程，仅供参考，如果出现新问题我恐怕可不能解决，谨慎参考，大神请随意~ 

#### 文章目录
- - - - - - - - 


## 第一步：安装NVIDIA显卡驱动、安装vs2019

关于 **NVIDIA显卡驱动**、**安装vs2019** 可以参考我之前的博客： 或者文章一开始提到的教程;

## 第二步：新建环境

1、打开anaconda prompt <img src="https://img-blog.csdnimg.cn/7b759070c1164f37814d62c1b676e533.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_17,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

2、命令行输入：`conda create --name detecrton2 python=3.6` python_gpu为anaconda下虚拟环境名称，可自定义，python=3.6为选择安装的python版本。

3、如果要启用创建的环境，输入指令：`conda activate detecrton2` 关闭该环境的话，输入指令：`conda deactivate detecrton2`

## 第三步：安装cocoapi（windows）

下载以下链接的cocoapi，因为cocoapi官方暂不支持Windows 下载地址：https://github.com/philferriere/cocoapi 然后用以下指令安装

```
cd coco/PythonAPI
python setup.py build_ext --inplace
python setup.py build_ext install

```

打开cmd输入

```
import pycocotools;
from pycocotools.coco import COCO

```

若安装提示缺失包，自行pip一下 <img src="https://img-blog.csdnimg.cn/78b6cf73b8eb44188c2cfc0a249a20f7.png" alt="在这里插入图片描述">

没报错即成功<img src="https://img-blog.csdnimg.cn/5ea707fdece6449d9eaa046119863993.png" alt="在这里插入图片描述">

## 第四步：安装fvcore

下载链接：https://github.com/facebookresearch/fvcore 然后cd到setup.py所在目录，用以下指令安装

```
python setup.py build --force develop

```

打开cmd输入

```
import fvcore 

```

没报错即成功

若无法下载，可以尝试下图这种方法，亲试可用！ <img src="https://img-blog.csdnimg.cn/5e2cceb90cc440b7aa8516dbabf27691.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 第五步：安装pytorch

**Facebook 发布 Detectron2：基于 PyTorch 的新一代目标检测工具** 可以参考我之前的博客：

这次遇到新的报错，进行以下指令后-》cuda无法使用

```
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.2 -c pytorch -c conda-forge

```

**降级大法**

```
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge

```

<img src="https://img-blog.csdnimg.cn/4afb90f00c3e482b9976131bcecf84b8.png" alt="在这里插入图片描述"> cuda可以使用了，玄学。

## 第六步：安装detectron2

在安装detectron2前需要先修改detectron2与pytorch的代码以保证顺利安装。 下载地址：https://github.com/conansherry/detectron2 1、根据官方文档对pytorch进行如下修改(觉得难找可以下载Everything)

**file1:** {your evn path}\Lib\site-packages\torch\include\torch\csrc\jit\runtime\argumenta_spec.h example: {C:\Miniconda3\envs\py36}\Lib\site-packages\torch\include\torch\csrc\jit\argument_spec.h(190) static **constexpr** size_t DEPTH_LIMIT = 128; change to --&gt; static **const** size_t DEPTH_LIMIT = 128;

改之前： <img src="https://img-blog.csdnimg.cn/9a53fe164b3c4c34af4ea4545a45256d.png" alt="在这里插入图片描述"> 改之后： <img src="https://img-blog.csdnimg.cn/1293a11b38a1426f98861abe4aa3919e.png" alt="在这里插入图片描述"> **file2:** {your evn path}\Lib\site-packages\torch\include\pybind11\cast.h example: {C:\Miniconda3\envs\py36}\Lib\site-packages\torch\include\pybind11\cast.h(1449) explicit operator type&amp;() { return ***(this-&gt;value);** } change to --&gt; explicit operator type&amp;() { return **((type)this-&gt;value)**; }

改之前：

<img src="https://img-blog.csdnimg.cn/3c0ed44271d04fa399d0ff999ccd3ad6.png" alt="在这里插入图片描述"> 改之后： <img src="https://img-blog.csdnimg.cn/9c586e69209a4b358a9ce37a9de8e29a.png" alt="在这里插入图片描述">

2、将detectron2\detectron2\layers\csrc\deformable 文件夹下三个文件中全部的 AT_CHECK 全部替换为 TORCH_CHECK

3、安装detectron2 进入解压后setup.py的路径后，用以下指令安装

```
python setup.py build --force develop

```

安装成功后显示：

```
Using d:\program files (x86)\anaconda3\envs\detecrton2\lib\site-packages
Finished processing dependencies for detectron2==0.1

```

pip list查看结果： <img src="https://img-blog.csdnimg.cn/f9fa87f8727a45b1bb9cd23a7de98a40.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

## 第七步：安装Detectron

下载地址：https://github.com/facebookresearch/Detectron 进入解压后setup.py的路径后，用以下指令安装

```
python setup.py build --force develop

```

报错： <img src="https://img-blog.csdnimg.cn/e0cb3cac57b540bab5e713a96993814e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 参考此博客方法： 将setup.py文件中注释掉 关于Wno-cpp的部分 <img src="https://img-blog.csdnimg.cn/9de3bc61502c4d7a97a4240b0a3d290f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 重新安装 安装成功显示： <img src="https://img-blog.csdnimg.cn/f7f94663b3744341be8ada26eae7e1fb.png" alt="在这里插入图片描述"> pip list查看结果： <img src="https://img-blog.csdnimg.cn/1a7738914ec64edaaf0b77b4028bb8da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述">

安装成功后显示：

## 测试：使用detectron2

```
python demo/demo.py --config-file configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.yaml 

```

报错： <img src="https://img-blog.csdnimg.cn/8ab34b983f864713ac42cb7ef99571cf.png" alt="在这里插入图片描述"> 网上寻找下载配置文件后：

```
python tools/train_net.py \ --cfg configs/getting_started/tutorial_1gpu_e2e_faster_rcnn_R-50-FPN.yaml \  OUTPUT_DIR /tmp/detectron-output

```

```
python demo/demo.py --config-file configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml --input img/street.jpg --output _output/bicycle_COCO-PanopticSegmentation.jpg --confidence-threshold 0.5 --opts MODEL.WEIGHTS models/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x/139514569/model_final_c10459.pkl

```

结果： <img src="https://img-blog.csdnimg.cn/8c62eb2a49c7438692da0825e6a791d9.jpg?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAenhtXw==,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 虽然效果很差，但至少是可以用了是吧~

<img src="https://img-blog.csdnimg.cn/98842ae2ba10476e945566dc59dbc736.png" alt="在这里插入图片描述">
