
--- 
title:  关系抽取：SemEval2010 Task8数据集 
tags: []
categories: [] 

---
### 任务描述

SemEval2010 Task8详细信息请参考。

#### 任务：

对于给定了的句子和两个做了标注的名词，从给定的关系清单中选出最合适的关系。

关系清单（9+1）如下所示：
<td style="width:107px;">关系</td><td style="width:347px;">定义</td><td style="width:398px;">例子</td>
<td style="width:107px;"> Cause-Effect （因果关系） </td><td style="width:347px;"> Cause-Effect(X, Y)  is true for a sentence S that mentions entities X and Y if and only if (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails that X is the cause of Y, or that X causes/makes/produces/emits/... Y. </td><td style="width:398px;"> "A person infected with a particular &lt;e1&gt;flu&lt;/e1&gt; &lt;e2&gt;virus&lt;/e2&gt; strain develops an antibody against that virus." Cause-Effect(e2, e1) Comment: flu is a state, virus is the causal agent, thus (a) is satisfied; the virus is actively involved in causing flu and thus (c) is satisfied. </td>

（因果关系）

(1) S, X and Y are in accordance with the general annotation guidelines ()

"A person infected with a particular &lt;e1&gt;flu&lt;/e1&gt; &lt;e2&gt;virus&lt;/e2&gt; strain develops an antibody against that virus."

Comment: flu is a state, virus is the causal agent, thus (a) is satisfied; the virus is actively involved in causing flu and thus (c) is satisfied.
<td style="width:107px;"> Instrument-Agency </td><td style="width:347px;"> Instrument-Agency(X, Y) is true of a sentence S that mentions entities X and Y if and only if: (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails the fact that X is the instrument (tool) of Y or, equivalently, that Y uses X. </td><td style="width:398px;"> "A person infected with a particular &lt;e1&gt;flu&lt;/e1&gt; &lt;e2&gt;virus&lt;/e2&gt; strain develops an antibody against that virus." Cause-Effect(e2, e1) Comment: flu is a state, virus is the causal agent, thus (a) is satisfied; the virus is actively involved in causing flu and thus (c) is satisfied. </td>

Instrument-Agency(X, Y) is true of a sentence S that mentions entities X and Y if and only if:

(2) the situation described in S entails the fact that X is the instrument (tool) of Y or, equivalently, that Y uses X.

Cause-Effect(e2, e1)
<td style="width:107px;"> Product-Producer （生产与被生产之间的关系） </td><td style="width:347px;"> Product-Producer (X, Y) is true for a sentence S that mentions entities X and Y if and only if: (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails the fact that X is a product of Y, or Y produces X. </td><td style="width:398px;"> "The &lt;e1&gt;honey&lt;/e1&gt; &lt;e2&gt;bee&lt;/e2&gt; is the third insect genome published by scientists, after a lab workhorse, the fruit fly, and a health menace, the mosquito." Product-Producer(e1, e2) Comment: This is a typical example of Product-Producer. Honey is a tangible concrete object (c), and the bee is actively involved in producing it (a). </td>

（生产与被生产之间的关系）

(1) S, X and Y are in accordance with the general annotation guidelines ()

"The &lt;e1&gt;honey&lt;/e1&gt; &lt;e2&gt;bee&lt;/e2&gt; is the third insect genome published by scientists, after a lab workhorse, the fruit fly, and a health menace, the mosquito."

Comment: This is a typical example of Product-Producer. Honey is a tangible concrete object (c), and the bee is actively involved in producing it (a).
<td style="width:107px;"> Content-Container </td><td style="width:347px;"> Content-Container(X, Y) is true for a sentence S that mentions entities X and Y if and only if (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails that X is or was (usually temporarily) stored or carried inside Y. </td><td style="width:398px;"> "The &lt;e1&gt;apples&lt;/e1&gt; are in the &lt;e2&gt;basket&lt;/e2&gt;." Content-Container(e1, e2) Comment: This is a prototypical example of Content-Container. </td>

Content-Container(X, Y) is true for a sentence S that mentions entities X and Y if and only if

(2) the situation described in S entails that X is or was (usually temporarily) stored or carried inside Y.

Content-Container(e1, e2)
<td style="width:107px;"> Entity-Origin </td><td style="width:347px;"> Entity-Origin(X, Y) is true for a sentence S that mentions the entities X and Y if and only if (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails that Y is the origin of an entity X (rather than its location), and X is coming or derived from that origin. </td><td style="width:398px;"> "Under state law, minors are not permitted to have &lt;e1&gt;grain&lt;/e1&gt; &lt;e2&gt;alcohol&lt;/e2&gt;, even if a parent provides it to their children." Entity-Origin(e2, e1) Comment: This is a prototypical example of a material Entity-Origin relation. Restriction (b.4) applies. </td>

Entity-Origin(X, Y) is true for a sentence S that mentions the entities X and Y if and only if

(2) the situation described in S entails that Y is the origin of an entity X (rather than its location), and X is coming or derived from that origin.

Entity-Origin(e2, e1)
<td style="width:107px;"> Entity-Destination </td><td style="width:347px;"> Entity-Destination(X, Y) is true for a sentence S that mentions the entities X and Y if and only if: (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails the fact that Y is the destination of X in the sense of X moving (in a physical or abstract sense) toward Y. </td><td style="width:398px;"> "The&lt;e1&gt;boy&lt;/e1&gt; ran into the school &lt;e2&gt;cafeteria&lt;/e2&gt;." Entity-Destination(e1,e2) Comment: school cafeteria is a spatial/geographical destination. </td>

Entity-Destination(X, Y) is true for a sentence S that mentions the entities X and Y if and only if:

(2) the situation described in S entails the fact that Y is the destination of X in the sense of X moving (in a physical or abstract sense) toward Y.

Entity-Destination(e1,e2)
<td style="width:107px;"> Component - Whole </td><td style="width:347px;"> Component-Whole (X,Y) is true for a sentence S that mentions entities X and Y if and only if: (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails that X is a component of Y; (3) X has a functional relation with Y. In other words, X has an operating or usable purpose within Y. </td><td style="width:398px;"> We don't need Einstein's quantum mechanics to understand why each &lt;e1&gt;hand&lt;/e1&gt; has 5 &lt;e2&gt;fingers&lt;/e2&gt;, and not 4 or 6. Component-Whole(e2, e1) Comment: Fingers are functional, integral parts of the hand. </td>

Component-Whole (X,Y) is true for a sentence S that mentions entities X and Y if and only if:

(2) the situation described in S entails that X is a component of Y;

We don't need Einstein's quantum mechanics to understand why each &lt;e1&gt;hand&lt;/e1&gt; has 5 &lt;e2&gt;fingers&lt;/e2&gt;, and not 4 or 6.

Comment: Fingers are functional, integral parts of the hand.
<td style="width:107px;"> Member-Collection </td><td style="width:347px;"> Member-Collection(X, Y) is true for a sentence S that mentions entities X and Y if and only if: (1) S, X and Y are in accordance with the general annotation guidelines () (2) the situation described in S entails the fact that X is a member of Y. </td><td style="width:398px;"> "Italian playing cards most commonly consist of a &lt;e1&gt;deck&lt;/e1&gt; of 40 &lt;e2&gt;cards&lt;/e2&gt;." Member-Collection(e2, e1) Comment: A deck is a collection of cards, cards are different and separable from the deck, not functional to the deck. </td>

Member-Collection(X, Y) is true for a sentence S that mentions entities X and Y if and only if:

(2) the situation described in S entails the fact that X is a member of Y.

Member-Collection(e2, e1)
<td style="width:107px;"> Message-Topic </td><td style="width:347px;"> Message-Topic(X, Y) is true for a sentence S that mentions the entities X and Y if and only if:   (1) S, X and Y are in accordance with the general annotation guidelines ()   (2) the situation described in S entails the fact that X is a communicative message containing information about Y. </td><td style="width:398px;"> "The recommendations contained the following key &lt;e1&gt;points&lt;/e1&gt; about the &lt;e2&gt;new politics&lt;/e2&gt; of the government." Message-Topic(e1, e2) Comment: politics is the topic of the key points. </td>

Message-Topic(X, Y) is true for a sentence S that mentions the entities X and Y if and only if:

(1) S, X and Y are in accordance with the general annotation guidelines ()

(2) the situation described in S entails the fact that X is a communicative message containing information about Y.

Message-Topic(e1, e2)
<td style="width:107px;">Other</td><td style="width:347px;">当句子中实体之前不满足前九种关系时，将标签设置为Other</td><td style="width:398px;"> </td>

各类数据的占比如下图所示：

                      <img alt="" class="has" src="https://img-blog.csdnimg.cn/20190315111003445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5ODgzNTkx,size_16,color_FFFFFF,t_70">

### 数据集
1. **Trial Dataset：****试验数据集于2009年8月30日发布，它包含前五个关系的数据。但是，其中也包含了一些其他四种关系的引用，  这些数据在试验数据集上可以被视为Other关系，而不必多加处理。**1. **Training Dataset:训练集包含8000个样例，涵盖上文提到的9+1中关系。**1. **Development Dataset：没有提供官方开发集，但是参与者可以使用该部分训练数据集来调整期参数，如使用交叉验证。**1. **Test Dataset：测试集包含2717个样例，涵盖上文提到的9+1中关系，于2010年3月18日发布。**1. **WordNet senses提示：和SemEval-2007 Task 4不同，此处不提供人工标注的WordNet senses，会使得任务更加真实。**
### **SemEval-2010 Task 8 VS SemEval-2007 Task 4**
- l**相比****于****2007****中对于每一种关系提供一个****单独****的数据集和一个对应的二分类任务，****2010****仅仅提供一个单独的多类别数据集。**- l**多****分类任务**- l**候选的实体仍然会提供，但是评测系统需要去决策实体在关系中的槽位。**- l**WordNet senses ****和** **query ****strings****将不再提供。**- l**数据****集中数据量大了很多（超过****10000****条标记的句子）。**- l**关系的集合也变大了**
### 难点

**关系清单种中两组相近的关系：**

l**组****1****：**
- l****Component-Whole****- l****Member-Collection****- l****都是********Part-Whole********的特殊情况****
l****组********2********：****
- l****Content-Container****- l****Entity-Origin****- l****Entity-Destination****- l****可以通过考虑所表达的状态是静态的还是动态的进行区分****
 
