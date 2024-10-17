
--- 
title:  pytorch测试的时候为何要加上model.eval()？ 
tags: []
categories: [] 

---
很多机器学习的教程都有提到，在使用pytorch进行训练和测试的时候一定要给实例化的model指定eval，那么pytorch测试时为什么要设置model.eval()呢？model.eval()的功能是什么？接下来的这篇文章告诉你。

使用PyTorch进行训练和测试时一定注意要把实例化的model指定train/eval，eval（）时，框架会自动把BN和DropOut固定住，不会取平均，而是用训练好的值，不然的话，一旦test的batch_size过小，很容易就会被BN层导致生成图片颜色失真极大！！！！！！

### model.eval()和with torch.no_grad()的区别

在PyTorch中进行validation时，会使用model.eval()切换到测试模式，在该模式下，

主要用于通知dropout层和batchnorm层在train和val模式间切换

在train模式下，dropout网络层会按照设定的参数p设置保留激活单元的概率（保留概率=p); batchnorm层会继续计算数据的mean和var等参数并更新。

在val模式下，dropout层会让所有的激活单元都通过，而batchnorm层会停止计算和更新mean和var，直接使用在训练阶段已经学出的mean和var值。

该模式不会影响各层的gradient计算行为，即gradient计算和存储与training模式一样，只是不进行反传（backprobagation）

而with torch.no_grad()则主要是用于停止autograd模块的工作，以起到加速和节省显存的作用，具体行为就是停止gradient计算，从而节省了GPU算力和显存，但是并不会影响dropout和batchnorm层的行为。

不理解为什么在训练和测试函数中model.eval()，和model.train()的区别，经查阅后做如下整理

#### 一般情况下，我们训练过程如下：

1、拿到数据后进行训练，在训练过程中，使用

`model.train(）`：告诉我们的网络，这个阶段是用来训练的，可以更新参数。

2、训练完成后进行预测，在预测过程中，使用

`model.eval()` ： 告诉我们的网络，这个阶段是用来测试的，于是模型的参数在该阶段不进行更新。
