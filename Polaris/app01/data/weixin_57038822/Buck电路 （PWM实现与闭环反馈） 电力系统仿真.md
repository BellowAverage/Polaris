
--- 
title:  Buck电路 （PWM实现与闭环反馈） 电力系统仿真 
tags: []
categories: [] 

---
****Buck电路 （PWM实现与闭环反馈）****

Buck电路是降压型的DC-DC变换器。

<img src="https://img-blog.csdnimg.cn/direct/07cdffecc8dc413dbf35b625d06400fc.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/f6c4d2420b8e4211bfea08c3ee8dcf62.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/73edab80c3d4431db51200dc32f54777.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/3e121c43af974fd4b0feda847a6b6272.png" alt="在这里插入图片描述"> 三角波：

<img src="https://img-blog.csdnimg.cn/direct/f5fe16df8c184966b0236b4ffe892234.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/c78857c30701437b8f4b4797a309d7a2.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/0eb6b82165a54c96bb01b55da20e0607.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b107e78c12bc40d8a30c0b13428ddc0f.png" alt="在这里插入图片描述">

闭环控制怎么实现呢？

比例积分微分控制（proportional-integral-derivative control），简称PID控制，是最早发展起来的控制策略之一，由于其算法简单、鲁棒性好和可靠性高，被广泛应用于工业过程控制，仍有90%左右的控制回路具有PID结构。

<img src="https://img-blog.csdnimg.cn/direct/8fd8c78a9edc4491ad77599f9fde91d0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/930901684e414b5182d8bd1c5246bc63.png" alt="在这里插入图片描述"> 效果不明显，所以我们要把PID值调大一点，进而看可视化。

<img src="https://img-blog.csdnimg.cn/direct/a7c9e94676e54054adde203d141719e1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/e879dcbaadb649bc903fd7b6841b37bc.png" alt="在这里插入图片描述"> 误差信号也接近0了，说明状态很好。

<img src="https://img-blog.csdnimg.cn/direct/e00e766060344727b0ca40ba037bac92.png" alt="在这里插入图片描述"> 传递函数 小信号模型创立

<img src="https://img-blog.csdnimg.cn/direct/70f17601831d4727bd63c8987fb46913.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b8a3ad3610034babb01401236014e777.png" alt="在这里插入图片描述">
