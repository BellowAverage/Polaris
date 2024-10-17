
--- 
title:  zabbix4.0-动作-邮件告警 
tags: []
categories: [] 

---
**目录**



























### 1、创建动作Actions

>  
 **根据支持的事件源定义操作** 
 - **触发事件 - 当trigger的状态从 **OK** 转到 **PROBLEM** 或者从 **PROBLEM** 转到 **OK****- **发现事件 - 发生网络发现时**- **自动注册事件 -当新的活动代理自动注册**- **内部事件 - 当项目不受支持或触发器进入未知状态** 


>  
 **配置动作** 
 - **进入 **配置 - &gt;操作****- **从**Event source**下拉单中选择所需的来源**- **点击 **创建 action****- **命名action**- **选择进行操作的条件**- **选择来执行**- **选择来执行** 


#### 动作触发流程 

<img alt="" height="168" src="https://img-blog.csdnimg.cn/89d78ac8d7b14c7cb5a16fabb714f22f.png" width="894">



#### 创建一个动作

<img alt="" height="456" src="https://img-blog.csdnimg.cn/a2933d82f4f54ae3abb0d757050c6042.png" width="1200">

<img alt="" height="435" src="https://img-blog.csdnimg.cn/16d8811d2faa463ebf45e1bb201a1016.png" width="734">

<img alt="" height="488" src="https://img-blog.csdnimg.cn/0c1205cfad244e92aee4e976e97acc01.png" width="809">

>  
 ** Operations 操作配置** 


<img alt="" height="1105" src="https://img-blog.csdnimg.cn/bbc9db46df5a425ea9e79da69788231e.png" width="989">

>  
 ** recovery operation  恢复操作配置：** 


<img alt="" height="853" src="https://img-blog.csdnimg.cn/fc33febbfeae46e592f6a23a5222bb7e.png" width="862">

 动作添加完成：

<img alt="" height="349" src="https://img-blog.csdnimg.cn/f60f490dfc2946229997b99ad4c63498.png" width="1187">

 <img alt="" height="510" src="https://img-blog.csdnimg.cn/9faa93eeaf6b488c8f03fc3a62c5a360.png" width="1200">



**##############################################################################**

### 2、配置 Media types 媒介类型，添加一个发件邮箱来发送告警邮件

<img alt="" height="656" src="https://img-blog.csdnimg.cn/26b39fdc15cb4592bdd0a47320b5aa76.png" width="781">

**##############################################################################**

### 3、配置 Users  Media，添加一个收件邮箱来接收告警邮件

<img alt="" height="637" src="https://img-blog.csdnimg.cn/7e676fdd7daf4dd699dd25f0f362ccb9.png" width="915">



<img alt="" height="330" src="https://img-blog.csdnimg.cn/c2a5a3a585f64f6586d679d314db678b.png" width="895">



 **##############################################################################**

### 4、更改一个触发器表达式来触发动作Action，最终发送告警邮件给接收邮箱

>  
 **测试一个触发器触发以后能否给我们发邮件通知** 


 这里我们找到刚才创建的触发器，修改它的表达式，让它一定能触发

<img alt="" height="1189" src="https://img-blog.csdnimg.cn/79f3f626a73a4eecbea745fd1dabe670.png" width="1200">

 <img alt="" height="456" src="https://img-blog.csdnimg.cn/4f187527e8a34147b5dec595988282fa.png" width="977">

>  
 **接下来可以看到Monitoring里的problems会出现一个问题** 


<img alt="" height="862" src="https://img-blog.csdnimg.cn/bbe1a49a49bb4bdf84657eba635e6802.png" width="1200">

>  
 ** 触发器状态由OK转为PROBLEM，然后触发Action，action会发送预定义好的一些信息给定义的用户组，这里设置的是发送给zabbix administrator组** 


<img alt="" height="620" src="https://img-blog.csdnimg.cn/79eec780d273432db7a64680fcca32db.png" width="1199">

 **##############################################################################**

### 5、登录接收告警通知的邮箱，可以看到zabbix发送的告警邮件

 <img alt="" height="569" src="https://img-blog.csdnimg.cn/63edf34e15174f69ba47b22c120a3062.png" width="924">

  **##############################################################################**

### 6、收到告警邮件以后，将触发器表达式改回来，应该还会收到一个恢复邮件

<img alt="" height="455" src="https://img-blog.csdnimg.cn/60513ef8af7443feb43a7318f7583873.png" width="846">

>  
 ** 改回来以后，触发器状态会由PROBLEM状态变成OK状态** 


<img alt="" height="913" src="https://img-blog.csdnimg.cn/ef003bb3f46643d9a0537b918c6bc9c1.png" width="1200">

>  
 ** 然后收到一封resolved邮件** 


<img alt="" height="623" src="https://img-blog.csdnimg.cn/b9001084b0bc44819f05b03e1c120b47.png" width="1192">

   **##############################################################################**

### 7、更改动作里面的发送信息内容，让邮件看起来更加标准

```
zabbix alert:
告警主机:{HOSTNAME1}
告警时间:{EVENT.DATE} {EVENT.TIME}
告警等级:{TRIGGER.SEVERITY}
告警信息:{TRIGGER.NAME}
告警项目:{TRIGGER.KEY1}
问题详情:{ITEM.NAME}:{ITEM.VALUE}
当前状态:{TRIGGER.STATUS}:{ITEM.VALUE1}
事件ID:{EVENT.ID}
```

<img alt="" height="614" src="https://img-blog.csdnimg.cn/59a6705c379c4517bd4590f865a4380f.png" width="994">

>  
 ** 更改触发器表达式以后收到的告警邮件应该就是刚才设置的动作选项里面的Default messages** 


<img alt="" height="542" src="https://img-blog.csdnimg.cn/c777b7f5bc584643a78a9c4c682d94da.png" width="787">

  **##############################################################################**

### 8、总结：

>  
 **发送邮件告警一共三步** 
 <h4 id="1%E3%80%81%E4%BF%AE%E6%94%B9%E9%BB%98%E8%AE%A4%E5%8F%91%E4%BB%B6email%E7%9A%84%E5%9C%B0%E5%9D%80%EF%BC%8C%E4%BF%AE%E6%94%B9%E4%B8%BA%E8%87%AA%E5%B7%B1%E7%9A%84%E5%8F%91%E4%BB%B6%E9%82%AE%E7%AE%B1">**1、修改默认发件email的地址，修改为自己的发件邮箱**</h4> 
 <h4 id="2%E3%80%81%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%8A%A8%E4%BD%9C%E6%9D%A5%E5%8C%B9%E9%85%8D%E8%AD%A6%E7%A4%BA%E5%BA%A6">**2、创建一个动作来匹配警示度**</h4> 


#### **2、创建一个动作来匹配警示度**

<img alt="" height="541" src="https://img-blog.csdnimg.cn/1b7b14485fc94fa9898305ea1eab58e5.png" width="863">

>  
 **动作警示度匹配到了以后就会进行操作，发送信息给用户组，通过邮件的方式 ** 


<img alt="" height="606" src="https://img-blog.csdnimg.cn/57cf49aa004d416eb02e9f320c05dbf3.png" width="1053">

#### 3、要设置用户的报警媒介，添加用户接收告警邮件的邮箱地址

<img alt="" height="323" src="https://img-blog.csdnimg.cn/c806babd33634d269e305880abf01f9c.png" width="834">




