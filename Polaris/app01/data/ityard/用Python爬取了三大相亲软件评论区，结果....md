
--- 
title:  用Python爬取了三大相亲软件评论区，结果... 
tags: []
categories: [] 

---
>  
  **小三**：怎么了小二？一副愁眉苦脸的样子。 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzc0RYcWdVWTEyakdVMTRheTRjUFNjdkxpYVNEeTBxNk9aenR6czRiWElVN1U3RTgzMWFRZENiZy82NDA?x-oss-process=image/format,png">

>  
  **小二**：唉！这不是快过年了吗，家里又催相亲了 ... 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzSGJhYm9BZVU5NmVuV2ljaWNqRDc1Q0tZUTJFcENGUnVmNHU5bXRrYlo5Rk5XNDhDSHhiekdKS3cvNjQw?x-oss-process=image/format,png">

>  
  **小三**：现在不是流行网恋吗，你可以试试相亲软件呀。 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzaHQ3aDlpYUx1bGpHRFdwNGlhWUVmYmEzdVJQYzhCTmE2cmdlN2RRVlppYUsxY24wR0JlYURIdDdBLzY0MA?x-oss-process=image/format,png">

>  
  **小二**：这玩意靠谱吗？ 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzM1dCenI4MFMwUGNRNjNpYjZ0ckxzaWFnMWs4M3dZZlF2N2lhd3FqU0tmSUtucGR5VWliRkpyUXVmUS82NDA?x-oss-process=image/format,png">

>  
  **小三**：我也没用过，你自己看看软件评论区吧。 
  **小二**：这 ... 不过也只能先到评论区看看了。 
 

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzZzQyckQzWlZ0d2ljTmhzUENwb29RTjRtaWExUm9JSk9KaHl3R0s0cHV1ZnZSeHpYSm9mWTBEQXcvNjQw?x-oss-process=image/format,png">

本文以 360 手机助手为例，地址为：`http://zhushou.360.cn/`，相亲软件选择 3 个比较流行的，分别为：世纪佳缘、百合婚恋、有缘网，我们使用 Python 爬取软件评论区，看看用户评价情况。

先来看一下这三款软件的下载量和好中差评占比情况（下图单位为万次）。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzWmRtTzlUQTNhb3lya1ZwZFlOb1o0T2hIc1BGSDFZNHJzZnNSNW83NFRvTEoxV2ljMGljQVBpY2d3LzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzSURCQ3BlZmRaeXRuT3Z1cmFYWkVhYjJzRlRWZ2pOTURMSDlUV2JXN2ljM3hIV2liN0hWNzIzUVEvNjQw?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzWEFpYWJsV0RBVWZCNzlzZVVtdmc3aWMxblNYU0ZpYWpZbERSdk9OaWEySGlieDJ1T281bWlicEhJWlFRLzY0MA?x-oss-process=image/format,png">

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzczlpYjV6Q0U0aGhVcVZSdm5QMTFxQXVGbDRwMGJDdGVJdW5JQlR0eVdPU21EVzJpYlFOM1MwQlEvNjQw?x-oss-process=image/format,png">

下面开始爬取评论区，以世纪佳缘为例，首先，在搜索框输入世纪佳缘进行搜索，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzWEJvNzlRZ2xndHBoTDVUaWNKZUVBa21FMFZwQVpoRzBJNU4yS2NibWhzRlNCV25JU0tLSFFZZy82NDA?x-oss-process=image/format,png">

接着，点击搜索到的软件进入其详情页，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzYkJndXJGM1JjaDhwalNYYWNuaWF3SWVGSTd5TWNtNk82Q0lXYWZsZmVWeExib1FCUE5mbmZXQS82NDA?x-oss-process=image/format,png">

将页面向下拉就可以看到评论区了，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzOVJJZ3d6aWF2cmw2bW9OR01iaDczN1FvRjFxaFFISUFIYjRxQWFFMFJwenM1WUlVUmliYURkOWcvNjQw?x-oss-process=image/format,png">

此时打开开发者工具并选择`Network`项，点击`查看更多评论`，然后可以看到`getComments`请求，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzTDR5b3c1VVBRcVN5aGJTc2oyVTBXWk9ValJZdHoxWHlRaDA1b1ZaMmVIeWg1WmZsOUxIeEhnLzY0MA?x-oss-process=image/format,png">

通过这个请求我们就可以动态获取评论区数据了，其中参数`star`为开始的评论索引，参数`count`为每次加载的评论个数，可以通过参数`callback`、`baike`指定不同应用，爬取代码实现如下：

```
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "keep-alive",
    "Host": "comment.mobilem.360.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}
def comment_spider(param, file_name):
    base_url = "http://comment.mobilem.360.cn/comment/getComments?c=message&amp;a=getmessage&amp;&amp;count=50"
    start = 0
    for i in range(1, 50):
        print("第{}页".format(i))
        url = base_url + param + "&amp;start=" + str(start)
        r = requests.get(url, headers=headers)
        data = re.findall("{\"errno\"(.*)\);}catch\(e\){}", r.text)
        # 转为 Json 格式
        jdata = json.loads("{\"errno\"" + data[0])
        for message in jdata["data"]["messages"]:
            content = message["content"]
            print(content)
            with open(file_name + ".txt", "a", encoding="utf-8") as f:
                f.write(content)
        start = start + 50
        time.sleep(2)

```

我们将爬取的评论数据存到了 txt 文件中。

接着，我们将评论数据进行词云展示，代码实现如下：

```
with open("yy.txt", "r", encoding="utf-8") as f:
    content = f.read()
    stylecloud.gen_stylecloud(text=content, max_words=600,
                              collocations=False,
                              font_path="SIMLI.TTF",
                              icon_name="fas fa-heart",
                              size=800,
                              output_name="yy.png")
    Image(filename="yy.png")

```

最后，通过词云看一下用户对上述软件的评价情况。

世纪佳缘：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEza0JzVFR1YVFjZGliTnFIQzJKazF1eTBpYUwwT3JkZ09lVG9pYWxDOGpNTEd1V3ViREYwVmt4bDdRLzY0MA?x-oss-process=image/format,png">

百合婚恋：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzaWEzNzg1TjdYdmtROXNXdElONFhRZTFQRHQwU250NDFUQklkbHpRY3NnZzk4T2tVS2swaGFldy82NDA?x-oss-process=image/format,png">

有缘网：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJb1dUNnRORWljVmNJNzd3a0IzakV4aWEzT2U5bk9ZMHg2aWJqaHNSaWNVTmlhY093M0U2VmljdDJpYXN5MnBpY1NpYzBrY3NVMFJSNTZRbWNSbDlCZy82NDA?x-oss-process=image/format,png">

>  
  **小二**：看了有缘网的评论，我感觉自己和相亲软件无缘 ... 
  **小三**：... 
 

源码在公号后台回复 **201207** 获取。

PS：如果觉得分享内容有一些帮助，欢迎大家随手分享、点赞、在看。

**声明：本文不构成对上述相亲软件的任何使用建议。**

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">
