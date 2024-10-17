
--- 
title:  tensor中数据类型的相互转换 
tags: []
categories: [] 

---
Pytorch中的Tensor常用的类型转换函数

    tensor数据类型转换

   例如：

   a = tensor(282, device='cuda:0')

  b = int(a)

 print(b)  # 282,int类型     在tensor的后面添加: .int()、.float()、.double()等.     同时也可以使用 .to(type) 进行实现。     同时也可以使用 type()函数 ,data为Tensor数据类型，data.type()为给出data的类型，如果使用data.type(torch.FloatTensor)则强制转换为torch.FloatTensor类型张量。当你不知道要转换为什么类型时，但需要求a1,a2两个张量的乘积，可以使用a1.type_as(a2)将a1转换为a2同类型。     tensor&lt;–&gt;numpy     Tensor----&gt;Numpy 使用 tensor.numpy()，tensor为Tensor变量     Numpy ----&gt; Tensor 使用 torch.from_numpy(data)，data为numpy变量     tensor&lt;–&gt;Python     Tensor ----&gt; 单个Python数据，使用data.item()，data为Tensor变量且只能为包含单个数据     Tensor ----&gt; Python list，使用data.tolist()，data为Tensor变量，返回shape相同的可嵌套的list     数据存储位置转换     CPU张量 ----&gt; GPU张量，使用data.cuda()     GPU张量 ----&gt; CPU张量，使用data.cpu()  
