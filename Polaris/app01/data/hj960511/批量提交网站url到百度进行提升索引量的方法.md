
--- 
title:  批量提交网站url到百度进行提升索引量的方法 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解通过百度的推送接口，向百度批量提交网站url并让百度加快收录网站页面的方法 作者：任聪聪 日期：2023年4月7日 


### 前置条件

1.需要去百度站长平台，绑定自己的域名。前往用户中心，添加网站。 <img src="https://img-blog.csdnimg.cn/e2fac6aad5dd416abd64101b31eca065.png" alt="在这里插入图片描述"> 注：添加网站的步骤异常简单，百度有详细的步骤引导。

2.获取到token，如下界面复制。 <img src="https://img-blog.csdnimg.cn/9bcc08b62a5f40ebbfa68237dbc4fd22.png" alt="在这里插入图片描述"> token位置： <img src="https://img-blog.csdnimg.cn/65135bd896b04154a8bb04e2262f94d3.png" alt="在这里插入图片描述">

### 推送方式一、批量推送

注：有限制一般是100000条/日。

php的代码推送片段：

```
$urls = [];
foreach(range(7000,7100) as $k=&gt;$v){<!-- -->
    $urls[]="https://这里是自定义的规则类型页面输出可以改成自己的/".$v;
}
// print_r($urls);
$api = 'http://data.zz.baidu.com/urls?site=不带http的域名&amp;token=你的token';
$ch = curl_init();
$options =  array(
    CURLOPT_URL =&gt; $api,
    CURLOPT_POST =&gt; true,
    CURLOPT_RETURNTRANSFER =&gt; true,
    CURLOPT_POSTFIELDS =&gt; implode("\n", $urls),
    CURLOPT_HTTPHEADER =&gt; array('Content-Type: text/plain'),
);
curl_setopt_array($ch, $options);
$result = curl_exec($ch);
echo $result;

```

python的代码推送片段：

```
import requests

urls = []
for v in range(7000, 7101):
    urls.append('https://dq.youqiong.net/ask_details/' + str(v))

api = 'http://data.zz.baidu.com/urls?site=你的域名不带http&amp;token=你的token'
headers = {<!-- -->'Content-Type': 'text/plain'}
response = requests.post(api, data='\n'.join(urls), headers=headers)
print(response.text)

```

返回的响应信息说明： 1.提交容量为0时，提交条数超出，显示400 <img src="https://img-blog.csdnimg.cn/09dcf8c2d2624bbb93de54b2b9055f80.png" alt="在这里插入图片描述"> 2.成功提交时，显示成功数目和剩余数目。 <img src="https://img-blog.csdnimg.cn/87bf3ea8bd934a2f8b12160444b9d9b3.png" alt="在这里插入图片描述">

### 推送方式二、制作地图文件上传到网站运行目录

注：如网站的运行目录为public那么就放在这个下面

使用python或php自动生成一个文件或页面为，site.xml、site.txt。

如下是使用python的方式：

```
#生成地图文件
content = []
for i in range(1,100001):
    content.append("https://你的域名/详细页面/"+str(i)) 

with open('site.txt', 'w') as f:
    for line in content:
        print(line)
        f.write(line + '\n')

```

生成的文件： <img src="https://img-blog.csdnimg.cn/950fb1ef8604477faca4e3bbfeca6e94.png" alt="在这里插入图片描述">

回到站长平台，进入普通收录选择sitemap，并填写这个文件在网站上的路径。

<img src="https://img-blog.csdnimg.cn/4b00105eb57e4f3fae45f6cff1031530.png" alt="在这里插入图片描述"> end：以上便是百度批量提交的方法详解。

### 相关文章推荐：

 
