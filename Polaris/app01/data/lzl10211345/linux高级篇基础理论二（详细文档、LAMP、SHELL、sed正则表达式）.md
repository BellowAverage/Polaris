
--- 
title:  linux高级篇基础理论二（详细文档、LAMP、SHELL、sed正则表达式） 
tags: []
categories: [] 

---
>  
 ♥️**作者：小刘在C站** 
 ♥️**个人主页：<strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong><strong>**</strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong></strong> 
 ♥️**不能因为人生的道路坎坷,就使自己的身躯变得弯曲;不能因为生活的历程漫长,就使求索的  脚步迟缓。** 
 ♥️**学习两年总结出的运维经验，以及思科模拟器全套网络实验教程。专栏：** 
 ♥️**感谢CSDN让你我相遇！** 


运维人员辛苦和汗水总结的干货理论希望对你有所帮助

<img alt="" class="right" height="80" src="https://img-blog.csdnimg.cn/fd3fee85df1d4cffba97164ba01cdf81.gif" width="640">

**目录**















































































### LAMP

1、LAMP的作用： 一种企业网站应用模式，可提供动态web网站

2、LAMP构成组件 linux、Apache、MySQL、PHP/perl/python 安装顺序：先L再A和M，最后P

3、LAMP的优势 成本低廉 可定制、易于开发 方便易用、安全和稳定

4、phpmyadmin系统的作用：用来管理MySQL数据库的web应用系统(图形界面)

shell（重点）

#### 1、执行脚本的方法：

方法一：直接执行脚本文件（必须为决对路径需要x权限）     ./脚本文件    或    /路径/脚本文件 方法二：sh    /路径/脚本文件 方法三：source    /路径/脚本文件     备注：source也可以用 . 来代替

#### 2、完善的脚本构成：

脚本声明

<img alt="" height="294" src="https://img-blog.csdnimg.cn/3b5affc44ee14db89ec6301afbef4641.png" width="1200"> 注释信息 可执行语句

#### 3、重定向

输入重定向：  &lt; 输出重定向（正确）：  &gt;   覆盖   &gt;&gt;  追加 错误输出重定向： 2&gt;     覆盖 2&gt;&gt;  追加 混合输出（错误和正确）：&amp;&gt;

#### 4、管道符：  |

将上一个命令的输出当做下一个命令的输入

#### 5、awk 命令 ：

在一行中提取需要的字段。 例：awk   -F :  '{print $1,$7}'

grep : 在一个文件中过滤出符合条件的行。

#### 6.变量的类型

自定义变量：由用户自己定义、修改和使用 环境变量：由系统维护，用于设置工作环境 位置变量：通过命令给脚本程序传递参数 预定义变量：Bash中内置的一类变量，不能直接修改

#### 7.自定义变量

变量名=变量值 查看变量的值：  echo   $变量名

#### 8、给变量赋值时使用的引号：

双引号：允许通过$符号引用其他变量值(“”) 单引号：禁止引用其他变量值，$视为普通字符（‘’） 反撇号：命令替换，提取命令执行后的输出结果（``）,可以用$代替。 $()   //命令替换，直接在括号中输入命令

#### 9、从键盘输入内容给变量赋值：

read -p "提示信息" 变量名

#### 10、设置作用范围：（输入为全局变量）

方法一：export  变量名          //无$开头 方法二：export  变量名=变量值67

#### 11、整数变量的运算

expr   变量1     运算符     变量2      常用运算符：     加法运算：+     减法运算：-     乘法运算：\*     除法运算：/     求模（取余）运算：%

#### 12、环境变量：

查看环境变量（全局变量）：env 常见的环境变量：     PWD:保存了当前工作路径     PATH：保存了命令搜索的路径     USER：保存了当前登录的用户     SHELL：保存了当前登录的shell     HOME：保存了当前登录用户的宿主目录

#### 13、位置变量

$1$2....$9，总共9个位置变量

#### 14、预定义变量

$#:命令行中位置变量的个数 $*:所有位置变量的内容 $@:所有位置变量分别单独的区分 $?:上一条命令执行后返回的状态，当返回状态值为0时表示执行正常，非0值表示执行异常或出错 $0:当前执行的进程/程序名

### shell测试选项（重点）

#### 1、条件测试操作的方法

语法一：test  条件表达式 语法二：[ 条件表达式 ]  //前后有空格

#### 2、文件测试

[ 操作符   文件或目录 ] 操作符： -d :是否为目录 -e :目录或文件是否存在 -f :是否为文件 -r :当前用户是否有读取权限 -w :当前用户是否有写入权限 -x :当前用户是否有执行权限

#### 3、整数值比较

[ 整数1   操作符   整数2 ] 操作符： -eq : 等于 -ne : 不等于 -gt : 大于 -ge : 大于或等于 -lt : 小于 -le : 小于或等于

#### 4、字符串比较

= ：字符串内容相同 ！：字符串内容不同、！号表示相反的意思 -z：字符串内容为空

#### 5、逻辑测试：

方法一：[ 表达式1 ] 操作符  [ 表达式2 ] 方法二：命令1   操作符   命令2 操作符： &amp;&amp;：逻辑与，“而且”的意思 ||：逻辑或：“或者”的意思 ！：逻辑否

### 编程四大语句（重点）

#### 1、if语句的结构（条件判断语句）

##### （1）单分支

 if   条件测试      then     命令序列 fi

###### （2）双分支

if   条件测试      then     命令序列      else     命令序列 fi

###### （3）多分支

if  条件测试1      then     命令序列1 elif  条件测试2      then     命令序列 else         命令序列 fi

####  2、for循环语句的结构：

 for  变量名  in   取值列表 do     命令序列 done

#### 3、while循环语句的结构：

while  条件测试 do 命令序列 done

#### 4、case语句结构：（用于多分支）

case  变量值  in 模式1）     命令序列1     ；； 模式2）     命令序列2     ；； ... *) 默认命令序列 esac

##### for和while的区别

for：控制循环来自于取值列表。 while：控制循环来自于条件测试。

### 正则表达式（重点）

#### 1、正则表达式定义：

是使用单个字符来描述、匹配一系列符合某个语法规则的字符串

#### 2、正则表达式组成

（1）普通字符 大小写字母、数字、标点符号及一些其他符合 （2）元字符 在正则表达式中具有特殊意义的专用字符

#### 3、正则表达式的类型：

（1）基础正则：grep （2）扩展正则：egrep

#### 4、元字符的总结

^：已…开头 $：已…结尾 . ：匹配任意单个字符 *：重复前面的字符 \：转义字符 [ ]：在中括号中的任意一个 [^ ]：除了中括号中的任意一个 {数字 }：连续重复的字符

#### 5、sed命令的作用

对文本内容进行编辑（删除，替换，添加，移动等）

#### 6、sed的用法：

sed    选项      ‘操作’     /路径/文件名 选项： -e  :用指定命令或脚本来处理输入的文本文件。 -i   :直接编辑文本文件 -n  :仅显示处理后的结构 操作： a   :增加，在当前行下面增加一行指定的内容。 c   :替换，将选定的行替换为指定内容。 d   :删除，删除选定的行 p   :打印，屏幕显示结果 s    :替换，替换指定字符

>  
 人生要尽全力度过每一关,不管遇到什么困难不可轻言放弃！！！ 

