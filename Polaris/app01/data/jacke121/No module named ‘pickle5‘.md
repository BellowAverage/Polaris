
--- 
title:  No module named ‘pickle5‘ 
tags: []
categories: [] 

---


报错代码：

```
No module named 'pickle5'
```

解决方法

```
import pickle
if motionfile.split(".")[-1] == "pkl":
     pkl_data = pickle.load(open(motionfile, "rb"))
```


