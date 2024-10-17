
--- 
title:  pytorch model.train() 
tags: []
categories: [] 

---
model.train(): 在使用pytorch构建神经网络的时候，训练过程中会在程序上方添加一句model.train()，作用是启用batch normalization和drop out。

model.eval(): 测试过程中会使用model.eval()，这时神经网络会沿用batch normalization的值，并不使用drop out。

 如果模型中有BN层(Batch Normalization）和Dropout，需要在训练时添加model.train()，在测试时添加model.eval()。其中model.train()是保证BN层用每一批数据的均值和方差，而model.eval()是保证BN用全部训练数据的均值和方差；而对于Dropout，model.train()是随机取一部分网络连接来训练更新参数，而model.eval()是利用到了所有网络连接。  
