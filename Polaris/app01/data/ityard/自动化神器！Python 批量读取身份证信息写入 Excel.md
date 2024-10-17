
--- 
title:  自动化神器！Python 批量读取身份证信息写入 Excel 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/20210704131629752.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

今天分享一个实用技能，利用 Python 批量读取身份证信息写入 Excel。

### 读取

以图片形式的身份证为例，信息读取我们使用`百度文字识别OCR`来实现，百度接口提供了免费额度，日常使用基本差不多够了，下面来具体看一下如何使用百度文字识别。

##### SDK 安装

百度云 SDK 提供了 Python、Java 等多种语言的支持，Python 版的 SDK 安装很简单，使用`pip install baidu-aip`即可，支持 Python 2.7+ &amp; 3.x 版本。

##### 创建应用

创建应用需要一个百度或百度云账号，注册登录地址为：`https://login.bce.baidu.com/?redirect=http%3A%2F%2Fcloud.baidu.com%2Fcampaign%2Fcampus-2018%2Findex.html`，登录后将鼠标移到登录头像位置，在弹出菜单中点击`用户中心`，如图所示：

<img src="https://img-blog.csdnimg.cn/2021070413140458.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

首次进入需选一下相应信息，如图所示：

<img src="https://img-blog.csdnimg.cn/20210704131420596.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

选完之后点保存即可。

接着将鼠标移到左侧`&gt;`符号位置，再选`人工智能`，点击`文字识别`，如图所示：

<img src="https://img-blog.csdnimg.cn/20210704131435513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

点击之后会进到如下所示图中：

<img src="https://img-blog.csdnimg.cn/2021070413144850.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

现在，我们就可以点击`创建应用`了，之后进到如下所示图中：

<img src="https://img-blog.csdnimg.cn/20210704131459404.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

从上图中我们可以看出`百度文字识别OCR`能够识别的信息类别非常多，也就是说不只是身份证，如果你有其他信息识别的需求也是可以通过它来快速实现的。

这里我们填一下`应用名称`和`应用描述`，填完之后点立即创建即可。

创建完成后返回应用列表，如下图所示：

<img src="https://img-blog.csdnimg.cn/20210704131512752.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

我们需要用到`AppID`&amp;`API Key`&amp;`Secret Key`这三个值，记录一下。

##### 代码实现

代码实现很简单，几行 Python 代码即可搞定，如下所示：

```
from aip import AipOcr

APP_ID = '自己的APP_ID'
API_KEY = '自己的API_KEY'
SECRET_KEY = '自己的SECRET_KEY'
# 创建客户端对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
# 打开并读取文件内容
fp = open("idcard.jpg", "rb").read()
# res = client.basicGeneral(fp)  # 普通
res = client.basicAccurate(fp)  # 高精度

```

从上述代码中可以看出识别功能分为`普通`和`高精度`两种模式，为了识别率更高，我们这里采用`高精度`模式。

以如下三张我在网上找的假身份证为例：

<img src="https://img-blog.csdnimg.cn/20210704131527883.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l0eWFyZA==,size_16,color_FFFFFF,t_70#pic_center" alt="">

因为有多张身份证图片，我们需要写一个方法来进行遍历，代码实现如下：

```
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield base + f

```

通过识别功能获取到的身份证原始信息格式如下：

```
{<!-- -->'words_result': [{<!-- -->'words': '姓名韦小宝'}, {<!-- -->'words': '性别男民族汉'}, {<!-- -->'words': '出生1654年12月20日'}, {<!-- -->'words': '住址北京市东城区景山前街4号'}, {<!-- -->'words': '紫禁城敬事房'}, {<!-- -->'words': '公民身份证号码11204416541220243X'}], 'log_id': 1411522933129289151, 'words_result_num': 6}

```

### 写入

证件信息的写入使用 Pandas 来实现。这里我们还需要先将获取的原始证件信息进行预处理以便写入 Excel 中，我们将证件的姓名…住址分别存放在数组中，处理代码实现如下：

```
for tex in res["words_result"]:
    row = tex["words"]
    if "姓名" in row:
        names.append(row[2:])
    elif "性别" in row:
        genders.append(row[2:3])
        nations.append(row[5:])
    elif "出生" in row:
        births.append(row[2:])
    elif "住址" in row:
        addr += row[2:]
    elif "公民身份证号码" in row:
        ids.append(row[7:])
    else:
        addr += row

```

之后就可以很方便的将信息直接写入到 Excel 中了，写入代码实现如下：

```
df = pd.DataFrame({<!-- -->"姓名": names, "性别": genders, "民族": nations,
                       "出生": births, "住址": address, "身份证号码": ids})
df.to_excel('idcards.xlsx', index=False)

```

看一下写入效果：

<img src="https://img-blog.csdnimg.cn/2021070413154595.PNG#pic_center" alt="">

到此，我们就实现了身份证信息的批量读写功能。

源码在公众号**Python小二**后台回复**身份证**获取。
