
--- 
title:  qt 定时器用法 
tags: []
categories: [] 

---
在qt开发中，定时器是我们经常用到的。我们接下来说一下定时器的三种用法，需要注意的是定时器事件是在主线程中触发的，因此在处理耗时操作时应特别小心，以避免阻塞应用程序的事件循环。

## 1. 三种定时器使用

### 1.1 QObject的定时器

使用startTimer()函数启动一个定时器，并在派生类中实现timerEvent(QTimerEvent*)函数来处理定时器事件，所以我们要重写 void timerEvent(QTimerEvent* ev)函数，如：

```
/*
my_class.h
*/
// 在头文件中声明
protected:
    void timerEvent(QTimerEvent* ev);

/*
my_class.cpp
*/
// 在派生类中
void MyClass::timerEvent(QTimerEvent *event) {<!-- -->
    if (event-&gt;timerId() == m_timerId) {<!-- -->
        // 处理定时器事件
    } else {<!-- -->
        // 处理其他定时器事件
    }
}

// 启动定时器(可放在构造函数里)
m_timerId = startTimer(1000); // 每1000毫秒触发一次定时器事件

```

### 1.2 QTimer类：

创建一个QTimer对象，然后使用start()函数来启动定时器，使用timeout()信号连接到槽函数来处理定时器超时事件。如：

```
QTimer *timer = new QTimer(this);
connect(timer, &amp;QTimer::timeout, this, &amp;MyClass::onTimeout);
timer-&gt;start(1000); // 每1000毫秒触发一次定时器超时事件

// 槽函数
void MyClass::onTimeout() {<!-- -->
    // 处理定时器超时事件
}

```

### 1.3 单次定时器：

当只需要定时器触发一次时，可以使用setSingleShot(true)来设置定时器为单次模式。如：

```
QTimer *timer = new QTimer(this);
timer-&gt;setSingleShot(true); // 设置为单次定时器
connect(timer, &amp;QTimer::timeout, this, &amp;MyClass::onTimeout);
timer-&gt;start(1000); // 在1000毫秒后触发一次定时器超时事件

// 槽函数
void MyClass::onTimeout() {<!-- -->
    // 处理定时器超时事件
}

```

## 2 定时器阻塞主线程问题

当定时器处理耗时操作时，为了不阻塞主线程，可以考虑以下方法：
-  使用多线程：将耗时操作放在单独的线程中执行，以避免阻塞主线程。在定时器触发时，启动一个新线程执行耗时操作，这样定时器事件处理和主线程可以同时进行。 -  异步操作：使用异步操作来执行耗时操作，例如使用异步函数、Promise或回调函数。在定时器事件触发时，调用相应的异步操作来执行耗时任务，它们会在后台执行，而主线程可以继续执行其他任务。 -  分解任务：将耗时操作分解为多个较小的子任务，并在定时器事件触发时，每次执行一个子任务。这样可以避免长时间的单一操作阻塞主线程，而是将任务划分为多个短时间的操作，使得主线程能够处理其他任务。 
无论使用哪种方法，重要的是确保定时器事件的处理不会导致主线程的阻塞，保持应用的响应性和流畅性。
