
--- 
title:  promql怎么读promql详解 
tags: []
categories: [] 

---
PromQL（Prometheus Query Language）为Prometheus tsdb的查询语言。是结合grafana进行数据展示和告警规则的配置的关键部分。

## promQL详解

Prometheus提供了内置的数据查询语言PromQL（全称为Prometheus Query Language），支持用户进行实时的数据查询及聚合操作。

### PromQL基本介绍

Prometheus基于指标名称（metrics name）以及附属的标签集（labelset）唯一定义一条时间序列：

 - 指标名称代表着监控目标上某类可测量属性的基本特征标识
 - 标签则是这个基本特征上再次细分的多个可测量维度

时间序列数据：按照时间顺序记录系统、设备状态变化的数据，每个数据称为一个样本：

 - 数据采集以特定的时间周期进行，因而，随着时间流逝，将这些样本数据记录下来，将生成一个离散的样本数据序列
 - 该序列也称为向量（Vector）；而将多个序列放在同一个坐标系内（以时间为横轴，以序列为纵轴），将形成一个由数据点组成的矩阵

#### Prometheus数据模型

Prometheus中，每个时间序列都由指标名称（Metric Name）和标签（Label）来唯一标识，格式为“{=, …}”；

指标名称：通常用于描述系统上要测定的某个特征；

 &lt;
