
--- 
title:  springboot集成seata个人笔记 
tags: []
categories: [] 

---
### 安装seata 本人是使用docker安装的

>  
 需要看怎么安装的请移步到 本人的文档 docker安装个人笔记观看 


### 集成seata 的基本配置
<li> 创建db储存（global_table，branch_table，lock_table），用于储存事务信息： <pre><code class="prism language-java">
-- -------------------------------- The script used when storeMode is 'db' --------------------------------
-- the table to store GlobalSession data
CREATE TABLE IF NOT EXISTS `global_table`
(
    `xid`                       VARCHAR(128) NOT NULL,
    `transaction_id`            BIGINT,
    `status`                    TINYINT      NOT NULL,
    `application_id`            VARCHAR(32),
    `transaction_service_group` VARCHAR(32),
    `transaction_name`          VARCHAR(128),
    `timeout`                   INT,
    `begin_time`                BIGINT,
    `application_data`          VARCHAR(2000),
    `gmt_create`                DATETIME,
    `gmt_modified`              DATETIME,
    PRIMARY KEY (`xid`),
    KEY `idx_gmt_modified_status` (`gmt_modified`, `status`),
    KEY `idx_transaction_id` (`transaction_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
 
-- the table to store BranchSession data
CREATE TABLE IF NOT EXISTS `branch_table`
(
    `branch_id`         BIGINT       NOT NULL,
    `xid`               VARCHAR(128) NOT NULL,
    `transaction_id`    BIGINT,
    `resource_group_id` VARCHAR(32),
    `resource_id`       VARCHAR(256),
    `branch_type`       VARCHAR(8),
    `status`            TINYINT,
    `client_id`         VARCHAR(64),
    `application_data`  VARCHAR(2000),
    `gmt_create`        DATETIME,
    `gmt_modified`      DATETIME,
    PRIMARY KEY (`branch_id`),
    KEY `idx_xid` (`xid`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
 
-- the table to store lock data
CREATE TABLE IF NOT EXISTS `lock_table`
(
    `row_key`        VARCHAR(128) NOT NULL,
    `xid`            VARCHAR(96),
    `transaction_id` BIGINT,
    `branch_id`      BIGINT       NOT NULL,
    `resource_id`    VARCHAR(256),
    `table_name`     VARCHAR(32),
    `pk`             VARCHAR(36),
    `gmt_create`     DATETIME,
    `gmt_modified`   DATETIME,
    PRIMARY KEY (`row_key`),
    KEY `idx_branch_id` (`branch_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
</code></pre> </li><li> 每个用到分布式事务的数据库都要建立 ，SEATA AT 模式需要 UNDO_LOG 表（本人使用的是at模式） <pre><code class="prism language-java">	-- 注意此处0.3.0+ 增加唯一索引 ux_undo_log
CREATE TABLE `undo_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `branch_id` bigint(20) NOT NULL,
  `xid` varchar(100) NOT NULL,
  `context` varchar(128) NOT NULL,
  `rollback_info` longblob NOT NULL,
  `log_status` int(11) NOT NULL,
  `log_created` datetime NOT NULL,
  `log_modified` datetime NOT NULL,
  `ext` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ux_undo_log` (`xid`,`branch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
</code></pre> </li>1.  springboot 项目中，在资源文件夹下面 需要建立 registry.conf 和 file.conf 1.  然后在所需添加事务的地方，加上 **@GlobalTransactional** 就行了 
### springboot 里需要配置什么呢
1. 需要配置yml文件
```
spring:
  cloud:
    alibaba:
      seata:
        tx-service-group: my_test_tx_group

```

2.需要在resources 下建立 file.conf文件

```
transport {<!-- -->
  # tcp udt unix-domain-socket
  type = "TCP"
  #NIO NATIVE
  server = "NIO"
  #enable heartbeat
  heartbeat = true
  # the client batch send request enable
  enableClientBatchSendRequest = true
  #thread factory for netty
  threadFactory {<!-- -->
    bossThreadPrefix = "NettyBoss"
    workerThreadPrefix = "NettyServerNIOWorker"
    serverExecutorThread-prefix = "NettyServerBizHandler"
    shareBossWorker = false
    clientSelectorThreadPrefix = "NettyClientSelector"
    clientSelectorThreadSize = 1
    clientWorkerThreadPrefix = "NettyClientWorkerThread"
    # netty boss thread size,will not be used for UDT
    bossThreadSize = 1
    #auto default pin or 8
    workerThreadSize = "default"
  }
  shutdown {<!-- -->
    # when destroy server, wait seconds
    wait = 3
  }
  serialization = "seata"
  compressor = "none"
}
service {<!-- -->
  #transaction service group mapping
  vgroupMapping.my_test_tx_group = "default"
  #only support when registry.type=file, please don't set multiple addresses
  default.grouplist = "192.168.37.1:8091"
  #degrade, current not support
  enableDegrade = false
  #disable seata
  disableGlobalTransaction = false
}

client {<!-- -->
  rm {<!-- -->
    asyncCommitBufferLimit = 10000
    lock {<!-- -->
      retryInterval = 10
      retryTimes = 30
      retryPolicyBranchRollbackOnConflict = true
    }
    reportRetryCount = 5
    tableMetaCheckEnable = false
    reportSuccessEnable = false
  }
  tm {<!-- -->
    commitRetryCount = 5
    rollbackRetryCount = 5
  }
  undo {<!-- -->
    dataValidation = true
    logSerialization = "jackson"
    logTable = "undo_log"
  }
  log {<!-- -->
    exceptionRate = 100
  }
}

```

3.需要在resources 下建立 registry.conf文件

```
registry {<!-- -->
  # file 、nacos 、eureka、redis、zk、consul、etcd3、sofa
  type = "nacos"

  nacos {<!-- -->
    application = "seata-server"
    serverAddr = "192.168.37.1:8848"
    namespace = ""
    username = "nacos"
    password = "nacos"
  }
  eureka {<!-- -->
    serviceUrl = "http://localhost:8761/eureka"
    weight = "1"
  }
  redis {<!-- -->
    serverAddr = "localhost:6379"
    db = "0"
    password = ""
    timeout = "0"
  }
  zk {<!-- -->
    serverAddr = "127.0.0.1:2181"
    sessionTimeout = 6000
    connectTimeout = 2000
    username = ""
    password = ""
  }
  consul {<!-- -->
    serverAddr = "127.0.0.1:8500"
  }
  etcd3 {<!-- -->
    serverAddr = "http://localhost:2379"
  }
  sofa {<!-- -->
    serverAddr = "127.0.0.1:9603"
    region = "DEFAULT_ZONE"
    datacenter = "DefaultDataCenter"
    group = "SEATA_GROUP"
    addressWaitTime = "3000"
  }
  file {<!-- -->
    name = "file.conf"
  }
}

config {<!-- -->
  # file、nacos 、apollo、zk、consul、etcd3、springCloudConfig
  type = "file"

  nacos {<!-- -->
    serverAddr = "localhost"
    namespace = ""
    group = "SEATA_GROUP"
    username = ""
    password = ""
  }
  consul {<!-- -->
    serverAddr = "127.0.0.1:8500"
  }
  apollo {<!-- -->
    appId = "seata-server"
    apolloMeta = "http://192.168.1.204:8801"
    namespace = "application"
  }
  zk {<!-- -->
    serverAddr = "127.0.0.1:2181"
    sessionTimeout = 6000
    connectTimeout = 2000
    username = ""
    password = ""
  }
  etcd3 {<!-- -->
    serverAddr = "http://localhost:2379"
  }
  file {<!-- -->
    name = "file.conf"
  }
}

```

### 运行成果

1.docker 容器中的日志 <img src="https://img-blog.csdnimg.cn/20200724000808231.png" alt="在这里插入图片描述"> 2.项目中 <img src="https://img-blog.csdnimg.cn/20200724000900437.png" alt="在这里插入图片描述">
