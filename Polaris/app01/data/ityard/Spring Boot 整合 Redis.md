
--- 
title:  Spring Boot 整合 Redis 
tags: []
categories: [] 

---
##### 简介

Redis 是目前使用十分广泛的内存数据库。Redis 比 Memcached 支持更丰富的数据类型，如 Lists, Hashes, Sets 及 Ordered Sets 等，支持数据持久化、备份；除此之外，Redis 还支持事务，HA，主从库，同时兼具了非关系型数据库与关系型数据的特性，有着丰富的应用场景。

##### 快速上手

**1、引入依赖**

```
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
  &lt;artifactId&gt;spring-boot-starter-data-redis&lt;/artifactId&gt;
  &lt;version&gt;2.1.5.RELEASE&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.apache.commons&lt;/groupId&gt;
  &lt;artifactId&gt;commons-pool2&lt;/artifactId&gt;
  &lt;version&gt;2.0&lt;/version&gt;
&lt;/dependency&gt;

```

**2、配置文件**

单机模式

```
# Redis数据库索引（默认为0）
spring.redis.database=0
# Redis服务器地址
spring.redis.host=127.0.0.1
# Redis服务器连接端口
spring.redis.port=6379
# Redis服务器连接密码（默认为空）
spring.redis.password=
# 连接池最大连接数（使用负值表示没有限制）
spring.redis.jedis.pool.max-active=8
# 连接池最大阻塞等待时间（使用负值表示没有限制）
spring.redis.jedis.pool.max-wait=-1
# 连接池中的最大空闲连接
spring.redis.jedis.pool.max-idle=8
# 连接池中的最小空闲连接
spring.redis.jedis.pool.min-idle=0
# 连接超时时间（毫秒）
spring.redis.timeout=5000

```

哨兵模式

```
spring.redis.lettuce.pool.max-active=8
spring.redis.lettuce.pool.max-wait=-1
spring.redis.lettuce.pool.max-idle=8
spring.redis.lettuce.pool.min-idle=0
spring.redis.timeout=5000
spring.redis.database=0
spring.redis.sentinel.master=mymaster
spring.redis.sentinel.nodes=127.0.0.1:26380,127.0.0.1:26381,127.0.0.1:26382
spring.redis.password=

```

**3、测试**

```
@RunWith(SpringRunner.class)
@SpringBootTest
public class RedisTests {<!-- -->
    @Autowired
    private StringRedisTemplate stringRedisTemplate;
  @Test
  public void contextLoads() {<!-- -->
  }
  @Test
  public void setRedis(){<!-- -->
      stringRedisTemplate.opsForValue().set("key1","张三");
  }
  @Test
  public void getRedis(){<!-- -->
        String s = stringRedisTemplate.opsForValue().get("key1");
    System.out.println("s:    "+s);
    }
}

```

**4、实现共享 Session**

1）添加依赖

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.session&lt;/groupId&gt;
    &lt;artifactId&gt;spring-session-data-redis&lt;/artifactId&gt;
&lt;/dependency&gt;

```

2）配置

```
@Configuration
@EnableRedisHttpSession(maxInactiveIntervalInSeconds = 86400)
public class SessionConfig {<!-- -->
}
maxInactiveIntervalInSeconds: 设置 Session 失效时间
使用 Redis Session 之后，原 Spring Boot 的 server.session.timeout 属性不再生效。

```

`注` maxInactiveIntervalInSeconds: 设置 Session 失效时间。 使用 Redis Session 之后，原 Spring Boot 的 server.session.timeout 属性不再生效。

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
