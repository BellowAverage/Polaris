
--- 
title:  说说 Java 线程间通信 
tags: []
categories: [] 

---
### 序言

<img src="https://img-blog.csdnimg.cn/20191001081338114.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081348723.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081356961.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081405695.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081416514.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081423693.jpg#pic_center" alt="">

<img src="https://img-blog.csdnimg.cn/20191001081435483.jpg#pic_center" alt="">

### 正文

##### 1 Java线程间如何通信？

线程间通信的目标是使线程间能够互相发送信号，包括如下几种方式：

**1.1 通过共享对象通信**

线程间发送信号的一个简单方式是在共享对象的变量里设置信号值；线程A在一个同步块里设置boolean型成员变量hasDataToProcess为true，线程B也在同步块里读取hasDataToProcess这个成员变量；线程A和B必须获得指向一个MySignal共享实例的引用，以便进行通信；如果它们持有的引用指向不同的MySingal实例，那么彼此将不能检测到对方的信号；需要处理的数据可以存放在一个共享缓存区里，它和MySignal实例是分开存放的。示例如下：

```
public class MySignal{<!-- -->
  protected boolean hasDataToProcess = false;
  public synchronized boolean getHasDataToProcess(){<!-- -->
    return this.hasDataToProcess;
  }
  public synchronized void setHasDataToProcess(boolean hasData){<!-- -->
    this.hasDataToProcess = hasData;
  }
}

```

【场景展现】：

B同学去了图书馆，发现这本书被借走了(执行了例子中的hasDataToProcess)，他回到宿舍，等了几天，再去图书馆找这本书，发现这本书已经被还回，他顺利借走了书。

**1.2 忙等待**

准备处理数据的线程B正在等待数据变为可用；换句话说，它在等待线程A的一个信号，这个信号使hasDataToProcess()返回true，线程B运行在一个循环里，以等待这个信号。示例如下：

```
protected MySignal sharedSignal = ...
...
while(!sharedSignal.hasDataToProcess()){<!-- -->
  //do nothing... busy waiting
}

```

【场景展现】：

假如A同学在B同学走后一会就把书还回去了，B同学却是在几天后再次去图书馆找的书，为了早点借到书(减少延迟)，B同学可以就在图书馆等着，比如，每隔几分钟(while循环)他就去检查这本书有没有被还回，这样只要A同学一还回书，B同学很快就会知道。

**1.3 wait(),notify()和notifyAll()**

忙等待没有对运行等待线程的CPU进行有效的利用，除非平均等待时间非常短，否则，让等待线程进入睡眠或者非运行状态更为明智，直到它接收到它等待的信号。

一个线程一旦调用了任意对象的wait()方法，就会变为非运行状态，直到另一个线程调用了同一个对象的notify()方法；为了调用wait()或者notify()，线程必须先获得那个对象的锁；也就是说，线程必须在同步块里调用wait()或者notify()。示例如下：

```
public class MonitorObject{<!-- -->
}

public class MyWaitNotify{<!-- -->
  MonitorObject myMonitorObject = new MonitorObject();

  public void doWait(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      try{<!-- -->
        myMonitorObject.wait();
      } catch(InterruptedException e){<!-- -->...}
    }
  }
  public void doNotify(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      myMonitorObject.notify();
    }
  }
}

```

等待线程调用doWait()，而唤醒线程调用doNotify()；当一个线程调用一个对象的notify()方法，正在等待该对象的所有线程中将有一个线程被唤醒并允许执行（这个将被唤醒的线程是随机的，不可以指定唤醒哪个线程），可以使用notifyAll()方法来唤醒正在等待一个指定对象的所有线程。

【场景展现】：

检查很多次后，B同学发现这样做自己太累了，身体有点吃不消，不过很快，学校图书馆系统改进，加入了短信通知功能(notify())，只要A同学一还回书，立马会短信通知B同学，这样B同学就可以在家睡觉等短信了。

**1.4 丢失的信号**

notify()和notifyAll()方法不会保存调用它们的方法，因为当这两个方法被调用时，有可能没有线程处于等待状态，通知信号过后便丢弃了；因此，如果一个线程先于被通知线程调用wait()前调用了notify()，等待的线程将错过这个信号，在某些情况下，这可能使等待线程永远在等待，不再醒来，因为线程错过了唤醒信号。 为了避免丢失信号，必须把它们保存在信号类里。示例如下：

```
public class MyWaitNotify2{<!-- -->
  MonitorObject myMonitorObject = new MonitorObject();
  boolean wasSignalled = false;

  public void doWait(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      if(!wasSignalled){<!-- -->
        try{<!-- -->
          myMonitorObject.wait();
         } catch(InterruptedException e){<!-- -->...}
      }
      //clear signal and continue running.
      wasSignalled = false;
    }
  }

  public void doNotify(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      wasSignalled = true;
      myMonitorObject.notify();
    }
  }
}

```

【场景展现】：

学校图书馆系统是这么设计的：当一本书被还回来的时候，会给等待者发送短信，并且只会发一次，如果没有等待者，他也会发(只不过没有接收者)，这样问题就出现了，因为短信只会发一次，当书被还回来的时候，没有人等待借书，他会发一条空短信，但是之后有等待借此本书的同学永远也不会再收到短信，导致这些同学会无休止的等待；为了避免这个问题，我们在等待的时候先打个电话问问图书馆管理员是否继续等待(if(!wasSignalled))。

**1.5 假唤醒**

由于某种原因，线程有可能在没有调用过notify()和notifyAll()的情况下醒来，这就是所谓的假唤醒（spurious wakeups）。

如果在MyWaitNotify2的doWait()方法里发生了假唤醒，等待线程即使没有收到正确的信号，也能够执行后续的操作，这可能出现严重问题。

为了防止假唤醒，保存信号的成员变量将在一个while循环里接受检查，而不是在if表达式里，这样的一个while循环叫做自旋锁（这种做法会消耗CPU，如果长时间不调用doNotify方法，doWait方法会一直自旋，CPU会有很大消耗），被唤醒的线程会自旋直到自旋锁(while循环)里的条件变为false。示例如下：

```
public class MyWaitNotify3{<!-- -->
  MonitorObject myMonitorObject = new MonitorObject();
  boolean wasSignalled = false;

  public void doWait(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      while(!wasSignalled){<!-- -->
        try{<!-- -->
          myMonitorObject.wait();
         } catch(InterruptedException e){<!-- -->...}
      }
      //clear signal and continue running.
      wasSignalled = false;
    }
  }
  public void doNotify(){<!-- -->
    synchronized(myMonitorObject){<!-- -->
      wasSignalled = true;
      myMonitorObject.notify();
    }
  }
}

```

【场景展现】：

图书馆系统还有一个bug：系统会偶尔给你发条错误短信，说书可以借了(其实书不可以借)，我们之前已经给图书馆管理员打过电话了，他说让我们等短信，我们很听话，一等到短信(其实是bug引起的错误短信)，就去借书了，到了图书馆后发现这书根本就没还回来！我们很郁闷，但也没办法啊，学校不修复bug，我们得聪明点：每次在收到短信后，再打电话问问书到底能不能借(while(!wasSignalled))。

##### 2 多个线程如何按顺序执行？

多个线程如何保证执行顺序，是一个很高频的面试题，实现方式很多，这里介绍四种实现方式：

**2.1 使用Thread的join方法**

Thread类中的join方法的主要作用就是同步，调用线程需等待join线程执行完或指定时间后执行，如：join(10)，表示等待某线程执行10秒后再执行。示例如下：

```
public class ThreadChildJoin {<!-- -->
    public static void main(String[] args) {<!-- -->
        final Thread t1 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                System.out.println("需求分析...");
            }
        });

        final Thread t2 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    t1.join();
                    System.out.println("功能开发...");
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        Thread t3 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    t2.join();
                    System.out.println("功能测试...");
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        t3.start();
        t1.start();
        t2.start();
    }
}

```

**2.2 使用Condition(条件变量)**

Condition是一个多线程间协调通信的工具类，使得某个或者某些线程一起等待某个条件（Condition），只有当该条件具备( signal 或者 signalAll方法被带调用)时 ，这些等待线程才会被唤醒，从而重新争夺锁。

Condition类主要方法包括：await方法（类似于Object类中的wait()方法）、signal方法（类似于Object类中的notify()方法）、signalAll方法（类似于Object类中的notifyAll()方法）。示例如下：

```
public class ThreadCondition {<!-- -->
    private static Lock lock = new ReentrantLock();
    private static Condition condition1 = lock.newCondition();
    private static Condition condition2 = lock.newCondition();

    /**
     * 为什么要加这两个标识状态?
     * 如果没有状态标识，当t1已经运行完了t2才运行，t2在等待t1唤醒导致t2永远处于等待状态
     */
    private static Boolean t1Run = false;
    private static Boolean t2Run = false;

    public static void main(String[] args) {<!-- -->

        final Thread t1 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                lock.lock();
                System.out.println("需求分析...");
                t1Run = true;
                condition1.signal();
                lock.unlock();
            }
        });

        final Thread t2 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                lock.lock();
                try {<!-- -->
                    if(!t1Run){<!-- -->
                        condition1.await();
                    }
                    System.out.println("功能开发...");
                    t2Run = true;
                    condition2.signal();
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
                lock.unlock();
            }
        });

        Thread t3 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                lock.lock();
                try {<!-- -->
                    if(!t2Run){<!-- -->
                        condition2.await();
                    }
                    System.out.println("功能测试...");
                    lock.unlock();
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        t3.start();
        t1.start();
        t2.start();
    }
}

```

**2.3 使用CountDownLatch(倒计数)**

顾名思义，使用CountDownLatch可以实现类似计数器的功能。示例如下：

```
public class ThreadCountDownLatch {<!-- -->
    private static CountDownLatch c1 = new CountDownLatch(1);

    /**
     * 用于判断线程二是否执行，倒计时设置为1，执行后减1
     */
    private static CountDownLatch c2 = new CountDownLatch(1);

    public static void main(String[] args) {<!-- -->
        final Thread t1 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                System.out.println("需求分析...");
                //对c1倒计时-1
                c1.countDown();
            }
        });

        final Thread t2 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    //等待c1倒计时，计时为0则往下运行
                    c1.await();
                    System.out.println("功能开发...");
                    //对c2倒计时-1
                    c2.countDown();
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        Thread t3 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    //等待c2倒计时，计时为0则往下运行
                    c2.await();
                    System.out.println("功能测试...");
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        t3.start();
        t1.start();
        t2.start();
    }
}

```

**2.4 使用CyclicBarrier(回环栅栏)**

CyclicBarrier可以实现让一组线程等待至某个状态之后再全部同时执行，“回环”是因为当所有等待线程都被释放以后，CyclicBarrier可以被重用，可以把这个状态当做barrier，当调用await()方法之后，线程就处于barrier了。示例如下：

```
public class ThreadCyclicBarrier {<!-- -->
    static CyclicBarrier barrier1 = new CyclicBarrier(2);
    static CyclicBarrier barrier2 = new CyclicBarrier(2);

    public static void main(String[] args) {<!-- -->

        final Thread t1 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    System.out.println("需求分析...");
                    //放开栅栏1
                    barrier1.await();
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                } catch (BrokenBarrierException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        final Thread t2 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    //放开栅栏1
                    barrier1.await();
                    System.out.println("功能开发...");
                    //放开栅栏2
                    barrier2.await();
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                } catch (BrokenBarrierException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        final Thread t3 = new Thread(new Runnable() {<!-- -->
            @Override
            public void run() {<!-- -->
                try {<!-- -->
                    //放开栅栏2
                    barrier2.await();
                    System.out.println("功能测试...");
                } catch (InterruptedException e) {<!-- -->
                    e.printStackTrace();
                } catch (BrokenBarrierException e) {<!-- -->
                    e.printStackTrace();
                }
            }
        });

        t3.start();
        t1.start();
        t2.start();
    }
}

```

参考： 

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
