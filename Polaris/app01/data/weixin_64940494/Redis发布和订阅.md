
--- 
title:  Redis发布和订阅 
tags: []
categories: [] 

---
#### 一、什么是Redis发布和订阅

        发布是指一个人需要把自己想说的发告诉别人就是发布的动作，他50.60年代时他可能需要写一封信然后投给邮局，这个动作就是发布。

        订阅是另外一个人需要知道别人对他说了什么，那么他就需要告知邮局我的信封是你这个邮局来传递的，同时从这个邮局拿到信这个就是订阅的操作。

        Redis的发布(pub)和订阅(sub)就是通过redis来传递消息的一种通信模式。

        在这里包含有三个角色分别是：发送者、订阅者、频道。

        发送者：需要传递消息的一方，发送者向指定的频道发送消息。

        订阅者：需要接收消息的一方，订阅者可以订阅一个或者多个频道中的消息。

        频道：发送者和订阅者之间用于传递消息是的通信渠道。

####  二、Redis发布和订阅的结构图

<img alt="" height="296" src="https://img-blog.csdnimg.cn/4de82e152de549048fa03c9b34589b6b.jpeg" width="555">

#### 三、订阅和发布的工作流程
- 发送者向一个或多个频道发送消息。- Redis将消息存储在内部缓冲区中，等待订阅者订阅相应的频道。- 订阅者通过订阅一个或多个频道。- 当有消息发送到已订阅的频道时，Redis将消息发送给订阅者。- 订阅者可以取消订阅某个频道，不再接收该频道的消息
#### 四、Redis发布和订阅的常用命令        

##### 1.  publish &lt;channel&gt; &lt;message&gt; 

发送消息到频道中，返回值代表订阅者的数量

<img alt="" height="75" src="https://img-blog.csdnimg.cn/cdbbe1e9353b4f6aa27b18419c2771dd.png" width="444">

#####  2. subscribe &lt;channel1&gt; &lt;channel2&gt; ....

订阅一个或多个频道

<img alt="" height="199" src="https://img-blog.csdnimg.cn/3688eda1f4d648839868268110cc5705.png" width="474">

##### 3. pubsub &lt;subcommand&gt; &lt;pattern&gt;

查看订阅和发布系统的状态

<img alt="" height="55" src="https://img-blog.csdnimg.cn/5e6a27b2f9a54987be90a4443adb9bcd.png" width="417">

<img alt="" height="91" src="https://img-blog.csdnimg.cn/cd36281c94f145fea1ce6770014b248b.png" width="572">

#####  4. unsubscribe &lt;channel1&gt; &lt;channel2&gt; ... 

取消指定的频道

<img alt="" height="67" src="https://img-blog.csdnimg.cn/ab412095178b4d4abb561fc8f8705035.png" width="560">

##### 5.  psubscribe  &lt;pattern&gt; 

订阅一个或多个符合给定模式的频道,支持指定和 * 匹配

##### 6.  punsubscribe &lt;pattern&gt;

退订一个或多个符合给定模式的频道,支持指定和 * 匹配

#### 五、应用场景

##### 1. 异步消息和任务推送

        业务流程状态变化时，可以使用发布和订阅功能做异步消息推送，以及下一环节任务推送功能。使用redis发布和订阅，应用系统旧不需要使用定时任务做推送功能。

##### 2. 系统订阅和关注

        在一些博客和直播的应用上可以使用redis发布和订阅用于用户对博文和主播的关注、收藏和订阅等操作。

#### 总结

        Redis的发布和订阅其实就是简单的实现了类似RabbitMQ消息队列，其作用都是实现异步和应用程序的解耦。在项目中最好还是使用专业的消息队列中间件，因为Redis的发布和订阅需要客户端保持持续的在线连接状态，如果出现中断就有数据的丢失。
