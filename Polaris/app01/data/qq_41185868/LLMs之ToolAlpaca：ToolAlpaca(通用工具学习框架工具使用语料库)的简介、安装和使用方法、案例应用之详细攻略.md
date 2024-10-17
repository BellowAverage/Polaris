
--- 
title:  LLMs之ToolAlpaca：ToolAlpaca(通用工具学习框架/工具使用语料库)的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLMs之ToolAlpaca：ToolAlpaca(通用工具学习框架/工具使用语料库)的简介、安装和使用方法、案例应用之详细攻略





**目录**







































## **<strong><strong>ToolAlpaca**</strong>**<strong>的简介**</strong></strong>

<img alt="" height="610" src="https://img-blog.csdnimg.cn/direct/f6fa659f17c5452bb6ed64fca2df8826.png" width="642">

2023年6月8日，中国科学院发布ToolAlpaca，ToolAlpaca是一个面向紧凑语言模型的3000个模拟案例的通用工具学习框架，旨在最小化人工监督的情况下，在紧凑语言模型中学习通用工具使用能力。它通过生成一个工具使用语料库来处理工具学习挑战，该语料库通过一个多智能体模拟环境提供，包含来自400多种工具的3.9千个工具使用实例。

**<strong>论文地址**</strong>：

**<strong>GitHub地址**</strong>：



**<strong>数据集源地址**</strong>：、

**<strong>查阅地**</strong>址：





### **0、《ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases》翻译与解读**
<td style="vertical-align:top;width:38.75pt;"> **<strong>地址**</strong> </td><td style="vertical-align:top;width:387.35pt;"> 论文地址： </td>

论文地址：
<td style="vertical-align:top;width:38.75pt;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:387.35pt;"> 2023年6月8日 </td>

2023年6月8日
<td style="vertical-align:top;width:38.75pt;"> **<strong>作者**</strong> </td><td style="vertical-align:top;width:387.35pt;"> 中国科学院 </td>

中国科学院
<td style="vertical-align:top;width:38.75pt;"> **<strong>摘要**</strong> </td><td style="vertical-align:top;width:387.35pt;"> 使大型语言模型有效地利用现实世界工具是实现具体化智能的关键。现有的工具学习方法要么主要依赖于非常大的语言模型，如GPT-4，以零样本的方式获得泛化的工具使用能力，要么利用监督学习在紧凑模型上训练有限范围内的工具。然而，目前尚不确定较小的语言模型是否可以在没有特定工具训练的情况下获得泛化的工具使用能力。为了解决这个问题，本文引入了**<strong>ToolAlpaca**</strong>，这是一个新颖的框架，旨在自动生成多样化的工具使用语料库，并在最少的人工干预下，在紧凑语言模型上学习泛化的工具使用能力。具体来说，ToolAlpaca首先通过构建一个多智能体模拟环境，自动创建了一个高度多样化的工具使用语料库。该语料库包含来自超过400个现实世界工具API的3938个工具使用实例，涵盖50个不同类别。随后，构建的语料库被用于微调紧凑语言模型，分别得到了两个模型，即ToolAlpaca-7B和ToolAlpaca-13B。最后，我们评估了这些模型在没有特定训练的情况下利用未见过的工具的能力。实验结果表明，ToolAlpaca实现了与GPT-3.5等非常大语言模型相媲美的有效泛化工具使用能力，证明了紧凑语言模型学习泛化的工具使用能力是可行的。 </td>

使大型语言模型有效地利用现实世界工具是实现具体化智能的关键。现有的工具学习方法要么主要依赖于非常大的语言模型，如GPT-4，以零样本的方式获得泛化的工具使用能力，要么利用监督学习在紧凑模型上训练有限范围内的工具。然而，目前尚不确定较小的语言模型是否可以在没有特定工具训练的情况下获得泛化的工具使用能力。为了解决这个问题，本文引入了**<strong>ToolAlpaca**</strong>，这是一个新颖的框架，旨在自动生成多样化的工具使用语料库，并在最少的人工干预下，在紧凑语言模型上学习泛化的工具使用能力。具体来说，ToolAlpaca首先通过构建一个多智能体模拟环境，自动创建了一个高度多样化的工具使用语料库。该语料库包含来自超过400个现实世界工具API的3938个工具使用实例，涵盖50个不同类别。随后，构建的语料库被用于微调紧凑语言模型，分别得到了两个模型，即ToolAlpaca-7B和ToolAlpaca-13B。最后，我们评估了这些模型在没有特定训练的情况下利用未见过的工具的能力。实验结果表明，ToolAlpaca实现了与GPT-3.5等非常大语言模型相媲美的有效泛化工具使用能力，证明了紧凑语言模型学习泛化的工具使用能力是可行的。





### **1、****数据集列表**

train_data.json：400多种API的训练数据 

eval_simulated.json：10个模拟API的评估数据

eval_real.json：11个真实API的评估数据，一些API需要认证。







### **2、****数据格式**

```
{
  "Name": "公共API中的名称",
  "Description": "公共API中的描述",
  "Category": "公共API中的类别",
  "Introduction": "由LLM生成的介绍",
  "Functions": "由LLM生成的论文版本NLDocumentation",
  "Documentation": "str(json)，由LLM生成的OpenAPI规范文档",
  "NLDocumentation": "类似于Functions的自然语言文档，从Documentation转换而来",
  "Function_Description": "NLDocumentation中每个函数的描述",
  "Function_Projection": "函数到HTTP请求方法的映射",
  "Instructions": "由LLM生成的指令",
  "Instances": [
    {
      "input": "使用agent的init指令",
      "output": "assistant agent的最终输出",
      "Final Thought": "输出之前的最终想法，来自assistant agent",
      "intermediate_steps": [
        [
          [
            "来自assistant agent的动作",
            "来自assistant agent的动作输入，str(json)",
            "想法 + 动作 + 动作输入，assistant agent的输出"
          ],
          "来自[user agent, 类型检查Python代码, 工具执行agent]的观察"
        ]
      ]
    }
  ]
}

```





## **<strong><strong>ToolAlpaca**</strong>**<strong>的安装和使用方法**</strong></strong>

### **1、****数据集生成 **

#### **克隆此仓库并安装包 **

```
git clone git@github.com:tangqiaoyu/ToolAlpaca.git
cd ToolAlpaca
pip install -r requirements.txt
```



#### **下载public-api数据**



```
python tool_maker/preprocess_public_apis.py -api data/public_apis.json
```



#### **下载公共 API 数据**



```
python tool_maker/preprocess_public_apis.py -api data/public_apis.json
```







### **2、****工具集构建**



```
export PYTHONPATH=$PYTHONPAT:$(pwd)
export OPENAI_API_KEY=""
python tool_maker/get_elements.py -api data/public_apis.json -out ./data
python tool_maker/natural_language_documentation.py -api ./data/api_data.json
```





#### **工具使用实例生成**



```
python instance_generation/instruction.py -api ./data/api_data.json -out ./data
python instance_generation/simulator.py -api ./data/api_data.json
python instance_generation/generation.py -api ./data/api_data.json -out ./data --use_cache
```





### **3、****训练**

要训练 Toolapaca，我们需要创建一个提示以组织数据集，使其以标准 SFT 训练代码可读的格式呈现，类似于 build_dataset.py 中所做的操作。之后，我们可以使用标准的 SFT 方法进行训练，仅优化思想、行动和行动输入的损失。

```
deepspeed --num_gpus=2 --master_port=12345 train.py \
    --deepspeed ${deepspeed config path} \
    --model_name_or_path ${path to base model like vicuna-7b}  \
    --data_path ${data path} \
    --bf16 True \
    --output_dir outputs/vicuna-7b-toolalpaca/ \
    --num_train_epochs 3 \
    --per_device_train_batch_size 32 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_total_limit 10 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --lazy_preprocess True
```

您可以在 huggingface hub 上找到我们的模型：ToolAlpaca-7B，ToolAlpaca-13B。



### **4、****评估**

#### **对于模拟的 API：**

```
# 启动 API 模拟器
python instance_generation/simulator.py -api ./data/eval_simulated.json
# 获取 LLM 输出
python instance_generation/generation.py \
  -api ./data/eval_simulated.json \
  -out ./eval \
  -llm TangQiaoYu/ToolAlpaca-13B \
  --agent_prompt test_v1 \
  --use_cache
# 使用类似 GPT-4 的 LLM 进行评估
python evaluation.py -api ${api_data_path} -out ./eval
```









#### **对于真实的 API：您应该注册网站并获取 API_KEYs。**

```

python instance_generation/generation.py \
  -api ./data/eval_real.json \
  -out ./data \
  -llm TangQiaoYu/ToolAlpaca-13B \
  --agent_prompt test_v1 \
  --real
python evaluation.py -api ${api_data_path} -out ./eval
```









## **<strong><strong>ToolAlpaca**</strong>**<strong>的案例应用**</strong></strong>

持续更新中……






