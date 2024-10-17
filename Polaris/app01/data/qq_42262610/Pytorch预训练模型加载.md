
--- 
title:  Pytorch预训练模型加载 
tags: []
categories: [] 

---
1. 保存模型：torch.save(model.state_dict(), PATH)

加载模型：model.load_state_dict(torch.load(PATH))

model.eval()



2. 什么是状态字典：state_dict?

在PyTorch中， torch.nn.Module 模型的可学习参数（即权重和偏差）包含在模型的参数中，（使用model.parameters() 可以进行访问）。 state_dict 是Python字典对象，它将每一层映射到其参数张量。注意，只有具有可学习参数的层（如卷积层，线性层等）的模型才具有state_dict 这一项。目标优化torch.optim 也有state_dict 属性，它包含有关优化器的状态信息，以及使用的超参数。

因为state_dict的对象是Python字典，所以它们可以很容易的保存、更新、修改和恢复，为PyTorch模型和优化器添加了大量模块。

3. torch.nn.Module.state_dict(destination=None, prefix='', keep_vars=False)返回一个包含模型状态信息的字典。包含参数（weighs and biases）和持续的缓冲值（如：观测值的平均值）。只有具有可更新参数的层才会被保存在模型的 state_dict 数据结构中。

当保存好模型用来推断的时候，只需要保存模型学习到的参数，使用torch.save() 函数来保存模型state_dict ,它会给模型恢复提供最大的灵活性

4. pytorch中自带几种常用的深度学习网络预训练模型，torchvision.models包中包含alexnet、densenet、inception、resnet、squeezenet、vgg等常用网络结构，并且提供了预训练模型，可通过调用来读取网络结构和预训练模型（模型参数）。往往为了加快学习进度，训练的初期直接加载pretrain模型中预先训练好的参数。加载model如下所示：

import torchvision.models as models

1.加载网络结构和预训练参数：resnet34 = models.resnet34(pretrained=True)

2.#只加载网络结构，不加载预训练参数，即不需要用预训练模型的参数来初始化：

resnet18 = models.resnet18(pretrained=False) #pretrained参数默认是False,为了代码清晰，最好还是加上参数赋值.

resnet18.load_state_dict(torch.load(**path**_params.pkl))#其中，path_params.pkl为预训练模型参数的保存**路径**。加载预先下载好的预训练参数到resnet18，用预训练模型的参数初始化resnet18的层，此时resnet18发生了改变。调用model的load_state_dict方法用预训练的模型参数来初始化自己定义的新网络结构，这个方法就是PyTorch中通用的用一个模型的参数初始化另一个模型的层的操作。load_state_dict方法还有一个重要的参数是strict，该参数默认是True，表示预训练模型的层和自己定义的网络结构层**严格对应相等**（比如层名和维度）。故，当新定义的网络（model_dict）和预训练网络（pretrained_dict）的层名不严格相等时，需要先将pretrained_dict里不属于model_dict的键剔除掉 ： pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in model_dict} ，再用预训练模型参数更新model_dict，最后用load_state_dict方法初始化自己定义的新网络结构。

5.例子：

model   = DeepLab(num_classes=num_classes, backbone=backbone, downsample_factor=downsample_factor, pretrained=False)  # 加载模型，不加载预训练参数

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') model_dict  = model.state_dict()  # 读取

pretrained_dict = torch.load(model_path, map_location = device)

pretrained_dict = {k: v for k, v in pretrained_dict.items() if np.shape(model_dict[k]) == np.shape(v)} # 将pretrained_dict和model_dict中命名一致的层加入pretrained_dict（包括参数)

model_dict.update(pretrained_dict)  # 更新现有的model_dict model.load_state_dict(model_dict)   #加载真正需要的state_dict  # 加载预先下载好的预训练参数到model

无论是从缺少某些键的 state_dict 加载还是从键的数目多于加载模型的 state_dict , 都可以通过在 load_state_dict() 函数中将strict 参数设置为 False来忽略非匹配键的函数。 如果要将参数从一个层加载到另一个层，但是某些键不匹配，主要修改正在加载的 state_dict 中的 参数键的名称以匹配要在加载到模型中的键即可。

model.load_state_dict(torch.load(PATH), strict=False)


