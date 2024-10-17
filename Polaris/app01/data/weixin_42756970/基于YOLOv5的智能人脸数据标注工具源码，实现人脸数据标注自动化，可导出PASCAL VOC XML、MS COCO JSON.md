
--- 
title:  基于YOLOv5的智能人脸数据标注工具源码，实现人脸数据标注自动化，可导出PASCAL VOC XML、MS COCO JSON 
tags: []
categories: [] 

---
  

 基于YOLOv5的智能人脸数据标注工具，实现人脸数据标注自动化 

 可自定义人脸检测模型、可导出多种格式标签，包括PASCAL VOC XML、MS COCO JSON、YOLO TXT 

下载地址：

#### 📌 项目整体流程与扩展应用

#### 📌 项目功能结构与信息流

### 💡项目结构

```
.
├── face-labeling							# 项目名称
│   ├── util								# 工具包
│   │   ├── voc_xml.py						# PASCAL VOC XML
│   │   ├── coco_json.py					# MS COCO JSON
│   │   ├── yolo_txt.py						# YOLO TXT
│   │   ├── model_opt.py					# 模型管理
│   │   ├── obj_opt.py						# 目标管理
│   │   ├── path_opt.py						# 路径管理
│   │   ├── log.py							# 日志管理
│   │   └── time_format.py					# 日期格式化
│   ├── data								# 测试数据
│   │   └── imgs							# 测试图片，来源于WIDER FACE Test
│   ├── models								# 模型Hub
│   │   ├── readme.md						# 模型Hub README
│   │   ├── *.pt							# PyTorch模型
│   │   └── *.onnx							# ONNX模型
│   ├── face_labeling.py					# 主运行文件
│   ├── LICENSE								# 项目许可
│   ├── CodeCheck.md						# 代码检查
│   ├── .gitignore							# git忽略文件
│   ├── yolov5_widerface.md					# 基于YOLOv5的人脸检测模型的构建
│   ├── yolov5_pytorch_gpu.md				# YOLOv5 PyTorch GPU安装教程
│   ├── README.md							# 项目说明
│   └── requirements.txt					# 脚本依赖包

```

### 🔥安装教程

#### ✅ 第一步：安装Face Labeling

📌 创建conda环境

```
conda create -n facelabel python==3.8
conda activate facelabel # 进入环境

```

📌 克隆

```
git clone https://gitee.com/CV_Lab/face-labeling.git

```

#### ✅ 第二步：安装Face Labeling依赖

```
cd ./face-labeling
conda activate facelabel # 进入环境
pip install -r requirements.txt -U

```

📌 将人脸模型文件（.pt）放入`models` 目录中

❗ 注意：yolov5默认采用pip安装PyTorch GPU版，如果采用官网安装**PyTorch GPU**版，参见

#### ✅ 基于YOLOv5的人脸检测模型的构建

📌 **widerface-m人脸检测模型**是在数据集上，基于训练的，具体训练过程参见

📌 **darkface-m人脸检测模型**是在数据集上，基于训练的，具体训练过程参见

❤️ 本项目提供了以下人脸检测模型：

<th align="center">模型名称</th><th align="center">下载地址</th><th align="center">模型大小</th><th align="center">适用范围</th><th align="center">适用设备</th>
|------
<td align="center">widerface-m</td><td align="center"> , 提取码：5gfs</td><td align="center">42.1MB</td><td align="center">实时,图片,视频</td><td align="center">GPU</td>
<td align="center">darkface-m</td><td align="center"> , 提取码：mm2k</td><td align="center">42.2MB</td><td align="center">实时,图片,视频</td><td align="center">GPU</td>

### ⚡使用教程

#### 💡 webcam实时标注

```
# a键捕获视频帧，q键退出
python face_labeling.py

```

#### 💡 图片标注（包括批量图片标注）

```
python face_labeling.py -m img # 默认测试图片目录data/imgs
python face_labeling.py -m img -imd ./img_dir # 指定图片目录

```

❗ 注：本项目支持的图片输入格式：**jpg** | **jpeg** | **png** | **bmp** | **tif** | **webp**

#### 💡 视频标注（包括批量视频标注）

```
python face_labeling.py -m video # 默认测试视频目录data/videos
python face_labeling.py -m video -vd ./video_dir # 指定视频目录

```

❗ 注：本项目支持的视频输入格式：**mp4** | **avi** | **wmv** | **mkv** | **mov** | **gif** | **vob** | **swf** | **mpg** | **flv** | **3gp** | **3g2**

❗ 说明：以上三种检测模式都会在项目根目录中生成`FaceFrame`目录，该目录会生成`frame*`的子目录，子目录结构如下：

```
# webcam和图片标注的目录
.
├── FaceFrame						# 人脸数据保存目录
│   ├── frame						# 子目录
│   │   ├── raw						# 原始图片
│   │   ├── tag						# 标记图片（包括：人脸检测框、人脸ID、置信度、帧ID、FPS、人脸总数，人脸尺寸类型（小、中、大）数量）
│   │   ├── voc_xml					# PASCAL VOC XML 标注文件
│   │   ├── coco_json				# MS COCO JSON 标注文件
│   │   ├── yolo_txt				# YOLO TXT 标注文件
│   ├── frame2						# 子目录
│   │   ├── raw						# 原始图片
│   │   ├── ......

```

```
# 视频标注的目录
.
├── FaceFrame						# 人脸数据保存目录
│   ├── frame						# 子目录
│	│   ├── video_name01			# 子视频目录
│   │   │   ├── raw					# 原始图片
│   │   │   ├── tag					# 标记图片（包括：人脸检测框、人脸ID、置信度、帧ID、FPS、人脸总数，人脸尺寸类型（小、中、大）数量）
│   │   │   ├── voc_xml				# PASCAL VOC XML 标注文件
│   │   │   ├── coco_json			# MS COCO JSON 标注文件
│   │   │   ├── yolo_txt			# YOLO TXT 标注文件
│	│   ├── video_name02			# 子视频目录
│   │   │   ├── raw					# 原始图片
│   │   │   ├── ......

```

❗ 查看检测结果：人脸图片检测结果会保存在`FaceFrame/frame*/tag`中，以`python face_labeling.py -m img`为例运行项目自带检测图片，检测结果如下：

#### 💡 自定义人脸模型

```
# 默认为widerface-m
python face_labeling.py -mn face_model # 以实时标注为例
python face_labeling.py -mn darkface-m # 以实时标注为例，darkface-m.pt

```

#### 💡 自定义类别

```
# 默认为face，以口罩识别为例
python face_labeling.py -cls mask # 口罩类
python face_labeling.py -cls without-mask # 未戴口罩类

```

#### 💡 自定义模型参数

```
# 可以根据自定义人脸模型进行相应的调参，以实时标注为例

# 自定义设备，默认为cuda:0
python face_labeling.py
python face_labeling.py -dev 0 # cuda:0版
python face_labeling.py -dev cpu # cpu版

# NMS 置信度阈值，默认为0.5
python face_labeling.py -conf 0.8

# NMS IoU阈值，默认为0.45
python face_labeling.py -iou 0.5

# 单张图片的最大检测目标数，默认为1000
python face_labeling.py -mdn 10

# 以上参数也可以同时使用，例如：
python face_labeling.py -conf 0.8 -iou 0.5
python face_labeling.py -conf 0.8 -iou 0.5 -mdn 10

# 模型推理尺寸
python face_labeling.py -isz 320

# 强制重载YOLOv5
python face_labeling.py -ry

```

#### 💡 设置标签样式

```
# 以实时标注为例
python face_labeling.py -ls id # 标签仅显示ID
python face_labeling.py -ls conf # 标签仅显示置信度（%）

```

#### 💡 设置标签进度条

```
python face_labeling.py -lpb bar

```

#### 💡 关闭检测标签

```
python face_labeling.py -lds # 以实时标注为例

```

#### 💡 自定义保存目录名称

```
# 默认为FaceFrame
python face_labeling.py -fsd face_dir # 以实时标注为例

```

#### 💡 自定义保存子目录名称

```
# 默认为frame
python face_labeling.py -fdn face_subDir # 以实时标注为例

```

#### 💡 自定义图片前缀

```
# 默认为face_test
python face_labeling.py -in face # 以实时标注为例

```

下载地址：
