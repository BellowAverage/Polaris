
--- 
title:  如何用Python一键修改上万个文件名 
tags: []
categories: [] 

---
<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcTIyWFdpY3diaDlXTGtsazJYNTF6dkdEWTN4UmtpY0NzT2huSlQ5V2xDejFvbnZ2c2RXd0JRb0IwaWNaZkNRaDl5SVJvaWM0MUlYd05XRVEvNjQw?x-oss-process=image/format,png">

## 头疼的修改文件名，我是傻了

同事问我会不会改目录下的文件名，我大叫一声：你傻呀，你不会右键重命名呀呀，或者按 <mark>F2</mark>快捷键，但是当我解压完同事的目录后，人都傻了，自己看图哈！！

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcTIyWFdpY3diaDlXTGtsazJYNTF6dkc1V205UmJiS2g1NllMNFExa0tpYkpyaWJtVDk0aWJUUk8wV1JuSzBER09QSDJGcHh3dmlhUnZmZzFBLzY0MA?x-oss-process=image/format,png">

偷偷告诉你，这样的文件有一大堆，如果你右键估计一天才能搞定，顿时我就不敢出声了。

先看<mark>同事的需求是什么</mark>：帮他去掉类似 **[图灵程序设计丛书].**的词，只留下书名

看到这，请问小伙伴们你是怎么解决的，欢迎留言一起吐槽，哈哈哈哈哈哈。

### 茅塞顿开，秒解决同事问题

在我思考如何解决同事这个问题时，我的脑海中突然<mark>灵光一闪</mark>，之前写过一键修改图片大小的程序，那我为何不也写个程序直接一键修改文件名呢！！！说干就干

<mark></mark><mark>考虑到时效性，我用了Python来写这个小程序</mark>，上代码：

```
import os
import re
import time


"""对指定目录下的所有文件进行有选择的修改名称"""
def ReFileName(dirPath,pattern):
    """
    :param dirPath: 文件夹路径
    :param pattern: 正则匹配模式
    :return:
    """
    # 对目录下的文件进行遍历
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
            # 用正则匹配，去掉不需要的词
            newName = re.sub(pattern, "", file)
            # 设置新文件名
            newFilename = file.replace(file, newName)
            # 重命名
            os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newFilename))
    print("文件名已统一修改成功")




if __name__ == '__main__':
    timeStart = time.time()
    dirPath = r"F:\test"
    pattern = re.compile(r'\[{1}(.+)]\.')
    ReFileName(dirPath,pattern)
    timeEnd = time.time()
    print("程序走了%d秒"%(timeEnd-timeStart))

```

代码简要说明一下：

>  
  1. 因为这里需求只是简单的修改文件名，所以小伙伴们<mark>千万不要用open（）……这种方法</mark>，虽然它也是可以的，但是因为文件太多，读写太慢，时效极低。2. 还有需要替换或者提取的文件名，不仅限于图中所示，你可以<mark>灵活运用正则表达式</mark>来达到自己的需求。 
 

看效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcTIyWFdpY3diaDlXTGtsazJYNTF6dkd5V0hvTkh5UmdmZzdWeFIxeVg4QkJZYUdKbXlwWXc1cUxKNklaWFZoTW04a1pnOWliVXRXTndBLzY0MA?x-oss-process=image/format,png">

再看程序运行时间：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9VTGliSGdYSXQzanlSRXRTNjRZT0RKamR0a1UxSHU5STg5MWljc1J5cm9LMHluWmVEdDBySWVpY0FXNzNiUGZLaWJJOGU5SG1JekNWRjhpY0oySmhYWXdCbjdnLzY0MA?x-oss-process=image/format,png">

这里再分享一个干货给小伙伴们哈！！python获取当前目录下的一些信息。

```
"""获取当前目录下的信息"""
def ReFileName1(dirPath):
    for root, dirs, files in os.walk(dirPath):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件

```

好了，此篇文章就分享到这里咯，<mark>看到这还不留个赞，有点说不过去了吧！！</mark> 哈哈~

>  
  作者：放牛娃学编程 
  版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。  
  本文链接： 
  https://blog.csdn.net/qiukui111/article/details/106160745 
 
