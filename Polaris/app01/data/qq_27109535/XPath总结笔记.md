
--- 
title:  XPath总结笔记 
tags: []
categories: [] 

---
接下来我们来讲提取细节，首先加载库

```
from lxml import etree

```

<img src="https://img-blog.csdnimg.cn/5c48258ab1f3404b873d85fac1871387.png" alt=""> 提取标签内容， /text()[0]或者/string()[0] 提取标签属性值， /@属性名 *表示任意节点 ,@*表示任何属性, node()表示任意节点

<img src="https://img-blog.csdnimg.cn/3ded4c60259a4fc6a93ee59931002170.png" alt="在这里插入图片描述">

### 1. 解析html流程说明

```
url_02 = 'https://www.qdfd.com.cn/qdweb/realweb/fh/FhProjectInfo.jsp'
data_02 = {
   <!-- -->'projectID': shuzi_01}
response_02 = requests.post(url_02, data=data_02,headers=header)
if response.status_code == 200:
	response_02.encoding = 'GBK'
	sleep(random.uniform(0.2, 0.3))  # 生成一个a到b的小数等待时间
	# 请求是否成功
	# print(response_02.status_code)
	
	html_02 = etree.HTML(response_02.text)
	
	
	# #/html/body/div[1]/div[2]/ul[2]/table[2]/tbody/tr[position()&gt;1]/td[2]/a
	shuzi_2 = html_02.xpath('/html/body/div[1]/div[2]/ul[2]//tr[position()&gt;1]/td[2]/a')

```

```
a = '''&lt;title&gt;标题&lt;/title&gt;
&lt;body&gt;
    &lt;ul class='list1'&gt;
        &lt;li&gt;列表1第1项&lt;/li&gt;
        &lt;li&gt;列表1第2项&lt;/li&gt;
    &lt;/ul&gt;
    &lt;p class='first'&gt;文字1&lt;/p&gt;
    &lt;p class='second'&gt;文字2&lt;/p&gt;
    &lt;ul class='list2'&gt;
        &lt;li&gt;列表2第1项&lt;/li&gt;
        &lt;li&gt;列表2第2项&lt;/li&gt;
    &lt;/ul&gt;
&lt;/body&gt;'''

from lxml import etree
html = etree.HTML(a)
html.xpath('//title/text()')[0] # '标题'
html.xpath("//p[@class='first']//text()")[0] # '文字1'
html.xpath(&lt;/
```
