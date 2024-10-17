
--- 
title:  LLMs之Keras CodeGemma：Keras CodeGemma的简介、安装和使用方法、案例应用之详细攻略 
tags: []
categories: [] 

---
LLMs之Keras CodeGemma：Keras CodeGemma的简介、安装和使用方法、案例应用之详细攻略





**目录**



















































## **Keras CodeGemma的简介**

2024年4月9日，Google发布CodeGemma ，CodeGemma 是 Gemma 的开放版本系列，专注于代码。

CodeGemma 是由谷歌推出的一系列代码专家 LLM 模型，基于预训练的 2B 和 7B Gemma 检查点。CodeGemma 进一步在额外的 500B个主要为英语数据、数学和代码的令牌上进行训练，以改善逻辑和数学推理，并适用于代码完成和生成。

CodeGemma 是一系列轻量级、最先进的开放模型，是基于用于创建 Gemini 模型的相同研究和技术构建的。CodeGemma 模型主要在超过 500B个令牌的代码上进行训练，使用与 Gemma 模型系列相同的架构。因此，CodeGemma 模型在完成和生成任务中实现了最先进的代码性能，同时在大规模上保持了强大的理解和推理能力。

**<strong>官方地**</strong>址：

**<strong>官方文档**</strong>：







### **<strong><strong>1、CodeGemma 有 3 个变体**</strong></strong>

&gt;&gt; 一个专门用于填充和开放式生成的 2B 基础模型。 &gt;&gt; 一个 7B 基础模型，同时训练了代码填充和自然语言。 &gt;&gt; 一个 7B 指令模型，用户可以与其就代码进行对话。

CodeGemma 2B 专门用于代码填充，适用于快速的代码完成和生成，特别是在延迟和/或隐私至关重要的环境中。CodeGemma 7B 的训练混合了代码填充数据（80%）和自然语言。它可用于代码完成，以及代码和语言理解和生成。CodeGemma 7B Instruct 是在 CodeGemma 7B 之上对指令进行微调的。它适用于对话使用，特别是围绕代码、编程或数学推理主题。所有模型的上下文大小均与其前任相同，为 8K 个令牌。

<img alt="" height="314" src="https://img-blog.csdnimg.cn/direct/fb257f4e39c74810a7e6c20d4dd072fa.png" width="458">







### **<strong><strong>2、评估结果**</strong></strong>

在 HumanEval 上，CodeGemma-7B 在 Python 上表现优于大小相似的 7B 模型，除了 DeepSeek-Coder-7B。其他编程语言（如 Java、JavaScript 和 C++）的评估也是如此，来自 MultiPL-E，这是 HumanEval 的翻版。根据技术报告，在 7B 模型中，该模型在 GSM8K 上表现最佳。指导版本 CodeGemma-7B-it 在 HumanEval 和 MBPP 上改进了最受欢迎的语言。更多详情，您可以查看 BigCode 排行榜或下面的一些指标。

|Model|Pretraining size [tokens]|Python|JavaScript
|------
|10B+ models|||
|StarCoder 2 15B|4,000B+|44.15|44.24
|Code Llama 13B|2,500B|35.07|38.26
|7B models|||
|DeepSeek Coder 7B|2,000B|45.83|45.9
|CodeGemma 7B|500B of extra training|40.13|43.06
|Code Llama 7B|2,500B|29.98|31.8
|StarCoder 2 7B|3,500B+|34.09|35.35
|StarCoderBase 7B|3,000B+|28.37|27.35
|&lt;3B models|||
|CodeGemma 2B|500B of extra training|27.28|29.94
|Stable Code 3B|1,300B|30.72|28.75
|StarCoder 2 3B|3,000B+|31.44|35.37

|Model|Pretraining size [tokens]|Python|JavaScript
|------
|10B+ models|||
|Code Llama 13B|2,620B|50.6|40.92
|Code Llama 13B|2,620B|42.89|40.66
|7B models|||
|CodeGemma 7B|500B|52.74|47.71
|Code Llama 7B|2,620B|40.48|36.34
|Code Llama 7B|2,620B|25.65|33.11



<img alt="" height="460" src="https://img-blog.csdnimg.cn/direct/8b7929047b18485aa1c694407c1b8008.png" width="337">





### **<strong><strong>3、**</strong>**<strong>提示格式**</strong></strong>

CodeGemma 2B 和 CodeGemma 7B 使用填充（代码、注释、文档字符串、导入语句）进行代码完成。CodeGemma 是为了这项任务而训练的，使用了填充中间（FIM）目标，您在其中提供前缀和后缀作为完成的上下文。以下标记用于分隔输入的不同部分：

&lt;|fim_prefix|&gt; 位于我们要运行的完成之前的上下文之前。

&lt;|fim_suffix|&gt; 位于后缀之前。您必须将此令牌精确放置在编辑器中光标的位置上，因为这是模型将要代码完成的位置。

&lt;|fim_middle|&gt;是提示，邀请模型运行生成。

除此之外，还有，提供多文件上下文。我们将在与 transformers 使用部分展示使用示例。





## **Keras CodeGemma的安装和使用方法**

随着 Transformers 释放 4.39，您可以使用 CodeGemma 并利用 Hugging Face 生态系统中的所有工具，本指南将引导您使用 KerasNLP 进行代码完成任务的 CodeGemma 2B 模型。

```
pip install --upgrade transformers
```





### **<strong><strong>1、环境配置**</strong></strong>

#### **<strong><strong>设置**</strong></strong>

获取 CodeGemma 访问权限

要完成本教程，您首先需要完成 Gemma 设置指令。Gemma 设置指令会向您展示如何执行以下操作：

&gt;&gt; 在 kaggle.com 上获取 Gemma 的访问权限。

&gt;&gt; 选择具有足够资源运行 Gemma 2B 模型的 Colab 运行时。

&gt;&gt; 生成并配置 Kaggle 用户名和 API 密钥。

完成 Gemma 设置后，继续下一节，在该节中，您将为 Colab 环境设置环境变量。



#### **<strong><strong>选择runtime**</strong></strong>

要完成本教程，您需要具有足够资源运行 CodeGemma 2B 模型的 Colab 运行时。在这种情况下，您可以使用 T4 GPU：

&gt;&gt; 在 Colab 窗口右上角，选择 ▾（其他连接选项）。

&gt;&gt; 选择更改运行时类型。

&gt;&gt; 在硬件加速器下，选择 T4 GPU。





#### **<strong><strong>配置您的 API 密钥**</strong></strong>

要使用 Gemma，您必须提供您的 Kaggle 用户名和 Kaggle API 密钥。

要生成 Kaggle API 密钥，请转到您的 Kaggle 用户配置文件的账户选项卡，然后选择创建新 Token。这将触发下载一个包含您的 API 凭据的 kaggle.json 文件。

在 Colab 中，选择左侧窗格中的 Secrets（��），然后添加您的 Kaggle 用户名和 Kaggle API 密钥。将您的用户名存储在名称为 KAGGLE_USERNAME 的变量下，将您的 API 密钥存储在名称为 KAGGLE_KEY 的变量下。





### **<strong><strong>2、前置配置**</strong></strong>

#### **<strong><strong>设置环境变量**</strong></strong>

为 KAGGLE_USERNAME 和 KAGGLE_KEY 设置环境变量。

```
import os
from google.colab import userdata


os.environ["KAGGLE_USERNAME"] = userdata.get('KAGGLE_USERNAME')
os.environ["KAGGLE_KEY"] = userdata.get('KAGGLE_KEY')
```

#### **<strong><strong>安装依赖项**</strong></strong>



```
!pip install -q -U keras-nlp
```





#### **<strong><strong>选择后端**</strong></strong>

Keras 是一个高级、多框架的深度学习 API，设计简单易用。使用 Keras 3，您可以在 TensorFlow、JAX 或 PyTorch 中运行工作流。

对于本教程，请将后端配置为 TensorFlow。

```
os.environ["KERAS_BACKEND"] = "tensorflow"  # Or "jax" or "torch".
```





#### **<strong><strong>导入包**</strong></strong>

导入 Keras 和 KerasNLP。

```
import keras_nlp
import keras
```





#### **<strong><strong>加载模型**</strong></strong>

KerasNLP 提供了许多流行模型架构的实现。在本教程中，您将使用 GemmaCausalLM 创建一个模型，这是一个端到端的 Gemma 模型，用于因果语言建模。因果语言模型根据先前的令牌预测下一个令牌。



##### **<strong><strong>使用 from_preset 方法创建模型：**</strong></strong>



```
gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("code_gemma_2b_en")
gemma_lm.summary()
```

from_preset 方法从预设的架构和权重中实例化模型。在上面的代码中，字符串 code_gemma_2b_en 指定了预设架构 —— 一个具有 20 亿参数的 CodeGemma 模型。



注意： 也提供了具有 70 亿参数的 CodeGemma 模型。要在 Colab 中运行更大的模型，您需要访问付费计划中提供的高级 GPU。





### **<strong><strong>3、使用 CodeGemma 根据周围的上下文填充代码案例应用——填充中间代码完成**</strong></strong>

此示例使用了 CodeGemma 的填充中间（FIM）功能，根据周围的上下文完成代码。这在代码编辑器应用程序中特别有用，用于根据周围的代码插入代码（在光标之前和之后）。

CodeGemma 允许您使用 4 个用户定义的令牌 - 3 个用于 FIM，一个用于多文件上下文支持。使用这些定义常量。

```
BEFORE_CURSOR = ""
AFTER_CURSOR = ""
AT_CURSOR = ""
FILE_SEPARATOR = ""
```

定义模型的停止令牌。

```
END_TOKEN = gemma_lm.preprocessor.tokenizer.end_token
stop_tokens = (BEFORE_CURSOR, AFTER_CURSOR, AT_CURSOR, FILE_SEPARATOR, END_TOKEN)
stop_token_ids = tuple(gemma_lm.preprocessor.tokenizer.token_to_id(x) for x in stop_tokens)
```





格式化用于代码完成的提示。注意：

&gt;&gt; 在任何 FIM 令牌和前缀、后缀之间都不应有空格

&gt;&gt; FIM 中间令牌应在最后，以便为模型继续填充

&gt;&gt; 前缀或后缀可能为空，具体取决于光标当前在文件中的位置，或者您要为模型提供的上下文量



使用辅助函数格式化提示。

```
def format_completion_prompt(before, after):
    return f"{BEFORE_CURSOR}{before}{AFTER_CURSOR}{after}{AT_CURSOR}"

before = "import "
after = """if __name__ == "__main__":\n    sys.exit(0)"""
prompt = format_completion_prompt(before, after)
print(prompt)
```



运行提示。建议以流式方式获取响应令牌。遇到任何用户定义的或回合/句子结束令牌时停止流式传输，以获得生成的代码完成。

```
gemma_lm.generate(prompt, stop_token_ids=stop_token_ids, max_length=128)
```

该模型提供 sys 作为建议的代码完成。



#### **<strong><strong>总结**</strong></strong>

本教程介绍了如何使用 CodeGemma 根据周围的上下文填充代码。接下来，查看 CodeGemma 和 KerasNLP 笔记本中的 AI 辅助编程示例，了解如何使用 CodeGemma。

还可以参考 CodeGemma 模型卡，了解 CodeGemma 模型的技术规格。





## **Keras CodeGemma的案例应用**

持续更新中……



### **<strong><strong>1、**</strong>**<strong>使用codegemma-2b通过**</strong>**<strong>transformers**</strong>**<strong>完成代码**</strong></strong>

下面的代码片段展示了如何使用codegemma-2b通过transformers完成代码。它需要大约6 GB使用float16精度的RAM，使其非常适合消费类gpu和设备上的应用程序。

```

from transformers import GemmaTokenizer, AutoModelForCausalLM
import torch

model_id = "google/codegemma-2b"
tokenizer = GemmaTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
	model_id,
	torch_dtype=torch.float16
).to("cuda:0")

prompt = '''\
&lt;|fim_prefix|&gt;import datetime
def calculate_age(birth_year):
    """Calculates a person's age based on their birth year."""
    current_year = datetime.date.today().year
    &lt;|fim_suffix|&gt;
    return age&lt;|fim_middle|&gt;\
'''

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
prompt_len = inputs["input_ids"].shape[-1]
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0][prompt_len:]))
```

观察到的&lt;|fim_suffix|&gt;标记出现在编辑器中光标所在的位置，标记着生成的位置。 &lt;|fim_prefix|&gt;提供了光标之前的上下文，直到&lt;|fim_middle|&gt;为止的是光标之后的附加上下文。如果光标位于文件的开头或结尾，它们中的任何一个都可以为空。

之前的代码可能会返回类似以下的内容：

```
age = current_year - birth_year&lt;|file_separator|&gt;test_calculate_age.py
&lt;|fim_suffix|&gt;
    assert calculate_age(1990) == 33
    assert calculate_age(1980) == 43
    assert calculate_age(1970) == 53
    assert calculate_age(1960) == 63
    assert calculate_age(1950) == 73
```



请注意正确完成后的额外内容。CodeGemma 7B特别如此，它更详细，并且倾向于在完成之后提供额外的代码或注释。我们必须忽略FIM标记或EOS标记之后出现的所有内容。我们可以通过向generate函数提供终止符列表，使用transformers提前停止生成，如下所示：

```
FIM_PREFIX = '&lt;|fim_prefix|&gt;'
FIM_SUFFIX = '&lt;|fim_suffix|&gt;'
FIM_MIDDLE = '&lt;|fim_middle|&gt;'
FIM_FILE_SEPARATOR = '&lt;|file_separator|&gt;'

terminators = tokenizer.convert_tokens_to_ids(
	[FIM_PREFIX, FIM_MIDDLE, FIM_SUFFIX, FIM_FILE_SEPARATOR]
)
terminators += [tokenizer.eos_token_id]

outputs = model.generate(
  **inputs,
  max_new_tokens=100,
  eos_token_id=terminators,
)
```

在这种情况下，生成将在找到第一个分隔符时停止：

```
age = current_year - birth_year&lt;|file_separator|&gt;
```



#### **<strong><strong>关于精度的说明**</strong></strong>

原始的CodeGemma检查点以bfloat16精度发布。如果您在未指定torch_dtype的情况下加载模型，PyTorch会将它们升级为float32。将它们转换为float16是完全可以的，并且在某些硬件上，它可能比bfloat16快得多。为了最大精度，我们建议您使用bfloat16而不是float32。

您还可以自动对模型进行量化，以8位或4位模式加载。以4位模式加载CodeGemma 7B大约需要9 GB的内存来运行，这使得它与许多消费者级显卡以及Google Colab中的所有GPU兼容。这就是您如何以4位模式加载生成管道：

```
pipeline = pipeline(
    "text-generation",
    model=model,
    model_kwargs={
        "torch_dtype": torch.float16,
        "quantization_config": {"load_in_4bit": True}
    },
)
```






