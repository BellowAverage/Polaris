
--- 
title:  PHP代码简单实现RabbitMQ 
tags: []
categories: [] 

---
        使用PHP代码实现RabbitMQ,主要是publisher.php(生产者)和consumer.php(消费者)。

**一、安装PHP AMQP扩展      **

  首先在PHP环境中需要先添加amqp扩展，这里演示的环境是windows环境，可以去PHP网站上下载相对应的dll文件，下载地址 。<img alt="" height="284" src="https://img-blog.csdnimg.cn/259171a7f2e646edb99811f21b92fa53.png" width="1088">

 大家根据自己的环境选择相对应的文件。

下载完解压后可以复制php_ampq.dll 和rabbitmq.4.dll 两个文件到PHP的ext目录下<img alt="" height="305" src="https://img-blog.csdnimg.cn/2117d051145e42d2a62e6927bfbb2a36.png" width="566">

在php.ini 文件中添加 extension=amqp 

<img alt="" height="115" src="https://img-blog.csdnimg.cn/0612ba0fe1ce49fc842aa77cbad85724.png" width="444">

重启apache后可以查看是否添加成功

<img alt="" height="320" src="https://img-blog.csdnimg.cn/6f6ee3bba38f488591ccfd7ab443450e.png" width="967"> 

 出现这个证明添加成功了。

**二、代码实现RabbitMQ**

1. publisher.php 生产者创建消息。

>  
 <pre>//创建连接rabbitmq
$config = [
   'host' =&gt; '127.0.0.1',
   'vhost' =&gt; '/',
   'port' =&gt; '5672',
   'login' =&gt; 'guest',
   'password' =&gt; 'guest'
];
$conn = new AMQPConnection($config);
if(!$conn-&gt;connect()){
   echo "连接失败";
   exit;
}
//创建通道
$channel  = new \AMQPChannel($conn);
//创建一个交换机
$exchange = new \AMQPExchange($channel);
//申明路由键
$routKey = 'key1';
//设置交换机名称
$exchangeName = "exchange1";
$exchange-&gt;setName($exchangeName);
//设置交换机类型
$exchange-&gt;setType(AMQP_EX_TYPE_DIRECT);

//数据持久化类型
$exchange-&gt;setFlags(AMQP_DURABLE);
//申明交换机
$exchange-&gt;declareExchange();

//创建消息
for($i=0 ; $i&lt;=5; $i++){
   $message = "message_".$i;
   //推送消息
   $exchange-&gt;publish($message,$routKey,AMQP_DURABLE);
}
exit;</pre> 


 2. consumer.php消费者接收消息

>  
 <pre>//创建连接rabbimq
$config = [
   'host' =&gt; '127.0.0.1',
   'vhost' =&gt; '/',
   'port' =&gt; '5672',
   'login' =&gt; 'guest',
   'password' =&gt; 'guest'
];
$conn = new AMQPConnection($config);
if(!$conn-&gt;connect()){
   echo "连接失败";
   exit;
}
//创建通道
$channel  = new \AMQPChannel($conn);
//创建一个交换机
$exchange = new \AMQPExchange($channel);
//申明路由键
$routKey = 'key1';
//设置交换机名称
$exchangeName = "exchange1";
$exchange-&gt;setName($exchangeName);
//设置交换机类型
$exchange-&gt;setType(AMQP_EX_TYPE_DIRECT);

//数据持久化类型
$exchange-&gt;setFlags(AMQP_DURABLE);
//申明交换机
$exchange-&gt;declareExchange();

//创建队列
$queue = new \AMQPQueue($channel);
//设置队列的名称
$queue-&gt;setName('queue01');
//设置队列的持久
$queue-&gt;setFlags(AMQP_DURABLE);
$queue-&gt;declareQueue();

//队列绑定交换机通过路由键绑定
$queue-&gt;bind($exchange-&gt;getName(),$routKey);

//监听消息队列
$queue-&gt;consume(function($envelope,$queue){
   echo $envelope-&gt;getBody()."\n";
});

exit;</pre> 


以上代码使用PHP简单的实现了RabbitMQ的消息推送和消息接收。
