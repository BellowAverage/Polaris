
--- 
title:  基于树莓派4B和Python语言的人脸识别追逃预警项目(天网追逃小demo) 
tags: []
categories: [] 

---
 https://blog.csdn.net/meenr/article/details/118735409



#### 目录
- - <ul><li>- - <ul><li>- - - - - - <ul><li>


## 基于树莓派4B和Python语言的人脸识别预警项目(天网追逃小demo)

### 效果演示

**视频地址：**  https://www.bilibili.com/video/BV1Z64y1W7Ab/  https://mp.weixin.qq.com/s/5Um-3LlMt6v_CUwUEh6HdA

### 设计背景

#### 天网监控系统

百度百科关于的表述： 天网工程是指为满足城市治安防控和城市管理需要，利用GIS地图、图像采集、传输、控制、显示等设备和控制软件组成，对固定区域进行实时监控和信息记录的视频监控系统。天网工程通过在交通要道、治安卡口、公共聚集场所、宾馆、学校、医院以及治安复杂场所安装视频监控设备，利用视频专网、互联网、移动等网络通网闸把一定区域内所有视频监控点图像传播到监控中心（即“天网工程”管理平台），对刑事案件、治安案件、交通违章、城管违章等图像信息分类，为强化城市综合管理、预防打击犯罪和突发性治安灾害事故提供可靠的影像资料。 公安机关通过监控平台，可以对城市各街道辖区的主要道路、重点单位、热点部位进行24小时监控，可有效消除治安隐患，使发现、抓捕街面现行犯罪的水平得到提高。

#### 人脸识别追逃

人脸识别追逃技术被大家广为熟知应该是因为在张学友——“追逃大神”的多次演唱会上大展身手。 张学友演唱会的“逃犯八连杀”连同“半年的积蓄，买了手铐一对”的调侃引发社会热议。警方在张学友演唱会安检时使用人脸识别技术抓捕到8位潜逃多年的犯人，不得不让人承认如今人脸识别技术的强大。 人脸识别追逃系统，是通过应用高度成熟的人脸识别技术，实现监控场景中，在目标非配合的情况下，抓取并识别所有监控目标的人脸，并与数据库中的人脸名单匹配，用于抓取逃犯、识别重要人物等，辅助监控人员、公安人员对现场实时的安全防范工作，以及案发后抓取现场人脸分析嫌疑人身份，进行破案证据搜集。监控场景的人脸追逃是人脸识别的重要应用，是高度成熟的人脸识别技术所驱动的追逃系统。

### 设计要求

参考天网系统与人脸识别追逃系统，设计模型实现初步功能，模拟出人脸识别追逃类似效果。

### 技术路线

#### 功能设计

1、能够读取本地文件夹中保存的“嫌疑人”人脸图像或调用摄像头实时采集人脸数据； 2、能够对读取的原人脸数据进行预处理，归一化，包括重命名、文件后缀为.jpg或.png、图像尺寸灰度为200x200像素； 3、能够识别出“嫌疑人”并以合理的方式给出必要的预警提示信息； 4、其他可完善的扩展功能。

#### 方案设计

<img src="https://img-blog.csdnimg.cn/814b7316cd76471c8622b4894315e656.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_50,color_222FFF,t_70#pic_center" alt="请添加图片描述" width="400" height="250">

### 软硬件需求

#### 硬件需求

开发平台：树莓派4B，4G内存，32G TF卡。 摄像头：500万+像素CSI摄像头或USB摄像头。 显示：HDMI接口显示屏或显示器。 音频：扬声器或音响。 输入：键盘和鼠标。

#### 软件需求

##### 系统环境

操作系统：Raspbian 开发语言：Python3.7.3 开发工具：Thonny

如果您需要本文的相关资料或者其它意见与建议，可通过下面方式联系：

扫描下方二维码，加入 2贰进制社区 学习交流QQ群“ **480558240** ”，下载群文件或者联系管理员咨询。 <img src="https://img-blog.csdnimg.cn/20210501161747688.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="QQ群" width="250" height="300">

也可扫描下方二维码，或打开微信搜索并关注“ **2贰进制** ”公众号，回复：“ **追逃小demo** ”； <img src="https://img-blog.csdnimg.cn/2020070300554991.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="二维码" width="200" height="200"> **2贰进制–Echo 20201年7月** 如果您觉得本文还不错，请点赞＋评论＋收藏，要是关注那更我极大地荣幸！ 如果本文对你有所帮助，解决了您的困扰，可以通过赞赏来请我吃包辣条： <img src="https://img-blog.csdnimg.cn/20210424133535613.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21lZW5y,size_16,color_FFFFFF,t_70#pic_center" alt="在这里插入图片描述" width="500" height="250">

参考文献： [1] https://baike.baidu.com/item/%E5%A4%A9%E7%BD%91%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F [2 ] https://baijiahao.baidu.com/s?id=1606591829790048900&amp;wfr=spider&amp;for=pc [3] https://www.1633.com/act/742/collegeproject/415/
