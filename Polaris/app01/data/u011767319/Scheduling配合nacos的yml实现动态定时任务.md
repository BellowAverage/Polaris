
--- 
title:  Scheduling配合nacos的yml实现动态定时任务 
tags: []
categories: [] 

---
### ------------不带时区的自定义定时任务--------start--------

>  
 配置好nacos的yml动态配置，为前提 


### 配置nacos的yml

```
test:
	schedule:
	   #服务器为0时区，因此设置每天下午16点执行，相当于东8区的晚上12点
	   crons: {<!-- -->"guideUserSchedule":"0/20 * * * * ?"}
	   # 默认是115
	   min: 20

```

### 编写调用器

```
package app.ljq.service.admin.config.scheduled;

import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.SchedulingConfigurer;
import org.springframework.scheduling.config.ScheduledTaskRegistrar;
import org.springframework.stereotype.Component;

import java.util.Map;

/**
 * 定时任务配置
 */
//@RefreshScope - 使用这个会创建两个任务-弃用
@Component
@EnableScheduling
@Slf4j
public class ScheduledConfig implements SchedulingConfigurer, ApplicationContextAware {<!-- -->

    private ApplicationContext applicationContext;
    @Autowired
    private Crons crons;

    /**
     * 添加定时任务
     */
    @Override
    public void configureTasks(ScheduledTaskRegistrar scheduledTaskRegistrar) {<!-- -->
        crons.getCrons().forEach((beanId, cron) -&gt; {<!-- -->
            try {<!-- -->
                Runnable runnable = (Runnable) applicationContext.getBean(beanId);
                scheduledTaskRegistrar.addCronTask(runnable, cron);
            } catch (Exception e) {<!-- -->
                log.warn("实例化task失败[" + beanId + "]", e);
            }
        });
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {<!-- -->
        this.applicationContext = applicationContext;
    }

    @Configuration
    @ConfigurationProperties(prefix = "test")
    @Data
    @RefreshScope
    public static class Crons {<!-- -->
        public Map&lt;String, String&gt; crons;

        private Integer min = 115;
    }
}


```

### 编写任务

```
package app.ljq.service.admin.job;

import app.ljq.lib.mq.config.MqDefineConstant;
import app.ljq.lib.mq.domain.OfflineMessageDTO;
import app.ljq.lib.mq.rabbit.RabbitRouter;
import app.ljq.lib.mq.rabbit.RabbitSender;
import app.ljq.service.admin.config.scheduled.ScheduledConfig;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import java.time.LocalDateTime;
import java.util.concurrent.TimeUnit;

@Slf4j
@Component("guideUserSchedule") //指定值，方便上下文获取任务
public class GuideUserSchedule implements Runnable {<!-- -->
    @Resource
    private ScheduledConfig.Crons crons;
    
    @Override
    public void run() {<!-- -->
        //定义要延迟多少分钟
        int min = crons.getMin();
        //头像时间
        long avatarTime = TimeUnit.MINUTES.toMillis(getRandomMin(min));
        log.debug("offlineMessage: 上传头像信息触发的时间：{}, 现在时间：{}", avatarTime, LocalDateTime.now());
        RabbitSender.convertAndDelaySend(RabbitRouter.builder()
                        .exchange(MqDefineConstant.Exchange.OFFLINE_MESSAGE_DELAY_EXCHANGE)
                        .routingKey(MqDefineConstant.RoutingKey.OFFLINE_MESSAGE_DELAY_KEY).build(),
                OfflineMessageDTO.builder().type(OfflineMessageDTO.OfflineMessageType.UPLOAD_AVATAR_MESSAGE.name()).build(),
                avatarTime
        );
        //促活时间
        long promoteTime = TimeUnit.MINUTES.toMillis(getRandomMin(min));
        log.debug("offlineMessage: 促活信息触发的时间：{}, 现在时间：{}", promoteTime, LocalDateTime.now());
        RabbitSender.convertAndDelaySend(RabbitRouter.builder()
                        .exchange(MqDefineConstant.Exchange.OFFLINE_MESSAGE_DELAY_EXCHANGE)
                        .routingKey(MqDefineConstant.RoutingKey.OFFLINE_MESSAGE_DELAY_KEY).build(),
                OfflineMessageDTO.builder().type(OfflineMessageDTO.OfflineMessageType.GUIDE_USER_MESSAGE.name()).build(),
                promoteTime
        );
    }

    /**
     * 得到随机分钟数
     *
     * @param min 最小值
     * @return int
     */
    public int getRandomMin(int min) {<!-- -->
        return (int) (Math.random() * min + 5);
    }

}


```

### ------------不带时区的自定义定时任务--------end--------

### ------------带时区的自定义定时任务--------start--------

>  
 nacos 的yml 


```
static:
  schedule:
    crons:
      - {<!-- -->beanId: "countryDayStatsSchedule", cron: "0 0/5 * * * ?", ofHours: 8}

```

### 任务配置

```
package app.woya.service.statis.config.scheduled;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.SchedulingConfigurer;
import org.springframework.scheduling.config.CronTask;
import org.springframework.scheduling.config.ScheduledTaskRegistrar;
import org.springframework.scheduling.support.CronTrigger;
import org.springframework.stereotype.Component;

import java.time.ZoneOffset;
import java.util.List;
import java.util.TimeZone;

/**
 * 定时任务配置
 */
//@RefreshScope
@Component
@EnableScheduling
@Slf4j
public class ScheduledConfig implements SchedulingConfigurer, ApplicationContextAware {<!-- -->

    private ApplicationContext applicationContext;
    @Autowired
    private Crons crons;

    /**
     * 添加定时任务
     */
    @Override
    public void configureTasks(ScheduledTaskRegistrar scheduledTaskRegistrar) {<!-- -->
        crons.getCrons().forEach(baseCronsData -&gt; {<!-- -->
            try {<!-- -->
                Runnable runnable = (Runnable) applicationContext.getBean(baseCronsData.getBeanId());
                scheduledTaskRegistrar.addCronTask(
                        new CronTask(runnable,
                                new CronTrigger(
                                        baseCronsData.getCron(),
                                        TimeZone.getTimeZone(ZoneOffset.ofHours(baseCronsData.getOfHours()))
                                )
                        )
                );
            } catch (Exception e) {<!-- -->
                log.warn("实例化task失败[" + baseCronsData.getBeanId() + "]", e);
            }
        });
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {<!-- -->
        this.applicationContext = applicationContext;
    }

    @Configuration
    @ConfigurationProperties(prefix = "static.schedule")
    @Data
    @RefreshScope
    public static class Crons {<!-- -->
        public List&lt;BaseCronsData&gt; crons;
    }

    @NoArgsConstructor
    @Data
    public static class BaseCronsData {<!-- -->
        /**
         * runnable的类名
         */
        public String beanId;
        /**
         * cron
         */
        public String cron;
        /**
         * 时区
         */
        public Integer ofHours;
    }
}


```

### 任务

```
package app.ljq.service.statis.job;

import app.ljq.lib.redis.RedisKeyBaseBuilder;
import app.ljq.service.statis.service.user.ImCountryDayStatsService;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;
import java.time.LocalDate;
import java.time.ZoneOffset;

@Component("countryDayStatsSchedule")
public class CountryDayStatsSchedule implements Runnable {<!-- -->

    @Resource
    private RedissonClient redissonClient;
    @Resource
    private ImCountryDayStatsService imCountryDayStatsService;

    @Override
    public void run() {<!-- -->
        String key = RedisKeyBaseBuilder.build("stats", "countryDayStats", "schedule");
        RLock lock = redissonClient.getLock(key);
        try {<!-- -->
            if (lock.tryLock()) {<!-- -->
                LocalDate localDate = LocalDate.now().atStartOfDay(ZoneOffset.ofHours(8)).toLocalDate();
                imCountryDayStatsService.dealWithDailyUserNewData(localDate);
            }
        } finally {<!-- -->
            if (lock.isHeldByCurrentThread()) {<!-- -->
                lock.unlock();
            }
        }
    }

}


```

### ------------带时区的自定义定时任务--------end--------
