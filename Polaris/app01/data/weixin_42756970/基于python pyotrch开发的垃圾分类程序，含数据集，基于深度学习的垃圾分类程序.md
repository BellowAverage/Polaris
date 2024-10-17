
--- 
title:  基于python pyotrch开发的垃圾分类程序，含数据集，基于深度学习的垃圾分类程序 
tags: []
categories: [] 

---
## 基于python的垃圾分类程序，提供数据集（pytorch开发）

完整代码下载地址： <img src="https://img-blog.csdnimg.cn/img_convert/6712a214f23567417ceb3b3df6a9c3b5.png" alt="image-20210305103139860">

垃圾分类是目前社会的一个热点，分类的任务是计算机视觉任务中的基础任务，相对来说比较简单，只要找到合适的数据集，垃圾分类的模型构建并不难，这里我找到一份关于垃圾分类的数据集，一共有四个大类和245个小类，大类分别是厨余垃圾、可回收物、其他垃圾和有害垃圾，小类主要是垃圾的具体类别，果皮、纸箱等。

为了方便大家使用，我已经提前将数据集进行了处理，按照8比1比1的比例将原始数据集划分成了训练集、验证集和测试集，大家可以从下面的链接自取。

>  
 链接：https://pan.baidu.com/s/1BkDlOmJwN37TVhfig4llow 提取码：9avi 复制这段内容后打开百度网盘手机App，操作更方便哦–来自百度网盘超级会员V4的分享 


### 代码结构

```
trash1.0
├─ .idea idea配置文件
├─ imgs 图片文件
├─ main_window.py 图形界面代码
├─ models
│    └─ mobilenet_trashv1_2.pt
├─ old 一些废弃的代码
├─ readme.md 你现在看到的
├─ test.py 测试文件
├─ test4dataset.py  测试所有的数据集
├─ test4singleimg.py 测试单一的图片
├─ train_245_class.py 训练代码
└─ utils.py 工具类，用于划分数据集

```

### 训练

训练前请执行命令按照好项目所需的依赖库，关于如何在python中使用conda和pip对项目包管理可以看这篇文章或者是看我b站的这个视频，里面有详细的讲解。

>  
 csdn文章： 


```
conda create -n torch1.6 python==3.6.10
conda activate torch1.6
conda install pytorch torchvision cudatoolkit=10.2 # GPU(可选)
conda install pytorch torchvision cpuonly
pip install opencv-python
pip install matplotlib

```

首先需要把数据集下载之后进行解压，记住解压的路径，并在`train.py`的18行将数据集路径修改为你本地的数据集路径，修改之后执行运行`train.py`文件即可开始模型训练，训练之后的模型将会保存在models目录下。

模型训练部分则选用了大名鼎鼎的mobilenet，mobilenet是比较轻量的网络，在cpu上也可以运行的很快，训练的代码如下，首先通过pytorch的dataloader加载数据集，并加载预训练的mobilenet进行微调。

```
# coding:utf-8
# TODO 添加一个图形化界面
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
import torch
import torchvision.transforms as transforms
from PIL import Image
from old.train_based_torchvision import Net

names = []


class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('imgs/面性铅笔.png'))
        self.setWindowTitle('垃圾识别')
        # 加载网络
        self.net = torch.load("models/mobilenet_trashv1_2.pt", map_location=lambda storage, loc: storage)
        self.transform = transforms.Compose(
            # 这里只对其中的一个通道进行归一化的操作
            [transforms.Resize([224, 224]),
             transforms.ToTensor(),
             transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        font = QFont('楷体', 15)
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        img_title = QLabel("测试样本")
        img_title.setFont(font)
        img_title.setAlignment(Qt.AlignCenter)
        self.img_label = QLabel()
        self.predict_img_path = "imgs/img111.jpeg"
        img_init = cv2.imread(self.predict_img_path)
        img_init = cv2.resize(img_init, (400, 400))
        cv2.imwrite('imgs/target.png', img_init)
        self.img_label.setPixmap(QPixmap('imgs/target.png'))
        left_layout.addWidget(img_title)
        left_layout.addWidget(self.img_label, 1, Qt.AlignCenter)
        left_widget.setLayout(left_layout)

        right_widget = QWidget()
        right_layout = QVBoxLayout()
        btn_change = QPushButton(" 上传垃圾图像 ")
        btn_change.clicked.connect(self.change_img)
        btn_change.setFont(font)
        btn_predict = QPushButton(" 识别垃圾种类 ")
        btn_predict.setFont(font)
        btn_predict.clicked.connect(self.predict_img)

        label_result = QLabel(' 识 别 结 果 ')
        self.result = QLabel("待识别")
        label_result.setFont(QFont('楷体', 16))
        self.result.setFont(QFont('楷体', 24))
        right_layout.addStretch()
        right_layout.addWidget(label_result, 0, Qt.AlignCenter)
        right_layout.addStretch()
        right_layout.addWidget(self.result, 0, Qt.AlignCenter)
        right_layout.addStretch()
        right_layout.addWidget(btn_change)
        right_layout.addWidget(btn_predict)
        right_layout.addStretch()
        right_widget.setLayout(right_layout)

        # 关于页面
        about_widget = QWidget()
        about_layout = QVBoxLayout()
        about_title = QLabel('欢迎使用智能垃圾识别系统')
        about_title.setFont(QFont('楷体', 18))
        about_title.setAlignment(Qt.AlignCenter)
        about_img = QLabel()
        about_img.setPixmap(QPixmap('imgs/logoxx.png'))
        about_img.setAlignment(Qt.AlignCenter)
        label_super = QLabel()
        label_super.setText("&lt;a href='https://blog.csdn.net/ECHOSON'&gt;我的个人主页&lt;/a&gt;")
        label_super.setFont(QFont('楷体', 12))
        label_super.setOpenExternalLinks(True)
        label_super.setAlignment(Qt.AlignRight)
        # git_img = QMovie('images/')
        about_layout.addWidget(about_title)
        about_layout.addStretch()
        about_layout.addWidget(about_img)
        about_layout.addStretch()
        about_layout.addWidget(label_super)
        about_widget.setLayout(about_layout)

        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)
        main_widget.setLayout(main_layout)
        self.addTab(main_widget, '主页面')
        self.addTab(about_widget, '关于')
        self.setTabIcon(0, QIcon('imgs/面性计算器.png'))
        self.setTabIcon(1, QIcon('imgs/面性本子vg.png'))

    def change_img(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Image files(*.jpg , *.png, *.jpeg)')
        print(openfile_name)
        img_name = openfile_name[0]
        if img_name == '':
            pass
        else:
            self.predict_img_path = img_name
            img_init = cv2.imread(self.predict_img_path)
            img_init = cv2.resize(img_init, (400, 400))
            cv2.imwrite('imgs/target.png', img_init)
            self.img_label.setPixmap(QPixmap('imgs/target.png'))

    def predict_img(self):
        # 预测图片
        # 开始预测
        # img = Image.open()
        transform = transforms.Compose(
            [transforms.Resize([224, 224]),
             transforms.ToTensor(),
             transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

        img = Image.open(self.predict_img_path)
        RGB_img = img.convert('RGB')
        img_torch = transform(RGB_img)
        img_torch = img_torch.view(-1, 3, 224, 224)
        outputs = self.net(img_torch)
        _, predicted = torch.max(outputs, 1)
        result = str(names[predicted[0].numpy()])

        self.result.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()
    sys.exit(app.exec_())

```

### 测试

模型训练好之后就可以进行模型的测试了，其中`test4dataset.py`文件主要是对数据集进行测试，也就是解压之后的test目录下的所有文件进行测试，那么`test4singleimg.py`文件主要是对单一的图片进行测试。

考虑到大家可能想省去训练的过程，所以我在models目录下放了我训练好的模型，你可以直接使用我训练好的模型进行测试，目前在测试集上的准确率大概在80%左右，不是很高，但是也足够使用。

另外，处理基本的测试之外，还有分类别的测试以及heatmap形式的演示，这部分的代码写的比较乱，暂时放在了abandon目录下，如果项目的star超过100的话，我会再更新这部分的内容。以下就是部分测试的代码；

```
# from train import load_data
from PIL import ImageFile
import torch
import os
from torchvision import transforms, datasets
import numpy as np
from torch.utils.data import Dataset
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
# 有些图片信息不全，不能读取，跳过这些图片
ImageFile.LOAD_TRUNCATED_IMAGES = True
np.set_printoptions(suppress=True)

# todo
def load_test_data(data_dir="E:/遥感目标检测数据集/垃圾分类数据集/trash_real_split"):
    data_transforms = {
        'val': transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'test': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                              data_transforms[x])
                      for x in ['val', 'test']}
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=32,
                                                  shuffle=True, num_workers=0)
                   for x in ['val', 'test']}
    dataset_sizes = {x: len(image_datasets[x]) for x in ['val', 'test']}
    class_names = image_datasets['test'].classes
    return dataloaders, dataset_sizes, class_names


def test_test_dataset(model_path="models/mobilenet_trashv1_2.pt"):
    # 加载模型
    net = torch.load(model_path, map_location=lambda storage, loc: storage)
    dataloaders, dataset_sizes, class_names = load_test_data()
    testloader = dataloaders['test']
    test_size = dataset_sizes['test']
    net.to(device)
    net.eval()
    # 测试全部的准确率
    correct = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += torch.sum(predicted == labels.data)
    correct = correct.cpu().numpy()
    print('Accuracy of the network on the %d test images: %d %%' % (test_size,
                                                                    100 * correct / total))


def test_test_dataset_by_classes(model_path="models/mobilenet_trashv1_2.pt"):
    # 加载模型
    net = torch.load(model_path, map_location=lambda storage, loc: storage)
    dataloaders, dataset_sizes, class_names = load_test_data()
    testloader = dataloaders['test']
    test_size = dataset_sizes['test']
    net.to(device)
    net.eval()
    classes = class_names
    # 测试每一类的准确率
    class_correct = list(0. for i in range(len(class_names)))
    class_total = list(0. for i in range(len(class_names)))
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs, 1)
            c = (predicted == labels).squeeze()
            for i in range(len(labels)):
                label = labels[i]
                class_correct[label] += c[i].item()
                class_total[label] += 1
    for i in range(len(class_names)):
        print('Accuracy of %5s : %2d %%' % (
            classes[i], 100 * class_correct[i] / class_total[i]))


if __name__ == '__main__':
    print('模型在整个数据集上的表现：')
    test_test_dataset()
    print('模型在每一类上的表现：')
    test_test_dataset_by_classes()

```

测试结果如下图：

<img src="https://img-blog.csdnimg.cn/img_convert/0127be7ca706bb759ea4528836e73aa3.png" alt="image-20210305140104656">

### 图形化界面

图形化界面主要通过Pyqt5来进行开发，主要是完成一些上传图片，对图片进行识别并把识别结果进行输出的功能，俺的审美不是很好，所以设计的界面可能不是很好看，大家后面可以根据自己的需要修改界面。

<img src="https://img-blog.csdnimg.cn/img_convert/d972e8ddbfdc6ba3e812c1c42aa4dbd7.png" alt="image-20210305142518950">

<img src="https://img-blog.csdnimg.cn/img_convert/0de46b0062c9d45630e80313ecc59012.png" alt="image-20210305142537660">

<img src="https://img-blog.csdnimg.cn/img_convert/674b8522ae6b79bc1abd30c441ee84ad.png" alt="image-20210305142602138">

完整代码下载地址：
