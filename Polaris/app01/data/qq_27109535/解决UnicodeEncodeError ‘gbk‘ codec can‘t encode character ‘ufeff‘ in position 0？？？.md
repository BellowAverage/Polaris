
--- 
title:  解决UnicodeEncodeError: ‘gbk‘ codec can‘t encode character ‘\ufeff‘ in position 0？？？ 
tags: []
categories: [] 

---
解决UnicodeEncodeError: ‘gbk’ codec can’t encode character ‘\ufeff’ in position 0: illegal multibyte sequence 在代码with open或open中添加编码

```
encoding='utf-8-sig'

```
