
--- 
title:  [python3] 读者-写者模式 
tags: []
categories: [] 

---
读者-写者模式是一种并发设计模式，用于控制对共享资源的访问。在该模式中，有两类线程：读者线程和写者线程。读者线程可以同时访问共享资源，但写者线程在写入共享资源时需要独占访问权，这样可以确保数据一致性。读者-写者模式旨在提高对共享资源的并发访问效率。

下面是一个使用 Python 3 实现的简单的读者-写者模式示例：

```
import threading
import time

class ReadWriteLock:
    def __init__(self):
        self._readers = 0
        self._writers = 0
        self._lock = threading.Lock()
        self._read_cv = threading.Condition(self._lock)
        self._write_cv = threading.Condition(self._lock)

    def acquire_read(self):
        with self._lock:
            while self._writers &gt; 0:
                self._read_cv.wait()
            self._readers += 1

    def release_read(self):
        with self._lock:
            self._readers -= 1
            if self._readers == 0:
                self._write_cv.notify()

    def acquire_write(self):
        with self._lock:
            self._writers += 1
            while self._readers &gt; 0:
                self._write_cv.wait()

    def release_write(self):
        with self._lock:
            self._writers -= 1
            self._write_cv.notify()
            self._read_cv.notify_all()

def reader(lock, reader_id):
    lock.acquire_read()
    print(f"Reader {<!-- -->reader_id} is reading")
    time.sleep(1)  # 模拟读取操作
    lock.release_read()

def writer(lock, writer_id):
    lock.acquire_write()
    print(f"Writer {<!-- -->writer_id} is writing")
    time.sleep(1)  # 模拟写入操作
    lock.release_write()

if __name__ == '__main__':
    rw_lock = ReadWriteLock()

    # 创建多个读者和写者线程进行测试
    for i in range(3):
        threading.Thread(target=reader, args=(rw_lock, i)).start()
    for i in range(2):
        threading.Thread(target=writer, args=(rw_lock, i)).start()

```

在上面的示例中，使用了 `threading.Lock` 和 `threading.Condition` 来实现读者-写者模式。`ReadWriteLock` 类管理了读者和写者的访问，通过 `acquire_read`、`release_read`、`acquire_write` 和 `release_write` 方法来控制对共享资源的访问。在主程序中创建了多个读者和写者线程，模拟了并发访问共享资源的情况。当运行这段代码时，你会看到读者和写者交替访问共享资源的输出。
