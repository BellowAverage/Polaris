
--- 
title:  如何批量导出 WordPress 的文章？ 
tags: []
categories: [] 

---
做程序员四年多的时间里，写了 400 多篇的博客和笔记，全部发表在自己的个人网站上，本地很多都没有存档。

今天突发奇想，想把网站上的所有文章全部导出到本地，方便本地的查阅和内容更新。

但是找了一圈，至今都没有专门插件可以做这件事，最后没办法只能自己研究一下。

把任务梳理拆解一下：
1. 第一步：理清数据库表关系1. 第二步：导出 csv 数据到本地1. 第三步：编写脚本 将csv 的数据内容进行分门别类的整理生成 md 文件
### 1. 理清库表关系

首先明确我们的目标，是要将文章的 md 原文保存到本地，这就决定了我们需要这些数据：
- 文章标题：用做 md 文件名- 文章内容：文件保存的内容- 文章分类：同一类的文章置于同一目录下
文章的标题和内容，很容易就可以在 wordpress.wp_posts 表中查到，字段名分别是：
- post_title- post_content_filtered
最麻烦的要属文章的分类。

我找了一圈才知道 wordpress 是如何管理这些文章的。

原来在 wp_term_relationships 表中记录了每篇文章的 term_taxonomy_id，一篇文章会可能会有多个 term_taxonomy

<img src="https://img-blog.csdnimg.cn/img_convert/7dcdbd2640cbf4c750ab720522b0f29a.png" alt="">

为什么会有多个 term_taxonomy ？这个 term_taxonomy 又如何理解 呢？

taxonomy 中文解释就是分类的意思。

在 wordpress 中，term_taxonomy 有多种，包括类别（category）、标签（tag）和导航菜单（nav_menu）

它们都用的同一张表记录，存于 wp_term_taxonomy 表中。

<img src="https://img-blog.csdnimg.cn/img_convert/b151b2c4a625ee9aed8b992c720f33a2.png" alt="">

这个库表理顺后，写 SQL 语句的逻辑就清晰了

```
use wordpress;
select 
	p.post_title,t.name,p.post_content_filtered 
from wp_posts p, wp_term_relationships r,wp_terms t, wp_term_taxonomy tt 
	where p.id=r.object_id 
	and r.term_taxonomy_id=t.term_id 
	and tt.term_id=t.term_id 
	and tt.taxonomy='category';

```

### 2. 导出 csv 数据

从 MySQL 中导出 csv 数据，可以使用 into 语法，但这个语法需要设置 --secure-file-priv ，我嫌麻烦就没用使用它。

于是我打开我的数据库连接管理软件（DBeaver），输入上面的 SQL 语句，将查询的结果直接导出到本地的 posts.csv 文件中

<img src="https://img-blog.csdnimg.cn/img_convert/f4b9359bbf8d863a657603c7b9e6cdbd.png" alt="">

### 3. 整理数据成md文件

posts.csv 就三个数据

```
"post_title","name","post_content_filtered"

```

编写一个 Python 脚本来处理一下

```
import os
import csv

WORK_DIR = os.getcwd()


def set_post_dir():
    post_dir = os.path.join(WORK_DIR, category)
    if not os.path.exists(post_dir):
        os.mkdir(post_dir)
    os.chdir(post_dir)


with open('posts.csv', newline='') as csvfile:
    posts = csv.reader(csvfile)
    for post in posts:
        if post[1] == "name":
            continue
        post_title, category, post_content = post

        set_post_dir()
        try:
            with open(post_title+".md", "w") as post_file:
                post_file.write(post_content)
        except Exception as exp:
            print(exp)
            print(f"category: {<!-- -->category}")
            print(f"title: {<!-- -->post_title}")
            print(f"content: {<!-- -->post_content}")

```

运行完成后，在本地查看一下，每个分类都有一个目录

<img src="https://img-blog.csdnimg.cn/img_convert/6908758b0466f8e5be193abdac13ed3e.png" alt="">

而每个分类下都有各自文章的 markdown 原文

<img src="https://img-blog.csdnimg.cn/img_convert/e0173c1635c05d79ff956f45f028949a.png" alt="">
