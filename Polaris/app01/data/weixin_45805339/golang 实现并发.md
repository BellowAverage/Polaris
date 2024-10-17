
--- 
title:  golang 实现并发 
tags: []
categories: [] 

---
### 1 关键字go和channel实现并发(阻塞主进程，防止其退出)

go语言，语言层面原生支持高并发，通过关键字go与信号通道channel组合实现。实现起来还是相当容易的例如：

```
package main

import (
	"fmt"
)

func main() {<!-- -->
	c := make(chan bool, 100)
	for i := 0; i &lt; 100; i++ {<!-- -->
		go func(i int) {<!-- -->
			fmt.Println(i)
			c &lt;- true
		}(i)
	}

	for i := 0; i &lt; 100; i++ {<!-- -->
		&lt;-c
	}
}

```

### 2 通过sync.WaitGroup

除了关键字go和channel，我们还有更简单的方法来实现，就是标准库sync中的WaitGrop WaitGroup等待一组goroutines完成。主goroutine调用Add来设置要等待的goroutine的数量。然后每个goroutines运行并在完成时调用Done。同时，Wait可以用来阻塞，直到所有goroutines完成。 WaitGroup在第一次使用后不能被复制。

```
package main

import (
	"fmt"
	"sync"
)

func main() {<!-- -->
	wg := sync.WaitGroup{<!-- -->}
	wg.Add(10)
	for i := 0; i &lt; 10; i++ {<!-- -->
		go func(i int) {<!-- -->
			fmt.Println(i)
			wg.Done()
		}(i)
	}
	wg.Wait()
}

```

WaitGroup 结构：

```
type WaitGroup struct {<!-- -->
	// contains filtered or unexported fields
}

```

我们来看看官网的例子：

```
package main

import (
	"sync"
)

type httpPkg struct{<!-- -->}

func (httpPkg) Get(url string) {<!-- -->}

var http httpPkg

func main() {<!-- -->
	var wg sync.WaitGroup
	var urls = []string{<!-- -->
		"http://www.golang.org/",
		"http://www.google.com/",
		"http://www.example.com/",
	}
	for _, url := range urls {<!-- -->
		// Increment the WaitGroup counter.
		wg.Add(1)
		// Launch a goroutine to fetch the URL.
		go func(url string) {<!-- -->
			// Decrement the counter when the goroutine completes.
			defer wg.Done()
			// Fetch the URL.
			http.Get(url)
		}(url)
	}
	// Wait for all HTTP fetches to complete.
	wg.Wait()
}

```

### 3 官网


