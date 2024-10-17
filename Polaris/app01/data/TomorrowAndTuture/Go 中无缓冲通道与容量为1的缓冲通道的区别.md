
--- 
title:  Go 中无缓冲通道与容量为1的缓冲通道的区别 
tags: []
categories: [] 

---
作为学Go的菜鸟，之前我以为这两个应该是同一个东西，以为无缓冲通道是缓冲通道容量为1的一种特殊情况。然鹅，这俩货根本不是同一个东西。

## 无缓冲通道

无缓冲通道也称为同步通道，发送操作会阻塞，直到另一个 goroutine 在对应通道执行接收操作。

在单线程中，往无缓冲通道写入数据是会造成死锁的。

**这里的A或B，无论谁先执行，谁都会阻塞以等待另一个goroutine执行**，也就是说往里写得等来读的，从里读得等来写的。最重要的是，**A和B对s1的读写是同步的**，直观的理解是A和B对s1的读写是同时发生的，当A对s1写完了，则B从s1中就读完了。这样的特性可以用于做并发单位之间的同步操作，如果在A和B中对同一个无缓冲通道进行了读写，那么A和B一定会在读写的地方进行同步，谁先到谁阻塞等待另外一个。

```
package main

func main() {
	s1 := make(chan int)
	s1 &lt;- 1 // A fatal error: all goroutines are asleep - deadlock!
	fmt.Println(&lt;-s1)   // B fatal error: all goroutines are asleep - deadlock!
}

```

这里以一个具体的示例来表现无缓冲通道的用法和特性。使用 WaitGroup 避免主线程提前结束。

```
package main

import (
	"fmt"
	"sync"
	"time"
)

const Interval = 5

func main() {
	fmt.Printf("%s: main thread start\n", time.Now().Format("2006-01-02 15:04:05"))
	naturals := make(chan int)
	var wg sync.WaitGroup
	// put
	wg.Add(1)
	go func() {
		defer wg.Done()
		for x := 0; x &lt; Interval; x++ {
			naturals &lt;- x
			fmt.Printf("%s: put %d \n", time.Now().Format("2006-01-02 15:04:05"), x)
			time.Sleep(time.Duration(x+1) * time.Second)
		}
		close(naturals)
	}()
	time.Sleep(Interval * time.Second) // wait sometime for writing
	// get
	wg.Add(1)
	go func() {
		defer wg.Done()
		for {
			x, ok := &lt;-naturals
			if !ok {
				fmt.Printf("%s: break", time.Now().Format("2006-01-02 15:04:05"))
				break // 通道关闭且读完
			}
			fmt.Printf("%s: get %d \n", time.Now().Format("2006-01-02 15:04:05"), x)
		}
	}()
	wg.Wait()
}
```

```
2024-04-09 22:40:43: main thread start
2024-04-09 22:40:48: get 0 
2024-04-09 22:40:48: put 0 
2024-04-09 22:40:49: put 1 
2024-04-09 22:40:49: get 1 
2024-04-09 22:40:51: put 2 
2024-04-09 22:40:51: get 2 
2024-04-09 22:40:54: put 3 
2024-04-09 22:40:54: get 3 
2024-04-09 22:40:58: put 4 
2024-04-09 22:40:58: get 4 
2024-04-09 22:41:03: break
```

我这块还把写入和获取的时间打印出来了，可以看到，针对同一个元素，往通道写入和从通道取出是同时完成的（get 和 put 对应的时间相同），这也是无缓冲通道为什么叫做同步通道的原因。

我在两个协程之间还特地 sleep 了几秒（因为有时间差，如果不同步的话，必然 put 操作早于 get 操作），但是从打印结果看出，put 写操作并没有先于 get 执行，而是同步执行。

## 容量为1的缓冲通道

对于容量为1的缓冲通道，只要从通道取值的时候，通道里有值，就是可以正常执行的。

```
package main

import "fmt"

func main() {
	s1 := make(chan int, 1)
	s1 &lt;- 1
	fmt.Println(&lt;-s1) // 1
}

```

我们可以尝试把上面例子中的无缓冲通道修改成容量为1的缓冲通道再运行试试，只是将

```
package main

import (
	"fmt"
	"sync"
	"time"
)

const Interval = 5

func main() {
	fmt.Printf("%s: main thread start\n", time.Now().Format("2006-01-02 15:04:05"))
	naturals := make(chan int, 1)
	var wg sync.WaitGroup
	// put
	wg.Add(1)
	go func() {
		defer wg.Done()
		for x := 0; x &lt; Interval; x++ {
			naturals &lt;- x
			fmt.Printf("%s: put %d \n", time.Now().Format("2006-01-02 15:04:05"), x)
			time.Sleep(time.Duration(x+1) * time.Second)
		}
		close(naturals)
	}()
	time.Sleep(Interval * time.Second) // wait sometime for writing
	// get
	wg.Add(1)
	go func() {
		defer wg.Done()
		for {
			x, ok := &lt;-naturals
			if !ok {
				fmt.Printf("%s: break", time.Now().Format("2006-01-02 15:04:05"))
				break // 通道关闭且读完
			}
			fmt.Printf("%s: get %d \n", time.Now().Format("2006-01-02 15:04:05"), x)
		}
	}()
	wg.Wait()
}
```

从打印结果可以看出，这里和无缓冲通道不同的地方在于，有缓冲的通道并不强制 channel 的读写者必须**同时完成发送和接收**，读操作只会在没有数据时阻塞，写操作只会在没有可用容量时阻塞，这就有点像阻塞队列了。  因此，本例中对于容量为1的缓冲通道，第一个数据写入后才开始阻塞然后等待读操作读取（因为读操作在 sleep 几秒之后才开始读取操作，通道已满，写操作暂时阻塞，待读操作读取数据后，写操作再继续执行）

```
2024-04-09 22:44:15: main thread start
2024-04-09 22:44:15: put 0 
2024-04-09 22:44:20: get 0 
2024-04-09 22:44:20: get 1 
2024-04-09 22:44:20: put 1 
2024-04-09 22:44:22: put 2 
2024-04-09 22:44:22: get 2 
2024-04-09 22:44:25: put 3 
2024-04-09 22:44:25: get 3 
2024-04-09 22:44:29: put 4 
2024-04-09 22:44:29: get 4 
2024-04-09 22:44:34: break
```

## 通道关闭

关闭后的通道有以下特点：
1. 对一个关闭的通道再发送值就会导致panic。1. 对一个关闭的通道进行接收会一直获取值直到通道为空。1. 对一个关闭的并且没有值的通道执行接收操作会得到对应类型的零值。1. 关闭一个已经关闭的通道会导致panic。
关于通道的更多知识可参考：
