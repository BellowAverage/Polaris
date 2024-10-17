
--- 
title:  python3多任务编程：多进程、多线程、协程、互斥锁、死锁 
tags: []
categories: [] 

---
## 多任务

多任务的最大好处是充分利用CPU资源，提高程序的执行效率。

### 1.概念

#### 多任务是指在同一时间内执行多个任务，例如: 现在电脑安装的操作系统都是多任务操作系统，可以同时运行着多个软件。

#### 小结
- 使用多任务就能充分利用CPU资源，提高程序的执行效率，让你的程序具备处理多个任务的能力。- 多任务执行方式有两种方式：并发和并行，这里并行才是多个任务真正意义一起执行。
### 2.执行方式

#### 并发
- 在一段时间内交替去执行任务。
#### 并行
- 对于多核cpu处理多任务，操作系统会给cpu的每个内核安排一个执行的软件，多个内核是真正的一起执行软件。这里需要注意多核cpu是并行的执行多任务，始终有多个软件一起执行。
### 3.进程

#### 介绍
- 在Python程序中，想要实现多任务可以使用进程来完成，进程是实现多任务的一种方式。
#### 概念
- 一个正在运行的程序或者软件就是一个进程，它是操作系统进行资源分配的基本单位，也就是说每启动一个进程，操作系统都会给其分配一定的运行资源(内存资源)保证进程的运行。- 比如:现实生活中的公司可以理解成是一个进程，公司提供办公资源(电脑、办公桌椅等)，真正干活的是员工，员工可以理解成线程。
#### 注意:
- 一个程序运行后至少有一个进程，一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程。
#### 小结
- 进程是操作系统进行资源分配的基本单位。- 进程是Python程序中实现多任务的一种方式
#### 多进程的使用
-  导入进程包 import multiprocessing -  创建子进程并指定执行的任务 sub_process = multiprocessing.Process (target=任务名) -  启动进程执行任务 sub_process.start() 
#### Process进程类的说明
<li>Process([group [, target [, name [, args [, kwargs]]]]]) 
  <ul>- group：指定进程组，目前只能使用None- target：执行的目标任务名- name：进程名字- args：以元组方式给执行任务传参- kwargs：以字典方式给执行任务传参- start()：启动子进程实例（创建子进程）- join()：等待子进程执行结束- terminate()：不管任务是否完成，立即终止子进程- name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
#### 多进程完成多任务的代码

```
import multiprocessing
import time

# 跳舞任务

def dance():
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)

# 唱歌任务

def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None
    # target: 表示执行的目标任务名(函数名、方法名)
    # name: 进程名称, 默认是Process-1, .....
    dance_process = multiprocessing.Process(target=dance, name="myprocess1")
    sing_process = multiprocessing.Process(target=sing)


# 启动子进程执行对应的任务
dance_process.start()
sing_process.start()

```

#### 获取进程编号
<li>获取进程编号的目的 
  <ul>- 获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的。<li>获取当前进程编号 
    <ul>- os.getpid() 表示获取当前进程编号- os.getppid() 表示获取当前父进程编号
#### 进程执行带有参数的任务的介绍
- args 表示以元组的方式给执行任务传参
```
  import multiprocessing
  import time

  # 带有参数的任务

  def task(count):
      for i in range(count):
          print("任务执行中..")
          time.sleep(0.2)
      else:
          print("任务执行完成")

  if __name__ == '__main__':
      # 创建子进程
      # args: 以元组的方式给任务传入参数
      sub_process = multiprocessing.Process(target=task, args=(5,))
      sub_process.start()

```
-  元组方式传参一定要和参数的顺序保持一致。 -  kwargs 表示以字典方式给执行任务传参 
```
  import multiprocessing
  import time

  # 带有参数的任务

  def task(count):
      for i in range(count):
          print("任务执行中..")
          time.sleep(0.2)
      else:
          print("任务执行完成")

  if __name__ == '__main__':
      # 创建子进程

  # kwargs: 表示以字典方式传入参数
  sub_process = multiprocessing.Process(target=task, kwargs={<!-- -->"count": 3})
  sub_process.start()

```
- 字典方式传参字典中的key一定要和参数名保持一致。
#### 进程的注意点
- 进程之间不共享全局变量
```
  import multiprocessing
  import time

  # 定义全局变量

  g_list = list()

  # 添加数据的任务

  def add_data():
      for i in range(5):
          g_list.append(i)
          print("add:", i)
          time.sleep(0.2)

  
  # 代码执行到此，说明数据添加完成
  print("add_data:", g_list)
  def read_data():
      print("read_data", g_list)

  if __name__ == '__main__':
      # 创建添加数据的子进程
      add_data_process = multiprocessing.Process(target=add_data)
      # 创建读取数据的子进程
      read_data_process = multiprocessing.Process(target=read_data)

  # 启动子进程执行对应的任务
  add_data_process.start()
  # 主进程等待添加数据的子进程执行完成以后程序再继续往下执行，读取数据
  add_data_process.join()
  read_data_process.start()
  
  print("main:", g_list)
  
  # 总结: 多进程之间不共享全局变量

```
<li> 小结 
  <ul>- 创建子进程会对主进程资源进行拷贝，也就是说子进程是主进程的一个副本，好比是一对双胞胎，之所以进程之间不共享全局变量，是因为操作的不是同一个进程里面的全局变量，只不过不同进程里面的全局变量名字相同而已。
主进程会等待所有的子进程执行结束再结束

```
  import multiprocessing
  import time

  # 定义进程所需要执行的任务

  def task():
      for i in range(10):
          print("任务执行中...")
          time.sleep(0.2)

  if __name__ == '__main__':
      # 创建子进程
      sub_process = multiprocessing.Process(target=task)
      sub_process.start()


  # 主进程延时0.5秒钟
  time.sleep(0.5)
  print("over")
  exit()
  
  # 总结： 主进程会等待所有的子进程执行完成以后程序再退出

```

#### 守护主进程:
- 守护主进程就是主进程退出子进程销毁不再执行
```
  import multiprocessing
  import time

  # 定义进程所需要执行的任务

  def task():
      for i in range(10):
          print("任务执行中...")
          time.sleep(0.2)

  if __name__ == '__main__':
      # 创建子进程
      sub_process = multiprocessing.Process(target=task)
      # 设置守护主进程，主进程退出子进程直接销毁，子进程的生命周期依赖与主进程
      # sub_process.daemon = True
      sub_process.start()

  time.sleep(0.5)
  print("over")
  # 让子进程销毁
  sub_process.terminate()
  exit()
  # 总结： 主进程会等待所有的子进程执行完成以后程序再退出
  # 如果想要主进程退出子进程销毁，可以设置守护主进程或者在主进程退出之前让子进程销毁

```

#### 子进程销毁:
- 子进程执行结束
#### 小结
- 为了保证子进程能够正常的运行，主进程会等所有的子进程执行完成以后再销毁，设置守护主进程的目的是主进程退出子进程销毁，不让主进程再等待子进程去执行。- 设置守护主进程方式： 子进程对象.daemon = True- 销毁子进程方式： 子进程对象.terminate()
### 进程和线程的对比

#### 关系对比
- 线程是依附在进程里面的，没有进程就没有线程。- 一个进程默认提供一条线程，进程可以创建多个线程。
#### 区别对比
- 进程之间不共享全局变量- 线程之间共享全局变量，但是要注意资源竞争的问题，解决办法: 互斥锁或者线程同步- 创建进程的资源开销要比创建线程的资源开销要大- 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位- 线程不能够独立执行，必须依存在进程中- 多进程开发比单进程多线程开发稳定性要强
#### 优缺点对比
<li>进程优缺点: 
  <ul>- 优点：可以用多核- 缺点：资源开销大- 优点：资源开销小- 缺点：不能使用多核
### 4.线程

#### 概念
- 线程是进程中执行代码的一个分支，每个执行分支（线程）要想工作执行代码需要cpu进行调度 ，也就是说线程是cpu调度的基本单位，每个进程至少都有一个线程，而这个线程就是我们通常说的主线程。
#### 多线程的使用
<li>导入线程模块 
  <ul>- import threading- sub_thread = threading.Thread(target=任务名)- sub_thread.start()
#### 线程类Thread参数说明
- Thread([group [, target [, name [, args [, kwargs]]]]])- group: 线程组，目前只能使用None- target: 执行的目标任务名- args: 以元组的方式给执行任务传参- kwargs: 以字典方式给执行任务传参- name: 线程名，一般不用设置
#### 多线程完成多任务的代码

```
import threading
import time

# 唱歌任务

def sing():
    # 扩展： 获取当前线程
    # print("sing当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)

# 跳舞任务

def dance():
    # 扩展： 获取当前线程
    # print("dance当前执行的线程为：", threading.current_thread())
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)

if __name__ == '__main__':
    # 扩展： 获取当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)

# 创建跳舞的线程
dance_thread = threading.Thread(target=dance)

# 开启线程
sing_thread.start()
dance_thread.start()

```

#### 进程执行带有参数的任务的介绍
- args 表示以元组的方式给执行任务传参
```
  import multiprocessing
  import time

  # 带有参数的任务

  def task(count):
      for i in range(count):
          print("任务执行中..")
          time.sleep(0.2)
      else:
          print("任务执行完成")

  if __name__ == '__main__':
      # 创建子进程
      # args: 以元组的方式给任务传入参数
      sub_process = multiprocessing.Process(target=task, args=(5,))
      sub_process.start()

  - 元组方式传参一定要和参数的顺序保持一致。

- kwargs 表示以字典方式给执行任务传参

  import multiprocessing
  import time

  # 带有参数的任务

  def task(count):
      for i in range(count):
          print("任务执行中..")
          time.sleep(0.2)
      else:
          print("任务执行完成")

  if __name__ == '__main__':
      # 创建子进程

  # kwargs: 表示以字典方式传入参数
  sub_process = multiprocessing.Process(target=task, kwargs={<!-- -->"count": 3})
  sub_process.start()

```
- 字典方式传参字典中的key一定要和参数名保持一致。
#### 注意点
- 线程之间执行是无序的
```
  import threading
  import time

  def task():
      time.sleep(1)
      print("当前线程:", threading.current_thread().name)

  if __name__ == '__main__':

     for _ in range(5):
         sub_thread = threading.Thread(target=task)
         sub_thread.start()

  - 线程之间执行是无序的，它是由cpu调度决定的 ，cpu调度哪个线程，哪个线程就先执行，没有调度的线程不能执行。
  - 进程之间执行也是无序的，它是由操作系统调度决定的，操作系统调度哪个进程，哪个进程就先执行，没有调度的进程不能执行。

- 主线程会等待所有的子线程执行结束再结束

  import threading
  import time

  # 测试主线程是否会等待子线程执行完成以后程序再退出

  def show_info():
      for i in range(5):
          print("test:", i)
          time.sleep(0.5)

  if __name__ == '__main__':
      # 创建子线程守护主线程 
      # daemon=True 守护主线程
      # 守护主线程方式1
      sub_thread = threading.Thread(target=show_info, daemon=True)
      # 设置成为守护主线程，主线程退出后子线程直接销毁不再执行子线程的代码
      # 守护主线程方式2
      # sub_thread.setDaemon(True)
      sub_thread.start()

  
  # 主线程延时1秒
  time.sleep(1)
  print("over")

```
- 守护主线程:
```
    import threading
    import time

    # 测试主线程是否会等待子线程执行完成以后程序再退出

    def show_info():
        for i in range(5):
            print("test:", i)
            time.sleep(0.5)

    if __name__ == '__main__':
        # 创建子线程守护主线程 
        # daemon=True 守护主线程
        # 守护主线程方式1
        sub_thread = threading.Thread(target=show_info, daemon=True)
        # 设置成为守护主线程，主线程退出后子线程直接销毁不再执行子线程的代码
        # 守护主线程方式2
        # sub_thread.setDaemon(True)
        sub_thread.start()

    # 主线程延时1秒
    time.sleep(1)
    print("over")

```
-  threading.Thread(target=show_info, daemon=True) -  线程对象.setDaemon(True) -  线程之间共享全局变量 
```
  import threading
  import time

  # 定义全局变量

  my_list = list()

  # 写入数据任务

  def write_data():
      for i in range(5):
          my_list.append(i)
          time.sleep(0.1)
      print("write_data:", my_list)

  # 读取数据任务

  def read_data():
      print("read_data:", my_list)

  if __name__ == '__main__':
      # 创建写入数据的线程
      write_thread = threading.Thread(target=write_data)
      # 创建读取数据的线程
      read_thread = threading.Thread(target=read_data)

  write_thread.start()
  # 延时
  # time.sleep(1)
  # 主线程等待写入线程执行完成以后代码在继续往下执行
  write_thread.join()
  print("开始读取数据啦")
  read_thread.start()

```
- 线程之间共享全局变量数据出现错误问题
```
  import threading

  # 定义全局变量

  g_num = 0

  # 循环一次给全局变量加1

  def sum_num1():
    for i in range(1000000):
      global g_num
      g_num += 1

    print("sum1:", g_num)

  # 循环一次给全局变量加1

  def sum_num2():
    for i in range(1000000):
      global g_num
      g_num += 1
    print("sum2:", g_num)

  if __name__ == '__main__':

  # 创建两个线程

    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

  # 启动线程

    first_thread.start()

  # 启动线程

    second_thread.start()

```
- 线程等待(join)
```
    import threading

    # 定义全局变量

    g_num = 0

    # 循环1000000次每次给全局变量加1

    def sum_num1():
        for i in range(1000000):
            global g_num
            g_num += 1

    ```
    print("sum1:", g_num)
    ```

    # 循环1000000次每次给全局变量加1

    def sum_num2():
        for i in range(1000000):
            global g_num
            g_num += 1
        print("sum2:", g_num)

    if __name__ == '__main__':
        # 创建两个线程
        first_thread = threading.Thread(target=sum_num1)
        second_thread = threading.Thread(target=sum_num2)

    # 启动线程
    first_thread.start()
    # 主线程等待第一个线程执行完成以后代码再继续执行，让其执行第二个线程
    # 线程同步： 一个任务执行完成以后另外一个任务才能执行，同一个时刻只有一个任务在执行
    first_thread.join()
    # 启动线程
    second_thread.start()

```
- 保证同一时刻只能有一个线程去操作全局变量 同步: 就是协同步调，按预定的先后次序进行运行。- 互斥锁
```
    import threading

    # 定义全局变量

    g_num = 0

    # 创建全局互斥锁

    lock = threading.Lock()

    # 循环一次给全局变量加1

    def sum_num1():

    # 上锁

      lock.acquire()
      for i in range(1000000):
        global g_num
        g_num += 1

      print("sum1:", g_num)

    # 释放锁

      lock.release()

    # 循环一次给全局变量加1

    def sum_num2():

    # 上锁

      lock.acquire()
      for i in range(1000000):
        global g_num
        g_num += 1
      print("sum2:", g_num)

    # 释放锁

      lock.release()

    if __name__ == '__main__':

    # 创建两个线程

      first_thread = threading.Thread(target=sum_num1)
      second_thread = threading.Thread(target=sum_num2)

    # 启动线程

      first_thread.start()
      second_thread.start()

    # 提示：加上互斥锁，那个线程抢到这个锁我们决定不了，那线程抢到锁那个线程先执行，没有抢到的线程需要等待

    # 加上互斥锁多任务瞬间变成单任务，性能会下降，也就是说同一时刻只能有一个线程去执行

```
<li> 概念 
  <ul>- 对共享数据进行锁定，保证同一时刻只能有一个线程去操作。
注意:
- 互斥锁是多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程需要等待，等互斥锁使用完释放后，其它等待的线程再去抢这个锁。
使用
-  1.穿件全局互斥锁 lock = threading.lock() -  2.上锁 lock.acquire() -  2.解锁 lock.release() 
小结
- 互斥锁的作用就是保证同一时刻只能有一个线程去操作共享数据，保证共享数据不会出现错误问题- 使用互斥锁的好处确保某段关键代码只能由一个线程从头到尾完整地去执行- 使用互斥锁会影响代码的执行效率，多任务改成了单任务执行- 互斥锁如果没有使用好容易出现死锁的情况
死锁

```

    mport threading
    import time

    # 创建互斥锁

    lock = threading.Lock()

    # 根据下标去取值， 保证同一时刻只能有一个线程去取值

    def get_value(index):

    ```
    # 上锁
    lock.acquire()
    print(threading.current_thread())
    my_list = [3,6,8,1]
    # 判断下标释放越界
    if index &gt;= len(my_list):
        print("下标越界:", index)
        return
    value = my_list[index]
    print(value)
    time.sleep(0.2)
    # 释放锁
    lock.release()
    ```

    if __name__ == '__main__':
        # 模拟大量线程去执行取值操作
        for i in range(30):
            sub_thread = threading.Thread(target=get_value, args=(i,))
            sub_thread.start()

```
<li> 概念 
  <ul>- 一直等待对方释放锁的情景就是死锁
结果
- 会造成应用程序的停止响应，不能再处理其它任务了
避免死锁

```
      import threading
      import time

      # 创建互斥锁

      lock = threading.Lock()

      # 根据下标去取值， 保证同一时刻只能有一个线程去取值

      def get_value(index):

    
      # 上锁
      lock.acquire()
      print(threading.current_thread())
      my_list = [3,6,8,1]
      if index &gt;= len(my_list):
          print("下标越界:", index)
          # 当下标越界需要释放锁，让后面的线程还可以取值
          lock.release()
          return
      value = my_list[index]
      print(value)
      time.sleep(0.2)
      # 释放锁
      lock.release()
     

      if __name__ == '__main__':
          # 模拟大量线程去执行取值操作
          for i in range(30):
              sub_thread = threading.Thread(target=get_value, args=(i,))
              sub_thread.start()

```

### 5.小结

#### 进程和线程都是完成多任务的一种方式

#### 多进程要比多线程消耗的资源多，但是多进程开发比单进程多线程开发稳定性要强，某个进程挂掉不会影响其它进程。

#### 多进程可以使用cpu的多核运行，多线程可以共享全局变量。

#### 线程不能单独执行必须依附在进程里面

### 协程

#### 介绍
- 协程是python个中另外一种实现多任务的方式。- 只不过比线程更小占用更小执行单元（理解为需要的资源）。<li>通俗的理解： 
  <ul>- 在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定。
#### 优点
- 最大的优势就是协程极高的执行效率。因为函数切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。- 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#### gevent
<li> 介绍 
  <ul>- gevent 是一个第三方库。- Python中仅提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。- 其原理是当一个任务函数遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的任务函数执行，等到IO操作完成，再在适当的时候切换回来继续执行。- 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有任务函数在运行，而不是等待IO,得以实现多任务,提高程序执行效率。
使用

```
  import gevent

  def f(n):
      for i in range(n):
          print(gevent.getcurrent(), i)

  g1 = gevent.spawn(f, 5)
  g2 = gevent.spawn(f, 5)
  g3 = gevent.spawn(f, 5)
  g1.join()
  g2.join()
  g3.join()

```
- 切换
```
  import gevent

  def f(n):
      for i in range(n):
          print(gevent.getcurrent(), i)
          #用来模拟一个耗时操作，注意不是time模块中的sleep
          gevent.sleep(1)

  g1 = gevent.spawn(f, 5)
  g2 = gevent.spawn(f, 5)
  g3 = gevent.spawn(f, 5)
  g1.join()
  g2.join()
  g3.join()

```
- 给程序打补丁
```
  from gevent import monkey
  import gevent
  import random
  import time

  def coroutine_work(coroutine_name):
      for i in range(10):
          print(coroutine_name, i)
          time.sleep(random.random())

  gevent.joinall([
          gevent.spawn(coroutine_work, "work1"),
          gevent.spawn(coroutine_work, "work2")
  ])
  work1 0
  work1 1
  work1 2
  work1 3
  work1 4
  work1 5
  work1 6
  work1 7
  work1 8
  work1 9
  work2 0
  work2 1
  work2 2
  work2 3
  work2 4
  work2 5
  work2 6
  work2 7
  work2 8
  work2 9
  from gevent import monkey
  import gevent
  import random
  import time

  # 有耗时操作时需要

  monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块

  def coroutine_work(coroutine_name):
      for i in range(10):
          print(coroutine_name, i)
          time.sleep(random.random())

  gevent.joinall([
          gevent.spawn(coroutine_work, "work1"),
          gevent.spawn(coroutine_work, "work2")
  ])
  运行结果
  work1 0
  work2 0
  work1 1
  work1 2
  work1 3
  work2 1
  work1 4
  work2 2
  work1 5
  work2 3
  work1 6
  work1 7
  work1 8
  work2 4
  work2 5
  work1 9
  work2 6
  work2 7
  work2 8
  work2 9

```
