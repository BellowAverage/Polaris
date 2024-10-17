
--- 
title:  NeRF神经网络介绍 
tags: []
categories: [] 

---


#### NeRF神经网络
- - - - <ul><li>- - <ul><li>- - - - 


## NeRF: Neural Radiance Fields简介

优化单个场景的神经表示并渲染新视图的Tensorflow实现。 NeRF:将场景表示为用于视图合成的 Neural Radiance Fields

## 团队介绍
- 来自加州大学伯克利分校<mark>Ben Mildenhall</mark>(本·米尔登霍尔)- 来自加州大学伯克利分校<mark>Pratul P. Srinivasan</mark>(普拉图尔·斯里尼瓦桑)- 来自加州大学伯克利分校<mark>Matthew Tancik</mark>(马修·坦西克)- 来自谷歌研究Jonathan T. Barron( 乔纳森·巴伦)- 来自加州大学圣地亚哥分校Ravi Ramamoorthi(拉维·拉马穆尔蒂)- 来自加州大学伯克利分校Ren Ng( 吴义仁)
黄色底为表示同等贡献 在ECCV 2020年(口头陈述，最佳论文荣誉奖)

<img src="https://img-blog.csdnimg.cn/9041d28e91714764b1eee2fe30bc86a4.png" alt="在这里插入图片描述">

## 快速入门

要设置conda环境，请下载示例培训数据，开始培训过程，并启动Tensorboard:

```
conda env create -f environment.yml
conda activate nerf
bash download_example_data.sh
python run_nerf.py --config config_fern.txt
tensorboard --logdir=logs/summaries --port=6006

```

如果一切正常，您现在可以进入`localhost:6006`在你的浏览器里观看“Fern”场景训练。

### 设置

Python 3依赖性:
- Tensorflow 1.15- matplotlib- numpy- imageio- configargparse
LLFF数据加载器需要ImageMagick。

我们提供了一个conda环境设置文件，包括上述所有依赖项。创造conda环境`nerf`通过运行:

```
conda env create -f environment.yml

```

你还需要LLFF code(和COLMAP)建立评估姿态，如果你想在自己的真实数据上运行。

## 什么是NeRF？

Neural Radiance Fields是一个简单的完全连接的网络(权重约为5MB )，它被训练为使用渲染损失来再现单个场景的输入视图。该网络直接从空间位置和观察方向(5D输入)映射到颜色和不透明度(4D输出)，充当“体积”，因此我们可以使用体积渲染来有区别地渲染新视图。 优化一个NeRF需要几个小时到一两天的时间(取决于分辨率),并且只需要一个GPU。从优化的NeRF渲染一幅图像需要不到一秒到30秒的时间，这也取决于分辨率。

### 运行代码

这里我们展示了如何在两个示例场景中运行我们的代码。您可以下载论文中使用的其他合成和真实数据。

#### 优化NeRF

启动程序

```
bash download_example_data.sh

```

来获取我们的合成乐高数据集和LLFF Fern数据集。

若要优化低分辨率Fern NeRF:

```
python run_nerf.py --config config_fern.txt

```

经过20万次迭代(大约15个小时)，应该可以在`logs/fern_test/fern_test_spiral_200000_rgb.mp4` <img src="https://img-blog.csdnimg.cn/593b1c97b64c4cf9952a9104b0f84055.gif" alt="在这里插入图片描述"> 要优化低分辨率乐高NeRF:

```
python run_nerf.py --config config_lego.txt

```

经过20万次迭代后，您应该会看到这样的视频: <img src="https://img-blog.csdnimg.cn/c4963bef891843f2892e5fc85473d9ef.gif" alt="在这里插入图片描述">

### 渲染一个NeRF

启动程序

```
bash download_example_weights.sh

```

为Fern数据集获得一个预训练的高分辨率NeRF。现在您可以使用`render_demo.ipynb`来呈现新的视图。

#### 复制纸质结果

示例配置文件的分辨率低于论文和视频中的定量/定性结果。要复制论文中的结果，从中的配置文件开始`paper_configs/`。我们的合成搅拌机数据和LLFF场景托管深度体素数据由文森特·西兹曼主持。

#### 从NeRF中提取几何体

检验`extract_mesh.ipynb`例如，运行行进立方体来从训练好的NeRF网络中提取三角形网格。你需要安装皮姆库斯用于行进立方体和的包三角形网线图和pyrender如果要渲染笔记本内部的网格，请执行以下操作:

```
pip install trimesh pyrender PyMCubes

```

### 为自己的场景生成姿势

#### 不摆姿势？

我们建议使用`imgs2poses.py`脚本来自LLFF电码。然后，您可以使用以下命令将基本场景目录传递到我们的代码中`--datadir &lt;myscene&gt;`随着`-dataset_type llff`。你可以看看`config_fern.txt`前向场景使用的设置示例。对于球形捕捉的360°场景，我们建议添加`--no_ndc --spherify --lindisp`旗帜。

#### 已经有姿势了！

在…里`run_nerf.py`和所有其他代码一样，我们使用与OpenGL中相同的姿态坐标系:图像的局部相机坐标系定义为X轴指向右侧，Y轴向上，Z轴从图像中看向后。

姿势存储为3x4 numpy数组，表示摄影机到世界的变换矩阵。您需要的其他数据是简单的针孔摄像机内部函数(`hwf = [height, width, focal length]`)和近/远场景边界。看一看我们的数据加载代码去看更多。
