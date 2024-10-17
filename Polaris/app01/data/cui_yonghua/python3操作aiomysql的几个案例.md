
--- 
title:  python3操作aiomysql的几个案例 
tags: []
categories: [] 

---
官方文档：

github：

#### 查询案例

```
import asyncio
import aiomysql


async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='', db='mysql',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT Host,User FROM user")
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))

```

#### 连接池

```
import asyncio
import aiomysql


async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 42
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))

```

#### 插入多条

```
import asyncio
import aiomysql


async def test_example_executemany(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='',
                                       db='test_pymysql', loop=loop)

    cur = await conn.cursor()
    async with conn.cursor() as cur:
        await cur.execute("DROP TABLE IF EXISTS music_style;")
        await cur.execute("""CREATE TABLE music_style
                                  (id INT,
                                  name VARCHAR(255),
                                  PRIMARY KEY (id));""")
        await conn.commit()

        # insert 3 rows one by one
        await cur.execute("INSERT INTO music_style VALUES(1,'heavy metal')")
        await cur.execute("INSERT INTO music_style VALUES(2,'death metal');")
        await cur.execute("INSERT INTO music_style VALUES(3,'power metal');")
        await conn.commit()

        # insert 3 row by one long query using *executemany* method
        data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
        await cur.executemany(
            "INSERT INTO music_style (id, name)"
            "values (%s,%s)", data)
        await conn.commit()

        # fetch all insert row from table music_style
        await cur.execute("SELECT * FROM music_style;")
        result = await cur.fetchall()
        print(result)

    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_executemany(loop))

```

#### 事务操作

```
import asyncio
import aiomysql


async def test_example_transaction(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='',
                                  db='test_pymysql', autocommit=False,
                                  loop=loop)

    async with conn.cursor() as cursor:
        stmt_drop = "DROP TABLE IF EXISTS names"
        await cursor.execute(stmt_drop)
        await cursor.execute("""
            CREATE TABLE names (
            id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(30) DEFAULT '' NOT NULL,
            cnt TINYINT UNSIGNED DEFAULT 0,
            PRIMARY KEY (id))""")
        await conn.commit()

        # Insert 3 records
        names = (('Geert',), ('Jan',), ('Michel',))
        stmt_insert = "INSERT INTO names (name) VALUES (%s)"
        await cursor.executemany(stmt_insert, names)

        # Roll back!!!!
        await conn.rollback()

        # There should be no data!
        stmt_select = "SELECT id, name FROM names ORDER BY id"
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        # Check there is no data
        assert not resp

        # Do the insert again.
        await cursor.executemany(stmt_insert, names)

        # Data should be already there
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        print(resp)
        # Do a commit
        await conn.commit()

        await cursor.execute(stmt_select)
        print(resp)

        # Cleaning up, dropping the table again
        await cursor.execute(stmt_drop)
        await cursor.close()
        conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_transaction(loop))

```

#### sa操作

```
import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
               sa.Column('id', sa.Integer, primary_key=True),
               sa.Column('val', sa.String(255)))


async def create_table(engine):
    async with engine.acquire() as conn:
        await conn.execute('DROP TABLE IF EXISTS tbl')
        await conn.execute('''CREATE TABLE tbl (
                              id serial PRIMARY KEY,
                              val varchar(255))''')


async def go(loop):
    engine = await create_engine(user='root', db='test_pymysql',
                                 host='127.0.0.1', password='', loop=loop)
    await create_table(engine)
    async with engine.acquire() as conn:
        await conn.execute(tbl.insert().values(val='abc'))
        await conn.execute(tbl.insert().values(val='xyz'))

        async for row in conn.execute(tbl.select()):
            print(row.id, row.val)

        await conn.execute("commit")

    engine.close()
    await engine.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))

```
