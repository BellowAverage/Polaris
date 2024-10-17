
--- 
title:  Linux安全之auditd审计工具使用说明 
tags: []
categories: [] 

---
## 一、auditd工具简介

  audited是Linux审核系统的用户空间组件。它负责将审核记录写入磁盘。查看日志是通过ausearch或aureport实用程序完成的。审核系统或加载规则的配置是使用auditctl实用程序完成的。在启动过程中，/etc/audit/audit.rules中的规则由auditctl读取并加载到内核中。另外，还有一个augenrules程序，它读取/etc/audit/rules.d/中的规则，并将它们编译为audit.rules文件。审核守护进程本身有一些管理员可能希望自定义的配置选项，它们位于audited.conf文件中。

## 二、auditd配置文件说明

### 1、配置文件关键字说明

<th align="left">关键字</th><th align="left">关键字说明</th>
|------
<td align="left">num_days</td><td align="left">日志保留的天数</td>
<td align="left">idletime</td><td align="left">空闲时间</td>
<td align="left">max_log_file</td><td align="left">这个关键字指定了以兆字节为单位的最大文件大小。当达到这个限制时，它将触发一个可配置的操作。给定的值必须是数值。</td>
<td align="left">max_log_file_action</td><td align="left">此参数告诉系统当系统检测到已达到最大文件大小限制时采取什么操作。有效值为ignore、syslog、suspend、rotate和keep_logs。如果设置为ignore，审计守护进程什么都不做。Syslog表示它将向Syslog发出警告。Suspend将导致审计守护进程停止向磁盘写入记录。守护进程还会活着。rotate选项将导致审计守护进程旋转日志。需要注意的是，数值大的日志比数值小的日志要早。这与logrotate实用程序使用的约定相同。keep_logs选项类似于rotate，只是它不使用num_logs设置。这可以防止审计日志被覆盖。</td>
<td align="left">space_left</td><td align="left">这是一个以兆字节为单位的数值，它告诉审计守护进程何时执行可配置的操作，因为系统的磁盘空间开始不足。</td>
<td align="left">space_left_action</td><td align="left">这个参数告诉系统，当系统检测到磁盘空间开始变少时，应该采取什么行动。有效值为:ignore、syslog、email、exec、suspend、single和halt。如果设置为ignore，审计守护进程什么都不做。Syslog表示它将向Syslog发出警告。Email意味着它将向action_mail_acct中指定的电子邮件帐户发送警告，同时将消息发送到syslog。Exec /path-to-script将执行脚本。您不能将参数传递给脚本。Suspend将导致审计守护进程停止向磁盘写入记录。守护进程还会活着。single选项将导致审计守护进程将计算机系统置于单用户模式。Halt选项将导致审计守护进程关闭计算机系统。</td>
<td align="left">local_events</td><td align="left">本地的事件是否记录，设置为no的场景应该是只作为远程日志收集的服务器，但自身的日志大多数时候也是有必要记录的</td>
<td align="left">write_logs</td><td align="left">日志是否落盘，设置为no的场景应该是将会把日志存储到远程服务器的客户端(没有足够空间的情况下)</td>
<td align="left">log_file</td><td align="left">此关键字指定存储审计记录的日志文件的完整路径名。它必须是一个普通文件。</td>
<td align="left">log_format</td><td align="left">日志格式描述了信息应该如何存储在磁盘上。有两个选项:raw和nolog。如果设置为RAW，审计记录将按照内核发送的格式存储。如果该选项设置为NOLOG，那么所有审计信息将被丢弃，而不会写入磁盘。该模式不影响发送到审计事件分配器的数据。</td>
<td align="left">log_group</td><td align="left">此关键字指定应用于日志文件权限的组。默认为root。组名可以是数字，也可以拼写出来。</td>
<td align="left">priority_boost</td><td align="left">这是一个非负数，告诉审计守护进程应该提高多少优先级。默认值为4。没有变化是0。</td>
<td align="left">flush</td><td align="left">有效值为none、incremental、data和sync。如果设置为none，则不会进行特殊操作将审计记录刷新到磁盘。如果设置为增量，那么freq参数用于确定显式刷写磁盘的频率。data参数告诉审计守护进程始终保持磁盘文件的数据部分同步。sync选项告诉审计守护进程在每次写入磁盘时保持数据和元数据完全同步。</td>
<td align="left">freq</td><td align="left">这是一个非负数，告诉审计守护进程在发出显式刷写到磁盘命令之前要写入多少条记录。只有将flush关键字设置为incremental时，这个值才有效。</td>
<td align="left">num_logs</td><td align="left">如果rotate指定了max_log_file_action，则该关键字指定了保留的日志文件数。如果数字是&lt;2、日志不旋转。这个数字必须小于等于99。默认值为0，表示没有旋转。随着要旋转的日志文件数量的增加，可能需要向上调整内核积压工作表的设置，因为旋转文件需要更多的时间。这通常在/etc/audit/audit.rules中完成。如果配置日志轮换，守护进程将检查多余的日志并删除它们，以保持磁盘空间可用。只有在启动和重新配置导致空间检查时，才会进行多余的日志检查。</td>
<td align="left">disp_qos</td><td align="left">此选项控制您想要在审计守护进程和调度程序之间进行阻塞/无损通信还是非阻塞/有损通信。在审计守护进程和分配器之间有一个128k的缓冲区。对于大多数应用来说，这已经足够了。如果选择了lossy，那么当队列满时，进入分派器的事件将被丢弃。(如果log_format不是nlog，事件仍然写入磁盘。)否则，auditd守护进程将等待队列有一个空位，然后将日志记录到磁盘。风险在于，当守护进程等待网络IO时，事件不会被记录到磁盘上。有效值有:lossy和lossless。默认值为Lossy。</td>
<td align="left">dispatcher</td><td align="left">dispatcher是一个由审计守护进程在启动时启动的程序。它将把所有审计事件的副本传递给应用程序的stdin。请确保您信任添加到这一行的应用程序，因为它以root权限运行。</td>
<td align="left">name_format</td><td align="left">该选项控制计算机节点名如何插入到审计事件流中。它有以下选项:none、hostname、fqd、numeric和user。None表示没有向审计事件插入计算机名。Hostname是gethostname系统调用返回的名称。fqd意味着它接收主机名并通过dns解析为该机器的完全限定域名。Numeric类似于fqd，只是它可以解析机器的IP地址。为了使用这个选项，你可能想测试`hostname -i`或`domainname -i`是否返回一个数字地址。此外，如果使用dhcp，则不建议使用此选项，因为随着时间的推移，同一台机器可能有不同的地址。User是一个从name选项中定义的管理员字符串。默认值为none。</td>
<td align="left">name</td><td align="left">这是管理员定义的字符串，如果user被指定为name_format选项，它将标识该机器。</td>
<td align="left">action_mail_acct</td><td align="left">此选项应包含有效的电子邮件地址或别名。默认地址为root。如果电子邮件地址不是本机的，你必须确保在你的机器和网络上正确配置了电子邮件。此外，该选项要求计算机上存在/usr/lib/sendmail。</td>
<td align="left">admin_space_left</td><td align="left">这是一个以兆字节为单位的数值，它告诉审计守护进程何时执行可配置的操作，因为系统磁盘空间不足。这应该被视为耗尽磁盘空间之前执行某些操作的最后机会。该参数的数值应该小于space_left的数值。</td>
<td align="left">admin_space_left_action</td><td align="left">此参数告诉系统当系统检测到磁盘空间不足时采取什么操作。有效值为:ignore、syslog、email、exec、suspend、single和halt。如果设置为ignore，审计守护进程什么都不做。Syslog表示它将向Syslog发出警告。Email意味着它将向action_mail_acct中指定的电子邮件帐户发送警告，同时将消息发送到syslog。Exec /path-to-script将执行脚本。您不能将参数传递给脚本。Suspend将导致审计守护进程停止向磁盘写入记录。守护进程还会活着。single选项将导致审计守护进程将计算机系统置于单用户模式。停止</td>
<td align="left">disk_full_action</td><td align="left">这个参数告诉系统，当系统检测到日志文件写入的分区已满时，应该采取什么行动。有效值为ignore、syslog、exec、suspend、single和halt。如果设置为ignore，审计守护进程将发出syslog消息，但不采取其他操作。Syslog表示它将向Syslog发出警告。Exec /path-to-script将执行脚本。您不能将参数传递给脚本。Suspend将导致审计守护进程停止向磁盘写入记录。守护进程还会活着。single选项将导致审计守护进程将计算机系统置于单用户模式。Halt选项将导致审计守护进程关闭计算机系统。</td>
<td align="left">disk_error_action</td><td align="left">这个参数告诉系统，在将审计事件写入磁盘或循环日志时，如果检测到错误，应该采取什么操作。有效值为ignore、syslog、exec、suspend、single和halt。如果设置为ignore，审计守护进程将不执行任何操作。Syslog表示对Syslog连续发出的警告不超过5次。Exec /path-to-script将执行脚本。您不能将参数传递给脚本。Suspend将导致审计守护进程停止向磁盘写入记录。守护进程还会活着。single选项将导致审计守护进程将计算机系统置于单用户模式。Halt选项将导致审计守护进程关闭计算机系统。</td>
<td align="left">tcp_listen_port</td><td align="left">这是一个范围为1的数值。65535，如果指定，将导致auditd在对应的TCP端口上监听来自远程系统的审计记录。审计守护进程可以链接到tcp_wrapper。您可能希望通过主机中的一个条目来控制访问。允许和拒绝文件。</td>
<td align="left">tcp_listen_queue</td><td align="left">这是一个数值，表示允许的挂起(请求但未接受的)连接数。默认值为5。如果在同一时间启动的主机太多，例如停电后，这个值设置得太小可能会导致连接被拒绝。</td>
<td align="left">tcp_max_per_addr</td><td align="left">这是一个数值，表示一个IP地址允许的并发连接数。默认值为1，最大1024。设置得太大可能导致对日志服务器的拒绝服务攻击。还要注意，内核有一个内部的最大值，即使auditd通过config允许这样做，最终也会阻止该操作。默认值在大多数情况下应该足够了，除非运行自定义编写的恢复脚本来转发未发送的事件。在这种情况下，你只需要增加足够大的数字就可以让它进来。</td>
<td align="left">use_libwrap</td><td align="left">该设置确定是否使用tcp_wrapper来识别来自允许的计算机的连接尝试。合法的取值包括“yes”和“no”。默认值为“yes”。</td>
<td align="left">tcp_client_ports</td><td align="left">这个参数可以是一个数值，也可以是两个由破折号分隔的值(不允许有空格)。它表明客户端端口允许传入的连接。如果没有指定，则允许任何端口。允许取值为1 ~ 65535。例如，要要求客户端使用特权端口，请将此参数指定为1-1023。你还需要在audio -remote.conf文件中设置local_port选项。确保客户发送从特权端口安全功能,以防止不可信用户日志注入攻击。</td>
<td align="left">tcp_client_max_idle</td><td align="left">该参数表示在auditd发出报警之前，客户端可能空闲的秒数(即根本没有数据)。如果客户端机器出现问题，无法干净地关闭连接，则用于关闭非活动连接。注意，这是一个全局设置，必须比任何单独的客户端heartbeat_timeout设置高，最好是2倍。默认为零,禁用此检查。</td>
<td align="left">enable_krb5</td><td align="left">如果设置为“yes”，Kerberos 5将用于身份验证和加密。默认值为no。</td>
<td align="left">krb5_principal</td><td align="left">这是此服务器的主体。默认值是auditd。有了这个默认值，服务器将查找存储在/etc/audit/audit.中名为auditd/hostname@EXAMPLE.COM的键key进行身份验证，其中hostname是服务器主机的规范名称，通过DNS查找其IP地址返回。</td>
<td align="left">krb5_key_file</td><td align="left">此客户端主体的密钥位置。注意，密钥文件必须为root用户所有，模式为0400。默认的是/etc/audit/audit.key</td>

### 2、默认配置释义

>  
 [root@s166 audit]# cat /etc/audit/auditd.conf # # This file controls the configuration of the audit daemon # #记录本地事件 local_events = yes #日志落盘存储 write_logs = yes #审计日志存储路径 log_file = /var/log/audit/audit.log #日志文件属组 log_group = root #日志文件格式 log_format = RAW #异步增量方式刷新到磁盘 flush = INCREMENTAL_ASYNC #记录数量达到此数值时写入磁盘，与flush结合使用 freq = 50 #单个日志文件大小，单位为M，超过8M进行日志分割 max_log_file = 8 #日志文件保存数量，超过的会被清除 num_logs = 5 #守护进程优先级 priority_boost = 4 #队列满是，丢弃事件记录 disp_qos = lossy #守护进程启动的程序 dispatcher = /sbin/audispd #审计事件不插入主机名 name_format = NONE #管理员可以指定主机名，默认注释，未启用 ##name = mydomain #日志文件超过大小时的动作，ROTATE表示将日志轮转分割 max_log_file_action = ROTATE #系统磁盘空间剩余大小时执行动作，但是为M space_left = 75 #系统磁盘空间不足时执行的操作，发送SYSLOG告警 space_left_action = SYSLOG #是否发送邮件，取值yes或者no verify_email = yes #发送邮箱的账户，默认root@localhost,如果配置的是网络邮箱，/usr/lib/sendmail确保正确配置 action_mail_acct = root #磁盘空间剩余大小，剩余不足50M时停止审计记录写入 admin_space_left = 50 admin_space_left_action = SUSPEND #磁盘满或者磁盘错误的时候停止写入审计记录 disk_full_action = SUSPEND disk_error_action = SUSPEND #如下是审计客户端连接相关参数 use_libwrap = yes ##tcp_listen_port = 60 tcp_listen_queue = 5 tcp_max_per_addr = 1 ##tcp_client_ports = 1024-65535 tcp_client_max_idle = 0 enable_krb5 = no krb5_principal = auditd ##krb5_key_file = /etc/audit/audit.key distribute_network = no 


## 三、auditd相关命令与配置文件

### 1、auditd相关命令
- **auditctl :** 即时控制审计守护进程的行为的工具，如添加规则等。- **auditd ：**audit 守护进程负责把内核产生的信息写入到硬盘上，这些信息由应用程序和系统活动触发产生。用户空间审计系统通过 auditd 后台进程接收内核审计系统传送来的审计信息，将信息写入到 /var/log/audit/audit.log。- aureport : 查看和生成审计报告的工具。- **ausearch :** 查找审计事件的工具- **auditspd :** 转发事件通知给其他应用程序，而不是写入到审计日志文件中。- **autrace :** 一个用于跟踪进程的命令。类似于 strace，跟踪某一个进程，并将跟踪的结果写入日志文件之中。- **aulast:** 与last类似，但使用审计框架安装- **aulastlog:** 与lastlog类似，也使用审计框架- **ausyscall:** 映射syscall ID和名称- **auvirt:** 显示关于虚拟机的审计信息
### 2、auditd相关配置文件
- /etc/audit/auditd.conf : auditd工具的配置文件- /etc/audit/rules.d/audit.rules：包含审核规则的文件，如果我们需要修改审计范围，直接编辑该文件，并使用auditctl -R 命令重载审计规则配置文件- /etc/audit/audit.rules : 记录审计规则的文件，该配置文件是根据etc/audit/rules.d/audit.rules下的配置文件自动生成
## 四、auditd使用举例

### 1、查看当前审计规则

>  
 [root@s166 audit]# auditctl -l No rules 


### 2、配置一条审计规则

>  
 [root@s166 audit]# echo “-w /etc/hosts -p wa -k hosts_change” &gt;&gt; rules.d/audit.rules 


### 3、重载配置

>  
 [root@s166 audit]# auditctl -R /etc/audit/rules.d/audit.rules 


### 4、再次查看审计规则

>  
 [root@s166 audit]# auditctl -l -w /etc/hosts -p wa -k hosts_change 


### 5、修改/etc/hosts文件

>  
 [root@s166 audit]# vim /etc/hosts … 192.168.0.186 s186 


### 6、查看审计记录

>  
 [root@s166 audit]# ausearch --start today -k “hosts_change” <img src="https://img-blog.csdnimg.cn/1e7b157d51ac49018af40df0d8795580.png" alt="在这里插入图片描述"> 


## 五、auditd服务管理

  auditd服务默认开机自启动，配置了禁止手动启停服务，如果我们需要启动或者停止服务，需要修改/usr/lib/systemd/system/auditd.service中的RefuseManualStop=no，否则服务启停服务命令，修改完成后执行systemctl daemon-reload ，然后就可以手动启停管理服务了。实际上我们也可以不停止服务的情况下停止审计，只需要执行auditd -s disable命令就可以停止审计记录。
- 查看auditd服务状态：systemctl status auditd- 配置服务开机自启动：systemctl enable auditd- 取消服务开机自启动：systemctl disable auditd- 停止auditd服务：systemctl stop auditd- 启动auditd服务：systemctl start auditd- 重启auditd服务：systemctl restart auditd- 重载审计规则配置：auditctl -R /etc/audit/rules.d/audit.rules- 停止审计：auditd -s disable- 开启审计：auditd -s enable
## 六、auditctl命令简介

  audit 我们可以使用auditctl临时配置规则，服务重启失效，如果需要配置永久生效，我们需要将规则写入到配置文件中。auditd审计规则分成三个部分，
- 控制规则：这些规则用于更改审计系统本身的配置和设置。- 文件系统规则：这些是文件或目录监视。 使用这些规则，我们可以审核对特定文件或目录的任何类型的访问。- 系统调用规则：这些规则用于监视由任何进程或特定用户进行的系统调用。
### 1、命令语法

>  
 #auditctl [选项] filter,action -S syscall -F condition -k label 


### 2、命令参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-w path</td><td align="left">指定要监控的路径</td>
<td align="left">-p</td><td align="left">指定触发审计的文件/目录的访问权限rwxa，指定的触发条件，r 读取权限，w 写入权限，x 执行权限，a 属性（attr）</td>
<td align="left">-k</td><td align="left">在审核规则上设置过滤名称，方便后面使用ausearch查找</td>
<td align="left">-D</td><td align="left">删除所有规则和监控</td>
<td align="left">-W</td><td align="left">删除指定path的规则和-w对应，参数都要一样才能删除</td>
<td align="left">-b</td><td align="left">在 Kernel 中设定最大数量的已存在的审核缓冲区</td>
<td align="left">-R</td><td align="left">读取审计规则配置</td>
<td align="left">-l</td><td align="left">列表展示审计规则</td>
<td align="left">-s</td><td align="left">查看审计状态</td>
<td align="left">-v</td><td align="left">查看命令帮助</td>
<td align="left">-h</td><td align="left">获取命令帮助</td>
<td align="left">-a</td><td align="left">添加一条系统调用规则</td>
<td align="left">-d</td><td align="left">删除一条系统调用规则</td>
<td align="left">-r</td><td align="left">设置每秒生成信息的速率</td>
<td align="left">-S</td><td align="left">表示系统调用号或名字</td>
<td align="left">-F</td><td align="left">表示规则域</td>

### 3、命令选项说明

<th align="left">项目</th><th align="left">可选参数</th><th align="left">说明</th>
|------
<td align="left">filter</td><td align="left">user,exit,task,exclude filter</td><td align="left">详细说明哪个内核规则匹配过滤器应用在事件中。以下是其中之一的与规则匹配的过滤器： task、exit、user 以及 exclude</td>
<td align="left">action</td><td align="left">always, never</td><td align="left">是否审核事件（always 表示是）（never 表示否）</td>
<td align="left">syscall</td><td align="left">all, 2, open 等</td><td align="left">所有的系统调用都可以在/usr/include/asm/unistd_64.h 文件中找到。许多系统调用都能形成一个规则</td>
<td align="left">condition</td><td align="left">euid=0, arch=b64</td><td align="left">详细说明其他选项，进一步修改规则来与以特定架构、组 ID、进程 ID 和其他内容为基础的事件相匹配</td>
<td align="left">label</td><td align="left">任意文字</td><td align="left">标记审核事件并检索日志</td>

### 4、命令使用示例
- 添加一条指定路径规则
>  
 [root@s166 audit]# auditctl -w /mnt/testfile -p wa -k config-change [root@s166 audit]# auditctl -l -w /etc/hosts -p wa -k hosts_change -w /mnt/testfile -p wa -k config-change 

- 删除一条指定路径规则
>  
 [root@s166 audit]# auditctl -W /mnt/testfile -p wa -k config-change [root@s166 audit]# auditctl -l -w /etc/hosts -p wa -k hosts_change 

- 删除所有规则
>  
 [root@s166 audit]# auditctl -D No rules [root@s166 audit]# auditctl -l No rules 

- 查看规则
>  
 [root@s166 audit]# auditctl -l No rules 


## 七、ausearch命令简介

  使用 ausearch ，您可以过滤和搜索事件类型。 它还可以通过将数值转换为更加直观的值（如系统调用或用户名）来解释事件。以根用户身份执行 ausearch 命令，当显示结果时，每个记录用 4 条虚线组成的一行隔开，每个记录前均显示时间标记。

### 1、常用参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-f,–file &lt;文件名&gt;</td><td align="left">根据文件名搜索</td>
<td align="left">-c,–comm</td><td align="left">根据命令行名称搜索</td>
<td align="left">-ui,–uid</td><td align="left">&lt;用户id&gt; 根据用户id搜索</td>
<td align="left">-p,–pid</td><td align="left">&lt;进程id&gt; 根据进程id搜索</td>
<td align="left">-k,–key</td><td align="left">根据key字段搜索</td>
<td align="left">-te,–end</td><td align="left">[结束日期] [结束时间] 搜索的结束日期和时间</td>
<td align="left">-ts,–start</td><td align="left">[开始日期] [开始时间] 开始数据和搜索时间</td>
<td align="left">-m</td><td align="left">指定消息类型</td>

### 2、命令使用示例
- 查询所有事件
>  
 [root@s166 audit]# ausearch -m all 

- 查询指定时间段的日志
>  
 [root@s166 audit]# ausearch --start today --end “now” 

- 查询指定用户日志
>  
 [root@s166 audit]# ausearch -ua kingbase 

- 根据文件路径查找日志
>  
 [root@s166 audit]# ausearch -f /etc/hosts 

- 根据系统调用查询日志
>  
 [root@s166 audit]# ausearch -sc open 

- 根据过滤关键字查询日志
>  
 [root@s166 audit]# ausearch -k “hosts_change” 

- 搜索系统登录失败日志
>  
 [root@s166 audit]# ausearch --message USER_LOGIN --success no --interpret 

- 搜索所有的账户，群组，角色变更
>  
 [root@s166 audit]# ausearch -m ADD_USER -m DEL_USER -m ADD_GROUP -m USER_CHAUTHTOK -m DEL_GROUP -m CHGRP_ID -m ROLE_ASSIGN -m ROLE_REMOVE -i 

- 搜寻从制定时间段的失败的系统调用
>  
 [root@s166 audit]# ausearch --start “2023年10月22日” --end “now” -m SYSCALL -sv no -i 


## 八、aureport命令简介

  要生成审计消息的报表，可使用 aureport 命令。如果执行 aureport 时没有使用任何选项，则会显示如汇总报表。

### 1、常用参数说明

<th align="left">参数</th><th align="left">参数说明</th>
|------
<td align="left">-a、 --avc</td><td align="left">avc报告</td>
<td align="left">-au，–auth</td><td align="left">身份验证报告</td>
<td align="left">–comm</td><td align="left">命令运行报告</td>
<td align="left">-c、 --config</td><td align="left">配置更改报告</td>
<td align="left">-cr，–crypto</td><td align="left">加密报告</td>
<td align="left">-e、 --event</td><td align="left">事件报告</td>
<td align="left">-f、 --file</td><td align="left">文件名报告</td>
<td align="left">–failed</td><td align="left">报表中只有失败的事件</td>
<td align="left">-h、 --主机</td><td align="left">远程主机名报告</td>
<td align="left">–help</td><td align="left">帮助</td>
<td align="left">-i、 --interpret</td><td align="left">解释模式</td>
<td align="left">-if，–input＜input File name＞</td><td align="left">使用此文件作为输入</td>
<td align="left">–input logs</td><td align="left">即使stdin是管道，也要使用日志</td>
<td align="left">–integrity</td><td align="left">完整性事件报告</td>
<td align="left">-l、 --login</td><td align="left">登录报告</td>
<td align="left">-k、 --key</td><td align="left">密钥报告</td>
<td align="left">-m、 --mods</td><td align="left">修改帐户报告</td>
<td align="left">-ma，–mac</td><td align="left">强制访问控制（mac）报告</td>
<td align="left">-n、 --异常</td><td align="left">anomaly报告</td>
<td align="left">-nc，–no config</td><td align="left">不包括配置事件</td>
<td align="left">–node＜node name＞</td><td align="left">仅来自特定节点的事件</td>
<td align="left">-p、 --pid</td><td align="left">pid报告</td>
<td align="left">-r、 --响应</td><td align="left">对异常报告的响应</td>
<td align="left">-s、 --syscall</td><td align="left">系统调用报告</td>
<td align="left">–success</td><td align="left">报表中只有成功事件</td>
<td align="left">–summary</td><td align="left">报表中主对象的排序汇总</td>
<td align="left">-t、 --log</td><td align="left">日志时间范围报告</td>
<td align="left">-te，–end[结束日期][结束时间]</td><td align="left">报表的结束日期和时间</td>
<td align="left">-tm，–terminal</td><td align="left">terminal名称报告</td>
<td align="left">-ts，–开始[开始日期][开始</td><td align="left">时间]开始数据和报告时间</td>
<td align="left">–tty</td><td align="left">关于tty击键的报告</td>
<td align="left">-u、 --user</td><td align="left">用户名报告</td>
<td align="left">-v、 --版本</td><td align="left">版本</td>
<td align="left">–virt</td><td align="left">虚拟化报告</td>
<td align="left">-x、 --可执行文件</td><td align="left">可执行名称报告</td>

### 2、命令使用示例
- 生成所有报告
>  
 [root@s166 audit]# aureport <img src="https://img-blog.csdnimg.cn/614c33ce30854285bda11640cde80418.png" alt="在这里插入图片描述"> 

- 生成文件相关的报告
>  
 [root@s166 audit]# aureport -f <img src="https://img-blog.csdnimg.cn/a1b8a2a8697c410a90e1c03c7937b714.png" alt="在这里插入图片描述"> 

- 生成用户相关的报告
>  
 [root@s166 audit]# aureport -u 

- 生成配置变更报告
>  
 [root@s166 audit]# aureport -c 

- 生成登录记录报告
>  
 [root@s166 audit]# aureport -l 

- 生成指定时间段的报告
>  
 [root@s166 audit]# aureport -ts “8:00:00” -te “now” -l -i  Login Report ============================================ # date time auid host term exe success event ============================================ \1. 2023年10月25日 11:01:08 root 192.168.0.186 ssh /usr/sbin/sshd no 1413 

- 生成所有用户失败事件的总结报告
>  
 [root@s166 audit]# aureport -u --failed --summary -i  Failed User Summary Report =========================== total auid =========================== 34 root 20 unset 

- 生成系统调用事件报告
>  
 [root@s166 audit]# aureport -s -i --summary  Syscall Summary Report ========================== total syscall ========================== 161 setsockopt 57 execve 30 init_module 27 unshare 5 ioctl 4 open 2 write 2 rename 2 chmod 2 setxattr 1 fchmodat 1 unlinkat 

