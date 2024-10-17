
--- 
title:  静态分析C语言生成函数调用关系的利器——cally和egypt 
tags: []
categories: [] 

---


#### 大纲
- - - - - - <ul><li>- - - - - 


在和中，我们介绍了使用cflow直接分析c语言源码导出调用栈的方法。在做实验的过程中，我一直在思考一个问题：cflow能解释C语言？看了下源码后，发现它的确有解析的模块。大家可以看下它的部分代码。

```
// parser.c
typedef struct {<!-- -->
     char *name;
     int type_end;
     int parmcnt;
     int line;
     enum storage storage;
} Ident;

void parse_declaration(Ident*, int);
void parse_variable_declaration(Ident*, int);
void parse_function_declaration(Ident*, int);
……
static void
print_token(TOKSTK *tokptr)
{<!-- -->
     switch (tokptr-&gt;type) {<!-- -->
     case IDENTIFIER:
     case TYPE:
     case WORD:
     case MODIFIER:
     case STRUCT:
     case PARM_WRAPPER:
     case QUALIFIER:
     case OP:
	  fprintf(stderr, "`%s'", tokptr-&gt;token);
	  break;
     case LBRACE0:
     case LBRACE:
	  fprintf(stderr, "`{'");
	  break;
     case RBRACE0:
     case RBRACE:
	  fprintf(stderr, "`}'");
	  break;
     case EXTERN:
	  fprintf(stderr, "`extern'");
	  break;
     case STATIC:
	  fprintf(stderr, "`static'");
	  break;
     case TYPEDEF:
	  fprintf(stderr, "`typedef'");
	  break;
     case STRING:
	  fprintf(stderr, "\"%s\"", tokptr-&gt;token);
	  break;
     default:
	  fprintf(stderr, "`%c'", tokptr-&gt;type);
     }
}

```

可以发现它是纯纯的文本解析。这就引发了我的一个担忧：如果C语言的编译器对文件的解释和cflow的解释器对同一份文件的结果解析不同怎么办？这个可能性还是存在的。 本文介绍的cally和egypt就很好的避开了这个问题，因为对文件的解析交给了GCC编译器。它们只是对编译器产生的中间结构化内容（Register transfer language）进行解释和整理，这个难度就比解析C语言源码要简单。产出的DOT (graph description language)文件交给dot程序生成调用栈的图。 <img src="https://img-blog.csdnimg.cn/direct/6720d3124e3046d297ff51afa7b4219d.png" alt="在这里插入图片描述"> 我们还是以中的libevent库为例。

## 准备工作

## 安装graphviz

```
sudo apt install graphviz

```

## 安装cally

cally就是一个python脚本，我们只要把工程代码下载下来即可。

```
git clone https://github.com/chaudron/cally.git

```

## 安装egypt

```
wget https://www.gson.org/egypt/download/egypt-1.11.tar.gz .
tar xzf egypt-1.11.tar.gz
rm egypt-1.11.tar.gz
cd egypt-1.11
perl Makefile.PL
make
sudo make install
cd -

```

## 简单分析

我们使用的是libevent库作为示例，就先将其依赖的库安装好。

```
sudo apt-get install libssl-dev

```

否则会报如下错误

>  
 ./bufferevent_openssl.c:36:10: fatal error: openssl/ssl.h: No such file or directory 


### GCC产生RTL（Register transfer language）文件

libevent库中的test-time程序是通过链接编译完的libevent.a和libevent_core.a生成的。现在我们不能依赖原工程中的cmake来生成，需要自己编写编译指令。（还是需要先把整个工程编译一遍，具体见中坑3：缺失编译时产生的文件）。

```
gcc ./test/test-time.c \
 -I./build/include/ -I./include -I./ \
 -L./build/lib/ -Wl,-Bstatic -levent -levent_core -Wl,-Bdynamic \
 -o test-time-main

```

上面的脚本可以正确将test-time.c编译成可执行文件。 现在我们只要让它产出RTL文件即可。

```
gcc ./test/test-time.c \
 -I./build/include/ -I./include -I./ \
 -L./build/lib/ -Wl,-Bstatic -levent -levent_core -Wl,-Bdynamic \
 -fdump-rtl-expand

```

这样就产生了一个名字叫a-test-time.c.245r.expand的RTL文件。

### cally

将上一步生成的文件拷贝到cally.py所在的目录，然后执行

```
python3 ./cally.py a-test-time.c.245r.expand \
 | dot -Grankdir=LR -Tpng -o cally_test_time_call_graph.png

```

<img src="https://img-blog.csdnimg.cn/direct/f0501ae03b72407b87fd7b19a6cf7157.png" alt="请添加图片描述">

### egypt

```
egypt a-test-time.c.245r.expand --include-external \
 |dot -Grankdir=LR -Tpng -o egypt_test_time_call_graph.png

```

<img src="https://img-blog.csdnimg.cn/direct/ba9c8fb4117e4d4a931b87d6a0630d82.png" alt="请添加图片描述">

### 总结

我们看下test-time.c的部分源码。可以看到egypt的展现更加准确，因为它将time_cb和main进行了关联，而cally则没展现出来这层关系。

```
static int
rand_int(int n)
{<!-- -->
	return evutil_weakrand_(&amp;weakrand_state) % n;
}

static void
time_cb(evutil_socket_t fd, short event, void *arg)
{<!-- -->
	struct timeval tv;
	int i, j;

	called++;

	if (called &lt; 10*NEVENT) {<!-- -->
		for (i = 0; i &lt; 10; i++) {<!-- -->
			j = rand_int(NEVENT);
			tv.tv_sec = 0;
			tv.tv_usec = rand_int(50000);
			if (tv.tv_usec % 2 || called &lt; NEVENT)
				evtimer_add(ev[j], &amp;tv);
			else
				evtimer_del(ev[j]);
		}
	}
}

int
main(int argc, char **argv)
{<!-- -->
	struct event_base *base;
	struct timeval tv;
	int i;

#ifdef _WIN32
	WORD wVersionRequested;
	WSADATA wsaData;

	wVersionRequested = MAKEWORD(2, 2);

	(void) WSAStartup(wVersionRequested, &amp;wsaData);
#endif

	evutil_weakrand_seed_(&amp;weakrand_state, 0);

	if (getenv("EVENT_DEBUG_LOGGING_ALL")) {<!-- -->
		event_enable_debug_logging(EVENT_DBG_ALL);
	}

	base = event_base_new();

	for (i = 0; i &lt; NEVENT; i++) {<!-- -->
		ev[i] = evtimer_new(base, time_cb, event_self_cbarg());
		tv.tv_sec = 0;
		tv.tv_usec = rand_int(50000);
		evtimer_add(ev[i], &amp;tv);
	}

	i = event_base_dispatch(base);

	printf("event_base_dispatch=%d, called=%d, EVENT=%d\n",
		i, called, NEVENT);

	if (i == 1 &amp;&amp; called &gt;= NEVENT) {<!-- -->
		return EXIT_SUCCESS;
	} else {<!-- -->
		return EXIT_FAILURE;
	}
}

```

我们看到上面图片并没有展现诸如event_add这类外部函数的底层调用栈。这是因为这些函数是作为静态库提供给test-time进行链接的。且我们并没有生成它们的RTL文件，所以不能分析出完整的调用关系。 为了展现更加具体的调用关系，我们将进行一些改造，以获得更多RTL进行分析。

## 高级分析

上面问题的根源在于test-time编译依赖于静态库，我们首先要解决这个问题，就是要手撸一条可用的编译指令。 这个实验的主要难点也是在这个指令的正确书写，中间修正的过程我就不表了，直接贴出结果。

```
gcc `find . -regextype posix-extended -regex '^./[^/]*\.c$' ! -name 'wepoll.c' ! -name 'win32select.c' ! -name 'evthread_win32.c' ! -name 'buffer_iocp.c' ! -name 'bufferevent_async.c' ! -name 'arc4random.c' ! -name 'event_iocp.c' ! -name 'bufferevent_mbedtls.c'` \
 ./test/test-time.c \
 -I./build/include/ -I./include -I./ \
 -L./build/lib/ -lcrypto -lssl \
 -DLITTLE_ENDIAN -D__clang__ \
 -UD_WIN32 -UDMBEDTLS_SSL_RENEGOTIATION \
 -fdump-rtl-expand

```

这样我们得到一堆RTL文件。这些文件我都将其拷贝到cally和egypt测试工程的sample目录下。

### cally

```
python3 ./cally.py ../sample/*.expand --caller main |  dot -Grankdir=LR -Tsvg -o cally_full_test_time_call_graph.svg

```

生成文件非常大，就不展示了。（见） 只展示event_add函数的调用栈。 <img src="https://img-blog.csdnimg.cn/direct/35109eb9df7a4a74a2c4277ed4fe395a.png" alt="在这里插入图片描述">

### egypt

```
egypt sample/*.expand --include-external --callees main |  dot -Grankdir=LR -Tsvg -o egypt_full_test_time_call_graph.svg

```

生成文件非常大，就不展示了。（见） 只展示event_add函数的调用栈。 <img src="https://img-blog.csdnimg.cn/direct/4c1e5b300ea74fb897c6396b4f084dd9.png" alt="在这里插入图片描述">

## 总结

egypt比cally优秀，可以分析出更加复杂的调用关系。

## 参考资料
- - - - 