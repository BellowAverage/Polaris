
--- 
title:  python中时间模块datetime总结 
tags: []
categories: [] 

---
python关于时间模块，做一下总结

**1、常用参数：**

```
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）

```

**2、获取系统当前时间**

```
#获取系统当前时间
now=datetime.datetime.now()
print(now,type(now))


```

**3、 时间转为字符串并格式化**

```
strtime = now.strftime('%Y-%m-%d %H:%M:%S')
print(strtime, type(strtime))

```

**4、时间差格式化天数和秒**

```
#间隔天数
deltaday = (date2 - date1).days
print("间隔天数 ", deltaday)
#间隔秒数
deltasecond = (date2 - date1).seconds
print("间隔秒数 ", deltasecond)

```

**5、当期时间加减天数 使用timedelta**

```
#当前时间减去时间间隔
repair_time = now + datetime.timedelta(days=-2)
#格式化输出
print(repair_time)

```

**6、字符串转时间**

```
date1 = datetime.datetime.strptime('2018-12-01 01:32:25', '%Y-%m-%d %H:%M:%S')
print(date1)
#或者

date2 = datetime.datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S')
print(date2)

```

**7、时间格式转换**

```
# 将'2021/3/30' 转成'20210330'
s = '2021/3/30'
s = datetime.datetime.strptime(s, '%Y/%m/%d').date()
print(str(s).replace('-', ''))


# 将'2021-04-01T00:00:00' 转成 '2021-04-01'
a ='2021-04-01T00:00:00'
a = datetime.datetime.strptime(a, '%Y-%m-%dT%H:%M:%S').date()
print(str(a))

```
