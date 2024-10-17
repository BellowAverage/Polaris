
--- 
title:  ZMQ特点及消息模式 
tags: []
categories: [] 

---
### ZMQ特点

普通的socket是端对端的关系，ZMQ是N:M的关系，socket的连接需要显式地建立连接，销毁连接，选择协议(TCP/UDP)和错误处理，ZMQ屏蔽了这些细节，像是一个封装了的socket库，让网络编程变得更简单。ZMQ不光用于主机与主机之间的socket通信，还可以是线程和进程之间的通信。ZMQ提供的套接字可以在多种协议中传输消息，线程间，进程间，TCP等。可以使用套接字创建多种消息模式，如‘请求-应答模式’，‘发布-订阅模式’，‘分布式模式’等。

组件来去自如，ZMQ会负责自动重连，服务端和客户端可以随意的退出网络。tcp的话，必须先服务端启动，再启动客户端，否则会报错。
1. ZMQ会在必要的情况下将消息放入队列中保存，一旦建立了连接就开始发送。1. ZMQ有阈值机制，当队列满的时候，可以自动阻塞发送者，或者丢弃部分消息。1. ZMQ可以使用不同的通信协议进行连接，TCP，进程间，线程间。1. ZMQ提供了多种模式进行消息路由。如请求-应答模式，发布-订阅模式等，这些模式可以用来搭建网络拓扑结构。1. ZMQ会在后台线程异步的处理I/O操作，他使用一种不会死锁的数据结构来存储消息。
### ZMQ消息模式

#### **Reuqest-Reply(请求-应答模式)**
1. 使用Request-Reply模式，需要遵循一定的规律。1. 客户端必要先发送消息，在接收消息；服务端必须先进行接收客户端发送过来的消息，在发送应答给客户端，如此循环1. 服务端和客户端谁先启动，效果都是一样的。1. 服务端在收到消息之前，会一直阻塞，等待客户端连上来。
server.py

```
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count = 0

# 必须要先接收消息，然后再应答
if __name__ == '__main__':
    print('zmq server start....')
    while True:
        message = socket.recv().decode("UTF-8")
        count += 1
        print(f'received request. message:{message}; count:{count}')
        time.sleep(1)
        socket.send_string("world!")

```

client.py

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# 客户端必须要先发送消息，然后在接收消息
if __name__ == '__main__':
    print('zmq client start....')
    for i in range(1, 10):
        socket.send_string("hello")
        message = socket.recv().decode("UTF-8")
        print(f'received response. message:{message}')

```

常用数据发送和接收：

```
# 发送数据
socket.send_json(data)                      # data 会被json序列化后进行传输 (json.dumps)
socket.send_string(data, encoding="utf-8")  # data为unicode字符串，会进行编码成子节再传输
socket.send_pyobj(obj)                      # obj为python对象，采用pickle进行序列化后传输
socket.send_multipart(msg_parts)            # msg_parts, 发送多条消息组成的迭代器序列，每条消息是子节类型，
                                            # 如[b"message1", b"message2", b"message2"]

# 接收数据
socket.recv_json()
socket.recv_string()
socket.recv_pyobj()
socket.recv_multipart()

```

#### **Publisher-Subscriber(发布-订阅模式)**

Publisher-Subscriber模式，消息是单向流动的，发布者只能发布消息，不能接受消息；订阅者只能接受消息，不能发送消息（可参考 Redis 的发布和订阅方式）。服务端发布消息的过程中，如果有订阅者退出，不影响发布者继续发布消息，当订阅者再次连接上来，收到的消息是后来发布的消息。比较晚加入的订阅者，或者中途离开的订阅者，必然会丢掉一部分信息，如果发布者停止，所有的订阅者会阻塞，等发布者再次上线的时候回继续接受消息。

"慢连接": 我们不知道订阅者是何时开始接受消息的，就算启动"订阅者"，再启动"发布者", "订阅者"还是会缺失一部分的消息，因为建立连接是需要时间的，虽然时间很短，但不是零。ZMQ在后台是进行异步的IO传输，在建立TCP连接的短时间段内，ZMQ就可以发送很多消息了。有种简单的方法来同步"发布者" 和"订阅者", 通过sleep让发布者延迟发布消息，等连接建立完成后再进行发送。

publisher.py

```
import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

if __name__ == '__main__':
    print("发布者启动.....")
    for i in range(1000):
        time.sleep(0.1)
        temperature = random.randint(-10, 40)
        message = f"我是publisher, 这是我发布给你们的第{i+1}个消息！今日温度{temperature}"
        socket.send_string(message)

```

subscriber.py

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

# 客户端需要设定一个过滤，否则收不到任何信息
socket.setsockopt_string(zmq.SUBSCRIBE, '')

if __name__ == '__main__':
    print('订阅者一号启动....')
    while True:
        message = socket.recv_string()
        print(f"（subscriber1）接收到'发布者'发送的消息：{message}")

```

#### **Push-Pull(平行管道模式/分布式处理)**

**Ventilator**：任务发布器会生成大量可以并行运算的任务。

**Worker**：有一组worker会处理这些任务。

**Sink：**结果接收器会在末端接收所有的Worker的处理结果，进行汇总。

Worker上游和"任务发布器"相连，下游和"结果接收器"相连，"任务发布器" 和 "结果接收器"是这个网路结构中比较稳定的部分，由他们绑定至端点

Worker只是连接两个端点，需要等Worker全部启动后，再进行任务分发。Socket的连接会消耗一定时间(慢连接), 如果不进行同步的话，第一个Worker启动，会一下子接收很多任务。

"任务分发器" 会向Worker均匀的分发任务(负载均衡机制)

"结果接收器" 会均匀地从Worker处收集消息(公平队列机制)

 ventilator.py

```
import zmq
import random

raw_input = input
context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

if __name__ == '__main__':
    # 同步操作
    print("Press Enter when the workers are ready: ")
    _ = raw_input()
    print("Sending tasks to workers…")

    sink.send_string('0')

    # 发送十个任务
    total_msec = 0
    for task_nbr in range(10):
        # 每个任务耗时为N
        workload = random.randint(1, 5)
        total_msec += workload

        sender.send_string(f"{workload}")

    print("10个任务的总工作量: %s 秒" % total_msec)

```

```
Sending tasks to workers…
10个任务的总工作量: 25 秒
```

 worker1.py

```
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

if __name__ == '__main__':
    while True:
        s = receiver.recv().decode("UTF-8")
        print(f'work1 接收到一个任务... 需要{s}秒')

        # Do the work
        time.sleep(int(s))

        # Send results to sink
        sender.send_string(f'work1 完成一个任务，耗时{s}秒')

```

```
work1 接收到一个任务... 需要2秒
work1 接收到一个任务... 需要1秒
work1 接收到一个任务... 需要3秒
work1 接收到一个任务... 需要5秒
work1 接收到一个任务... 需要3秒
```

worker2.py

```
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

if __name__ == '__main__':
    while True:
        s = receiver.recv().decode("UTF-8")
        print(f'work2 接收到一个任务... 需要{s}秒')

        # Do the work
        time.sleep(int(s))

        # Send results to sink
        sender.send_string(f'work2 完成一个任务，耗时{s}秒')

```

```
work2 接收到一个任务... 需要3秒
work2 接收到一个任务... 需要2秒
work2 接收到一个任务... 需要3秒
work2 接收到一个任务... 需要1秒
work2 接收到一个任务... 需要2秒
```

 sink.py

```
import time
import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

if __name__ == '__main__':
    s = receiver.recv()
    print('开始接收处理结果.....')

    # 计时，所有任务处理完一共需要多久
    start_time = time.time()

    # 接受十个任务的处理结果
    for task_nbr in range(10):
        s = receiver.recv_string()
        print(s)

    end_time = time.time()
    print("2个worker同时工作，耗时: %d 秒" % (end_time-start_time))
```

```
开始接收处理结果.....
work1 完成一个任务，耗时2秒
work2 完成一个任务，耗时3秒
work1 完成一个任务，耗时1秒
work2 完成一个任务，耗时2秒
work1 完成一个任务，耗时3秒
work2 完成一个任务，耗时3秒
work2 完成一个任务，耗时1秒
work1 完成一个任务，耗时5秒
work2 完成一个任务，耗时2秒
work1 完成一个任务，耗时3秒
2个worker同时工作，耗时: 14 秒
```

### ZMQ超时重试

server.py

```
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count = 0

# 必须要先接收消息，然后再应答
if __name__ == '__main__':
    print('zmq server start....')
    while True:
        message = socket.recv().decode("UTF-8")
        count += 1
        print(f'received request. message:{message}; count:{count}')
        time.sleep(1)
        socket.send_string("ping test success")

```

client.py

```
import zmq


# 超时重连
class PingPort():
    def __init__(self):
        self.port = '5555'
        self.socket_req_url = 'tcp://localhost:{}'.format(self.port)
        self.socket_req = zmq.Context().socket(zmq.REQ)
        self.socket_req.connect(self.socket_req_url)
        self.poller = zmq.Poller()
        self.poller.register(self.socket_req, zmq.POLLIN)

    def ping(self):
        self.socket_req.send_string('ping test')
        if self.poller.poll(5555):
            resp = self.socket_req.recv().decode("UTF-8")
            print(resp)
        else:
            print('ping {} port fail, no response.'.format(self.port))
            self.socket_req.setsockopt(zmq.LINGER, 0)
            self.socket_req.close()
            self.poller.unregister(self.socket_req)
            print('-------------begin reconnect--------------------')
            self.socket_req = zmq.Context().socket(zmq.REQ)
            self.socket_req.connect(self.socket_req_url)
            self.poller = zmq.Poller()
            self.poller.register(self.socket_req, zmq.POLLIN)
            self.ping()


if __name__ == '__main__':
    obj = PingPort()
    obj.ping()

```

未超时： 

```
ping test success
```

已超时（若服务端未开启）：

```
ping 5555 port fail, no response.
-------------begin reconnect--------------------
ping 5555 port fail, no response.
-------------begin reconnect--------------------

```


