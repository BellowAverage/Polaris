
--- 
title:  用Python爬取英雄联盟（lol）全部皮肤 
tags: []
categories: [] 

---
小三：“怎么了小二？一副无精打采的样子！”

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzltbDhjWW1sZFNQTDJGdmliN1Z3eDBnaWFPbVYxRnV0bGljQVo0eldkYk9pY3FJTXNpYnh5aWFpY2VyWGhnLzY0MA?x-oss-process=image/format,png">

小二：“唉！别提了，还不是最近又接触了一个叫英雄联盟的游戏，游戏中很多皮肤都需要花钱买，但是我钱不够呀...”

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2pwZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlpYVRiSDdpYlJPU1BUbEFkcWZQREEwWmNaUTdTM0tQaWF5OExpYmZDRW1lN3gzQ1Z0dlp6aWFWRmxZdy82NDA?x-oss-process=image/format,png">

小三：“咋得，钱攒够了你还要买呀？还吃不吃饭了？！要我说，你干脆将英雄的炫彩皮肤都爬下来欣赏一下得了，饭钱还给你省下了。”

小二：“你说的也对，毕竟吃饭更重要，那我还是爬取皮肤欣赏一下算了。”

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlnWDlCalcxMHNMOHRRSkRhT0FpYk5md1pyRUU5NnhlYW5NZU44MVR0YU9FVG1wRlNSUURxR3VnLzY0MA?x-oss-process=image/format,png">

首先，我们打开英雄联盟官网主页，网址为：`https://lol.qq.com/main.shtml`，然后向下拉，可以看到英雄列表，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlybzFXOFZVNlRWNEZVRjRObldXTG9OVzdxbE1VTDlqNEZEV0xOVlYwdHFvc2g3dkhnTXhZaWF3LzY0MA?x-oss-process=image/format,png">

接着随意选一个英雄点击进入看一下，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlubzBFcEZRcjc2ZzVhRE9aaWNzaWFnUDJaZUdkSktnVHpBcnNvNTg1cW43ZVFrYU5FdnVxaWNuclEvNjQw?x-oss-process=image/format,png">

再点击鼠标右键，接着选择`检查`，看一下皮肤的 URL，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlRUFJBT0xPelBwQmdFWUE1RXBpYTBlVzVXcHJEdVBFeDJUNWlhTmhEN0RBMjVTNGduOG1Mazg3Zy82NDA?x-oss-process=image/format,png">

通过观察，可以发现英雄皮肤 URL 组成方式为：`https://game.gtimg.cn/images/lol/act/img/skin/big + 英雄id + 皮肤id.jpg`。

我们先看`皮肤id`，也就是看皮肤的个数，选择开发者工具的`Network`项，之后刷新一下页面，可以发现有一个`17.js`的请求，`17`实际就是`英雄id`，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlUcDVjb055b2VmR29vQkpuZWc4MDVCb2liUzFHNlZmWnJiZXNSV2JjdjF3bnh2NFd5RXdlOWZ3LzY0MA?x-oss-process=image/format,png">

再选择`Response`项看一下相应数据，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlzQmlhRHJaMHdLZjc3SVoxRjMyb2NZaWJMN0hKaktKdmRjTkRDVHN2aWFHeVpQMUZObzdFRXhQRXcvNjQw?x-oss-process=image/format,png">

我们可以看到数据都显示在了一行，看着不太方便，我们将其格式化看一下，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlIcmV3b2pvUjdMZW9HcjNZVDN0aWJpYWZLTDNORDVXd2xJSjRlTGQwQ3VDTlU2OFZJcm10dEFHQS82NDA?x-oss-process=image/format,png">

通过观察，可以发现获取指定英雄`皮肤id`的 URL 就是：`https://game.gtimg.cn/images/lol/act/img/js/hero/ + 英雄id.js`，获取`皮肤id`及下载皮肤图片的代码实现如下：

```
hero_skin_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/' + hero_id + '.js'
# 通过 url 获取英雄的皮肤数量
skin_text = requests.get(hero_skin_url).text
skin_json = json.loads(skin_text)
skin_list = skin_json['skins']
# 获取皮肤名
hero_skins.clear()
for skin in skin_list:
    hero_skins.append(skin['name'].replace('/', '').replace('\\', '').replace(' ', ''))
# 皮肤数量
skins_num = len(hero_skins)
s = ''
for i in tqdm(range(skins_num), desc='【' + hero_name + '】皮肤下载'):
    if len(str(i)) == 1:
        s = '00' + str(i)
    elif len(str(i)) == 2:
        s = '0' + str(i)
    elif len(str(i)) == 3:
        pass
    try:
        # 拼接指定皮肤的 url
        skin_url = 'https://game.gtimg.cn/images/lol/act/img/skin/big' + hero_id + '' + s + '.jpg'
        img = requests.get(skin_url)
    except:
        # 没有炫彩皮肤 url 则跳过
        continue
    # 保存皮肤图片
    if img.status_code == 200:
        with open(hero_skins[i] + '.jpg', 'wb') as f:
            f.write(img.content)

```

现在就差`英雄id`参数的获取了，我们接着看如何获取全部的`英雄id`，返回到 `https://lol.qq.com/main.shtml`页面，打开开发者工具并选择`Network`，然后刷新页面，我们可以观察到有一个`hero_list.js`的请求，如图所示：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzlTR3NKWk5XNTM4WEo3Y0o1RUk4Wk5IMXREREFOVHdmc3E0UW1hTTZlTTZwSldLaGdqMTVpYjFnLzY0MA?x-oss-process=image/format,png">

与`皮肤id`的获取基本类似，通过这个请求就可以获取到全部`英雄id`，代码实现如下：

```
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
hero_text = requests.get(url).text
# 转为 json 格式
hero_json = json.loads(hero_text)['hero']
path = os.getcwd()
# 获取当前文件夹路径
workspace = os.getcwd()
# 皮肤路径
skin_path = "{}\\{}".format(workspace, 'skins')
# 遍历列表
for hero in hero_json:
    # 将每一个英雄的 id、name 放入一个字典中
    hero_dict = {'id': hero['heroId'], 'name': hero['name']}
    # 放入列表
    heros.append(hero_dict)

```

我们可以看出：代码中除了`英雄id`，还获取了`英雄name`，并将每一个英雄的`id`、`name`放在了一个字典中，又将所有英雄对应的字典放在了列表中。

最后，我们看一下下载效果：

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X2dpZi9QdlA2cWpVcHZJcktadVpUeWliN1BDVVNmbXNDWGdvMzl1cGdpYUZWRGxqcE5qZEVvOHNrcUY5ZUVCUGs5aWFPQUNQYnNXOVJlTTBFZ2pGTzJpY2ZZQ2FxZXcvNjQw?x-oss-process=image/format,png">

源码在公众号 **Python小二** 后台回复 **201130** 获取，有问题可以添加我个人微信号：**ityard**。

&lt; END &gt;

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9tbWJpei5xcGljLmNuL21tYml6X3BuZy9QdlA2cWpVcHZJcGFPWnF1SzE4eGM0V2JIT05pYmVoZU9HTXNJMUdIR0Z1UmpycUxpY2lhNld1aWNxaWNNWTZuY2t2Y21pYUZaWUcxWnM4Zjd5bnBwRTJaR2JFQS82NDA?x-oss-process=image/format,png">

如果觉得有帮助，就给个分享、在看、赞吧~
