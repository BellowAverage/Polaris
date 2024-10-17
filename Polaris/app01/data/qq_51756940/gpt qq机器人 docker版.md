
--- 
title:  gpt qq机器人 docker版 
tags: []
categories: [] 

---
自己基于ubuntu20.04+python3.87+nonebot2创建了一个镜像，可以将你的qq通过后台扫码登录变成gpt机器人，用到了gocqhttp、ChatGPT官方接口版两个插件

**1、拉取镜像**

```
docker pull nowindandmoon/qqgptbot:latest
```



**2、部署容器**

```
docker run -itd -p 8096:8096 \
-e GOCQ_WEBUI_USERNAME='admin' \
-e GOCQ_WEBUI_PASSWORD='admin' \
-e OPENAI_API_KEY='' \
-e OPENAI_MODEL_NAME='gpt-3.5-turbo-16k-0613' \
--name qqbot nowindandmoon/qqgptbot:latest

```

**参数解释**

**GOCQ_WEBUI_USERNAME**------后台登录用户名

**GOCQ_WEBUI_PASSWORD**------后台登录密码

**OPENAI_API_KEY**------OPENAI API KEY

**OPENAI_MODEL_NAME**------gpt模型

<img alt="" height="268" src="https://img-blog.csdnimg.cn/direct/03e834891d2447b1b8c1bb5bbe31b390.png" width="900">



**3、登录后台**

通过访问 <u>http://ip:8096/go-cqhttp</u> 进入后台，账号密码是

**GOCQ_WEBUI_USERNAME**和**GOCQ_WEBUI_PASSWORD。**

 <img alt="" height="588" src="https://img-blog.csdnimg.cn/26dff0e6e1fb4b63a026a20d5eca59ee.png" width="1200">



**4、登录qq**

点击提交

<img alt="" height="550" src="https://img-blog.csdnimg.cn/7cbd291125724021b4754a1402708c38.png" width="1153">



点击启动 

<img alt="" height="552" src="https://img-blog.csdnimg.cn/57ee9adae4fb4d5c954d629e00963417.png" width="991">

扫码登录

<img alt="" height="504" src="https://img-blog.csdnimg.cn/0e369ca827c541479174d44cd68b115c.png" width="948">



 登录成功

<img alt="" height="537" src="https://img-blog.csdnimg.cn/0ef61d8e0ec04596927e89e190f6d26f.png" width="1000">



**5、测试机器人**



<img alt="" height="173" src="https://img-blog.csdnimg.cn/fd946904b7414167a977dd9c72c3d67a.png" width="730">






























