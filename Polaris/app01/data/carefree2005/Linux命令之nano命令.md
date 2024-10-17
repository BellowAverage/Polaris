
--- 
title:  Linux命令之nano命令 
tags: []
categories: [] 

---
## 一、nano命令简介

  nano是一个小型、免费、友好的编辑器，旨在取代非免费Pine包中的默认编辑器Pico。nano不仅复制了Pico的外观，还实现了Pico中一些缺失（或默认禁用）的功能，例如“搜索和替换”和“转到行号和列号”。nano是一个字符终端的文本编辑器，有点像DOS下的editor程序。它比vi/vim要简单得多，比较适合Linux初学者使用。某些Linux发行版的默认编辑器就是nano，比如Ubuntu系统默认安装了nano。

## 二、nano命令使用示例

### 1、命令安装

>  
 [root@s142 ~]# yum install -y nano 


### 2、查看命令版本

>  
 [root@s142 ~]# nano -V GNU nano version 2.3.1 (compiled 04:47:52, Jun 10 2014) 


### 3、获取命令帮助

>  
 [root@s142 ~]# nano --help 


### 4、编辑一个文件

>  
 [wuhs@s142 ~]$ nano hi.txt <img src="https://img-blog.csdnimg.cn/4776c68e6db3425f84170cc0334a77c6.png" alt="在这里插入图片描述"> 


### 5、不自动换行编辑

  nano命令可以打开指定文件进行编辑，默认情况下它会自动断行，即在一行中输入过长的内容时自动拆分成几行，但用这种方式来处理某些文件可能会带来问题，比如Linux系统的/etc/fstab文件，所以非必要情况下建议不使用自动换行功能，使用-w开启编辑模式。 <img src="https://img-blog.csdnimg.cn/75a6b629279a49fc933a95392d430fb2.png" alt="在这里插入图片描述">

>  
 [wuhs@s142 ~]$ nano -w hi.txt 


### 6、搜索字符串

  如果我们想从打开的文件中搜索字符串，输入Ctl+W开启搜索框，输入字符串后回车，光标自动定位到搜索到的第一个结果。 <img src="https://img-blog.csdnimg.cn/d63a6f70357f4f869c31317aec1fe8bc.png" alt="在这里插入图片描述">

### 7、往编辑文件中插入1个文件

  nano支持往编辑的文件中插入一个文件，使用Ctl+R，输入框中输入文件的路径及文件名，默认是当前路径。 <img src="https://img-blog.csdnimg.cn/cb56975cab434c848ec02b4a96b499bf.png" alt="在这里插入图片描述">

### 8、其他快捷键

  nano编辑器的快捷键都是Ctl或者Alt一起组合键，如下是常用的快捷键，如果需要了解更多可以通过Ctl+G获取快捷键的帮助。

<th align="left">快捷键</th><th align="left">用途</th>
|------
<td align="left">Ctl+K</td><td align="left">剪切一行</td>
<td align="left">Alt+6</td><td align="left">复制一行</td>
<td align="left">Ctl+U</td><td align="left">黏贴一行</td>
<td align="left">Ctl+Y</td><td align="left">向前翻一页</td>
<td align="left">Ctl+V</td><td align="left">向后翻一页</td>
<td align="left">Ctl+O</td><td align="left">保存更新</td>
<td align="left">Ctl+X</td><td align="left">退出编辑模式</td>
<td align="left">Ctl+6</td><td align="left">开始标记，移动光标，再按一次结束标记，期间可以与剪切、复制等快捷键结合使用</td>
<td align="left">Ctl+R</td><td align="left">插入一个文件</td>
<td align="left">Ctl+G</td><td align="left">获取使用帮助</td>
<td align="left">Ctl+P</td><td align="left">光标上移一行</td>
<td align="left">Ctl+N</td><td align="left">光标下移一行</td>

## 三、nano命令语法及参数说明

### 1、命令语法

>  
 #nano [OPTIONS] [[+LINE,COLUMN] FILE]… #nano [选项] [[+行,列] 文件名]… 


### 2、参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-h, -? , --help</td><td align="left">显示帮助信息</td>
<td align="left">+行,列</td><td align="left">从所指列数与行数开始</td>
<td align="left">-A , --smarthome</td><td align="left">启用智能 HOME 键</td>
<td align="left">-B , --backup</td><td align="left">储存既有文件的备份</td>
<td align="left">-C &lt;目录&gt; , --backupdir=&lt;目录&gt;</td><td align="left">用以储存独一备份文件的目录</td>
<td align="left">-D , --boldtext</td><td align="left">用粗体替代颜色反转</td>
<td align="left">-E , --tabstospaces</td><td align="left">将已输入的制表符转换为空白</td>
<td align="left">-F , --multibuffer</td><td align="left">启用多重文件缓冲区功能</td>
<td align="left">-H , --historylog</td><td align="left">记录与读取搜索/替换的历史字符串</td>
<td align="left">-I , --ignorercfiles</td><td align="left">不要参考nanorc 文件</td>
<td align="left">-K , --rebindkeypad</td><td align="left">修正数字键区按键混淆问题</td>
<td align="left">-L , --nonewlines</td><td align="left">不要将换行加到文件末端</td>
<td align="left">-N , --noconvert</td><td align="left">不要从 DOS/Mac 格式转换</td>
<td align="left">-O , --morespace</td><td align="left">编辑时多使用一行</td>
<td align="left">-Q &lt;字符串&gt; , --quotestr=&lt;字符串&gt;</td><td align="left">引用代表字符串</td>
<td align="left">-R , --restricted</td><td align="left">限制模式</td>
<td align="left">-S , --smooth</td><td align="left">按行滚动而不是半屏</td>
<td align="left">-T &lt;#列数&gt; , --tabsize=&lt;#列数&gt;</td><td align="left">设定制表符宽度为 #列数</td>
<td align="left">-U , --quickblank</td><td align="left">状态行快速闪动</td>
<td align="left">-V , --version</td><td align="left">显示版本资讯并离开</td>
<td align="left">-W , --wordbounds</td><td align="left">更正确地侦测单字边界</td>
<td align="left">-Y &lt;字符串&gt; , --syntax=&lt;字符串&gt;</td><td align="left">用于加亮的语法定义</td>
<td align="left">-c , --const</td><td align="left">持续显示游标位置</td>
<td align="left">-d , --rebinddelete</td><td align="left">修正退格键/删除键混淆问题</td>
<td align="left">-i , --autoindent</td><td align="left">自动缩进新行</td>
<td align="left">-k , --cut</td><td align="left">从游标剪切至行尾</td>
<td align="left">-l , --nofollow</td><td align="left">不要依照符号连结，而是覆盖</td>
<td align="left">-m , --mouse</td><td align="left">启用鼠标功能</td>
<td align="left">-o &lt;目录&gt; , --operatingdir=&lt;目录&gt;</td><td align="left">设定操作目录</td>
<td align="left">-p , --preserve</td><td align="left">保留XON (^Q) 和XOFF (^S) 按键</td>
<td align="left">-q , --quiet</td><td align="left">沉默忽略启动问题, 比如rc 文件错误</td>
<td align="left">-r &lt;#列数&gt; , --fill=&lt;#列数&gt;</td><td align="left">设定折行宽度为 #列数</td>
<td align="left">-s &lt;程序&gt; , --speller=&lt;程序&gt;</td><td align="left">启用替代的拼写检查程序</td>
<td align="left">-t , --tempfile</td><td align="left">离开时自动储存，不要提示</td>
<td align="left">-u , --undo</td><td align="left">允许通用撤销[试验性特性]</td>
<td align="left">-v , --view</td><td align="left">查看(只读)模式</td>
<td align="left">-w , --nowrap</td><td align="left">不要自动换行</td>
<td align="left">-x , --nohelp</td><td align="left">不要显示辅助区</td>
<td align="left">-z , --suspend</td><td align="left">启用暂停功能</td>
<td align="left">-$ , --softwrap</td><td align="left">启用软换行</td>
