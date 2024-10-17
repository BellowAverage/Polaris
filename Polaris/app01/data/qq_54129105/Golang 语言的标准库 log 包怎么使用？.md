
--- 
title:  Golang 语言的标准库 log 包怎么使用？ 
tags: []
categories: [] 

---
**目录**











**1 **

### 介绍



Golang 语言的标准库中提供了一个简单的 log 日志包，它不仅提供了很多函数，还定义了一个包含很多方法的类型 Logger。但是它也有缺点，比如不支持区分日志级别，不支持日志文件切割等。

**2 **

### 函数



Golang 的 log 包主要提供了以下几个具备输出功能的函数：
-  func Fatal(v ...interface{}) -  func Fatalf(format string, v ...interface{}) -  func Fatalln(v ...interface{}) -  func Panic(v ...interface{}) -  func Panicf(format string, v ...interface{}) -  func Panicln(v ...interface{}) -  func Print(v ...interface{}) -  func Printf(format string, v ...interface{}) -  func Println(v ...interface{}) 
这些函数的使用方法和 fmt 包完全相同，通过查看源码可以发现，`Fatal[ln|f]` 和 `Print[ln|f]` 实际上是调用的 `Print[ln|f]`，而 `Print[ln|f]` 实际上是调用的 `Output()` 函数。

其中 `Fatal[ln|f]` 是调用 `Print[ln|f]` 之后，又调用了 `os.Exit(1)` 退出程序。

其中 `Panic[ln|f]` 是调用 `Panic[ln|f]` 之后，又调用了 `panic()` 函数，抛出一个恐慌。

所以，我们很有必要阅读一下 `Output()` 函数的源码。

函数 `Output()` 的源码：

```
func (l *Logger) Output(calldepth int, s string) error {
 now := time.Now() // get this early.
 var file string
 var line int
 l.mu.Lock()
 defer l.mu.Unlock()
 if l.flag&amp;(Lshortfile|Llongfile) != 0 {
  // Release lock while getting caller info - it's expensive.
  l.mu.Unlock()
  var ok bool
  _, file, line, ok = runtime.Caller(calldepth)
  if !ok {
   file = "???"
   line = 0
  }
  l.mu.Lock()
 }
 l.buf = l.buf[:0]
 l.formatHeader(&amp;l.buf, now, file, line)
 l.buf = append(l.buf, s...)
 if len(s) == 0 || s[len(s)-1] != '\n' {
  l.buf = append(l.buf, '\n')
 }
 _, err := l.out.Write(l.buf)
 return err
}

```

通过阅读 `Output()` 函数的源码，可以发现使用互斥锁来保证多个 goroutine 写日志的安全，并且在调用 `runtime.Caller()` 函数之前，先释放互斥锁，获取到信息后再加上互斥锁来保证安全。

使用 `formatHeader()` 函数来格式化日志的信息，然后保存到 `buf` 中，然后再把日志信息追加到 `buf` 的末尾，然后再通过判断，查看日志是否为空或末尾不是 `\n`，如果是就再把 `\n` 追加到 `buf` 的末尾，最后将日志信息输出。

函数 `Output()` 的源码也比较简单，其中最值得注意的是 `runtime.Caller()` 函数，源码如下：

```
func Caller(skip int) (pc uintptr, file string, line int, ok bool) {
 rpc := make([]uintptr, 1)
 n := callers(skip+1, rpc[:])
 if n &lt; 1 {
  return
 }
 frame, _ := CallersFrames(rpc).Next()
 return frame.PC, frame.File, frame.Line, frame.PC != 0
}

```

通过阅读 `runtime.Caller()` 函数的源码，可以发现它接收一个 `int` 类型的参数 `skip`，该参数表示跳过栈帧数，log 包中的输出功能的函数，使用的默认值都是 `2`，原因是什么？

举例说明，比如在 `main` 函数中调用 `log.Print`，方法调用栈为 `main-&gt;log.Print-&gt;*Logger.Output-&gt;runtime.Caller`，所以此时参数 `skip` 的值为 `2`，表示 `main` 函数中调用 `log.Print` 的源文件和代码行号；

参数值为 `1`，表示 `log.Print` 函数中调用 `*Logger.Output` 的源文件和代码行号；参数值为 `0`，表示 `*Logger.Output` 函数中调用 `runtime.Caller` 的源文件和代码行号。

至此，我们发现 log 包的输出功能的函数，全部都是把信息输出到控制台，那么该怎么将信息输出到文件中呢？

函数 `SetOutPut` 就是用来设置输出目标的，源码如下：

```
func SetOutput(w io.Writer) {
 std.mu.Lock()
 defer std.mu.Unlock()
 std.out = w
}

```

我们可以通过函数 `os.OpenFile` 来打开一个用于 `I/O` 的文件，返回值作为函数 `SetOutput` 的参数。

除此之外，读者应该还发现了一个问题，输出信息都是以日期和时间开头，我们该怎么记录更加丰富的信息呢？比如源文件和行号。

这就用到了函数 `SetFlags`，它可以设置输出的格式，源码如下：

```
func SetFlags(flag int) {
 std.SetFlags(flag)
}

```

参数 `flag` 的值可以是以下任意常量：

```
const (
 Ldate         = 1 &lt;&lt; iota     // the date in the local time zone: 2009/01/23
 Ltime                         // the time in the local time zone: 01:23:23
 Lmicroseconds                 // microsecond resolution: 01:23:23.123123.  assumes Ltime.
 Llongfile                     // full file name and line number: /a/b/c/d.go:23
 Lshortfile                    // final file name element and line number: d.go:23. overrides Llongfile
 LUTC                          // if Ldate or Ltime is set, use UTC rather than the local time zone
 Lmsgprefix                    // move the "prefix" from the beginning of the line to before the message
 LstdFlags     = Ldate | Ltime // initial values for the standard logger
)

```

其中 `Ldate`、`Ltime` 和 `Lmicroseconds` 分别表示日期、时间和微秒，需要注意的是，如果设置 `Lmicroseconds`，那么设置 `Ltime`，也不会生效。

其中 `Llongfile` 和 `Lshortfile` 分别代码绝对路径、源文件名、行号，和代码相对路径、源文件名、行号，需要注意的是，如果设置 `Lshortfile`，那么即使设置 `Llongfile`，也不会生效。

其中 `LUTC` 表示设置时区为 `UTC` 时区。

其中 `LstdFlags` 表示标准记录器的初始值，包含日期和时间。

截止到现在，还缺少点东西，就是日志信息的前缀，比如我们需要区分日志信息为 DEBUG、INFO 和 ERROR。是的，我们还有一个函数 `SetPrefix` 可以实现此功能，源码如下：

```
func SetPrefix(prefix string) {
 std.SetPrefix(prefix)
}

```

函数 `SetPrefix` 接收一个 `string` 类型的参数，用来设置日志信息的前缀。

**3 **

### Logger



log 包定义了一个包含很多方法的类型 Logger。我们通过查看输出功能的函数，发现它们都是调用 `std.Output`，`std` 是什么？我们查看 log 包的源码。

```
type Logger struct {
 mu     sync.Mutex // ensures atomic writes; protects the following fields
 prefix string     // prefix on each line to identify the logger (but see Lmsgprefix)
 flag   int        // properties
 out    io.Writer  // destination for output
 buf    []byte     // for accumulating text to write
}

func New(out io.Writer, prefix string, flag int) *Logger {
 return &amp;Logger{out: out, prefix: prefix, flag: flag}
}

var std = New(os.Stderr, "", LstdFlags)

```

通过阅读源码，我们发现 `std` 实际上是 `Logger` 类型的一个实例，`Output` 是 `Logger` 的一个方法。

`std` 通过 `New` 函数创建，参数分别是 `os.Stderr`、空字符串和 `LstdFlags`，分别表示标准错误输出、空字符串前缀和日期时间。

`Logger` 类型的字段，注释已经说明了，这里就不再赘述了。

自定义 Logger：

```
func main () {
 logFile, err := os.OpenFile("error1.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0755)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer logFile.Close()
 logs := DefinesLogger(logFile, "", log.LstdFlags|log.Lshortfile)
 logs.Debug("message")
 logs.Debugf("%s", "content")
}

// 自定义 logger
type Logger struct {
 definesLogger *log.Logger
}

type Level int8

const(
 LevelDebug Level = iota
 LevelInfo
 LevelError
)

func (l Level) String() string {
 switch l {
 case LevelDebug:
  return " [debug] "
 case LevelInfo:
  return " [info] "
 case LevelError:
  return " [error] "
 }
 return ""
}

func DefinesLogger(w io.Writer, prefix string, flag int) *Logger {
 l := log.New(w, prefix, flag)
 return &amp;Logger{definesLogger: l}
}

func (l *Logger) Debug(v ...interface{}) {
 l.definesLogger.Print(LevelDebug, fmt.Sprint(v...))
}

func (l *Logger) Debugf(format string, v ...interface{}) {
 l.definesLogger.Print(LevelDebug, fmt.Sprintf(format, v...))
}

func (l *Logger) Info(v ...interface{}) {
 l.definesLogger.Print(LevelInfo, fmt.Sprint(v...))
}

func (l *Logger) Infof(format string, v ...interface{}) {
 l.definesLogger.Print(LevelInfo, fmt.Sprintf(format, v...))
}

func (l *Logger) Error(v ...interface{}) {
 l.definesLogger.Print(LevelError, fmt.Sprint(v...))
}

func (l *Logger) Errorf(format string, v ...interface{}) {
 l.definesLogger.Print(LevelError, fmt.Sprintf(format, v...))
}

```

**4 **

### 总结



本文主要介绍 Golang 语言的标准库中的 log 包，包括 log 包的函数和自定义类型 logger 的使用方法和一些细节上的注意事项。开篇也提到了，log 包不支持日志文件的切割，我们需要自己编码去实现，或者使用三方库，比如 `lumberjack`。在生产环境中，一般比较少用 log 包来记录日志，通常会使用三方库来记录日志，比如 `zap` 和 `logrus` 等。

**参考资料：**

https://golang.org/pkg/log/
