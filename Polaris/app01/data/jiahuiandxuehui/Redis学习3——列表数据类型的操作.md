
--- 
title:  Redis学习3——列表数据类型的操作 
tags: []
categories: [] 

---
## List

<img src="https://img-blog.csdnimg.cn/6b2576af907945ba99dc708baa42c92a.png" alt="在这里插入图片描述">

### 数据结构

<img src="https://img-blog.csdnimg.cn/9f09ac4cb5044e648140b4763c76bc74.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/36cd60d797684c09bf4d23a19be53a5a.png" alt="在这里插入图片描述">

### 常用操作

```
LPUSH key value [value ...]：

描述：将一个或多个值插入到列表头部。
示例：LPUSH mylist "Hello" "World"

```

```
RPUSH key value [value ...]：

描述：将一个或多个值插入到列表尾部。
示例：RPUSH mylist "Hello" "Redis"

```

```
LPOP key：

描述：移除并返回列表的头部元素。
示例：LPOP mylist

```

```
RPOP key：

描述：移除并返回列表的尾部元素。
示例：RPOP mylist

```

```
LINDEX key index：

描述：获取列表指定索引位置的元素。
示例：LINDEX mylist 2 会返回列表中索引为 2 的元素。

```

```
LRANGE key start stop：

描述：获取列表指定范围内的所有元素。
示例：LRANGE mylist 0 2 会返回列表中索引从 0 到 2 的元素。

```

```
LLEN key：

描述：获取列表的长度。
示例：LLEN mylist 会返回列表的长度。

```

```
LREM key count value：

描述：从列表中移除指定个数的元素，该元素与给定的值相等。
示例：LREM mylist 2 "Hello" 会从列表中移除前两个值为 "Hello" 的元素。

```

```
LSET key index value：

描述：设置列表指定索引位置的元素的值。
示例：LSET mylist 1 "NewValue" 会将列表中索引为 1 的元素设置为 "NewValue"。

```

```
LTRIM key start stop：

描述：保留列表指定范围内的元素，其他的元素都将被删除。
示例：LTRIM mylist 0 2 会保留列表中索引从 0 到 2 的元素。

```

```
BLPOP key1 [key2 ...] timeout 和 BRPOP key1 [key2 ...] timeout：

描述：类似于 LPOP 和 RPOP，但是会在列表为空时阻塞并等待直到新元素出现或超时。

```

```
BRPOPLPUSH source destination timeout：

描述：从 source 列表尾部弹出一个元素并将其推入 destination 列表头部，如果 source 列表为空则会阻塞等待新元素出现或超时。

```

```
RPUSHX key value 和 LPUSHX key value：

描述：将值插入到已存在的列表的尾部（RPUSHX）或头部（LPUSHX）。

```

```
LINSERT key BEFORE|AFTER pivot value：

描述：在列表中指定元素的前面或后面插入一个新元素。
LPOP/RPOP/BRPOP/BRPOPLPUSH 操作的超时机制允许 Redis 在列表为空时阻塞等待，直到新元素出现或者超时。

```
