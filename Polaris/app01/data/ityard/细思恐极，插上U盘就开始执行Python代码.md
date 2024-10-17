
--- 
title:  细思恐极，插上U盘就开始执行Python代码 
tags: []
categories: [] 

---
源 / 知乎    文 / DeepWeaver

昨天在上厕所的时候突发奇想，当你把usb插进去的时候，能不能自动执行usb上的程序。查了一下，发现只有windows上可以，具体的大家也可以搜索(搜索关键词usb autorun)到。但是，如果我想，比如，当一个usb插入时，在后台自动把usb里的重要文件神不知鬼不觉地拷贝到本地或者上传到某个服务器，就需要特殊的软件辅助。

于是我心想，能不能用python写一个程序，让它在后台运行。每当有u盘插入的时候，就自动拷贝其中重要文件。

### **如何判断U盘的插入与否?**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cGhDWlBlQkxoaExaMDRFdExNNUFIbXpHMlZaUjAwelJVdDB0T092TW1OcjdjdVdyYlZpYlVKTkEvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

首先我们打开电脑终端，进入/Volumes目录，这时候插入U盘，可以发现它被挂载在了这个目录之下，也就是说，我们只要在固定时间扫描这个目录，当这个目录有新文件夹出现的时候，很可能有U盘被插入了。

我的设计是这样的，用time.sleep(3)函数，让程序保持运行状态，并且每隔三秒查看一下/Volumes/目录，如果多出来文件夹，就将其拷贝到另外的文件夹。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cGliQ1hHZnJzWEJpY1h3dnNpYzJzcWljUnRyN0pjR1pCanhsTUZRVHRGenBMSVRnT08zYThPczFUbGcvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

就像标题所示，我们真的只用了10行(其实是11行，凑个整：)完成了这个“病毒”。我们可以发现usb中的目录，在插入半分钟后全部躺在了home目录下了。

### **如何选择性的复制文件?**

刚刚我们写了一个很简易的脚本测试了一下这个想法的可行性，但是还是有问题。刚才之所以能把U盘中所有文件很快复制进去，是因为U盘中只有两三个文件，大小不超过15M。如果目标U盘中有很多电影，音乐，这些我们并不需要的文件，我们的程序就应该能跳过它们，仅仅选择一些重要的比如.docx比如.ppt文件，或者仅仅复制最近修改过的那些文件，或者排除所有大小大于5M的文件。我们可以用python做到吗?当然!

#### **os.walk 递归文件夹中所有文件**

http://www.runoob.com/python/os-walk.html

这里我放了一个别人的教程。大家可以大概了解一下，总之我大概理解是这么个东西。

还是举个例子吧。

我在某目录下创建了testwalk文件夹，里面有file123.txt三个文件，folder123三个文件夹，其中folder1中有文件file4.txt以及folder4

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cFRTUDVIbmFsTE1NNVRDYTY4bkM3ZGNreGZLM09qWnFxejJnOU1XOXlvRWlhSllZMHdjNjdVVHcvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

现在我们来测试一下

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cEtSR0FrQ3RSUGFtMFlqR3BuNlZvcUxXQllOdnR4aWFhZVBrS0xibnJiMXUyV1ExeEIxV2g2Q0EvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

root存放的是当前位置，它会把./testwalk/下所有的文件夹作为根目录，往下搜索

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cFhRSklFSHh5c29hUE1xaGNPZjh0TVl3a0hSVHl2cm9rczFKemUycE9JV2RvdTdjRlk4eGFTZy82NDA?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

#### **单独查看 dirs**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cEIxWUZkbUowYXduNFVrZHV5RFNiR2Z2aWNwODJpY0JRaWFpYU9JZHF5YjZCN2hhdnh4Umozb3NLb2cvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

#### **单独查看 files**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cEZBMlVURWZLNXVpYlZkeFNKa08xMWtQRlpZM1JRSVp3ODhrWVNmQjhuT3pNNWZQSGlheFB1SDBnLzY0MA?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

好了，我们现在需要递归usb文件夹，找到所有的file，查看大小，如果小于，比如3M，就拷贝进home，大于就舍去。

#### **shutil模块**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cFY4VTlNcmdsTUNlVk1GSDZFOUxJQ2NUUXRMbFhkWm1ZWmljc0RKd0hpYVM3SWRIUDM3MkpvRUl3LzY0MA?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

现在我们拿刚才的文件夹举例子，如果想把file1.txt拷贝到folder2：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cDl1UjRGUGpjTGJSb2VTM3M1cW5ibmtkZkR2cWJHZ24xVENOMjg3VEJLdmhFTGlhb2FPSlp4RXcvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

还有许多使用工具在shutil里面这里就不详述了。

#### **os.path.getsize()判断大小**

os.path.getsize(文件名)返回的是一个单位为byte的数值，如果用来查看文件大小，我们则需要手动写一个函数，将其换算成容易阅读的形式。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cDZnb1l2QjhkZ20xNGVUSlFvQ2VZaElFSzBNME8waWNYUE1tZEN5YWlhRzBKc3M3S1cya2NsN1NBLzY0MA?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

这里我们只要选择文件大小小于3M的即可，3M = 3 * 1024kB = 3 * 1024*1024byte

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cFlkN05iV1FKTG9IdWFvV3NaYzVmMGthUWVCSkpVUVUxeGt3VmlhdU9JSGZvc1ZTb1BvdE5wUGcvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

结合shutil.copy2就可以把选定大小的文件复制进我们的目标文件夹了

### **如何指定文件类型**

这里就需要正则表达式来帮助我们了。

正则表达式内容很多，《python核心编程》中用了整整一章来讲，所以我们也不深入了。下面是官方文档，感兴趣的可以看一下。

https://docs.python.org/2/library/re.html

如下，我们让指定文件后缀以及指定文件大小可以复制进我们的目标文件：

#### **别忘了导入 re**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cDRIVEFsTWdDcUxUTlpNSjVWZzVaQW91aWI5SzdBV2puaGlhN1h0Unc0WkFsWUVHWHcxaWIxaWNQSncvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

用更加复杂的正则表达式可以更好地指定文件类型

### **根据修改时间筛选文件**

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cDd6cXpnZGd4YzJXUGZ6S0xhOXdTU1Vkb1dhNEhoS001RmJlNWU2R3pPcDZLOHJKckJ5TDJIZy82NDA?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

这时候我在目录下创建了一个文件叫做newfile

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9IWlcwd3dGeGJRRFZxTzNoTzViRnRkVGFxWHY0bHg1cGlhNk5UOU5TWVR0REpzMnVVWWhzRkhicXhrNk9aQ3pjU1R2WXhLdTZhUWpPUWFJMjhwa2g1bXcvNjQw?x-oss-process=image/format,png" title="十行代码--用Python写一个USB病毒">

总之，对每一个文件进行修改时间的筛选可以只复制那些近期，或者特定时期修改或者添加过的文件，这个功能在特定情况下很有用。

### **总结**

其实，标题这么起只是为了吸引大家注意，这就是一个小程序，也谈不上病毒。我更想通过这个例子，展示python对于文件处理的强大能力，引发大家的学习热情。以上实现都是基于macos，linux应该一样，windows稍加修改也可以成功。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcFh1ZmlibEhVcndWT0loNFg4WWhwYXBpYU1rQk9sSE16b0ZRQm1Qd3dUWEREOG1Dd3pQWEdydUxRbEVBR1VTT3c4aWNQV0FydnRRaWFMTVEvNjQw?x-oss-process=image/format,png">

微信扫码关注，了解更多内容
