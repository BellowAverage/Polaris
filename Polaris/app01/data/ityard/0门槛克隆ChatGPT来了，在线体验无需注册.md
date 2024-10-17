
--- 
title:  0门槛克隆ChatGPT来了，在线体验无需注册 
tags: []
categories: [] 

---
来源：机器之心

以 ChatGPT、GPT4 为代表的 AI 应用和大模型火爆全球，被视为开启了新的科技工业革命和 AGI （通用人工智能）的新起点。不仅科技巨头间你追我赶，争相推出新品，许多学术界、工业界的 AI 大佬也纷纷投入投身相关创业浪潮。生成式 AI 正以 “天” 为单位，快速迭代，持续狂飙！

然而，OpenAI 并未将其开源，它们背后的技术细节有哪些？如何快速跟进、追赶并参与到此轮技术浪潮中？如何降低 AI 大模型构建和应用的高昂成本？如何保护核心数据与知识产权不会因使用第三方大模型 API 外泄？

作为当下最受欢迎的开源 AI 大模型解决方案，Colossal-AI 率先建立了包含**监督数据集收集 -&gt; 监督微调 -&gt; 奖励模型训练 -&gt; 强化学习微调的完整 RLHF 流程**，以 LLaMA 为基础预训练模型，推出 ColossalChat，**是目前最接近 ChatGPT 原始技术方案的实用开源项目！**

开源地址：https://github.com/hpcaitech/ColossalAI

包含以下内容：

1. **Demo：**可直接在线体验模型效果，无需注册或 waitinglist

2. **训练代码：**开源完整 RLHF 训练代码，已开源至含 7B 和 13B 两种模型

3. **数据集：**开源 104K 中、英双语数据集

4. **推理部署：**4bit 量化推理 70 亿参数模型仅需 4GB 显存

5. **模型权重：**仅需单台服务器少量算力即可快速复现

6. 更大规模模型、数据集、其他优化等将保持高速迭代添加

**平价模型，强大能力**

ColossalChat 仅需不到百亿参数，在大语言模型的基础上进行 RLHF 微调，即可掌握中、英双语能力，达到与 ChatGPT 和 GPT-3.5 类似的效果。

例如常识问答：

<img src="https://img-blog.csdnimg.cn/img_convert/fc316646c957ad58df7a8fba9b41b946.png" alt="fc316646c957ad58df7a8fba9b41b946.png">

中文应答：

<img src="https://img-blog.csdnimg.cn/img_convert/10ba5e17667ebd8503deceb7442c61eb.png" alt="10ba5e17667ebd8503deceb7442c61eb.png">

写一封邮件：

<img src="https://img-blog.csdnimg.cn/img_convert/3fb6283e0d9b808e259f20101cab63dd.png" alt="3fb6283e0d9b808e259f20101cab63dd.png">

写个算法：

<img src="https://img-blog.csdnimg.cn/img_convert/7c81252d8d2f9bf3affdde4b722e5e46.png" alt="7c81252d8d2f9bf3affdde4b722e5e46.png">

**完整 ChatGPT 克隆方案**

尽管 ChatGPT 和 GPT-4 等 GPT 系列模型非常强大，但是它们不太可能被完全开源。幸运的是，开源社区一直在不断努力。

例如 Meta 开源了 LLaMA 模型，该模型的参数量从 70 亿到 650 亿不等，130 亿参数即可胜过 1750 亿的 GPT-3 模型在大多数基准测试的表现。但是由于没有被指令微调（instruct tuning），因此实际生成效果不够理想。

斯坦福的 Alpaca 通过调用 OpenAI API，以 self-instruct 方式生成训练数据，使得仅有 70 亿参数的轻量级模型以极低成本微调后，即可获得媲美 GPT-3.5 这样千亿参数的超大规模语言模型的对话效果。

但是**现有开源方案都可以被视为只得到了人类反馈强化学习（RLHF）中第一步的监督微调模型**，没有进行后续的对齐和微调工作。同时 Alpaca 的训练数据集过小，语料只有英文，也在一定程度上限制了模型的性能。

而 **ChatGPT 和 GPT-4 的惊艳效果，还在于将 RLHF 引入训练过程，使得生成内容更加符合人类价值观。**

<img src="https://img-blog.csdnimg.cn/img_convert/71cdc7931ae0189907626e1bb8345227.png" alt="71cdc7931ae0189907626e1bb8345227.png">

**RLHF 的三个阶段 **

基于 LLaMA 模型，Colossal-AI 首个开源包含完整 RLHF 流程的类 Chat 模型复现方案 ColossalChat，是目前**最接近 ChatGPT 原始技术路线**的实用开源项目！

**训练数据集开源**

ColossalChat 开源了包含约 10 万条问答的中、英双语数据集。该数据集收集并清洗了社交平台上人们的真实提问场景作为种子数据集，利用 self-instruct 技术扩充数据，花费约 900 美元进行标注。对比其他 self-instruct 方法生成的数据集，该数据集的种子数据更加真实、丰富，生成的数据集涵盖的话题更多。该数据可以同时用于微调和 RLHF 训练。通过高质量的数据，ColossalChat 能进行更好地对话交互，同时支持中文。

<img src="https://img-blog.csdnimg.cn/img_convert/bd33e12f53aa07b80206501dadb329eb.png" alt="bd33e12f53aa07b80206501dadb329eb.png">

**ColossalChat 数据集收集流程**

**RLHF 算法复现**

RLHF-Stage1 是 supervised-fintuning，即使用上文提到的数据集进行模型微调。

RLHF-Stage2 训练了奖励模型，它通过对于同一个 prompt 的不同输出进行人工排序，得到对应分数，监督训练奖励模型。

RLHF-Stage3 使用了强化学习算法，是训练流程中最复杂的一部分：

<img src="https://img-blog.csdnimg.cn/img_convert/a23689575bae76111131b9266a08c2ef.jpeg" alt="a23689575bae76111131b9266a08c2ef.jpeg">

**RLHF-Stage3 算法流程图**

在 PPO 部分，ColossalChat 分为两个阶段进行：首先是 Make Experience 部分，利用 SFT 、Actor、RM、Critic 模型计算生成 Experience 存入 buffer 中；之后是参数更新部分，利用 Experience 计算策略损失和价值损失。

在 PTX 部分，ColossalChat 计算 Actor 输出 response 和输入语料的回答部分的交叉熵损失函数，用来在 PPO 梯度中加入预训练梯度，以保持语言模型原有性能防止遗忘。最后将策略损失、价值损失和 PTX 损失加和进行反向传播和参数更新。

**快速上手**

ColossalChat 开源了基于 LLaMA 模型，复现训练 ChatGPT 三个阶段的完整代码。

第一阶段，训练 SFT 模型：

```
# Training with a 4-GPU servers
colossalai run --nproc_per_node=4 train_sft.py \
    --pretrain "/path/to/LLaMa-7B/" \
    --model 'llama' \
    --strategy colossalai_zero2 \
    --log_interval 10 \
    --save_path  /path/to/Coati-7B \
    --dataset /path/to/data.json \
    --batch_size 4 \
    --accimulation_steps 8 \
    --lr 2e-5
```

第二阶段，训练奖励模型：

```
# Training with a 4-GPU servers
colossalai run --nproc_per_node=4 train_reward_model.py \
    --pretrain "/path/to/LLaMa-7B/" \
    --model 'llama' \
    --strategy colossalai_zero2 \
    --dataset /path/to/datasets
```

第三阶段，使用 RL 训练：

```
# Training with a 8-GPU servers
colossalai run --nproc_per_node=8 train_prompts.py prompts.csv \
    --strategy colossalai_zero2 \
    --pretrain "/path/to/Coati-7B" \
    --model 'llama' \
    --pretrain_dataset /path/to/dataset
```

在获得最终模型权重后，还可通过量化降低推理硬件成本，并启动在线推理服务，仅需单张约 4GB 显存的 GPU 即可完成 70 亿参数模型推理服务部署。

```
python server.py/path/to/pretrained --quant 4bit --gptq_checkpoint /path/to/coati-7b-4bit-128g.pt --gptq_group_size 128
```

**系统性能优化与开发加速**

ColossalChat 能够快速跟进 ChatGPT 完整 RLHF 流程复现，离不开 AI 大模型基础设施 Colossal-AI 及相关优化技术的底座支持，相同条件下**训练速度**相比 Alpaca 采用的 FSDP (Fully Sharded Data Parallel) **可提升三倍左右**。

**系统基础设施 Colossal-AI**

AI 大模型开发系统 Colossal-AI 为该方案提供了基础支持，它可基于 PyTorch 高效快速部署 AI 大模型训练和推理，从而降低 AI 大模型应用的成本。Colossal-AI 由加州伯克利大学杰出教授 James Demmel 和新加坡国立大学校长青年教授尤洋领导开发。自从它开源以来，Colossal-AI 已经多次在 GitHub 热榜位列世界第一，获得 GitHub Star 约两万颗，并成功入选 SC、AAAI、PPoPP、CVPR、ISC 等国际 AI 与 HPC 顶级会议的官方教程。

**减少内存冗余的 ZeRO + Gemini**

Colossal-AI 支持使用无冗余优化器 (ZeRO) 提高内存使用效率，低成本容纳更大模型，同时不影响计算粒度和通信效率。自动 Chunk 机制可以进一步提升 ZeRO 的性能，提高内存使用效率，减少通信次数并避免内存碎片。异构内存空间管理器 Gemini 支持将优化器状态从 GPU 显存卸载到 CPU 内存或硬盘空间，以突破 GPU 显存容量限制，扩展可训练模型的规模，降低 AI 大模型应用成本。

**使用 LoRA 低成本微调**

Colossal-AI 支持使用低秩矩阵微调（LoRA）方法，对 AI 大模型进行低成本微调。LoRA 方法认为大语言模型是过参数化的，而在微调时，参数改变量是一个低秩矩阵。因此，可以将这个矩阵分解为两个更小的矩阵的乘积。在微调过程中，大模型的参数被固定，只有低秩矩阵参数被调整，从而显著减小了训练所需的参数量，并降低成本。

**低成本量化推理**

<img src="https://img-blog.csdnimg.cn/img_convert/c40f267a6019b0425c27d7dcca646923.png" alt="c40f267a6019b0425c27d7dcca646923.png">

**GPTQ 量化**

为降低推理部署成本，Colossal-AI 使用 GPTQ 4bit 量化推理。在 GPT/OPT/BLOOM 类模型上，它比传统的 RTN (rount-to-nearest) 量化技术能够获得更好的 Perplexity 效果。相比常见的 FP16 推理，它可将显存消耗降低 75%，只损失极少量的吞吐速度与 Perplexity 性能。

以 ColossalChat-7B 为例，在使用 4bit 量化推理时，70 亿参数模型仅需大约 4GB 显存即可完成短序列（生成长度为 128 ）推理，在普通消费级显卡上即可完成（例如 RTX 3060 Laptop），仅需一行代码即可使用。

```
if args.quant == '4bit':
    model = load_quant (args.pretrained, args.gptq_checkpoint, 4, args.gptq_group_size)
```

如果采用高效的异步卸载技术 (offload)，还可以进一步降低显存要求，使用更低成本的硬件推理更大的模型。

**ColossalChat和Alpaca的区别**

1. ColossalChat 开源了**第一个完整的RLHF pipeline**，斯坦福Alpaca没有做 RLHF，也就是没有做 Stage 2 和 Stage 3。

2. ColossalChat 采用了更多的指令数据，质量更好，范围更大，并使用强化学习做alignment 使回答更接近人类。

3. ColossalChat训练流程集成了Colossal-AI的诸多系统优化，同等数据集和模型大小的训练速度可以比Alpaca**快3倍左右**，让科研人员和中小企业也能独立训练部署自己的会话系统。

4.ColossalChat 团队自己采集了更多数据集：训练的英文一共 24M tokens，中文大约 30M tokens，总共约 54M tokens。其中 ColossalChat 自己收集的数据集英文 6M，中文 18M tokens。

以下是 ColossalChat 和 Alpaca 在语言对话上的一些表现 (上面是ColossalChat，下面是Alpaca)。

用 Python 写 Quicksort：

<img src="https://img-blog.csdnimg.cn/img_convert/bf3a82d23f35e3253cd5f57a1a50f7b0.jpeg" alt="bf3a82d23f35e3253cd5f57a1a50f7b0.jpeg">

给教授写邮件请求推荐信：

<img src="https://img-blog.csdnimg.cn/img_convert/2ac114d90a8af9170eca983bcf07a5ca.jpeg" alt="2ac114d90a8af9170eca983bcf07a5ca.jpeg">

**开放协作**

尽管已经进一步引入 RLHF，但由于算力和数据集有限，在部分场景下的实际性能仍有提升空间。

<img src="https://img-blog.csdnimg.cn/img_convert/b908a4783f15faad5da7e25c6e48bb6a.png" alt="b908a4783f15faad5da7e25c6e48bb6a.png">

幸运的是，不同以往 AI 大模型与前沿技术仅由少数科技巨头垄断，PyTorch、Hugging Face 和 OpenAI 等开源社区与初创企业在本轮浪潮中也起到了关键作用。借鉴开源社区的成功经验，Colossal-AI 欢迎各方参与共建，拥抱大模型时代！

可通过以下方式联系或参与：

1. 在 GitHub 发布 issue 或提交 pull request (PR)

2. 加入 Colossal-AI 用户微信或 Slack 群交流

3. 发送正式合作提案到邮箱 youy@comp.nus.edu.sg

开源地址：

https://github.com/hpcaitech/ColossalAI
- - - - - 