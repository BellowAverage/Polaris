
--- 
title:  LLMs之Gemma：sampling_tutorial.ipynb文件解读——利用预训练的Gemma模型进行自然语言采样生成 
tags: []
categories: [] 

---
LLMs之Gemma：sampling_tutorial.ipynb文件解读——利用预训练的Gemma模型进行自然语言采样生成





**目录**



























## 相关文章

### LLMs之Gemma：Gemma(Google开发的新一代领先的开源模型)的简介、安装、使用方法之详细攻略









## **主要步骤如下所示**

&gt;&gt; 加载Gemma模型检查点，并使用它进行采样生成。 &gt;&gt; 安装依赖库gemma和kaggle &gt;&gt; 下载Gemma模型检查点，支持2B/7B等不同规模版本 &gt;&gt; 加载模型参数和tokenizer &gt;&gt; 根据参数自动构建Transformer配置 &gt;&gt; 构建Sampler，用于采样生成 &gt;&gt; 提供输入 prompt，调用Sampler进行采样 &gt;&gt; 输出结果



## **开始使用Gemma采样：分步指南**

您将在这个colab中找到一个详细的教程，解释如何加载Gemma检查点并从中进行采样。

## **安装**

```
! pip install git+https://github.com/google-deepmind/gemma.git
! pip install --user kaggle
```





### **<strong><strong>下载检查点**</strong></strong>

"要使用Gemma的检查点，您需要一个Kaggle帐户和API密钥。以下是获取它们的方法：

访问 https://www.kaggle.com/ 并创建一个帐户。

进入您的帐户设置，然后是'API'部分。

点击'创建新令牌'以下载您的密钥。

然后运行下面的单元格。

```
import kagglehub
kagglehub.login()
```

如果一切顺利，您应该看到：

Kaggle credentials set.

Kaggle credentials successfully validated.现在选择并下载您想要尝试的检查点。请注意，您需要A100运行时来运行7b模型。

```
import os

VARIANT = '2b-it' # @param ['2b', '2b-it', '7b', '7b-it'] {type:"string"}
weights_dir = kagglehub.model_download(f'google/gemma/Flax/{VARIANT}')

ckpt_path = os.path.join(weights_dir, variant)
vocab_path = os.path.join(weights_dir, 'tokenizer.model')
# @title Python imports
from gemma import params as params_lib
from gemma import sampler as sampler_lib
from gemma import transformer as transformer_lib
import sentencepiece as spm
```







## **使用****你****的模型开始生成**

加载并准备您的LLM的检查点以与Flax一起使用。

### **<strong><strong># 加载**</strong>**<strong>模型和分词器**</strong></strong>



```
# Load parameters
params = params_lib.load_and_format_params(ckpt_path)


vocab = spm.SentencePieceProcessor()
vocab.Load(vocab_path)


transformer_config=transformer_lib.TransformerConfig.from_params(
    params,
    cache_size=1024  # Number of time steps in the transformer's cache
)
transformer = transformer_lib.Transformer(transformer_config)

```



### **<strong><strong># 构建一个采样器**</strong></strong>

最后，在您的模型和分词器之上构建一个采样器。

```
# Create a sampler with the right param shapes.
sampler = sampler_lib.Sampler(
    transformer=transformer,
    vocab=vocab,
    params=params['transformer'],
)

```



### **<strong><strong>提供输入 prompt，调用Sampler进行采样**</strong></strong>

您已经准备好开始采样了！这个采样器使用即时编译，所以更改输入形状会触发重新编译，这可能会减慢速度。为了获得最快和最有效的结果，请保持您的批量大小一致。

```
input_batch = [
    "\n# Python program for implementation of Bubble Sort\n\ndef bubbleSort(arr):",
    "What are the planets of the solar system?",
  ]

out_data = sampler(
    input_strings=input_batch,
    total_generation_steps=300,  # number of steps performed when generating
  )

for input_string, out_string in zip(input_batch, out_data.text):
  print(f"Prompt:\n{input_string}\nOutput:\n{out_string}")
  print()
  print(10*'#')
```






