
--- 
title:  windows11 ssd掉盘（无法访问） 
tags: []
categories: [] 

---
## 故障描述：
- 开机的时候能够正常访问SSD，然后突然IO到100%不可用- 通过任务管理器发现磁盘使用率100%，使用率却为0- 放在对应磁盘的文件根本打不开，放在对应磁盘的exe直接卡死（可能会打开目录）- 重装系统无效，升级到win11无效，任何版本windows直接无效- ssd版本是金士顿
## 故障原因1：SSD寿命到了

https://www.zhihu.com/question/600848176/answer/3026786279?utm_id=0

总结：杂牌的话品控不是很理想，在1年后会出现各种各样的问题。 包括刚写入2T数据就到寿命、100%IO占用。

只能尽量保住数据。

磁盘坏道越修越严重，需要尽快做数据转移

## 故障原因2：版本不兼容

https://blog.csdn.net/qq_44720952/article/details/125039718

https://blog.csdn.net/Fitz1318/article/details/54766795

和这两个人的说法完全一致。

解决方案：升级系统标准版到对应的控制器即可。 <img src="https://img-blog.csdnimg.cn/direct/ed64402cf03347d6a3b6d4ef6e78ef5b.png" alt="在这里插入图片描述"> 然后（可以尝试）：
- 卸载了两个控制器，然后直接重装相同的控制器。- 删除一小部分的磁盘文件
反正就是这个的问题，但是怎么恢复正常有点难。
