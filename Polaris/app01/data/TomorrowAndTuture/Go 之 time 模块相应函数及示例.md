
--- 
title:  Go 之 time 模块相应函数及示例 
tags: []
categories: [] 

---
## 时间获取

### time.Hours()

`time.Hours()`函数就是用于获取时间点以来的小时数。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t1 := time.Now()
	t2, _ := time.Parse("2006-01-02 15:04:05 -0700 MST", "2023-12-24 14:41:40 +0800 CST")
	hours := t2.Sub(t1)
	fmt.Println(hours.Hours()) // 3021.5102945206113
}

```

### time.Clock()

主要用于获取一个 time.Time 值的小时、分钟和秒数。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	hour, min, sec := now.Clock()
	fmt.Printf("now is %02d:%02d:%02d\n", hour, min, sec) // now is 11:40:22
}

```

### time.Hour()/Minute()/Second()

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now() // 获取当前时间

	hour := t.Hour()
	fmt.Println(hour) // 输出当前时间的小时数
	minute := t.Minute()
	fmt.Println(minute) // 输出当前时间的分钟数
	second := t.Second()
	fmt.Println(second) // 输出当前时间的秒数
}

```

### time.Date()

主要用于获取 time.Time 类型变量表示的时间的年月日信息。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	year, month, day := t.Date()
	fmt.Printf("now is %04d-%02d-%02d\n", year, month, day) // now is 2023-09-10
}

```

### time.Day()

time.Time.Day()函数是一个用来获取当前时间的天数的函数。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	// 当前时间
	t := time.Now()

	// 获取当前时间的天数
	day := t.Day()

	// 输出结果
	fmt.Printf("today is %d号\n", day) // today is 9号
}

```

### time.Weekday()

time.Weekday()函数用来获取当前时间的星期。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println("today is", now.Weekday()) // today is Monday
}

```

## 时间解析

### time.Parse()

time.Parse()函数将字符串转换为了Time类型。其中第一个参数是时间格式，第二个参数是待转换的字符串。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t, _ := time.Parse("2006-01-02 15:04:05 -0700 MST", "2021-12-24 14:41:40 +0800 CST")
	fmt.Printf("Time: %v\n", t) // Time: 2021-12-24 14:41:40 +0800 CST
}

```

###  time.ParseDuration()

时间间隔解析

```
package main

import (
	"fmt"
	"time"
)

func main() {
	d, _ := time.ParseDuration("3600s")
	fmt.Printf("Duration in seconds: %f\n", d.Seconds())

	d, _ = time.ParseDuration("1.5h")
	fmt.Printf("Duration in minutes: %f\n", d.Minutes())

	d, _ = time.ParseDuration("2h45m")
	fmt.Printf("Duration in hours: %f\n", d.Hours())

	d, _ = time.ParseDuration("1m30s")
	fmt.Printf("Duration in nanoseconds: %d\n", d.Nanoseconds())

	d, _ = time.ParseDuration("500ms")
	fmt.Printf("Duration in microseconds: %d\n", d.Microseconds())

	// Duration in seconds: 3600.000000
	// Duration in minutes: 90.000000
	// Duration in hours: 2.750000
	// Duration in nanoseconds: 90000000000
	// Duration in microseconds: 500000
}

```

## 时间格式化

### time.Format()

```
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	a := now.AppendFormat([]byte{}, time.RFC3339)
	a2 := now.Format(time.RFC3339)
	fmt.Println(string(a)) // 2023-09-10T11:25:32+08:00
	fmt.Println(a2)        // 2023-09-10T11:25:32+08:00

	layout := "Jan 2, 2006 at 3:04pm (MST)"
	b := now.AppendFormat([]byte{}, layout)
	b2 := now.Format(layout)
	fmt.Println(string(b)) // Sep 10, 2023 at 11:25am (CST)
	fmt.Println(b2)        // Sep 10, 2023 at 11:25am (CST)

	layout = "2006-01-02 15:04:05"
	c := now.AppendFormat([]byte{}, layout)
	c2 := now.Format(layout)
	fmt.Println(string(c)) // 2023-09-10 11:25:32
	fmt.Println(c2)        // 2023-09-10 11:25:32

	layout = "2006-01-02 15:04:05.000"
	fmt.Println(now.Format(layout))        // 2023-09-10 11:25:32 612

	layout = "2006-01-02 15:04:05.999"
	fmt.Println(now.Format(layout))        // 2023-09-10 11:25:32 612

	layout = "2006-01-02"
	fmt.Println(now.Format(layout))        // 2023-09-10

	layout = "15:04:05"
	fmt.Println(now.Format(layout))        // 11:25:32
}

```

## 时间序列化

### time.GobEncode()

```
package main

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"time"
)

type TimeWrapper struct {
	Time time.Time
}

func main() {
	var buffer bytes.Buffer
	encoder := gob.NewEncoder(&amp;buffer)

	now := TimeWrapper{Time: time.Now()}
	err := encoder.Encode(&amp;now)
	if err != nil {
		fmt.Println("encode error: ", err)
	}

	var otherTime TimeWrapper
	decoder := gob.NewDecoder(&amp;buffer)
	err = decoder.Decode(&amp;otherTime)
	if err != nil {
		fmt.Println("decode error: ", err)
	}

	fmt.Println(now.Time)       // 2023-09-10 12:15:57.6990592 +0800 CST m=+0.001000001
	fmt.Println(otherTime.Time) // 2023-09-10 12:15:57.6990592 +0800
}

```

## 时间定时器

### time.After()

time.After() 函数用于创建一个 Timer 对象并在指定的持续时间后向其 C 字段发送一个时间值。当然，如果在循环中多路复用使用 time.After 的话，记得不要在 case 直接写 time.After 哟，因为每一次执行 select 的 time.After() 都会重新开始计时。

```
package main

import (
	"time"
	"fmt"
)

func main() {
	ch := make(chan int)
	go func() {
		fmt.Println("Start goroutine...")
		time.Sleep(3 * time.Second)
		ch &lt;- 1
	}()

	select {
	case &lt;- ch:
		fmt.Println("chan get message")
	case &lt;- time.After(2 * time.Second):
		fmt.Println("timeout!") // timeout!
	}
}

```

### time.AfterFunc()

`time.AfterFunc()`函数是在指定的时间之后执行一个函数的方法。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Start main...")
	fmt.Println("print hello world after 5 seconds...")
	time.AfterFunc(time.Second*5, func() {
		fmt.Println("hello world")
	})
	time.Sleep(time.Second*10)
	fmt.Println("the end")
	// Start main...
	// print hello world after 5 seconds...
	// hello world
	// the end
}

```

###  time.NewTicker()

在使用select语句的时候，我们首先需要注意下面几个事情。
-  有默认分支，那么无论涉及通道操作的表达式是否有阻塞，select 语句都不会被阻塞。如果那几个表达式都阻塞了，或者说都没有满足求值的条件，那么默认分支就会被选中并执行。- 没有加入默认分支，那么一旦所有的 case 表达式都没有满足求值条件，那么 select 语句就会被阻塞。直到至少有一个 case 表达式满足条件为止。- 我们需要通过接收表达式的第二个结果值来判断通道是否已经关闭。一旦发现某个通道关闭了，我们就应该及时地屏蔽掉对应的分支或者采取其他措施。这对于程序逻辑和程序性能都是有好处的。- select 语句只能对其中的每一个 case 表达式各求值一次。如果我们想连续或定时地操作其中的通道的话，就往往需要通过在 for 语句中嵌入 select 语句的方式实现。但这时要注意，简单地在 select 语句的分支中使用 break 语句，只能结束当前的 select 语句的执行，而并不会对外层的 for 语句产生作用。这种错误的用法可能会让这个 for 语句无休止地运行下去。
```
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Program started.", time.Now().Format("2006-01-02 15:04:05"))
	timer := time.NewTimer(3 * time.Second)
	&lt;- timer.C
	fmt.Println("Timer expired.", time.Now().Format("2006-01-02 15:04:05"))

	ticker := time.NewTicker(2 * time.Second)
	defer ticker.Stop()
	for {
		select {
		case &lt;-ticker.C:
			fmt.Println("ticker:", time.Now().Format("2006-01-02 15:04:05"))
		}
	}
// 	Program started. 2023-09-02 14:02:06
// 	Timer expired. 2023-09-02 14:02:09
//  ticker: 2023-09-02 14:02:11
//  ticker: 2023-09-02 14:02:13
}

```

### time.Tick()

```
package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.Tick(2 * time.Second)
	count := 0
	for now := range ticker {
		count++
		fmt.Printf("%d: %s\n", count, now)
		if count == 5 {
			break
		}
	}
	// 1: 2023-09-02 15:47:57.8208432 +0800 CST m=+2.002114501
	// 2: 2023-09-02 15:47:59.8209576 +0800 CST m=+4.002228901
	// 3: 2023-09-02 15:48:01.821072 +0800 CST m=+6.002343301
	// 4: 2023-09-02 15:48:03.8211864 +0800 CST m=+8.002457701
	// 5: 2023-09-02 15:48:05.8213008 +0800 CST m=+10.002572101
}

```

### time.Ticker.Stop()

```
package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()

	for {
		select {
		case &lt;-ticker.C:
			fmt.Println("Ticker tick")
		}
	}
}

```

## 时间戳

time.Unix()

```
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now().Unix()
	fmt.Println("Unix时间戳（  秒）为：", now)

	milli := time.Now().UnixMilli()
	fmt.Println("Unix时间戳（毫秒）为：", milli)

	micro := time.Now().UnixMicro()
	fmt.Println("Unix时间戳（微秒）为：", micro)

	nano := time.Now().UnixNano()
	fmt.Println("Unix时间戳（纳秒）为：", nano)

	// Unix时间戳（秒）  为： 1692523606
	// Unix时间戳（毫秒）为： 1692523606723
	// Unix时间戳（微秒）为： 1692523606723707
	// Unix时间戳（纳秒）为： 1692523606723707200
}

```

### time.Second

```
package main

import (
	"fmt"
	"time"
)

func main() {
	nano := time.Now().UnixNano()
	fmt.Println("Unix时间戳（纳秒）为：", nano)
	fmt.Println("Unix时间戳（纳秒）为：", nano / int64(time.Nanosecond))
	fmt.Println("Unix时间戳（微秒）为：", nano / int64(time.Microsecond))
	fmt.Println("Unix时间戳（毫秒）为：", nano / int64(time.Millisecond))
	fmt.Println("Unix时间戳（  秒）为：", nano / int64(time.Second))

	// Unix时间戳（纳秒）为： 1692531897930937100
	// Unix时间戳（纳秒）为： 1692531897930937100
	// Unix时间戳（微秒）为： 1692531897930937
	// Unix时间戳（毫秒）为： 1692531897930
	// Unix时间戳（  秒）为： 1692531897
}

```

## 时间计算

### time.Round()

四舍五入

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2021, 1, 17, 4, 37, 0, 0, time.UTC)
	fmt.Println(t.Round(time.Hour))        // 输出：2021-01-17 05:00:00 +0000 UTC
	fmt.Println(t.Round(30 * time.Minute)) // 输出：2021-01-17 04:30:00 +0000 UTC
}

```

### time.Since()

计算当前时间和开始时间的间隔

```
package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Date(2023, 9, 1, 4, 37, 0, 0, time.UTC)
	diff := time.Since(start)
	fmt.Println(diff) // 26h19m50.8567339s
}

```

### time.Add()

在时间点上加上一个固定时长，例如 2 个小时、5 分钟等；或根据时间信息，计算出距离当前时间点一定时长之后的时间。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t1 := time.Now()
	t2 := t1.Add(5 * time.Minute)
	t3 := t1.Add(2 * time.Hour)
	fmt.Println(t1)
	fmt.Println(t2)
	fmt.Println(t3)
	// 2023-09-10 11:12:09.7998193 +0800 CST m=+0.000000001
	// 2023-09-10 11:17:09.7998193 +0800 CST m=+300.000000001
	// 2023-09-10 13:12:09.7998193 +0800 CST m=+7200.000000001
}

```

### time.AddDate()

它接受三个参数：`years`、`months`和`days`，分别表示要增加（或减少）的年数、月数和天数。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Date(2023, time.May, 18, 0, 0, 0, 0, time.UTC)
	t2 := t.AddDate(1, 2, 3)
	fmt.Println(t2) // 2024-07-21 00:00:00 +0000 UTC
}

```

### time.Sub()

求两个时间之间的差值。返回一个时间段t-u。如果结果超出了Duration可以表示的最大值/最小值，将返回最大值/最小值。要获取时间点t-d（d为Duration），可以使用t.Add(-d)。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	t1 := time.Now()
	t2 := t1.Add(5 * time.Minute)
	t3 := t2.Sub(t1)
	fmt.Println(t1)
	fmt.Println(t2)
	fmt.Println(t3)
	// 2023-09-10 11:12:09.7998193 +0800 CST m=+0.000000001
	// 2023-09-10 11:17:09.7998193 +0800 CST m=+300.000000001
	// 5m0s
}

```

## 时间比较

### time.Before()

time.Time.Before() 用来判断一个时间是否早于另一个时间。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	// 2022年1月1日
	t1 := time.Date(2022, 1, 1, 0, 0, 0, 0, time.UTC)
	// 2021年12月31日
	t2 := time.Date(2021, 12, 31, 0, 0, 0, 0, time.UTC)

	if t2.Before(t1) {
		fmt.Println("t2 is earlier than t1") // t2 is earlier than t1
	} else {
		fmt.Println("t1 is earlier than t2")
	}
}

```

### time.Equal()

表示要比较的两个时间对象是否表示相同时间。通过调用此方法，我们可以避免手动解析和比较日期和时间。

```
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	n1 := now.Add(5 * time.Second)
	n2 := now.Add(10 * time.Second)

	fmt.Println(n1.Equal(now))  // false
	fmt.Println(n2.Equal(now))  // false
	fmt.Println(now.Equal(now)) // true
}

```

## 常用时间获取操作

```
package model

import (
	"time"
)

// 时间戳间戳转换成日期时间
func UnixToDate(timestamp int) string {
	t := time.Unix(int64(timestamp), 0)
	return t.Format("2006-01-02 15:04:05")
}

// 日期转换成时间戳 2020-05-02 15:04:05
func DateToUnix(str string) int64 {
	template := "2006-01-02 15:04:05"
	t, err := time.ParseInLocation(template, str, time.Local)
	if err != nil {
		return 0
	}
	return t.Unix()
}

// 获取时间戳
func GetUnix() int64 {
	return time.Now().Unix()
}

// 获取当前日期
func GetDate() string {
	template := "2006-01-02 15:04:05"
	return time.Now().Format(template)
}

// 获取年月日
func GetDay() string {
	template := "2006-01-02"
	return time.Now().Format(template)
}

```


