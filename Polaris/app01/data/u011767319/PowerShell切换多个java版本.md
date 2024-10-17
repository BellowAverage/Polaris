
--- 
title:  PowerShell切换多个java版本 
tags: []
categories: [] 

---
### 安装jdk1.8 和 jdk17

>  
 下载jdk 前往 oracle官网下载 


### 配置环境变量

**变量名**

```
CLASSPATH

```

**变量值**

```
.;%JAVA_HOME%\lib;%JAVA_HOME%\lib\tools.jar

```

**效果图：** <img src="https://img-blog.csdnimg.cn/bcbd86a43936428782b40d2973defbc1.png" alt="在这里插入图片描述">

**变量名（jdk1.8同理）**

```
JAVA_HOME17

```

**变量值**

```
C:\Program Files\Java\jdk-17

```

**效果图：** <img src="https://img-blog.csdnimg.cn/82c26ad6c2d64eab838f9fd48feb9009.png" alt="在这里插入图片描述">

```
Path

```

**变量值**

```
%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

```

**效果图：** <img src="https://img-blog.csdnimg.cn/56dcd5b4fa944ff687a2549819081b28.png" alt="在这里插入图片描述">

### 使用vscode编辑powershell profile

```
code $PROFILE

```

>  
 没有$PROFILE的自己新建一个，在~\Documents\PowerShell\下新建一个文件Microsoft.PowerShell_profile.ps1 //然后在Microsoft.PowerShell_profile.ps1中新增以下内容 


```
#旧的方式使用%%引用变量可能会不生效，因此更改成下面那种
#function Java8{<!-- -->
#    [System.Environment]::SetEnvironmentVariable('JAVA_HOME','%JAVA_HOME8%','Machine')
#}

#function Java17{<!-- -->
#    [System.Environment]::SetEnvironmentVariable('JAVA_HOME','%JAVA_HOME17%','Machine')
#}
function Java8{<!-- -->
    $JAVA_HOME8 = [System.Environment]::GetEnvironmentVariable('JAVA_HOME8','Machine')
    Write-Host $JAVA_HOME8
    [System.Environment]::SetEnvironmentVariable('JAVA_HOME',$JAVA_HOME8,'Machine')
}

function Java17{<!-- -->
    $JAVA_HOME17 = [System.Environment]::GetEnvironmentVariable('JAVA_HOME17','Machine')
    Write-Host $JAVA_HOME17
    [System.Environment]::SetEnvironmentVariable('JAVA_HOME',$JAVA_HOME17,'Machine')
}

Set-Alias jvm8 JAVA8
Set-Alias jvm17 JAVA17

```

**保存后重启powershell**

**然后就可以通过在powershell中运行jvm8 和 jvm17来切换 java jdk的版本**
