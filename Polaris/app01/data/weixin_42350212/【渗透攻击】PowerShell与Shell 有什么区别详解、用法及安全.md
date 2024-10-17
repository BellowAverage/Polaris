
--- 
title:  【渗透攻击】PowerShell与Shell 有什么区别详解、用法及安全 
tags: []
categories: [] 

---
**目录**



























 

## PowerShell

###  执行策略

>  
 PowerShell 提供了 Restricted、AllSigned、RemoteSigned、Unrestricted、Bypass、Undefined 六种类型的执行策略。 


>  
 Restricted 策略可以执行单个的命令，但是不能执行脚本，Windows 8、 Windows Server 2012中默认使用该策略。 


>  
 AllSigned 策略允许执行所有具有数字签名的脚本。 
 RemoteSigned 当执行从网络上下载的脚本时，需要脚本具有数字签名，否则不会运行这个脚本。如果是在本地创建的脚本则可以直接执行，不要求脚本具有数字签名。 


>  
 Unrestricted 这是一种比较宽容的策略，允许运行未签名的脚本。对于从网络上下载的脚本，在运行前会进行安全性提示。 
 BypassBypass 执行策略对脚本的执行不设任何的限制，任何脚本都可以执行，并且不会有安全性提示。 
 UndefinedUndefined 表示没有设置脚本策略，会继承或使用默认的脚本策略。 


###  混淆
- `-EC`- `-EncodedCommand`- `-EncodedComman`- `-EncodedComma`- `-EncodedComm`
###  常见功能

####  计划任务

```
$Action = New-ScheduledTaskAction -Execute "calc.exe"
$Trigger = New-ScheduledTaskTrigger -AtLogon
$User = New-ScheduledTaskPrincipal -GroupId "BUILTIN\Administrators" -RunLevel Highest
$Set = New-ScheduledTaskSettingsSet
$object = New-ScheduledTask -Action $Action -Principal $User -Trigger $Trigger -Settings $Set
Register-ScheduledTask AtomicTask -InputObject $object
Unregister-ScheduledTask -TaskName "AtomicTask" -confirm:$false
```

####  创建链接

```
$Shell = New-Object -ComObject ("WScript.Shell")
$ShortCut = $Shell.CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\test.lnk")
$ShortCut.TargetPath="cmd.exe"
$ShortCut.WorkingDirectory = "C:\Windows\System32";
$ShortCut.WindowStyle = 1;
$ShortCut.Description = "test.";
$ShortCut.Save()
```

####  编码

```
$OriginalCommand = '#{powershell_command}'
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($OriginalCommand)
$EncodedCommand =[Convert]::ToBase64String($Bytes)
```

####  其他
<li> 别名 
  <ul>- `alias`
下载文件
- `Invoke-WebRequest "https://example.com/test.zip" -OutFile "$env:TEMP\test.zip"`
解压缩
- `Expand-Archive $env:TEMP\test.zip $env:TEMP\test -Force`
进程

>  
   - 启动进程 `Start-Process calc`- 停止进程 `Stop-Process -ID $pid` 
  

文件

>  
   - 新建文件 `New-Item #{file_path} -Force | Out-Null`- 设置文件内容 `Set-Content -Path #{file_path} -Value "#{Content}"`- 追加文件内容 `Add-Content -Path #{file_path} -Value "#{Content}"`- 复制文件 `Copy-Item src dst`- 删除文件 `Remove-Item #{outputfile} -Force -ErrorAction Ignore`- 子目录 `Get-ChildItem #{file_path}` 
  

服务

>  
   - 获取服务 `Get-Service -Name "#{service_name}"`- 启动服务 `Start-Service -Name "#{service_name}"`- 停止服务 `Stop-Service -Name "#{service_name}"`- 删除服务 `Remove-Service -Name "#{service_name}"` 
  

###  参考链接
- 
 -------------------------------------------------------------------

##  Shell

###  简介

Shell 是一个特殊的程序，是用户使用 Linux 的桥梁。Shell 既是一种命令，又是一种程序设计语言。

Linux 包含多种 Shell ，常见的有：

>  
 - Bourne Shell（ATT的Bourne开发，名为sh）- Bourne Again Shell（/bin/bash）- C Shell（Bill Joy开发，名为csh）- K Shell（ATT的David G.koun开发，名为ksh）- Z Shell（Paul Falstad开发，名为zsh） 


###  元字符

shell一般会有一系列特殊字符，用来实现的一定的效果，这种字符被称为元字符（Meta），不同的Shell支持的元字符可能会不相同。

常见的元字符如下：

>  
 - `IFS` 由 &lt;space&gt; 或 &lt;tab&gt; 或 &lt;enter&gt; 三者之一组成- `CR` 由 &lt;enter&gt; 产生。- `=` 设定变量- `$` 作变量或运算替换- `&gt;` 重定向 stdout- `&gt;&gt;` 追加到文件- `&lt;` 重定向 stdin- `|` 命令管道- `&amp;` 后台执行命令- `;` 在前一个命令结束后，执行下一个命令- `&amp;&amp;` 在前一个命令未报错执行后，执行下一个命令- `||` 在前一个命令执行报错后，执行下一个命令- `'` 在单引号内的命令会保留原来的值- `"` 在双引号内的命令会允许变量替换- ``` 在反引号内的内容会当成命令执行并替换- `()` 在子Shell中执行命令- `{}` 在当前Shell中执行命令- `~` 当前用户的主目录- `!number` 执行历史命令，如 `!1` 


###  通配符

除元字符外，通配符（wildcard）也是shell中的一种特殊字符。当shell在参数中遇到了通配符时，shell会将其当作路径或文件名去在磁盘上搜寻可能的匹配：若符合要求的匹配存在，则进行替换，否则就将该通配符作为一个普通字符直接传递。

常见的通配符如下：

>  
 - `*` 匹配 0 或多个字符- `?` 匹配任意一个字符- `[list]` 匹配 list 中的任意一个字符- `[!list]` 匹配除 list 外的任意一个字符- `[a-c]` 匹配 a-c 中的任意一个字符- `{string1,string2,...}` 分别匹配其中字符串 


###  推荐阅读

**优质资源**
- **Java实现照片GPS定位【完整脚本】**- - **Python实现照片GPS定位【完整脚本】**- - **女神忘记相册密码 python20行代码打开【完整脚本】**- - **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- 
**python实战**
- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>...</strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>- **<strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong>**<strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong>