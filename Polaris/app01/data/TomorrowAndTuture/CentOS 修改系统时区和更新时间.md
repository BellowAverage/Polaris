
--- 
title:  CentOS 修改系统时区和更新时间 
tags: []
categories: [] 

---
### 修改时区

新安装 centOS 系统后，可能会出现由于时区问题，导致时间与现有正常时间相差 8 个小时的情况。我们可以通过相应的命令来重新设置时区。

```
[root@master ~]# timedatectl
               Local time: Mon 2021-01-25 07:03:18 UTC
           Universal time: Mon 2021-01-25 07:03:18 UTC
                 RTC time: Mon 2021-01-25 07:03:32
                Time zone: UTC (UTC, +0000)
System clock synchronized: no
              NTP service: active
          RTC in local TZ: no

```

**1、查看时间各种状态：**

```
[root@master ~]# timedatectl
      Local time: Mon 2021-01-25 14:57:51 CST
  Universal time: Mon 2021-01-25 06:57:51 UTC
        RTC time: Mon 2021-01-25 06:57:51
       Time zone: Asia/Shanghai (CST, +0800)
     NTP enabled: yes
NTP synchronized: yes
 RTC in local TZ: no
      DST active: n/a

```

**2、 列出所有时区：**

```
timedatectl list-timezones
```

**3、将硬件时钟调整为与本地时钟一致, 0 为设置为 UTC 时间：**

```
timedatectl set-local-rtc 1
```

**4、设置系统时区为上海：**

```
timedatectl set-timezone Asia/Shanghai
```

### 更新时间

有时候系统的当前时间可能并不准确，这时候我们就需要重新更新一下了(我想大部分进来看的都是想找下面这个 ntpdate 方法的)。

```
ntpdate -u ntp.api.bz
```

```
[root@localhost ~]# date
Tue Apr 19 08:27:55 CST 2022
[root@localhost ~]# ntpdate -u ntp.api.bz
19 Apr 08:29:58 ntpdate[19188]: step time server 114.118.7.161 offset 113.166172 sec
[root@localhost ~]# date
Tue Apr 19 08:30:01 CST 2022

```


