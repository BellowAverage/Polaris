
--- 
title:  服务器流量只有1tb，害怕被刷怎办，这篇文章教你防止对方刷流量！ 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解，服务器流量监控和关闭网络请求的方法教程，在某种情况下可以有效杜绝被刷流量的困扰。 日期：2023年10月2日 作者：任聪聪 


### 根本有效避免刷流的前置办法

<img src="https://img-blog.csdnimg.cn/787e1b4d75684e5080ddd33359807fee.png" alt="在这里插入图片描述"> 说明：只选择固定带宽，不限流量的服务器配置。不选择计费计量类型的服务器，这类服务器一般性价比很高，但是对于各类型攻击就很困扰了，先对比固定带宽类型的服务器，固定带宽本身就可以过滤大量的请求。

### 选择了计费计量服务器的解决办法

说明：linux环境下，可以安装bmon 进行流量的监控和管理，具体步骤如下：

#### 步骤一、安装bmon

```
sudo apt-get install bmon


```

#### 步骤二、执行如下命令

```
0 0 1 * * bash -c 'for i in $(seq 1 30); do bmon --read-bytes --write-bytes --bandwidth --time | grep "$(date -d "${i} days ago" +%b)"; done' | while read line; do if [[ $line == *"sent"* &amp;&amp; $line != *"sent"* ]] || [[ $line == *"recv"* &amp;&amp; $line != *"recv"* ]]; then echo "流量超过1TB，关闭网络！" &amp;&amp; sudo service network-manager stop; break; fi; done


```

说明：此命令为实现，本月1-30日的实际流量使用情况，可以根据自己的需求进行更改，定时检测时间也可自行更改，或自定义编辑成执行脚本均可，达到监控峰值后默认自动关闭网关，避免被刷。
