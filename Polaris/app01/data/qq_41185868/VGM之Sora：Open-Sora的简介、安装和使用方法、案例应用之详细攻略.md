
--- 
title:  VGM之Sora：Open-Sora的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
VGM之Sora：Open-Sora的简介、安装和使用方法、案例应用之详细攻略



>  
 **导读**：2024年3月18日，Colossal-AI团队开源了全球首个类Sora架构的视频生成模型Open-Sora 1.0，全面公开，包含完整的训练流程、所有训练细节和模型权重。 
 &gt;&gt; Open-Sora 1.0采用了Diffusion Transformer结构，在空时注意力上加入了文本编码机制，可以生成根据描述的视频。 
 &gt;&gt; 该项目采用了三个阶段的训练流程：首先在大量图像数据上预训练，得到初始化权重；然后在大量视频数据上预训练，学习视频时序关系；最后在少量高质量视频数据上微调提升生成质量。每个阶段都会基于前一阶段权重继续训练，实现了从低到高的逐步过渡训练。 
 &gt;&gt; 该项目提供了数据预处理脚本，可以自动为视频数据生成描述，降低了项目入门难度。 
 &gt;&gt; 该项目可以在64块GPU上以1万美元的成本实现复现，采用了模型和训练策略优化可以实现更高效训练。 
 &gt;&gt; 模型结构采用空时注意力机制，训练效率比全Attention高5倍。 
 &gt;&gt; 该项目当前版本视频生成质量和描述依赖能力还需提升，后续将使用更多数据实现更高质量长时长视频生成。未来将使用更多数据生成更高质量长视频，并在电影、游戏等领域实际应用。 
 &gt;&gt; 该项目旨在通过开源和持续优化，推动视频合成技术在电影、游戏等领域的发展。 






**目录**



















## **Open-Sora的简介**

<img alt="" height="249" src="https://img-blog.csdnimg.cn/direct/e6de81087c3a4544981dd020ad7e3345.png" width="249">

2024年3月18日，Colossal-AI团队重磅发布Open-Sora项目是一项致力于高效制作高质量视频，并使所有人都能使用其模型、工具和内容的计划。 通过采用开源原则，Open-Sora 不仅实现了先进视频生成技术的低成本普及，还提供了一个精简且用户友好的方案，简化了视频制作的复杂性。 通过 Open-Sora，我们希望更多开发者一起探索内容创作领域的创新、创造和包容。

**GitHub地址**：





### **<strong><strong>1、更新**</strong></strong>

[2024.03.18] ��� 我们发布了Open-Sora 1.0，这是一个完全开源的视频生成项目。

Open-Sora 1.0 支持视频数据预处理、 加速训练、推理等全套流程。

我们提供的模型权重只需 3 天的训练就能生成 2 秒的 512x512 视频。

[2024.03.04] Open-Sora：开源Sora复现方案，成本降低46%，序列扩充至近百万





### **<strong><strong>2、**</strong>**<strong>新功能**</strong></strong>

���Open-Sora-v1 已发布。这里提供了模型权重。只需 400K 视频片段和在单卡 H800 上训200天（类比Stable Video Diffusion 的 152M 样本），我们就能生成 2 秒的 512×512 视频。

✅ 从图像扩散模型到视频扩散模型的三阶段训练。我们提供每个阶段的权重。

✅ 支持训练加速，包括Transformer加速、更快的 T5 和 VAE 以及序列并行。在对 64x512x512 视频进行训练时，Open-Sora 可将训练速度提高55%。详细信息请参见训练加速。

✅ 我们提供用于数据预处理的视频切割和字幕工具。有关说明请点击此处，我们的数据收集计划请点击 数据集。

✅ 我们发现来自VideoGPT的 VQ-VAE 质量较低，因此采用了来自Stability-AI 的高质量 VAE。我们还发现使用添加了时间维度的采样会导致生成质量降低。更多讨论，请参阅我们的 报告。

✅ 我们研究了不同的架构，包括 DiT、Latte 和我们提出的 STDiT。我们的STDiT在质量和速度之间实现了更好的权衡。更多讨论，请参阅我们的 报告。

✅ 支持剪辑和 T5 文本调节。

✅ 通过将图像视为单帧视频，我们的项目支持在图像和视频（如 ImageNet 和 UCF101）上训练 DiT。更多说明请参见 指令解析。

✅ 利用DiT、Latte 和 PixArt 的官方权重支持推理。







## **Open-Sora的安装和使用方法**

### **1、安装环境及其依赖**
<td style="vertical-align:top;width:63.25pt;"> **<strong>创建虚拟环境**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 创建虚拟环境 conda create -n opensora python=3.10 </td>



conda create -n opensora python=3.10
<td style="vertical-align:top;width:63.25pt;"> **<strong>安装 torch**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 安装 torch 下面的命令适用于 CUDA 12.1，请根据您自己的 CUDA 版本从 https://pytorch.org/get-started/locally/ 中选择安装命令 pip3 install torch torchvision </td>



下面的命令适用于 CUDA 12.1，请根据您自己的 CUDA 版本从 https://pytorch.org/get-started/locally/ 中选择安装命令
<td style="vertical-align:top;width:63.25pt;"> **<strong>安装 Flash Attention（可选）**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 安装 Flash Attention（可选） pip install packaging ninja pip install flash-attn --no-build-isolation </td>



pip install packaging ninja
<td style="vertical-align:top;width:63.25pt;"> **<strong>安装 Apex（可选）**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 安装 Apex（可选） pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" git+https://github.com/NVIDIA/apex.git </td>



pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" git+https://github.com/NVIDIA/apex.git
<td style="vertical-align:top;width:63.25pt;"> **<strong>安装 XFormers**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 安装 XFormers pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu121 </td>



pip3 install -U xformers --index-url https://download.pytorch.org/whl/cu121



### 2、安装项目
<td style="vertical-align:top;width:63.25pt;"> **<strong>安装该项目**</strong>  </td><td style="vertical-align:top;width:362.85pt;"> 安装该项目 git clone https://github.com/hpcaitech/Open-Sora cd Open-Sora pip install -v . </td>



git clone https://github.com/hpcaitech/Open-Sora

pip install -v .



### 3、下载模型权重

|分辨率|数据|迭代次数|批量大小|GPU 天数 (H800)|网址
|------
|16×256×256|366K|80k|8×64|117|
|16×256×256|20K HQ|24k|8×64|45|
|16×512×512|20K HQ|20k|2×64|35|

我们模型的权重部分由 初始化。参数数量为 724M。有关训练的更多信息，请参阅我们的 ****。有关数据集的更多信息，请参阅。HQ 表示高质量。 :warning: **局限性**：我们的模型是在有限的预算内训练出来的。质量和文本对齐度相对较差。特别是在生成人类时，模型表现很差，无法遵循详细的指令。我们正在努力改进质量和文本对齐。



### 4、推理

要使用我们提供的权重进行推理，首先要将权重下载到pretrained_models/t5_ckpts/t5-v1_1-xxl 中。然后下载模型权重。运行以下命令生成样本。请参阅自定义配置。

```
# Sample 16x256x256 (5s/sample, 100 time steps, 22 GB memory)
torchrun --standalone --nproc_per_node 1 scripts/inference.py configs/opensora/inference/16x256x256.py --ckpt-path ./path/to/your/ckpt.pth --prompt-path ./assets/texts/t2v_samples.txt
# Auto Download
torchrun --standalone --nproc_per_node 1 scripts/inference.py configs/opensora/inference/16x256x256.py --ckpt-path OpenSora-v1-HQ-16x256x256.pth --prompt-path ./assets/texts/t2v_samples.txt

# Sample 16x512x512 (20s/sample, 100 time steps, 24 GB memory)
torchrun --standalone --nproc_per_node 1 scripts/inference.py configs/opensora/inference/16x512x512.py --ckpt-path ./path/to/your/ckpt.pth --prompt-path ./assets/texts/t2v_samples.txt
# Auto Download
torchrun --standalone --nproc_per_node 1 scripts/inference.py configs/opensora/inference/16x512x512.py --ckpt-path OpenSora-v1-HQ-16x512x512.pth --prompt-path ./assets/texts/t2v_samples.txt

# Sample 64x512x512 (40s/sample, 100 time steps)
torchrun --standalone --nproc_per_node 1 scripts/inference.py configs/opensora/inference/64x512x512.py --ckpt-path ./path/to/your/ckpt.pth --prompt-path ./assets/texts/t2v_samples.txt

# Sample 64x512x512 with sequence parallelism (30s/sample, 100 time steps)
# sequence parallelism is enabled automatically when nproc_per_node is larger than 1
torchrun --standalone --nproc_per_node 2 scripts/inference.py configs/opensora/inference/64x512x512.py --ckpt-path ./path/to/your/ckpt.pth --prompt-path ./assets/texts/t2v_samples.txt
```

我们在 H800 GPU 上进行了速度测试。如需使用其他模型进行推理，请参阅获取更多说明。



### 5、数据处理

高质量数据是高质量模型的关键。有我们使用过的数据集和数据收集计划。我们提供处理视频数据的工具。目前，我们的数据处理流程包括以下步骤：
- 下载数据集。[]- 将视频分割成片段。 []- 生成视频字幕。 []


### 6、训练

#### T1、单个节点上启动训练

要启动训练，首先要将权重下载到pretrained_models/t5_ckpts/t5-v1_1-xxl 中。然后运行以下命令在单个节点上启动训练。

```
# 1 GPU, 16x256x256
torchrun --nnodes=1 --nproc_per_node=1 scripts/train.py configs/opensora/train/16x256x512.py --data-path YOUR_CSV_PATH
# 8 GPUs, 64x512x512
torchrun --nnodes=1 --nproc_per_node=8 scripts/train.py configs/opensora/train/64x512x512.py --data-path YOUR_CSV_PATH --ckpt-path YOUR_PRETRAINED_CKPT
```



#### T2、多个节点上启动训练

要在多个节点上启动训练，请根据 准备一个主机文件，并运行以下命令。

```
colossalai run --nproc_per_node 8 --hostfile hostfile scripts/train.py configs/opensora/train/64x512x512.py --data-path YOUR_CSV_PATH --ckpt-path YOUR_PRETRAINED_CKPT
```





## **Open-Sora的案例应用**

更新中……








