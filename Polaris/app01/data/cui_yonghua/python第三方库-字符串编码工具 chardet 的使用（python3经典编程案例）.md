
--- 
title:  python第三方库-字符串编码工具 chardet 的使用（python3经典编程案例） 
tags: []
categories: [] 

---
#### 一. chardet介绍

chardet这个第三方库的使用非常容易，chardet支持检测中文、日文、韩文等多种语言。

字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。

对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。

官方文档：

github地址：

安装：`pip3 install chardet`

截至目前，可以检测的编码：
- ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)- Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)- EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)- EUC-KR, ISO-2022-KR, Johab (Korean)- KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)- ISO-8859-5, windows-1251 (Bulgarian)- ISO-8859-1, windows-1252 (Western European languages)- ISO-8859-7, windows-1253 (Greek)- ISO-8859-8, windows-1255 (Visual and Logical Hebrew)- TIS-620 (Thai)
#### 二. 使用chardet

##### 2.1 检测编码是ascii

当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：

```
import chardet
print(chardet.detect(b'Hello, world!'))

# 运行结果
# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
{<!-- -->'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

```

##### 2.2 检测GBK编码：

```
import chardet
data = '真相只有一个'.encode('gbk')
print(chardet.detect(data))

# 运行结果
# 检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是99%，
# language字段指出的语言是'Chinese'。
{<!-- -->'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}

```

##### 2.3 对UTF-8编码进行检测

```
import chardet
data = '真相只有一个'.encode('utf-8')
print(chardet.detect(data))

# 运行结果
{<!-- -->'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

```

##### 2.4 检测日文

```
import chardet
data = '真実はいつもひとつ'.encode('euc-jp')
print(chardet.detect(data))

# 运行结果
{<!-- -->'encoding': 'EUC-JP', 'confidence': 1.0, 'language': 'Japanese'}

```

可见，用chardet检测编码，非常简单。获取到编码后，再转换为str，就可以方便后续处理。
