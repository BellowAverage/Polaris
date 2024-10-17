
--- 
title:  游戏CE修改器精确数值扫描 
tags: []
categories: [] 

---
游戏CE修改器需要将100这个数值修改为1000则本关就算通过，看下面具体的步骤

1.首先游戏规则是每次我们点击`打我`按钮则健康值则会减一,我们首先搜索这个`100`看能不能找到些什么

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/6f1fb67fa071a8760009c264df4fa0d6.png">

现在开始搜索精确数值 `100` 数值中`输入100` 点击 ，`首次扫描，` 按钮，如图

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/597c25f57e47afcc4913319cbec71e6d.png">

默认情况下一般游戏就是4字节，这里不需要改动`扫描类型和数值类型`，默认就好了.

这次扫描我们得到 35 个结果，里面肯定有我们要找的那个血值，不过好像太多了,没关系继续往下看.

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d9e7627cec08a37eb8ce3506f806d814.png">

关键一步：为了找到更加精确的数据，我们回到 Tutorial 点击 `打我` 按钮，此时血值已有变化了：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/b52bd1512ef7731fb8176c6b03ab92d8.png">

我们再输入 `95` 点击 `再次扫描` 按钮 结果只剩1个（这就是我们要找的），我们双击此地址将其添加到地址栏：

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/d4894008e1fbe0954a3b24cb272c3c27.png">

此时地址栏里面只有1个结果了，这个就是我们要找的内存地址，双击将其加入到地址栏

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/f1afe847d386bfb6b57f118225547d46.png">

在数值95上面双击，并修改把 95 改成 1000 点击`确定`按钮,此时通关.

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a929683f303043990655b1acccdffddd.png">

此时回到Tutorial-i386.exe程序，会发现教程的 `下一步` 按钮变成可用,再次点击打我按钮，数值变大了，继续点击下一步进入第三关
