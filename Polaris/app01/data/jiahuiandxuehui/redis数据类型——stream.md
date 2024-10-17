
--- 
title:  redis数据类型——stream 
tags: []
categories: [] 

---
Redis Stream（Redis流）是Redis数据库的一种数据结构，用于实时数据流的处理。它是在Redis 5.0版本中引入的，用于解决消息队列和日志处理等实时数据流场景的需求。Redis Stream提供了一种非常灵活和高效的方式来处理时间序列数据，允许应用程序实时地读取和写入事件。

以下是Redis Stream的一些主要特点和用法：
1. 事件驱动的数据结构：Redis Stream是一个事件日志，其中包含时间戳和消息内容。每个消息都有一个唯一的ID，消息是按照时间顺序存储的。1. 发布与订阅：你可以使用XADD命令将消息发布到流中，同时使用XREAD或XREADGROUP命令来订阅和读取流中的消息。这使得Redis Stream适用于实时消息传递。1. 消费者组：Redis Stream支持消费者组（Consumer Groups），多个消费者可以以组的形式消费流中的消息。这允许消息负载均衡和故障恢复。1. 消息确认：消费者可以确认已处理的消息，这有助于确保消息被正确处理，避免消息的重复处理。1. 阻塞读取：XREAD和XREADGROUP命令支持阻塞模式，允许消费者等待新消息并立即处理它们。1. 消费者自动分区：消费者组可以自动分区消息以平衡负载，这对高吞吐量应用程序非常有用。1. 消息修剪：你可以为流启用消息修剪（Trimming），以限制流的大小，自动删除旧的消息。
Redis Stream通常用于以下应用场景：

>  
 消息队列：Redis Stream可用作轻量级的消息队列，允许多个生产者将消息发布到流中，而多个消费者以分组的形式订阅和处理消息。 
 实时日志处理：Redis Stream可用于实时监控和处理日志数据，以快速分析和响应事件。 
 数据流处理：适用于流式数据分析和处理，例如实时指标计算和报警。 
 协同编辑：在协作应用程序中，多个用户可以通过Redis Stream实时共享和同步数据。 


## 常用命令

XADD：将一个消息添加到指定的流中。

```
XADD mystream * field1 value1 field2 value2 ...


```

XREAD：读取一个或多个流中的消息。

```
XREAD COUNT count STREAMS stream1 stream2 ... ID id

```

XREADGROUP：读取一个或多个流中的消息，支持消费者组。

```
XREADGROUP GROUP groupname consumername COUNT count STREAMS stream1 stream2 ... ID id

```

XGROUP CREATE：创建一个新的消费者组。

```
XGROUP CREATE stream groupname id [MKSTREAM]

```

XGROUP SETID：设置消费者组的消费位置。

```
XGROUP SETID stream groupname id

```

XGROUP DESTROY：销毁一个消费者组。

```
XGROUP DESTROY stream groupname

```

XACK：确认一个或多个消息已经被消费。

```
XACK stream groupname id [id ...]

```

XLEN：获取流的长度，即其中包含的消息数量。

```
XLEN stream

```

XTRIM：修剪流中的消息，保留指定数量的消息。

```
XTRIM stream MAXLEN [~] count

```

XRANGE：获取指定范围内的消息。

```
XRANGE stream start end [COUNT count]

```

XREVRANGE：获取指定范围内的消息，反向顺序。

```
XREVRANGE stream end start [COUNT count]

```

XREAD：从一个或多个流中读取消息，支持阻塞模式。

```
XREAD BLOCK milliseconds STREAMS stream1 stream2 ... [COUNT count]

```

XDEL：删除指定的消息。

```
XDEL stream id [id ...]

```

XINFO：获取关于流的信息。

```
XINFO STREAM stream [FULL [COUNT count]]

```

XINFO：获取关于消费者组的信息。

```
XINFO GROUPS stream

```

XINFO：获取消费者组的消费者列表。

```
XINFO CONSUMERS stream groupname

```
