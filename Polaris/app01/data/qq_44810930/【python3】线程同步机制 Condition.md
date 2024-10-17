
--- 
title:  【python3】线程同步机制 Condition 
tags: []
categories: [] 

---
`threading.Condition` 是 Python 中用于线程同步的一种机制，它提供了一个条件变量，允许一个或多个线程等待某个条件变为真时再继续执行。`Condition` 对象内部包含一个锁对象，线程可以在调用 `wait()` 方法时释放这个锁，并在条件满足时重新获取锁以继续执行。

下面是 `threading.Condition` 的几个常用方法：
- `acquire()`: 获取底层锁。- `release()`: 释放底层锁。- `wait(timeout=None)`: 线程等待直到被通知或超时。在调用这个方法时，线程会释放底层锁，进入等待状态。- `notify(n=1)`: 通知一个等待该条件的线程，n 表示通知的数量，默认为1。- `notify_all()`: 通知所有等待该条件的线程。
下面是一个简单的示例展示如何使用 `threading.Condition`：

```
import threading
import time

# 共享资源，初始为空列表
shared_resource = []
# 创建一个 Condition 对象
condition = threading.Condition()

def producer():
    global shared_resource
    for i in range(5):
        with condition:
            # 获取底层锁并添加数据到共享资源
            shared_resource.append(i)
            print(f"Produced: {<!-- -->i}")
            # 通知等待该条件的线程
            condition.notify()
            # 等待其他线程通知并释放底层锁
            condition.wait()
            time.sleep(1)  # 为了更好地观察输出结果，等待一秒钟

def consumer():
    global shared_resource
    for i in range(5):
        with condition:
            # 检查共享资源是否为空，为空则等待生产者生产数据
            while not shared_resource:
                condition.wait()
            # 从共享资源中取出数据并打印
            data = shared_resource.pop(0)
            print(f"Consumed: {<!-- -->data}")
            # 通知生产者可以继续生产
            condition.notify()
            time.sleep(1)  # 等待一秒钟

if __name__ == '__main__':
    # 创建生产者和消费者线程
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # 启动线程
    producer_thread.start()
    consumer_thread.start()

    # 等待线程结束
    producer_thread.join()
    consumer_thread.join()


```

在上面的示例中，生产者线程负责向 `shared_resource` 中生产数据，消费者线程负责从 `shared_resource` 中消费数据。通过 `threading.Condition` 实现了生产者和消费者之间的同步。生产者在生产数据后通知消费者，消费者在消费数据后通知生产者，从而实现了线程间的协作。
