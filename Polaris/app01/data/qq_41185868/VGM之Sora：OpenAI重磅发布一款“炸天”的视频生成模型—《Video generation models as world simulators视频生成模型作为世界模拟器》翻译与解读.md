
--- 
title:  VGM之Sora：OpenAI重磅发布一款“炸天”的视频生成模型—《Video generation models as world simulators视频生成模型作为世界模拟器》翻译与解读 
tags: []
categories: [] 

---
VGM之Sora：OpenAI重磅发布一款“炸天”的视频生成模型—《Video generation models as world simulators视频生成模型作为世界模拟器》翻译与解读





**目录**

































































## **相关文章**

### **<strong><strong>AI之Sora：Sora(文本指令生成视频的里程碑模型)的简介(能力/安全性/技术细节)、使用方法、案例应用之详细攻略**</strong></strong>





### **<strong><strong>VGM之Sora：OpenAI重磅发布一款“炸天”的视频生成模型—《Video generation models as world simulators视频生成模型作为世界模拟器》翻译与解读**</strong></strong>





## **《Video generation models as world simulators**视频生成模型作为世界模拟器**》翻译与解读**
<td style="vertical-align:top;width:37.55pt;"> **<strong>地址**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 文章地址： </td>

文章地址：
<td style="vertical-align:top;width:37.55pt;"> **<strong>时间**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 2024年2月15日 </td>

2024年2月15日
<td style="vertical-align:top;width:37.55pt;"> **<strong>作者**</strong> </td><td style="vertical-align:top;width:388.55pt;"> OpenAI </td>

OpenAI
<td style="vertical-align:top;width:37.55pt;"> **<strong>总结**</strong> </td><td style="vertical-align:top;width:388.55pt;"> 此文章阐述了OpenAI开发的**<strong>视频生成模型**</strong>**<strong>Sora**</strong>，并将其视为模拟真实世界的潜在世界模拟器。 ****<strong><em>背景****</em></strong>：之前的视频生成模型通常只能处理特定类别或短视频，无法处理不同时长、分辨率和比例的视频。之前的视频生成模型都局限于特定类别或时长较短的视频，难以大规模地学习各种格式和时长的视频数据。这限制了它们成为通用世界模拟器的能力。 ****<strong><em>解决方案****</em></strong>： &gt;&gt; 将视频和图片转化为统一的三维时空patch表示，让模型可以学习各种格式和分辨率的视觉数据。 &gt;&gt; 使用transformer模型处理patch表示，并将其应用于视频生成领域，实现大规模学习。 &gt;&gt; 训练模型不对视频进行裁剪缩放，保留原始尺寸和比例，提高生成效果。 &gt;&gt; 通过大量描述性字幕训练，提升条件生成视频的语言理解能力。 ****<strong><em>关键技术****</em></strong>： &gt;&gt; 将不同视频和图片统一表示为“视觉补丁”，即将视频压缩为低维空间后分解为时空补丁，实现跨视频样式训练。 &gt;&gt;使用变分自编码器将视觉数据压缩为统一的低维表示，然后提取时空补丁作为Transformer的输入tokens。 &gt;&gt;将Transformer用于视频生成，发现它也能很好地应用于视频，生成效果随训练规模不断提升。 &gt;&gt;直接在原始尺寸上训练，而不是对视频进行resize、crop等规格化处理，提升生成视频的框架和组成质量。 &gt;&gt;通过描述性字幕和GPT对用户提示进行生成，使生成视频能更好跟随用户需求。 ****<strong><em>主要优势****</em></strong>： &gt;&gt;可以生成不同时长、分辨率和比例的视频，实现采样灵活度。 &gt;&gt;性能和质量随训练规模不断提升，可以生成1分钟高清视频。 &gt;&gt;可以利用图片和视频作为输入进行生成和编辑，实现广泛应用场景。 &gt;&gt;在一定程度上具备三维一致性、长期连贯性或长程协同能力等世界模拟能力。 &gt;&gt;相比前工作，该模型直接利用自训练数据规模得以实现上述优势。 总之，文章认为通过继续扩大视频模型的规模训练，有望构建功能全面、高质量的物理和数字世界模拟器。随着学习规模的继续扩大，视频生成模型很可能实现更加强大的世界模拟能力，了解及模拟现实世界中的物体、动物和人的行为。Sora示范了这一方法未来的发展方向。 </td>

此文章阐述了OpenAI开发的**<strong>视频生成模型**</strong>**<strong>Sora**</strong>，并将其视为模拟真实世界的潜在世界模拟器。

****<strong><em>解决方案****</em></strong>：

&gt;&gt; 使用transformer模型处理patch表示，并将其应用于视频生成领域，实现大规模学习。

&gt;&gt; 通过大量描述性字幕训练，提升条件生成视频的语言理解能力。

&gt;&gt; 将不同视频和图片统一表示为“视觉补丁”，即将视频压缩为低维空间后分解为时空补丁，实现跨视频样式训练。

&gt;&gt;将Transformer用于视频生成，发现它也能很好地应用于视频，生成效果随训练规模不断提升。

&gt;&gt;通过描述性字幕和GPT对用户提示进行生成，使生成视频能更好跟随用户需求。

&gt;&gt;可以生成不同时长、分辨率和比例的视频，实现采样灵活度。

&gt;&gt;可以利用图片和视频作为输入进行生成和编辑，实现广泛应用场景。

&gt;&gt;相比前工作，该模型直接利用自训练数据规模得以实现上述优势。



## **引言**
<td style="vertical-align:top;width:240.05pt;"> We explore large-scale training of generative models on video data. Specifically, we train text-conditional diffusion models jointly on videos and images of variable durations, resolutions and aspect ratios. We leverage a transformer architecture that operates on spacetime patches of video and image latent codes. Our largest model, Sora, is capable of generating a minute of high fidelity video. Our results suggest that scaling video generation models is a promising path towards building general purpose simulators of the physical world. </td><td style="vertical-align:top;width:186.05pt;"> 我们探索了在视频数据上进行大规模生成模型训练的方法。具体来说，我们联合训练了文本条件扩散模型，这些模型能够处理变化的视频和图像，包括可变持续时间、分辨率和长宽比等方面的变化。我们利用了一个能够处理视频和图像潜在编码的时空补丁的transformer 架构。我们最大的模型 **<strong>Sora **</strong>能够生成一分钟的高保真视频。我们的研究结果表明，**<strong>扩展视频生成模型**</strong>是建立通用物理世界模拟器的一个有前途的路径。 </td>

我们探索了在视频数据上进行大规模生成模型训练的方法。具体来说，我们联合训练了文本条件扩散模型，这些模型能够处理变化的视频和图像，包括可变持续时间、分辨率和长宽比等方面的变化。我们利用了一个能够处理视频和图像潜在编码的时空补丁的transformer 架构。我们最大的模型 **<strong>Sora **</strong>能够生成一分钟的高保真视频。我们的研究结果表明，**<strong>扩展视频生成模型**</strong>是建立通用物理世界模拟器的一个有前途的路径。





## **View Sora overview查看Sora概述**

<img alt="" height="509" src="https://img-blog.csdnimg.cn/direct/616c877f3cda4fc5af396d31af883082.gif" width="889">
<td style="vertical-align:top;width:243.55pt;"> This technical report focuses on (1) our method for turning visual data of all types into a unified representation that enables large-scale training of generative models, and (2) qualitative evaluation of Sora’s capabilities and limitations. Model and implementation details are not included in this report. Much prior work has studied generative modeling of video data using a variety of methods, including recurrent networks,1,2,3 generative adversarial networks,4,5,6,7 autoregressive transformers,8,9 and diffusion models.10,11,12 These works often focus on a narrow category of visual data, on shorter videos, or on videos of a fixed size. Sora is a generalist model of visual data—it can generate videos and images spanning diverse durations, aspect ratios and resolutions, up to a full minute of high definition video. </td><td style="vertical-align:top;width:182.55pt;"> 本技术报告主要关注以下两点： (1)我们将各种类型的视觉数据转换为统一的表示形式，从而实现能够大规模训练生成模型方法； (2)对 Sora 的能力和限制进行定性评估。模型和实现细节不包括在本报告中。 许多先前的工作已经使用各种方法研究了视频数据的生成建模，包括****<strong><em>循环网络、生成对抗网络、自回归****</em></strong>****<strong><em>transformer****</em></strong>和****<strong><em>扩散模型****</em></strong>。这些工作通常集中一类视觉数据、较短的视频或固定大小的视频上。**<strong>Sora **</strong>是一种视觉数据的通用模型——它可以生成跨越不同持续时间、长宽比和分辨率的视频和图像，甚至可以生成一分钟的高清视频。 </td>

Much prior work has studied generative modeling of video data using a variety of methods, including recurrent networks,1,2,3 generative adversarial networks,4,5,6,7 autoregressive transformers,8,9 and diffusion models.10,11,12 These works often focus on a narrow category of visual data, on shorter videos, or on videos of a fixed size. Sora is a generalist model of visual data—it can generate videos and images spanning diverse durations, aspect ratios and resolutions, up to a full minute of high definition video.

(1)我们将各种类型的视觉数据转换为统一的表示形式，从而实现能够大规模训练生成模型方法；

许多先前的工作已经使用各种方法研究了视频数据的生成建模，包括****<strong><em>循环网络、生成对抗网络、自回归****</em></strong>****<strong><em>transformer****</em></strong>和****<strong><em>扩散模型****</em></strong>。这些工作通常集中一类视觉数据、较短的视频或固定大小的视频上。**<strong>Sora **</strong>是一种视觉数据的通用模型——它可以生成跨越不同持续时间、长宽比和分辨率的视频和图像，甚至可以生成一分钟的高清视频。





### **<strong><strong>Turning visual data into patches将视觉数据转换为补丁**</strong></strong>

<img alt="" height="372" src="https://img-blog.csdnimg.cn/direct/8bd35fc9970a451e90fb64498dc2a0f2.png" width="1200">
<td style="vertical-align:top;width:240.05pt;"> We take inspiration from large language models which acquire generalist capabilities by training on internet-scale data.13,14 The success of the LLM paradigm is enabled in part by the use of tokens that elegantly unify diverse modalities of text—code, math and various natural languages. In this work, we consider how generative models of visual data can inherit such benefits. Whereas LLMs have text tokens, Sora has visual patches. Patches have previously been shown to be an effective representation for models of visual data.15,16,17,18 We find that patches are a highly-scalable and effective representation for training generative models on diverse types of videos and images. </td><td style="vertical-align:top;width:186.05pt;"> 我们受到大型语言模型的启发，这些模型通过在互联网规模的数据上训练获得了通用能力。LLM 范式的成功部分得益于优雅地(通过令牌)统一了文本的各种形式，包括代码、数学和各种自然语言。在这项工作中，我们考虑了视觉数据的生成模型如何继承这些好处。而**<strong> LLM 有文本令牌**</strong>，**<strong>Sora 有视觉补丁**</strong>。补丁已被证明是视觉数据模型的一种有效表示形式。我们发现，补丁是一种高度可扩展且有效的表示形式，适用于训练各种类型的视频和图像生成模型。 </td>

我们受到大型语言模型的启发，这些模型通过在互联网规模的数据上训练获得了通用能力。LLM 范式的成功部分得益于优雅地(通过令牌)统一了文本的各种形式，包括代码、数学和各种自然语言。在这项工作中，我们考虑了视觉数据的生成模型如何继承这些好处。而**<strong> LLM 有文本令牌**</strong>，**<strong>Sora 有视觉补丁**</strong>。补丁已被证明是视觉数据模型的一种有效表示形式。我们发现，补丁是一种高度可扩展且有效的表示形式，适用于训练各种类型的视频和图像生成模型。
<td style="vertical-align:top;width:240.05pt;"> At a high level, we turn videos into patches by first compressing videos into a lower-dimensional latent space,19 and subsequently decomposing the representation into spacetime patches. </td><td style="vertical-align:top;width:186.05pt;"> 在高层次上，我们首先将视频压缩到一个较低维度的潜在空间，然后将其分解为时空补丁，从而将视频转化为补丁。 </td>

在高层次上，我们首先将视频压缩到一个较低维度的潜在空间，然后将其分解为时空补丁，从而将视频转化为补丁。





#### **<strong><strong>Figure Patches**</strong></strong>



### **<strong><strong>Video compression network视频压缩网络**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> We train a network that reduces the dimensionality of visual data.20 This network takes raw video as input and outputs a latent representation that is compressed both temporally and spatially. Sora is trained on and subsequently generates videos within this compressed latent space. We also train a corresponding decoder model that maps generated latents back to pixel space. </td><td style="vertical-align:top;width:186.05pt;"> 我们训练了一个降低视觉数据维度的网络。该网络以原始视频作为输入，并输出一个在时间和空间上都被压缩的潜在表示。Sora 在这个压缩的潜在空间上进行训练，然后生成视频。我们还训练了一个相应的**<strong>解码器模型**</strong>，将生成的潜在表示映射回像素空间。  </td>

我们训练了一个降低视觉数据维度的网络。该网络以原始视频作为输入，并输出一个在时间和空间上都被压缩的潜在表示。Sora 在这个压缩的潜在空间上进行训练，然后生成视频。我们还训练了一个相应的**<strong>解码器模型**</strong>，将生成的潜在表示映射回像素空间。





### **<strong><strong>Spacetime Latent Patches时空潜在补丁**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Given a compressed input video, we extract a sequence of spacetime patches which act as transformer tokens. This scheme works for images too since images are just videos with a single frame. Our patch-based representation enables Sora to train on videos and images of variable resolutions, durations and aspect ratios. At inference time, we can control the size of generated videos by arranging randomly-initialized patches in an appropriately-sized grid. </td><td style="vertical-align:top;width:186.05pt;"> 给定一个压缩的输入视频，我们提取一个时空补丁序列，作为transformer的标记。这个方案也适用于图像，因为图像只是单帧的视频。我们基**<strong>于补丁的表示**</strong>使Sora能够在不同分辨率、持续时间和宽高比的视频和图像上进行训练。在推理时，我们可以通过在适当大小的网格中安排随机初始化的补丁来控制生成视频的大小。 </td>

给定一个压缩的输入视频，我们提取一个时空补丁序列，作为transformer的标记。这个方案也适用于图像，因为图像只是单帧的视频。我们基**<strong>于补丁的表示**</strong>使Sora能够在不同分辨率、持续时间和宽高比的视频和图像上进行训练。在推理时，我们可以通过在适当大小的网格中安排随机初始化的补丁来控制生成视频的大小。





### **<strong><strong>Scaling transformers for video generation扩展视频生成的transformer**</strong></strong>

<img alt="" height="312" src="https://img-blog.csdnimg.cn/direct/cdcfb8d7e7b74d5f8bb022f2a98fc6d6.png" width="1200">
<td style="vertical-align:top;width:240.05pt;"> Sora is a diffusion model21,22,23,24,25; given input noisy patches (and conditioning information like text prompts), it’s trained to predict the original “clean” patches. Importantly, Sora is a diffusion transformer.26 Transformers have demonstrated remarkable scaling properties across a variety of domains, including language modeling,13,14 computer vision,15,16,17,18 and image generation.27,28,29 </td><td style="vertical-align:top;width:186.05pt;"> Sora 是一个扩散模型；给定噪声补丁输入（以及文本提示等条件信息），它被训练来预测原始的“干净”补丁。重要的是，**<strong>Sora **</strong>是一个扩散transformer。transformer在各种领域，包括语言建模、计算机视觉和图像生成中，已经展示了卓越的扩展性能。 </td>

Sora 是一个扩散模型；给定噪声补丁输入（以及文本提示等条件信息），它被训练来预测原始的“干净”补丁。重要的是，**<strong>Sora **</strong>是一个扩散transformer。transformer在各种领域，包括语言建模、计算机视觉和图像生成中，已经展示了卓越的扩展性能。
<td style="vertical-align:top;width:240.05pt;"> In this work, we find that diffusion transformers scale effectively as video models as well. Below, we show a comparison of video samples with fixed seeds and inputs as training progresses. Sample quality improves markedly as training compute increases. </td><td style="vertical-align:top;width:186.05pt;"> 在这项工作中，我们发现扩散变压器在视频模型中也能有效扩展。下面，我们展示了随着训练计算量增加，具有固定种子和输入的视频样本的比较。随着训练计算量的增加，样本质量显著提高。 </td>

在这项工作中，我们发现扩散变压器在视频模型中也能有效扩展。下面，我们展示了随着训练计算量增加，具有固定种子和输入的视频样本的比较。随着训练计算量的增加，样本质量显著提高。

<img alt="" height="622" src="https://img-blog.csdnimg.cn/direct/34bbbc2da63541898a765dfe79fac0dd.gif" width="1200">



#### **<strong><strong>Figure Diffusion**</strong></strong>





### **<strong><strong>Variable durations, resolutions, aspect ratios不同持续时间、分辨率、长宽比**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Past approaches to image and video generation typically resize, crop or trim videos to a standard size – e.g., 4 second videos at 256x256 resolution. We find that instead training on data at its native size provides several benefits. </td><td style="vertical-align:top;width:186.05pt;"> 过去的图像和视频生成方法通常是调整大小，裁剪或修剪视频到标准尺寸-例如，例如，256x256 分辨率的 4 秒视频。我们发现，训练原始尺寸的数据而不是调整大小带来了几个好处。 </td>

过去的图像和视频生成方法通常是调整大小，裁剪或修剪视频到标准尺寸-例如，例如，256x256 分辨率的 4 秒视频。我们发现，训练原始尺寸的数据而不是调整大小带来了几个好处。





#### **<strong><strong>Sampling flexibility抽样的灵活性**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Sora can sample widescreen 1920x1080p videos, vertical 1080x1920 videos and everything inbetween. This lets Sora create content for different devices directly at their native aspect ratios. It also lets us quickly prototype content at lower sizes before generating at full resolution—all with the same model. </td><td style="vertical-align:top;width:186.05pt;"> Sora 可以抽样宽屏 1920x1080p 视频、竖屏 1080x1920 视频以及两者之间的所有情况。这使得 Sora 可以直接按照其原生长宽比为不同设备创建内容。这还允许我们在生成完整分辨率之前，以较低的尺寸快速原型化内容——而且这一切都是使用同一个模型完成的。 </td>

Sora 可以抽样宽屏 1920x1080p 视频、竖屏 1080x1920 视频以及两者之间的所有情况。这使得 Sora 可以直接按照其原生长宽比为不同设备创建内容。这还允许我们在生成完整分辨率之前，以较低的尺寸快速原型化内容——而且这一切都是使用同一个模型完成的。

<img alt="" height="535" src="https://img-blog.csdnimg.cn/direct/71e1dc9ff18d4efaadbdc719ccef4907.gif" width="1200">



#### **<strong><strong>Improved framing and composition改进框架和构图**</strong></strong>

<img alt="" height="435" src="https://img-blog.csdnimg.cn/direct/152e90318bba46e88006434fc3c54ba8.gif" width="892">
<td style="vertical-align:top;width:240.05pt;"> We empirically find that training on videos at their native aspect ratios improves composition and framing. We compare Sora against a version of our model that crops all training videos to be square, which is common practice when training generative models. The model  trained on square crops (left) sometimes generates videos where the subject is only partially in view. In comparison, videos from Sora (right)s have improved framing. </td><td style="vertical-align:top;width:186.05pt;"> 我们经验性地发现，训练视频时使用其原生长宽比可以改善构图和组合。我们将 Sora 与将所有训练视频裁剪为方形的模型版本进行了比较，这是在训练生成模型时常见的做法。 在方形裁剪(左图)上训练的模型，有时会生成部分不在视野中的视频。相比之下，Sora 生成的视频（右侧）具有改进的构图。 </td>

我们经验性地发现，训练视频时使用其原生长宽比可以改善构图和组合。我们将 Sora 与将所有训练视频裁剪为方形的模型版本进行了比较，这是在训练生成模型时常见的做法。





## **Language understanding语言理解**
<td style="vertical-align:top;width:240.05pt;"> Training text-to-video generation systems requires a large amount of videos with corresponding text captions. We apply the re-captioning technique introduced in DALL·E 330 to videos. We first train a highly descriptive captioner model and then use it to produce text captions for all videos in our training set. We find that training on highly descriptive video captions improves text fidelity as well as the overall quality of videos. Similar to DALL·E 3, we also leverage GPT to turn short user prompts into longer detailed captions that are sent to the video model. This enables Sora to generate high quality videos that accurately follow user prompts. </td><td style="vertical-align:top;width:186.05pt;"> 训练文本到视频生成系统需要大量带有相应文本说明的视频。我们将DALL·E 3中介绍的重新标题(字幕)化技术应用到视频中。我们首先训练一个高度描述性的字幕模型，然后使用它为我们训练集中的所有视频生成文本字幕。我们发现，在高度描述性的视频标题上进行训练不仅可以提高文本的准确性，还可以提高视频的整体质量。 与DALL·E 3类似，我们还利用GPT将简短的用户提示转换为更长的详细字幕，并将其发送到视频模型。这使得Sora能够准确地按照用户提示生成高质量的视频。 </td>

Similar to DALL·E 3, we also leverage GPT to turn short user prompts into longer detailed captions that are sent to the video model. This enables Sora to generate high quality videos that accurately follow user prompts.

与DALL·E 3类似，我们还利用GPT将简短的用户提示转换为更长的详细字幕，并将其发送到视频模型。这使得Sora能够准确地按照用户提示生成高质量的视频。





## **Prompting with images and videos使用图像和视频进行提示**
<td style="vertical-align:top;width:240.05pt;"> All of the results above and in our landing page show text-to-video samples. But Sora can also be prompted with other inputs, such as pre-existing images or video. This capability enables Sora to perform a wide range of image and video editing tasks—creating perfectly looping video, animating static images, extending videos forwards or backwards in time, etc. </td><td style="vertical-align:top;width:186.05pt;"> 上面的所有结果和我们的登陆页面都显示了文本到视频的示例。但Sora也可以通过其他输入进行提示，比如预先存在的图像或视频。这种能力使 Sora 能够执行各种图像和视频编辑任务——创建完美循环视频、为静态图像添加动画、向前或向后延长视频等。 </td>

上面的所有结果和我们的登陆页面都显示了文本到视频的示例。但Sora也可以通过其他输入进行提示，比如预先存在的图像或视频。这种能力使 Sora 能够执行各种图像和视频编辑任务——创建完美循环视频、为静态图像添加动画、向前或向后延长视频等。





### **<strong><strong>Animating DALL·E images为 DALL·E 图像添加动画**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Sora is capable of generating videos provided an image and prompt as input. Below we show example videos generated based on DALL·E 231 and DALL·E 330 images. </td><td style="vertical-align:top;width:186.05pt;"> **<strong>Sora **</strong>能够根据输入的图像和提示生成视频。下面我们展示了基于 DALL·E 2 和 DALL·E 3 图像生成的示例视频。 </td>

**<strong>Sora **</strong>能够根据输入的图像和提示生成视频。下面我们展示了基于 DALL·E 2 和 DALL·E 3 图像生成的示例视频。
<td style="vertical-align:top;width:240.05pt;"> A Shiba Inu dog wearing a beret and black turtleneck.  Monster Illustration in flat design style of a diverse family of monsters. The group includes a furry brown monster, a sleek black monster with antennas, a spotted green monster, and a tiny polka-dotted monster, all interacting in a playful environment. </td><td style="vertical-align:top;width:186.05pt;"> 一只戴着贝雷帽和黑色高领衫的柴犬狗。 以扁平设计风格描绘的多样化怪物家族插画。该群体包括一只毛茸茸的棕色怪物、一只带有天线的光滑黑色怪物、一只斑点绿色怪物和一只带有小圆点的微小怪物，它们在一个充满活泼氛围的环境中互动。 </td>



一只戴着贝雷帽和黑色高领衫的柴犬狗。
<td style="vertical-align:top;width:240.05pt;"> An image of a realistic cloud that spells “SORA”.  In an ornate, historical hall, a massive tidal wave peaks and begins to crash. Two surfers, seizing the moment, skillfully navigate the face of the wave. </td><td style="vertical-align:top;width:186.05pt;"> 一张写有“SORA”字样的逼真云朵图片。 在一座华丽的历史性大厅中，一股巨大的潮水波峰开始翻滚。两名冲浪者抓住机会，熟练地驾驭着波浪的表面。 </td>



一张写有“SORA”字样的逼真云朵图片。









### **<strong><strong>Extending generated videos扩展生成视频**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Sora is also capable of extending videos, either forward or backward in time. Below are four videos that were all extended backward in time starting from a segment of a generated video. As a result, each of the four videos starts different from the others, yet all four videos lead to the same ending. </td><td style="vertical-align:top;width:186.05pt;"> Sora还能够在时间上向前或向后延长视频。下面是四个视频，它们都是从一个生成的视频片段开始向后延长的。因此，这四个视频的开始都不同，但四个视频的结局都是一样的。 </td>

Sora还能够在时间上向前或向后延长视频。下面是四个视频，它们都是从一个生成的视频片段开始向后延长的。因此，这四个视频的开始都不同，但四个视频的结局都是一样的。
<td style="vertical-align:top;width:240.05pt;"> We can use this method to extend a video both forward and backward to produce a seamless infinite loop. </td><td style="vertical-align:top;width:186.05pt;"> 我们可以使用这种方法来向前和向后扩展视频，以产生无缝的无限循环。 </td>

我们可以使用这种方法来向前和向后扩展视频，以产生无缝的无限循环。



### **<strong><strong>Video-to-video editing**</strong>**<strong>视频到视频编辑**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Diffusion models have enabled a plethora of methods for editing images and videos from text prompts. Below we apply one of these methods, SDEdit,32 to Sora. This technique enables Sora to transform  the styles and environments of input videos zero-shot. </td><td style="vertical-align:top;width:186.05pt;"> **<strong>扩散模型**</strong>已经为根据文本提示编辑图像和视频提供了大量方法。下面我们将其中一种方法 SDEdit 应用到 Sora 上。这种技术使 Sora 能够以零样本的方式转换输入视频的风格和环境。 </td>

**<strong>扩散模型**</strong>已经为根据文本提示编辑图像和视频提供了大量方法。下面我们将其中一种方法 SDEdit 应用到 Sora 上。这种技术使 Sora 能够以零样本的方式转换输入视频的风格和环境。





#### **<strong><strong>把场景设置成茂密的丛林**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Input video change the setting to be in a lush jungle </td><td style="vertical-align:top;width:186.05pt;"> 输入视频 把场景设置成茂密的丛林 </td>

change the setting to be in a lush jungle

把场景设置成茂密的丛林







### **<strong><strong>Connecting videos连接视频**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> We can also use Sora to gradually interpolate between two input videos, creating seamless transitions between videos with entirely different subjects and scene compositions. In the examples below, the videos in the center interpolate between the corresponding videos on the left and right. </td><td style="vertical-align:top;width:186.05pt;"> 我们还可以使用Sora在两个输入视频之间逐渐插入，在具有完全不同主题和场景构图的视频之间创建无缝过渡。在下面的例子中，中间的视频插值了左侧和右侧相应视频之间的差异。 </td>

我们还可以使用Sora在两个输入视频之间逐渐插入，在具有完全不同主题和场景构图的视频之间创建无缝过渡。在下面的例子中，中间的视频插值了左侧和右侧相应视频之间的差异。



## **Image generation capabilities图像生成功能**
<td style="vertical-align:top;width:240.05pt;"> Sora is also capable of generating images. We do this by arranging patches of Gaussian noise in a spatial grid with a temporal extent of one frame. The model can generate images of variable sizes—up to 2048x2048 resolution. </td><td style="vertical-align:top;width:186.05pt;"> Sora还能生成图像。我们通过在时空范围内将高斯噪声补丁排列成空间网格来实现这一点。该模型可以生成各种尺寸的图像，分辨率最高可达 2048x2048。 </td>

Sora还能生成图像。我们通过在时空范围内将高斯噪声补丁排列成空间网格来实现这一点。该模型可以生成各种尺寸的图像，分辨率最高可达 2048x2048。
<td style="vertical-align:top;width:240.05pt;"> Close-up portrait shot of a woman in autumn, extreme detail, shallow depth of field Vibrant coral reef teeming with colorful fish and sea creatures Digital art of a young tiger under an apple tree in a matte painting style with gorgeous details A snowy mountain village with cozy cabins and a northern lights display, high detail and photorealistic dslr, 50mm f/1.2 </td><td style="vertical-align:top;width:186.05pt;"> 一张极其详细的、拍摄于秋天的女性特写照，景深较浅。 一个充满色彩斑斓的珊瑚礁，鱼类和海洋生物繁盛。 一幅数字艺术作品，采用哑光油画风格描绘了一只年轻的老虎站在苹果树下，细节精美。 一个被雪覆盖的山村，有舒适的小屋和北极光的展示，高度细致且接近照片般真实，使用50mm f/1.2的数码单反相机拍摄。 </td>

Vibrant coral reef teeming with colorful fish and sea creatures

A snowy mountain village with cozy cabins and a northern lights display, high detail and photorealistic dslr, 50mm f/1.2

一个充满色彩斑斓的珊瑚礁，鱼类和海洋生物繁盛。

一个被雪覆盖的山村，有舒适的小屋和北极光的展示，高度细致且接近照片般真实，使用50mm f/1.2的数码单反相机拍摄。







## **Emerging simulation capabilities新兴的模拟能力**
<td style="vertical-align:top;width:240.05pt;"> We find that video models exhibit a number of interesting emergent capabilities when trained at scale. These capabilities enable Sora to simulate some aspects of people, animals and environments from the physical world. These properties emerge without any explicit inductive biases for 3D, objects, etc.—they are purely phenomena of scale. </td><td style="vertical-align:top;width:186.05pt;"> 我们发现视频模型在大规模训练时表现出许多有趣的新兴能力。这些能力使得 Sora 能够从现实世界中模拟人、动物和环境的某些方面。这些属性在没有任何关于 3D、物体等明确归纳偏差的情况下出现——它们纯粹是规模现象。 </td>

我们发现视频模型在大规模训练时表现出许多有趣的新兴能力。这些能力使得 Sora 能够从现实世界中模拟人、动物和环境的某些方面。这些属性在没有任何关于 3D、物体等明确归纳偏差的情况下出现——它们纯粹是规模现象。



### **<strong><strong>3D consistency**</strong>**<strong>一致性**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Sora can generate videos with dynamic camera motion. As the camera shifts and rotates, people and scene elements move consistently through three-dimensional space. </td><td style="vertical-align:top;width:186.05pt;"> Sora可以生成带有动态摄像机运动的视频。随着摄像机的移动和旋转，人物和场景元素在三维空间中始终如一地移动。 </td>

Sora可以生成带有动态摄像机运动的视频。随着摄像机的移动和旋转，人物和场景元素在三维空间中始终如一地移动。



### **<strong><strong>Long-range coherence and object permanence长程连贯性和对象持久性**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> A significant challenge for video generation systems has been maintaining temporal consistency when sampling long videos. We find that Sora is often, though not always, able to effectively model both short- and long-range dependencies. For example, our model can persist people, animals and objects even when they are occluded or leave the frame. Likewise, it can generate multiple shots of the same character in a single sample, maintaining their appearance throughout the video. </td><td style="vertical-align:top;width:186.05pt;"> 视频生成系统面临的一个重大挑战是在抽样长视频时保持时间一致性。我们发现Sora经常(虽然不是总是)能够有效地为短期和长期依赖关系建模。例如，我们的模型可以持续存在人物、动物和物体，即使它们被遮挡或离开画面。同样，它可以在单个样本中生成同一角色的多个镜头，并在整个视频中保持它们的外观。 </td>

视频生成系统面临的一个重大挑战是在抽样长视频时保持时间一致性。我们发现Sora经常(虽然不是总是)能够有效地为短期和长期依赖关系建模。例如，我们的模型可以持续存在人物、动物和物体，即使它们被遮挡或离开画面。同样，它可以在单个样本中生成同一角色的多个镜头，并在整个视频中保持它们的外观。





### **<strong><strong>Interacting with the world**</strong>**<strong>与世界互动**</strong></strong>
<td style="vertical-align:top;width:240.05pt;"> Sora can sometimes simulate actions that affect the state of the world in simple ways. For example, a painter can leave new strokes along a canvas that persist over time, or a man can eat a burger and leave bite marks. </td><td style="vertical-align:top;width:186.05pt;"> Sora有时可以用简单的方式模拟影响世界状态的行为。例如，一位画家可以在画布上留下新的笔触，这些笔触随着时间的推移而保持不变，或者一个人可以吃汉堡并留下咬痕。 </td>

Sora有时可以用简单的方式模拟影响世界状态的行为。例如，一位画家可以在画布上留下新的笔触，这些笔触随着时间的推移而保持不变，或者一个人可以吃汉堡并留下咬痕。





### **<strong><strong>Simulating digital worlds**</strong>**<strong>模拟数字世界**</strong></strong>
<td style="vertical-align:top;width:253.55pt;"> Sora is also able to simulate artificial processes–one example is video games. Sora can simultaneously control the player in Minecraft with a basic policy while also rendering the world and its dynamics in high fidelity. These capabilities can be elicited zero-shot by prompting Sora with captions mentioning “Minecraft.” These capabilities suggest that continued scaling of video models is a promising path towards the development of highly-capable simulators of the physical and digital world, and the objects, animals and people that live within them. </td><td style="vertical-align:top;width:172.55pt;"> Sora还能够模拟人工过程，比如视频游戏。Sora 可以同时在 Minecraft 中控制玩家并以高保真度渲染世界及其动态。通过在提及“Minecraft”的标题中提示 Sora，可以零样本调用这些功能。 这些功能表明，视频模型的持续缩放是发展物理和数字世界以及生活在其中的物体、动物和人的高性能模拟器的一条有希望的道路。 </td>

These capabilities suggest that continued scaling of video models is a promising path towards the development of highly-capable simulators of the physical and digital world, and the objects, animals and people that live within them.

这些功能表明，视频模型的持续缩放是发展物理和数字世界以及生活在其中的物体、动物和人的高性能模拟器的一条有希望的道路。



## **Discussion讨论**
<td style="vertical-align:top;width:240.05pt;"> Sora currently exhibits numerous limitations as a simulator. For example, it does not accurately model the physics of many basic interactions, like glass shattering. Other interactions, like eating food, do not always yield correct changes in object state. We enumerate other common failure modes of the model—such as incoherencies that develop in long duration samples or spontaneous appearances of objects—in our landing page. </td><td style="vertical-align:top;width:186.05pt;"> 作为一个模拟器，**<strong>Sora**</strong>目前显示出许多局限性。例如，它不能准确地模拟许多基本相互作用的物理过程，比如玻璃破碎。其他的交互，比如吃东西，并不总是在对象状态中产生正确的变化。我们在登陆页面中列举了模型的其他常见故障模式，例如在长时间样本中发展的不一致性或物体的突然出现。 </td>

作为一个模拟器，**<strong>Sora**</strong>目前显示出许多局限性。例如，它不能准确地模拟许多基本相互作用的物理过程，比如玻璃破碎。其他的交互，比如吃东西，并不总是在对象状态中产生正确的变化。我们在登陆页面中列举了模型的其他常见故障模式，例如在长时间样本中发展的不一致性或物体的突然出现。
<td style="vertical-align:top;width:240.05pt;"> We believe the capabilities Sora has today demonstrate that continued scaling of video models is a promising path towards the development of capable simulators of the physical and digital world, and the objects, animals and people that live within them. </td><td style="vertical-align:top;width:186.05pt;"> 我们相信，Sora今天所拥有的能力表明，视频模型的持续缩放是一条很有前途的道路，可以开发出物理和数字世界的模拟器，以及生活在其中的物体、动物和人。 </td>

我们相信，Sora今天所拥有的能力表明，视频模型的持续缩放是一条很有前途的道路，可以开发出物理和数字世界的模拟器，以及生活在其中的物体、动物和人。










