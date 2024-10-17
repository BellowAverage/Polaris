
--- 
title:  在ubuntu上搭建系统监控系统 
tags: []
categories: [] 

---


#### 大纲
- - <ul><li>- - - - - - - - <ul><li>- - - 


在一个监控系统中，一定会有“数据生产方”和“数据消费方”存在。“数据生产方”用于产出需要监控的相关指标数据；“数据消费方”使用这些数据产生额外的信息和功能，比如数据图表化表达、异常数据预警等。 <img src="https://img-blog.csdnimg.cn/direct/299cc3ded5a4417bbe9d0e0908cfb8a8.png" alt="请添加图片描述"> 当“数据生产方”变多时，系统往往会演化出“数据收集方”用于统一收集数据。这个时候“数据消费方”可以通过“数据收集方”获得全部数据。 <img src="https://img-blog.csdnimg.cn/direct/de7b221ff0ad41e992c37a45d40512d7.png" alt="请添加图片描述"> 当“数据消费方”变多时，不同的“数据消费方”会有不同诉求。比如有的只要A“数据生产方”的数据；有的既要A的、也要B的数据。于是整个系统又会演化出“数据分发方”，用于满足消费方的不同诉求。 <img src="https://img-blog.csdnimg.cn/direct/c5a195dd7518451eaae876a2006ae027.png" alt="在这里插入图片描述"> 随着数据越来越多，且生产和消费并非一定要紧密连接，在“数据收集方”和“数据分发方”之间就会演化出“数据仓储方”。它的出现让“数据收集方”和“数据分发方”实现了解耦，且提升了系统的健壮性。 <img src="https://img-blog.csdnimg.cn/direct/5f3090113d7f49a0915082295a1bd84a.png" alt="在这里插入图片描述"> 在实际生产中，我们往往使用prometheus和grafana来实现该系统中重要的两部分。 prometheus主要用于收集、存储和分发数据。虽然prometheus可以展现数据，但是功能并不强大，所以将其限定在非消费区域。 grafana主要用于消费数据。主要体现就是各种报表形式展现数据，以及提供一些基于规则数据告警。 <img src="https://img-blog.csdnimg.cn/direct/d5745f21c6384d128e2d8b80b1c8bff9.png" alt="在这里插入图片描述"> “数据生产方”需要给prometheus提供规定协议的数据。本文我们并不对此进行介绍，而是专注于将系统搭建和验证。为了简单起见，我们选用了prometheus开源项node_exporter作为“数据生产方”。

## 数据生产方

### 安装和运行

下载并解压node_exporter。（可以从找到最新的版本）

```
wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz 
tar xvfz node_exporter-1.7.0.linux-amd64.tar.gz 

```

运行node_exporter

```
cd node_exporter-1.7.0.linux-amd64/
./node_exporter

```

### 验证

在本机上使用localhost:9100/metrics(跨环境使用，则配置IP)访问node_exporter产生的数据。 <img src="https://img-blog.csdnimg.cn/direct/f62f089371ce42b0b6a46efe847dd4d1.png" alt="在这里插入图片描述">

## 数据收集、存储和分发方

### 下载和解压

下载并解压prometheus。（可以在找到最新版）

```
wget https://github.com/prometheus/prometheus/releases/download/v2.51.0/prometheus-2.51.0.linux-amd64.tar.gz .
tar -zvxf prometheus-2.51.0.linux-amd64.tar.gz

```

### 修改配置

进入prometheus目录下可以找到prometheus.yml

```
cd prometheus-2.51.0.linux-amd64/

```

修改prometheus.yml文件，新增对node_exporter的监控。 原来的部分配置

```
scrape_configs:
  # The job name is added as a label `job=&amp;lt;job_name&amp;gt;` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]

```

修改后的配置

```
scrape_configs:
  # The job name is added as a label `job=&amp;lt;job_name&amp;gt;` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
      - targets: ["localhost:9090"]
  - job_name: "node_exporter"
    static_configs:
      - targets: ["localhost:9100"]

```

### 运行

通过指定配置的方式启动prometheus。

```
./prometheus --config.file=./prometheus.yml 

```

### 验证

在本机上使用localhost:9090(跨环境使用，则配置IP)访问prometheus后台页面。 <img src="https://img-blog.csdnimg.cn/direct/1ff818b11641487facea34af04bb73a4.png" alt="在这里插入图片描述"> 可以看到node_exporter已经被监控。 <img src="https://img-blog.csdnimg.cn/direct/a7a050d228574730be3efb69923b59e3.png" alt="在这里插入图片描述">

我们还可以在图形化（Graph）的输入框中输入以下指令查看数据图表展现效果。

|Metric|Meaning
|------
|rate(node_cpu_seconds_total{mode=“system”}[1m])|在最后一分钟内，每秒在系统模式下花费的平均CPU时间（以秒为单位）
|node_filesystem_avail_bytes|非root用户可用的文件系统空间（以字节为单位）
|rate(node_network_receive_bytes_total[1m])|最后一分钟内每秒接收的平均网络流量（以字节为单位）

<img src="https://img-blog.csdnimg.cn/direct/b7e14154f0fd4d3796dc20bbf7011187.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/7c8ce74944284fb4bfdd5b9b07a7c3e9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/13d5d80484474075b6654cbd49921100.png" alt="在这里插入图片描述">

## 数据消费方

prometheus虽然可以配置一些看板和告警，但是可视化并不是它的核心。于是我们引入效果更好的grafana来做“数据消费方”。

### 下载和运行

下载并解压grafana。（可以在找到最新版）

```
wget https://dl.grafana.com/enterprise/release/grafana-enterprise-10.4.1.linux-amd64.tar.gz
tar -zxvf grafana-enterprise-10.4.1.linux-amd64.tar.gz
cd grafana-v10.4.1/
./bin/grafana server

```

### 验证

在本机上使用localhost:3000(跨环境使用，则配置IP)访问grafana后台页面。 第一次登录时，我们可以使用admin名称登录，密码也是admin。进入这个账号后会提示修改初始密码，我们还是设置为admin以方便记忆。

#### 新增数据源

我们要让grafana连接prometheus，以提供数据。具体操作如下 <img src="https://img-blog.csdnimg.cn/direct/0e01ac83758a4f7487219964afac99cb.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/fb1cdb4084a1419496f1138aaa579c03.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/306d27496a4a4caa97c56db3bc21c4be.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a512fc8384e04dca93bed63c4335cfbf.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/ef06bbd26e174240a54915224630ef27.png" alt="在这里插入图片描述">

#### 新增看板

<img src="https://img-blog.csdnimg.cn/direct/2c606c9fa8c04b6b8de44bb41ac3fc23.png" alt="在这里插入图片描述"> 我们到grafana官网上找为node_exporter定制的开源看板。 <img src="https://img-blog.csdnimg.cn/direct/1f9559026e0d418388b5f286ea316fde.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/318aeb7943b1437caaa01324eab628d7.png" alt="在这里插入图片描述"> 把上一步看板网页地址https://grafana.com/grafana/dashboards/1860-node-exporter-full/复制到下图的输入框中，以加载它。 <img src="https://img-blog.csdnimg.cn/direct/54531c8710cf4033930a5b56f48ae45e.png" alt="在这里插入图片描述">

#### 关联看板和数据源

上个页面往下滚动，可以看到输入数据源的地方。我们选择之前步骤创建的prometheus。 <img src="https://img-blog.csdnimg.cn/direct/62a6fdaa9eed4129987ca09ca317c61d.png" alt="在这里插入图片描述">

#### 效果展现

<img src="https://img-blog.csdnimg.cn/direct/f9c45604a7234c45b8e185033dc3b863.png" alt="在这里插入图片描述">

## 参考资料
- - - - - 