
--- 
title:  C/C++ 实现UDP发送或接收组播消息，并可指定接收发送网卡 
tags: []
categories: [] 

---
### 一、发送端代码

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;net/if.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;netdb.h&gt;
#include &lt;sys/ioctl.h&gt;
#include "UDPOperation.h"
#include "GlobalVariable.h"
#include "Logger.h"
#include "EndException.h"
#include "BaseException.h"

UDPOperation::UDPOperation(char* remote_host, int remote_port, char* interface) : fd(-1)
{<!-- -->
    // 创建通信的套接字
    this-&gt;remote_host = remote_host;
    this-&gt;remote_port = remote_port;
    this-&gt;interface = interface;

    memset(&amp;(this-&gt;cliaddr), 0, sizeof(sockaddr_in));
    this-&gt;cliaddr.sin_family = AF_INET;
    this-&gt;cliaddr.sin_port = htons(this-&gt;remote_port); // 接收端需要绑定remote_port端口
}

UDPOperation::~UDPOperation() {<!-- -->}

bool UDPOperation::create_udpsocket()
{<!-- -->
    this-&gt;fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (this-&gt;fd == -1)
    {<!-- -->
        LOG_ERROR("Socket creation failed: %s", strerror(errno));
        throw EndException(errno, strerror(errno));
    }

    inet_pton(AF_INET, this-&gt;remote_host, &amp;this-&gt;cliaddr.sin_addr.s_addr);

    hostent* host = gethostbyname(remote_host);
    unsigned long hostip = *(unsigned long *)host-&gt;h_addr;
    
    this-&gt;cliaddr.sin_addr.s_addr = hostip;
    
    unsigned char net = hostip &amp; 0xff;
    if (net &gt; 223 &amp;&amp; net &lt; 240)  // 如果是多播
    {<!-- -->   
        char numeric_ip[32] = "\0";
        get_ifaddr (numeric_ip);
        struct in_addr outputif;
        outputif.s_addr = inet_addr (numeric_ip);
        LOG_INFO("interface = %s, numeric_ip = %s", interface, numeric_ip);
        if (setsockopt(this-&gt;fd, IPPROTO_IP, IP_MULTICAST_IF, (char* ) &amp;outputif, sizeof(struct in_addr)))
        {<!-- -->
            throw EndException(errno, strerror(errno));
        }
    }

    return true;
}

int UDPOperation::get_ifaddr(char* addr)
{<!-- -->
  int sock = socket (AF_INET, SOCK_DGRAM, 0);

  struct ifreq ifr;
  memset (&amp;ifr, 0, sizeof (ifr));
  strcpy (ifr.ifr_name, interface);
  if (ioctl (sock, SIOCGIFADDR, &amp;ifr) &lt; 0) {<!-- -->
    close (sock);
    throw EndException(errno, strerror(errno));
    return 1;
  }
  
  strcpy (addr, inet_ntoa(((struct sockaddr_in* ) &amp;(ifr.ifr_addr))-&gt;sin_addr));
  close (sock);

  return 0;
}

void UDPOperation::destory_udpsocket()
{<!-- -->
    close(this-&gt;fd);
}

bool UDPOperation::send_buffer(char *buffer)
{<!-- -->
    socklen_t len = sizeof(struct sockaddr_in);
    // 数据广播
    int t = sendto(this-&gt;fd, buffer, SEND_UDP_PER_TSPACKET_SIZE, 0, (struct sockaddr *)&amp;cliaddr, len);
    if (t == -1)
    {<!-- -->
        LOG_ERROR("Socket send failed: %s", strerror(errno));
        throw BaseException(errno, strerror(errno));
    }
    return true;
}

```

### 二、接收端代码

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;net/if.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;netdb.h&gt;
#include &lt;sys/ioctl.h&gt;
#include "UDPOperation.h"
#include "GlobalVariable.h"
#include "Logger.h"
#include "EndException.h"
#include "BaseException.h"

UDPOperation::UDPOperation(std::string remote_host, int remote_port, char* interface) : fd(-1)
{<!-- -->
    // 创建通信的套接字
    this-&gt;remote_host = remote_host;
    this-&gt;remote_port = remote_port;
    this-&gt;interface = interface;

    memset(&amp;(this-&gt;cliaddr), 0, sizeof(sockaddr_in));
    this-&gt;cliaddr.sin_family = AF_INET;
    this-&gt;cliaddr.sin_addr.s_addr = inet_addr(this-&gt;remote_host.c_str());
    this-&gt;cliaddr.sin_port = htons(this-&gt;remote_port); // 接收端需要绑定remote_port端口
}

UDPOperation::~UDPOperation() {<!-- -->}

bool UDPOperation::create_udpsocket()
{<!-- -->
    this-&gt;fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (this-&gt;fd == -1)
    {<!-- -->
        LOG_ERROR("Socket creation failed: %s", strerror(errno));
        throw EndException(errno, strerror(errno));
    }

    // 设置socket选项，允许重用地址  
    int reuse = 1;  
    if (setsockopt(this-&gt;fd, SOL_SOCKET, SO_REUSEADDR, &amp;reuse, sizeof(reuse)) &lt; 0) {<!-- -->  
        LOG_ERROR("Error setting socket option: %s", strerror(errno));
        throw EndException(errno, strerror(errno)); 
    }  

    struct sockaddr_in local_addr;      //local address
    memset(&amp;local_addr, 0, sizeof(local_addr));
    local_addr.sin_family = AF_INET;
    local_addr.sin_addr.s_addr = inet_addr("0.0.0.0");   // 设定本地监听必须是0.0.0.0 这里是关键！
    local_addr.sin_port = htons(remote_port);             //this port must be the group port
    //建立本地捆绑（主机地址/端口号）
    if (bind(fd, (struct sockaddr*)&amp;local_addr, sizeof(local_addr)) != 0)
    {<!-- -->
        LOG_ERROR("Error binding socket: %s", strerror(errno));
        throw EndException(errno, strerror(errno)); 
    }
    
    // 如果是组播 加入组播
    int net = stoi(remote_host.substr(0, remote_host.find('.')));
    if (net &gt;= 224 &amp;&amp; net &lt;= 239)
    {<!-- -->
        struct ip_mreq mreq;
        mreq.imr_multiaddr.s_addr = inet_addr(this-&gt;remote_host.c_str());
        if(strlen(interface) == 0){<!-- -->
            mreq.imr_interface.s_addr = htonl(INADDR_ANY);                //任意接口接收组播信息
        }else{<!-- -->
            char numeric_ip[32] = "\0";
            get_ifaddr (numeric_ip);
            LOG_INFO("interface = %s, numeric_ip = %s", interface, numeric_ip);
            mreq.imr_interface.s_addr = inet_addr(numeric_ip);    //指定新接口接收组播信息
        }

        if (setsockopt(fd, IPPROTO_IP, IP_ADD_MEMBERSHIP, &amp;mreq, sizeof(mreq)) != 0) {<!-- -->
            LOG_ERROR("Error setting socket option for multicast: %s", strerror(errno));
            throw EndException(errno, strerror(errno));
        }
    }
    return true;
}

void UDPOperation::destory_udpsocket()
{<!-- -->
    close(this-&gt;fd);
}

int UDPOperation::recv_buffer(uint8_t *buffer, int size)
{<!-- -->
    socklen_t len = sizeof(struct sockaddr_in);
    int bytes_received = recvfrom(this-&gt;fd, buffer, size, 0, (struct sockaddr *)&amp;this-&gt;cliaddr, &amp;len);  
    if (bytes_received &lt; 0) {<!-- -->  
        LOG_ERROR("Error receiving data: %s", strerror(errno));
        throw BaseException(errno, strerror(errno)); 
    }  
    return bytes_received;
}

int UDPOperation::get_ifaddr(char* addr)
{<!-- -->
    int sock = socket (AF_INET, SOCK_DGRAM, 0);

    struct ifreq ifr;
    memset (&amp;ifr, 0, sizeof (ifr));
    strcpy (ifr.ifr_name, interface);
    if (ioctl (sock, SIOCGIFADDR, &amp;ifr) &lt; 0) {<!-- -->
        close (sock);
        throw EndException(errno, strerror(errno));
        return 1;
    }

    strcpy (addr, inet_ntoa(((struct sockaddr_in* ) &amp;(ifr.ifr_addr))-&gt;sin_addr));
    close (sock);

    return 0;
}

```

### 三、若udp组播接收不到数据可能是如下原因

```
# 2. 看系统有没有过滤组播包：
# 2.1 看接受组播的网卡是否过滤了：
cat /proc/sys/net/ipv4/conf/en4/rp_filter
# 如果是0， good。
# 2.2 看all网卡是否过滤了：
cat /proc/sys/net/ipv4/conf/all/rp_filter
# 如果是0， good。
# 这两个值都必须是0，才行！如果不是0，这样修改：
# 2.3 临时修改取消过滤：
sudo sysctl -w net.ipv4.conf.en4.rp_filter=0
sudo sysctl -w net.ipv4.conf.all.rp_filter=0
# 2.4 永久修改取消过滤（重启亦有效）：
sudo vi /etc/sysctl.conf
# 改为：
net.ipv4.conf.default.rp_filter=0
net.ipv4.conf.all.rp_filter=0

```

**rp_filter参数详细介绍：** rp_filter参数有三个值，0、1、2，具体含义：

0：不开启源地址校验。

1：开启严格的反向路径校验。对每个进来的数据包，校验其反向路径是否是最佳路径。如果反向路径不是最佳路径， 则直接丢弃该数据包。

2：开启松散的反向路径校验。对每个进来的数据包，校验其源地址是否可达，即反向路径是否能通（通过任意网口），如果反向路径不同，则直接丢弃该数据包。
