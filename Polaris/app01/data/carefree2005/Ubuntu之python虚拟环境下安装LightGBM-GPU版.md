
--- 
title:  Ubuntu之python虚拟环境下安装LightGBM-GPU版 
tags: []
categories: [] 

---
## 一、LightGBM简介

  LightGBM是一种基于梯度提升决策树（Gradient Boosting Decision Tree）的机器学习算法，它由微软亚洲研究院开发。与传统的梯度提升决策树相比，LightGBM采用了一些优化技术，使其在训练速度和模型性能上具有更好的表现。LightGBM的主要特点包括：
- 快速训练速度：LightGBM采用了基于直方图的算法来高效地处理特征的离散化，从而加快了训练速度。- 低内存占用：LightGBM使用了稀疏特征优化算法，可以有效地减少内存的使用。- 高准确率：LightGBM采用了基于直方图的算法来进行特征分割，可以更好地处理离散和连续特征，从而提高了模型的准确率。- 支持并行化：LightGBM可以使用多线程来并行地训练模型，加快了训练速度。- 可扩展性：LightGBM支持大规模数据集的训练，可以处理亿级别的样本和特征。
  总之，LightGBM是一种快速、高效、准确的机器学习算法，适用于处理大规模数据集和高维特征的问题。它在许多机器学习竞赛中取得了优秀的成绩，并被广泛应用于实际的数据科学项目中。

## 二、安装环境要求

  安装要求见，可以看到linux环境安装lightgbm-gpu版本要求：
- OpenCL 1.2以上版本- libboost 1.56以上版本- CMake 3.2 以上版本- glibc 2.14以上版本 <img src="https://img-blog.csdnimg.cn/direct/ff52f1331dad43d58a31397d5466b722.png" alt="在这里插入图片描述">   博主是在Ubuntu18.04系统环境下安装，经过测试发现如果是安装cuda支持除了以上要求还需要：- cuda10.0以上- cmake 3.16以上版本
## 三、安装步骤

### 1、检查系统环境

  检查当前系统环境，可以看到OpenCL、libboost、cuda、glibc版本都满足要求，只有cmake版本不满足要求。

>  
 (base) ubuntu@test:~$ ldd --version ldd (Ubuntu GLIBC 2.27-3ubuntu1.5) 2.27 <img src="https://img-blog.csdnimg.cn/direct/042fbaf99c4f4b46aabc16fbe6b721d2.png" alt="在这里插入图片描述"> 


### 2、安装cmake2.24版本

  当前系统cmake已经安装，如果安装到默认路径下会有冲突需要先卸载，为了避免不影响现有系统运行，建议安装到其他目录，通过绝对路径调用此版本的cmake。我们这里安装在/opt/cmake目录下，安装完成后验证版本显示为3.24.2。

>  
 root@test:/opt# wget https://github.com/Kitware/CMake/releases/download/v3.24.2/cmake-3.24.2.tar.gz root@test:/opt# tar -zxvf cmake-3.24.2.tar.gz root@test:/opt# cd cmake-3.24.2 root@test:/opt/cmake# ./configure --prefix=/opt/cmake root@test:/opt/cmake# make -j8　　　　　　　　　　　　　　　　　　　　　　　　 root@test:/opt/cmake# make install … root@test:/opt/cmake# ./bin/cmake --version cmake version 3.24.2 


### 3、创建python虚拟环境

  我们可以使用anconda3管理python虚拟环境，关于anconda3安装见博文。

>  
 ubuntu@test:~/anaconda3$ conda create -n py38 python=3.8 … (base) ubuntu@test:~$ conda activate py38 


### 4、下载lightgbm

>  
 (py38) ubuntu@test:~$ git clone --recursive https://github.com/microsoft/LightGBM 


### 5、构建lightgbm

  构建的时候记得使用满足版本要求的cmake，为了不影响全局我们可以不添加环境变量，使用绝对路径cmake命令进行构建。

>  
 (py38) ubuntu@test:~$ cd LightGBM/ (py38) ubuntu@test:~/LightGBM$ mkdir build (py38) ubuntu@test:~/LightGBM$ cd build/ (py38) ubuntu@test:~/LightGBM/build$ /opt/cmake/bin/cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=/usr/local/cuda/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=/usr/local/cuda/include/ … … – Build files have been written to: /home/ubuntu/LightGBM/build 


### 6、编译lightgbm

>  
 (py38) ubuntu@test:~/LightGBM/build$ make -j8 … [100%] Linking CXX executable /home/ubuntu/LightGBM/lightgbm [100%] Built target lightgbm 


### 7、安装到python虚拟环境

  官网提供的编译步骤到第6步就结束了，第6步完成后会生产lightgbm二进制可执行文件，执行make install可以安装到系统中。如果我们需要安装到python虚拟环境，在LightGBM目录下有一个build-python.sh脚本，可以查看使用说明，执行如下命令可以安装到python虚拟环境中，记得要先切换到你需要安装的虚拟环境哦。

>  
 (py38) ubuntu@test:~/LightGBM/build$ cd … (py38) ubuntu@test:~/LightGBM$ sh ./build-python.sh install --precompile … Successfully installed lightgbm-4.1.0.99 numpy-1.24.4 scipy-1.10.1 cleaning up 


### 8、版本验证

  我们直接pip install lightgbm可以安装CPU版本，版本号是4.1.0，编译安装GPU版本号是4.1.0.99。python交互模式下引入lightgbm模块不报错，说明安装成功。 <img src="https://img-blog.csdnimg.cn/direct/746c1be72d8d4a128262e849f2521b05.png" alt="在这里插入图片描述">

### 9、执行测试

  是否真的执行GPU，我们编写一个简单测试代码，然后执行该python代码，执行结果可以看到程序正常执行，使用到了GPU，说明安装成功。

```
(py38) ubuntu@test:~/LightGBM$ cat test.py 
import lightgbm as lgb
import numpy as np

# 创建一个示例数据集
X_train = np.random.rand(100, 10)
y_train = np.random.randint(2, size=100)

# 将数据集加载到LightGBM的Dataset对象中
train_data = lgb.Dataset(X_train, label=y_train)

# 设置LightGBM的参数，包括使用GPU加速
params = {'boosting_type': 'gbdt',
          'objective': 'binary',
          'metric': 'binary_logloss',
          'device': 'gpu'}

# 在GPU上训练模型
model = lgb.train(params, train_data, num_boost_round=10)

# 打印模型的预测结果
print(model.predict(X_train))

```

<img src="https://img-blog.csdnimg.cn/direct/34475c672411428ea99aef1f6abb59ca.png" alt="在这里插入图片描述">## 10、总结   博主安装过程中主要遇到了两个问题，一个就是使用系统当前cmake版本构建的时候一直报错，安装cmake3.24版本后构建成功。另一个就是编译完成后不知道如何安装到python虚拟环境中，回头看结构目录、README文档，发现有一个专门的build-python.sh脚本。所以安装软件的时候一个是多找官方文档，多角度对比评估，仔细阅读README文档，查看软件包下的可读文件，也许你需要的答案就在其中。
