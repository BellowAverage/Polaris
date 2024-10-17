
--- 
title:  PyTorch框架GPU代码转CPU代码 
tags: []
categories: [] 

---
#### 在进行深度学习的训练和测试时，所用的代码有的需要GPU计算，但当需要将代码部署在没有GPU的云端服务器或者自己本地电脑上运行时，就需要将GPU代码转换为CPU代码，修改代码的位置大概如下：

**1.此时可以在代码开头添加如下代码获取当前计算机是否有GPU**

**device = torch.device("cuda" if torch.cuda.is_available() else "cpu")**

**print(device) #cpu**

**2.****然后在代码中用 .to(device)或者.cpu()替换.cuda() **

**3.有torch.cuda.empty_cache()的地方全部注释掉**

**4.有torch.load(ckpt_dir)的地方，修改为torch.load(ckpt_dir，map_location = ‘cpu’)**

**5.****segmenter = torch.nn.DataParallel(create_segmenter(enc_pretrained, num_classes) ).cuda() #将.cuda()改为.cpu()**

**torch.load()**先在CPU上加载，不会依赖于保存模型的设备。如果加载失败，可能是因为没有包含某些设备，比如你在gpu上训练保存的模型，而在cpu上加载，可能会报错，此时，需要使用map_location来将存储动态重新映射到可选设备上。

综上所述：需要将网络改为cpu和将模型加载改为cpu

网络部分：GlassMask_Net = ResnetGeneratorMask(input_nc=64, output_nc=2, norm_layer=norm).to(device)   # device=‘cpu'

模型加载加载部分：ckpt = torch.load(args.ckpt_path, map_location='cpu') 

**在后期的设备上调用修改的cpu版本时，分割算法没有执行，解决方法如下：**

在分割算法上打印print，最终定位到binary, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# 获取轮廓，这句没有执行，从而判断出并不是修改cpu的问题，通过百度查cv2.findContours查这个函数，OpenCV2和OpenCV4运行这个函数会有两个返回值，OpenCV3会有三个返回值。因为代码中写了三个返回值，所以OpenCV的版本应该采用OpenCV3，但是查看平台版本是OpenCV4，所以应该是版本的问题。

**解决方案：pip3 uninstall opencv-python(卸载);   pip3 install  opencv-python==3.4.10.35 -i https://pypi.tuna.tsinghua.edu.cn/simple（安装）**
