
--- 
title:  【python3】多进程Pipe实现数据流模型 
tags: []
categories: [] 

---
当涉及到数据流模型时，常见的方法是使用管道（Pipe）来实现进程间的通信。在数据流模型中，计算过程表示为数据流图，数据从一个节点流向另一个节点，并在节点之间进行转换和处理。

以下是一个稍微复杂一些的数据流模型示例代码：

```
from multiprocessing import Process, Pipe

def producer(conn):
    for i in range(10):
        conn.send(i)
    conn.close()

def transformer(conn_in, conn_out):
    while True:
        data = conn_in.recv()
        transformed_data = data * 2
        conn_out.send(transformed_data)

def consumer(conn):
    while True:
        data = conn.recv()
        print("Received:", data)

if __name__ == '__main__':
    producer_conn, transformer_conn = Pipe()
    transformer_conn2, consumer_conn = Pipe()

    p1 = Process(target=producer, args=(producer_conn,))
    p2 = Process(target=transformer, args=(transformer_conn, transformer_conn2))
    p3 = Process(target=consumer, args=(consumer_conn,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

```

在这个示例中，我们定义了三个函数：`producer`、`transformer` 和 `consumer`。`producer` 函数用于生成数据并将其发送到 `transformer` 进程；`transformer` 进程接收来自 `producer` 的数据，进行转换，并将转换后的数据发送给 `consumer` 进程；`consumer` 进程接收来自 `transformer` 的数据并进行处理。

通过使用 `multiprocessing` 库中的 `Pipe` 类，我们创建了多个管道来实现进程间的通信。每个管道都有一个发送端和一个接收端，它们可以在不同的进程中使用。

在主程序中，我们创建了三个进程 `p1`、`p2` 和 `p3`，分别对应生产者、转换器和消费者。这些进程通过管道进行通信，并使用 `start` 方法启动它们。最后，通过 `join` 方法等待所有进程执行完成。

当程序运行时，生产者进程将生成从 0 到 9 的整数，并将它们发送到转换器进程。转换器进程将接收这些数据并将其乘以 2，然后将转换后的数据发送给消费者进程。消费者进程将接收并打印出接收到的数据。


