
--- 
title:  python关于matplotlib的画图工具 
tags: []
categories: [] 

---
```
#绘制纽约市年均气温
#,months,nyc_temp_2022,months,nyc_temp_2024
from pylab import plot,show #调用画图和显示
nyc_temp_2021 =[53.9,56.3,56.4,58.6,57.8,54.9,67.3,56.3,56.7,57.1,67.3,56.3]
nyc_temp_2020 =[53.9,56.3,56.4,58.6,57.8,54.9,67.3,56.3,56.7,57.1,67.3,56.3]
nyc_temp_2022 =[53.3,56.4,57.4,59.6,57.3,54.4,67.4,57.3,59.7,59.3,67.3,56.3]
nyc_temp_2024 =[63.9,57.3,66.4,68.6,67.8,64.9,67.3,56.3,66.7,57.7,67.3,56.3]
months = range(1,13)
plot(months,nyc_temp_2021,months,nyc_temp_2020,months,nyc_temp_2022,months,nyc_temp_2024)

from pylab import legend #调用图例
legend([2021,2020,2022,2024])
show()

```

结果 <img src="https://img-blog.csdnimg.cn/direct/027185430e83454d94f27f37ca24ccc9.png" alt="在这里插入图片描述">
