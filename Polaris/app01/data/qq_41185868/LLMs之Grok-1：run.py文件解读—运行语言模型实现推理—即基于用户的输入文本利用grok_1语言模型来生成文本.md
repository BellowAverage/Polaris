
--- 
title:  LLMs之Grok-1：run.py文件解读—运行语言模型实现推理—即基于用户的输入文本利用grok_1语言模型来生成文本 
tags: []
categories: [] 

---
LLMs之Grok-1：run.py文件解读—运行语言模型实现推理—即基于用户的输入文本利用grok_1语言模型来生成文本





**目录**

























## **run.py文件解读****—运行语言模型实现推理—即基于用户的输入文本****利用grok_1语言模型来生成文本**

**<strong>源码地址**</strong>：



### **<strong><strong>概述**</strong></strong>

这段代码使用了一个预训练的语言模型 grok_1_model 来生成文本。代码首先定义了模型的配置，然后创建了一个 InferenceRunner 对象来运行模型推理。最后，代码定义了一个输入字符串，并使用 sample_from_model 函数从模型中获取一个样本，将其打印出来。





### **<strong><strong>1、加载预训练的语言模型 grok_1**</strong></strong>

#### **<strong><strong>1.1、**</strong>**<strong>定义模型的配置**</strong></strong>

定义一个名为 grok_1_model 的 LanguageModelConfig 对象，该对象包含有关模型配置的详细信息，例如词汇表大小、序列长度、嵌入层初始化比例、输出和嵌入层的乘数比例等。模型的架构是一个 TransformerConfig 对象，其中包括了嵌入大小、扩展因子、键大小、头数量、层数、注意力输出乘数等参数。





### **<strong><strong>2、定义并**</strong>**<strong>初始化推理运行器**</strong></strong>

#### **<strong><strong>2.1、**</strong>**<strong>创建一个 InferenceRunner 对象**</strong>**<strong>(**</strong>**<strong>用于运行模型推理**</strong>**<strong>)**</strong></strong>

InferenceRunner 接受一个 ModelRunner 对象作为参数，该对象包含了模型配置、批处理大小、检查点路径等信息。InferenceRunner 还需要指定一些其他参数，如名称、加载路径、分词器路径、本地和跨主机配置等。





#### **<strong><strong>2.2、**</strong>**<strong>调用 inference_runner.initialize() 方法初始化推理运行器。**</strong></strong>

#### **<strong><strong>2.3、**</strong>**<strong>调用 inference_runner.run() 方法运行模型推理并获取生成器。**</strong></strong>

### **<strong><strong>3、模型生成**</strong></strong>

定义一个输入字符串 inp，然后使用 sample_from_model 函数从生成器中获取一个样本，并将其打印出来。







## **全部代码**

```
# Copyright 2024 X.AI Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from model import LanguageModelConfig, TransformerConfig, QuantizedWeight8bit as QW8Bit
from runners import InferenceRunner, ModelRunner, sample_from_model


CKPT_PATH = "./checkpoints/"


def main():
    grok_1_model = LanguageModelConfig(
        vocab_size=128 * 1024,
        pad_token=0,
        eos_token=2,
        sequence_len=8192,
        embedding_init_scale=1.0,
        output_multiplier_scale=0.5773502691896257,
        embedding_multiplier_scale=78.38367176906169,
        model=TransformerConfig(
            emb_size=48 * 128,
            widening_factor=8,
            key_size=128,
            num_q_heads=48,
            num_kv_heads=8,
            num_layers=64,
            attn_output_multiplier=0.08838834764831845,
            shard_activations=True,
            # MoE.
            num_experts=8,
            num_selected_experts=2,
            # Activation sharding.
            data_axis="data",
            model_axis="model",
        ),
    )
    inference_runner = InferenceRunner(
        pad_sizes=(1024,),
        runner=ModelRunner(
            model=grok_1_model,
            bs_per_device=0.125,
            checkpoint_path=CKPT_PATH,
        ),
        name="local",
        load=CKPT_PATH,
        tokenizer_path="./tokenizer.model",
        local_mesh_config=(1, 8),
        between_hosts_config=(1, 1),
    )
    inference_runner.initialize()
    gen = inference_runner.run()

    inp = "The answer to life the universe and everything is of course"
    print(f"Output for prompt: {inp}", sample_from_model(gen, inp, max_len=100, temperature=0.01))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

```






