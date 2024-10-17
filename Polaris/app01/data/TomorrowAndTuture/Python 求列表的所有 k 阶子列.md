
--- 
title:  Python 求列表的所有 k 阶子列 
tags: []
categories: [] 

---
### 求所有 k 阶子列

这儿的 **k 阶子列** 和线性代数里边矩阵的** k 阶子式** 差不多，子列个数也和组合的公式相符，所以我就不啰嗦了。

<img alt="\mathbb{C}_{n}^{k} = \frac{n!}{k!*(n-k)!}" class="mathcode" src="https://latex.csdn.net/eq?%5Cmathbb%7BC%7D_%7Bn%7D%5E%7Bk%7D%20%3D%20%5Cfrac%7Bn%21%7D%7Bk%21*%28n-k%29%21%7D">

```
import itertools

input_list = [1, 2, 4, 3, 5]
n = len(input_list)
k = 3
for i in range(1, n + 1):
    i_subsequence = itertools.combinations(input_list, i)
    if i == k:
        k_subsequence = list(i_subsequence)
        print(k_subsequence)

```

```
[(1, 2, 4), (1, 2, 3), (1, 2, 5), (1, 4, 3), (1, 4, 5), (1, 3, 5), (2, 4, 3), (2, 4, 5), (2, 3, 5), (4, 3, 5)]
```

### 求最具竞争力的 k 阶子列

所谓最具竞争力，就是在相同位置上，对应的数更小，则更具竞争力。比如 (1, 2, 3) 比 (1, 2, 4) 更具竞争力。

```
import itertools

input_list = [1, 2, 4, 3, 5]
n = len(input_list)
k = 3
k_subsequence = list(itertools.combinations(input_list, k))
k_subsequence.sort()
print(k_subsequence[0])

```

```
(1, 2, 3)
```


