
--- 
title:  Python 批量合并 Excel 
tags: []
categories: [] 

---
经常使用 Excel 的人可能会遇到合并 Excel 文件的情况，如果需要合并的文件比较少，怎么搞都无所谓了，但要是需要合并的文件比较多，自己一顿 CV 操作也是比较耗时的，这时我们就可以考虑利用 Python 来帮我们合并了。

比如我们有很多很多个 Excel 文件需要合并，每个 Excel 文件格式都是相同的，我们合并文件只是对文件中数据的直接合并，这时利用 Python 来帮我们合并就事半功倍了，下面通过示例来做进一步了解。

需要合并的 Excel 如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb0w4OUdaeGNzYmQzNFBGOGExbmhpYUJBaWNWMUFnR0l1TXZ1aGxNRlVkR2NyZmdQMm5od0tDOGp4aWFGNmdROFg5TDRDajZSVFdTejdOQS82NDA?x-oss-process=image/format,png">

代码实现如下：

```
import os, pandas as pd

# 获取文件夹下文件全路径名
def get_files(path):
    fs = []
    for root, dirs, files in os.walk(path):
        for file in files:
            fs.append(os.path.join(root, file))
    return fs

# 合并文件
def merge():
    files = get_files('D:/excels')
    arr = []
    for i in files:
      arr.append(pd.read_excel(i))
    writer = pd.ExcelWriter('D:/excels/merge.xlsx')
    pd.concat(arr).to_excel(writer, 'Sheet1', index=False)
    writer.save()

if __name__ == '__main__':
    merge()

```

合并后的 Excel 文件如下：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb0w4OUdaeGNzYmQzNFBGOGExbmhpYUJPOU81aGhxamlhSExjOEs5VHlNSEhXdGx0OWtuYnh6c2liMHVlMHB4WWZvRXZEdnRDdFNsTk1zQS82NDA?x-oss-process=image/format,png">

当然了，你可能会想到这只是简单的合并，如果是是复杂的 Excel 合并呢？比如需要合并的 Excel 文件格式不同，最终合并的 Excel 文件格式也是自定义的，对于这种情况，如果对你而言是一个多次重复的工作，可以考虑利用 Python 进行编码实现；反之，则并一定要编码来实现合并，因为你用编码来实现合并可能比手动合并花费的时间更多。<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
