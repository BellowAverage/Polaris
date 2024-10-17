
--- 
title:  Power BI依据列中值的范围不同计算公式增加一列 
tags: []
categories: [] 

---
Power BI依据列的范围不同计算公式增加一列，在我们遇到了依据范围不同的公式计算时，就可以采用下面公式 一、增加组计算公式

```
佣金分组 = SWITCH(TRUE(),
'ry_vue clawer_zhuan'[到手价]&gt;0&amp;&amp;'ry_vue clawer_zhuan'[到手价]&lt;=475,80,
'ry_vue clawer_zhuan'[到手价]&lt;=499,20,
'ry_vue clawer_zhuan'[到手价]&lt;=999,15,
'ry_vue clawer_zhuan'[到手价]&lt;=1499,13,
'ry_vue clawer_zhuan'[到手价]&lt;=1999,11,
'ry_vue clawer_zhuan'[到手价]&gt;2499,10,
'ry_vue clawer_zhuan'[到手价]&lt;=2999,9,
'ry_vue clawer_zhuan'[到手价]&lt;=4999,7,
'ry_vue clawer_zhuan'[到手价]&lt;=6999,6,
'ry_vue clawer_zhuan'[到手价]&gt;7000,400

)

```

结果显示 <img src="https://img-blog.csdnimg.cn/342c29fd8f0d4d8bbdbc9f4a1450e474.png" alt="">

二、增加值计算公式

```
花费 = SWITCH(TRUE(),
'ry_vue clawer_zhuan'[到手价]&gt;0&amp;&amp;'ry_vue clawer_zhuan'[到手价]&lt;=475,80,
'ry_vue clawer_zhuan'[到手价]&lt;=499,'ry_vue clawer_zhuan'[到手价]*120/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=999,'ry_vue clawer_zhuan'[到手价]*115/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=1499,'ry_vue clawer_zhuan'[到手价]*113/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=1999,'ry_vue clawer_zhuan'[到手价]*111/100-15,
'ry_vue clawer_zhuan'[到手价]&gt;2499,'ry_vue clawer_zhuan'[到手价]*110/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=2999,'ry_vue clawer_zhuan'[到手价]*109/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=4999,'ry_vue clawer_zhuan'[到手价]*107/100-15,
'ry_vue clawer_zhuan'[到手价]&lt;=6999,'ry_vue clawer_zhuan'[到手价]*106/100-15,
'ry_vue clawer_zhuan'[到手价]&gt;7000,'ry_vue clawer_zhuan'[到手价]+400-15
)

```

<img src="https://img-blog.csdnimg.cn/86209337a2114f519e15766089b0ad19.png" alt="在这里插入图片描述">
