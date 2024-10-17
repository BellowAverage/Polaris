
--- 
title:  实战案例 Python批量识别银行卡号码并且写入Excel，初学者也可以轻松使用~ 
tags: []
categories: [] 

---
<img alt="" src="https://img-blog.csdnimg.cn/img_convert/a430e90b5660b82a9c024e74b9ee39cd.webp?x-oss-process=image/format,png">

大家好，这里是恶霸

今天我们继续学习Python自动化办公：每次有新员工入职，都要收集大量的工资卡信息，并且生成Excel文档，能不能用Python**准确、快速**地解决呢？

今天我们就来学习一下，如何**用1行代码，自动识别银行卡信息并且自动生成Excel文件**~

<img alt="" src="https://img-blog.csdnimg.cn/img_convert/189ed66da49906fa3f5bcdc9f8ff95e5.webp?x-oss-process=image/format,png">

### 第一步：识别一张银行卡

识别银行卡的代码最简单，只需要1行腾讯云AI的第三方库`potencent`的代码，如下所示。左右滑动，查看全部。👇

```
# pip install potencent
import potencent

# 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url
# 如果2个都填，则只用在线图片
res = potencent.ocr.BankCardOCR(
            img_path=r'C:\Users\程序员晚枫的文件夹\银行卡图片',
            img_url='https://python-office-13006153
```
