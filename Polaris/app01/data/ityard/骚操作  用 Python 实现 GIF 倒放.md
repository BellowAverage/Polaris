
--- 
title:  骚操作 | 用 Python 实现 GIF 倒放 
tags: []
categories: [] 

---
### 简介 

提到 GIF，大家应该都比较熟悉，它与 JPG、PNG 等文件格式一样，可用于制作静态图像，但是 GIF 格式还具有一项独有技能：可以用于创建动态图像。

不知大家有没有想过：如果将 GIF 倒放会是一种怎么样的景象？本文我们就用 Python 来实现一下 GIF 倒放。

### 实现 

我们可以将 GIF 看作是由若干张静态图片组成的，要实现倒放，我们只需要将 GIF 分解成一张张静态图片，然后再将这些静态图片倒序合成为 GIF 即可。

倒放的实现需要用到 Pillow 模块，安装使用 `pip install pillow` 即可，代码的实现也比较简单，如下所示：

```
# 读取 GIF 
im = Image.open("1.gif")
# GIF 图片流的迭代器
iter = ImageSequence.Iterator(im)
index = 1
# 遍历图片流的每一帧 
for frame in iter:
    print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
    frame.save("./images/img%d.png" % index)
    index += 1
# 把 GIF 拆分为图片流 
imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
# 图片流反序
imgs.reverse()
# 将反序后的所有帧图像保存下来
imgs[0].save("reverse.gif", save_all=True, append_images=imgs[1:])

```

最后，我们来一起看一下实现效果。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcno3QlJod0RUb0hEbm8zZVRpY241Q3pUcHRNMzFUUHVTcnNCWnhBZGVxa1d4cENGZGY5QWRUTjh3OXNTbGlheDQ4Szd2MEFOSHFnSmNRLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcno3QlJod0RUb0hEbm8zZVRpY241Q3o5SG9WZk1JenhJdGhKNVZxRmtraWNPUkFrbGdoaWFkd3ppYUNDSWhUZ2ljdHlGWmlhREp5NE5ES01wZy82NDA?x-oss-process=image/format,png">

源码在公号后台回复 **200829** 获取。 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9RQjZHNFpvRTE4NGliejlNc2N3YXE5OHcwNXVHQWljMXh0UXZqNWhzTEQ1eFdmcjlIYlhsTDVSTnFRcU1wcnVnNlhqRDdtSTRVY1F2Y3U2NEdHZTI3VDdBLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb24walFiZjlpYVdGcTBMaWJaSVQ0WXJCNGlhd0ZmZE5lQjFJcks0eXhrWVplbnFvWWY2dHc3dElpY0EyMUxNWEFSVzN6bkk5ajU0NmliMzFRLzY0MA?x-oss-process=image/format,png">

分享或在看是对我最大的支持 
