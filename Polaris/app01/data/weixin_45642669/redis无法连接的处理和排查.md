
--- 
title:  redis无法连接的处理和排查 
tags: []
categories: [] 

---
这个花费了大概半个小时，记录一下。

报错提示：XXXX：6379不存在。

### 防火墙：

```
// 新增端口
firewall-cmd --zone=public --add-port=8080/tcp --permanent（端口可以变化，不一定是8080）
// 删除端口
firewall-cmd --zone=public --remove-port=8080/tcp --permanent（端口可以变化，不一定是8080）
// 只有执行这个才生效
firewall-cmd --reload
// 展示端口列表
firewall-cmd --zone=public --list-ports

```

执行一下list然后执行一下add、reload即可。

### blind

redis.conf 里面有个blind，也就是啥设备可以登陆该服务器。默认是只有本机可以

```
# bind 127.0.0.1 -::1

```
- 如果想所有的人都可以登陆，那么就直接注释掉。（这个官方不推荐）- 如果指定服务器的话，那么需要新增bind
### 需要设置密码和安全策略拒绝

redis默认是：

```
protected-mode yes

```

不允许无密码登陆

需要在vim里面查找：

```
/requirepass

```

然后取消注释并写入密码即可。（除去前方空格）

### 修改后重启redis

所有操作都需要重启redis,不然不会生效。

```
redis-cli -p 6379
shutdown
quit
redis-server redis.conf

```

## 故障排除
<li> 没有防火墙或者没有启动，那么会提示不存在。 
  <ul>- telnet ip 6379可以测试
如果是没有设置密码强行登陆，会提示安全策略不允许。

只有修改conf文件并重启，才能长期生效。其余的设置只会一次性生效。

测试代码：

```
import redis.clients.jedis.Jedis;

public class text01 {
    public static void main(String[] args) {
        Jedis jedis = new Jedis("43.128.57.71", 6379);
        jedis.auth("123456");
        String ping = jedis.ping();
        System.out.println(ping);

    }
}

```
