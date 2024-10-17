
--- 
title:  Python 多线程中的 join() 和 setDaemon() 
tags: []
categories: [] 

---
Demo 是最好的老师！！！

参考链接：

**知识点一（setDaemon(False)）：** 当一个进程启动之后，会默认产生一个主线程，因为线程是程序执行流的最小单元，当设置多线程时，主线程会创建多个子线程，在 python 中，默认情况下（其实就是setDaemon(False)），主线程执行完自己的任务以后，此时子线程会继续执行自己的任务，直到自己的任务结束。

```
import threading
import time


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.start()

    print('主线程结束！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)

```

```
这是主线程： MainThread
主线程结束！ MainThread
一共用时： 0.001401662826538086
当前线程的名字是：  Thread-3
当前线程的名字是：  Thread-4
当前线程的名字是：  Thread-2
当前线程的名字是：  Thread-1
当前线程的名字是：  Thread-5

Process finished with exit code 0
```

**知识点二（setDaemon(True)）：** 当我们使用 setDaemon(True) 方法，设置子线程为守护线程时，主线程一旦执行结束，则全部线程全部被终止执行，可能出现的情况就是，子线程的任务还没有完全执行结束，就被迫停止。

```
import threading
import time


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    print('主线程结束了！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)

```

```
这是主线程： MainThread
主线程结束了！ MainThread
一共用时： 0.002007722854614258

Process finished with exit code 0
```

**知识点三（setDaemon(True) and join）：** 此时 join 的作用就凸显出来了，join 所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态（并没有退出），会一直等待其他的子线程都执行结束之后，主线程再终止（退出）。所以多线程里边同时使用 join() 和 setDaemon() 是并不矛盾的。

```
import threading
import time


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        t.join()

    print('主线程结束了！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)

```

```
这是主线程： MainThread
当前线程的名字是：  Thread-1
当前线程的名字是：  Thread-3
当前线程的名字是：  Thread-2
当前线程的名字是：  Thread-5
当前线程的名字是：  Thread-4
主线程结束了！ MainThread
一共用时： 4.003052711486816

Process finished with exit code 0
```

**知识点四（join(timeout=param)）：** join 有一个 timeout 参数：当设置守护线程时，含义是主线程对于子线程等待 timeout 的时间将会杀死该子线程，最后退出程序。所以说，如果有10个子线程，全部的等待时间就是每个 timeout 的累加和（10 * timeout）。简单的来说，就是给每个子线程一个 timeout 的时间，让他去执行，时间一到，不管任务有没有完成，直接杀死。

```
import threading
import time


def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()

    for t in thread_list:
        # 线程列表总共 5 个元素，所以主线程会在这儿等待 5 * 0.2 秒
        t.join(timeout=0.2)

    print('主线程结束了！', threading.current_thread().name)
    print('一共用时：', time.time() - start_time)

```

```
这是主线程： MainThread
主线程结束了！ MainThread
一共用时： 1.0173823833465576

Process finished with exit code 0
```

没有设置守护线程时，主线程将会等待 timeout 的累加和这样的一段时间，时间一到，主线程结束，但是并没有杀死子线程（设置守护的话才会去杀死子线程），子此时线程依然可以继续执行，直到子线程全部结束，程序退出。

**最后来个自己实际项目中遇到的例子：**

**需求：已知有一个 src.rpm 的包，我只知道它和 conf.ini 中的地址拼接起来的 url 中，只有一个是有效的。如何快速把这个包下载下来？**

conf.ini：

```
[centos]
src_package1=https://vault.centos.org/7.6.1810/centosplus/Source/SPackages/
src_package2=https://vault.centos.org/7.6.1810/cloud/Source/openstack-ocata/
src_package3=https://vault.centos.org/7.6.1810/cloud/Source/openstack-ocata/common/
src_package4=https://vault.centos.org/7.6.1810/cloud/Source/openstack-pike/
src_package5=https://vault.centos.org/7.6.1810/opstools/Source/common/
src_package6=https://vault.centos.org/7.6.1810/cloud/Source/openstack-queens/
src_package7=https://vault.centos.org/7.6.1810/cloud/Source/openstack-rocky/
src_package8=https://vault.centos.org/7.6.1810/cloud/Source/openstack-stein/

```

```
import configparser
import os
import threading
import time


def download(download_url):
    global is_downloaded
    with pool_sema:
        status_code = os.system('wget -q %s' % download_url)
        if status_code == 0:
            # 如果已经成功下载，修改全局变量，方便主线程获取已下载信号后跳出循环，结束程序执行。
            is_downloaded = True


if __name__ == '__main__':
    global is_downloaded
    is_downloaded = False
    src_package = 'centos-release-opstools-1-4.el7.src.rpm'
    conf = configparser.ConfigParser()
    conf.read('conf.ini', encoding="UTF-8")
    thread_list = []
    max_connections = 10  # 定义最大线程数
    pool_sema = threading.BoundedSemaphore(max_connections)
    t1 = time.perf_counter()
    for i in range(1, 9):
        url = conf.get('centos', 'src_package' + str(i))
        download_url = os.path.join(url, src_package)
        thread = threading.Thread(target=download, args=(download_url,))
        thread_list.append(thread)

    # 设置守护，也即主线程（main函数）结束的话（下载超时或者源码包已经成功下载），
    # 所有子线程必须强制退出（后面的download_url就不必再去尝试 wget 了）
    for t in thread_list:
        t.setDaemon(True)
        t.start()
    # 主线程不需要等待子线程全部结束后才退出，
    # 只需要获取到某个子线程已经成功下载的信号（is_downloaded）之后即可自行退出
    # for t in thread_list:
    #     t.join()
    while True:
        t2 = time.perf_counter()
        # 下载超时后跳出循环，结束执行
        if t2 - t1 &gt; 5 * 10:
            print('download timeout')
            break
        if is_downloaded:
            print('download success')
            break
    t2 = time.perf_counter()
    print('download costs %.2f seconds' % (t2 - t1))

```

```
[root@localhost insight-tool]# python3 test.py
download success
download costs 4.35 seconds

```

**Ruby线程中的join**

在Ruby线程中，join方法的作用是阻塞当前线程，直到调用join方法的线程执行完成。具体而言，当在某个线程中调用另一个线程的join方法时，调用线程会被阻塞，直到被调用的线程执行完成。通过这种方式，可以保证被调用线程的执行顺序。通常情况下，主线程（调用线程）会等待所有子线程（被调用线程）执行完成后再继续执行。这样可以避免主线程在子线程还未执行完成时提前结束，确保程序的正确执行顺序。以下是一个简单示例，演示了join方法的作用：

```
# 创建一个子线程，模拟一些耗时操作
thread = Thread.new do
    sleep(2)
    puts "子线程执行完成"
end
puts "等待子线程执行..."
thread.join
puts "子线程已执行完成"
```

```
等待子线程执行...
子线程执行完成
子线程已执行完成
```

如果没有调用join方法，主线程会立即执行最后一行的输出语句，而不会等待子线程执行完成。

```
thread = Thread.new do
    sleep(2)
    puts "子线程执行完成"
end
puts "等待子线程执行..."
# thread.join
puts "子线程已执行完成"
```

```
等待子线程执行...
子线程已执行完成
```
