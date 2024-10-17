
--- 
title:  Go 语言使用 XORM 操作 MySQL 的陷阱 
tags: []
categories: [] 

---
**1 **

### 介绍



在 Go 语言开发中，大家为了方便，通常会选择使用 ORM 操作数据库，比如使用 XORM 或 GORM 操作 MySQL。

虽然使用 ORM 操作 MySQL 比直接使用标准库 `sql`和三方 MySQL 数据库驱动包操作 MySQL 更加方便，但是也会遇到一些陷阱。

本文我们来介绍一下使用 XORM 操作 MySQL 可能会遇到的陷阱。

**2 **

### 使用 XORM 操作 MySQL 的陷阱

**类型零值**

在 Golang 中，每个数据类型都有各自的类型零值，比如 int 的零值是 `0`，string 的零值是 ''等。

示例代码：

```
package main

import (
 "fmt"
 _ "github.com/go-sql-driver/mysql"
 "xorm.io/xorm"
)

func main() {
 // 创建 Engine
 engine, err := xorm.NewEngine("mysql", "root:root@/example?charset=utf8")
 defer func() {
  err = engine.Close()
  if err != nil {
   fmt.Printf("engine close err=%v\n", err)
   return
  }
 }()
 if err != nil {
  fmt.Printf("init xorm engine fail, err=%v\n", err)
  return
 }

 // 更新数据
 example := &amp;Example{
  Title: "go",
  View:  0,
 }
 condi := &amp;Example{
  Id: 2,
 }
 affected, err := engine.Update(example, condi)
 if err != nil {
  fmt.Printf("Update err=%v\n", err)
  return
 }
 fmt.Printf("affected=%d\n", affected)
}

type Example struct {
 Id      int    `json:"id" form:"id"`
 Title   string `json:"title" form:"title"`
 View    int    `json:"view" form:"view"`
 Created int    `json:"created" form:"created" xorm:"created"`
 Updated int    `json:"updated" form:"updated" xorm:"updated"`
}

```

阅读上面这段代码，我们可以发现示例代码中将 `id=2` 的数据 view 字段更新为 `0`，因为 `0` 是 int 的类型零值，XORM 的 Update 方法会自动忽略类型零值，所以该数据 view 字段的值没有更改。

但是，在实际项目开发中，我们可能需要将某个字段的值更新为该字段类型的类型零值，此时我们该怎么操作呢？

```
affected, err := engine.Cols("title", "view").Update(example, condi)

```

我们可以使用 `Cols()` 方法，指定需要更新的字段，这样即便需要更新字段的值是该字段类型的类型零值，也可以正常更改。

>  
 提示：建议在设计数据库表时，字段的值尽量使用非类型零值。 


**自增 id**

在插入数据时，我们可能需要返回自增 id，我们先看一段代码：

```
// 插入数据
example := &amp;Example{
  Title: "PHP",
  View:  90,
}
affected, err := engine.Insert(example)
if err != nil {
  fmt.Printf("Insert err=%v\n", err)
  return
}
fmt.Printf("affected=%v\n", affected)

```

阅读上面这段代码，我们插入一条数据，返回结果是影响行数和错误信息，而不是直接返回该条数据的自增 id。

可能有些读者朋友们会接着使用查询方法，查询最新一条数据的 id，在并发请求数低的场景中，该方法是可以查到新插入数据的自增 id。

但是在并发请求数高的场景中，该方法查到的最新一条数据的 id，未必是我们刚插入的数据的自增 id。

```
id := example.Id
fmt.Printf("affected=%v || id=%d\n", affected, id)

```

阅读上面这段代码，我们想要获取新插入数据的自增 id，直接 `example.Id` 即可获取，但是**前提条件**是结构体中，`id` 字段使用 `xorm:"autoincr"` 标签。

**更新 created 字段**

我们在结构体中，使用标签 `xorm:created` 和 `xorm:updated` 即可自动插入当前时间。

但是，使用 `xorm:created` 标签的字段，只有在第一次插入数据时写入当前时间，此后将不再会更改；使用 `xorm:updated` 标签的字段，在第一次插入数据时写入当前时间，此后每次 Update 操作，时间都会更改。

如果我们的业务需求是需要更改使用 `xorm:created` 标签的字段，可以做到吗？

```
// 更改数据
example := &amp;Example{
  Title: "JavaScript",
  View:  98,
}

condi := &amp;Example{
  Id: 2,
}

affected, err := engine.Update(example, condi)
if err != nil {
  fmt.Printf("Update err=%v\n", err)
  return
}
fmt.Printf("affected=%d\n", affected)

```

阅读上面这段代码，我们发现执行 Update 方法之后，使用 `xorm:updated` 标签的字段的值被更改，而使用 `xorm:created` 标签的字段的值没被更改。

我们换一种更新数据的方式，代码如下：

```
// 更改数据
sql := "UPDATE example SET title=?, view=?, created=? WHERE id=?"
res, err := engine.Exec(sql, "Python", 60, time.Now().Unix(), 2)
if err != nil {
  fmt.Printf("Update err=%v\n", err)
  return
}
affected, err := res.RowsAffected()
if err != nil {
  fmt.Printf("RowsAffected err=%v\n", err)
  return
}
fmt.Printf("affected=%d\n", affected)

```

阅读上面这段代码，我们可以发现使用 Exec 方法执行原生 SQL 可以满足我们的需求。

** 3 **

### 总结

本文我们主要介绍为什么 Go 协程比进程和线程占用的系统资源低，通过进程、线程、协程的 CPU 资源和内存占用的比较，发现无论是在切换时消耗的 CPU 资源（时间片），还是内存占用，Go 协程都有明显优势。

一句话总结就是 Go 协程的切换成本和内存占用比线程和进程都低。

需要注意的是，Go 协程占用系统资源低，并不代表可以无限创建 Go 协程。
