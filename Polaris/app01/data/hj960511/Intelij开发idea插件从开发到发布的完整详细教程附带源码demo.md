
--- 
title:  Intelij开发idea插件从开发到发布的完整详细教程附带源码demo 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用Intelij开发idea插件的完整详细开发教程，包含了创建项目、开发相对应的功能demo实例等等，以及打包发布插件到插件市场。 日期：2024年01月21日 作者：任聪聪 教程附带源码获取地址： 备忘：可以下载文章附件进行本地的运行和个人的二次开发，里面我封装和书写了很多更清晰的内容，使用附件结合文章掌握idea插件开发的速度会更快一点。 


### 前提条件：

1.下载斌安装了intelij 2020版本或更新版本 2.注册并创建了idea插件市场账号。 3.安装和配置了所需的sdk，和安装了DevKit插件（用于创建插件的action很方便） <img src="https://img-blog.csdnimg.cn/direct/d5ce9ddb325a4ddea5b03945cc873620.png" alt="在这里插入图片描述">

### 一、前提准备——安装所需的sdk及配置项目

#### 0、安装所需的插件

##### 步骤一、进入到项目后打开file菜单，选择setting。

<img src="https://img-blog.csdnimg.cn/direct/d0ec3bc8f4c54c268af5e713a11d47e2.png" alt="在这里插入图片描述">

##### 步骤二、进入到设置节目，点击plugin。

<img src="https://img-blog.csdnimg.cn/direct/539023e5560c472a96be28348aa28b99.png" alt="在这里插入图片描述"> Tips：这个设置界面也可以通过首页的右下角的设置进入。

#### 1、插件所需sdk安装方法，如下是已经安装完毕的。

<img src="https://img-blog.csdnimg.cn/direct/25790b9cdd3748078bfd4cfddf16cf54.png" alt="在这里插入图片描述">

##### 安装说明：

<img src="https://img-blog.csdnimg.cn/direct/aa61a723456c40b38fbc8ad3724eab11.png" alt="在这里插入图片描述"> 点击红框的目录即可完成sdk的添加，无需下载和安装其他类型的sdk，默认弹出的intelij目录即是。

备注：这里添加后，选择sdk，下一步创建项目即可，进入到项目后我们将开始插件的其他sdk的配置

#### 2、创建项目并添加其他所需的java sdk

<img src="https://img-blog.csdnimg.cn/direct/4274c0b46dc8429a9f161c88360f4843.png" alt="在这里插入图片描述">

##### 步骤一、点击Finish进入到项目节目，点击file找到如下的菜单入口

<img src="https://img-blog.csdnimg.cn/direct/11f69577a5e9407482706665c51817e2.png" alt="在这里插入图片描述">

##### 步骤二、进入到配置界面，切换到这个Sdks.

<img src="https://img-blog.csdnimg.cn/direct/720745425992428692d34acedd5301cc.png" alt="在这里插入图片描述">

##### 步骤三、配置所需的jbr，如下图路径，不同版本有所不同，但大致类似

```
C:\Program Files\JetBrains\IntelliJ IDEA 2020.1.4\jbr

```

还有所需的java sdk <img src="https://img-blog.csdnimg.cn/direct/f8aa3a4fe209447db3ae87d15a713ed5.png" alt="在这里插入图片描述"> 配置完毕后，我们就完成了所有的项目开发初期的配置准备。

### 二、填写自己的插件配置信息

#### 进入到项目中，点击plugin.xml，进行编辑如下的配置信息。

<img src="https://img-blog.csdnimg.cn/direct/536536224ddd4f45bb20c180ed28055c.png" alt="在这里插入图片描述"> 你也可以找到配置文件后，直接复制粘贴下面的配置信息：

```
&lt;idea-plugin&gt;
&lt;!--  插件的独立id--&gt;
  &lt;id&gt;com.ideaPlugindemo.rcc.id&lt;/id&gt;
&lt;!--  你的插件名称，也是对应市场的那个--&gt;
  &lt;name&gt;idea学习演示插件&lt;/name&gt;
  &lt;version&gt;1.0&lt;/version&gt;
&lt;!--  你的邮箱、网址和昵称--&gt;
  &lt;vendor email="861157525@qq.com" url="http://rccblogs.com"&gt;任聪聪&lt;/vendor&gt;

  &lt;description&gt;&lt;![CDATA[
      这是插件的描述信息，支持富文本。
    ]]&gt;&lt;/description&gt;

  &lt;change-notes&gt;&lt;![CDATA[
      这是插件的更新记录，支持富文本。
    ]]&gt;
  &lt;/change-notes&gt;

  &lt;!-- please see https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started/build_number_ranges.html for description --&gt;
&lt;!-- 最低可安装的idea版本--&gt;
  &lt;idea-version since-build="173.0"/&gt;

  &lt;!-- please see https://www.jetbrains.org/intellij/sdk/docs/basics/getting_started/plugin_compatibility.html
       on how to target different products --&gt;
  &lt;depends&gt;com.intellij.modules.platform&lt;/depends&gt;
&lt;!--插件所需的依赖信息--&gt;
  &lt;extensions defaultExtensionNs="com.intellij"&gt;
    &lt;!-- Add your extensions here --&gt;
  &lt;/extensions&gt;
&lt;!--方法和行为都在这里--&gt;
  &lt;actions&gt;
    &lt;!-- Add your actions here --&gt;
  &lt;/actions&gt;

&lt;/idea-plugin&gt;

```

### 三、配置完毕后创建我们的插件功能

#### 0、优先创建一个包，如下操作，点击src目录，选择创建包

<img src="https://img-blog.csdnimg.cn/direct/dc2dc6044e0647168e7b94205bd7e9f8.png" alt="在这里插入图片描述"> 设置包名为：com.rcc.ideaPluginDemo <img src="https://img-blog.csdnimg.cn/direct/19b6cbd3801a4363b1bf8cac965acdd6.png" alt="在这里插入图片描述"> 完成后右键，创建action，操作如下图： <img src="https://img-blog.csdnimg.cn/direct/2005fb03bc4a493e8b8d3369ff4bd7e8.png" alt="在这里插入图片描述"> 点击action后，进入到下一步，创建右键选中菜单弹出文本提示的效果。

#### 1、实现右键选中文本弹出提示的效果

##### 步骤一、创建一个右键选中菜单的方法，配置如下

<img src="https://img-blog.csdnimg.cn/direct/22a661f24d5c4298b653a70d72b9d544.png" alt="在这里插入图片描述">

##### 步骤二、创建完毕后，我们会发现plugin.xml的配置文件发生了变化.

<img src="https://img-blog.csdnimg.cn/direct/aeea16e09d034bbda74ec5af72816a18.png" alt="在这里插入图片描述"> 同事在src的包下，新生了一个文件。 <img src="https://img-blog.csdnimg.cn/direct/e4ffd06a34b84b3898e7147c75ef8a67.png" alt="在这里插入图片描述"> 点击右上角的，甲壳虫我们进行插件的运行。 <img src="https://img-blog.csdnimg.cn/direct/9e03836ce2da46f2870b0cb0727d734d.png" alt="在这里插入图片描述"> 进入到沙箱运行的intelij中，右键菜单插件是否生效： <img src="https://img-blog.csdnimg.cn/direct/bf44c1bd21d546479b97961d659433d7.png" alt="在这里插入图片描述"> 可以看到已经生效，接下来我们进入到步骤三、进行书写这个插件功能的效果。

##### 步骤三、填充我们的事件函数

<img src="https://img-blog.csdnimg.cn/direct/7a6f200d6b9c41f0988470ce931f1843.png" alt="在这里插入图片描述"> 按照如图的代码进行填充，依次导入所需的包，完成后保存，点击运行，我们会看到如下效果： <img src="https://img-blog.csdnimg.cn/direct/b7f913002d964e00962d3efddabfb874.png" alt="在这里插入图片描述">

#### 2、实现快捷键呼出弹出框的效果

##### 步骤一、回到plugin.xml插件中，创建自定义的action并绑定快捷键，代码如下：

<img src="https://img-blog.csdnimg.cn/direct/cd6e8cb7ee2a4ceaadcd623b401f23f9.png" alt="在这里插入图片描述"> 说明：此处的代码是直接写上即可，无需通过devkit进行创建，如果你通过devkit进行创建，记得什么都不要选择，之后再回到这个配置文件配置你想设置的快捷键，如图中的first-key…=“你的快捷键多个用空格隔开”

##### 步骤二、创建一个java类，并填充这个类的内容，让其能够在快捷键被按下时执行弹出框的能力

<img src="https://img-blog.csdnimg.cn/direct/f97816b660a7434a981598387b27d64f.png" alt="在这里插入图片描述"> 运行效果如下： <img src="https://img-blog.csdnimg.cn/direct/ba86bcc751ae41c8bffea61437b047f1.png" alt="在这里插入图片描述">

#### 3、设置插件出现的位置——在主菜单显示，点击斌天厨文本输入框的效果

##### 步骤一、创建acion，配置信息如下：

<img src="https://img-blog.csdnimg.cn/direct/df33f51099f2431a968ee092ef93304b.png" alt="在这里插入图片描述">

##### 步骤二、填写action的文件内容，配置一个确认框：

<img src="https://img-blog.csdnimg.cn/direct/fc7d846e2e724b8189acc3e218c12bd3.png" alt="在这里插入图片描述">

##### 步骤三、完成后运行插件，效果如下：

<img src="https://img-blog.csdnimg.cn/direct/142b9c2154f14027b515ecb718762ea2.png" alt="在这里插入图片描述"> 点击后即可弹出确认框： <img src="https://img-blog.csdnimg.cn/direct/cf945b0d2d0344a4a1816bb189913e4c.png" alt="在这里插入图片描述">

##### 其他菜单的设置说明：

在我们创建菜单的时候，会看到如下的菜单名称，默认未other，如果先啧file则会在file下出现，同理其他类似。 <img src="https://img-blog.csdnimg.cn/direct/a34e731cc1304b27ab92ff03e4aba275.png" alt="在这里插入图片描述">

#### 4.实现点击菜单和快捷键打开一个链接的效果

##### 步骤一、创建一个方法，配置如下：

<img src="https://img-blog.csdnimg.cn/direct/d7a47437d193481c82d501f9d83163a8.png" alt="在这里插入图片描述"> Tips：配置快捷键只需要按下按键即可输入。

##### 步骤二、点击ok创建文件后，填充代码，内容如下：

<img src="https://img-blog.csdnimg.cn/direct/305a049546984b1cbac0bb7cf49257eb.png" alt="在这里插入图片描述"> 运行插件，效果如下： <img src="https://img-blog.csdnimg.cn/direct/bced391b1892460699407e2a6160b425.png" alt="在这里插入图片描述">

#### 5.替换选中的文本内容

##### 步骤一、创建一个新的右键菜单，配置如下：

<img src="https://img-blog.csdnimg.cn/direct/b0f25967b4b9454a9ea9798854cf6bfe.png" alt="在这里插入图片描述">

##### 步骤二、进入到对应的java文件中，书写获取选中文本和文本位置进行替换的代码逻辑，内容如下：

<img src="https://img-blog.csdnimg.cn/direct/b05b18dfb6354371a5b6a8531dcdb1c5.png" alt="在这里插入图片描述"> 运行效果如下： <img src="https://img-blog.csdnimg.cn/direct/bc8f7f2cd91e499c8d32445f5cca2d30.gif#pic_center" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/9d6fc162f6ad43779dd9b3f27676a564.gif#pic_center" alt="在这里插入图片描述">

### 四、打包和发布说明：

#### 1、打包配置和说明

##### 步骤一、点击file，点击如下菜单

<img src="https://img-blog.csdnimg.cn/direct/7b452871b75e4d7aa0f3293c0ebac1e3.png" alt="在这里插入图片描述"> 进入到配置界面，点击如图所示Artifacts配置项： <img src="https://img-blog.csdnimg.cn/direct/8069cb907a8b4eb0848e86eb4b2496e7.png" alt="在这里插入图片描述"> 点击+号，点击jar，点击from，进入到步骤二的环节中。 <img src="https://img-blog.csdnimg.cn/direct/4dc9010351034d6da89bd722d3b16c26.png" alt="在这里插入图片描述">

##### 步骤二、进入到jar配置界面，无需过多配置，直接点击ok即可。

<img src="https://img-blog.csdnimg.cn/direct/c833da51cad54d62a8969892e0b0af0e.png" alt="在这里插入图片描述"> 进入到如下界面后，继续点击ok，完成配置。 <img src="https://img-blog.csdnimg.cn/direct/9c36b22274aa43e1ad014a9cd73ef55f.png" alt="在这里插入图片描述">

#### 2.发布的操作说明

##### 步骤一、回到我们的项目界面 ，点击bulid菜单，会看到Bulid Artifacts 已经可以点击。

<img src="https://img-blog.csdnimg.cn/direct/5a72e51f43d141a2ad8c1cfc288426bf.png" alt="在这里插入图片描述"> 点击Bulid Artifacts，进入到下一环节，如下图： <img src="https://img-blog.csdnimg.cn/direct/00d741aa2d5943c7b68d9eccf666abb8.png" alt="在这里插入图片描述"> 此处点击bulid，进入到步骤二环节中。

##### 步骤二、等待打包完成，完成后我们会在out中发现一个jar文件，如下图：

<img src="https://img-blog.csdnimg.cn/direct/c63e8eed81364ab5bbea46f97cd16b32.png" alt="在这里插入图片描述"> 这个文件我们可以在setting的plugin中进行安装和测试，详细见五、常见问题中的安装和测试说明：

#### 3.发布插件

idea插件市场地址：，记得先准备好自己的开发者账号。

##### 步骤一、登录后我们点击自己的昵称，将会看到upload plugin的菜单。

<img src="https://img-blog.csdnimg.cn/direct/048fccda6b144b87860e94ca2e223242.png" alt="在这里插入图片描述"> 点击此菜单，进入到插件信息的填写页面。

##### 步骤二、填写插件的信息

<img src="https://img-blog.csdnimg.cn/direct/bdcccbad2728440aae9db140541efb11.png" alt="在这里插入图片描述"> …此处按照表单说填写即可，填写完毕后提交审核。 <img src="https://img-blog.csdnimg.cn/direct/d461e9bd929f4fad91f5a892b514fbfb.png" alt="在这里插入图片描述"> 不久后，如果idea审核没有问题，你就会搜索到自己的插件了，上线前不要忘记测试下~

### 五、常见问题：

#### 1.logo设置:

名称必须为：pluginIcon.svg 深色模式logo必须为：pluginIcon_dark.svg 路径必须在插件的：META-INF目录下，与plugin.xml同目录 svg必须要支持：40px和80px且尺寸在128px

#### 2.发布事项：

建议打包提交jar格式的，zip打包类型为自己的项目目录。

#### 3.主菜单失效问题修复方法：

<img src="https://img-blog.csdnimg.cn/direct/59870bcfe26f4014ba022d2433278d02.png" alt="在这里插入图片描述"> 默认插件生成的是MainMenu,你会发现测试看不到自己的菜单或者other菜单，这里改为图片的名称即可。

#### 4.按钮为灰色的情况

<img src="https://img-blog.csdnimg.cn/direct/97b1cc267e7543a5b65006c57c3ee3e0.png" alt="在这里插入图片描述"> 这是正常情况，idea系列的编辑器都需要在索引建立完毕后加载插件功能。

#### 5.安装自己做的插件

打开我们的插件安装界面如下图： <img src="https://img-blog.csdnimg.cn/direct/763da2460f7b4e26bc3e43987e35ac67.png" alt="在这里插入图片描述"> 选择install …disk…，进入到目录选择界面，这里选择我们的out目录的jar，并点击ok即可完成安装，如下图： <img src="https://img-blog.csdnimg.cn/direct/691c1162a9dc4652b9a52039e2cd90e4.png" alt="在这里插入图片描述">

#### 6.发布插件到市场报错提示字符数问题

问题截图: <img src="https://img-blog.csdnimg.cn/direct/0ab9485e19c242a5b02945cb5b391056.png#pic_center" alt="在这里插入图片描述"> 解决办法：

```
&lt;description&gt;&lt;![CDATA[超过40个字符]]&gt;&lt;/description&gt;

&lt;change-notes&gt;&lt;![CDATA[超过40个字符]]&gt;&lt;/change-notes&gt;

```

注意必须用英文才能解决问题，同时插件的name标签也要是英文才可。
