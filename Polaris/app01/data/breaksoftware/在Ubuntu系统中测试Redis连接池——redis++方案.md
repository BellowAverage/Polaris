
--- 
title:  在Ubuntu系统中测试Redis连接池——redis++方案 
tags: []
categories: [] 

---


#### 大纲
- - - - - 


## 安装依赖

```
sudo apt install gcc
sudo apt install g++
sudo apt install cmake
sudo apt install libhiredis-dev
sudo apt install libssl-dev

```

## 安装redis++

```
git clone https://github.com/sewenew/redis-plus-plus.git
cd redis-plus-plus
mkdir build
cd build
cmake ..
make
sudo make install
cd ..

```

## 代码

```
#include &lt;iostream&gt;
#include &lt;thread&gt;
#include &lt;sw/redis++/redis++.h&gt;
#include &lt;sw/redis++/connection.h&gt;
#include &lt;sw/redis++/connection_pool.h&gt;
using namespace sw::redis;

void test_multithreads(Redis redis, int thread_num, int times) {<!-- -->
    std::vector&lt;std::string&gt; keys;
    keys.reserve(thread_num);
    for (auto idx = 0; idx != thread_num; ++idx) {<!-- -->
        auto key = "multi-threads::" + std::to_string(idx);
        keys.push_back(key);
        redis.set(key, key);
    }

    std::vector&lt;std::thread&gt; workers;
    workers.reserve(thread_num);
    for (const auto &amp;key : keys) {<!-- -->
        workers.emplace_back([&amp;redis, key, times]() {<!-- -->
                                try {<!-- -->
                                    for (auto i = 0; i != times; ++i) {<!-- -->
                                        auto val = redis.get(key);
                                        if (!val) {<!-- -->
                                            std::cout&lt;&lt; "failed to test multithreads, cannot get value of " + key &lt;&lt; std::endl;
                                            return;
                                        }
                                    }
                                } catch (std::exception &amp;e) {<!-- -->
                                    std::cerr&lt;&lt; "failed to test multithreads, " &lt;&lt; e.what() &lt;&lt; std::endl;
                                    return;
                                }
                            });
    }

    for (auto &amp;worker : workers) {<!-- -->
        worker.join();
    }
}

int main() {<!-- -->
    ConnectionOptions opts;
    opts.host = "127.0.0.1";
    opts.port = 6379;
    opts.socket_timeout = std::chrono::milliseconds(50);
    opts.keep_alive = true;

    ConnectionPoolOptions pool_opts;
    pool_opts.size = 300;
    
    auto thread_num = 500;
    auto times_in_one_second = 1000000;
    test_multithreads(Redis(opts, pool_opts), thread_num, times_in_one_second);
}

```

上面代码启动了500个线程，它们公用一个redis连接池。该池子上限被设置为300个。每个线程内部会查询1000000次，以维持程序运行，让我们可以观察到中间连接数变化。 使用下面的脚本进行编译

```
g++ -std=c++17 -o main main.cpp /usr/local/lib/libredis++.a /usr/lib/x86_64-linux-gnu/libhiredis.a -pthread

```

## 查看连接数

使用下面命令进入交互界面

```
redis-cli -h 127.0.0.1 -p 6379

```

然后使用下面命令查看连接数，connected_clients为1，即当前redis-cli的连接。

```
info clients

```

>  
 # Clients connected_clients:1 client_recent_max_input_buffer:8 client_recent_max_output_buffer:0 blocked_clients:0 tracking_clients:0 clients_in_timeout_table:0 


在一个新窗口中运行上面编译的测试程序。

```
./main 

```

然后再查看连接数

>  
 # Clients connected_clients:301 client_recent_max_input_buffer:8 client_recent_max_output_buffer:0 blocked_clients:0 tracking_clients:0 clients_in_timeout_table:0 


可以看到连接数增加了300。这个和我们代码中设置的连接池大小上限匹配。

## 参考资料
- 