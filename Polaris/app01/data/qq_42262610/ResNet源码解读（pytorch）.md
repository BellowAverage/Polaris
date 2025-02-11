
--- 
title:  ResNet源码解读（pytorch） 
tags: []
categories: [] 

---
```
import torch
import torchvision
import argparse
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms, models
import torch.utils.model_zoo as model_zoo
import math

__all__ = ['ResNet', 'resnet18', 'resnet34', 'resnet50', 'resnet101',
           'resnet152']

# 在imagenet数据集上训练的模型
model_urls = {
    'resnet18': 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
    'resnet34': 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
    'resnet50': 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
    'resnet101': 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
    'resnet152': 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
}


def conv3x3(in_planes, out_planes, stride=1):
    # 3x3 kernel
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)


# get BasicBlock which layers &lt; 50(18, 34)
class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_planes, planes, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(in_planes, planes, stride)
        self.BN = nn.BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes, stride) # outplane is not in_planes*self.expansion, is planes
        self.stride = stride
        self.downsample = downsample

    def forward(self, x):
        residual = x   # mark the data before BasicBlock
        x = self.conv1(x)
        x = self.BN(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.BN(x)  # BN operation is before relu operation
        if self.downsample is not None:  # is not None
            residual = self.downsample(residual)  # resize the channel
        x += residual
        x = self.relu(x)
        return x


# get BottleBlock which layers &gt;= 50
class Bottleneck(nn.Module):
    expansion = 4 # the factor of the last layer of BottleBlock and the first layer of it

    def __init__(self, in_planes, planes, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(in_planes, planes, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.con2 = conv3x3(planes, planes)
        self.bn2 = nn.BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes*4, kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(planes*4)
        self.downsample = downsample
        self.stride = stride
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        residual = x
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)

        x = self.con2(x)
        x = self.bn2(x)
        x = self.relu(x)

        x = self.conv3(x)
        x = self.bn3(x)
        if self.downsample is not None:
            residual = self.downsample(residual)

        x += residual
        x = self.relu(x)

        return x


class ResNet(nn.Module):

    def __init__(self, block, layers, num_classes=100):
        self.inplanes = 64 # the original channel
        super(ResNet, self).__init__()
        self.num_classes = num_classes
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.max_pool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        # 以下构建残差块， 具体参数可以查看resnet参数表
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        self.average_pool = nn.AvgPool2d(7, stride=1)
        self.fc = nn.Linear(512*block.expansion, num_classes)
        # 对卷积和与BN层初始化，论文中也提到过
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, math.sqrt(2. / n))
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
    # 这里是为了结局两个残差块之间可能维度不匹配无法直接相加的问题，相同类型的残差块只需要改变第一个输入的维数就好，后面的输入维数都等于输出维数
    def _make_layer(self, block, planes, num_blocks, stride=1):
        downsample = None

        # 扩维
        if stride != 1 or self.inplanes != block.expansion * planes:
            downsample = nn.Sequential(
                nn.Conv2d(self.inplanes, block.expansion*planes,kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(block.expansion*planes)
            )

        layers = []
        # 特判第一残差块
        layers.append(block(self.inplanes, planes, downsample=downsample)) # outplane is planes not planes*block.expansion
        self.inplanes = planes * block.expansion
        for i in range(1, num_blocks):
            layers.append(block(self.inplanes, planes))

        return nn.Sequential(*layers)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.max_pool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.average_pool(x)
        x = x.view(x.size(0), -1) # resize batch-size x H
        x = self.fc(x)
        return x


def resnet18(pretrained=False, **kwargs):
    """Constructs a ResNet-18 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [2, 2, 2, 2], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet18']))
    return model


def resnet34(pretrained=False, **kwargs):
    """Constructs a ResNet-34 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(BasicBlock, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet34']))
    return model


def resnet50(pretrained=False, **kwargs):
    """Constructs a ResNet-50 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 6, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet50']))
    return model


def resnet101(pretrained=False, **kwargs):
    """Constructs a ResNet-101 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 4, 23, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet101']))
    return model


def resnet152(pretrained=False, **kwargs):
    """Constructs a ResNet-152 model.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = ResNet(Bottleneck, [3, 8, 36, 3], **kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['resnet152']))
    return model


```


