
--- 
title:  linux安装单机版redis详细步骤，及python连接redis案例 
tags: []
categories: [] 

---


#### 文章目录
- <ul><li><ul><li>- - - - - 


#### linux相关工具

```
./redis-benchmark     #用于进行redis性能测试的工具 
./redis-check-dump    #用于修复出问题的dump.rdb文件	
./redis-cli           #redis的客户端
./redis-server        #redis的服务端
./redis-check-aof     #用于修复出问题的AOF文件
./redis-sentinel      #用于集群管理


```

#### yum方式安装redis

yum安装版本固定，不能达到我们的需求

```
yum -y install redis

```

#### 使用编译安装redis

```


mkdir -p /data/application     //创建工作目录

cd  /data/application
wget http://download.redis.io/releases/redis-5.0.10.tar.gz   //下载redis

tar xf redis-5.0.10.tar.gz    //解压

mv redis-5.0.10/ redis

cd redis/

yum install -y gcc make     //安装编译工具

make       //编译安装

cp redis.conf redis.conf.bak     //备份编译后的配置文件

vim redis.conf     //配置文件
bind 0.0.0.0　　          #所有ip可以访问
daemonize yes　　　　    　#开启后台模式将on改为yes
timeout 300　　　　　　    #连接超时时间
port 6379                #端口号
dir /data/application/redis/data　　#本地数据库存放持久化数据的目录该目录-----需要存在
pidfile /var/run/redis_6379.pid　　 #定义pid文件存放位置
logfile /var/log/redis.log　　      #定义log文件存放位置

创建存放数据的目录
mkdir -p /data/application/redis/data


```

#### 配置redis为systemctl启动

```
cd /lib/systemd/system
vim redis.service

[Unit]
Description=Redis
After=network.target

[Service]
ExecStart=/data/application/redis/src/redis-server /data/application/redis/redis.conf --daemonize no 
ExecStop=/data/application/redis/src/redis-cli shutdown 

[Install]
WantedBy=multi-user.target
===================================
参数详解:
[Unit] 表示这是基础信息 
Description 是描述
After 是在那个服务后面启动，一般是网络服务启动后启动

[Service] 表示这里是服务信息 
ExecStart 是启动服务的命令
ExecStop 是停止服务的指令

[Install] 表示这是是安装相关信息 
WantedBy 是以哪种方式启动：multi-user.target表明当系统以多用户方式（默认的运行级别）启动时，这个服务需要被自动运行。
=====================================
启动服务:
systemctl daemon-reload
systemctl start redis.service


配置环境变量启动
vim /etc/profile
export PATH=$PATH:/redis文件目录/src

source /etc/profile    刷新环境变量文件


启动
redis/src/redis-server redis/redis.conf --daemonize yes   //本机


停止
redis/src/redis-cli shutdown    //本机
redis/src/redis-cli -h ip -p 端口  shutdown 


```

#### 其它: 安装redis6.0

```
# 下载压缩包
wget https://download.redis.io/releases/redis-6.2.1.tar.gz

# 解压
tar xzf redis-6.2.1.tar.gz

# 进入压缩包
cd redis-6.2.1

# 编译安装
make

# 终端启动
src/redis-server

# 进入redis终端界面
src/redis-cli
redis&gt; set foo bar
OK
redis&gt; get foo
"bar"

# 启动，进入redis安装目录: /home/xxx/redis-6.2.1 ,执行：
nohup src/redis-server &amp;

# 关闭保护模式和设置密码，如下设置密码为：redisxxx，然后退出
src/redis-cli
redis&gt;config get protected-mode
redis&gt;config set protected-mode no
redis&gt;config get requirepass
redis&gt;config set requirepass "redisxxx"
redis&gt;quit

# 再访问终端时需要加上密码
src/redis-cli -a redisxxx

```

#### python连接redis案例

```
# -*- encoding: utf-8 -*-
import time
import redis

# 连接方式一: 直接连接Redis数据库
client = redis.Redis(host='123.56.xx.xx', port=6379, password='redisredis', db=2, decode_responses=True)
# print(client)
# 连接方式二: 创建Redis连接池，用于管理所有连接，避免每次建立、释放连接的开销
# pool = redis.ConnectionPool(host='123.56.67.212', port=6379, decode_responses=True)
# client = redis.Redis(connection_pool=pool)


# 连接数据库
# client = redis.StrictRedis(host='123.56.67.212', port=6379, password='redisredis', db=1)


def write_str():
    """# 写入字符串类型的数据"""
    client.set('name11', 'Django11')
    # 获取name的数据
    print('获取数据方法一：', client['name11'])
    # print('获取数据方法二：', client.get('name'), client.get('name').decode())

    client.set(name='string', value='Python')
    # 获取字符串的数据
    print('获取字符串的数据：', client['string'])
    print('获取字符串的数据：', client.get('string'))


def write_hset():
    # 写入散列类型的数据
    # client.hset(name='hash', key='name', value='Tom')
    # client.hset(name='hash', key='age', value=10)
    # client.hset(name='hash', key='address', value='UK')
    # # 获取散列的数据
    # print('获取散列的数据：', client.hget(name='hash', key='name'))

    with client.pipeline(transaction=False) as pipe:
        start = time.time()
        for i in range(1, 10000):
            pipe.lpush('num_data', f'num{<!-- -->i}')
            # pipe.hset()
            if i % 100 == 0:
                try:
                    res = pipe.execute()
                    print(res)
                except Exception as e:
                    print(e)
        print("程序耗时：", time.time() - start)


    # # 创建管道对象
    # pipe = client.pipeline()
    # client.hset(name='my_hmset', key='zhangsan', value=0)
    # client.hset(name='lisi', key='zhangsan', value=0)
    # client.hset(name='wangwu', key='zhangsan', value=0)
    # client.hset(name='zhaoliu', key='zhangsan', value=0)
    # ret = pipe.execute()
    #

    # client.hset(name='data_type', key='size', value='Tom')
    # client.hset(name='data_type', key='num', value=10)
    # # 获取散列的数据
    # print('获取散列的数据：', client.hget(name='hash', key='name'))


def write_list():
    # 写入列表类型的数据: 将元素写入列表的左边
    client.lpush('list', 'Mr Li', 'Miss Lu')
    # 将元素写入列表的右边
    client.rpush('list', 'Miss Wang', 'Mir Zhang')
    # 获取列表的数据
    # lpop()从最左边获取元素，数据获取后在数据库中移除
    print('获取列表的数据：', client.lpop('list'))
    # rpop()从最右边获取元素，数据获取后在数据库中移除
    print('获取列表的数据：', client.rpop('list'))


def write_set():
    # 写入集合类型的数据
    client.sadd('set', 'UK', 'CN', 'US', 'JP')
    # 获取集合的数据
    print('获取集合的数据：', client.smembers('set'))

    # # 写入有序集合类型的数据，每个数据设有权重，权重以整数表示
    # client.zadd(name='sord_set', mapping={'GZ': 1, 'BJ': 2, 'SZ': 3, 'SH': 4})
    # # 获取有序集合的数据
    # print('获取有序集合的数据：', client.zrange('sord_set', 0, -1))


def write_bytes():
    # 写入位图类型的数据
    # 将bytes的数据设为字符串数据
    client.set(name='bytes', value='Python')
    print('二进制数据的第二位数为：', client.getbit(name='bytes', offset=1))
    # setbit()将字符串数据转为二进制数据，然后将第二位数改为0
    client.setbit(name='bytes', offset=1, value=0)


def write_stream():
    # 写入流类型的数据
    stream_id = client.xadd(name='stream', fields={<!-- -->'name': 'Tom'})
    # 获取流数据的id
    print('获取流数据的id：', stream_id)
    stream_id = client.xadd(name='stream', fields={<!-- -->'msg': 'Hello Python'})
    # 获取流数据的id
    print('获取流数据的id：', stream_id)


if __name__ == '__main__':
    # write_str()
    # write_hset()
    # write_list()
    write_set()
    # write_bytes()
    # write_stream()


```
