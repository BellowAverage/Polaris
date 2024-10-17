
--- 
title:  Image.fromarray的用法（实现array到image的转换） 
tags: []
categories: [] 

---
#### 一、Image.fromarray的作用：

简而言之，就是实现`array`到`image`的转换。

#### 二、PIL中的Image和中的数组array相互转换：

1. PIL image转换成array

```
img = np.asarray(image)

```

需要注意的是，如果出现`read-only`错误，并不是转换的错误，一般是你读取的图片的时候，默认选择的是"r","rb"模式有关。

修正的办法:　手动修改图片的读取状态

```
img.flags.writeable = True  # 将数组改为读写模式`

```

2. array转换成image

```
Image.fromarray(np.uint8(img))
```

**np**.**astype** **uint8**之后发生了什么

uint8变成float没什么好说的就是添加了.0

```
b = np.arange(10).astype('float32')
c = -b
b[9] = 0.7

print('b',b)
print('c',c)
print(b.astype('uint8'))
print(c.astype('uint8'))

输出
b [0.  1.  2.  3.  4.  5.  6.  7.  8.  0.7]
c [-0. -1. -2. -3. -4. -5. -6. -7. -8. -9.]
[0 1 2 3 4 5 6 7 8 0]
[  0 255 254 253 252 251 250 249 248 247]


总结 小数部分直接截去，0-255之间的整数保留  
```
