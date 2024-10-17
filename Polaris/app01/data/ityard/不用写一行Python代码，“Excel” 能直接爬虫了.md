
--- 
title:  不用写一行Python代码，“Excel” 能直接爬虫了 
tags: []
categories: [] 

---
来源：量子位

家人们，要爬虫——现在用**一个电子表格**就行了。

<img src="https://img-blog.csdnimg.cn/img_convert/678562892d4a2bf93f35c4fdee6c5294.png" alt="678562892d4a2bf93f35c4fdee6c5294.png">

一行代码也别写，第三方软件也甭安。

只需在表格里**点几下**就ok。

不信，你瞧：

就这么两下，网页上的商品信息都有了。

<img src="https://img-blog.csdnimg.cn/img_convert/803f8aea03124622fffbc6aa851de1ce.gif" alt="803f8aea03124622fffbc6aa851de1ce.gif">

网友看完都惊呆了，码个不停。

<img src="https://img-blog.csdnimg.cn/img_convert/2ee3e27824d141d0d4886fbfa1579c13.png" alt="2ee3e27824d141d0d4886fbfa1579c13.png">

**一看到这是来自谷歌的产品**（Google Sheet，谷歌的“Excel”），大家就立马cue起了**微软**，问它慌不慌。

还有人称这是在“跨界打击”它。<img src="https://img-blog.csdnimg.cn/img_convert/5efa3e5ab0c238180093ec82d185dbd5.png" alt="5efa3e5ab0c238180093ec82d185dbd5.png">

<img src="https://img-blog.csdnimg.cn/img_convert/476be6e555c155d742679c2a0ba46097.png" alt="476be6e555c155d742679c2a0ba46097.png">

###### **△** 扫盲：“巨硬”就是微软，网友给的调侃

好不热闹。

来看具体怎么实现。

### 详细步骤

以爬亚马逊某个手机产品的商品页为例。

我们先打开谷歌Sheet（网友版即可），新建一个文档。

然后copy一下要爬的网址，粘进去。

<img src="https://img-blog.csdnimg.cn/img_convert/23433e4e43b5dd39e9ef1bbd142ae680.gif" alt="23433e4e43b5dd39e9ef1bbd142ae680.gif">

剩下的都在Sheet里完成。

我们先列一下要爬的元素，这里依次为：

商品图片-识别码（asin，亚马逊给每个商品生成的唯一标识）-商品名-价格-评分-图片网址。

<img src="https://img-blog.csdnimg.cn/img_convert/37297e179065e7cb6432bad853a57d74.png" alt="37297e179065e7cb6432bad853a57d74.png">

然后就可以正式开始爬了。

要诀就是一个叫做**ImportFromWe****b**的函数。

它也是个插件，没有的需要先安装一下（安装地址放文末了），然后通过Google Sheet程序的“扩展程序”菜单导入就行。

<img src="https://img-blog.csdnimg.cn/img_convert/9d5f2b58e8973955dfc66f7daf6061e7.png" alt="9d5f2b58e8973955dfc66f7daf6061e7.png">

我们只需把ImportFromWeb函数放进asin那一列，然后第一个参数选中刚刚粘过来的网址，第二个参数把要爬的元素单元格拖一遍（除了“图片”）。

**稍等个1～2s**，价格、商品名等信息就都出来了！

<img src="https://img-blog.csdnimg.cn/img_convert/ca6470a0c191b47ec6668a4d39e52412.gif" alt="ca6470a0c191b47ec6668a4d39e52412.gif">

还差图片。

简单～基操～

用IMAGE函数把G3格子里得到的图片网址值给过去就行。

<img src="https://img-blog.csdnimg.cn/img_convert/ab3a424a37128a6792fcfb87d05a4954.gif" alt="ab3a424a37128a6792fcfb87d05a4954.gif">

至此，第一个商品页里的东西就爬到了。

唯一麻烦的是，如果还需要爬更多商品的信息，需要把商品网址挨个粘一遍。

然后就没啥了，除了给单元格地址的行标列标加一下**绝对引用符“$”**。

这里可以不学视频，直接一个**f4**就行。

拖一下，全部搞定！

<img src="https://img-blog.csdnimg.cn/img_convert/d24281ba6b60441563cf9fbed9bd4716.gif" alt="d24281ba6b60441563cf9fbed9bd4716.gif">

怎么样？是不是非常方便。

<img src="https://img-blog.csdnimg.cn/img_convert/af6678d972ba5e93b9ecb605d47c1f0e.png" alt="af6678d972ba5e93b9ecb605d47c1f0e.png">

看完整个操作，你也发现了，其实就是谷歌写了个脚本给咱封装好了直接用。

而据官方介绍，这个ImportFromWeb功能还能**自动更新**爬取到的信息。

而且只要是用JS写的网站都可以爬（基本等于绝大数网站了），每个函数还可支持50个url，以及数千个数据点。

快点**码**起来吧～

参考链接：[1]https://weibo.com/1402400261/M9ZY84thO?filter=hot&amp;root_comment_id=0&amp;type=comment[2]https://www.getapp.sg/software/2060417/importfromweb[3]https://workspace.google.com/marketplace/app/importfromweb_web_scraping_in_google_she/278587576794（安装ImportFromWeb）

### 往期推荐
- - - 