
--- 
title:  neo4j创建新数据库 
tags: []
categories: [] 

---
根据网上提供的教程，neo4j并没有提供创建数据库的命令，其只有一个默认数据库graph.db，该数据库中的所有数据将存储在neo4j安装路径下的data/databases/graph.db目录中。

因此，我们猜想，如果我们将默认数据库的名字修改成希望新建数据库的名字，那么，启动成功后，所使用的数据库即为新建的数据库，其数据也将在data/databases目录下，新建一个文件夹进行存储，该文件夹的名字即为新建数据库的名字。

那么，我们来实践一下：
- 打开conf目录下的neo4j.conf文件修改默认数据库名称<img alt="" height="87" src="https://img-blog.csdnimg.cn/direct/e44931d120f44731869d719372863262.png" width="337">- 启动neo4j<img alt="" height="205" src="https://img-blog.csdnimg.cn/direct/c4a9d128e7e54eac9d8c7d94392594f7.png" width="1093">- 访问
<img alt="" height="325" src="https://img-blog.csdnimg.cn/direct/92eb29ed268a44a09ef39de050f83edb.png" width="357">​
- 查看data/databases目录下是否以新建数据库名称新建了一个文件夹进行存储数据<img alt="" height="228" src="https://img-blog.csdnimg.cn/direct/06008fb18a984f9c94346d93eeef9a07.png" width="683">