
--- 
title:  推荐系统（十）用户行为序列建模-Pooling 路线 
tags: []
categories: [] 

---
对推荐系统而言，准确捕捉用户兴趣是其面临的核心命题。不管是样本、特征还是模型结构等方面的优化，本质上做的事情都是在提高推荐系统对用户兴趣的捕捉能力，因此如何提高这种能力，对推荐效果的提升有重要作用，也是算法工程师日常工作的核心出发点。 用户历史行为是非常重要的信息。基于丰富、不同用户差异大、随时间不断变化的行为数据，如何有效利用这些信息，挖掘出用户隐藏在行为背后的真正兴趣，从而将其准确表达出来，既能体现出不同用户的差异性，又能捕捉到用户兴趣随着时间的变化，对推荐效果非常关键。

### 1.常用的特征

**推荐本质是排序，而排序则是特征的艺术** 。虽然特征工程看上去似乎没有深度模型那么“高大上”，但在实际业务中，基于特征工程优化，比基于模型更稳定可靠，且效果往往不比优化模型逊色。特征工程一定要结合业务理解，在具体业务场景上，想象自己就是一个实际用户，会有哪些特征对你是否点击、是否转化有比较大的影响。一般来说，可以枚举如下特征：

#### 1.1 Context 特征

如星期、时间、网络类型、操作系统、客户端版本等。

#### 1.2 User 特征

即常说的用户画像，可以共享其他 APP 或者同一 APP 不同场景内的、用户各个维度的特征（例如一些大型互联网企业，通常涉及多个电商、短视频、出行、支付等多个领域，因此可以很容易获得用户各个维度的特征，构建准确的用户画像），主要包括三部分 ：
- **静态特征**：User ID、性别、年龄、城市、职业、收入水平、是否大学生、是否结婚、是否有小孩、注册时间、是否 VIP、是否新用户等。静态特征一般区分度还是挺大的，比如不同性别、年龄的人，兴趣会差异很大。再比如是否有小孩，会直接决定母婴类目商品是否有兴趣。- **统计特征**：比如 User 近 30 天、14 天、7 天的 PV（Page View）、VV（Video View）、CTR（Click-Through-Rate）、完播率、单 VV 时长等，最好同时包括绝对值和相对值。毕竟 2 次曝光 1 次点击，和 200 次曝光 100 次点击，CTR 虽然相同，但其置信度天差地别。统计特征大多数都是后验特征，对模型预测帮助很大。统计特征一定要注意**【数据穿越】**问题，构造特征时千万不要把当天的统计数据也计算进去了。- **行为序列特征**：是目前研究热度极高的方向，也是精排模型优化的关键。可以构建用户短期点击序列和长期购买序列，也可以构建用户正反馈点击购买序列和负反馈曝光未点击序列。序列长度目前是一个痛点，序列过长时，Transformer 等模型计算量可能很大，导致模型 RT 和 P99 等指标扛不住，出现大量超时。
>  
 **数据穿越**：即采用未来数据来进行训练。举个例子：当前时刻的样本的统计值只能是当前时刻之前的，而不能使用之后的数据统计。假设小时更新 CTR 的话，每个样本的 CTR 值使用当前小时的样本总数统计，21 点 01 分的样本的 CTR 其实不能采用 21 点整体的 CTR 计算的，应该使用 21 点 01 分之前的数据计算。不然就会出现数据穿越问题，21 点 01 分的样本实际使用了未来的点击数据。 


#### 1.3 Item 特征

与 User 特征不同，Item 特征通常无法与其他 APP 共享，不同 APP 的 Item ID 等重要特征不能对齐，导致无法领域迁移。主要有如下特征：
- **静态特征**：如 Item ID、作者 ID、类目 ID、上架时间、清晰度、物理时长、Item Tag等。这些特征一般由机器识别、人工打标、用户填写运营审核等方式产出，十分重要。- **统计特征**：如 Item 近 14 天、7 天、3 天的 PV、VV(Video View)、CTR、完播率、单 VV 时长等，最好同时包括绝对值和相对值。跟 User 侧统计特征一样，要注意数据穿越问题。
#### 1.4 交叉特征

Item 与 User 交叉特征，比如 Item 在不同性别年龄用户上的统计特征。虽然模型可以实现自动特征交叉，但是否交叉得好就要另说了。手工构造关键的交叉特征，还是很有意义的。

### 2.如何处理特征

特征的处理主要有如下几种情况：

#### 2.1 离散值

直接 embedding，注意高维稀疏 ID 特征，比如 Item ID 和 User ID 的收敛问题。

#### 2.2 连续值

主要有两种方式：其一，直接与其他 embedding concat：操作简单，但泛化能力差；其二，正样本等频分桶，再离散化：泛化能力较强，是目前通用的解决方案。

#### 2.3 多值特征

最典型的就是**用户行为序列**，主要方法有：
- **mean-pooling、sum-pooling**：将行为序列中 Item 特征，逐个进行 mean-pooling 或者sum-pooling。- **att-pooling**：将行为序列中各 Item，与待打分 target Item，进行 attention 计算再平均，也就是加权平均，比如 DIN。这个方法考虑了 Item 的重要程度，也支持引入Item 的重要 side info，通过引入 item index，其实也可以带有一定的时序信息，可以作为序列建模的 baseline。- **序列建模**：将行为序列中各 Item，通过 GRU 等 RNN 模型，进行建模，取出最后一个位置的输出即可，比如 DIEN。此方法考虑了用户行为的时序关系和兴趣迁移，目前基本都使用 Transformer 来进行时序建模，可以缓解反向传播梯度弥散、长序列建模能力差、串行耗时高等问题。
### 3.为什么需要用户行为序列建模？

在推荐场景（如商品推荐、视频推荐、音乐推荐等）中，用户的行为数据通常非常丰富，当 Item 曝光给用户之后，用户可能会产生基于 Item 的多种行为，典型案例如下：
- **电商平台**：点击、浏览、加购、下单、退出等；- **视频平台**：点击、播放、点赞、评论、打赏、重复播放等；
上述些行为隐含了用户多样的兴趣，直接表达了用户对 Item 的喜好程度，当用户重复播放（或重复购买、重复点击）某 Item，则表明用户大概率对当前 Item 很感兴趣，当用户直接划过某 Item，则用户大概率对当前 Item 没有兴趣。在日常生活中，很多用户可能无法明确表达自己的想法、兴趣，但透过用户的行为，则可以把用户自身都没有感知到的兴趣捕捉到——正所谓：嘴虽硬，但身体很诚实。一个人的行为是检验其想法最好的标准。

除了丰富之外，用户历史行为数据，还具有差异大、变化快的特点：
1. **差异大**：不同用户的行为数据差异巨大，比如，一个对科技感兴趣的用户，其历史行为数据中通常会有大量科技相关的 Item；一个对音乐感兴趣的用户，相关的音乐 Item 在其历史行为中将高频出现；1. **变化快**：用户的行为数据变化快，呈现出的结果是行为分布随着时间变化，比如在电商场景，用户的行为可能消费需要而变化。当用户需要购买电冰箱时，通常会货比三家，因此用户将浏览大量电冰箱相关的 Item。然而，一旦用户完成电冰箱购买，短期内将不再具有该需求，因此用户对电冰箱相关 Item 的兴趣将急剧降低。
>  
 用户历史行为是非常重要的信息。基于丰富、不同用户差异大、随时间不断变化的行为数据，如何有效利用这些信息，挖掘出用户隐藏在行为背后的真正兴趣，从而将其准确表达出来，既能体现出不同用户的差异性，又能捕捉到用户兴趣随着时间的变化，对推荐效果非常关键。 


### 4.用户行为序列建模方法

深度学习时代，各种表征 embedding 化。在构建特征时，用户行为数据采用行为序列的方式来表示。随着深度学习在推荐领域的应用加强，用户行为序列特征受到越来越高的重视。在推荐场景中，用户兴趣建模，关键点在于如何利用用户的行为序列特征，得到有效的 embedding 来表征用户兴趣。针对此，不少方法被陆续提出。

早期使用的行为序列长度有限，往往在十或百的量级。这一两年随着模型越来越难做出效果，从业人员开始从数据和特征的角度进行改进，同时配合工程改造和性能提升，使用的行为序列长度逐渐加长，从十或百的量级提高到了千甚至万的量级，用户兴趣表征也逐渐从短序列向长序列发展。随着序列长度的增加，用户的兴趣也从单一表征向多兴趣发展。

短序列和长序列这两种方法在建模思路上不同，方法设计的出发点差异主要源自模型复杂度带来的性能压力。处理短序列时，业界使用的方法主要有：
1. **基于 pooling 的思路**，这种思路简单，直接采用 sum、mean 等 pooling 的方式；1. **基于 RNN 的序列化建模思路**，这种思路一般利用 RNN[1]、LSTM[2]、GRU[3] 等相关的循环神经网络实现；1. **基于 attention 思路**，这种思路分为 self attention 和 target attention，其中 self attention 典型的方法是 transformer[4]，target attention 包括 din[5]、dien[6]、dsin[7]等。
长序列的方法核心是解决序列长度面临的计算性能问题，包括 MIMN[8]，SIM[9] 等。

用户在实际场景中往往呈现多样的兴趣，因此业界也提出一些对用户多兴趣的建模方法，如 MIND[10]、DMIN[11] 等。

本篇先分享基于 pooling 的建模方法。在之后的文章中，将继续介绍 attention、长序列、多兴趣等方法。

#### 4.1 基于pooling 的思路

早期深度模型刚开始应用于推荐领域时，对序列特征的处理方式简单直接，采用 pooling 的思路。google 的 YouTube 团队发表在 2016 年 RecSys 会议的论文《Deep Neural Networks for YouTube Recommendations》[12] 采用 mean pooling 的方式处理序列特征，在此之后，该思路被业界广泛采用，sum pooling、mean pooling、max pooling 是该思路中常用的方法。

如图 1 所示，为论文采用的 DNN 方法，在序列特征的处理上，分别对用户搜索历史和观看历史的 embedding 向量加权平均，得到用户整体的搜索和观看的历史状态。 <img src="https://img-blog.csdnimg.cn/fc45b7cf6e3640f3b022de21228829fd.png#pic_center#pic_center" alt="Alt" width="600" height="400"> 我们先给出行为序列的形式化定义， 
     
      
       
       
         U 
        
       
         = 
        
        
        
          { 
         
         
         
           u 
          
         
           1 
          
         
        
          , 
         
         
         
           u 
          
         
           2 
          
         
        
          , 
         
         
         
           u 
          
         
           3 
          
         
        
          , 
         
        
          . 
         
        
          . 
         
        
          . 
         
        
          , 
         
         
         
           u 
          
         
           n 
          
         
        
          } 
         
        
       
      
        U=\left \{ u_{1},u_{2},u_{3},...,u_{n} \right \} 
       
      
    U={<!-- -->u1​,u2​,u3​,...,un​} 代表用户集合， 
     
      
       
       
         I 
        
       
         = 
        
        
        
          { 
         
         
         
           i 
          
         
           1 
          
         
        
          , 
         
         
         
           i 
          
         
           2 
          
         
        
          , 
         
         
         
           i 
          
         
           3 
          
         
        
          , 
         
        
          . 
         
        
          . 
         
        
          . 
         
        
          , 
         
         
         
           i 
          
         
           n 
          
         
        
          } 
         
        
       
      
        I=\left \{ i_{1},i_{2},i_{3},...,i_{n} \right \} 
       
      
    I={<!-- -->i1​,i2​,i3​,...,in​}代表物料（可以是短视频、商品、音乐等）集合，用户的一系列用户行为可以被表达为  
     
      
       
        
        
          B 
         
        
          u 
         
        
       
         = 
        
        
        
          { 
         
         
         
           b 
          
         
           1 
          
         
           u 
          
         
        
          , 
         
         
         
           b 
          
         
           2 
          
         
           u 
          
         
        
          , 
         
         
         
           b 
          
         
           3 
          
         
           u 
          
         
        
          , 
         
        
          . 
         
        
          . 
         
        
          . 
         
        
          , 
         
         
         
           b 
          
          
          
            ∣ 
           
           
           
             B 
            
           
             u 
            
           
          
            ∣ 
           
          
         
           u 
          
         
        
          } 
         
        
       
      
        B_{u}=\left \{ b_{1}^{u},b_{2}^{u},b_{3}^{u},...,b_{\left | B_{u} \right |}^{u} \right \} 
       
      
    Bu​={<!-- -->b1u​,b2u​,b3u​,...,b∣Bu​∣u​}， 
     
      
       
       
         ∣ 
        
        
        
          B 
         
        
          u 
         
        
       
         ∣ 
        
       
      
        \left | B_{u} \right | 
       
      
    ∣Bu​∣表示用户行为序列的长度； 
     
      
       
        
        
          b 
         
        
          i 
         
        
          u 
         
        
       
      
        b_{i}^{u} 
       
      
    biu​ 代表用户 u 的第 i 个历史行为，可以包含多种 side info 信息， 
     
      
       
        
        
          b 
         
        
          i 
         
        
          u 
         
        
       
         = 
        
        
        
          ( 
         
         
         
           s 
          
          
          
            i 
           
          
            , 
           
          
            1 
           
          
         
           u 
          
         
        
          , 
         
         
         
           s 
          
          
          
            i 
           
          
            , 
           
          
            2 
           
          
         
           u 
          
         
        
          , 
         
        
          . 
         
        
          . 
         
        
          . 
         
        
          , 
         
         
         
           s 
          
          
          
            i 
           
          
            , 
           
          
            k 
           
          
         
           u 
          
         
        
          ) 
         
        
       
      
        b_{i}^{u}=\left ( s_{i,1}^{u} ,s_{i,2}^{u},...,s_{i,k}^{u}\right ) 
       
      
    biu​=(si,1u​,si,2u​,...,si,ku​)， 
     
      
       
        
        
          s 
         
         
         
           i 
          
         
           , 
          
         
           k 
          
         
        
          u 
         
        
       
      
        s_{i,k}^{u} 
       
      
    si,ku​代表用户 u 的第 i 次行为的第 k 个 side info 信息，一般是物料的 ID、类目、发生行为的时间等。在实践中，可将用户的每一个行为转换为稠密向量： 
     
      
       
        
        
          e 
         
        
          i 
         
        
          u 
         
        
       
         = 
        
       
         c 
        
       
         o 
        
       
         n 
        
       
         c 
        
       
         a 
        
       
         t 
        
       
         ( 
        
       
         E 
        
       
         m 
        
       
         b 
        
       
         e 
        
       
         d 
        
       
         d 
        
       
         i 
        
       
         n 
        
       
         g 
        
       
         ( 
        
        
        
          b 
         
        
          i 
         
        
          u 
         
        
       
         ) 
        
       
         ) 
        
       
      
        e_{i}^{u}=concat(Embedding(b_{i}^{u})) 
       
      
    eiu​=concat(Embedding(biu​))，进而用户的行为可表示为： 
     
      
       
        
        
          E 
         
        
          u 
         
        
       
         = 
        
        
        
          { 
         
         
         
           e 
          
         
           1 
          
         
           u 
          
         
        
          , 
         
         
         
           e 
          
         
           2 
          
         
           u 
          
         
        
          , 
         
         
         
           e 
          
         
           3 
          
         
           u 
          
         
        
          , 
         
        
          . 
         
        
          . 
         
        
          . 
         
        
          , 
         
         
         
           e 
          
          
          
            ∣ 
           
           
           
             B 
            
           
             u 
            
           
          
            ∣ 
           
          
         
           u 
          
         
        
          } 
         
        
       
      
        E_{u}=\left \{ e_{1}^{u},e_{2}^{u},e_{3}^{u},...,e_{\left | B_{u} \right |}^{u} \right \} 
       
      
    Eu​={<!-- -->e1u​,e2u​,e3u​,...,e∣Bu​∣u​}

经过 mean-pooling 之后，得到结果为：  
      
       
        
         
         
           A 
          
         
           u 
          
         
        
          = 
         
        
          f 
         
        
          ( 
         
         
         
           E 
          
         
           u 
          
         
        
          ) 
         
        
          = 
         
         
         
           1 
          
          
          
            ∣ 
           
           
           
             B 
            
           
             u 
            
           
          
            ∣ 
           
          
         
         
         
           ∑ 
          
          
          
            i 
           
          
            = 
           
          
            1 
           
          
          
          
            ∣ 
           
           
           
             B 
            
           
             u 
            
           
          
            ∣ 
           
          
         
         
         
           e 
          
         
           i 
          
         
           u 
          
         
        
       
         A_{u}=f(E_{u})=\frac{1}{\left | B_{u} \right |} \sum_{i=1}^{\left | B_{u} \right |}e_{i}^{u} 
        
       
     Au​=f(Eu​)=∣Bu​∣1​i=1∑∣Bu​∣​eiu​

基于 pooling 的思路处理用户行为序列特征，操作简单直接，使用 tensorflow 自带的函数 tf.reduce_sum、tf.reduce_mean、tf.reduce_max 即可实现。

上述思路的缺点也很明显，将序列作为无序集合，对每个 Item 同等对待，无法区分不同 Item 的重要度，从而使用户兴趣的表征效果减弱。而在实际场景中，用户历史行为中不同的 Item 对用户当前兴趣表征能力不同，如相比于用户在过去一个月前浏览的 Item，用户当前的兴趣用一天前浏览的 Item 来表征更合适。

#### 4.2 引申：pooling 技术在图像处理领域的应用

在图像处理领域，池化层有一个很明显的作用：减少特征图大小，也就是可以减少计算量和所需显存。 **mean-pooling（平均池化）：即对邻域内特征点只求平均** 优缺点：能很好的保留背景，但容易使得图片变模糊 正向传播：邻域内取平均

<img src="https://img-blog.csdnimg.cn/bf0f01cc36f74d40bca1329a589fa5d1.png#pic_center" alt="Alt" width="500" height="250">

**max-pooling（最大池化）：即对邻域内特征点取最大**

优缺点：能很好的保留纹理特征，一般现在都用 max-pooling 而很少用 mean-pooling 正向传播：取邻域内最大，并记住最大值的索引位置，以方便反向传播 <img src="https://img-blog.csdnimg.cn/7e29e231feb64b11811bbbcced6ca46d.png#pic_center" alt="Alt" width="500" height="250">

**Stochastic-pooling（随机池化）：只需对 feature map 中的元素按照其概率值大小随机选择，即元素值大的被选中的概率也大**。而不像 max-pooling 那样，永远只取那个最大值元素。在区域内，将左图的数值进行归一化处理，即 1/（1+2+3+4）=0.1；2/10=0.2；3/10=0.3；4/10=0.4 <img src="https://img-blog.csdnimg.cn/9e166f84d3414320900b827144c9d648.png#pic_center" alt="Alt" width="400" height="170">

接着按照概率值来随机选择，一般情况概率大的，容易被选择到，比如选择到了概率值为 0.3 的时候，那么（1，2，3，4）池化之后的值为 3。使用 stochastic pooling 时，其推理过程也很简单，对矩阵区域求加权平均即可，比如上面图中，池化输出值为：1**0.1+2**0.2+3**0.3+4**0.4=3。

### 5.参考文献

https://weibo.com/ttarticle/p/show?id=2309634696248908382628
- 1-RNN(ICLR2015), RECURRENT NEURAL NETWORK REGULARIZATION. https://arxiv.org/pdf/1409.2329.pdf- 2-LSTM, Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting. https://arxiv.org/pdf/1506.04214.pdf- 3-GRU. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. https://arxiv.org/pdf/1406.1078.pdf.- 4-Attention is All you Need. https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf- 5-Deep Interest Network for Click-Through Rate Prediction. https://dl.acm.org/doi/pdf/10.1145/3219819.3219823- 6-Deep Interest Evolution Network for Click-Through Rate Prediction. https://arxiv.org/pdf/1809.03672.pdf- 7-Deep Session Interest Network for Click-Through Rate Prediction. https://arxiv.org/pdf/1905.06482.pdf- 8-Practice on Long Sequential User Behavior Modeling for Click-Through Rate Prediction. https://arxiv.org/pdf/1905.09248.pdf- 9-Search-based User Interest Modeling with Lifelong Sequential Behavior Data for Click-Through Rate Prediction. https://arxiv.org/pdf/2006.05639.pdf- 10-Multi-Interest Network with Dynamic Routing for Recommendation at Tmall. https://arxiv.org/pdf/1904.08030.pdf.- 11-Deep Multi-Interest Network for Click-through Rate Prediction. https://dl.acm.org/doi/pdf/10.1145/3340531.3412092.- 12-Deep Neural Networks for YouTube Recommendations. https://static.googleusercontent.com/media/research.google.com/zh-CN//pubs/archive/45530.pdf.- 13-https://blog.csdn.net/m0_59023219/article/details/130883277