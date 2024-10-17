
--- 
title:  驾驭AI绘画：《AI魔法绘画》带你秒变顶级画手！ 
tags: []
categories: [] 

---
  大家好，我是herosunly。985院校硕士毕业，现担任算法研究员一职，热衷于机器学习算法研究与应用。曾获得阿里云天池比赛第一名，CCF比赛第二名，科大讯飞比赛第三名。拥有多项发明专利。对机器学习和深度学习拥有自己独到的见解。曾经辅导过若干个非计算机专业的学生进入到算法行业就业。希望和大家一起成长进步。

  今天给大家带来的文章是驾驭AI绘画：《AI魔法绘画》带你秒变顶级画手！，希望能对学习AI绘画的同学们有所帮助。



#### 文章目录
- - - - 


## 1. 前言

同学们，抖音买家秀中的那些极具设计感的作品是怎么来的？

你还在羡慕别人的绘画天赋，对着空白的画纸发呆吗？

有没有想过将生硬的代码和灵动的艺术完美融合？

有没有感到现代技术带来了戏剧性改变，从替代马车的汽车，到取代传统影像的数字摄影，再到今天的AI美术创作？

**是的，“AI绘画”，它来了。**

AI绘画，如雷贯耳，无处不在。

曾几何时，人们认为艺术需要人工创作，需要才情与灵感的瞬间迸发。

然而，技术的高速发展，打破了这种观念，AI绘画正在逐渐崭露头角，成为新的画坛巨擘。

但聊一聊看似高大上的AI技术可能让你觉得高不可攀。那就跟我一起，**用Stable Diffusion挑战无限可能，一窥AI绘画的花花世界！**

<img src="https://img-blog.csdnimg.cn/img_convert/0b71cb00d011159b3f3e1f1d12fb8139.jpeg#pic_center" alt="">   Stable Diffusion WebUI 中的核心组件，人脸图像面部画面修复模型 CodeFormer的核心代码如下所示：

```
import math
import torch
from torch import nn, Tensor
import torch.nn.functional as F
from typing import Optional

from modules.codeformer.vqgan_arch import VQAutoEncoder, ResBlock
from basicsr.utils.registry import ARCH_REGISTRY


class CodeFormer(VQAutoEncoder):
    def __init__(self, dim_embd=512, n_head=8, n_layers=9,
                codebook_size=1024, latent_size=256,
                connect_list=('32', '64', '128', '256'),
                fix_modules=('quantize', 'generator')):
        super(CodeFormer, self).__init__(512, 64, [1, 2, 2, 4, 4, 8], 'nearest',2, [16], codebook_size)

        if fix_modules is not None:
            for module in fix_modules:
                for param in getattr(self, module).parameters():
                    param.requires_grad = False

        self.connect_list = connect_list
        self.n_layers = n_layers
        self.dim_embd = dim_embd
        self.dim_mlp = dim_embd*2

        self.position_emb = nn.Parameter(torch.zeros(latent_size, self.dim_embd))
        self.feat_emb = nn.Linear(256, self.dim_embd)

        # transformer
        self.ft_layers = nn.Sequential(*[TransformerSALayer(embed_dim=dim_embd, nhead=n_head, dim_mlp=self.dim_mlp, dropout=0.0)
                                    for _ in range(self.n_layers)])

        # logits_predict head
        self.idx_pred_layer = nn.Sequential(
            nn.LayerNorm(dim_embd),
            nn.Linear(dim_embd, codebook_size, bias=False))

        self.channels = {<!-- -->
            '16': 512,
            '32': 256,
            '64': 256,
            '128': 128,
            '256': 128,
            '512': 64,
        }

        # after second residual block for &gt; 16, before attn layer for ==16
        self.fuse_encoder_block = {<!-- -->'512':2, '256':5, '128':8, '64':11, '32':14, '16':18}
        # after first residual block for &gt; 16, before attn layer for ==16
        self.fuse_generator_block = {<!-- -->'16':6, '32': 9, '64':12, '128':15, '256':18, '512':21}

        # fuse_convs_dict
        self.fuse_convs_dict = nn.ModuleDict()
        for f_size in self.connect_list:
            in_ch = self.channels[f_size]
            self.fuse_convs_dict[f_size] = Fuse_sft_block(in_ch, in_ch)

    def _init_weights(self, module):
        if isinstance(module, (nn.Linear, nn.Embedding)):
            module.weight.data.normal_(mean=0.0, std=0.02)
            if isinstance(module, nn.Linear) and module.bias is not None:
                module.bias.data.zero_()
        elif isinstance(module, nn.LayerNorm):
            module.bias.data.zero_()
            module.weight.data.fill_(1.0)

    def forward(self, x, w=0, detach_16=True, code_only=False, adain=False):
        # ################### Encoder #####################
        enc_feat_dict = {<!-- -->}
        out_list = [self.fuse_encoder_block[f_size] for f_size in self.connect_list]
        for i, block in enumerate(self.encoder.blocks):
            x = block(x)
            if i in out_list:
                enc_feat_dict[str(x.shape[-1])] = x.clone()

        lq_feat = x
        # ################# Transformer ###################
        # quant_feat, codebook_loss, quant_stats = self.quantize(lq_feat)
        pos_emb = self.position_emb.unsqueeze(1).repeat(1,x.shape[0],1)
        # BCHW -&gt; BC(HW) -&gt; (HW)BC
        feat_emb = self.feat_emb(lq_feat.flatten(2).permute(2,0,1))
        query_emb = feat_emb
        # Transformer encoder
        for layer in self.ft_layers:
            query_emb = layer(query_emb, query_pos=pos_emb)

        # output logits
        logits = self.idx_pred_layer(query_emb) # (hw)bn
        logits = logits.permute(1,0,2) # (hw)bn -&gt; b(hw)n

        if code_only: # for training stage II
          # logits doesn't need softmax before cross_entropy loss
            return logits, lq_feat

        # ################# Quantization ###################
        # if self.training:
        #     quant_feat = torch.einsum('btn,nc-&gt;btc', [soft_one_hot, self.quantize.embedding.weight])
        #     # b(hw)c -&gt; bc(hw) -&gt; bchw
        #     quant_feat = quant_feat.permute(0,2,1).view(lq_feat.shape)
        # ------------
        soft_one_hot = F.softmax(logits, dim=2)
        _, top_idx = torch.topk(soft_one_hot, 1, dim=2)
        quant_feat = self.quantize.get_codebook_feat(top_idx, shape=[x.shape[0],16,16,256])
        # preserve gradients
        # quant_feat = lq_feat + (quant_feat - lq_feat).detach()

        if detach_16:
            quant_feat = quant_feat.detach() # for training stage III
        if adain:
            quant_feat = adaptive_instance_normalization(quant_feat, lq_feat)

        # ################## Generator ####################
        x = quant_feat
        fuse_list = [self.fuse_generator_block[f_size] for f_size in self.connect_list]

        for i, block in enumerate(self.generator.blocks):
            x = block(x)
            if i in fuse_list: # fuse after i-th block
                f_size = str(x.shape[-1])
                if w&gt;0:
                    x = self.fuse_convs_dict[f_size](enc_feat_dict[f_size].detach(), x, w)
        out = x
        # logits doesn't need softmax before cross_entropy loss
        return out, logits, lq_feat

```

## 2. 书籍推荐《AI魔法绘画：用Stable Diffusion挑战无限可能》

俗话说，知识就是力量，掌握AI绘画技术，你不仅可以创造出令人眼花缭乱的艺术作品，还可能在众多同行中脱颖而出，走上职业生涯的新高峰。

看看那些因为AI的到来，开始大规模裁员的公司，你是否意识到了自己该学习AI绘画的重要性？答案是明显的。掌握潮流，主宰未来，你准备好了吗？

这里，向大家强烈推荐一本书——**《AI魔法绘画：用Stable Diffusion挑战无限可能》**。

<img src="https://img-blog.csdnimg.cn/img_convert/0abf6794829d5333488281adea7eb54b.png#pic_center" alt="">

**它是一本以实际操作为导向的入门级AI绘画图书。**

书中详细讲解了基于Stable Diffusion进行AI绘画的完整学习路线，包括绘画技巧、图片生成、提示词编写、ControlNet插件、模型训练等等。

如果你是零基础，无须恐惧，书中涵盖了丰富的实际操作案例，易懂易学，轻松入门。

如果你已经步入职场，那么这本书中的丰富技术内容，绝对能让你大有收获。

<img src="https://img-blog.csdnimg.cn/img_convert/581c99eede6f21bd5cc62b899f67c0e0.png#pic_center" alt="">

重要的是，本书的内容超级全面。无论是始于入门的基础理论知识，还是No-Code模型训练必备的ControlNet插件的详解，甚至是AI绘画全流程的操作教程，本书一应俱全，让你提前预知并掌握AI绘画的全貌，**将你从菜鸟级别提升至大师级**。

<img src="https://img-blog.csdnimg.cn/img_convert/5bb2bf7b99654af3fd77a899a606b7cd.png#pic_center" alt="">

此外，**书中包括了一些非常实用的商业设计案例，**如家具效果图、AI插画与插图、AI宠物、原创IP角色、自媒体运营等，这将为你的创新设计思路添砖加瓦！

<img src="https://img-blog.csdnimg.cn/img_convert/aa38d905f85898c9967723611f0799ba.jpeg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/794ced291f829c40027d238f8c39e5de.jpeg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/58ca75bfed63870a4bcbd4dcd0ad9464.jpeg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/be7cf0185f92fbc841ec1c4cdf227b9e.jpeg#pic_center" alt="">

**……**

**资源丰富，内容详细，各章节知识体系完备，示例形象生动，操作步骤清晰明了**，还有读者交流群可与作者互动，**本书简直是你学习AI绘画的绝佳教程！**

<img src="https://img-blog.csdnimg.cn/img_convert/a6f3fb9e5cf2fb6b4f7ad64175317101.png#pic_center" alt="">

朋友们，生活永远充满无限可能。

但是，如果你想把握未来的潮流，扬帆起航，那么记得装备自己，勇往直前。

快来！开始你的AI绘画之旅，与我一起，**用《AI魔法绘画，用stable Diffusion挑战无限可能》探秘AI绘画的奥妙之处，**在不断迭代的技术驱动下，一起走进神奇的AI绘画世界，一起挑战无限可能吧！

<img src="https://img-blog.csdnimg.cn/img_convert/4ca77fbc8223e89661292c3a4312438b.png#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/5a9c43db1c0924cd0f65996fdbd5cdc4.png#pic_center" alt="">

## 3. 粉丝福利

  🎁本次送书1~3本【取决于阅读量，阅读量越多，送的越多】👈   ⌛️活动时间：截止到2024-1月13号   ✳️参与方式：关注博主+三连（点赞、收藏、评论）

## 4. 自主购买

  小伙伴也可以访问链接进行自主购买哦~

  直达京东购买链接🔗：购买地址
