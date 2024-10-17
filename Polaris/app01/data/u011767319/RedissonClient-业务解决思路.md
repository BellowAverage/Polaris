
--- 
title:  RedissonClient-业务解决思路 
tags: []
categories: [] 

---
### 如何让多个负载的项目（同一个）只执行一次代码运行

例子：

```
package com.ljq.service.facebook.job;

import lombok.extern.slf4j.Slf4j;
import org.redisson.api.RBucket;
import org.redisson.api.RedissonClient;
import org.redisson.client.codec.StringCodec;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Configuration;
import org.springframework.util.CollectionUtils;
import shop.easysell.common.lib.builder.CacheKeyBuilder;
import shop.easysell.common.lib.enumeration.CommonCacheKeyModuleEnum;
import shop.easysell.lib.facebook.domain.po.Live;
import shop.easysell.service.facebook.service.LiveService;
import shop.easysell.service.facebook.service.thirdparty.FacebookLiveService;

import javax.annotation.Resource;
import java.util.List;
import java.util.concurrent.TimeUnit;

@Configuration
@Slf4j
public class LiveCommentStreamJob implements ApplicationRunner {<!-- -->

    @Resource
    private LiveService liveService;
    @Resource
    private FacebookLiveService facebookLiveService;
    @Resource
    private RedissonClient redissonClient;

    @Override
    public void run(ApplicationArguments args) throws Exception {<!-- -->
        String temporaryCommentStreamKey = CacheKeyBuilder.build(
                CommonCacheKeyModuleEnum.FACEBOOK,
                "live",
                "temporary",
                "commentStream",
                "job"
        );
        RBucket&lt;String&gt; bucket = redissonClient.getBucket(temporaryCommentStreamKey, StringCodec.INSTANCE);
        //获取缓存是否存在-存在就跳过执行
        if (!bucket.isExists()) {<!-- -->
            //设置数据一分钟过去
            bucket.set("running", 1, TimeUnit.MINUTES);
            //查询直播间正在直播，启动监听评论线程
            List&lt;Live&gt; activityLiveList = liveService.getActivityLiveList();
            if (!CollectionUtils.isEmpty(activityLiveList)) {<!-- -->
                activityLiveList.forEach(live -&gt; {<!-- -->
                    if (log.isInfoEnabled()) {<!-- -->
                        log.info("直播间id:{},直播间名称:{}", live.getId(), live.getName());
                    }
                    try {<!-- -->
                        facebookLiveService.dealWithRealtimeComments(live);
                    } catch (Exception e) {<!-- -->
                        log.error("直播间id:{},直播间名称:{},处理直播评论线程异常", live.getId(), live.getName(), e);
                    }
                });
            }
        }
    }
}


```

### 加锁的使用

```
//加锁
String commentDealWithKey = CacheKeyBuilder.build(
        CommonCacheKeyModuleEnum.FACEBOOK,
        "live",
        "comment",
        "dealWith",
        live.getId().toString());
RLock lock = redissonClient.getLock(commentDealWithKey);
try {<!-- -->
    //等待3三秒，最长等待5秒
    if (lock.tryLock(3,5, TimeUnit.SECONDS)) {<!-- -->
        //代码内容
    }
} catch (Exception e) {<!-- -->
    log.error("错误日志", e);
} finally {<!-- -->
    if (lock.isHeldByCurrentThread()) {<!-- -->
        lock.unlock();
    }
}

```
