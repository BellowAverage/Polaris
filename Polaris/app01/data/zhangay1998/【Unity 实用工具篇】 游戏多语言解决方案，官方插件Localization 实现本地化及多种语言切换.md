
--- 
title:  【Unity 实用工具篇】| 游戏多语言解决方案，官方插件Localization 实现本地化及多种语言切换 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/4ea0ad75b9c145e5ba7d219b7e425099.png" alt="请添加图片描述">



####  
- <ul><li><ul><li>- - <ul><li>- - - - - - - - - - 


<img src="https://img-blog.csdnimg.cn/direct/83016433a1ea46ef95810f2da012d18a.png" alt="在这里插入图片描述">

#### 前言
- Unity的**多语言本地化**是一个很实用的功能，它可以帮助游戏支持多种语言，让不同语言的玩家都能够更好地体验游戏。- 而实现本地化的方案也有很多种，各个方案之间也各有优劣，后面也会对多个方案进行介绍学习。- 本文就来介绍一个专门作用于多语言本地化的Unity官方插件：`Localization `。- 这个插件方便进行游戏的多语言本地化，让游戏支持多种语言，下面就来看看该插件的使用方法吧！
## <font color="#ff6984" size="5"> 【Unity 实用工具篇】</font>| 游戏多语言解决方案，官方插件Localization 实现本地化及多种语言切换

### 一、多语言本地化插件 Localization

#### 1.1 介绍

`Localization`是Unity官方推出的本地化插件，它可以帮助开发者在Unity项目中实现多语言支持。

在Unity中，Localization的工作原理是创建多个表格来存储不同语言的不同字符串。

可以通过Localization Tables创建这些表格，表格可以建立不同资源之间的对应关系，一个key对应多个语言的资源。

通过使用Localization插件，开发者可以方便地设置和获取当前语言和当前语言地区，从而为游戏或应用程序提供多种语言的支持。

这对于那些需要面向不同地区和不同语言的用户发布游戏或应用程序的开发者来说是非常有用的。

#### 1.2 效果展示

<img src="https://img-blog.csdnimg.cn/3d87502208fd489583a01cf98acf923a.gif" alt="请添加图片描述">

#### 1.3 使用说明

官方文档：

本文使用的Localization版本为1.4.5，Unity引擎版本为2023.1.9。

后续插件可能会有更新，或者使用老版本的插件时功能使用上可能会有所不同，实际使用时按照自己的版本要求即可。

### 二、 插件导入并配置

#### 2.1 安装 Localization

打开菜单栏 `Window -&gt; Package Manager` ，在搜索框中搜索Localization 并进行安装即可。

要注意Packages选择Unity Registry，不然可能搜不到该插件哦。 <img src="https://img-blog.csdnimg.cn/1abf322f73ca486b8ab0665b9a83700b.png" alt="在这里插入图片描述">

#### 2.2 全局配置

打开菜单栏 `Edit -&gt; Project Settings -&gt; Localization -&gt; Create`，找到Localization，点击Create创建，并选择一个文件目录进行文件保存。 <img src="https://img-blog.csdnimg.cn/51886a344555428d8180cf2a3f260cd1.png" alt="在这里插入图片描述">

点击 `Locale Generator` 搜索zh和en添加中英文配置，第一次添加时会让我们选择一个文件夹目录保存。 <img src="https://img-blog.csdnimg.cn/69f0e211467a4e1094c956dd8c3ec0f9.png" alt="在这里插入图片描述">

Locale Generator 用于添加或移出语言，每添加一种语言也会生成对应的配置文件，然后可以修改默认语言为中文，如下图所示： <img src="https://img-blog.csdnimg.cn/c85cd7e2d16e45e9abf3b76c89a69a6c.png" alt="在这里插入图片描述">

### 三、多语言映射表

#### 3.1 创建多语言文本配置表

打开菜单栏 `Window -&gt; Asset Management -&gt; Localization Tables `，点击New Table Collection创建表格。

该表格用于建立不同资源之间的对应关系，一个key对应多个语言的资源，可以选择创建文本表或者资源表。

这里我们选择文本表(String Table Collection)使用，写好表名后点击Create就可以创建了，然后选择一个路径目录进行保存。 <img src="https://img-blog.csdnimg.cn/e0a9dce0a25e440bb71562aa4056a73c.png" alt="在这里插入图片描述">

经过上面几个配置后可以在我们前面保存文件的路径下看到相关的文件，这里最好是根据自己的情况选择合适的文件夹进行管理保存。 <img src="https://img-blog.csdnimg.cn/7ec6082bfb814d709cd82447ce5d7bb3.png" alt="在这里插入图片描述">

#### 3.2 添加多语言文本配置表内容

此时在Localization Tables中添加多语言文本即可，配置内容主要是Key和对应多种语言的文本。

可通过`Window -&gt; Asset Management -&gt; Localization Tables `打开该窗口。 <img src="https://img-blog.csdnimg.cn/7e6bd49e56354d47a704ee21243567e0.png" alt="在这里插入图片描述">

实际项目中不一定将多语言内容全部写在一个配置表中，不同的文本内容也可以通过创建多个配置表进行填写，让不同的模块自己管理文本内容也是一个不错的选择。

#### 3.3 静态文本

此时在场景中添加一个文本组件Text，然后在该组件右侧菜单处点击`Localize`，会自动添加一个`Localize String Event`组件。 （这里也可以手动在下面添加`Localize String Event`组件，不过还要手动配置该组件绑定的Text组件，稍微麻烦一些，功能都是一样的） <img src="https://img-blog.csdnimg.cn/6b5f4f585c1e4f9eb08e750fdee46673.png" alt="在这里插入图片描述">

此时在该组件中的String Reference参数中选择之前配置的多语言文本配置表中的Key即可完成多语言的配置。 <img src="https://img-blog.csdnimg.cn/de70e35ef5c4495ca728513e9a07a429.png" alt="在这里插入图片描述">

此时运行程序，可以看到该Text组件的文本内容已经变成我们配置多语言文本配置表中的Key对应的文本了。

通过Game视图右上角的语言选择可以切换语种，点击切换不同语言后，Game视图中的文本也会即时的跟着切换了。 <img src="https://img-blog.csdnimg.cn/6b105ab80d7d4f58bcc71dec53a146ad.png" alt="在这里插入图片描述">

这样我们的静态文本就可以通过这种方法来添加多语言文本配置表中的Key绑定多语言了。

也可以通过脚本控制语言的切换，测试代码如下：

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;
using UnityEngine.ResourceManagement.AsyncOperations;

public class LanguageManager : MonoBehaviour
{<!-- -->
    AsyncOperationHandle m_InitializeOperation;
    private Locale _chineseLocale;
    private Locale _englishLocale;

    void Start()
    {<!-- -->
        // SelectedLocaleAsync will ensure that the locales have been initialized and a locale has been selected.
        m_InitializeOperation = LocalizationSettings.SelectedLocaleAsync;
        if (m_InitializeOperation.IsDone)
        {<!-- -->
            InitializeCompleted(m_InitializeOperation);
        }
        else
        {<!-- -->
            m_InitializeOperation.Completed += InitializeCompleted;
        }
    }

    void InitializeCompleted(AsyncOperationHandle obj)
    {<!-- -->
        var locales = LocalizationSettings.AvailableLocales.Locales;
        for (int i = 0; i &lt; locales.Count; ++i)
        {<!-- -->
            var locale = locales[i];
            if (locale.LocaleName == "Chinese (Simplified) (zh)")
            {<!-- -->
                _chineseLocale = locale;
            }
            else if (locale.LocaleName == "English (en)")
            {<!-- -->
                _englishLocale = locale;
            }
        }
    }

    public void SwitchChinese()
    {<!-- -->
        LocalizationSettings.Instance.SetSelectedLocale(_chineseLocale);
    }
    public void SwitchEnglish()
    {<!-- -->
        LocalizationSettings.Instance.SetSelectedLocale(_englishLocale);
    }
}

```

将该脚本挂载到场景中，并在场景中添加两个Button分别绑定切换中英文的方法即可。 <img src="https://img-blog.csdnimg.cn/3d87502208fd489583a01cf98acf923a.gif" alt="请添加图片描述">

上述脚本代码也可以换成下方这种，更简单粗暴的方法切换语言。

```
using UnityEngine;
using UnityEngine.Localization.Settings;

public class LanguageManager : MonoBehaviour
{<!-- -->
    public void SwitchChinese()
    {<!-- -->
        LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[0];
    }
    public void SwitchEnglish()
    {<!-- -->
        LocalizationSettings.SelectedLocale = LocalizationSettings.AvailableLocales.Locales[1];
    }
}

```

索引值为Localization 的配置项中的多种语言的顺序，如下方第一个语言为中文则索引为0。 <img src="https://img-blog.csdnimg.cn/8ea9489b7fa143748285523bab610e39.png" alt="在这里插入图片描述">

#### 3.2 动态文本

除了可以设置静态文本，也可以在代码中获取对应的文本并进行动态设置，下面看一下动态文本的设置方法。

设置动态文本的方法有很多种，可以看情况选择，具体原理可以在官方文档仔细查阅，这里就直接写几种方法的使用示例。

**1.最简单粗暴的方法，直接动态读表赋值。**

```
using UnityEngine;
using UnityEngine.Localization.Settings;
using UnityEngine.UI;

public class TestLocalization : MonoBehaviour
{<!-- -->
    public Text text;

    void Start()
    {<!-- -->
        var loadingResult = LocalizationSettings.StringDatabase.GetTableEntry("UITestTable", "ui_Test");
        text.text = loadingResult.Entry.GetLocalizedString();
    }
}

```

`GetTableEntry()` 第一个参数为多语言配置表的名字，第二个参数为该表里面的Key。

通过方法传入多语言配置表的名字及对应多语言的Key即可完成动态文本赋值。

不过要注意的是字符串表可能不会立即可用，例如在本地化系统初始化期间或尚未加载表时。

为了保险起见，可以确保该多语言配置表被加载出之后再进行赋值，可以来看第二种方法的使用示例。

**2.等待语言配置表初始化之后在赋值。**

```
using System.Collections;
using UnityEngine.ResourceManagement.AsyncOperations;
using UnityEngine;
using UnityEngine.Localization.Settings;
using UnityEngine.UI;

public class TestLocalization : MonoBehaviour
{<!-- -->
    public Text text;

    void Start()
    {<!-- -->
        StartCoroutine(LoadStrings());
    }

    IEnumerator LoadStrings()
    {<!-- -->
        // A string table may not be immediately available such as during initialization of the localization system or when a table has not been loaded yet.
        var loadingOperation = LocalizationSettings.StringDatabase.GetTableAsync("UITestTable");
        yield return loadingOperation;
    
        if (loadingOperation.Status == AsyncOperationStatus.Succeeded)
        {<!-- -->
            var stringTable = loadingOperation.Result;
            text.text = stringTable.GetEntry("ui_Test").GetLocalizedString();
        }
        else
        {<!-- -->
            Debug.LogError("Could not load String Table\n" + loadingOperation.OperationException.ToString());
        }
    }
}

```

**3.初始化时获得该多语言配置表，事件动态更新文本。**

```
using UnityEngine;
using UnityEngine.Localization;
using UnityEngine.Localization.Tables;
using UnityEngine.UI;

public class Demo : MonoBehaviour
{<!-- -->
    public Text Name;
    private LocalizedStringTable stringTable = new LocalizedStringTable {<!-- --> TableReference = "UITestTable" };

    void OnEnable()
    {<!-- -->
        stringTable.TableChanged += LoadStrings;
    }

    void OnDisable()
    {<!-- -->
        stringTable.TableChanged -= LoadStrings;
    }

    void LoadStrings(StringTable stringTable)
    {<!-- -->
        Name.text = GetLocalizedString(stringTable, "ui_Test");
    }

    static string GetLocalizedString(StringTable table, string entryName)
    {<!-- -->
        var entry = table.GetEntry(entryName);
        return entry.GetLocalizedString();
    }
}

```

以上几种方法都可以正常使用，根据实际需求选择合适的即可。

### 四、资源多语言映射表

除了上面说到的文本的本地化之外，Localization 还支持资源本地化，使用方法与配置文本的方法类似，下面来看一下。

打开菜单栏 `Window -&gt; Asset Management -&gt; Localization Tables `，点击New Table Collection创建表格。

该表格用于建立不同资源之间的对应关系，一个key对应多个语言的资源，这里选择创建一个资源配置表(AssetsTable Collection)，写好表名后点击Create就可以创建了，然后选择一个路径目录进行保存。 <img src="https://img-blog.csdnimg.cn/3c94fdfaac984470afd32cf8e4a1053c.png" alt="在这里插入图片描述">

创建完之后与文本配置的处理方式一样，在表中添加Key以及资源的内容，测试示例如下： <img src="https://img-blog.csdnimg.cn/8421441512c74f91b580fd2f2d1ea646.png" alt="在这里插入图片描述">

然后在场景中添加一个Image组件，在右侧菜单点击Localize(或者自己添加组件)，选择我们添加的资源配置表中的Key即可完成。 <img src="https://img-blog.csdnimg.cn/f66fd499a35c4c689f44958d697c4426.png" alt="在这里插入图片描述">

效果如下，可以使用方法控制切换语言，也可以通过右上角进行切换。 <img src="https://img-blog.csdnimg.cn/fc098c045fc143d2b4e1a5604c400491.gif" alt="请添加图片描述">

### 五、映射表 导入/导出 Excel 便于管理

当项目中的文本量比较多的时候，使用Localization Table的方法会有些难以操作不便于管理。

所以此时可以考虑将Localization Table导出为Excel表格对文本进行管理，Localization 是支持Table的导入和导出的，下面来看一下怎样操作。

#### 5.1 导出Localization Table为CSV

打开Localization Tables，然后右键Localization Table，选择 `Export -&gt; CSV...`导出。 <img src="https://img-blog.csdnimg.cn/4667d8bce0a043378aa7f200c333c29d.png" alt="在这里插入图片描述">

选择一个文件目录进行保存，就可以看到导出的Excel表格内容了，就是Localization Table中的内容。 <img src="https://img-blog.csdnimg.cn/5b6d7c1fbc7e43fda3a5d32e03773889.png" alt="在这里插入图片描述">

#### 5.2 修改Excel中并重新导入

在导出的Excel表格中我们可以进行增删改查的操作对表格进行管理，这样比直接在Localization Table中管理要轻松的多。

<img src="https://img-blog.csdnimg.cn/280e41a4342545068ea1320025169ab2.png" alt="在这里插入图片描述"> 修改完之后可以在导入Localization Table中，要注意的是修改完之后要改成`UTF-8的编码格式`再保存文件，不然导入之后中文会显示乱码。

如果不知道怎么直接保存为UTF-8的编码格式，可以使用Notepad++等工具转一下就可以了。 <img src="https://img-blog.csdnimg.cn/f179b88092104f338e52498126523ae5.png" alt="在这里插入图片描述">

点击`Import -&gt; CSV...`选择对应的文件进行导入。 <img src="https://img-blog.csdnimg.cn/b43361e9fb4f4f0a865ece6742f4dd27.png" alt="在这里插入图片描述">

这样就可以看到从Excel中修改后的内容导入到Localization Table中啦。 <img src="https://img-blog.csdnimg.cn/cf773aec53934c7c99afa7406a63c480.png" alt="在这里插入图片描述">

乱码问题：https://blog.csdn.net/shishuijun/article/details/129961436

### 六、Build

如果需要打包项目的话还需要对Localization Tables进行Build一次，方法也很简单，下面看一下怎样操作。

打开菜单栏 `Window -&gt; Asset Management -&gt; Addressables -&gt; Groups`。 <img src="https://img-blog.csdnimg.cn/145d833506ed4688b07cca5e6b4564de.png" alt="在这里插入图片描述">

然后在该窗口中选择`Build -&gt; New Build -&gt; Defaul Build Script` 进行Build，等待Build完成即可。 <img src="https://img-blog.csdnimg.cn/11d5e6978e374637b4b965f2186a076e.png" alt="在这里插入图片描述">

## 总结
- `Localization` 工具的优点在于该插件是Unity引擎原生解决方案，使用时只需要通过Package Manger导入即可。- 导入及配置都比较简单，对于一些文本量不是很大的项目来说，该方案非常的合适。- 当项目对文本量需求非常大的时候，就需要配合Excel来管理了。- 整理来说效果不错，操作简单易上手，基本功能都有，是值得学习的一款多语言本地化解决方案。
🎁🎁🎁 最后给大家推荐一个功能齐全而且很好用的 **IP代理网站**：

使用这个代理IP，可以很轻松地访问网站公开数据，避免被追踪和监控，保护自己的隐私和安全。而且这个代理IP还可以帮助我们加速网页的加载速度，提高工作效率。

现在使用这个链接（）注册的新用户还可以直接白嫖最少300M的流量，注册认证后最高可以送7.5G流量哦！

加上最近年终也有活动，优惠力度还是蛮大的，有需要的小伙伴可以去搞一下试试，`注册 == 白嫖`。

如果对此非常感兴趣之前没有用过或者不会使用的小伙伴也不用着急，在官网都有详细的教程可以看，后面有时间的话也可以出一期教程帮助大家快速上手使用的哦！

>  
 -  🎬 博客主页： -  🎥 本文由 **呆呆敲代码的小Y** 原创 🙉 -  🎄 学习专栏推荐： -  🌲 游戏制作专栏推荐： -  🌲Unity实战100例专栏推荐： -  🏅 欢迎点赞 👍 收藏 ⭐留言 📝 如有错误敬请指正！ -  📆 未来很长，值得我们全力奔赴更美好的生活✨ -  ------------------❤️分割线❤️-------------------------  


<img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述"><img src="https://img-blog.csdnimg.cn/fca9590298da4004906d83d81f4ca0e6.gif" alt="请添加图片描述">

<img src="https://img-blog.csdnimg.cn/01e7ec91f0984ce4a166bf72cb52bea5.gif" alt="请添加图片描述">
