
--- 
title:  【深度学习】MNIST手写数字数据集的分类识别 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>MNIST手写数字数据集的分类识别</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - -  
  
  


## 1. 目的及目标

目的：为了实现对MNIST手写数字数据集的分类识别。

目标：
1.  **构建模型**：使用PyTorch库定义并构建一个简单的深度学习模型（在这种情况下是一个全连接的多层感知器，MLP）。 1.  **训练模型**：通过反复地在MNIST训练数据上迭代，调整模型的权重，使其能够正确分类手写数字。 1.  **评估模型**：在每轮训练结束后，评估模型在MNIST测试集上的性能，以检查其泛化能力并了解其在未见过的数据上的表现。 
## 2. 代码实现

我们可以了解到如何使用PyTorch建立、训练和评估一个基本的深度学习模型。实现一个基本的深度学习网络，我们可以使用Python的TensorFlow或PyTorch库。

首先，确保你安装了`torch`和`torchvision`：

```
pip install torch torchvision

```

深度神经网络实现，用于处理手写数字识别（MNIST数据集）：

```
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, 500)
        self.fc2 = nn.Linear(500, 256)
        self.fc3 = nn.Linear(256, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)  # 将输入扁平化
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x, dim=1)

# 加载数据
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1000, shuffle=False)

# 创建模型、优化器和损失函数
model = Net()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
criterion = nn.CrossEntropyLoss()

# 训练模型
def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

# 测试模型
def test():
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset), 100. * correct / len(test_loader.dataset)))

for epoch in range(1, 11):  # 训练10轮
    train(epoch)
    test()

```

这是一个简单的三层全连接网络，它用于MNIST手写数字识别。可以通过调整网络结构、参数和训练次数来进一步优化模型。

## 3. 代码功能描述
1.  **数据加载和预处理**：代码使用`torchvision`库加载MNIST手写数字数据集，并对数据进行简单的归一化处理。 1.  **定义神经网络模型**：定义了一个简单的三层全连接网络（多层感知器，MLP）来对手写数字进行分类。 <li> **定义训练函数**：`train`函数执行以下操作： 
  1. 设置模型为训练模式。1. 在数据加载器`train_loader`中遍历每个批次的数据。1. 对每个批次的数据执行前向传播。1. 计算损失（使用交叉熵损失函数）。1. 执行反向传播。1. 使用SGD优化器更新网络权重。 </li><li> **定义测试函数**：`test`函数执行以下操作： 
  1. 设置模型为评估模式。1. 在数据加载器`test_loader`中遍历每个批次的数据。1. 对每个批次的数据执行前向传播。1. 计算损失和预测准确性。 </li>1.  **模型训练和评估**：循环训练模型10轮，并在每轮结束时评估模型在测试数据上的性能。 - 设置模型为评估模式。- 在数据加载器`test_loader`中遍历每个批次的数据。- 对每个批次的数据执行前向传播。- 计算损失和预测准确性。
总的来说，这段代码的主要功能是使用一个简单的深度学习模型（全连接网络）来进行手写数字识别。模型在MNIST数据集上进行训练，并在每轮训练后评估其在测试集上的性能。
