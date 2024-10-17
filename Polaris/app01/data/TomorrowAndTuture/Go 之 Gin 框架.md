
--- 
title:  Go 之 Gin 框架 
tags: []
categories: [] 

---
Gin 是一个 Go (Golang) 编写的轻量级 web 框架，运行速度非常快，擅长 Api 接口的高并发，如果项目的规模不大，业务相对简单，这个时候我们也推荐您使用 Gin，是 Go 实现微服务的利器。

我自己也是Go开发方面的菜鸟，额外的就不多废话了。

### 简单路由配置

```
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// 创建一个默认的路由引擎
	r := gin.Default()
	// 配置路由
	r.GET("/", func(c *gin.Context) {
		aid := c.Query("aid")
		c.JSON(200, gin.H{
			"username": "name1",
			"aid": aid,
			"data": []string{"hello", "world"},
		})
	})
	// 启动 HTTP 服务，默认在 0.0.0.0:8080 启动服务
	r.Run()
}
```

运行起来以后，在浏览器输入，即可获取到 url 请求的结果

```
{"aid":"xyz","data":["hello","world"],"username":"name1"}
```

### 动态路由

所谓动态路由，其实就是将传参作为 url 的一部分，这样的话，url 就不再是固定不变的，而是随着传参的变化而变化，像 Ruby 等其他语言也有类似的用法。

```
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/user/:id", func(c *gin.Context) {
		id := c.Param("id")
		c.JSON(200, gin.H{
			"username": "name1",
			"id": id,
			"data": []string{"hello", "world"},
		})
	})
	r.Run()
}

```

请求 url：

请求 result：

```
{"data":["hello","world"],"id":"looking","username":"name1"}
```

### 结果响应

#### c.String()

```
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/news", func(c *gin.Context) {
		c.String(200, "Hello world")
	})
	r.Run()
}

```

#### c.JSON()

大部分时候，我们直接返回 json 的数据格式要更多一些。数据返回我们可以使用 gin.H 的 map 形式，也可以直接用 struct 的形式，不过使用结构体的话，记得要给字段标注好 json 对应的 tag，方便直接将结构体实例解析成对应的 json 数据。

```
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/structJson", func(c *gin.Context) {
		// 结构体方式
		var msg struct {
			Username string `json:"username"`
			Msg string `json:"msg"`
			Age string `json:"age"`
		}
		msg.Username = "name1"
		msg.Msg = "msg1"
		msg.Age = "18"
		c.JSON(200, msg)
	})
	r.Run()
}
```

#### c.JSONP()

这个暂时用的比较少

```
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()
	r.GET("/JSONP", func(c *gin.Context) {
		data := map[string]interface{}{
			"foo": "bar",
		}
		c.JSONP(http.StatusOK, data)
	})
	r.Run()
}

```

请求 url：

请求 result：

```
x({"foo":"bar"});
```

#### c.HTML()

templates/index.html

```
&lt;!DOCTYPE  html&gt;
&lt;html  lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;这是一个 html 模板&lt;/h1&gt;

&lt;h3&gt;{<!-- -->{.title}}&lt;/h3&gt;
&lt;/body&gt;
&lt;/html&gt;

```

渲染之前，先对文件进行 load 加载，框架会自动将变量替换到 html 文件里进行渲染 

```
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	r.LoadHTMLFiles("./templates/index.html")
	r.GET("/index", func(c *gin.Context) {
		c.HTML(
			http.StatusOK, "index.html",
			map[string]interface{}{"title": "前台首页"})
	})

	r.Run()
}

```



<img alt="" height="176" src="https://img-blog.csdnimg.cn/direct/229804706b5b49a69909046bdf4725f3.png" width="547">

### 请求传值

get查询和动态路由前面已经有示例了，我们看下其他类型的传值。

#### post获取表单数据

```
package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	r.POST("/doAddUser", func(c *gin.Context) {
		username := c.PostForm("username")
		password := c.PostForm("password")
		age := c.DefaultPostForm("age", "20")
		c.JSON(200, gin.H{
			"usernmae": username, "password": password, "age": age,
		})
	})
	r.Run()
}

```

#### post/get传值绑定到结构体

**传值绑定结构体估计是我们正常开发时最常用的参数解析方式之一了（至少我周围同事大部分都用这种形式传值）**

```
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type Userinfo struct {
	Username string `form:"username" json:"user"`
	Password string `form:"password" json:"password"`
}

func main() {
	r := gin.Default()

	r.GET("/", func(c *gin.Context) {
		var userinfo Userinfo
		if err := c.ShouldBind(&amp;userinfo); err == nil {
			fmt.Printf("userinfo: %+v\n", userinfo) // userinfo: {Username:zhangsan Password:123456}
			c.JSON(http.StatusOK, userinfo)
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		}
	})

	r.Run()
}

```



```
{"user":"zhangsan","password":"123456"}
```

同理，POST请求等也可以将请求参数绑定到结构体中

```
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

type Userinfo struct {
	Username string `form:"username" json:"user"`
	Password string `form:"password" json:"password"`
}

func main() {
	r := gin.Default()

	r.POST("/doLogin", func(c *gin.Context) {
		var userinfo Userinfo
		if err := c.ShouldBind(&amp;userinfo); err == nil {
			c.JSON(http.StatusOK, userinfo)
		} else {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		}
	})

	r.Run()
}

```

#### post获取xml数据

一般请求传递 xml 格式数据的遇到的不多，不过也可以试试。

```
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type Article struct {
	Title   string `json:"title" xml:"title"`
	Content string `json:"content" xml:"content"`
}

func main() {
	r := gin.Default()

	r.POST("/xml", func(ctx *gin.Context) {
		var article Article
		if err := ctx.ShouldBindXML(&amp;article); err == nil {
			fmt.Printf("article: %+v\n", article)
			ctx.JSON(http.StatusOK, article)
		}else {
			ctx.JSON(http.StatusBadRequest, gin.H {
				"err": err.Error()})
		}
	})

	r.Run()
}

```

可以使用 Apifox 发送请求尝试，可以直观看到接口返回的结果

<img alt="" height="786" src="https://img-blog.csdnimg.cn/direct/c2a767b2fc4c498faeb3dc3550c2b83c.png" width="1200">

### 路由分组

路由分组即将相关的路由加上相同的前缀，用以和其他路由进行区分和辨别（我自己理解是这样，分组依据一般可以按照业务等进行划分）。

```
package main

import (
	"github.com/gin-gonic/gin"
)

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", func(ctx *gin.Context) {
			ctx.String(200, "api")
		})

		apiRouter.GET("articles", func(ctx *gin.Context) {
			ctx.String(200, "/api/articles")
		})
	}
}

func main() {
	r := gin.Default()
	ApiRouter(r)

	r.Run()
}
```

### 路由分离

路由分离可以将不相关的路由解耦，分离到单独的文件进行维护。

在项目新建文件夹 `router`, 然后在`router`目录下创建`apiRouter.go` 和`adminRouter.go`

`router/apiRouter.go`

```
package router
// apiRouter.go
import "github.com/gin-gonic/gin"

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", func(ctx *gin.Context) {
			ctx.String(200, "api")
		})

		apiRouter.GET("articles", func(ctx *gin.Context) {
			ctx.String(200, "/api/articles")
		})
	}
}

```

`router/apiAdmin.go` 

```
package router

// adminRouter.go
import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func AdminRouter(r *gin.Engine) {
	adminRouter := r.Group("/admin")
	{
		adminRouter.GET("/", func(ctx *gin.Context) {
			ctx.String(200, "admin")
		})

		adminRouter.GET("list", func(ctx *gin.Context) {
			ctx.String(http.StatusOK, "admin/list")
		})
	}
}

```

然后在 `main.go `中引入路由模块并使用即可（在真实的开发中，main.go 中的内容其实很少，一般只是一个启动整个服务的入口）

```
package main

import (
	"github.com/gin-gonic/gin"

	"github.com/test/router"
)


func main() {
	// 创建一个默认的路由引擎
	r := gin.Default()
	// 引入路由模块
	router.AdminRouter(r)
	router.ApiRouter(r)
	// 启动 HTTP 服务，默认在 0.0.0.0:8080 启动服务
	r.Run()
}

```

### 自定义控制器

当我们的项目比较大的时候有必要对我们的控制器进行分组 , 业务逻辑放在控制器中（**有时候我们习惯把业务逻辑处理部分所在的包称为 handler**）。

新建 controller/api/userController.go

```
package api

import "github.com/gin-gonic/gin"

func UserIndex(c *gin.Context) {
	c.String(200, "api UserIndex")
}

func UserAdd(c *gin.Context)  {
	c.String(200, "api UserAdd")
}

func UserList(c *gin.Context) {
	c.String(200, "api UserList")
}
func UserUpdate(c *gin.Context) {
	c.String(200, "api UserUpdate")
}

func UserDelete(c *gin.Context) {
	c.String(200, "api UserDelete")
}

```

router/apiRouter.go

```
package router
// apiRouter.go
import (
	"github.com/gin-gonic/gin"
	"github.com/test/controller/api"
)

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/")

		apiRouter.GET("/users", api.UserIndex)
		apiRouter.GET("/users/:id", api.UserList)
		apiRouter.POST("/users", api.UserAdd)
		apiRouter.PUT("/users/:id", api.UserUpdate)
		apiRouter.DELETE("/users", api.UserDelete)

	}
}
```

### 控制器继承

要让控制器可以继承，最好将控制器做成方法的形式（一般默认是函数的形式），这样的话，就可以根据结构体的匿名字段，实现对继承结构体的方法进行很方便的调用。

controller/api/baseController.go

```
package api

import "github.com/gin-gonic/gin"

type BaseController struct {
}

func (con BaseController) Success(c *gin.Context) {
	c.String(200, "success")
}

func (con BaseController) Error(c *gin.Context) {
	c.String(200, "failed")
}

```

controller/api/userController.go

```
package api

import "github.com/gin-gonic/gin"

type UserController struct {
	BaseController
}

func (con UserController) UserIndex(c *gin.Context) {
	// c.String(200, "api UserIndex")
	con.Success(c)
}

func (con UserController) UserAdd(c *gin.Context) {
	c.String(200, "api UserAdd")
}

func (con UserController) UserList(c *gin.Context) {
	c.String(200, "api UserList")
}
func (con UserController) UserUpdate(c *gin.Context) {
	c.String(200, "api UserUpdate")
}

func (con UserController) UserDelete(c *gin.Context) {
	c.String(200, "api UserDelete")
}

```

apiRouter.go

```
package router
// apiRouter.go
import (
	"github.com/gin-gonic/gin"
	"github.com/test/controller/api"
)

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/")

		apiRouter.GET("/index", api.UserController{}.UserIndex)
		apiRouter.GET("/users", api.UserController{}.UserList)
		apiRouter.GET("/users/:id", api.UserController{}.UserList)
		apiRouter.POST("/users", api.UserController{}.UserAdd)
		apiRouter.PUT("/users/:id", api.UserController{}.UserUpdate)
		apiRouter.DELETE("/users", api.UserController{}.UserDelete)

	}
}

```

### Gin中间件

Gin的中间件之前没特别注意过，看了下面的解释后，**其实和 Python 的装饰器的作用比较类似。**

Gin 框架允许开发者在处理请求的过程中，加入用户自己的钩子（Hook）函数。这个钩子函数就叫中间件，中间件适合处理一些公共的业务逻辑，比如登录认证、权限校验、数据分页、 记录日志、耗时统计等 通俗的讲：中间件就是匹配路由前和匹配路由完成后执行的一系列操作。

#### 路由中间件

Gin 中的中间件必须是一个 gin.HandlerFunc 类型，配置路由的时候可以传递多个 func 回调函数。中间件要放在最后一个回调函数的前面 ，触发的方法都可以称为中间件。

函数类型这个可以理解，以 GET 为例，后面虽然是可变参数，但传参类型其实已经定了。只不过常规来说，我们一般可能只加了一个 HandlerFunc 处理函数而已。

```
// GET is a shortcut for router.Handle("GET", path, handle).
func (group *RouterGroup) GET(relativePath string, handlers ...HandlerFunc) IRoutes {
	return group.handle(http.MethodGet, relativePath, handlers)
}
```

##### **c.Next()**

**c.Next() 调用该请求的剩余处理程序**

中间件里面加上 c.Next()后，c.Next() 的语句后面先不执行，跳转到后面的中间件和回调函数中执行完后，才执行 c.Next() 后面的语句，比如我们可以利用这个特性统计一个请求的执行时间。

```
package router

// apiRouter.go
import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
)

// 中间件函数
func InitMiddleWare(c *gin.Context) {
	fmt.Println("1- init middle ware")
	start := time.Now()
	c.Next()
	end := time.Now()
	fmt.Println("3- program execute done, calculate time")
	fmt.Println("total cost time:", end.Sub(start))
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", InitMiddleWare, func(context *gin.Context) {
			time.Sleep(2 * time.Second)
			fmt.Println("2- middle ware")
			context.String(200, "api UserIndex")
		})
	}
}

```

查看服务端的打印，用以了解中间件中程序的执行顺序。

```
1- init middle ware
2- middle ware
3- program execute done, calculate time
total cost time: 2.0006141s
```

##### **多个中间件执行**

这个原理有点像 Ruby 中 yield 的用法，简单来说其实就是一个嵌套调用，可以想象成 c.Next() 就是后续所有中间件和回调函数的调用过程。

```
package router

// apiRouter.go
import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
)

// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	c.Next()
	fmt.Println("1- init middle ware end")
}

func InitMiddleWareTwo(c *gin.Context) {
	fmt.Println("2- init middle ware start")
	c.Next()
	fmt.Println("2- init middle ware end")
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", InitMiddleWareOne, InitMiddleWareTwo, func(context *gin.Context) {
			time.Sleep(2 * time.Second)
			fmt.Println("Home page")
			context.String(200, "api UserIndex")
		})
	}
}

```

```
1- init middle ware start
2- init middle ware start
Home page
2- init middle ware end
1- init middle ware end
```

##### ctx.Abort()

ctx.Abort()表示终止调用该请求的剩余处理程序（包括后续的中间件和回调函数）

```
package router

// apiRouter.go
import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
)

// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	c.Next()
	fmt.Println("1- init middle ware end")
}

func InitMiddleWareTwo(c *gin.Context) {
	fmt.Println("2- init middle ware start")
	// c.Next()
	c.Abort()
	fmt.Println("2- init middle ware end")
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", InitMiddleWareOne, InitMiddleWareTwo, func(context *gin.Context) {
			time.Sleep(2 * time.Second)
			fmt.Println("Home page")
			context.String(200, "api UserIndex")
		})
	}
}

```

```
1- init middle ware start
2- init middle ware start
2- init middle ware end
1- init middle ware end
```

我们可能在想，如果我既不调用 c.Next() ，也不调用 c.Abort() 的话会发生什么呢？

```
package router

// apiRouter.go
import (
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
)

// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	c.Next()
	fmt.Println("1- init middle ware end")
}

func InitMiddleWareTwo(c *gin.Context) {
	fmt.Println("2- init middle ware start")
	// c.Next()
	// c.Abort()
	fmt.Println("2- init middle ware end")
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	{
		apiRouter.GET("/", InitMiddleWareOne, InitMiddleWareTwo, func(context *gin.Context) {
			time.Sleep(2 * time.Second)
			fmt.Println("Home page")
			context.String(200, "api UserIndex")
		})
	}
}

```

可以看到，如果没有调用 c.Abort() ，后续中间件和回调函数还是会按照顺序依次调用。

```
1- init middle ware start
2- init middle ware start
2- init middle ware end
Home page
1- init middle ware end
```

#### 全局中间件

全局中间件当然也属于中间件范畴的，只不过有个全局的作用。如果需要每个路由都加上相同的中间件，使用全局中间件就省去了在每个路由的地方都去加上中间件的繁琐过程了。

```
package router

// apiRouter.go
import (
	"fmt"
	"github.com/gin-gonic/gin"
)

// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	fmt.Println("1- init middle ware end")
}

func InitMiddleWareTwo(c *gin.Context) {
	fmt.Println("2- init middle ware start")
	fmt.Println("2- init middle ware end")
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")
	apiRouter.Use(InitMiddleWareOne, InitMiddleWareTwo)

	{
		apiRouter.GET("/", func(context *gin.Context) {
			fmt.Println("Home page")
			context.String(200, "api Index")
		})

		apiRouter.GET("/users", func(context *gin.Context) {
			fmt.Println("Users page")
			context.String(200, "api Users")
		})
	}
}

```

#### 默认中间件

其实我们去看源码的话，还会发现默认的 Default 引擎，其实也使用了全局中间件。 



```
// Default returns an Engine instance with the Logger and Recovery middleware already attached.
func Default() *Engine {
	debugPrintWARNINGDefault()
	engine := New()
	engine.Use(Logger(), Recovery())
	return engine
}
```
- Logger 中间件将日志写入gin.DefaultWriter- Recovery 中间件会 recover 任何 panic，如果有 panic 的话，为写入500响应码- 如果不想使用上面的默认中间件，可以使用 gin.New() 新建一个没有任何中间件的路由 
#### 中间件和对应控制器数据共享

可以使用 c.Set() 和 c.Get() 传递数据，毕竟对于 Gin 来说，上下文变量 context 基本上都会一直往下传递的（主要是包含的东西太多了，除非你确定后续不会用 context 相关的东西了，否则也不敢乱丢啊）。

router/apiRouter.go

```
package router

// apiRouter.go
import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/test/controller/api"
)

// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	c.Set("username", "Looking")
	fmt.Println("1- init middle ware end")
}

func ApiRouter(r *gin.Engine) {
	apiRouter := r.Group("/api")

	{
		apiRouter.GET("/", InitMiddleWareOne, api.UserController{}.UserIndex)
	}
}

```

controller/api/userController.go 

```
package api

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

type UserController struct {
	BaseController
}

func (con UserController) UserIndex(c *gin.Context) {
	userName, ok := c.Get("username")
	if ok {
		fmt.Println("controller get username: ", userName)
	}
	c.JSON(200, gin.H{
		"username": userName,
	})
}
```

#### gin中间件中使用goroutine

**当在中间件或 handler 中启动新的 goroutine 时，不能使用原始的上下文(`c *gin.Context`)，必须使用其只读副本(`c.Copy()`)。这也算一种规范性要求了吧。**

其实从语法上来说，直接使用原来的 context 没任何问题。但是可能会导致额外的难以发现的 bug，具体这么做的原因可以参考这个链接（隐式约束、包括锁争用、动态作用域等）：

比如我们常见的With系列函数（WithCancel、WithTimeout 等），其也是生成的 context 的副本然后再进行操作。 

```
// 中间件函数
func InitMiddleWareOne(c *gin.Context) {
	fmt.Println("1- init middle ware start")
	c.Set("username", "Looking")
	// 定义一个goroutine统计日志
	cCp := c.Copy()
	go func ()  {
		time.Sleep(2 * time.Second)
		fmt.Println("Done in path " + cCp.Request.URL.Path)
	}()
	fmt.Println("1- init middle ware end")
}
```

### Gin中的Cookie

#### Cookie 设置

c.SetCookie(name, value string, maxAge int, path, domain string, secure, httpOnly bool)
- 第一个参数key- 第二个参数value- 第三个参数过期时间. 如果只想设置 Cookie 的保存路径而不想设置存活时间，可以在第三个参数中传递 nil- 第四个参数 cookie 的路径- 第五个参数 cookie 的路径 Domain 作用域本地调试配置成 localhost 或 127.0.0.1 , 正式上线配置成真正的域名- 第六个参数是 secure ，当 secure 值为 true 时，cookie 在HTTP 中是无效，在HTTPS 中才有效- 第七个参数 httpOnly，如果在COOKIE 中设置了 httpOnly 属性，则通过程序（JS 脚本、applet 等）将无法读取到 COOKIE 信息，防止XSS 攻击产生
```
package router

// apiRouter.go
import (
	"fmt"
	"github.com/gin-gonic/gin"
)


func ApiRouter(r *gin.Engine) {

	apiRouter := r.Group("/api")

	{
		apiRouter.GET("/", func(ctx *gin.Context) {
			// 设置Cookie
			ctx.SetCookie("username", "张三", 3600, "/", "127.0.0.1", false, false)
			fmt.Println("首页")
			ctx.String(200, "/api")
		})

		apiRouter.GET("/news", func(ctx *gin.Context) {
			// 获取Cookie
			username, _ := ctx.Cookie("username")
			fmt.Println(username)
			ctx.String(200, "/news/"+username)
		})
	}
}

```

运行后，先请求 /api 接口触发 Cookie 设置，再请求 /api/news 获取设置的 Cookie。

<img alt="" height="114" src="https://img-blog.csdnimg.cn/direct/94509405b27a4b948f1b4ac08b73bd45.png" width="791">

从浏览器的请求中也可以看到设置的 Cookie， 

<img alt="" height="524" src="https://img-blog.csdnimg.cn/direct/e9ef119c71834fa2947525cb2bb7e505.png" width="775">

 当然，浏览器中的 Cookie 是经过转义后存储的，可以通过其他工具去掉转义后再进行对比。

<img alt="" height="80" src="https://img-blog.csdnimg.cn/direct/1f2f4be346fe45af8dfe2ee3aadb52b5.png" width="529">

#### Cookie 获取

```
cookie, err := c.Cookie("name")
```

#### Cookie 删除
- 把第三个参数时间设置为 `-1 。也就是将有效期设置为一个负数即可。`
<img alt="" height="304" src="https://img-blog.csdnimg.cn/direct/1f818666cd4149d48d6e6eab7822f0a4.png" width="864">

### Gin中使用 gorm

gorm的部分在另外一篇博客有介绍，这块就不多写了：

### 非Gin实现

当然，也可以不使用 Gin 来实现 Http 服务，但这个在我们讨论话题之外了。

```
package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Server is running on port 8080...")
	http.ListenAndServe(":8080", nil)
}

func handler(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case "GET":
		fmt.Fprintf(w, "GET request success!")
	case "POST":
		err := r.ParseForm()
		if err != nil {
			http.Error(w, "Failed to parse form", http.StatusBadRequest)
			return
		}

		formData := r.PostForm

		fmt.Fprintf(w, "POST request success! data: %+v", formData)
	default:
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
	}
}

```

GET

POST

<img alt="" height="641" src="https://img-blog.csdnimg.cn/direct/dc4aebece52c48ba9c61be275b9eeb35.png" width="1200">

PUT

<img alt="" height="657" src="https://img-blog.csdnimg.cn/direct/04bf382fedc94c529831636d24df77d5.png" width="1200"> 
