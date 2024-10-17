
--- 
title:  selenium之 定位以及切换frame（iframe） 
tags: []
categories: [] 

---
很多人在用selenium定位页面元素的时候会遇到定位不到的问题，明明元素就在那儿，用firebug也可以看到，就是定位不到，这种情况很有可能是frame在搞鬼（原因之一，改天专门说说定位不到元素，可能的一些原因及处理办法）。

frame标签有frameset、frame、iframe三种，frameset跟其他普通标签没有区别，不会影响到正常的定位，而frame与iframe对selenium定位而言是一样的，selenium有一组方法对frame进行操作。

### 1.怎么切到frame中(switch_to.frame())

selenium提供了switch_to.frame()方法来切换frame

```
switch_to.frame(reference)

```

不得不提到switch_to_frame()，很多人在这样写的时候会发现，这句话被划上了删除线，原因是这个方法已经out了，之后很有可能会不支持，建议的写法是switch_to.frame()

reference是传入的参数，用来定位frame，可以传入id、name、index以及selenium的WebElement对象，假设有如下HTML代码 index.html：

```
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;title&gt;FrameTest&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;iframe src="a.html" id="frame1" name="myframe"&gt;&lt;/iframe&gt;
&lt;/body&gt;
&lt;/html&gt;

```

想要定位其中的iframe并切进去，可以通过如下代码：

```
from selenium import webdriver
driver = webdriver.Firefox()
driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
# driver.switch_to.frame("frame1")  # 2.用id来定位
# driver.switch_to.frame("myframe")  # 3.用name来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位

```

通常采用id和name就能够解决绝大多数问题。但有时候frame并无这两项属性，则可以用index和WebElement来定位：
- index从0开始，传入整型参数即判定为用index定位，传入str参数则判定为用id/name定位- WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
### 实例

```
&lt;iframe src="myframetest.html" /&gt;

```

用xpath定位，传入WebElement对象：

```
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'myframe')]"))

```

### 2.从frame中切回主文档(switch_to.default_content())

切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。

```
driver.switch_to.default_content()

```

### 3.嵌套frame的操作(switch_to.parent_frame())

有时候我们会遇到嵌套的frame，如下：

```
&lt;html&gt;
    &lt;iframe id="frame1"&gt;
        &lt;iframe id="frame2" / &gt;
    &lt;/iframe&gt;
&lt;/html&gt;

```

**1.从主文档切到frame2，一层层切进去**

```
driver.switch_to.frame("frame1")
driver.switch_to.frame("frame2")

```

**2.从frame2再切回frame1，这里selenium给我们提供了一个方法能够从子frame切回到父frame，而不用我们切回主文档再切进来。**

```
driver.switch_to.parent_frame()  # 如果当前已是主文档，则无效果

```

有了parent_frame()这个相当于后退的方法，我们可以随意切换不同的frame，随意的跳来跳去了。

所以只要善用以下三个方法，遇到frame分分钟搞定：

```
driver.switch_to.frame(reference)
driver.switch_to.parent_frame()
driver.switch_to.default_content()

```

补充 另外补充一下，之前曾看到过用点分法来切入嵌套frame的方法，但我试验之后发现并不能定位到frame，如果有同学可以成功，麻烦留言告知一下，用法如下：

```
driver.switch_to.frame('frame1.0.frame3')

```

据说以上代码可以切到 “frame1” 下的 “第一个frame” 下的 “frame3” 中。
