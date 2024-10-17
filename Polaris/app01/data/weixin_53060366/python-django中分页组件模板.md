
--- 
title:  python-django中分页组件模板 
tags: []
categories: [] 

---
## python-django中分页组件模板

### 自定义分页组件

自己写一个分页组件，以后需要用的地方直接拿过来用即可。方便快速。比Django自带的分页组件要好用一些。 以后都可以套用这个模板，只需要按自己的需求更改就行。

#### 1、视图函数中

```
views.py

from app01.utils.pagination import Pageination

def user_list(request):
    # 根据需要获取数据库的数据
    queryset = employee.objects.all()
    # 分页
    page = Pageination(request,queryset,page_size=5)
    context = {<!-- -->
        "queryset": page.queryset,  # 分完页的数据（当前页）
        "page_string": page.html(), # 页码显示
    }
    return render(request, 'user_list.html', context)

```

#### 2、HTML中

```
&lt;!-- 显示页码 --&gt;
&lt;ul class="pagination"&gt;
    {<!-- -->{ page_string }}
&lt;/ul&gt;

```

#### 3、封装的分页组件函数

```
import copy
from django.utils.safestring import mark_safe


class Pageination(object):

    def __init__(self, request, queryset, page_param="page", page_size=10, plus=5):
        """"
        :param request: 请求的对象
        :param queryset: 符合的数据（根据这个数据分页）
        :param page_param: 在URl中获取分页的参数（/phone/list/?page=12）
        :param page_size: 每页显示多少数据
        :param plus: 显示当前页 前或后几页
        """
        # 拼接查询条件 ?q=888&amp;xx=123&amp;page=12 QueryDict:{'q':['888'],'xx':['123']} 有中括号[]
        quey_dict = copy.deepcopy(request.GET)
        quey_dict._mutable = True
        self.quey_dict = quey_dict
        # 当前页page
        self.page_param = page_param
        page = request.GET.get(self.page_param, "1")
        if page.isdecimal():
            self.page = int(page)
        else:
            self.page = 1

        self.page_size = page_size
        self.start = (self.page - 1) * self.page_size
        self.end = self.page * self.page_size
        # 获取当前页的这几个数据
        self.queryset = queryset[self.start:self.end]

        # 总页码数
        count = queryset.count()
        self.page_count, div = divmod(count, page_size)
        if div:
            self.page_count += 1

        # 计算出当前页的前后五页
        self.plus = plus
        if self.page_count &lt;= 2 * self.plus + 1:
            self.start_page = 1
            self.end_page = self.page_count + 1
        else:
            # 数据比较多的情况
            if self.page &lt;= 5:
                self.start_page = 1
                self.end_page = 2 * self.plus + 1
            elif self.page + self.plus &gt;= self.page_count:
                self.start_page = self.page_count - 2 * self.plus
                self.end_page = self.page_count
            else:
                self.start_page = self.page - self.plus
                self.end_page = self.page + self.plus + 1

    def html(self):

        # 页码显示
        page_str_list = []
        # 首页
        self.quey_dict.setlist(self.page_param, [1])
        page_str_list.append('&lt;li &gt;&lt;a href="?{}"&gt; 首页 &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode()))

        # 上一页
        if self.page &gt; 1:
            self.quey_dict.setlist(self.page_param, [self.page - 1])
            ele = '&lt;li &gt;&lt;a href="?{}"&gt; &lt;&lt; &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode())
        else:
            self.quey_dict.setlist(self.page_param, [1])
            ele = '&lt;li &gt;&lt;a href="?{}"&gt; &lt;&lt; &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode())
        page_str_list.append(ele)
        # 页码条
        for i in range(self.start_page, self.end_page):
            if i == self.page:
                self.quey_dict.setlist(self.page_param, [i])
                ele = '&lt;li class="active"&gt;&lt;a href="?{}"&gt;{}&lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode(), i)
            else:
                self.quey_dict.setlist(self.page_param, [i])
                ele = '&lt;li&gt;&lt;a href="?{}"&gt;{}&lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode(), i)
            page_str_list.append(ele)
        # 下一页
        if self.page == self.page_count:
            self.quey_dict.setlist(self.page_param, [self.page])
            ele = '&lt;li &gt;&lt;a href="?{}"&gt; &gt;&gt; &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode())
        else:
            self.quey_dict.setlist(self.page_param, [self.page + 1])
            ele = '&lt;li &gt;&lt;a href="?{}"&gt; &gt;&gt; &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode())
        page_str_list.append(ele)
        # 尾页
        self.quey_dict.setlist(self.page_param, [self.page_count])
        page_str_list.append('&lt;li &gt;&lt;a href="?{}"&gt; 尾页 &lt;/a&gt;&lt;/li&gt;'.format(self.quey_dict.urlencode()))

        # 页码合在一起
        ele = """
        &lt;li&gt;
            &lt;form style="float: left;margin-left: -1px" method="get"&gt;
                &lt;input style="position: relative;float: left;display: inline-block;width: 80px;" 
                type="text" name="page" class="form-control" placeholder="页码"&gt;
                &lt;button class="btn btn-primary" type="submit"&gt;
                    &lt;span class="glyphicon glyphicon-search" aria-hidden="true"&gt;&lt;/span&gt;
                &lt;/button&gt;
            &lt;/form&gt;
        &lt;/li&gt;
        """

        page_str_list.append(ele)
        page_string = mark_safe("".join(page_str_list))

        return page_string

```
