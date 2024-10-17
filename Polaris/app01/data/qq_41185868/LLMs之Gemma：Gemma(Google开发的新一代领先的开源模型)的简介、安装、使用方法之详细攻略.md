
--- 
title:  LLMs之Gemma：Gemma(Google开发的新一代领先的开源模型)的简介、安装、使用方法之详细攻略 
tags: []
categories: [] 

---
LLMs之Gemma：Gemma(Google开发的新一代领先的开源模型)的简介、安装、使用方法之详细攻略



>  
 **<strong>导读**</strong>：此文章介绍了Google推出的新一代开源模型Gemma，旨在帮助研发人员负责任地开发AI。 
 ****<strong><em>背景****</em></strong>： 
 &gt;&gt; Google长期致力于为开发者和研究人员提供各种开放模型，如Transformers、TensorFlow、BERT、T5等，以推动AI的负责任开发。 
 ****<strong><em>核心要点****</em></strong>： 
 &gt;&gt; Gemma是基于同样技术与架构研发的Gemini模型开发出来的轻量级开放模型家族，它是一系列体积较小但性能领先的开源模型。 
 &gt;&gt; Gemma有2B和7B两种规模，均搭载了预训练和指令调优版本，可以直接在笔记本电脑上运行。与其它同类开源模型相比，Gemma模型规模相对较小但性能表现更好。 
 &gt;&gt; 同时推出"可责任生成AI工具包"，提供安全开发指南和辅助工具，以帮助研发人员安全开发应用。 
 &gt;&gt; Gemma支持各主流框架进行推理和监督调优，如JAX、PyTorch、TensorFlow Keras，可以在不同设备与平台上应用。 
 &gt;&gt; 针对开发者提供多设备兼容性，如笔记本、服务器、 IoT、手机以及云平台。 
 &gt;&gt; 与NVIDIA合作，使Gemma在GPU上实现最优性能。同时支持Google Cloud平台。 
 &gt;&gt; Google提供300美元Google Cloud试用证和高达50万美元研究资助，支持开发者研究。 
 ****<strong><em>优势****</em></strong>： 
 &gt;&gt;比同规模模型在多项基准上表现更优。 
 &gt;&gt;安全性能出色，预训练模型过滤敏感信息，指令训练强调責任感。 
 &gt;&gt;可在开发者本地设备上运行，极低成本。 
 &gt;&gt;生态系统完善，支持多框架和设备，助推AI成果在多个场景的应用。 
 总之，Gemma旨在通过提供强大且低成本的开放模型，推动负责任的AI研发和应用。Gemma模型系列体现了谷歌长期开源AI领域贡献的精神，它旨在通过提供小体积高性能的开源模型，结合提供的安全工具，帮助研发人员以更负责任的方式开发应用AI能力。 






**目录**















































## **Gemma的简介**

<img alt="" height="312" src="https://img-blog.csdnimg.cn/direct/3e6a5c58a5c94234a5b82b66dab36124.png" width="554">

2024年2月21日，Gemma是由**<strong>Google **</strong>DeepMind推出的一系列开源的大型语言模型（LLM），基于Gemini研究和技术。该存储库包含一个基于Flax和JAX的推理实现和示例。

Gemma是使用与Gemini模型相同的研究和技术构建的，旨在推动负责任的人工智能发展。同时，Google长期以来一直致力于为开放社区贡献创新，例如Transformers、TensorFlow、BERT、T5、JAX、AlphaFold和AlphaCode。今天，Google向开发者和研究人员开源了新一代开放模型，以帮助他们负责任地构建人工智能。从今天开始，Gemma全球可用。

Gemma是一系列轻量级、领先的开放模型，它们是由Google DeepMind和Google其他团队开发的，受到了Gemini的启发，名称反映了拉丁语"gemma"的含义，即"宝石"。除了模型权重外，还发布了支持开发者创新、促进合作并引导负责任使用Gemma模型的工具。



**<strong>官网**</strong>**<strong>地址**</strong>：

**<strong>GitHub地址**</strong>：**<strong>官方文章**</strong>**<strong>地址**</strong>：





### **<strong><strong>1、关键细节**</strong></strong>

&gt;&gt; Google发布了两个尺寸的模型权重：Gemma 2B和Gemma 7B。每个尺寸都发布了经过预训练和指导调整的变体。

&gt;&gt; 新的负责任生成AI工具包提供了使用Gemma创建更安全人工智能应用程序的指导和基本工具。

&gt;&gt; 我们为推断和监督微调（SFT）提供了工具链，涵盖所有主要框架：JAX、PyTorch和TensorFlow通过本地Keras 3.0。

&gt;&gt; 准备就绪的Colab和Kaggle笔记本，以及与Hugging Face、MaxText、NVIDIA NeMo和TensorRT-LLM等流行工具的集成，使得开始使用Gemma变得轻而易举。

&gt;&gt; 经过预训练和指导调整的Gemma模型可以在您的笔记本电脑、工作站或Google Cloud上运行，并可轻松部署到Vertex AI和Google Kubernetes Engine（GKE）上。

&gt;&gt;  跨多个AI硬件平台的优化确保了行业领先的性能，包括NVIDIA GPU和Google Cloud TPU。 使用条款允许所有组织在尺寸上不受限制地进行负责任的商业使用和分发。



### **<strong><strong>2、**</strong>**<strong>尺寸上的领先性能**</strong></strong>

<img alt="" height="615" src="https://img-blog.csdnimg.cn/direct/d2ffaf7cf4444f67b9c3d9f3dc691ee5.png" width="1000">

Gemma模型与今天广泛可用的我们最大、最功能强大的AI模型Gemini共享技术和基础架构组件。这使得与其他开放模型相比，Gemma 2B和7B在其尺寸上实现了最佳性能。并且Gemma模型能够直接在开发者的笔记本电脑或台式电脑上运行。值得注意的是，Gemma在关键基准测试上明显优于更大的模型，同时符合我们对安全和负责任输出的严格标准。有关性能、数据集组成和建模方法的详细信息，请参阅技术报告。



#### **<strong><strong>显示Gemma在常见基准测试中的性能，与Llama-2 7B和13B进行比较的图表**</strong></strong>

### **<strong><strong>3、**</strong>**<strong>负责**</strong>**<strong>的设计**</strong></strong>

Gemma是根据我们的AI原则设计的。作为使Gemma预训练模型安全可靠的一部分，我们使用自动化技术从训练集中过滤出某些个人信息和其他敏感数据。此外，我们使用了广泛的微调和人类反馈的强化学习（RLHF），以使我们的指导调整模型与负责任的行为保持一致。为了了解和减少Gemma模型的风险概况，我们进行了强大的评估，包括手动红队测试、自动对抗测试以及对模型进行危险活动能力的评估。这些评估在我们的模型卡中概述。

我们还将一个新的负责任生成AI工具包与Gemma一起发布，以帮助开发者和研究人员优先考虑构建安全和负责任的人工智能应用程序。该工具包包括：

&gt;&gt; 安全分类：我们提供了一种新颖的方法，用于使用最少的示例构建健壮的安全分类器。

&gt;&gt; 调试：模型调试工具可帮助您调查Gemma的行为并解决潜在问题。

&gt;&gt; 指导：您可以根据Google在开发和部署大型语言模型方面的经验，获取模型构建者的最佳实践。



### **<strong><strong>4、**</strong>**<strong>跨框架、工具和硬件的优化**</strong></strong>

您可以根据自己的数据微调Gemma模型，以适应特定的应用需求，例如摘要或检索增强生成（RAG）。Gemma支持各种工具和系统：

&gt;&gt; 多框架工具：使用多框架Keras 3.0、本地PyTorch、JAX和Hugging Face Transformers的推理和微调的参考实现，带上您喜爱的框架。

&gt;&gt; 跨设备兼容性：Gemma模型可以在各种流行设备类型上运行，包括笔记本电脑、台式电脑、物联网、移动和云，实现广泛可访问的人工智能功能。

&gt;&gt; 尖端硬件平台：我们与NVIDIA合作，优化Gemma以适用于NVIDIA GPU，从数据中心到云端再到本地RTX AI个人电脑，确保行业领先的性能和与尖端技术的集成。

&gt;&gt; 为Google Cloud优化：Vertex AI提供了广泛的MLOps工具集，具有一系列调优选项，并使用内置的推理优化进行一键部署。使用完全托管的Vertex AI工具或自管理的GKE，包括从任一平台的成本效益高的基础设施部署。



### **<strong><strong>5、**</strong>**<strong>用于研究和开发的免费信用额**</strong></strong>

Gemma是为驱动AI创新的开放开发者和研究人员社区构建的。您可以通过Kaggle的免费访问、Colab笔记本的免费套餐以及首次使用Google Cloud用户的300美元信用额来开始使用Gemma。研究人员还可以申请高达50万美元的Google Cloud信用额来加速他们的项目。







## **Gemma的安装**

### **<strong><strong>0、**</strong>**<strong>系统要求**</strong></strong>

Gemma可以在CPU、GPU和TPU上运行。对于GPU，我们建议在2B检查点上使用8GB+ GPU RAM，在7B检查点上使用24GB+ GPU RAM。





### **<strong><strong>1、**</strong>**<strong>安装**</strong></strong>

要安装Gemma，您需要使用Python 3.10或更高版本。

安装用于CPU、GPU或TPU的JAX。请按照JAX网站上的说明操作。

运行

```
python -m venv gemma-demo
. gemma-demo/bin/activate
pip install git+https://github.com/google-deepmind/gemma.git
```







### **<strong><strong>2、**</strong>**<strong>下载模型**</strong></strong>

模型检查点可通过Kaggle上的http://kaggle.com/models/google/gemma获取。选择其中一个Flax模型变体，单击⤓按钮下载模型存档，然后将内容提取到本地目录。存档包含模型权重和标记器，例如2b Flax变体包含：

2b/ # 包含模型权重的目录

tokenizer.model # 标记器



### **<strong><strong>3、**</strong>**<strong>运行单元测试**</strong></strong>

要运行单元测试，请安装可选的[test]依赖项（例如，在源树的根目录下使用pip install -e .[test]），然后：

pytest .

请注意，默认情况下会跳过sampler_test.py中的测试，因为Gemma源代码中未包含标记器。要运行这些测试，请按照上述说明下载标记器，并在sampler_test.py中的_VOCAB常量中更新路径。





### **<strong><strong>4、**</strong>**<strong>示例**</strong></strong>

要运行示例抽样脚本，请传递权重目录和标记器的路径：

```
python examples/sampling.py --
--path_checkpoint=/path/to/archive/contents/2b/
--path_tokenizer=/path/to/archive/contents/tokenizer.model
```

#### LLMs之Gemma：sampling.py文件解读—利用Gemma库加载预训练模型、分词器，并进行文本采样，用户通过指定命令行参数(如输入的字符串、生成的最大步数)来控制生成过程







## **Gemma的使用方法**

### **<strong><strong>1、**</strong>**<strong>Colab笔记本教程：**</strong></strong>

colabs/sampling_tutorial.ipynb 包含一个带有抽样示例的Colab笔记本。

colabs/fine_tuning_tutorial.ipynb 包含一个简单的教程，介绍了如何对Gemma进行微调，例如将英语翻译成法语。

colabs/gsm8k_eval.ipynb 是一个带有参考GSM8K评估实现的Colab。

要运行这些笔记本，您需要下载权重和标记器的本地副本（参见上文），并将ckpt_path和vocab_path变量更新为相应的路径。



#### LLMs之Gemma：sampling_tutorial.ipynb文件解读——利用预训练的Gemma模型进行自然语言采样生成





#### LLMs之Gemma：fine_tuning_tutorial.ipynb文件解读——利用fine-tuning方法调优2B的Gemma模型实现英法翻译任务





#### LLMs之Gemma：gsm8k_eval.ipynb文件解读——通过构建基于问题-答案对的 prompting 模式来评估Gemma模型在GSM8K数据集上的表现水平




