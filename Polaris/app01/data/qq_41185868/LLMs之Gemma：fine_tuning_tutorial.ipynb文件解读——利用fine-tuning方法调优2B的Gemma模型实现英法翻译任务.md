
--- 
title:  LLMs之Gemma：fine_tuning_tutorial.ipynb文件解读——利用fine-tuning方法调优2B的Gemma模型实现英法翻译任务 
tags: []
categories: [] 

---
LLMs之Gemma：fine_tuning_tutorial.ipynb文件解读——利用fine-tuning方法调优2B的Gemma模型实现英法翻译任务







**目录**

































## **fine_tuning_tutorial.ipynb文件解读****——****利用fine-tuning方法调优2B的Gemma模型实现英法翻译任务**

## **主要步骤**

&gt;&gt; 准备数据集：使用公开可得的MTNT英法翻译数据集。为数据增加语言标记前缀和后缀，使用字符分词模型对数据进行分词。

&gt;&gt; 构建数据加载器：封装数据预处理和批量化处理的类，生成训练和验证数据集。

&gt;&gt; 加载模型：从预训练权重中恢复2B Gemma Transformer模型。

&gt;&gt; 定义前向和损失计算：实现模型前馈和交叉熵损失计算。

&gt;&gt; 构建训练步骤：实现反向传播计算参数更新的训练步骤。

&gt;&gt; 训练循环：使用训练数据集和训练步骤进行差分学习，定期在验证数据集上评估效果。

&gt;&gt; 调优和测试：实现基于小批量和有限轮数的微调，测试微调后的模型是否能正确翻译单个样本。







## **利用flax对2B Gemma模型进行微调**

在本教程中，您将学习如何使用Flax对2B Gemma模型进行微调以完成简单的翻译任务。要运行此Colab，您需要使用TPU v4运行时。



## **Setup**

```
# @title Installation
! pip install git+https://github.com/google-deepmind/gemma.git
! pip install --user kaggle
```



### **<strong><strong>Downloading the checkpoint**</strong></strong>下载检查点

要使用Gemma的检查点，你需要一个Kaggle帐户和API密钥。以下是如何获得它们: 访问https://www.kaggle.com/并创建一个帐户。 转到您的帐户设置，然后进入“API”部分。 点击“创建新令牌”下载密钥。 然后运行下面的单元格。

```

import kagglehub
kagglehub.login()
If everything went well, you should see:

Kaggle credentials set.
Kaggle credentials successfully validated.
Now select and download the checkpoint you want to try. On a single host, only the 2b model can fit in memory for fine-tuning.

import os

VARIANT = '2b-it' # @param ['2b', '2b-it'] {type:"string"}
weights_dir = kagglehub.model_download(f'google/gemma/Flax/{VARIANT}')

ckpt_path = os.path.join(weights_dir, variant)
vocab_path = os.path.join(weights_dir, 'tokenizer.model')
# @title Python imports

import enum
import re
import string

# We import JAX and some related packages.
import chex
import jax
import jax.numpy as jnp
import optax

# We will use tensorflow to handle the dataset
import tensorflow as tf
import tensorflow_datasets as tfds

# Finally, we import Gemma.
from gemma import params as params_lib
from gemma import sampler as sampler_lib
from gemma import transformer as transformer_lib
import sentencepiece as spm
```



## **步骤1:准备数据集**

### **<strong><strong>The MTNT dataset**</strong></strong>

在本教程中，我们将使用MTNT数据集，来自论文MTNT:嘈杂文本的机器翻译测试平台。该数据集可直接在TensorFlow数据集目录中获得。

更准确地说，我们将重点关注英语到法语的翻译。

但让我们来看看数据本身。

```
ds = tfds.load("mtnt/en-fr", split="train")
ds = ds.take(2)
ds = ds.as_numpy_iterator()
for idx, example in enumerate(ds):
  print(f'Example {idx}:')
  for key, val in example.items():
    print(f'{key}: {val}')
  print()
Each sample in the dataset contains two entries:

'src': The original English sentence.
'dst': The corresponding French translation.
```



### **<strong><strong>Tokenizer**</strong></strong>

分词器 让我们从加载词汇库标记器开始，我们将使用sentencepece库构造它。

让我们为英语到法语的翻译任务定制SentencePieceProcessor。由于我们正在微调只有英语的杰玛2B模式，我们需要进行一些调整:

输入前缀:为每个输入添加一个公共前缀，表示翻译任务。例如，我们可以使用这样的提示:Translate this into French: [INPUT_SENTENCE]。

翻译开始后缀:我们在每个提示符的末尾添加一个后缀，告诉模型何时开始翻译过程。一条新线应该能完成这项工作。

LM标记:Gemma模型期望在每个序列的开始处有一个序列的开始标记。类似地，我们需要在每个训练示例的末尾添加一个序列结束标记。

```
class GemmaTokenizer:
  """Custom wrapper around a SentencePieceProcessor for tensorflow."""

  def __init__(self,
               spm_processor: spm.SentencePieceProcessor):
    self._spm_processor = spm_processor

  @property
  def pad_id(self) -&gt; int:
    """Fast access to the pad id."""
    return self._spm_processor.pad_id()

  def tokenize(self,
               example: str | bytes,
               prefix: str = '',
               suffix: str = '',
               add_eos: bool = True) -&gt; jax.Array:
    """
    Tokenization function.

    Args:
      example: input string to tokenize.
      prefix:  prefix to add to the input string.
      suffix:  suffix to add to the input string.
      add_eos: if True, add an end of sentence token at the end of the output
               sequence.
    Returns:
      Tokens corresponding to the input string.
    """
    int_list = [self._spm_processor.bos_id()]
    int_list.extend(self._spm_processor.EncodeAsIds(prefix + example + suffix))
    if add_eos:
      int_list.append(self._spm_processor.eos_id())

    return jnp.array(int_list, dtype=jnp.int32)

  def tokenize_tf_op(self,
                     str_tensor: tf.Tensor,
                     prefix: str = '',
                     suffix: str = '',
                     add_eos: bool = True) -&gt; tf.Tensor:
    """Tensforflow operator for the tokenize function."""
    encoded = tf.numpy_function(
        self.tokenize,
        [str_tensor, prefix, suffix, add_eos],
        tf.int32)
    encoded.set_shape([None])
    return encoded

  def to_string(self, tokens: jax.Array) -&gt; str:
    """Convert an array of tokens to a string."""
    return self._spm_processor.EncodeIds(tokens.tolist())
Now let's try our custom tokenizer on the MTNT dataset

tokenizer = GemmaTokenizer(vocab)

def tokenize_source(tokenizer, example: tf.Tensor):
  return tokenizer.tokenize_tf_op(example,
                                  prefix='Translate this into French:\n',
                                  suffix='\n',
                                  add_eos=False)
def tokenize_destination(tokenizer, example: tf.Tensor):
  return tokenizer.tokenize_tf_op(example,
                                  add_eos=True)

ds = tfds.load("mtnt/en-fr",split="train")
ds = ds.take(2)
ds = ds.map(lambda x: {'src': tokenize_source(tokenizer, x['src']),
                       'dst': tokenize_destination(tokenizer, x['dst'])})
ds = ds.as_numpy_iterator()
for idx, example in enumerate(ds):
  print(f'Example {idx}:')
  for key, val in example.items():
    print(f'{key}: {val}')
  print()
```



### **<strong><strong>Data loader**</strong></strong>数据加载器

现在我们可以在构建数据加载器时包装所有内容。

确定哪些令牌导致目标丢失的掩码

```


@chex.dataclass(frozen=True)
class TrainingInput:
  # Input tokens given to the model
  input_tokens: jax.Array

  # A mask that determines which tokens contribute to the target loss
  # calculation.
  target_mask: jax.Array

class DatasetSplit(enum.Enum):
  TRAIN = 'train'
  VALIDATION = 'valid'


class MTNTDatasetBuilder:
  """Data loader for the MTNT dataset."""

  N_ITEMS = {DatasetSplit.TRAIN: 35_692,
             DatasetSplit.VALIDATION: 811}

  BUFFER_SIZE_SHUFFLE = 10_000
  TRANSLATION_PREFIX = 'Translate this into French:\n'
  TRANSLATION_SUFFIX = '\n'

  def __init__(self,
               tokenizer : GemmaTokenizer,
               max_seq_len: int):
    """Constructor.

    Args:
      tokenizer: Gemma tokenizer to use.
      max_seq_len: size of each sequence in a given batch.
    """
    self._tokenizer = tokenizer
    self._base_data = {
        DatasetSplit.TRAIN: tfds.load("mtnt/en-fr",split="train"),
        DatasetSplit.VALIDATION: tfds.load("mtnt/en-fr",split="valid"),
    }
    self._max_seq_len = max_seq_len

  def _tokenize_source(self, example: tf.Tensor):
    """Tokenization function for the source."""
    return self._tokenizer.tokenize_tf_op(example,
                                          prefix=self.TRANSLATION_PREFIX,
                                          suffix=self.TRANSLATION_SUFFIX,
                                          add_eos=False)

  def _tokenize_destination(self, example: tf.Tensor):
    """Tokenization function for the French translation."""
    return self._tokenizer.tokenize_tf_op(example,
                                          add_eos=True)

  def _pad_up_to_max_len(self,
                         input_tensor: tf.Tensor,
                         pad_value: int | bool,
                         ) -&gt; tf.Tensor:
    """Pad the given tensor up to sequence length of a batch."""
    seq_len = tf.shape(input_tensor)[0]
    to_pad = tf.maximum(self._max_seq_len - seq_len, 0)
    return tf.pad(input_tensor,
                  [[0, to_pad]],
                  mode='CONSTANT',
                  constant_values=pad_value,
                  )

  def _to_training_input(self,
                         src_tokens: jax.Array,
                         dst_tokens: jax.Array,
                         ) -&gt; TrainingInput:
    """Build a training input from a tuple of source and destination tokens."""

    # The input sequence fed to the model is simply the concatenation of the
    # source and the destination.
    tokens = tf.concat([src_tokens, dst_tokens], axis=0)

    # We want to prevent the model from updating based on the source (input)
    # tokens. To achieve this, we add a target mask to each input.
    q_mask = tf.zeros_like(src_tokens, dtype=tf.bool)
    a_mask = tf.ones_like(dst_tokens, dtype=tf.bool)
    mask = tf.concat([q_mask, a_mask], axis=0)

    # If the output tokens sequence is smaller than the target sequence size,
    # then we pad it with pad tokens.
    tokens = self._pad_up_to_max_len(tokens, self._tokenizer.pad_id)

    # We don't want to perform the backward on the pad tokens.
    mask = self._pad_up_to_max_len(mask, False)

    return TrainingInput(input_tokens=tokens, target_mask=mask)


  def get_train_dataset(self, batch_size: int, num_epochs: int):
    """Build the training dataset."""

    # Tokenize each sample
    ds = self._base_data[DatasetSplit.TRAIN].map(lambda x : (self._tokenize_source(x['src']),
                                                             self._tokenize_destination(x['dst'])))

    # Convert them to training inputs
    ds = ds.map(lambda x, y: self._to_training_input(x, y))

    # Remove the samples which are too long
    ds = ds.filter(lambda x: tf.shape(x.input_tokens)[0] &lt;= self._max_seq_len)

    # Shuffle the dataset
    ds = ds.shuffle(buffer_size=self.BUFFER_SIZE_SHUFFLE)

    # Repeat if necessary
    ds = ds.repeat(num_epochs)

    # Build batches
    ds = ds.batch(batch_size, drop_remainder=True)
    return ds

  def get_validation_dataset(self, batch_size: int):
    """Build the validation dataset."""

    # Same as the training dataset, but no shuffling and no repetition
    ds = self._base_data[DatasetSplit.VALIDATION].map(lambda x : (self._tokenize_source(x['src']),
                                                                  self._tokenize_destination(x['dst'])))
    ds = ds.map(lambda x, y: self._to_training_input(x, y))
    ds = ds.filter(lambda x: tf.shape(x.input_tokens)[0] &lt;= self._max_seq_len)
    ds = ds.batch(batch_size, drop_remainder=True)
    return ds
Let's give it a try.

tokenizer = GemmaTokenizer(vocab)
dataset_builder = MTNTDatasetBuilder(tokenizer, max_seq_len=20)
ds = dataset_builder.get_train_dataset(3, 1)
ds = ds.take(2)
ds = ds.as_numpy_iterator()
for idx, example in enumerate(ds):
  print(f'Example {idx}:')
  for key, val in example.items():
    print(f'{key}: {val}')
  print()
```



## **微调Gemma模型**

### **<strong><strong>Getting started**</strong></strong>

首先让我们加载模型

```
# Load parameters

# TODO: change once the downloading url is known
params = params_lib.load_and_format_params(ckpt_path)

# We use the `transformer_lib.TransformerConfig.from_params` function to
# automatically load the correct configuration from a checkpoint. Note that the
# vocabulary size is smaller than the number of input embeddings due to unused
# tokens in this release.
config_2b = transformer_lib.TransformerConfig.from_params(
    params,
    cache_size=30  # Number of time steps in the transformer's cache
)
model_2b = transformer_lib.Transformer(config=config_2b)
Can our model translate French ? Well let's try it out !

sampler_old = sampler_lib.Sampler(
    transformer=model_2b,
    vocab=vocab,
    params=params['transformer'],
)
print(sampler_old(
    ["Translate this into French:\nHello, my name is Morgane.\n"],
    # number of steps performed when generating
    total_generation_steps=30,
  ).text)
```

不出所料，它没有起作用。让我们看看能否通过微调得到更好的结果。在继续前进之前，如果有必要，不要忘记清除记忆。

del sampler_old



### **<strong><strong>模型正向传播和损失函数**</strong></strong>

Gemma Transformer类继承自亚麻.亚麻. module。它提供了两种基本方法: init:初始化模型的参数。 apply:使用给定的参数集执行模型的__call__函数。 因为我们使用的是预训练的权重，所以我们不会使用init函数。 我们定义forward_and_loss_fn如下

```


def forward_and_loss_fn(params,
                        *,
                        model: transformer_lib.Transformer,
                        input_tokens: jax.Array,            # Shape [B, L]
                        input_mask: jax.Array,              # Shape [B, L]
                        positions: jax.Array,               # Shape [B, L]
                        attention_mask: jax.Array,          # [B, L, L]
                        ) -&gt; jax.Array:
  """Foward pass and loss function.

  Args:
    params: model's input parameters.
    model: gemma transformer model to call.
    input_tokens: input tokens sequence, shape [B, L].
    input_mask: tokens to ignore when computing the loss, shape [B, L].
    positions: relative position of each token, shape [B, L].
    attention_mask: input attention mask, shape [B, L].

  Returns:
    Softmax cross-entropy loss for the next-token prediction task.
  """

  # Foward pass on the input data.
  # No attention cache is needed here.
  logits, _ = model.apply(
        params,
        input_tokens,
        positions,
        None,              # Attention cache is None.
        attention_mask,
    )

  # Exclude the last step as it does not appear in the targets.
  logits = logits[0, :-1]

  # Similarly, the first token cannot be predicteds.
  target_tokens = input_tokens[0, 1:]
  target_mask = input_mask[0, 1:]

  # Convert the target labels into one-hot encoded vectors.
  one_hot = jax.nn.one_hot(target_tokens, logits.shape[-1])

  # Don't update on unwanted tokens.
  one_hot = one_hot * target_mask.astype(one_hot.dtype)[...,None]

  # Normalisation factor.
  norm_factor = 1 / (jnp.sum(target_mask) + 1e-8)

  # Return the nll loss.
  return -jnp.sum(jax.nn.log_softmax(logits) * one_hot) * norm_factor
The Gemma transformer requires an attention mask and position vector alongside each input. We can conveniently generate these using the following function:

def get_attention_mask_and_positions(example: jax.Array,
                                     pad_id : int,
                                     )-&gt; tuple[jax.Array, jax.Array]:
  """Builds the position and attention mask vectors from the given tokens."""
  pad_mask = example != pad_id
  current_token_position = transformer_lib.build_positions_from_mask(pad_mask)
  attention_mask = transformer_lib.make_causal_attn_mask(pad_mask)
  return current_token_position, attention_mask
We can now build the train_step function which performs the backward pass and updates the model's parameters accordingly.

def train_step(model: transformer_lib.Transformer,
               params,
               optimizer: optax.GradientTransformation,
               opt_state: optax.OptState,
               pad_id: int,
               example: TrainingInput):
  """Train step.

  Args:
    model: gemma transformer model.
    params: model's input parameters.
    optimizer: optax optimizer to use.
    opt_state: input optimizer's state.
    pad_id: id of the pad token.
    example: input batch.

  Returns:
    Training loss, updated parameters, updated optimizer state.
  """

  # Build the position and attention mask vectors.
  positions, attention_mask = get_attention_mask_and_positions(example.input_tokens, pad_id)

  # Forward and backward passes
  train_loss, grads = jax.value_and_grad(forward_and_loss_fn)(params,
                                                             model=model,
                                                             input_tokens=example.input_tokens,
                                                             input_mask=example.target_mask,
                                                             positions=positions,
                                                             attention_mask=attention_mask)
  # Update the parameters
  updates, opt_state = optimizer.update(grads, opt_state)
  params = optax.apply_updates(params, updates)

  return train_loss, params, opt_state
Similarly, we build a validation_step function without backward pass.

def validation_step(model: transformer_lib.Transformer,
                    params,
                    pad_id: int,
                    example: TrainingInput,
                    ):
  positions, attention_mask = get_attention_mask_and_positions(example.input_tokens, pad_id)
  val_loss = forward_and_loss_fn(params,
                                 model=model,
                                 input_tokens=example.input_tokens,
                                 input_mask=example.target_mask,
                                 positions=positions,
                                 attention_mask=attention_mask)
  return val_loss
And now the training loop itself.

@chex.dataclass(frozen=True)
class TrainingConfig:
  learning_rate: float
  num_epochs: int
  eval_every_n: int
  batch_size: int
  max_steps: int | None = None


def train_loop(
    model: transformer_lib.Transformer,
    params,
    dataset_builder: MTNTDatasetBuilder,
    training_cfg: TrainingConfig):


  # We jit the train step, making the whole loop much more efficient
  compiled_train_step = jax.jit(train_step, static_argnames=['model', 'optimizer'])

  # We do the same with the validation step
  compiled_validation_step = jax.jit(validation_step, static_argnames=['model'])

  # To save memory, we use a SGD optimizer instead of the usual Adam. Note that
  # for this specific example SGD is more than enough.
  optimizer = optax.sgd(training_cfg.learning_rate)
  opt_state = optimizer.init(params)

  # Build the training dataset
  train_ds = dataset_builder.get_train_dataset(batch_size=training_cfg.batch_size,
                                               num_epochs=training_cfg.num_epochs)
  train_ds = train_ds.as_numpy_iterator()

  # Build the validation dataset, with a limited number of samples for this demo
  validation_ds = dataset_builder.get_validation_dataset(batch_size=training_cfg.batch_size)
  validation_ds = validation_ds.take(50)

  n_steps = 0
  avg_loss=0

  # A first round of validation loss
  n_steps_eval = 0
  eval_loss = 0
  val_iterator = validation_ds.as_numpy_iterator()
  for val_example in val_iterator:
    eval_loss += compiled_validation_step(model,
                                          params,
                                          dataset_builder._tokenizer.pad_id,
                                          val_example)
    n_steps_eval += 1
  print(f"Start, validation loss: {eval_loss/n_steps_eval}")

  for train_example in train_ds:
    train_loss, params, opt_state = compiled_train_step(model=model,
                                                        params=params,
                                                        optimizer=optimizer,
                                                        opt_state=opt_state,
                                                        pad_id=dataset_builder._tokenizer.pad_id,
                                                        example=train_example)
    n_steps += 1
    avg_loss += train_loss
    if n_steps % training_cfg.eval_every_n == 0:
      eval_loss = 0

      n_steps_eval = 0
      val_iterator = validation_ds.as_numpy_iterator()
      for val_example in val_iterator:
        eval_loss += compiled_validation_step(model,
                                              params,
                                              dataset_builder._tokenizer.pad_id,
                                              val_example)
        n_steps_eval +=1
      avg_loss /= training_cfg.eval_every_n
      eval_loss /= n_steps_eval
      print(f"STEP {n_steps} training loss: {avg_loss} - eval loss: {eval_loss}")
      avg_loss=0
    if training_cfg.max_steps is not None and n_steps &gt; training_cfg.max_steps:
      break
  return params
We can fine-tune our model on a limited number of steps.

# Small seq size so that everything fits in memory
SEQ_SIZE = 25
tokenizer = GemmaTokenizer(vocab)
dataset_builder= MTNTDatasetBuilder(tokenizer, SEQ_SIZE)
training_cfg = TrainingConfig(learning_rate=1e-4,
                              num_epochs=1,
                              eval_every_n=20,
                              batch_size=1,
                              max_steps=100)

params = train_loop(model=model_2b,
                    params={'params': params['transformer']},
                    dataset_builder=dataset_builder,
                    training_cfg=training_cfg)
Both the training loss and the validation's are going down. But is it working ? Let's try again with our previous example:

sampler = sampler_lib.Sampler(
    transformer=model_2b,
    vocab=vocab,
    params=params['params'],
)
To ensure our input matches the training format, remember to use the prefix 'Translate this into French:\n' and a newline character at the end. This signals the model to begin translation.

sampler(
    ["Translate this into French:\nHello, my name is Morgane.\n"],
    total_generation_steps=30,
    ).text


```




