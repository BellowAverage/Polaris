
--- 
title:  纯 Python 搭建全文搜索引擎 
tags: []
categories: [] 

---
有一个群友在群里问个如何快速搭建一个搜索引擎，在搜索之后我看到了这个

<img src="https://img-blog.csdnimg.cn/img_convert/1b3520953418eed075fa8a3cfffcca64.png" title="">

### # 代码所在
- Git:https://github.com/asciimoo/searx
官方很贴心，很方便的是已经提供了docker 镜像，基本pull下来就可以很方便的使用了，执行命令

```
cid=$(sudo docker ps -a | grep searx | awk '{print $1}')
echo searx  cid is $cid
if [ "$cid" != "" ];then
    sudo docker stop $cid
    sudo docker rm $cid
fi
sudo docker run -d --name searx -e IMAGE_PROXY=True -e BASE_URL=http://yourdomain.com  -p 7777:8888 wonderfall/searx

```

然后就可以使用了,正常查看docker的状态，就可以正常的使用了

### # 思考

怎么样，是不是很方便，我们先看看源码是怎么样实现的

我们打开里面的代码，其实本质就是将request之后的结果做一个大的聚合，至于数据来源，我们可以是来于DB,或者文件，我们可以看一下他的核心代码

```
from urllib import urlencode
from json import loads
from collections import Iterable

search_url = None
url_query = None
content_query = None
title_query = None
suggestion_query = ''
results_query = ''

# parameters for engines with paging support
#
# number of results on each page
# (only needed if the site requires not a page number, but an offset)
page_size = 1
# number of the first page (usually 0 or 1)
first_page_num = 1

def iterate(iterable):
    if type(iterable) == dict:
        it = iterable.iteritems()

    else:
        it = enumerate(iterable)
    for index, value in it:
        yield str(index), value

def is_iterable(obj):
    if type(obj) == str:
        return False
    if type(obj) == unicode:
        return False
    return isinstance(obj, Iterable)

def parse(query):
    q = []
    for part in query.split('/'):
        if part == '':
            continue
        else:
            q.append(part)
    return q

def do_query(data, q):
    ret = []
    if not q:
        return ret

    qkey = q[0]

    for key, value in iterate(data):

        if len(q) == 1:
            if key == qkey:
                ret.append(value)
            elif is_iterable(value):
                ret.extend(do_query(value, q))
        else:
            if not is_iterable(value):
                continue
            if key == qkey:
                ret.extend(do_query(value, q[1:]))
            else:
                ret.extend(do_query(value, q))
    return ret

def query(data, query_string):
    q = parse(query_string)

    return do_query(data, q)

def request(query, params):
    query = urlencode({'q': query})[2:]

    fp = {'query': query}
    if paging and search_url.find('{pageno}') &gt;= 0:
        fp['pageno'] = (params['pageno'] - 1) * page_size + first_page_num

    params['url'] = search_url.format(**fp)
    params['query'] = query

    return params

def response(resp):
    results = []
    json = loads(resp.text)
    if results_query:
        for result in query(json, results_query)[0]:
            url = query(result, url_query)[0]
            title = query(result, title_query)[0]
            content = query(result, content_query)[0]
            results.append({'url': url, 'title': title, 'content': content})
    else:
        for url, title, content in zip(
            query(json, url_query),
            query(json, title_query),
            query(json, content_query)
        ):
            results.append({'url': url, 'title': title, 'content': content})

    if not suggestion_query:
        return results
    for suggestion in query(json, suggestion_query):
        results.append({'suggestion': suggestion})
    return results

```

### # 结果

每个response的时候我们都要以轻松的定制返回的数据（可以是网络，可以是数据库，可以是文件），那我们进一步想一下，如果我们可以hack response 结果，那我们完全可以将自己爬来的数据做为返回结果。如果是1024之类的，完全可以打造自己的“爱好”小引擎，代码我就不贴了，大家可以自己动手自己玩玩。结合jieba分词，可以更好玩一点。

## **最重要的事**

好了，今天的分享就到这里，绿水青山总是情，给个点赞行不行 ???? ???? ???? 感谢各位大佬了。
