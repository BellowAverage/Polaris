
--- 
title:  springboot redis 分布式锁 工具类 
tags: []
categories: [] 

---
### springboot redis 分布式锁 工具类

本篇文章知识简单的了解一下redis的加锁 释放锁，具体的redis分布式锁的业务逻辑，请参考  参考  自己整理一下，方便后期的复习

```

import org.apache.commons.lang3.StringUtils;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Repository;
import java.util.UUID;
import java.util.concurrent.TimeUnit;

/**
 * redis锁操作类
 *
 * @author zk
 * @date 2020-9-10
 */
@Repository
public class RedisLock {

    private StringRedisTemplate stringredisTemplate;

    public RedisLock(StringRedisTemplate stringredisTemplate) {
        this.stringredisTemplate = stringredisTemplate;
    }

    /**
     * 加锁，无阻塞
     * 加锁过程必须设置过期时间
     * 如果没有设置过期时间,手动释放锁的操作出现问题,那么就发生死锁,锁永远不能被释放.
     * 加锁和设置过期时间过程必须是原子操作
     * 如果加锁后服务宕机或程序崩溃,来不及设置过期时间,同样会发生死锁.
     *
     * @param key 锁id
     * @param expire 过期时间
     * @return
     */
    public String tryLock(String key, long expire) {
        String token = UUID.randomUUID().toString();
        //setIfAbsent方法:当key不存在的时候,设置成功并返回true,当key存在的时候,设置失败并返回false
        //token是对应的value,expire是缓存过期时间
        Boolean isSuccess = stringredisTemplate.opsForValue().setIfAbsent(key, token, expire, TimeUnit.MILLISECONDS);
        if (isSuccess) {
            return token;
        }
        return null;
    }

    /**
     * 加锁，有阻塞
     *
     * @param name 锁名称
     * @param expire 锁过期时间
     * @param timeout 请求超时时间
     * @return
     */
    public String lock(String name, long expire, long timeout) {
        long startTime = System.currentTimeMillis();
        String token;
        do {
            token = tryLock(name, expire);
            if (token == null) {
                if ((System.currentTimeMillis() - startTime) &gt; (timeout - 50)) {
                    break;
                }
                try {
                    //try 50 per sec
                    Thread.sleep(50);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                    return null;
                }
            }
        } while (token == null);

        return token;
    }

    /**
     * 解锁操作
     * 解锁必须是解除自己加上的锁
     * 试想一个这样的场景,服务A加锁,但执行效率非常慢,导致锁失效后还未执行完,但这时候服务B已经拿到锁了,这时候服务A执行完毕了去解锁,
     * 把服务B的锁给解掉了,其他服务C、D、E...都可以拿到锁了,这就有问题了.
     * 加锁的时候我们可以设置唯一value,解锁时判断是不是自己先前的value就行了.
     *
     * @param key
     * @param token
     * @return
     */
    public boolean unlock(String key, String token) {
        //解锁时需要先取出key对应的value进行判断是否相等,这也是为什么加锁的时候需要放不重复的值作为value
        String value = stringredisTemplate.opsForValue().get(key);
        if (StringUtils.equals(value, token)) {
            stringredisTemplate.delete(key);
            return true;
        }
        return false;
    }
}

```
