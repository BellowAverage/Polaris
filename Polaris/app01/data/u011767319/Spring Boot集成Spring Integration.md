
--- 
title:  Spring Boot集成Spring Integration 
tags: []
categories: [] 

---
### 导包

```
&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
    &lt;artifactId&gt;spring-boot-starter-integration&lt;/artifactId&gt;
&lt;/dependency&gt;

```

### QueueChannel 的简单使用

**配置**

```
@Configuration
@IntegrationComponentScan
public class SpringIntegrationConfig {

    @Bean
    public QueueChannel synDingtalkOrganQueueChannel() {
        return new QueueChannel();
    }

}

```

**发送消息**

```
@Autowired
private QueueChannel synDingtalkOrganQueueChannel;

```

**消费消息**

```

@Component
public class SynDingtalkOrganReceiver {

		@Resource
		private ExecutorService executorService;
		
		@ServiceActivator(inputChannel = "synDingtalkOrganQueueChannel", poller = @Poller)
   		 public void onMessage(Long userId) {
	         executorService.execute(() -&gt; {
	            /**
	             *  处理数据
	           	 * */
	       	  });
    	  }
}

```
