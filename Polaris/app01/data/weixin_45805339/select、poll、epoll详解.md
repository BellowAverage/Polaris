
--- 
title:  select、poll、epoll详解 
tags: []
categories: [] 

---
### 1.IO读写基本原理

>  
 用户程序进行IO操作实际依赖于linux系统内核read()、write()函数 read()函数的调用并不是直接从网卡把数据读取到用户内存中，而是把内核缓冲区中的数据复制到用户缓冲区中 write()函数的调用也并不是直接把数据写入网卡中，而是把用户缓冲区的数据写入到内核缓冲区中 网卡与内核缓冲区数据的读写则是由操作系统内核完成 


<img src="https://img-blog.csdnimg.cn/5b39cdf7251b4ec58e3a507ad5d287ed.png" alt="在这里插入图片描述">

### 2.阻塞IO和非阻塞IO

>  
 网卡同步数据到内核缓冲区，如果内核缓冲区中的数据未准备好，用户进程发起read操作，阻塞则会一直等待内存缓冲区数据完整后再解除阻塞，而非阻塞则会立即返回不会等待 而内核缓冲区与用户缓冲区之间的读写操作肯定是阻塞的 


### 3.同步和异步

>  
 同步：调用者主动发起请求，调用者主动等待这个结果返回，一但调用就必须有返回值 异步：调用发出后直接返回，所以没有返回结果。被调用者处理完成后通知回调、通知等机制来通知调用者 


### 4.同步阻塞IO

<img src="https://img-blog.csdnimg.cn/eca988e49f3c41edb5e301ea15864742.png" alt="在这里插入图片描述"> **读取数据流程：**
- 用户进程调用read()系统函数，用户进程进入阻塞状态- 系统内核收到read()系统调用，网卡开始准备接收数据，在一开始内核缓冲区数据为空，内核在等待接收数据，用户进程同步阻塞等待- 内核缓冲区中有完整的数据后，内核会将内核缓冲区中的数据复制到用户缓冲区- 直到用户缓冲区中有数据，用户进程才能解除阻塞状态继续执行
#### 4.1同步阻塞IO底层实现

```
// 创建socket
int listenfd = socket(AF_INET, SOCK_STREAM, 0);
// 绑定
bind(listenfd, (struct sockaddr*)&amp;my_addr, sizeof(my_addr));
// 监听
listen(listenfd, 5);
// 接受客户端连接
int socketFd = accept(listenfd, (struct sockaddr*) &amp;clientaddr, &amp;clientaddrlen) 

// 接收客户端数据
recv(socketFd, buf, 256, 0); 

```

#### 4.2同步阻塞IO的优缺点

**优点：**
- 开发简单，由于accept()、recv()都是阻塞的，为了服务于多个客户端请求，新的连接创建一个线程去处理即可- 阻塞的时候，线程挂起，不消耗CPU资源
**缺点：**
- 每新来一个IO请求，都需要新建一个线程对应，高并发下系统开销大，多线程上下文切换频繁- 创建线程太多，内存消耗大
**同步阻塞IO缺点带来的思考**

>  
 因为accept()、recv()函数都是阻塞的，如果系统想要支持多个IO请求，就创建更多的线程，如果去解决这个问题呢？ 如果可以把accept、recv函数变成非阻塞的方式，是不是就可以避免创建多个线程了？这就引入了我们的同步非阻塞IO 


### 5.同步非阻塞IO

<img src="https://img-blog.csdnimg.cn/9126c4a26b89420b836a0045f61ca2e8.png" alt="在这里插入图片描述"> **读取数据流程：**
- 用户进程发起请求调用read()函数，系统内核收到read()系统调用，网卡开始准备接收数据- 内核缓冲区数据没有准备好，请求立即返回，用户进程不断的重试查询内核缓冲区数据有没有准备好- 当内核缓冲区数据准备好了之后，用户进程阻塞，内核开始将内核缓冲区数据复制到用户缓冲区- 复制完成后，用户进程解除阻塞，读取数据继续执行
#### 5.1 同步非阻塞IO底层实现

```
// 创建socket
int listenfd = socket(AF_INET, SOCK_STREAM, 0);
// 绑定
bind(listenfd, (struct sockaddr*)&amp;my_addr, sizeof(my_addr));
// 监听
listen(listenfd, 5);
// 设置为非阻塞
ioctl(listenfd, FIONBIO, 1);
// 接受客户端连接
int socketFd = accept(listenfd, (struct sockaddr*) &amp;clientaddr, &amp;clientaddrlen);
// 设置为非阻塞
ioctl(socketFd, FIONBIO, 1);
while (1) {<!-- -->
    int fd;
    // 循环遍历
    for (fd : fds) {<!-- -->
        // 接收客户端数据
		recv(fd, buf, 256, 0); 
    }
}

```

#### 5.2 同步非阻塞IO的优缺点

**优点：**
- 非阻塞， accept()、recv()均不阻塞，用户线程立即返回- 规避了同步阻塞模式的多线程问题
**缺点：**
- 假如现在有1万个客户端连接，但只有1个客户端发送数据过来，为了获取这个1个客户端发送的消息，我需要循环向内核发送1万遍recv()系统调用，而这其中有9999次是无效的请求，浪费CPU资源
**同步非阻塞IO缺点带来的思考**

>  
 针对同步非阻塞IO的缺点，设想如果内核提供一个方法，可以一次性把1万个客户端socket连接传入，在内核中去遍历，如果没有数据这个方法就一直阻塞，一但有数据这个方法解除阻塞并把所有有数据的socket返回，把这个遍历的过程交给内核去处理，是不是就可以避免空跑，避免1万次用户态到内核态的切换呢？ 


### 6.IO多路复用模型

<img src="https://img-blog.csdnimg.cn/0b074e306eb74a679743913db651bfb3.png" alt="在这里插入图片描述">

#### 6.1 什么是IO多路复用？

>  
 一个线程监测多个IO操作 


#### 6.2 IO多路复用实现原理

>  
 IO多路复用模型是建立在内核提供的多路分离函数select基础之上的，使用select函数可以避免同步非阻塞IO模型中轮询等待的问题，即一次性将N个客户端socket连接传入内核然后阻塞，交由内核去轮询，当某一个或多个socket连接有事件发生时，解除阻塞并返回事件列表，用户进程在循环遍历处理有事件的socket连接。这样就避免了多次调用recv()系统调用，避免了用户态到内核态的切换。 


### 7.IO多路复用的三种实现

#### 7.1 select

##### 7.1.1 select函数

>  
 select函数仅仅知道有几个I/O事件发生了，但并不知道具体是哪几个socket连接有I/O事件，还需要轮询去查找，时间复杂度为O(n)，处理的请求数越多，所消耗的时间越长。 


##### 7.1.2 select函数执行流程
- 从用户空间拷贝fd_set（注册的事件集合）到内核空间- 遍历所有fd文件，并将当前进程挂到每个fd的等待队列中，当某个fd文件设备收到消息后，会唤醒设备等待队列上睡眠的进程，那么当前进程就会被唤醒- 如果遍历完所有的fd没有I/O事件，则当前进程进入睡眠，当有某个fd文件有I/O事件或当前进程睡眠超时后，当前进程重新唤醒再次遍历所有fd文件
##### 7.1.3 select函数接口定义

```
#include &lt;sys/select.h&gt;
#include &lt;sys/time.h&gt;

// 最大支持1024个连接
#define FD_SETSIZE 1024
#define NFDBITS (8 * sizeof(unsigned long))
#define __FDSET_LONGS (FD_SETSIZE/NFDBITS)

/**
* 数据结构 (bitmap)
* fd_set保存了相关的socket事件
*/
typedef struct {<!-- -->
    unsigned long fds_bits[__FDSET_LONGS];
} fd_set;

/**
* select是一个阻塞函数
*/
// 返回值就绪描述符的数目
int select(
    int max_fd,  // 最大的文件描述符值，遍历时取0-max_fd
    fd_set *readset,  // 读事件列表
    fd_set *writeset,  // 写事件列表
    fd_set *exceptset,  // 异常列表
    struct timeval *timeout  // 阻塞超时时间
)

FD_ZERO(int fd, fd_set* fds)   // 清空集合
FD_SET(int fd, fd_set* fds)    // 将给定的描述符加入集合
FD_ISSET(int fd, fd_set* fds)  // 判断指定描述符是否在集合中 
FD_CLR(int fd, fd_set* fds)    // 将给定的描述符从文件中删除  

```

##### 7.1.4 select使用示例

```
#include&lt;stdio.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;						
#include &lt;unistd.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;arpa/inet.h&gt;	

void server() {<!-- -->
	
	// 创建socket连接
	int lfd = socket(AF_INET,SOCK_STREAM,0);
	struct sockaddr_in my_addr; 
	bzero(&amp;my_addr, sizeof(my_addr));
	my_addr.sin_family = AF_INET; // ipv4
	my_addr.sin_port   = htons(9090);
	my_addr.sin_addr.s_addr = htonl(INADDR_ANY); 
	// 绑定端口
	bind(lfd, (struct sockaddr*)&amp;my_addr, sizeof(my_addr));
	// 监听连接请求
	listen(lfd, 128);
	printf("listen client @port=%d...\n", 9090);
	int lastfd = lfd;
	// 定义文件描述符集
	fd_set read_fd_set, all_fd_set;
	// 服务socket描述符加入set集合中
	FD_ZERO(&amp;all_fd_set);
	FD_SET(lfd, &amp;all_fd_set);
	printf("准备进入while循环\n");
	while (1) {<!-- -->
		read_fd_set = all_fd_set;
		printf("阻塞中... lastfd=%d\n", lastfd);
		int nready = select(lastfd+1, &amp;read_fd_set, NULL, NULL, NULL);
		switch (nready) {<!-- -->
			case 0 :
				printf("select time out ......\n");
				break;
			case -1 :
				perror("select error \n");
				break;
			default:
				// 监听到新的客户端连接
				if (FD_ISSET(lfd, &amp;read_fd_set)) {<!-- -->
					struct sockaddr_in client_addr;	
					socklen_t cliaddr_len = sizeof(client_addr);
					char cli_ip[INET_ADDRSTRLEN] = "";	
					// 肯定有连接不会阻塞
					int clientfd = accept(lfd, (struct sockaddr*)&amp;client_addr, &amp;cliaddr_len);
					inet_ntop(AF_INET, &amp;client_addr.sin_addr, cli_ip, INET_ADDRSTRLEN);
					printf("----------------------------------------------\n");
					printf("client ip=%s,port=%d\n", cli_ip, ntohs(client_addr.sin_port));
					// 将clientfd加入读集合
					FD_SET(clientfd, &amp;all_fd_set);	
					lastfd = clientfd;
					if(0 == --nready) {<!-- -->
						continue;
					}
				}
				int i;
				for (i = lfd + 1;i &lt;= lastfd; i++) {<!-- -->
					// 处理读事件
					if (FD_ISSET(i, &amp;read_fd_set)) {<!-- -->
						char recv_buf[512] = "";
						int rs = read(i, recv_buf, sizeof(recv_buf));
						if (rs == 0 ) {<!-- -->
							close(i);
							FD_CLR(i, &amp;all_fd_set);
						} else {<!-- -->
							printf("%s\n",recv_buf);
							// 给每一个服务端写数据
							int j;
							for (j = lfd + 1;j &lt;= lastfd; j++) {<!-- -->
								if (j != i) {<!-- -->
									write(j, recv_buf, strlen(recv_buf));
								}
							}
						}
					}
				}
		}
		
	}
}

int main(){<!-- -->
	server();
	return 0;
}

```

##### 7.1.5 select函数的缺点
- 单个进程所打开的FD是有限制的，通过 FD_SETSIZE 设置，默认1024- 每次调用 select，都需要把 fd 集合从用户态拷贝到内核态，这个开销在 fd 很多时会很大- 每次调用select都需要将进程加入到所有监视socket的等待队列，每次唤醒都需要从每个队列中移除- select函数在每次调用之前都要对参数进行重新设定，这样做比较麻烦，而且会降低性能- 进程被唤醒后，程序并不知道哪些socket收到数据，还需要遍历一次
#### 7.2 poll

>  
 poll本质上和select没有区别，它将用户传入的数组拷贝到内核空间，然后查询每个fd对应的设备状态， 但是它没有最大连接数的限制，原因是它是基于链表来存储的 


##### 7.2.1 poll函数接口

```
#include &lt;poll.h&gt;
// 数据结构
struct pollfd {<!-- -->
    int fd;                         // 需要监视的文件描述符
    short events;                   // 需要内核监视的事件
    short revents;                  // 实际发生的事件，1：表示有事件发生，0：没有事件发生
};

// 阻塞方法
int poll(struct pollfd fds[],   // 需要监听的文件描述符列表
         nfds_t nfds,           // 文件描述符个数
         int timeout            // 超时时间
        );

```

##### 7.2.2 poll示例

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;arpa/inet.h&gt;
#include &lt;poll.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/time.h&gt;


#define MAX_POLLFD_LEN 4096  
#define PORT 9108


void server() {<!-- -->
	
	// 创建socket连接
	int lfd = socket(AF_INET,SOCK_STREAM,0);
	struct sockaddr_in my_addr; 
	bzero(&amp;my_addr, sizeof(my_addr));
	my_addr.sin_family = AF_INET; // ipv4
	my_addr.sin_port   = htons(PORT);
	my_addr.sin_addr.s_addr = htonl(INADDR_ANY); 
	// 绑定端口
	bind(lfd, (struct sockaddr*)&amp;my_addr, sizeof(my_addr));
	// 监听连接请求
	listen(lfd, 128);
	printf("listen client @port=%d...\n",PORT);
	
	// 定义pollfd对象
	struct pollfd fds[MAX_POLLFD_LEN];
	memset(fds, 0, sizeof(fds));
	// 添加socket服务监听
	fds[0].fd = lfd;
	fds[0].events = POLLIN;
	int nfds = 1;
	int i;
	for(i = 1; i &lt; MAX_POLLFD_LEN; i++) {<!-- -->
		fds[i].fd = -1;
	}
	int maxFds = 0;
	printf("准备进入while循环\n");
	while (1) {<!-- -->
		printf("阻塞中, [maxFds=%d]...\n", maxFds);
		int nready = poll(fds, maxFds + 1, -1);
		switch (nready) {<!-- -->
			case 0 :
				printf("select time out ......\n");
				break;
			case -1 :
				perror("select error \n");
				break;
			default:
				// 监听到新的客户端连接
				if (fds[0].revents &amp; POLLIN) {<!-- -->
					struct sockaddr_in client_addr;	
					socklen_t cliaddr_len = sizeof(client_addr);
					char cli_ip[INET_ADDRSTRLEN] = "";	
					// 肯定有连接不会阻塞
					int clientfd = accept(lfd, (struct sockaddr*)&amp;client_addr, &amp;cliaddr_len);
					inet_ntop(AF_INET, &amp;client_addr.sin_addr, cli_ip, INET_ADDRSTRLEN);
					printf("----------------------------------------------\n");
					printf("client ip=%s,port=%d\n", cli_ip, ntohs(client_addr.sin_port));
					// 将clientfd加入读集合
					int j;
					for (j = 1; j &lt; MAX_POLLFD_LEN; ++j) {<!-- -->
						if (fds[j].fd &lt; 0) {<!-- -->
							fds[j].fd = clientfd;
							fds[j].events = POLLIN;
							printf("添加客户端成功...\n");
							maxFds++;   
							break;
						}
						if(j == MAX_POLLFD_LEN){<!-- -->
							printf("too many clients"); 
							exit(1);
						}
						
					}
				    
					if(--nready &lt;= 0) {<!-- -->
						continue;
					}
				}
				int i;
				printf("maxFds=%d\n", maxFds);
				for (i = 1; i &lt;= maxFds; i++) {<!-- -->
					printf("i=%d\n", i);
					// 处理读事件
					if (fds[i].revents &amp; POLLIN) {<!-- -->
						int sockfd = fds[i].fd;
						char recv_buf[512] = "";
						int rs = read(sockfd, recv_buf, sizeof(recv_buf));

						if (rs == 0) {<!-- -->
							close(sockfd);
							fds[i].fd = -1;
						} else {<!-- -->
							printf("%s\n",recv_buf);
							// 给每一个服务端写数据
							int j;
							for (j = 1;j &lt;= maxFds; j++) {<!-- -->
								if (j != i) {<!-- -->
									write(fds[j].fd, recv_buf, strlen(recv_buf));
								}
							}
						}
					}
				}
		}
		
	}
}

int main(){<!-- -->
	server();
	return 0;
}

```

#### 7.3 epoll

>  
 epoll可以理解为event pool，不同与select、poll的轮询机制，epoll采用的是事件驱动机制，每个fd上有注册有回调函数，当网卡接收到数据时会回调该函数，同时将该fd的引用放入rdlist就绪列表中。 当调用epoll_wait检查是否有事件发生时，只需要检查eventpoll对象中的rdlist双链表中是否有epitem元素即可。如果rdlist不为空，则把发生的事件复制到用户态，同时将事件数量返回给用户。 


##### 7.3.1 epoll函数的接口定义

```
#include &lt;sys/epoll.h&gt;

// 数据结构
// 每一个epoll对象都有一个独立的eventpoll结构体
// 用于存放通过epoll_ctl方法向epoll对象中添加进来的事件
// epoll_wait检查是否有事件发生时，只需要检查eventpoll对象中的rdlist双链表中是否有epitem元素即可
struct eventpoll {<!-- -->
    /*红黑树的根节点，这颗树中存储着所有添加到epoll中的需要监控的事件*/
    struct rb_root  rbr;
    /*双链表中则存放着将要通过epoll_wait返回给用户的满足条件的事件*/
    struct list_head rdlist;
};

// API
// 内核中间加一个 ep 对象，把所有需要监听的socket都放到ep对象中
int epoll_create(int size); 
// epoll_ctl 负责把 socket 增加、删除到内核红黑树
int epoll_ctl(int epfd,  // 创建的ep对象
              int op,    // 操作类型 新增、删除等
              int fd,    // 要操作的对象
              struct epoll_event *event  // 事件
             ); 
// epoll_wait 负责检测可读队列，没有可读 socket 则阻塞进程
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);

```

##### 7.3.2 epoll执行流程
- 调用epoll_create()创建一个ep对象，即红黑树的根节点，返回一个文件句柄- 调用epoll_ctl()向这个ep对象（红黑树）中添加、删除、修改感兴趣的事件- 调用epoll_wait()等待，当有事件发生时网卡驱动会调用fd上注册的函数并将该fd添加到rdlist中，解除阻塞
<img src="https://img-blog.csdnimg.cn/a51cb194b5e1479a888c8f59ea2005e4.png" alt="在这里插入图片描述">

##### 7.3.3 示例代码

```
#include&lt;stdio.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;						
#include &lt;unistd.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;arpa/inet.h&gt;	
#include &lt;sys/epoll.h&gt;

void server() {<!-- -->
	
	// 创建socket连接
	int lfd = socket(AF_INET,SOCK_STREAM,0);
	struct sockaddr_in my_addr; 
	bzero(&amp;my_addr, sizeof(my_addr));
	my_addr.sin_family = AF_INET; // ipv4
	my_addr.sin_port   = htons(8088);
	my_addr.sin_addr.s_addr = htonl(INADDR_ANY); 
	// 绑定端口
	bind(lfd, (struct sockaddr*)&amp;my_addr, sizeof(my_addr));
	// 监听连接请求
	listen(lfd, 128);
	printf("listen client @port=%d...\n", 8088);
	int epct, i;
	struct epoll_event event;
	struct epoll_event events[100];
	memset(events, 0, 100 * sizeof(struct epoll_event));
	int epfd = epoll_create(1);
	event.data.fd = lfd;
	event.events = EPOLLIN;
	epoll_ctl(epfd, EPOLL_CTL_ADD, lfd, &amp;event);
	while (1) {<!-- -->
		printf("阻塞中....\n");
		int nready = epoll_wait(epfd, events, 20, -1);
		int i;
		for (i = 0; i &lt; nready; ++i) {<!-- -->
			// 监听到新的客户端连接
			if (events[i].data.fd == lfd) {<!-- -->
				struct sockaddr_in client_addr;	
				socklen_t cliaddr_len = sizeof(client_addr);
				char cli_ip[INET_ADDRSTRLEN] = "";	
				// 肯定有连接不会阻塞
				int clientfd = accept(lfd, (struct sockaddr*)&amp;client_addr, &amp;cliaddr_len);
				inet_ntop(AF_INET, &amp;client_addr.sin_addr, cli_ip, INET_ADDRSTRLEN);
				
				event.data.fd = clientfd;
				event.events = EPOLLIN | EPOLLET;
				epoll_ctl(epfd, EPOLL_CTL_ADD, clientfd, &amp;event);
				
				printf("----------------------------------------------\n");
				printf("client ip=%s,port=%d\n", cli_ip, ntohs(client_addr.sin_port));
			} else {<!-- -->
				char recv_buf[512] = "";
				int rs = read(events[i].data.fd, recv_buf, sizeof(recv_buf));
				if (rs &lt; 0) {<!-- -->
					close(events[i].data.fd);
					epoll_ctl(epfd, EPOLL_CTL_DEL, events[i].data.fd, &amp;event);
					continue;
				}
				printf("%s\n",recv_buf);
			}
		}
	
		
	}
}

int main(){<!-- -->
	server();
	return 0;
}

```

##### 7.3.4 epoll总结
- EPOLL支持的最大文件描述符上限是整个系统最大可打开的文件数目, 1G内存理论上最大创建10万个文件描述符- 每个文件描述符上都有一个callback函数，当socket有事件发生时会回调这个函数将该fd的引用添加到就绪列表中，select和poll并不会明确指出是哪些文件描述符就绪，而epoll会。造成的区别就是，系统调用返回后，调用select和poll的程序需要遍历监听的整个文件描述符找到是谁处于就绪，而epoll则直接处理即可- select、poll采用轮询的方式来检查文件描述符是否处于就绪态，而epoll采用回调机制。造成的结果就是，随着fd的增加，select和poll的效率会线性降低，而epoll不会受到太大影响，除非活跃的socket很多
#### 7.4 select、poll、epoll比较

<img src="https://img-blog.csdnimg.cn/ebd70a2250b54036b7c4c82a81b2c0c9.png" alt="在这里插入图片描述">
