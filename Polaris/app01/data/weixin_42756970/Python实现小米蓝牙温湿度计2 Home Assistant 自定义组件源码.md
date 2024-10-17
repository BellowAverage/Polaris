
--- 
title:  Python实现小米蓝牙温湿度计2 Home Assistant 自定义组件源码 
tags: []
categories: [] 

---
## 小米 米家蓝牙温湿度计2

这是一个Home Assistant自定义组件，用于 Home Assistant 通过 蓝牙适配器 直接集成 小米 米家蓝牙温湿度计 (LYWSDCGQ/01ZM) 和 米家蓝牙温湿度计2 (LYWSD03MMC)。

v0.2.0-dev版本以后，已经支持自动发现功能，不需要任何配置。

不需要蓝牙网关。

<img src="https://img-blog.csdnimg.cn/858d6ad50300438db868f86681e1ad50.png" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-PhGsyqNE-1673577634095)(/pictures/LYWSD03MMC.jpg)]"> |<img src="https://img-blog.csdnimg.cn/900c83f2e4184cbdaf2b63c7f83df1d0.png" alt="[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-g5OwkMqy-1673577634096)(/pictures/LYWSDCGQ01ZM.jpg)]">

### 必要条件
<li>已支持和测试版本 HassOS 4.13 (HassOS Release-4 build 13 (Stable)) 
  <ul>- 注意: 版本HassOS 4.14 存在蓝牙缺陷，蓝牙设备无法连接.- 其它版本有待大家提交测试报告- 其它硬件有待大家提交测试报告
### 支持的设备

|Name|Model|Model no.
|------
|小米 米家蓝牙温湿度计||LYWSDCGQ/01ZM
|小米 米家蓝牙温湿度计2||LYWSD03MMC

### 功能

#### 米家蓝牙温湿度计 (LYWSDCGQ/01ZM)
<li>Attributes 
  <ul>- `temperature`- `humidity`- `battery`
#### 米家蓝牙温湿度计2 (LYWSD03MMC)
<li>Attributes 
  <ul>- `temperature`- `humidity`- `battery`
### 安装

你可以先在HACS设置菜单中，把这个库 () 添加到  . 你将在集成菜单中找到定制组件，然后查找关键字 ‘Xiaomi Mijia BLE Temperature Hygrometer 2 Integration’ 进行添加. 或者, 也可以通过将该自定义组件的 custom_component 文件夹，复制到 Home Assistant 的 config 文件夹.

### 设置 (**可选**)

v0.2.0-dev版本以后, 支持免配置自动发现，安装后即可自动找到符合条件的设备。

```
# configuration.yaml

sensor:
  - platform: mitemp_bt2
    mac: 'A4:C1:38:AA:AA:AA'
    mode: 'LYWSD03MMC'
    name: book room
    period: 60
  - platform: mitemp_bt2
    mac: 'A4:C1:38:FF:FF:FF'
    mode: 'LYWSD03MMC'
    name: living room
    period: 60

```

配置变量:
- **mac** (**Required**): The MAC of your device.- **mode** (**Optional**): The mode of your device. Default LYWSD03MMC- **name** (**Optional**): The name of your device.- **period** (**Optional**): The scan period of your device. Default 300 seconds.
### 面板显示

<img src="https://img-blog.csdnimg.cn/c2009f67cf604d9b8b3490ff08f7cfdd.png" alt="在这里插入图片描述">
