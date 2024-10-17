
--- 
title:  银河麒麟之PaddleNLP大模型部署 
tags: []
categories: [] 

---
## 一、PaddleNLP简介

  PaddleNLP是一款简单易用且功能强大的自然语言处理和大语言模型(LLM)开发库。聚合业界优质预训练模型并提供开箱即用的开发体验，覆盖NLP多场景的模型库搭配产业实践范例可满足开发者灵活定制的需求。2023年8月15日PaddleNLP v2.6发布，发布全流程大模型工具链，涵盖预训练，精调，压缩，推理以及部署等各个环节，为用户提供端到端的大模型方案和一站式的开发体验；内置4D并行分布式Trainer，高效微调算法LoRA/Prefix Tuning, 自研INT8/INT4量化算法等等；全面支持LLaMA 1/2, BLOOM, ChatGLM 1/2, GLM, OPT等主流大模型本博文将以银河麒麟V10系统环境下部署paddlenlp为例做部署步骤介绍，系统环境如下：
- 操作系统：银河麒麟kylinV10.1- python版本：3.11.5- 显卡驱动版本：545.23.08- paddle版本：2.6.0- paddlenlp版本：2.7.2
## 二、部署要求

  环境依赖要求如下：
- python &gt;= 3.7- paddlepaddle &gt;= 2.5.1- 如需大模型功能，请使用 paddlepaddle-gpu &gt;= 2.5.1
## 三、部署步骤

### 1、检查系统是否有GPU显卡

  使用命令"lspci | grep -i nvidia"查看主机是否有显卡，paddlenlp在cpu环境也可以运行，但是如果需要大模型功能需要GPU。 <img src="https://img-blog.csdnimg.cn/direct/d64e2ee91f6840c690d8a1e4c7c9fc41.png" alt="在这里插入图片描述">

### 2、安装显卡驱动

  银河麒麟环境下安装显卡驱动参考博文。使用nvidia-smi命令可以确认是否安装驱动，以及查看显卡参数和运行信息。 <img src="https://img-blog.csdnimg.cn/direct/0cd0afa5cc0540fe922332044769d626.png" alt="在这里插入图片描述">

### 3、安装anaconda3

  anaconda3的安装可以参考博文，虽然系统略有区别，但是安装方式是一样的。anaconda3不是必须的，只是如果我们需要使用不同的python版本进行验证测试，anaconda3是一个非常不错的选择，通过虚环境管理，非常方便。

>  
 (base) wuhs@test:~/anaconda3$ conda --version conda 24.1.2 


### 4、创建一个paddlenlp虚拟环境

  安装完成anaconda3后我们创建一个python版本为3.11.5的虚拟环境。

>  
 (base) wuhs@test:~$ conda create -n paddlenlp python=3.11.5 


### 5、切换到paddlenlp虚拟环境

  通过conda activate切换到新建的paddlenlp虚拟环境。

>  
 (base) wuhs@test:~$ conda activate paddlenlp (paddlenlp) wuhs@test:~$ 


### 6、安装paddle-gpu

  访问百度飞浆 <img src="https://img-blog.csdnimg.cn/direct/0dc74b56fe1f4d74ae254035bc218f05.png" alt="在这里插入图片描述">

>  
 (paddlenlp) wuhs@test:~$ conda install paddlepaddle-gpu==2.6.0 cudatoolkit=11.7 -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/ -c conda-forge … 


### 7、验证paddle

>  
 (paddlenlp) wuhs@test:~$ python Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux Type “help”, “copyright”, “credits” or “license” for more information. &gt;&gt;&gt; import paddle &gt;&gt;&gt; paddle.**version** ‘2.6.0’ 


### 8、下载paddlenlp的requirements文件

  访问，可以下载该文件或者复制文件内容自己创建requirements.txt文件。 <img src="https://img-blog.csdnimg.cn/direct/4aefa9a002024035a9c8dcf5606446be.png" alt="在这里插入图片描述">

>  
 (paddlenlp) wuhs@test :~/anaconda3/requirementfiles$ cat paddlenlp_github.txt jieba colorlog colorama seqeval dill&lt;0.3.5 multiprocess&lt;=0.70.12.2 datasets &gt;= 2.0.0 tqdm paddlefsl sentencepiece huggingface_hub&gt;=0.11.1 onnx&gt;=1.10.0 protobuf==3.20.2 # onnx require: protobuf&lt;4,&gt;=3.20.2, paddle require different version on platforms, refer to: https://github.com/PaddlePaddle/Paddle/blob/cd88156a369bbfb83d6306f89e0ae6ebd78b8040/python/requirements.txt#L3 paddle2onnx Flask-Babel visualdl fastapi uvicorn typer rich safetensors 


### 9、根据requirements文件安装软件依赖

  根据创建的requirements.txt文件，使用pip3命令安装相关软件包。

>  
 (paddlenlp) wuhs@test:~/data/requirements$ pip3 install -r paddlenlp_github.txt … Successfully installed Babel-2.14.0 Flask-3.0.2 Flask-Babel-4.0.0 Jinja2-3.1.3 MarkupSafe-2.1.5 Werkzeug-3.0.1 aiohttp-3.9.3 aiosignal-1.3.1 annotated-types-0.6.0 attrs-23.2.0 bce-python-sdk-0.9.5 blinker-1.7.0 charset-normalizer-3.3.2 click-8.1.7 colorama-0.4.6 colorlog-6.8.2 contourpy-1.2.0 cycler-0.12.1 datasets-2.18.0 dill-0.3.4 fastapi-0.110.0 filelock-3.13.1 fonttools-4.49.0 frozenlist-1.4.1 fsspec-2024.2.0 future-1.0.0 huggingface_hub-0.21.3 itsdangerous-2.1.2 jieba-0.42.1 joblib-1.3.2 kiwisolver-1.4.5 markdown-it-py-3.0.0 matplotlib-3.8.3 mdurl-0.1.2 multidict-6.0.5 multiprocess-0.70.12.2 onnx-1.15.0 packaging-23.2 paddle2onnx-1.1.0 paddlefsl-1.1.0 pandas-2.2.1 protobuf-3.20.2 psutil-5.9.8 pyarrow-15.0.0 pyarrow-hotfix-0.6 pycryptodome-3.20.0 pydantic-2.6.3 pydantic-core-2.16.3 pygments-2.17.2 pyparsing-3.1.1 python-dateutil-2.9.0.post0 pytz-2024.1 pyyaml-6.0.1 rarfile-4.1 requests-2.31.0 rich-13.7.1 safetensors-0.4.2 scikit-learn-1.4.1.post1 scipy-1.12.0 sentencepiece-0.2.0 seqeval-1.2.2 six-1.16.0 starlette-0.36.3 threadpoolctl-3.3.0 tqdm-4.66.2 typer-0.9.0 tzdata-2024.1 urllib3-2.2.1 uvicorn-0.27.1 visualdl-2.5.3 xxhash-3.4.1 yarl-1.9.4 


### 10、安装paddlenlp

  安装完成依赖后安装paddlenlp，使用pip3命令直接安装即可。

>  
 (paddlenlp) wuhs@test:~/anaconda3/requirementfiles$ pip3 install paddlenlp … Successfully installed aistudio-sdk-0.1.7 paddlenlp-2.7.2 pybind11-2.11.1 tool-helpers-0.1.1 


### 11、查验paddlenlp

  安装完成之后进入python交互模式，导入paddlenlp模块，无报错说明安装成功，就开始开始使用啦。

>  
 (paddlenlp) wuhs@test :~/anaconda3/requirementfiles$ pip3 show paddlenlp Name: paddlenlp Version: 2.7.2 (paddlenlp) wuhs@test :~/data/code$ python Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux Type “help”, “copyright”, “credits” or “license” for more information. &gt;&gt;&gt; import paddlenlp &gt;&gt;&gt; paddlenlp.**version** ‘2.7.2.post’ 

