
--- 
title:  前端调用exe程序 
tags: []
categories: [] 

---
**实现过程：**Java语言编写程序并操作注册表，通过exe4j工具将程序打包成exe,通过前端界面联动exe程序并传参。

## 一、使用技术

>  
 【**java.util.prefs.Preferences**】 
 优点：java API中的类，使用简单方便 
 缺点：64位系统下只能在 
         [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\JavaSoft\Prefs] 
         [HKEY_CURRENT_USER\Software\JavaSoft\Prefs]中操作 
 【由于前端启动的exe程序的注册表需要在HKEY_CLASSES_ROOT下，所以该方法不可用】 


>  
 **com.ice.jni.registry**使用JNI技术 &lt;&gt;，该包是Windows注册表API的Java本机接口，这使得Java程序可以非常方便的访问，修改Windows的注册表资源。Java Native  Interface（**JNI**）是Java语言的本地编程接口，是J2SDK的一部分。它提供了若干的实现了Java和其他语言的通信（主要是&amp;），通俗来说，就是JAVA调用C/C++函数的接口，如果你要想调用C系列的函数,你就必须遵守这样的约定。 


>  
 **exe4j**是一款很经典的将Java类文件打包成.exe文件的软件，支持把jar class文件等编译成windows下能够直接运行的exe文件，还可以添加启动等待画面 


## 二、Java操作

### 2.1创建JavaSE项目

### 2.2导入资源

1.添加registry.jar包

2.将dll文件放入jdk/bin目录下

如果出现以下报错，说明jdk和dll文件的位数不符：

<img alt="" height="199" src="https://img-blog.csdnimg.cn/f0ccc5d67701469984eebf82611ddf07.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 解决办法：下载64为的dll 

###  2.3创建注册表目录

```
public class RegisteryUtil {
    static final String KEY_NAME = "aClient";
    static final String EXE__PATH="C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe";

    @SneakyThrows
    public void isRegExist() {
        RegistryKey subKey = Registry.HKEY_CLASSES_ROOT.createSubKey(KEY_NAME,"");
        RegStringValue value = new RegStringValue(subKey, "");
        value.setData("aClientProtocol");
        subKey.setValue(value);
        subKey.setValue(new RegStringValue(subKey, "URL Protocol", EXE__PATH));
        subKey.closeKey();

        RegistryKey subKey1 = Registry.HKEY_CLASSES_ROOT.createSubKey(KEY_NAME + "\\DefaultIcon", EXE__PATH);
        RegStringValue value1 = new RegStringValue(subKey1, "");
        value1.setData(EXE__PATH);
        subKey1.setValue(value1);
        subKey1.closeKey();
        RegistryKey subKey2 = Registry.HKEY_CLASSES_ROOT.createSubKey(KEY_NAME + "\\shell", "");
        subKey2.closeKey();
        RegistryKey subKey3 = Registry.HKEY_CLASSES_ROOT.createSubKey(KEY_NAME + "\\shell\\open", "");
        subKey3.closeKey();
        RegistryKey subKey4 = Registry.HKEY_CLASSES_ROOT.createSubKey(KEY_NAME + "\\shell\\open\\command", "");
        RegStringValue value2 = new RegStringValue(subKey4, "");
        value2.setData(EXE__PATH);
        subKey4.setValue(value2);
        subKey4.closeKey();

    }

}

```

运行结果：

<img alt="" height="725" src="https://img-blog.csdnimg.cn/1491e9e515b64158acc4ea4a6d10ab2a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

##  三、exe4j打包

>  
 ，提取码： b3cy 


<img alt="" height="964" src="https://img-blog.csdnimg.cn/92dd7892942745f78e26c4ce7ab0be00.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

<img alt="" height="306" src="https://img-blog.csdnimg.cn/b9950f0e81214e4fbbc46ba14c2ff2ea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_13,color_FFFFFF,t_70,g_se,x_16" width="567">

>  
 **密匙：A-XVK275016F-15wjjcbn4tpj ** 


 <img alt="" height="948" src="https://img-blog.csdnimg.cn/fde5f77cd5d0403081c892da51abb059.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 <img alt="" height="505" src="https://img-blog.csdnimg.cn/b037f6470eda44d5bb32a506fe66b7ff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 <img alt="" height="520" src="https://img-blog.csdnimg.cn/546a05a2c2e941889531985f2fad4d3d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1053">

<img alt="" height="639" src="https://img-blog.csdnimg.cn/9ff77e2bf4164704b8f2a8cc25868f18.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

<img alt="" height="809" src="https://img-blog.csdnimg.cn/29fda65fe1264bd0864177130473c4e8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="972">

 <img alt="" height="890" src="https://img-blog.csdnimg.cn/96bae12bac734404a4d1e4faecc4665f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

如果是springboot项目，选择这个：

<img alt="" height="429" src="https://img-blog.csdnimg.cn/09ed9242f87c412eb0b7d95be783a93c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="936">

 <img alt="" height="420" src="https://img-blog.csdnimg.cn/7f7a8c89a6684a3882f50de89a7bb1a7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1191">

 <img alt="" height="943" src="https://img-blog.csdnimg.cn/e3cdc642d3674bf381761c668535dbdb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

## 四、前端

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;title&gt;ForC&lt;/title&gt;
  &lt;meta name="language" content="zh-CN"&gt;
&lt;/head&gt;

&lt;body&gt;

&lt;a href="aClient://=参数1=参数2"&gt;打开程序&lt;/a&gt;

&lt;/body&gt;

&lt;/html&gt;

```

因为前端给exe传参只能传递一个参数，所以需要用=号连接，后端进行解析即可。

【注意：后边会有一个 /】

## 五、注册表传参格式

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\aClient]
@="aClientProtocol"
"URL Protocol"="C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"
 
[HKEY_CLASSES_ROOT\aClient\DefaultIcon]
@="C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe,1" 

[HKEY_CLASSES_ROOT\aClient\shell]
@="" 

[HKEY_CLASSES_ROOT\aClient\shell\open]
@=""

[HKEY_CLASSES_ROOT\aClient\shell\open\command]
@="\"C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe\" \"%1\""

```

## 六、错误解决

### 6.1依赖问题

<img alt="" height="302" src="https://img-blog.csdnimg.cn/02d574ed10c140a6a5dbdf8e3619195d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

解决方案：可以将依赖包推送至本地maven仓库

### 6.2启动类错误

<img alt="" height="226" src="https://img-blog.csdnimg.cn/c7be928ff88748668899d675adce431d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 解决：

<img alt="" height="429" src="https://img-blog.csdnimg.cn/09ed9242f87c412eb0b7d95be783a93c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="936">

###  6.3启动awt错误

<img alt="" height="339" src="https://img-blog.csdnimg.cn/57bc6f0cf300428c9d4a49378a95e49d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 解决方案：

<img alt="" height="363" src="https://img-blog.csdnimg.cn/4e497ecd6ab24295a88c98e709d5bf99.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

>  
  -Djava.awt.headless=false 
  -Dfile.encoding=UTF-8（解决获取数据乱码问题） 


## 七、运行问题

此时生成exe有一个问题：在开发的电脑上运行完全没有问题，但是一旦在别人的电脑上就有问题，尤其是没有配置jdk环境的电脑上运行会报错：

<img alt="" height="384" src="https://img-blog.csdnimg.cn/ebdb8ce98f894d0ea134a59306dbd048.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="856">

原因就是：没有将程序所依赖的环境进行打包。

解决方案：

<img alt="" height="804" src="https://img-blog.csdnimg.cn/e5cca56607fe48bd8f8b74646a94ee9a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 <img alt="" height="632" src="https://img-blog.csdnimg.cn/262cde51eaca40d5b9ddd9542db36cb9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 <img alt="" height="896" src="https://img-blog.csdnimg.cn/7247d854e55a42f0a6fb0275c19fe30c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200">

 此时，将生成的exe和jdk的上次目录同级，就可以在没有jdk环境的电脑上正常运行exe程序了。

## 八、Inno setup打包

 以上效果，需要我们手动的将exe程序和包含jdk的目录放在同级，为了解决这个手动过程，需要使用Inno Setup软件进行打包。

>  
  是一个免费的 Windows 安装程序制作软件。第一次发表是在 1997 年，现在已经更新到Inno Setup 5了。Inno Setup是一个十分简单实用的打包小工具，可以按照我们自己的意愿设置功能，稳定性也十分好。下载地址 


### 8.1增加中文语言包

>  
  将下面内容复制保存为ChineseSimplified.isl文件名放入Inno Setup/Languages目录下 


```
; *** Inno Setup version 6.0.3+ Chinese Simplified messages ***
;
; Maintained by Zhenghan Yang
; Email: 847320916@QQ.com
; Translation based on network resource
; The latest Translation is on https://github.com/kira-96/Inno-Setup-Chinese-Simplified-Translation
;

[LangOptions]
; The following three entries are very important. Be sure to read and 
; understand the '[LangOptions] section' topic in the help file.
LanguageName=简体中文
; If Language Name display incorrect, uncomment next line
; LanguageName=&lt;7B80&gt;&lt;4F53&gt;&lt;4E2D&gt;&lt;6587&gt;
LanguageID=$0804
LanguageCodePage=936
; If the language you are translating to requires special font faces or
; sizes, uncomment any of the following entries and change them accordingly.
;DialogFontName=
;DialogFontSize=8
;WelcomeFontName=Verdana
;WelcomeFontSize=12
;TitleFontName=Arial
;TitleFontSize=29
;CopyrightFontName=Arial
;CopyrightFontSize=8

[Messages]

; *** 应用程序标题
SetupAppTitle=安装
SetupWindowTitle=安装 - %1
UninstallAppTitle=卸载
UninstallAppFullTitle=%1 卸载

; *** Misc. common
InformationTitle=信息
ConfirmTitle=确认
ErrorTitle=错误

; *** SetupLdr messages
SetupLdrStartupMessage=现在将安装 %1。您想要继续吗？
LdrCannotCreateTemp=不能创建临时文件。安装中断。
LdrCannotExecTemp=不能执行临时目录中的文件。安装中断。
HelpTextNote=

; *** 启动错误消息
LastErrorMessage=%1.%n%n错误 %2: %3
SetupFileMissing=安装目录中的文件 %1 丢失。请修正这个问题或获取一个新的程序副本。
SetupFileCorrupt=安装文件已损坏。请获取一个新的程序副本。
SetupFileCorruptOrWrongVer=安装文件已损坏，或是与这个安装程序的版本不兼容。请修正这个问题或获取新的程序副本。
InvalidParameter=无效的命令行参数: %n%n%1
SetupAlreadyRunning=安装程序正在运行。
WindowsVersionNotSupported=这个程序不支持该版本的计算机运行。
WindowsServicePackRequired=这个程序要求%1服务包%1或更高。
NotOnThisPlatform=这个程序将不能运行于 %1。
OnlyOnThisPlatform=这个程序必须运行于 %1。
OnlyOnTheseArchitectures=这个程序只能在为下列处理器结构设计的 Windows 版本中进行安装:%n%n%1
WinVersionTooLowError=这个程序需要 %1 版本 %2 或更高。
WinVersionTooHighError=这个程序不能安装于 %1 版本 %2 或更高。
AdminPrivilegesRequired=在安装这个程序时您必须以管理员身份登录。
PowerUserPrivilegesRequired=在安装这个程序时您必须以管理员身份或有权限的用户组身份登录。
SetupAppRunningError=安装程序发现 %1 当前正在运行。%n%n请先关闭所有运行的窗口，然后单击“确定”继续，或按“取消”退出。
UninstallAppRunningError=卸载程序发现 %1 当前正在运行。%n%n请先关闭所有运行的窗口，然后单击“确定”继续，或按“取消”退出。

; *** 启动问题
PrivilegesRequiredOverrideTitle=选择安装程序模式
PrivilegesRequiredOverrideInstruction=选择安装模式
PrivilegesRequiredOverrideText1=%1 可以为所有用户安装(需要管理员权限)，或仅为您安装。
PrivilegesRequiredOverrideText2=%1 只能为您安装，或为所有用户安装(需要管理员权限)。
PrivilegesRequiredOverrideAllUsers=为所有用户安装(&amp;A)
PrivilegesRequiredOverrideAllUsersRecommended=为所有用户安装(建议选项)(&amp;A)
PrivilegesRequiredOverrideCurrentUser=只为我安装(&amp;M)
PrivilegesRequiredOverrideCurrentUserRecommended=只为我安装(建议选项)(&amp;M)

; *** 其它错误
ErrorCreatingDir=安装程序不能创建目录“%1”。
ErrorTooManyFilesInDir=不能在目录“%1”中创建文件，因为里面的文件太多

; *** 安装程序公共消息
ExitSetupTitle=退出安装程序
ExitSetupMessage=安装程序未完成安装。如果您现在退出，您的程序将不能安装。%n%n您可以以后再运行安装程序完成安装。%n%n退出安装程序吗？
AboutSetupMenuItem=关于安装程序(&amp;A)...
AboutSetupTitle=关于安装程序
AboutSetupMessage=%1 版本 %2%n%3%n%n%1 主页:%n%4
AboutSetupNote=
TranslatorNote=

; *** 按钮
ButtonBack=&lt; 上一步(&amp;B)
ButtonNext=下一步(&amp;N) &gt;
ButtonInstall=安装(&amp;I)
ButtonOK=确定
ButtonCancel=取消
ButtonYes=是(&amp;Y)
ButtonYesToAll=全是(&amp;A)
ButtonNo=否(&amp;N)
ButtonNoToAll=全否(&amp;O)
ButtonFinish=完成(&amp;F)
ButtonBrowse=浏览(&amp;B)...
ButtonWizardBrowse=浏览(&amp;R)...
ButtonNewFolder=新建文件夹(&amp;M)

; *** “选择语言”对话框消息
SelectLanguageTitle=选择安装语言
SelectLanguageLabel=选择安装时要使用的语言。

; *** 公共向导文字
ClickNext=单击“下一步”继续，或单击“取消”退出安装程序。
BeveledLabel=
BrowseDialogTitle=浏览文件夹
BrowseDialogLabel=在下列列表中选择一个文件夹，然后单击“确定”。
NewFolderName=新建文件夹

; *** “欢迎”向导页
WelcomeLabel1=欢迎使用 [name] 安装向导
WelcomeLabel2=现在将安装 [name/ver] 到您的电脑中。%n%n推荐您在继续安装前关闭所有其它应用程序。

; *** “密码”向导页
WizardPassword=密码
PasswordLabel1=这个安装程序有密码保护。
PasswordLabel3=请输入密码，然后单击“下一步”继续。密码区分大小写。
PasswordEditLabel=密码(&amp;P):
IncorrectPassword=您输入的密码不正确，请重试。

; *** “许可协议”向导页
WizardLicense=许可协议
LicenseLabel=继续安装前请阅读下列重要信息。
LicenseLabel3=请仔细阅读下列许可协议。您在继续安装前必须同意这些协议条款。
LicenseAccepted=我同意此协议(&amp;A)
LicenseNotAccepted=我不同意此协议(&amp;D)

; *** “信息”向导页
WizardInfoBefore=信息
InfoBeforeLabel=请在继续安装前阅读下列重要信息。
InfoBeforeClickLabel=如果您想继续安装，单击“下一步”。
WizardInfoAfter=信息
InfoAfterLabel=请在继续安装前阅读下列重要信息。
InfoAfterClickLabel=如果您想继续安装，单击“下一步”。

; *** “用户信息”向导页
WizardUserInfo=用户信息
UserInfoDesc=请输入您的信息。
UserInfoName=用户名(&amp;U):
UserInfoOrg=组织(&amp;O):
UserInfoSerial=序列号(&amp;S):
UserInfoNameRequired=您必须输入名字。

; *** “选择目标目录”向导面
WizardSelectDir=选择目标位置
SelectDirDesc=您想将 [name] 安装在什么地方？
SelectDirLabel3=安装程序将安装 [name] 到下列文件夹中。
SelectDirBrowseLabel=单击“下一步”继续。如果您想选择其它文件夹，单击“浏览”。
DiskSpaceGBLabel=至少需要有 [gb] GB 的可用磁盘空间。
DiskSpaceMBLabel=至少需要有 [mb] MB 的可用磁盘空间。
CannotInstallToNetworkDrive=安装程序无法安装到一个网络驱动器。
CannotInstallToUNCPath=安装程序无法安装到一个UNC路径。
InvalidPath=您必须输入一个带驱动器卷标的完整路径，例如:%n%nC:\APP%n%n或下列形式的 UNC 路径:%n%n\\server\share
InvalidDrive=您选定的驱动器或 UNC 共享不存在或不能访问。请选选择其它位置。
DiskSpaceWarningTitle=没有足够的磁盘空间
DiskSpaceWarning=安装程序至少需要 %1 KB 的可用空间才能安装，但选定驱动器只有 %2 KB 的可用空间。%n%n您一定要继续吗？
DirNameTooLong=文件夹名或路径太长。
InvalidDirName=文件夹名是无效的。
BadDirName32=文件夹名不能包含下列任何字符:%n%n%1
DirExistsTitle=文件夹存在
DirExists=文件夹:%n%n%1%n%n已经存在。您一定要安装到这个文件夹中吗？
DirDoesntExistTitle=文件夹不存在
DirDoesntExist=文件夹:%n%n%1%n%n不存在。您想要创建此目录吗？

; *** “选择组件”向导页
WizardSelectComponents=选择组件
SelectComponentsDesc=您想安装哪些程序的组件？
SelectComponentsLabel2=选择您想要安装的组件；清除您不想安装的组件。然后单击“下一步”继续。
FullInstallation=完全安装
; if possible don't translate 'Compact' as 'Minimal' (I mean 'Minimal' in your language)
CompactInstallation=简洁安装
CustomInstallation=自定义安装
NoUninstallWarningTitle=组件存在
NoUninstallWarning=安装程序侦测到下列组件已在您的电脑中安装。:%n%n%1%n%n取消选定这些组件将不能卸载它们。%n%n您一定要继续吗？
ComponentSize1=%1 KB
ComponentSize2=%1 MB
ComponentsDiskSpaceGBLabel=当前选择的组件至少需要 [gb] GB 的磁盘空间。
ComponentsDiskSpaceMBLabel=当前选择的组件至少需要 [mb] MB 的磁盘空间。

; *** “选择附加任务”向导页
WizardSelectTasks=选择附加任务
SelectTasksDesc=您想要安装程序执行哪些附加任务？
SelectTasksLabel2=选择您想要安装程序在安装 [name] 时执行的附加任务，然后单击“下一步”。

; *** “选择开始菜单文件夹”向导页
WizardSelectProgramGroup=选择开始菜单文件夹
SelectStartMenuFolderDesc=您想在哪里放置程序的快捷方式？
SelectStartMenuFolderLabel3=安装程序现在将在下列开始菜单文件夹中创建程序的快捷方式。
SelectStartMenuFolderBrowseLabel=单击“下一步”继续。如果您想选择其它文件夹，单击“浏览”。
MustEnterGroupName=您必须输入一个文件夹名。
GroupNameTooLong=文件夹名或路径太长。
InvalidGroupName=文件夹名是无效的。
BadGroupName=文件夹名不能包含下列任何字符:%n%n%1
NoProgramGroupCheck2=不创建开始菜单文件夹(&amp;D)

; *** “准备安装”向导页
WizardReady=准备安装
ReadyLabel1=安装程序现在准备开始安装 [name] 到您的电脑中。
ReadyLabel2a=单击“安装”继续此安装程序。如果您想要回顾或改变设置，请单击“上一步”。
ReadyLabel2b=单击“安装”继续此安装程序?
ReadyMemoUserInfo=用户信息:
ReadyMemoDir=目标位置:
ReadyMemoType=安装类型:
ReadyMemoComponents=选定组件:
ReadyMemoGroup=开始菜单文件夹:
ReadyMemoTasks=附加任务:

; *** “正在准备安装”向导页
WizardPreparing=正在准备安装
PreparingDesc=安装程序正在准备安装 [name] 到您的电脑中。
PreviousInstallNotCompleted=先前程序的安装/卸载未完成。您需要重新启动您的电脑才能完成安装。%n%n在重新启动电脑后，再运行安装完成 [name] 的安装。
CannotContinue=安装程序不能继续。请单击“取消”退出。
ApplicationsFound=下列应用程序正在使用的文件需要更新设置。它是建议您允许安装程序自动关闭这些应用程序。
ApplicationsFound2=下列应用程序正在使用的文件需要更新设置。它是建议您允许安装程序自动关闭这些应用程序。安装完成后，安装程序将尝试重新启动应用程序。
CloseApplications=自动关闭该应用程序(&amp;A)
DontCloseApplications=不要关闭该应用程序(D)
ErrorCloseApplications=安装程序无法自动关闭所有应用程序。在继续之前，我们建议您关闭所有使用需要更新的安装程序文件。
PrepareToInstallNeedsRestart=安装程序必须重新启动计算机。重新启动计算机后，请再次运行安装程序以完成 [name] 的安装。%n%n是否立即重新启动？

; *** “正在安装”向导页
WizardInstalling=正在安装
InstallingLabel=安装程序正在安装 [name] 到您的电脑中，请稍等。

; *** “安装完成”向导页
FinishedHeadingLabel=[name] 安装完成
FinishedLabelNoIcons=安装程序已在您的电脑中安装了 [name]。
FinishedLabel=安装程序已在您的电脑中安装了 [name]。此应用程序可以通过选择安装的快捷方式运行。
ClickFinish=单击“完成”退出安装程序。
FinishedRestartLabel=要完成 [name] 的安装，安装程序必须重新启动您的电脑。您想现在重新启动吗？
FinishedRestartMessage=要完成 [name] 的安装，安装程序必须重新启动您的电脑。%n%n您想现在重新启动吗？
ShowReadmeCheck=是，您想查阅自述文件
YesRadio=是，立即重新启动电脑(&amp;Y)
NoRadio=否，稍后重新启动电脑(&amp;N)
; 用于象“运行 MyProg.exe”
RunEntryExec=运行 %1
; 用于象“查阅 Readme.txt”
RunEntryShellExec=查阅 %1

; *** “安装程序需要下一张磁盘”提示
ChangeDiskTitle=安装程序需要下一张磁盘
SelectDiskLabel2=请插入磁盘 %1 并单击“确定”。%n%n如果这个磁盘中的文件不能在不同于下列显示的文件夹中找到，输入正确的路径或单击“浏览”。
PathLabel=路径(&amp;P):
FileNotInDir2=文件“%1”不能在“%2”定位。请插入正确的磁盘或选择其它文件夹。
SelectDirectoryLabel=请指定下一张磁盘的位置。

; *** 安装状态消息
SetupAborted=安装程序未完成安装。%n%n请修正这个问题并重新运行安装程序。
AbortRetryIgnoreSelectAction=选项
AbortRetryIgnoreRetry=重试(&amp;T)
AbortRetryIgnoreIgnore=忽略错误并继续(&amp;I)
AbortRetryIgnoreCancel=关闭安装程序

; *** 安装状态消息
StatusClosingApplications=正在关闭应用程序...
StatusCreateDirs=正在创建目录...
StatusExtractFiles=正在解压缩文件...
StatusCreateIcons=正在创建快捷方式...
StatusCreateIniEntries=正在创建 INI 条目...
StatusCreateRegistryEntries=正在创建注册表条目...
StatusRegisterFiles=正在注册文件...
StatusSavingUninstall=正在保存卸载信息...
StatusRunProgram=正在完成安装...
StatusRestartingApplications=正在重启应用程序...
StatusRollback=正在撤销更改...

; *** 其它错误
ErrorInternal2=内部错误: %1
ErrorFunctionFailedNoCode=%1 失败
ErrorFunctionFailed=%1 失败；错误代码 %2
ErrorFunctionFailedWithMessage=%1 失败；错误代码 %2.%n%3
ErrorExecutingProgram=不能执行文件:%n%1

; *** 注册表错误
ErrorRegOpenKey=打开注册表项时出错:%n%1\%2
ErrorRegCreateKey=创建注册表项时出错:%n%1\%2
ErrorRegWriteKey=写入注册表项时出错:%n%1\%2

; *** INI 错误
ErrorIniEntry=在文件“%1”创建 INI 项目错误。

; *** 文件复制错误
FileAbortRetryIgnoreSkipNotRecommended=跳过这个文件 (不推荐)(&amp;S)
FileAbortRetryIgnoreIgnoreNotRecommended=忽略错误并继续 (不推荐)(&amp;I)
SourceIsCorrupted=源文件已损坏
SourceDoesntExist=源文件“%1”不存在
ExistingFileReadOnly2=无法替换现有文件，因为它是只读的。
ExistingFileReadOnlyRetry=移除只读属性并重试(&amp;R)
ExistingFileReadOnlyKeepExisting=保留现有文件(&amp;K)
ErrorReadingExistingDest=尝试读取现有文件时发生一个错误:
FileExists=文件已经存在。%n%n您想要安装程序覆盖它吗？
ExistingFileNewer=现有的文件新与安装程序要安装的文件。推荐您保留现有文件。%n%n您想要保留现有的文件吗？
ErrorChangingAttr=尝试改变下列现有的文件的属性时发生一个错误:
ErrorCreatingTemp=尝试在目标目录创建文件时发生一个错误:
ErrorReadingSource=尝试读取下列源文件时发生一个错误:
ErrorCopying=尝试复制下列文件时发生一个错误:
ErrorReplacingExistingFile=尝试替换现有的文件时发生错误:
ErrorRestartReplace=重启电脑后替换文件失败:
ErrorRenamingTemp=尝试重新命名以下目标目录中的一个文件时发生错误:
ErrorRegisterServer=不能注册 DLL/OCX: %1
ErrorRegSvr32Failed=RegSvr32 失败；退出代码 %1
ErrorRegisterTypeLib=不能注册类型库: %1

; *** 卸载显示名字标记
; used for example as 'My Program (32-bit)'
UninstallDisplayNameMark=%1 (%2)
; used for example as 'My Program (32-bit, All users)'
UninstallDisplayNameMarks=%1 (%2, %3)
UninstallDisplayNameMark32Bit=32位
UninstallDisplayNameMark64Bit=64位
UninstallDisplayNameMarkAllUsers=所有用户
UninstallDisplayNameMarkCurrentUser=当前用户

; *** 安装后错误
ErrorOpeningReadme=当尝试打开自述文件时发生一个错误。
ErrorRestartingComputer=安装程序不能重新启动电脑，请手动重启。

; *** 卸载消息
UninstallNotFound=文件“%1”不存在。不能卸载。
UninstallOpenError=文件“%1”不能打开。不能卸载。
UninstallUnsupportedVer=卸载日志文件“%1”有未被这个版本的卸载器承认的格式。不能卸载
UninstallUnknownEntry=在卸载日志中遇到一个未知的条目 (%1)
ConfirmUninstall=您确认想要完全删除 %1 及它的所有组件吗？
UninstallOnlyOnWin64=这个安装程序只能在 64 位 Windows 中进行卸载。
OnlyAdminCanUninstall=这个安装的程序只能是有管理员权限的用户才能卸载。
UninstallStatusLabel=正在从您的电脑中删除 %1，请等待。
UninstalledAll=%1 已顺利地从您的电脑中删除。
UninstalledMost=%1 卸载完成。%n%n有一些内容不能被删除。您可以手工删除它们。
UninstalledAndNeedsRestart=要完成 %1 的卸载，您的电脑必须重新启动。%n%n您现在想重新启动电脑吗？
UninstallDataCorrupted=“%1”文件被破坏，不能卸载

; *** 卸载状态消息
ConfirmDeleteSharedFileTitle=删除共享文件吗？
ConfirmDeleteSharedFile2=系统中包含的下列共享文件已经不被其它程序使用。您想要卸载程序删除这些共享文件吗？%n%n如果这些文件被删除，但还有程序正在使用这些文件，这些程序可能不能正确执行。如果您不能确定，选择“否”。把这些文件保留在系统中以免引起问题。
SharedFileNameLabel=文件名:
SharedFileLocationLabel=位置:
WizardUninstalling=卸载状态
StatusUninstalling=正在卸载 %1...

; *** Shutdown block reasons
ShutdownBlockReasonInstallingApp=正在安装 %1.
ShutdownBlockReasonUninstallingApp=正在卸载 %1.

; The custom messages below aren't used by Setup itself, but if you make
; use of them in your scripts, you'll want to translate them.

[CustomMessages]

NameAndVersion=%1 版本 %2
AdditionalIcons=附加快捷方式:
CreateDesktopIcon=创建桌面快捷方式(&amp;D)
CreateQuickLaunchIcon=创建快速运行栏快捷方式(&amp;Q)
ProgramOnTheWeb=%1 网站
UninstallProgram=卸载 %1
LaunchProgram=运行 %1
AssocFileExtension=将 %2 文件扩展名与 %1 建立关联(&amp;A)
AssocingFileExtension=正在将 %2 文件扩展名与 %1 建立关联...
AutoStartProgramGroupDescription=启动组:
AutoStartProgram=自动启动 %1
AddonHostProgramNotFound=%1无法找到您所选择的文件夹。%n%n您想要继续吗？

```

###  8.2打包

**以“管理员身份”运行**

新建

<img alt="" height="593" src="https://img-blog.csdnimg.cn/030edeb652494de295b5e3ba438647be.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

<img alt="" height="593" src="https://img-blog.csdnimg.cn/e2a82f33f19d4d1f88e0ea8705e4c4bc.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

<img alt="" height="593" src="https://img-blog.csdnimg.cn/1bb96ec8433842daadc0764d952cfbef.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

 <img alt="" height="593" src="https://img-blog.csdnimg.cn/255a7a48b8ad4e06b247f2884405c090.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

<img alt="" height="593" src="https://img-blog.csdnimg.cn/433874de51a84f139b995d6ed221c174.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

<img alt="" height="593" src="https://img-blog.csdnimg.cn/7c09b042a8f544fa8b3a1b05dcb02959.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5Y2B54K55Y2K55qE5q-b5q-b6Zuo,size_18,color_FFFFFF,t_70,g_se,x_16" width="765">

操作注册表

比如：

```
Root: HKCR; Subkey: "fClient"; Flags: uninsdeletekey
Root: HKCR; Subkey: "fClient"; ValueName: ""; ValueType: string; ValueData: "aClientProtocol"
Root: HKCR; Subkey: "fClient"; ValueName: "URL Protocol"; ValueType: string; ValueData: "C:\Program Files (x86)\fys\fys.exe,1"
Root: HKCR; Subkey: "fClient\DefaultIcon"; ValueName: ""; ValueType: string; ValueData: "C:\Program Files (x86)\fys\fys.exe"
Root: HKCR; Subkey: "fClient\shell"; ValueName: ""; ValueType: string; ValueData: ""
Root: HKCR; Subkey: "fClient\shell\open"; ValueName: ""; ValueType: string; ValueData: ""
Root: HKCR; Subkey: "fClient\shell\open\command"; ValueName: ""; ValueType: string; ValueData: """C:\Program Files (x86)\fys\fys.exe"" ""%1"""
```

## 十、Java调用cmd

```
    public static void main(String[] args){
        ProcessBuilder pb = null;
    	// 创建进程实例，用来启动cmd
        pb = new ProcessBuilder("cmd.exe");
        // 设置文件的工作目录，根据自己的需求设置
        pb.directory(new File("C://Users//86182"));
        // 启动进程，一个start会开启一个进程
        Process p = pb.start();
        // 创建字符缓冲输出流，getOutputStream是得到进程的写入流
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
        // 第一条CMD命令，cd到桌面，最关键得是\n一定要写，注意不要写成/n，不然命令不会被执行，会打印出More?
        bw.write("cd C:/Users/86182//Desktop \n");
        // 第二条命令，创建文件夹。举一反一，有多少条命令，这样写入刷新关闭就可以，不需要用&amp;拼接。
        // 后续可以拿到这个流继续向这个进程写入命令
        bw.write("md Myfile \n");
        // 刷新流，写入后一定要刷新
        bw.flush();
        // 关闭流，注意一定要关闭，不然会阻塞
		bw.close();
		// 下面是获取输出并打印
        InputStream is = p.getInputStream();
        InputStreamReader isr = new InputStreamReader(is, "GBK");
        BufferedReader br = new BufferedReader(isr);
        String line;
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }
    }

```

>  
 cmd /c dir 是执行完dir命令后关闭命令窗口。 
 cmd /k dir 是执行完dir命令后不关闭命令窗口。 
 cmd /c start dir 会打开一个新窗口后执行dir指令，原窗口会关闭。 
 cmd /k start dir 会打开一个新窗口后执行dir指令，原窗口不会关闭。 
 可以用cmd /?查看帮助信息。 

