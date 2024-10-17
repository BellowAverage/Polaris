
--- 
title:  LLMs之Gemma：gsm8k_eval.ipynb文件解读——通过构建基于问题-答案对的 prompting 模式来评估Gemma模型在GSM8K数据集上的表现水平 
tags: []
categories: [] 

---
LLMs之Gemma：gsm8k_eval.ipynb文件解读——通过构建基于问题-答案对的 prompting 模式来评估Gemma模型在GSM8K数据集上的表现水平





**目录**

































## **核心步骤**

&gt;&gt; 通过Kaggle下载Gemma模型的权重文件，作为本次评估的基础模型。

&gt;&gt; 加载和预处理GSM8K数据集，将训练集和测试集分离。

&gt;&gt; 定义一些辅助函数，如找出字符串中的数字，提取答案等。

&gt;&gt; 构建 prompting 输入，将 GSM8K 问题加入到 prompting 中。

&gt;&gt; 使用 sampler 对每个测试样本问题生成响应，并提取答案进行判断。

&gt;&gt; 记录模型在每个测试样本上的预测情况，最后计算准确率。





## **使用Gemma对GSM8K进行评估**

GSM8K数据集为小型模型提供了良好的评估挑战，原因如下：

&gt;&gt; 概念简单性：尽管GSM8K中的问题需要多步骤推理，但它们主要涉及基本的数学概念和基本算术运算。这使得数据集能够被小型模型所使用，这些模型可能没有能力处理复杂的数学推理。

&gt;&gt; 语言多样性：GSM8K强调语言多样性，确保问题不仅仅是同一模板的变化。这迫使模型推广他们对语言和数学概念的理解，而不是依赖于表面的模式匹配。

&gt;&gt; 适中的难度：GSM8K中的问题难度足以测试小型模型的极限，而不会完全无法处理。这允许在合理的难度范围内对不同的模型和方法进行有意义的评估和比较。

&gt;&gt; 自然语言解决方案：GSM8K提供自然语言解决方案，鼓励模型发展口语分析技能并产生人类可解释的推理步骤。这对于可能难以处理纯符号或基于方程的解决方案的小型模型尤其重要。

通过关注小学数学概念并强调语言多样性，GSM8K为评估小型语言模型的非形式推理能力提供了一个有价值的基准，并确定了改进领域。

2B Gemma检查点达到了19%的分数，这个结果高于使用更大竞争检查点获得的结果。





## **一、安装与下载**

```
! pip install git+https://github.com/google-deepmind/gemma.git
! pip install --user kaggle
```





### **<strong><strong>下载**</strong>**<strong>模型checkpoint**</strong></strong>

 "要使用Gemma的检查点，您需要一个Kaggle帐户和API密钥。以下是获取它们的方法：

访问 https://www.kaggle.com/ 并创建一个帐户。 进入您的帐户设置，然后是’API’部分。 点击’创建新令牌’以下载您的密钥。 然后运行下面的单元格。

```
import kagglehub
kagglehub.login()
如果一切顺利，您应该看到：
Kaggle credentials set.
Kaggle credentials successfully validated.
```





## **二、加载模型、数据集进行模型评估**

 现在选择并下载您想要尝试的检查点。请注意，您需要A100运行时来运行7b模型。

```

import os

VARIANT = '2b-it' # @param ['2b', '2b-it', '7b', '7b-it'] {type:"string"}
weights_dir = kagglehub.model_download(f'google/gemma/Flax/{VARIANT}')

ckpt_path = os.path.join(weights_dir, variant)
vocab_path = os.path.join(weights_dir, 'tokenizer.model')
# @title Python imports
import re
from gemma import params as params_lib
from gemma import sampler as sampler_lib
from gemma import transformer as transformer_lib

import datasets
import sentencepiece as spm

```



### **<strong><strong>加载GSM8K数据集**</strong></strong>



```
gsm8k = datasets.load_dataset("gsm8k", "main", cache_dir='/tmp')
gsm8k_train, gsm8k_test = gsm8k['train'], gsm8k['test']
```

#### **<strong><strong># @title Testing library**</strong></strong>



```

def find_numbers(x: str) -&gt; list[str]:
  """Finds all numbers in a string."""
  # Search for number, possibly negative (hyphen), with thousand separators
  # (comma), and with a decimal point (period inbetween digits).
  numbers = re.compile(
      r'-?[\d,]*\.?\d+',
      re.MULTILINE | re.DOTALL | re.IGNORECASE,
  ).findall(x)
  return numbers


def find_number(x: str,
                answer_delimiter: str = 'The answer is') -&gt; str:
  """Finds the most relevant number in a string."""
  # If model uses the answer delimiter, then select the first number following
  # that format.
  if answer_delimiter in x:
    answer = x.split(answer_delimiter)[-1]
    numbers = find_numbers(answer)
    if numbers:
      return numbers[0]

  # In general, select the last number in the string.
  numbers = find_numbers(x)
  if numbers:
    return numbers[-1]
  return ''


def maybe_remove_comma(x: str) -&gt; str:
  # Example: 5,600 -&gt; 5600
  return x.replace(',', '')
```





#### **<strong><strong># @title GSM8K Prompts**</strong></strong>

PREAMBLE = “”“作为一个专家级问题解决者，逐步解决以下数学问题。”“”

来自CoT论文的默认gsm8k提示

https://arxiv.org/pdf/2201.11903.pdf 第35页。

```
PREAMBLE = “”“作为一个专家级问题解决者，逐步解决以下数学问题。”“”
来自CoT论文的默认gsm8k提示
https://arxiv.org/pdf/2201.11903.pdf 第35页。


PREAMBLE = """As an expert problem solver solve step by step the following mathematical questions."""

# The default gsm8k prompt from the CoT paper
# https://arxiv.org/pdf/2201.11903.pdf page 35.

PROMPT = """Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?
A: We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted. So, they must have planted 21 - 15 = 6 trees. The answer is 6.

Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.

Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had 32 chocolates and Leah's sister had 42. That means there were originally 32 + 42 = 74 chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39.

Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?
A: Jason had 20 lollipops. Since he only has 12 now, he must have given the rest to Denny. The number of lollipops he has given to Denny must have been 20 - 12 = 8 lollipops. The answer is 8.

Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?
A: He has 5 toys. He got 2 from mom, so after that he has 5 + 2 = 7 toys. Then he got 2 more from dad, so in total he has 7 + 2 = 9 toys. The answer is 9.

Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?
A: There are 4 days from monday to thursday. 5 computers were added each day. That means in total 4 * 5 = 20 computers were added. There were 9 computers in the beginning, so now there are 9 + 20 = 29 computers. The answer is 29.

Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?
A: Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On Wednesday he lost 2 more so now he has 35 - 2 = 33 balls. The answer is 33.

Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: She bought 5 bagels for $3 each. This means she spent 5 * $3 = $15 on the bagels. She had $23 in beginning, so now she has $23 - $15 = $8. The answer is 8."""


# Extension of the default 8-shot prompt, page 35 in
# https://arxiv.org/pdf/2201.11903.pdf
# The extension is intended to improve performance on
# more complicated gsm8k examples.

EXTRA_3_SHOTS = """As an expert problem solver solve step by step the following mathematical questions.

Q: Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?
A: Here's how to calculate Tina's earnings:

**Regular Time:**
- Hours per shift: 8 hours
- Wage per hour: $18.00
- Regular pay per shift: 8 hours * $18.00/hour = $144.00

**Overtime:**
- Overtime hours per shift: 10 hours - 8 hours = 2 hours
- Overtime pay per hour: $18.00 + ($18.00 / 2) = $27.00
- Overtime pay per shift: 2 hours * $27.00/hour = $54.00

**Total per day:**
- Regular pay + overtime pay: $144.00/shift + $54.00/shift = $198.00/day

**Total for 5 days:**
- 5 days * $198.00/day = $990.00

**Therefore, Tina will make $990.00 in 5 days.** The answer is 990.

Q: Abigail is trying a new recipe for a cold drink. It uses 1/4 of a cup of iced tea and 1 and 1/4 of a cup of lemonade to make one drink. If she fills a pitcher with 18 total cups of this drink, how many cups of lemonade are in the pitcher?
A: ## Ambiguity in the Problem Statement:

There is one main ambiguity in the problem statement:

**Total volume vs. Number of servings:** The statement "18 total cups of this drink" could be interpreted in two ways:
  * **18 cups of the combined volume:** This would mean Abigail used a total of 18 cups of liquid, including both iced tea and lemonade.
  * **18 individual servings:** This would mean Abigail made 18 individual drinks, each containing 1/4 cup of iced tea and 1 1/4 cup of lemonade.

Let us assume the interpretation "18 cups of the combined volume".

## Solution assuming 18 cups of combined volume:

**Step 1: Find the proportion of lemonade in one drink:**

* Lemonade: 1 1/4 cups
* Iced tea: 1/4 cup
* Total: 1 1/4 + 1/4 = 1 1/2 cups
* Lemonade proportion: (1 1/4) / (1 1/2) = 5/6

**Step 2: Calculate the amount of lemonade in the pitcher:**

* Total volume: 18 cups
* Lemonade proportion: 5/6
* Volume of lemonade: 18 * (5/6) = 15 cups

Therefore, there are 15 cups of lemonade in the pitcher. The answer is 15.

Q: A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
A: Let us solve it using algebra. Let x be the number of people on the ship the monster ate in the first hundred years.

The number of people on the ship eaten in the second hundred years is 2x, and in the third hundred years is 4x.

Therefore, the total number of people eaten over three hundred years is x + 2x + 4x = 847.

Combining like terms, we get 7x = 847.

Dividing both sides by 7, we find x = 121.

Therefore, there were 121 people on the ship the monster ate in the first hundred years. The answer is 121."""
```





### **<strong><strong>加载语言模型**</strong>**<strong>、**</strong>**<strong>加载分词器**</strong></strong>

```
Load and prepare your LLM's checkpoint for use with Flax.
Start by loading the weights of your model.

# Load parameters
params = params_lib.load_and_format_params(ckpt_path)
Then load the tokenizer.

加载分词器：使用SentencePiece分词器，从vocab_path加载词汇表。
vocab = spm.SentencePieceProcessor()
vocab.Load(vocab_path)
Finally, build a sampler from the transformer configuration deduced from the checkpoint.
```





### **<strong><strong>构建采样器**</strong></strong>

首先，通过TransformerConfig.from_params从检查点推断出转换器配置。然后，使用这个配置创建一个转换器实例。最后，使用sampler_lib.Sampler创建一个具有正确参数形状的采样器。

```
首先，通过TransformerConfig.from_params从检查点推断出转换器配置。然后，使用这个配置创建一个转换器实例。最后，使用sampler_lib.Sampler创建一个具有正确参数形状的采样器。
transformer_config = transformer_lib.TransformerConfig.from_params(
    params, cache_size=1024)
transformer = transformer_lib.Transformer(transformer_config)

# Create a sampler with the right param shapes for the GSM8K prompt below
sampler = sampler_lib.Sampler(
    transformer=transformer,
    vocab=vocab,
    params=params['transformer'],
)
```



### **<strong><strong>通过一个循环来评估模型在GSM8K测试集上的性能**</strong></strong>

```

You should expect a score of 19.86% with the 2B model.

%%time
all_correct = 0
all_responses = {}
short_responses = {}
idx = 0
correct = 0

TEMPLATE = """
Q: {question}
A:"""

for task_id, problem in enumerate(gsm8k_test):

  if task_id in all_responses: continue

  # Print Task ID
  print(f"task_id {task_id}")

  # Formulate and print the full prompt
  full_prompt = (PREAMBLE +'\n\n' + PROMPT + '\n' +
                 TEMPLATE.format(question=problem['question']))
  short_prompt = PREAMBLE +'\n' + TEMPLATE.format(question=problem['question'])

  input_batch = [full_prompt]
  response = sampler(input_strings=input_batch, total_generation_steps=1024)
  print(response.text)

  all_responses[task_id] = response.text[0].split('\nQ:')[0]
  short_responses[task_id] = maybe_remove_comma(find_number(all_responses[task_id]))
  print(f"Short answer: {short_responses[task_id]}")
  try:
    correct += float(maybe_remove_comma(
        find_number(problem['answer']))) == float(short_responses[task_id])
  except:
    correct += maybe_remove_comma(
        find_number(problem['answer'])) == maybe_remove_comma(
            find_number(short_responses[task_id]))
  print('-'*40)
  print(f"Ground truth answer {problem['answer']}")
  print(f"Short ground truth answer {find_number(problem['answer'])}")
  print(f"Correct: {correct} out of {idx+1}")
  print("="*40)
  idx += 1


```






