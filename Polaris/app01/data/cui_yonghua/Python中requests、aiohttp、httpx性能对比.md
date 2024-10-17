
--- 
title:  Python中requests、aiohttp、httpx性能对比 
tags: []
categories: [] 

---
在Python中，有许多用于发送HTTP请求的库，其中最受欢迎的是requests、aiohttp和httpx。这三个库的性能和功能各不相同，因此在选择使用哪个库时，需要考虑到自己的需求和应用场景。

首先，让我们来了解一下这三个库的基本介绍。
-  <mark>requests</mark> 是一个简单易用的HTTP库，它可以发送HTTP请求和处理HTTP响应。它的API简单易用，可以轻松地实现HTTP请求和响应的处理。 -  <mark>aiohttp</mark> 是一个异步HTTP客户端/服务器框架，它使用asyncio库实现异步IO操作。它支持HTTP/1.1和HTTP/2协议，可以轻松地处理大量并发请求。 -  <mark>httpx</mark> 是一个全新的HTTP客户端库，它提供了更加现代化的API和更好的性能。它支持异步和同步请求，支持HTTP/1.1和HTTP/2协议，还提供了WebSocket和HTTP/1.1协议升级的支持。 
接下来，我们将对这三个库进行性能测试，以便更好地了解它们的性能和优缺点。

我们使用Python 3.9.1版本进行测试，测试的机器配置为Intel Core i7-7700HQ CPU @ 2.80GHz，16GB内存，Windows 10操作系统。

#### requests测试

首先，我们测试了发送1000个同步请求的时间。测试代码如下：

```
import requests
import time
start_time = time.time()
for i in range(1000):
    response = requests.get('https://www.baidu.com')
end_time = time.time()
print('Time taken: ', end_time - start_time)

```

测试结果如下：

```
Time taken:  8.606025457382202

```

#### aiohttp测试

接下来，我们测试使用aiohttp发送1000个异步请求的时间。测试代码如下：

```
import aiohttp
import asyncio
import time
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.read()
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1000):
            task = asyncio.ensure_future(fetch(session, 'https://www.baidu.com'))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end_time = time.time()
print('Time taken: ', end_time - start_time)

```

测试结果如下：

```
Time taken:  1.8979811668395996

```

#### httpx测试

最后，我们测试使用httpx发送1000个异步请求的时间。测试代码如下：

```
import httpx
import asyncio
import time
async def main():
    async with httpx.AsyncClient() as client:
        for i in range(1000):
            response = await client.get('https://www.baidu.com')
start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end_time = time.time()
print('Time taken: ', end_time - start_time)

```

测试结果如下：

```
Time taken:  1.4310226440429688

```

从上述测试结果可以看出，httpx的性能最好，aiohttp的性能次之，requests的性能最差。但是，在实际应用中，我们需要根据具体的需求来选择合适的库。如果我们需要处理大量并发请求，那么aiohttp和httpx是更好的选择，因为它们支持异步IO操作，可以更好地处理大量并发请求。如果我们只需要发送一些简单的HTTP请求，那么requests是一个更简单和易用的选择。

这三个库各有优缺点，我们需要根据自己的需求和应用场景来选择合适的库。
