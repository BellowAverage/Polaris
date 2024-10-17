
--- 
title:  Python+Flask实现的学生培养计划管理系统 
tags: []
categories: [] 

---
### 项目功能
- 学生培养计划可视化，学生能够直观地了解个人的培养计划进度情况和学分信息，从而更加有针对性地选择课程。- 使用SVD算法，可根据其他用户的课程评价及选课情况，向用户个性化地推荐课程，分享志同道合的朋友。- 通过论坛模块，学生还可以在课程讨论区交流想法，答疑解。- 模拟选课退课，提前把握自己的学业进度.
### 项目目录

```
|—— sql         # 存放相关数据库sql语句
|—— static      # 存放静态资源文件
|—— |—— css    
|—— |—— images
|—— |—— js
|—— templates   # 存放html文件
|—— |—— *.html
|—— utils       # 存放一些功能函数
|—— config.py
|—— errors.py
|—— main.py
```

### 项目环境
- Python:3.x- mysql:5.7- Flask:1.0x- numpy
### 使用
- 克隆项目- 安装相关库
```
pip install Flask
pip install numpy
```
<li>初始化数据库<pre class="has"><code class="language-go">mysql -u 'userName' -p 
```python
- 创建数据库
```python
create database studenttrainplan;</code></pre><pre class="has"><code class="language-go">use studenttrainplan;
source schema.sql;
source insert_student.sql;
source insert_loginformation.sql;
source insert_education_plan.sql;
source insert_choose.sql;
source insert_edu_stu_plan.sql;</code></pre> 
   <ul>- 插入数据- 来到`sql/目录下`命令行进入mysql
回到主目录

```
config = {
    'default': Config,
    'MYSQL_PASSWORD': '123456',
    'DATABASE_NAME': 'studentTrainPlan'
}
```

```
python main.py
```
- 执行- 修改`config.py`中
打开浏览器,输入

```
localhost:5000
```

## 效果图

如果对本项目感兴趣，可以添加小二微信：**ityard**，备注**培养计划系统**

免费领取本项目源码****

<img src="https://img-blog.csdnimg.cn/img_convert/a5f57be3f409ac8a41179706769d4769.png" alt="a5f57be3f409ac8a41179706769d4769.png">

******长按识别上方********<img src="https://img-blog.csdnimg.cn/img_convert/845e20f1c61fd40851923a8001e1bae4.png" alt="845e20f1c61fd40851923a8001e1bae4.png">二维码添加小二微信**
