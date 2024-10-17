
--- 
title:  有了这款神器，轻松用 Python 写个 APP 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/img_convert/45ea1b35513ea2b2fa0365d1ac0f12b7.png">

作者：Adrien Treuille

机器之心编译

机器学习开发者想要打造一款 App 有多难？事实上，你只需要会 Python 代码就可以了，剩下的工作都可以交给一个工具。近日，Streamlit 联合创始人 Adrien Treuille 撰文介绍其开发的机器学习工具开发框架——Streamlit，这是一款专为机器学习工程师创建的免费、开源 app 构建框架。这款工具可以在你写 Python 代码的时候，实时更新你的应用。目前，Streamlit 的 GitHub Star 量已经超过 3400，在 medim 上的热度更是达到了 9000+。

<img src="https://img-blog.csdnimg.cn/img_convert/ca82bf53b429e5ff5862ad19b18cf572.png">

Streamlit 网站：https://streamlit.io/

GitHub地址：https://github.com/streamlit/streamlit/

<img src="https://img-blog.csdnimg.cn/img_convert/bbfb1ccbb89eb1d1ef7bb6a1fed61cc7.gif">

**用 300 行 Python 代码，编程一个可实时执行神经网络推断的语义搜索引擎。**

以我的经验，每一个不平凡的机器学习项目都是用错误百出、难以维护的内部工具整合而成的。这些工具通常用 Jupyter Notebooks 和 Flask app 写成，很难部署，需要对客户端服务器架构（C/S 架构）进行推理，且无法与 Tensorflow GPU 会话等机器学习组件进行很好的整合。

我第一次看到此类工具是在卡内基梅隆大学，之后又在伯克利、Google X、Zoox 看到。这些工具最初只是小的 Jupyter notebook：传感器校准工具、仿真对比 app、激光雷达对齐 app、场景重现工具等。

当一个工具越来越重要时，项目经理会介入其中：进程和需求不断增加。这些单独的项目变成代码脚本，并逐渐发展成为冗长的「维护噩梦」……

<img src="https://img-blog.csdnimg.cn/img_convert/58b08c7a65bbdca47b6dfa4067bdfc1f.png">

**机器学习工程师创建 app 的流程（ad-hoc）。**

而当一个工具非常关键时，我们会组建工具团队。他们熟练地写 Vue 和 React，在笔记本电脑上贴满声明式框架的贴纸。他们的设计流程是这样式的：

<img src="https://img-blog.csdnimg.cn/img_convert/eae31b30a4af787386e658f0e5a2b412.png">

**工具团队构建 app 的流程（干净整洁，从零开始）。**

这简直太棒了！但是所有这些工具都需要新功能，比如每周上线新功能。然而工具团队可能同时支持 10 多个项目，他们会说：「我们会在两个月内更新您的工具。」

我们返回之前自行构建工具的流程：部署 Flask app，写 HTML、CSS 和 JavaScript，尝试对从 notebook 到样式表的所有一些进行版本控制。我和在 Google X 工作的朋友 Thiago Teixeira 开始思考：如果构建工具像写 Python 脚本一样简单呢？

我们希望在没有工具团队的情况下，机器学习工程师也能构建不错的 app。这些内部工具应该像机器学习工作流程的副产品那样自然而然地出现。写此类工具感觉就像训练神经网络或者在 Jupyter 中执行点对点分析（ad-hoc analysis）！同时，我们还想保留强大 app 框架的灵活性。我们想创造出令工程师骄傲的好工具。

我们希望的 app 构建流程如下：

<img src="https://img-blog.csdnimg.cn/img_convert/af261a5e8674fac3d696861eb5516bd9.png">

**Streamlit app 构建流程。**

与来自 Uber、Twitter、Stitch Fix、Dropbox 等的工程师一道，我们用一年时间创造了 Streamlit，这是一个针对机器学习工程师的免费开源 app 框架。不管对于任何原型，Streamlit 的核心原则都是更简单、更纯粹。

Streamlit 的核心原则如下：

1. 拥抱 Python

Streamlit app 是完全自上而下运行的脚本，没有隐藏状态。你可以利用函数调用来处理代码。只要你会写 Python 脚本，你就可以写 Streamlit app。例如，你可以按照以下代码对屏幕执行写入操作：

```
import streamlit as stst.write('Hello, world!')

```

<img src="https://img-blog.csdnimg.cn/img_convert/fca926a186f811386bd0cdefbec1e95d.png">

2. 把 widget 视作变量

Streamlit 中没有 callback！每一次交互都只是自上而下重新运行脚本。该方法使得代码非常干净：

```
import streamlit as stx = st.slider('x')
st.write(x, 'squared is', x * x)

```

<img src="https://img-blog.csdnimg.cn/img_convert/8be3ea834efb8155effb5fb2520ef539.png">

**3 行代码写成的 Streamlit 交互 app。**

3. 重用数据和计算

如果要下载大量数据或执行复杂计算，怎么办？关键在于在多次运行中安全地重用信息。Streamlit 引入了 cache primitive，它像一个持续的默认不可更改的数据存储器，保障 Streamlit app 轻松安全地重用信息。例如，以下代码只从 Udacity 自动驾驶项目（https://github.com/udacity/self-driving-car）中下载一次数据，就可得到一个简单快速的 app：

<img src="https://img-blog.csdnimg.cn/img_convert/457b304cf20f07883e50c8d3e20c7e3b.png">

**使用 st.cache，在 Streamlit 多次运行中保存数据。****代码运行说明，参见：**

**https://gist.github.com/treuille/c633dc8bc86efaa98eb8abe76478aa81#gistcomment-3041475。**

<img src="https://img-blog.csdnimg.cn/img_convert/353e1a0c8e166e94bb2ecfd3d89d37e2.png">

**运行以上 st.cache 示例的输出。**

简而言之，Streamlit 的工作流程如下：
1. 每次用户交互均需要从头运行全部脚本。1. Streamlit 根据 widget 状态为每个变量分配最新值。1. 缓存保证 Streamlit 重用数据和计算。
如下图所示：

<img src="https://img-blog.csdnimg.cn/img_convert/1d621006e9ff344b156a42c59bc07130.png">

**用户事件触发 Streamlit 从头开始重新运行脚本。****不同运行中仅保留缓存。**

感兴趣的话，你可以立刻尝试！只需运行以下行：

网页浏览器将自动打开，并转向本地 Streamlit app。如果没有出现浏览器窗口，只需点击链接。

<img src="https://img-blog.csdnimg.cn/img_convert/d99666300090b4ef98a00e6d83c59ca7.png">

这些想法很简洁，但有效，使用 Streamlit 不会妨碍你创建丰富有用的 app。我在 Zoox 和 Google X 工作时，看着自动驾驶汽车项目发展成为数 G 的视觉数据，这些数据需要搜索和理解，包括在图像数据上运行模型进而对比性能。我看到的每一个自动驾驶汽车项目都有整支团队在做这方面的工具。

在 Streamlit 中构建此类工具非常简单。以下 Streamlit demo 可以对整个 Udacity 自动驾驶汽车照片数据集执行语义搜索，对人类标注的真值标签进行可视化，并在 app 内实时运行完整的神经网络（YOLO）。

<img src="https://img-blog.csdnimg.cn/img_convert/50f75ec423e26dce0e1795872b3c9695.gif">

**这个 300 行代码写成的 Streamlit demo 结合了语义视觉搜索和交互式神经网络推断。**

整个 app 只有 300 行 Python 代码，其中大部分是机器学习代码。事实上，整个 app 里只有 23 次 Streamlit 调用。你可以试试看：

<img src="https://img-blog.csdnimg.cn/img_convert/68123cf490f2c792e4821b4cd316563b.png">

我们与机器学习团队合作，为他们的项目而努力时，逐渐意识到这些简单的想法会带来大量重要的收益：

Streamlit app 是纯 Python 文件。你可以使用自己喜欢的编辑器和 debugger。

<img src="https://img-blog.csdnimg.cn/img_convert/cdda04ef989934f4033a05c6a7bb83a5.png">

**我用 Streamlit 构建 app 时喜欢用 VSCode 编辑器（左）和 Chrome（右）。**

纯 Python 代码可与 Git 等源码控制软件无缝对接，包括 commits、pull requests、issues 和 comment。由于 Streamlit 的底层语言是 Python，因此你可以免费利用这些协作工具的好处。

<img src="https://img-blog.csdnimg.cn/img_convert/c4a9be268e961f1c4cd93e11f824be9d.png">

**Streamlit app 是 Python 脚本，因此你可以使用 Git 轻松执行版本控制。**

Streamlit 提供即时模式的编程环境。当 Streamlit 检测出源文件变更时，只需点击 Always rerun 即可。

<img src="https://img-blog.csdnimg.cn/img_convert/4f78f97f3e0e7d0271d886117c5d5c19.png">

**点击「Always rerun」，保证实时编程。**

缓存简化计算流程。一连串缓存函数自动创建出高效的计算流程！你可以尝试以下代码：

<img src="https://img-blog.csdnimg.cn/img_convert/85c1aa8e03bd4e686154da8de3fed9bd.png">

**Streamlit 中的简单计算流程。****运行以上代码，参见说明：**

**https://gist.github.com/treuille/ac7755eb37c63a78fac7dfef89f3517e#gistcomment-3041436。**

基本上，该流程涉及加载元数据到创建摘要等步骤（load_metadata → create_summary）。该脚本每次运行时，Streamlit 仅需重新计算该流程的子集即可。

<img src="https://img-blog.csdnimg.cn/img_convert/d98baa2aa3d83637c86c911ac342e539.png">

**为了保证 app 的可执行性，Streamlit 仅计算更新 UI 所必需的部分。**

Streamlit 适用于 GPU。Streamlit 可以直接访问机器级原语（如 TensorFlow、PyTorch），并对这些库进行补充。例如，以下 demo 中，Streamlit 的缓存存储了整个英伟达 PGGAN。该方法可使用户在更新左侧滑块时，app 执行近乎即时的推断。

<img src="https://img-blog.csdnimg.cn/img_convert/9e2fbae1c651cbf400a937628303e35a.gif">

**该 Streamlit app 使用 TL-GAN 展示了英伟达 PGGAN 的效果。**

Streamlit 是免费开源库，而非私有 web app。你可以本地部署 Streamlit app，不用提前联系我们。你甚至可以在不联网的情况下在笔记本电脑上本地运行 Streamlit。此外，现有项目也可以渐进地使用 Streamlit。

<img src="https://img-blog.csdnimg.cn/img_convert/714def0eb951cc991c8536d550a53f23.png">

**渐进地使用 Streamlit 的几种方式。**

以上只是 Streamlit 功能的冰山一角而已。它最令人兴奋的一点是，这些原语可以轻松组成复杂 app，但看起来却只是简单脚本。这就要涉及架构运作原理和功能了，本文暂不谈及。

<img src="https://img-blog.csdnimg.cn/img_convert/27d678dfe94d7d601d4d48dd2b9099ca.png">

**Streamlit 组件图示。**

我们很高兴与社区分享 Streamlit，希望它能够帮助大家轻松将 Python 脚本转化为美观实用的机器学习 app。

**原文链接：****https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace**

&lt; END &gt;

<img src="https://img-blog.csdnimg.cn/img_convert/35de4911a13e2fa1a9317ec11beef098.gif">

微信扫码关注，了解更多内容
