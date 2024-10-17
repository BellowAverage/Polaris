
--- 
title:  《Java 简易速速上手小册》第6章：Java 并发编程（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/e6ee6a4b463d43ea862b95164d3c9200.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 6.1 线程的创建和管理 - 召唤你的士兵

在Java并发编程的世界中，线程是执行任务的基本单位。正确地创建和管理线程就像是召唤和指挥你的士兵一样重要。让我们深入探索如何有效地召唤这些勇士，并确保他们能够有效地完成任务。

### 6.1.1 基础知识
<li> **创建线程的两种方式**： 
  <ul>- **继承Thread类**：创建一个新类继承`Thread`类，并重写`run()`方法。通过实例化这个类并调用其`start()`方法来启动线程。- **实现Runnable接口**：创建一个实现了`Runnable`接口的类，并实现`run()`方法。然后将这个实现类的实例传递给`Thread`类的构造函数，并通过新线程的`start()`方法来启动。
**线程的生命周期**：新建（New）、就绪（Runnable）、运行（Running）、阻塞（Blocked）和终止（Terminated）。

**线程的优先级**：每个线程都有一个优先级，它们可以从`Thread.MIN_PRIORITY`（1）到`Thread.MAX_PRIORITY`（10）变化，`Thread.NORM_PRIORITY`（5）是默认优先级。

### 6.1.2 重点案例：实现一个简单的计数器

假设我们要实现一个简单的计数器，每个线程负责将一个共享变量增加到特定的值。

**计数器Runnable实现**:

```
public class Counter implements Runnable {<!-- -->
    private final int limit;
    private static int count = 0;

    public Counter(int limit) {<!-- -->
        this.limit = limit;
    }

    @Override
    public void run() {<!-- -->
        while (count &lt; limit) {<!-- -->
            synchronized (Counter.class) {<!-- -->
                if (count &lt; limit) {<!-- -->
                    System.out.println(Thread.currentThread().getName() + ": " + (++count));
                }
            }
        }
    }

    public static void main(String[] args) {<!-- -->
        Runnable counter = new Counter(10);
        new Thread(counter, "Thread-1").start();
        new Thread(counter, "Thread-2").start();
    }
}

```

在这个例子中，我们创建了一个实现了`Runnable`接口的`Counter`类。每个线程在`run()`方法中增加计数器，直到达到了限制值。我们使用`synchronized`关键字来确保在同一时刻只有一个线程能够增加计数器。

### 6.1.3 拓展案例 1：定时器线程

创建一个线程，定时打印消息到控制台，演示如何使用线程来执行定时任务。

```
import java.util.Timer;
import java.util.TimerTask;

public class Reminder {<!-- -->
    Timer timer;

    public Reminder(int seconds) {<!-- -->
        timer = new Timer();
        timer.schedule(new RemindTask(), seconds * 1000);
    }

    class RemindTask extends TimerTask {<!-- -->
        public void run() {<!-- -->
            System.out.println("Time's up!");
            timer.cancel();
        }
    }

    public static void main(String[] args) {<!-- -->
        new Reminder(5);
        System.out.println("Task scheduled.");
    }
}

```

### 6.1.4 拓展案例 2：使用 Executor 框架管理线程

Executor框架提供了更高级的接口来管理线程池，使得管理一组任务更加容易。

```
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPoolDemo {<!-- -->
    public static void main(String[] args) {<!-- -->
        ExecutorService executor = Executors.newFixedThreadPool(5);
        
        for (int i = 0; i &lt; 10; i++) {<!-- -->
            Runnable worker = new WorkerThread("" + i);
            executor.execute(worker);
        }
        
        executor.shutdown();
        while (!executor.isTerminated()) {<!-- -->
        }
        
        System.out.println("Finished all threads");
    }
}

class WorkerThread implements Runnable {<!-- -->
    private String message;
    
    public WorkerThread(String message) {<!-- -->
        this.message = message;
    }

    public void run() {<!-- -->
        System.out.println(Thread.currentThread().getName() + " (Start) message = " + message);
        processMessage();
       

 System.out.println(Thread.currentThread().getName() + " (End)");
    }

    private void processMessage() {<!-- -->
        try {<!-- -->
            Thread.sleep(2000);
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }
    }
}

```

通过这些案例，我们看到了Java线程创建和管理的多样化方法。无论是通过实现`Runnable`接口，使用定时器任务，还是利用Executor框架管理线程池，正确的线程管理策略都能使你的并发程序运行得更加高效和稳定。现在，带着你的士兵们勇往直前，征服并发编程的世界吧！

<img src="https://img-blog.csdnimg.cn/direct/e208fe4162c542a792bff99671f92638.png#pic_center" alt="在这里插入图片描述" width="400">

## 6.2 同步机制 - 维持军队的秩序

在并发编程的战场上，正确的同步机制就像是用来维持你的数据军队秩序的军规，确保所有士兵行动协调，避免混乱和冲突。Java提供了多种同步工具和方法，帮助开发者有效管理线程间的协作和资源共享。

### 6.2.1 基础知识
-  **synchronized关键字**：可以用于方法或代码块，确保同一时刻只有一个线程可以执行该段代码，从而避免资源冲突或数据不一致的问题。 -  **volatile关键字**：用于标记变量，确保每次访问变量时都会从主内存中读取，而不是从线程的工作内存，从而保证了变量的可见性。 -  **Lock接口**：提供了比`synchronized`更灵活的锁定机制，包括可重入锁（ReentrantLock）、读写锁（ReadWriteLock）等，允许更细粒度的锁控制。 -  **Condition接口**：与Lock配合使用，允许线程间有更细致的通信（比如等待/通知机制），实现线程间的协调。 
### 6.2.2 重点案例：银行转账操作

假设我们需要实现一个银行账户的转账操作，这个操作需要确保线程安全，避免在并发环境下出现资金错误。

```
public class Account {<!-- -->
    private int balance;
    private final Lock lock = new ReentrantLock();

    public Account(int balance) {<!-- -->
        this.balance = balance;
    }

    // 转账操作
    public void transfer(Account target, int amount) {<!-- -->
        lock.lock();
        try {<!-- -->
            if (this.balance &gt;= amount) {<!-- -->
                this.balance -= amount;
                target.deposit(amount);
            }
        } finally {<!-- -->
            lock.unlock();
        }
    }

    public void deposit(int amount) {<!-- -->
        lock.lock();
        try {<!-- -->
            this.balance += amount;
        } finally {<!-- -->
            lock.unlock();
        }
    }

    public int getBalance() {<!-- -->
        return balance;
    }
}

```

在这个例子中，`transfer`方法使用了`ReentrantLock`来确保转账操作的原子性，避免了并发环境下的资金错误。

### 6.2.3 拓展案例 1：生产者消费者问题

生产者消费者是并发编程中的一个经典问题，它涉及到两个或多个线程间的协作。使用`Lock`和`Condition`可以优雅地解决这个问题。

```
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ProducerConsumer {<!-- -->
    private final Queue&lt;Integer&gt; queue = new LinkedList&lt;&gt;();
    private final int capacity = 10;
    private final Lock lock = new ReentrantLock();
    private final Condition notFull = lock.newCondition();
    private final Condition notEmpty = lock.newCondition();

    // 生产者方法
    public void produce(int value) throws InterruptedException {<!-- -->
        lock.lock();
        try {<!-- -->
            while (queue.size() == capacity) {<!-- -->
                notFull.await();
            }
            queue.add(value);
            notEmpty.signalAll();
        } finally {<!-- -->
            lock.unlock();
        }
    }

    // 消费者方法
    public int consume() throws InterruptedException {<!-- -->
        lock.lock();
        try {<!-- -->
            while (queue.isEmpty()) {<!-- -->
                notEmpty.await();
            }
            int value = queue.poll();
            notFull.signalAll();
            return value;
        } finally {<!-- -->
            lock.unlock();
        }
    }
}

```

### 6.2.4 拓展案例 2：读写锁实现缓存系统

读写锁（`ReadWriteLock`）允许多个读操作同时进行，但写操作是互斥的。这对于实现缓存系统来说非常有用。

```
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWrite

Lock;

public class Cache {<!-- -->
    private final Map&lt;String, Object&gt; map = new HashMap&lt;&gt;();
    private final ReadWriteLock rwLock = new ReentrantReadWriteLock();

    public Object get(String key) {<!-- -->
        rwLock.readLock().lock();
        try {<!-- -->
            return map.get(key);
        } finally {<!-- -->
            rwLock.readLock().unlock();
        }
    }

    public void put(String key, Object value) {<!-- -->
        rwLock.writeLock().lock();
        try {<!-- -->
            map.put(key, value);
        } finally {<!-- -->
            rwLock.writeLock().unlock();
        }
    }
}

```

通过这些案例，我们看到了Java中同步机制的强大之处，它不仅帮助我们维持线程间的协作和数据的一致性，还使我们能够设计出高效且线程安全的并发应用。掌握这些同步工具，成为并发编程的指挥官吧！

<img src="https://img-blog.csdnimg.cn/direct/4ebdcada5fd94a82aea1a6f7c753c788.png#pic_center" alt="在这里插入图片描述" width="400">

## 6.3 并发工具类 - 你的特殊武器

Java的并发工具类就像是隐藏在你的武器库中的特殊武器，它们可以帮助你在并发编程的战场上更加游刃有余。这些工具类提供了强大的功能来帮助管理线程间的协调，以及对共享资源的访问控制，让你能够写出更高效、更健壮的并发程序。

### 6.3.1 基础知识
-  **CountDownLatch**：允许一个或多个线程等待其他线程完成一系列操作。当倒计时达到零时，等待的线程被释放继续执行。 -  **CyclicBarrier**：允许一组线程互相等待，直到所有线程都达到了某个共同点，然后继续执行。 -  **Semaphore**：一种基于计数的同步机制，可以控制对共享资源的访问。它可以限制同时访问某个特定资源的线程数量。 -  **Concurrent Collections**：提供了线程安全的集合类，如`ConcurrentHashMap`、`CopyOnWriteArrayList`等，用于在并发环境中管理数据。 -  **Executor框架**：简化了线程的创建和管理，提供了线程池等高级功能，使得并发任务的调度和管理更加灵活和强大。 
### 6.3.2 重点案例：使用 CountDownLatch 协调任务

假设我们有一个任务，需要在开始执行主任务之前，等待其他几个服务初始化完成。

```
import java.util.concurrent.CountDownLatch;

public class ServiceInitializer {<!-- -->
    private static final int NUM_OF_SERVICES = 3;
    private final CountDownLatch latch = new CountDownLatch(NUM_OF_SERVICES);

    public void initialize() {<!-- -->
        for (int i = 1; i &lt;= NUM_OF_SERVICES; i++) {<!-- -->
            new Thread(new Service(latch), "Service " + i).start();
        }

        try {<!-- -->
            latch.await(); // 等待所有服务初始化完成
            System.out.println("All services are initialized. Main task is starting now.");
        } catch (InterruptedException e) {<!-- -->
            Thread.currentThread().interrupt();
        }
    }

    static class Service implements Runnable {<!-- -->
        private final CountDownLatch latch;

        public Service(CountDownLatch latch) {<!-- -->
            this.latch = latch;
        }

        @Override
        public void run() {<!-- -->
            try {<!-- -->
                // 模拟服务初始化耗时
                Thread.sleep((long) (Math.random() * 1000));
                System.out.println(Thread.currentThread().getName() + " initialized.");
            } catch (InterruptedException e) {<!-- -->
                Thread.currentThread().interrupt();
            } finally {<!-- -->
                latch.countDown();
            }
        }
    }

    public static void main(String[] args) {<!-- -->
        new ServiceInitializer().initialize();
    }
}

```

### 6.3.3 拓展案例 1：使用 CyclicBarrier 同步周期性任务

假设我们需要执行一个周期性任务，该任务需要在每个周期内的所有子任务完成后才能开始下一个周期。

```
import java.util.concurrent.CyclicBarrier;

public class CyclicTask implements Runnable {<!-- -->
    private CyclicBarrier barrier;

    public CyclicTask(CyclicBarrier barrier) {<!-- -->
        this.barrier = barrier;
    }

    @Override
    public void run() {<!-- -->
        try {<!-- -->
            System.out.println(Thread.currentThread().getName() + " is waiting at the barrier.");
            barrier.await();
            System.out.println(Thread.currentThread().getName() + " has crossed the barrier.");
        } catch (Exception e) {<!-- -->
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {<!-- -->
        final int parties = 3;
        CyclicBarrier barrier = new CyclicBarrier(parties, 
            () -&gt; System.out.println("All parties have arrived at the barrier, let's proceed to the next step."));

        for (int i = 0; i &lt; parties; i++) {<!-- -->
            new Thread(new CyclicTask(barrier), "Thread " + (i + 1)).start();
        }
    }
}

```

### 6.3.4 拓展案例 2：使用 Semaphore 控制资源访问

在某些情况下，我们需要限制对某个资源的并发访问数量

。Semaphore提供了一种简单有效的方法来实现这一目标。

```
import java.util.concurrent.Semaphore;

public class SemaphoreDemo {<!-- -->
    private static final int MAX_PERMITS = 3;
    private final Semaphore semaphore = new Semaphore(MAX_PERMITS);

    public void accessResource() {<!-- -->
        try {<!-- -->
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " is accessing the resource.");
            Thread.sleep(1000); // 模拟资源访问耗时
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        } finally {<!-- -->
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " has released the resource.");
        }
    }

    public static void main(String[] args) {<!-- -->
        SemaphoreDemo demo = new SemaphoreDemo();
        for (int i = 0; i &lt; 6; i++) {<!-- -->
            new Thread(demo::accessResource, "Thread " + (i + 1)).start();
        }
    }
}

```

通过这些案例，我们可以看到Java并发工具类如何成为处理并发和多线程问题的强大武器。无论是协调多个任务的完成，同步周期性任务的执行，还是控制对共享资源的访问，这些工具类都能让你的并发编程工作变得更加简单和高效。使用这些特殊的武器，指挥你的数据军团，优雅地完成并发任务！
