
--- 
title:  【Matlab】Matlab 汉/英语(A/a)声学特征比较与基音频率分析（源码+音频文件）【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>Matlab 汉/英声学特征比较与基音频率分析</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - -  
  
  


## 一、设计目的

使用 MATLAB 代码旨在通过详细分析汉语中的“a”和英语中的"A"这两个音素的语音特性，揭示同一音素在不同语言中的发音差异。它通过读取和处理语音样本，计算短时平均能量和幅度，绘制这些特性的图表，以及运用短时自相关法和平均幅度差法（AMDF）检测基音周期，从而提供对汉语和英语“A”音在能量、幅度和基频等方面差异的深入理解。 这一分析对于语音识别、语言学习、语音合成等领域具有重要价值，有助于促进跨语言交流的技术发展。

>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 


## 二、设计思路
1.  **录制音频**：录制汉语“a”和英语"A"的语音信号，并获取其采样率。 1.  **单声道处理**：如果音频是双声道的，则将其转换为单声道，以便后续处理。 1.  **计算短时平均能量和短时平均幅度**：通过调用相应的函数，计算汉语“a”和英语"A"语音信号的短时平均能量和短时平均幅度。 1.  **绘制能量和幅度图**：利用计算得到的短时平均能量和短时平均幅度，绘制出汉语“a”和英语"A"的能量和幅度变化图。 <li> **基音周期检测**： 
  1. 使用短时自相关法（Autocorrelation）检测基音周期，并得到基音频率。1. 使用短时平均幅度差法（AMDF）检测基音周期，并得到基音频率。 </li>1.  **绘制自相关曲线和AMDF曲线**：绘制汉语“a”和英语"A"的短时自相关曲线和短时平均幅度差曲线，以便观察基音周期检测的结果。 
>  
 👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 


## 三、代码实现
<li> **读取音频文件**： <pre><code class="prism language-matlab">[hanYu, fs1] = audioread('chinese_a.m4a');
[yingYu, fs2] = audioread('english_A.m4a');
</code></pre> 使用 `audioread` 函数读取汉语“a”和英语"A"的音频文件，分别存储在 `hanYu` 和 `yingYu` 变量中。`fs1` 和 `fs2` 是对应的采样频率。 </li><li> **音频处理**： <pre><code class="prism language-matlab">if size(hanYu, 2) == 2
    hanYu = mean(hanYu, 2);
end
if size(yingYu, 2) == 2
    yingYu = mean(yingYu, 2);
end
</code></pre> 检查音频是否为双声道，如果是，则将其转换为单声道。这是通过计算双声道样本的平均值来实现的。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  </blockquote> </li><li> **短时特征分析**： <pre><code class="prism language-matlab">frameLen = 256;
hanYu_energy = shortTimeEnergy(hanYu, frameLen);
hanYu_amplitude = shortTimeAmplitude(hanYu, frameLen);
yingYu_energy = shortTimeEnergy(yingYu, frameLen);
yingYu_amplitude = shortTimeAmplitude(yingYu, frameLen);
% 实现 略....
</code></pre> 这里设置了帧长，然后计算了短时平均能量和短时平均幅度。 </li><li> **绘图**： <pre><code class="prism language-matlab">subplot(2,2,1);
% 实现 略....
% 实现 略....
% 实现 略....
% 实现 略....
% 实现 略....
subplot(2,2,4);
</code></pre> 这部分代码使用 `subplot` 和 `plot` 函数创建图表，展示两种语言中“a”音的短时能量和幅度。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  </blockquote> <img src="https://img-blog.csdnimg.cn/direct/9a8df41c752b403b92e3a7b61426511e.png" alt="在这里插入图片描述"> </li><li> **基音周期检测**： 
  <ul><li>短时自相关法:<pre><code class="prism language-matlab">[hanYu_pitch1, hanYu_acf] = pitchDetectionAutocorr(hanYu, fs1);
[yingYu_pitch1, yingYu_acf] = pitchDetectionAutocorr(yingYu, fs2);
</code></pre> </li><li>短时平均幅度差法（AMDF）:<pre><code class="prism language-matlab">[hanYu_pitch2, hanYu_amdf] = pitchDetectionAMDF(hanYu, fs1);
[yingYu_pitch2, yingYu_amdf] = pitchDetectionAMDF(yingYu, fs2);
</code></pre> </li></ul> 这两个段落分别使用自相关法和AMDF法进行基音周期的检测，并将结果保存在相应的变量中。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  </blockquote> <img src="https://img-blog.csdnimg.cn/direct/ae8cd5875f284089af159bd71460063e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/4463780e9b8f43e1888d786536756035.png" alt="在这里插入图片描述"> 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  </blockquote> </li><li> **辅助函数定义**： <pre><code class="prism language-matlab">function energy = shortTimeEnergy(signal, frameLen)
...
% 实现 略...
% 实现 略...
function [pitch, amdfCurve] = pitchDetectionAMDF(signal, fs)
...
% 实现 略...
% 实现 略...
</code></pre> 这部分定义了用于短时能量、短时幅度、自相关法基音检测和AMDF法基音检测的辅助函数。 
  <blockquote> 
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  </blockquote> </li>
>  
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  
<li>短时自相关法:<pre><code class="prism language-matlab">[hanYu_pitch1, hanYu_acf] = pitchDetectionAutocorr(hanYu, fs1);
[yingYu_pitch1, yingYu_acf] = pitchDetectionAutocorr(yingYu, fs2);
</code></pre> </li><li>短时平均幅度差法（AMDF）:<pre><code class="prism language-matlab">[hanYu_pitch2, hanYu_amdf] = pitchDetectionAMDF(hanYu, fs1);
[yingYu_pitch2, yingYu_amdf] = pitchDetectionAMDF(yingYu, fs2);
</code></pre> </li>
>  
   👉👉👉 源码获取 关注【测试开发自动化】公众号，回复 “ 声学特征分析 ” 获取。👈👈👈 
  
