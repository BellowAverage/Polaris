
--- 
title:  springcloud 整合seata、nacos 
tags: []
categories: [] 

---
### springcloud 整合seata、nacos

版本： nacos:nacos-server-2.0.3.zip seata: seata-server-1.2.0.zip mysql: 5.6.28 项目地址：
1.  下载 seata并解压： https://gitee.com/qinenqi/parent seata下载地址： https://seata.io/zh-cn/blog/download.html <img src="https://img-blog.csdnimg.cn/2e187e69cc364bf58c5d0962631d83cb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 1.  把 doc里面的 config.txt、nacos-config.sh、registry.conf的文件全部放在 seata\conf 目录下 <img src="https://img-blog.csdnimg.cn/b1d3f7228df347b0a16bb8a59902123a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_19,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/17c4fe2c84f24e82a42db0c7fbe319bf.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 1.  根据自己的情况更改配置 config.txt <img src="https://img-blog.csdnimg.cn/51f70dd1154a4b4b8d73d334f8b80b5b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 1.  在 conf 下，打开git客户端执行：(再推送之前请先启动 nacos) 
```
sh nacos-config.sh 127.0.0.1

```

把配置项推到 nacos上 <img src="https://img-blog.csdnimg.cn/6596cc67408f4e5a922d206109529eb0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/602031fc439946ceb91a64f629e3a398.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 5. 启动 seata seata\bin目录下，双击 seata-server.bat <img src="https://img-blog.csdnimg.cn/e5d2bc61b07a4ccd82005b3395eeff0c.png" alt="在这里插入图片描述"> 6. 新建一个简单的项目，包括parent、business、service01、service02 需要留意的一点就是 <img src="https://img-blog.csdnimg.cn/597d6b695a24473cb802ede20f5026a7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> tx-service-group: my_test_tx_group要与config.txt一致 <img src="https://img-blog.csdnimg.cn/1506210c85d64839b621395d72c81143.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA56eL5Y-25riF6aOO,size_20,color_FFFFFF,t_70,g_se,x_16" alt="在这里插入图片描述"> 7. 测试项目： business 调用 service01 和service02， 不管哪个服务出现异常，三个服务的数据库都回滚
