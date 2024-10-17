
--- 
title:  Golang 建立简单web服务器 
tags: []
categories: [] 

---
Go语言里面提供了一个完善的net/http包，通过http包可以很 方便的就搭建起来一个可以运行的web服务。 那么我门来建立一个简单的demo吧！

```
package main

import (
	"fmt"
	"log"
	"net/http"
)

func IndexFunc(w http.ResponseWriter, r *http.Request) {<!-- -->
	w.WriteHeader(http.StatusOK)
	fmt.Fprintf(w, "Wellcome to my server")

}
func main() {<!-- -->
	http.HandleFunc("/", IndexFunc)            //设置访问的路由
	url := "0.0.0.0:9999"
	fmt.Printf("\x1b[%dmserver:%s online \x1b[0m\n", 32, url)
	err := http.ListenAndServe(url, nil) // 设置监听的端口
	if err != nil {<!-- -->
		log.Fatal("ListenAndServe: ", err)
	}

}

```

### 编译代码并运行服务程序

#### 编译代码

```
go build main.go

```

#### 运行代码

```
./main

```

运行效果如下： <img src="https://img-blog.csdnimg.cn/7176feb5a1224dd19858e5b3712d14c3.png#pic_center" alt="在这里插入图片描述"> 在浏览器端发起get请求： <img src="https://img-blog.csdnimg.cn/da074b31d79549508f47924a5334e04a.png#pic_center" alt="在这里插入图片描述">
