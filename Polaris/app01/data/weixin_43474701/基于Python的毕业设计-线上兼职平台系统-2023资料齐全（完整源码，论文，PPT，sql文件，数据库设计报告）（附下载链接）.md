
--- 
title:  基于Python的毕业设计-线上兼职平台系统-2023资料齐全（完整源码，论文，PPT，sql文件，数据库设计报告）（附下载链接） 
tags: []
categories: [] 

---
### 基于Python的毕业设计-线上兼职平台系统（注释详细）



线上兼职平台系统主要功能模块包括系统后台首页、轮播图、网站公告管理、资源管理（兼职资讯、资讯分类）、交流管理（交流论坛、交流分类）、系统用户（管理员、注册用户、商家用户）、模块管理（职位分类、招聘兼职、兼职申请、交流询问），采取面对对象的开发模式进行软件的开发和硬体的架设，能很好的满足实际使用的需求，完善了对应的软体架设以及程序编码的工作，主要采取Mysql作为后台数据的主要存储单元，运用软件工程原理和开发方法，采用Python的Django技术进行业务系统的编码及其开发，实现了本系统的全部功能。

<img src="https://img-blog.csdnimg.cn/d186c9005bd44d2aa0415fb685eee0ab.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c70aa97d1c684d108c2bcd4cf4acca5b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/efd34d9378cb4e7aa651df8f1c218128.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/cbfee13e7b7c4cb29d7ada086035cb9f.png" alt="在这里插入图片描述"> 部分代码展示： from app.core import controller from app.service import service_select

controllerClass = getattr(controller, “Controller”)

## 管理后台

class Admin(controllerClass): def **init**(self, config={}): “”" 构造函数 @param {Object} config 配置参数 “”" config_init = {<!-- --> # 选择的模板那路径模板 “tpl”: “./admin/”, # 选择的服务 “service”: “admin”, } config_temp = config config_temp.update(config_init) super(Admin, self).**init**(config_temp)

```
# 用户数，访问次数，营业额，消费人数统计，销售量，订单数
def Index(self, ctx):
    # 分类文章数
    article_type_num = service_select("article").Count_group(
        {}, {"groupby": "type"}
    )
    # 最近7日注册用户
    register_7day = service_select("user").date_comput(
        {}, {"date_key": "create_time", "size": 7}
    )
    # 最近7日订单量
    order_7day = service_select("user").date_comput(
        {}, {"date_key": "create_time", "size": 7}
    )
    # 最近7日营业额
    revenue_7day = service_select("user").date_comput(
        {},
        {
            "date_key": "create_time",
            "method": "sum",
            "field": "price_count",
            "size": 7,
        },
    )
    # 最近7日总销量
    sales_7day = service_select("user").date_comput(
        {},
        {
            "date_key": "create_time",
            "method": "sum",
            "field": "price_count",
            "size": 7,
        },
    )
    # 商品分类销量
    goods_type_sales = service_select("goods").Sum_group(
        {}, {"groupby": "type", "field": "sales"}
    )

    model = {
        "result": {
            "article_type_num": article_type_num,
            "register_7day": register_7day,
            "order_7day": order_7day,
            "revenue_7day": revenue_7day,
            "sales_7day": sales_7day,
            "goods_type_sales": goods_type_sales,
        }
    }
    return ctx.render(self.config["tpl"] + "index" + ".html", model)

```


