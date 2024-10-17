
--- 
title:  用python检测两个文本文件的相似性 
tags: []
categories: [] 

---
很多时候我们需要来检查两文件的相似性，到底存在着多少的雷同，或许以下的这个脚本文件可以派得上用场

```
from difflib import SequenceMatcher

def file_similarity_checker(f1, f2):
    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
        f1_data = file1.read()
        f2_data = file2.read()
        checking = SequenceMatcher(None, f1_data, f2_data).ratio()
        print(f"These files are {<!-- -->checking*100} % similar")
        
file_1 = "路径1"
file_2 = "路径2"
file_similarity_checker(file_1, file_2)

```
