
--- 
title:  okhttp-sse的使用笔记 
tags: []
categories: [] 

---
### 引入包

```
&lt;dependency&gt;
    &lt;groupId&gt;com.squareup.okhttp3&lt;/groupId&gt;
    &lt;artifactId&gt;okhttp&lt;/artifactId&gt;
    &lt;version&gt;4.9.3&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
    &lt;groupId&gt;com.squareup.okhttp3&lt;/groupId&gt;
    &lt;artifactId&gt;okhttp-sse&lt;/artifactId&gt;
    &lt;version&gt;4.9.3&lt;/version&gt;
&lt;/dependency&gt;

```

### 使用例子

```
package com.ljq.service.facebook;

import lombok.extern.slf4j.Slf4j;
import okhttp3.*;
import okhttp3.sse.EventSource;
import okhttp3.sse.EventSourceListener;
import okhttp3.sse.EventSources;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import javax.annotation.Resource;
import java.util.concurrent.CountDownLatch;

@SpringBootTest
@Slf4j
class EsFacebookServiceApplicationTests {<!-- -->

    @Resource
    private OkHttpClient okHttpClient;

    @Test
    void testOkhttpSSE() {<!-- -->
        String liveVideoId = "126634666668314";
        String token = "EAAHAVavpEUMBAKBAgoQa8UvfVOEMQfGs2u4bmUem9MuRiZB4Yig5HGBZB3p77ZCMlV5AHjmnGZCuwpjZAZBuZChYJViKZC3zvgIeAl4HZAF3KNIFLIOtGTCXZBZBtxphZCZCLgVIrd4npPZCRyuXT8hKhOX7T6ZCCeYrHplNtZCsZBszSMNXopBFQ0lkG89JVfpdNsq9AwZCEZD";
        String url = "https://streaming-graph.facebook.com/" + liveVideoId + "/live_comments" +
                "?access_token=" + token;
        Request request = new Request.Builder().url(url).build();
        EventSource.Factory factory = EventSources.createFactory(okHttpClient);
        EventSourceListener eventSourceListener = new EventSourceListener() {<!-- -->
            /**
             * {@inheritDoc}
             */
            @Override
            public void onOpen(final EventSource eventSource, final Response
                    response) {<!-- -->
                log.info("建立sse连接...");
            }

            /**
             * {@inheritDoc}
             */
            @Override
            public void onEvent(final EventSource eventSource, final String
                    id, final String type, final String data) {<!-- -->
                log.info("{}: {}", id, data);
            }

            /**
             * {@inheritDoc}
             */
            @Override
            public void onClosed(final EventSource eventSource) {<!-- -->
                log.info("sse连接关闭...");
            }

            /**
             * {@inheritDoc}
             */
            @Override
            public void onFailure(final EventSource eventSource, final
            Throwable t, final Response response) {<!-- -->
                log.error("使用事件源时出现异常... [响应：{}]...", response, t);
            }
        };
        //创建事件
        factory.newEventSource(request, eventSourceListener);
        //由于springboot test异步的，加下面代码卡住同步
        CountDownLatch countDownLatch = new CountDownLatch(1);
        try {<!-- -->
            countDownLatch.await();
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }
    }

}


```
