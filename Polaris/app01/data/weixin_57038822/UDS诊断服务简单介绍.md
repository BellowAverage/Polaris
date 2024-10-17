
--- 
title:  UDS诊断服务简单介绍 
tags: []
categories: [] 

---
****UDS简单介绍****

（1）UDS（Unified Diagnostic Service，统一诊断服务），诊断协议是ISO 15765和ISO 14229定义的一种汽车通用诊断协议，位于OSI模型中的应用层，可在不同的汽车总线（例如CAN、LIN、Flexray、Ethernet、K-line）上实现。UDS协议的应用层定义是ISO 14229-1，目前大部分汽车厂商均采用UDS on CAN的诊断协议。 UDS诊断服务的主要应用包括诊断/通讯管理、数据处理、故障信息读取、在线编程及功能/元件测试等。 UDS采用的是Client/Server的模式，基本是Client发送一个请求报文，Server会根据请求报文做出相应的响应。Client一般情况下是指测试仪（Tester），发送诊断请求；Server一般是指电控单元（诊断响应的提供者），发送诊断响应。 UDS本质上是一系列的服务，共包含6大类26种，每种服务都有自己独立的ID，即SID。

<img src="https://img-blog.csdnimg.cn/direct/4d9ef378bd554ad68a93dc9d0a689c3c.png" alt="在这里插入图片描述">

服务 描述 10 客户端请求控制与某个服务器的诊断对话 11 客户端强制服务器执行复位 27 客户端请求解锁某个受安全保护的服务器 28 客户端请求开启/关闭服务器收发报文的功能 3E 客户端向服务器指示客户端仍然在线 83 客户端使用该服务读取/修改某个已经激活的通信的定时参数 84 客户端使用该服务执行带扩展的数据链接安全保护的数据传输 85 客户端控制服务器设置DTC 86 客户端请求服务器启动某个时间机制 87 客户端请求控制通信波特率 22 客户端请求读取指定标识符的数据 23 客户端请求读取指定存储器地址范围内数据的当前值 24 客户端请求读取标识符的定标信息 2A 客户端请求周期性传输服务器中的数据 2C 客户端请求动态定义由ReadDataByIdentifier服务读取的标识符 2E 客户端请求写入由数据标识符指定的某个记录 3D 客户端请求将数据写入到指定存储器地址范围内 14 客户端请求清除诊断错误码信息（DTC） 19 客户端请求读取诊断错误码信息（DTC） 2F 客户端请求替换电子系统的输入信息值、内部服务器功能或控制系统的输出 31 远程请求启动，停止某个例程或请求例程执行结果 34 初始化数据传输，ECU接收到请求后，完成所有下载前准备工作后，发生肯定响应

SID：（Service Identifier，诊断服务ID），UDS本质上是一种定向的通信，是一种交互协议 肯定响应：回复[SID+0x40]，服务器端正确执行客户端诊断请求时做出的响应 否定响应：回复7F+SID+NRC，服务端无法正确执行客户端的诊断请求时做出的响应

（2）报文包含的4种类型： SID SID+SF（Sub-function） SID+DID（Data Identifier）读写使用 SID+SF+DID

（3）常用服务介绍 $10 Diagnostic Session Control $14 Clear Diagnostic Information $19 Read DTC Information $22 Read Data By Identifier $27 Security Access $2E Write Data By Identifier $3e Test Present

（4）寻址方式 在总线上往往有许多的ECU设备，作为诊断设备既可以与所有的ECU一起通讯，也可以与指定的某个ECU单独通讯。寻址方式分为功能寻址（Functionally Addressed）和物理寻址（Physically Addressed）这两种方式。 功能寻址：可以广播诊断请求Request，同时等待总线上的ECU给予响应 物理寻址：指定发送特定诊断请求Request，等待特定ECU给予响应 所以，诊断报文一般会有3个CAN ID，其中DiagRequest（诊断物理请求报文）和DiagState（诊断功能请求报文）是ECU接收来自Client的报文，而DiagRespone（诊断响应报文）是ECU反馈的报文。

UDS网络层，又称为TP（Transport Protocol Layer）层，其存在的目的是为了解决ISO 11898协议中定义的经典CAN数据链路层与ISO 14229协议中定义的应用层，彼此之间数据长度不统一的问题。

汽车统一诊断服务网络层的异常操作测试包括传输数据丢失测试、单帧无效测试、单帧DLC位不正确测试(datelengthcode位为根据ISO15765规定，用于规定数据场长度的字节位)、双帧测试、单帧中断请求测试、首帧短于DLC位定义测试、首帧中断请求测试、单独的首帧测试、首帧功能寻址测试、连续帧丢失测试、丢失某一连续帧测试、连续帧延迟测试、连续帧无效测试、连续帧DLC位不正确测试、不期望的连续帧测试、连续帧中断请求测试、无流控制帧测试、流控制帧延迟测试、多余流控制帧测试、流控帧短于DLC位定义测试、错误的流控帧测试、不期望的流控制帧测试、流控制帧功能寻址测试、流控制帧中断请求测试、溢出流控制帧中断响应测试、未知帧测试和未知帧中断响应测试。

P2server：ECU收到Tester（客户端）发送的Requset起到ECU做出响应之间的时间段。 P2client：Tester（客户端）发送Requset MSG起到收到ECU的响应的时间段。 P2**service：当ECU发送NRC 0x78（pending）开始计时到ECU发送下一响应需要的时间。 P2**client：这个时间段是Testers收到NRC 0x78开始计时到Tester（客户端）收到下一多帧或单帧的时间段。 P3client_Pyh：这个时间是Tester（客户端）成功发送物理寻址开始计时到下一次发送物理寻址的时间段。 P3client_Func:这个时间是Testerc（客户端）成功发送功能寻址开始计时到下一次发送功能寻址的时间段。

1.UDS 27服务（安全访问） 在读取一些特殊数据的时候，要先进行一个安全解锁。ECU上电之后是一个锁定的状态（Locked），我们通过$27服务，加上一个子服务，再加上一个钥匙，这样的服务请求可以进行解锁。例如，通过首轮种子27+01（0x01表示请求seed）的请求，首轮ECU会返回67+01+AA+BB+CC+DD，AA~DD就是种子了。之后第二轮，诊断端会利用种子进行运算（利用整车厂的算法），生成k1（不一定是1个字节），那么发送请求，27+02（0x02表示发送key）+[k1]。ECU同样也会通过种子算出k2。当k1和k2匹配时，解锁（Unlocked）成功。 “请求种子”子功能参数值始终为奇数；且同一安全级别相应的“发送密钥”子功能参数值始终为“请求种子”子功能参数值+1

2.$19 读DTC DTC（diagnostic trouble code）：如果系统检测到了一个错误，它将存储为DTC。DTC可表现为：一个显而易见的故障；通讯信号的丢失（不会使故障灯亮起）；排放相关的故障；安全相关的错误等。DTC可以揭示错误的位置和错误类型。 $19拥有28个子服务（Sub-Function），常用的子服务有02（通过DTC状态掩码读取DTC）、04（读取快照信息）、06（读取扩展信息）、0A（读ECU支持的所有DTC数据）。

<img src="https://img-blog.csdnimg.cn/direct/be6b29b5be51434693745f7faec3b701.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/12c46f183aec46da849b9d0cd89131d7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/2e8040e58fd048a5bd72846081349c51.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/edccb04a11534d14b951b236ab044795.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b6bc225112f6411fbe2335874df0edac.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/c43d2e27edd34c2fba0f0be50ed5f99f.png" alt="在这里插入图片描述">

3.UDS诊断服务中的诊断会话控制（DiagnosticSessionControl，0x10） 诊断会话在服务器中启用一组特定的诊断服务和/或功能，此服务提供服务器可以报告对启用的诊断会话有效的数据链路层特定参数值（例如定时参数值）的功能。 ISO 14229规定了几个特定的子功能，比如： 10 01 //默认会话：当服务器处于默认会话状态时，若客户端要求启动默认会话，则服务器应完全重新初始化默认会话，激活的会话期间，服务器应该重置所有已激活方/初始化的/更改过的设置/控制，但这不包括已编程如非易失性存储器中的长期更改。 10 02 //编程会话 10 03 //扩展会话 服务器从非默认会话的任何诊断会话转换为默认会话时，服务器应停止通过0x86服务在服务器中已经配置的所有事件，且应该启用安全性，应终止默认会话中不支持的任何其他活动的诊断功能。 以上几种在汽车ECU软件开发中最常用的三种，协议中规定，一次只能有一个会话，不能既是默认会话同时又是扩展会话。UDS其他服务在不同会话中会有不同的表现，比如安全认证只能在扩展会话下进行，而不能在默认话下进行。不同的会话可以相互切换，通常所有的会话都可以切回默认会话，而编程会话一般只会在扩展会话下进入，除了默认会话不需要保持之外，其他会话均需要发送指令来维持会话，否则超时之后返回默认会话。 例子：以CAN总线网络举例。八个帧数据字节，第一字节被网络层占用。 请求（Request）:02 10 02 xx xx xx xx xx ; 02是网络层单帧SF，数据域有2个字节，10是SID，02是子功能。 肯定响应:02 50 02 xx xx xx xx xx；02同上，10+40表示对SID的肯定回复，02是子功能。 否定响应:03 7F 10 22 xx xx xx xx；03同上，7F表示否定响应，10是SID，22是NRC。

<img src="https://img-blog.csdnimg.cn/direct/29b726a6bfc941c29cb02a9db1eedc77.png" alt="在这里插入图片描述">

a：在默认会话期间是否也允许0x86服务由具体实施情况而定 b：安全数据标识符需要安全访问服务，因此需要非默认诊断会话 c：安全内存区域需要安全访问服务，因此需要非默认诊断会话 d：数据标识符可以在默认和非默认诊断会话中动态定义 e：安全例行程序需要安全访问服务，因此需要非默认诊断会话，需要客户端主动停止的例行程序也需要非默认会话。 为什么设计三个会话模式呢？因为权限问题。默认会话权限最小，可操作的服务少；扩展模式通常用于解锁高权限诊断服务，例如写入数据/参数、读写诊断码；编程模式用于解锁bootloader相关的诊断服务，即程序烧录。

4.$14清除DTC 清除（复位）DTC格式，它可以改变DTC的状态。3个FF代表清除所有DTC。 Request：14+FF+FF+FF； Response：54

<img src="https://img-blog.csdnimg.cn/direct/f0ff43e6b70144d28bb96832d5dfb184.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/ab9f0d1b8f3743dba23295b436e62096.png" alt="在这里插入图片描述">

5.$22 ReadDataByIdentifier（$22根据标识符读取数据） $22读数据，Request（请求）：22+DID（Data Identifier，通常是两个字节） Response（响应）：62+DID+Data DID通俗的来讲，其实就是某一存储在非易失性存储器（Non-volatile memory，NVM）里、表示汽车或者软件的一些标识的ID，最为大家熟知的比如汽车的VIN码，还有软件发布日期等等。DID有一部分已经被ISO 14229-1规定了，比如0xF186就是当前诊断会话数据标识符，0xF187就是车厂备件号数据标识符，0xF188就是车厂ECU软件号码数据ID，0xF189就是车厂ECU软件版本号数据标识符。

6.WriteDataByLocalIdentifier $2E（$2E根据标识符写入数据） $2E写数据，Request（请求）：2E+DID+Data Response（响应）：6E+DID 对于写数据的请求，一般来说需要在一个非默认会话或解锁状态下才能进行。

7.InputOutputControlByIdentifier $2F（$2F按标识符的输入输出控制）

<img src="https://img-blog.csdnimg.cn/direct/47189157a88b4e8682642797ac2fb13f.png" alt="在这里插入图片描述">

controlOptionRecord，用于标识控制方式，比如是启动、停止控制，还可以有一些自定义的参数来进行更精准的控制，比如让某个执行器的动作持续多长时间。controlOptionRecord又分为两部分，分别是1个byte的inputOutputControlParameter，以及若干byte由厂家自定义使用的controlState。 controlEnableMaskRecord，这是一个可选参数，用于标识controlOptionRecord中的哪些parameter被使用。

<img src="https://img-blog.csdnimg.cn/direct/ef210353c6234997b9c5c68ea36a7dcb.png" alt="在这里插入图片描述">

以14229中举的一个例子来感受一下2F服务： 这个例子是使用2F控制Air Inlet Door Position （进气口门位置），用标识符0x9B00来标识进气口门的位置。Air Inlet Door Position [%] = decimal(Hex) * 1 [%] ，即用一个百分比来表示这个位置。 step1:tester 发送22 9B 00读取当前进气口门的位置 ECU返回62 9B 00 0A ， 0x0A = 10（dec），表示当前位置是10% step2:tester 发送2F 9B 00 03 3C ，表示要将进气口门的位置调整到60%，0x3C = 60（dec） ECU返回6F 9B 00 03 0C，表示接受控制，当前进气口门的位置为12%。因为ECU收到请求后是立刻响应的，而门的位置调节需要时间，所以还没有达到60%。 step3:过一段时间后tester 发送22 9B 00读取当前进气口门的位置 ECU返回62 9B 00 3C ， 0x3C = 60（dec），表示当前位置已经到了60% step4:tester 发送2F 9B 00 00，将控制权交还给ECU ECU返回6F 9B 00 00 3A，表示接受请求，当前位置为58% step5:tester 发送2F 9B 00 02，冻结9B 00这个ID所代表的进气口门位置这个状态 ECU返回6F 9B 00 02 32，表示接受请求，当前位置保持在50%

8.StartRoutineByLocalIdentifier $31（例程服务单元） 该服务用于维护和停止ECU内部例程。可以读取例程的结果以进行分析。该例程由两个字节的例程identifier标识。 （1）请求服务

<img src="https://img-blog.csdnimg.cn/direct/ea82fd6fe65a45208fed01b5194d5d9b.png" alt="在这里插入图片描述">

（2）子服务说明

<img src="https://img-blog.csdnimg.cn/direct/1dda9f7157f045849772a9f7f354f70e.png" alt="在这里插入图片描述"> （3）例程标识符：

<img src="https://img-blog.csdnimg.cn/direct/2a2b07e5f46a49bbb5ba8dd75c7bb761.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/4c4f77e904134d16af63c405ba80bf58.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/4d20f14340684d6288e53d7c56ab6eec.png" alt="在这里插入图片描述">

9.Communication $28（$28 通信控制） 服务的目的是开关ECU对特定报文的传送/接收。 0x28就是一个通信控制的服务，根据需求你想让什么类型的报文进行通信或者不让其进行通信，就可以用0x28服务来进行设置。例如bootloader刷写之前或者某些例程控制的时候可能会要求停止网络诊断功能等，就可以利用0x28服务来进行控制。

28服务的DID：

<img src="https://img-blog.csdnimg.cn/direct/19099570e28945ae8ff8204c05b1d00c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/dfe97391fa564569b753e42735666164.png" alt="在这里插入图片描述">

请求信息数据参数：

<img src="https://img-blog.csdnimg.cn/direct/14d4a234d4f84f72936bdb20f703cee3.png" alt="在这里插入图片描述">

10.DTC Setting $85（DTC设置） 控制诊断故障代码设置服务用于停止或重启电控单元设置诊断故障代码。 当接收到子功能参数为“开”的控制诊断故障代码服务请求，会话层时序参数超时（电控单元进入默认会话）或电控单元执行复位操作后，诊断故障代码状态信息应重新开始更新。

<img src="https://img-blog.csdnimg.cn/direct/11c1d83ec5ce426d84864fafb1c2d57f.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/667163eb5e164afa818d47341020a86e.png" alt="在这里插入图片描述">

11.Tester Present $3E（会话保持） 这个服务的目的是确保诊断服务或者之前激活的通信还处在激活的状态，可以保持当前的非默认（Default Session）会话，通过周期地发送请求帧来阻止自动跳转回默认（Default Session）会话。

12.Request Download 0x34（请求下载）

（1）请求服务：

<img src="https://img-blog.csdnimg.cn/direct/2263dc58d3c441278de462604a426d0a.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/540c5a03cbe24373b62f652d531e11f9.png" alt="在这里插入图片描述">

（2）肯定响应：

<img src="https://img-blog.csdnimg.cn/direct/92efd42f738b4546847091e9d966218b.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/2ef439470e914246939c222686ffc17a.png" alt="在这里插入图片描述">

（3）例子：

<img src="https://img-blog.csdnimg.cn/direct/e496898fb49643f1a690c6343a9c26e1.png" alt="在这里插入图片描述"> 13.TransferData 0x36（传输数据） 数据传输方向取决于请求下载或请求上传服务，收到0x34、0x35服务请求时，响应数据的块序列计数器（blockSequenceCounter）应该初始化为1。 （1）服务请求：

<img src="https://img-blog.csdnimg.cn/direct/b29fdadce25f466e9821845ae8fbbefe.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/30db2a53e6de457383490e86542c3c55.png" alt="在这里插入图片描述">

（2）肯定响应：

<img src="https://img-blog.csdnimg.cn/direct/78ee63f2a89d41eea25d7183c84b8f83.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/3dbc76aee69b4f84bba64be3f3d92325.png" alt="在这里插入图片描述"> 14.ECUReset 0x11（ECU重置） 客户端使用ECUReset服务来请求服务器重置。服务器应激活默认会话，建议在此期间ECU不接受任何请求消息，亦不发送任何响应消息。 （1）服务请求

<img src="https://img-blog.csdnimg.cn/direct/04a184fa2be744078dd4b601fc04db6e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/4ec6e810986d4968adfd09f15409f55c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/3b2fad9d67994b56b83afb9c4db7f0cb.png" alt="在这里插入图片描述"> （2）肯定响应

<img src="https://img-blog.csdnimg.cn/direct/69c86df6c8b94c49b51a7bed509e5511.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/direct/3d1cb163a6e542028497dfaf8b2fd678.png" alt="在这里插入图片描述">

DID：

<img src="https://img-blog.csdnimg.cn/direct/3684d74ff4834ff1a26e4586b896daa8.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/148af5b658ec40ba934b9cb5d263d273.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/fe7f21b8c8674abaaae030942a8a99a1.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/f5d15b8de1934ccfb10cf59019245482.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/2e9ba445522f4bbfa12ba3f156334c3c.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/805fec03de4345f6bb6bebed4c8ee89e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/6b768bcbeca744838e637191b7c7f166.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/8a398b9bd35f4a8faa77b8b530e0ede9.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b183bfcf2d8b4725a2906983d1662e45.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/92b0e7c440b7481fa6cf0c652cb92cb7.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/84ed5a08e3554f0c934d82755ef537db.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/1af7af3e3fed496c98302efdb3db19c8.png" alt="在这里插入图片描述"> ECU升级概述： 关于ECU升级数据的传输，是通过34（请求下载）、36（传输数据）、37（请求退出传输）这3个服务来完成的。关于升级文件中一个块的传输流程如下（假设正常升级，即没有否定响应的情况）： 诊断仪通过34服务传输该块的起始地址、该块的数据长度信息；进行下载请求； ECU收到34服务的下载请求后，通过74肯定响应报文通知诊断仪，其（诊断仪）接下来的每个数据传输的报文中（36服务）应包含多少数据字节。诊断仪则根据该返回的参数对自身的发送能力进行调整； 诊断仪通过36服务传输该块的数据，每个36服务传输的数据量大小由前面提到的ECU返回的74服务中的参数确定； ECU对36服务返回肯定响应； 通过36服务依次将该数据进行拆分发送，期间每完成一次36服务的发送，ECU进行肯定响应的回复。直到该块数据全部发送完； 诊断仪通过发送37服务进行传输退出的请求； ECU进行肯定响应回复。

升级文件中每个块（即升级数据分成的多个地址不连续的段）的数据传输都会有一个34服务进行传输的请求，并通过参数告知ECU该块数据的存放地址和长度；然后根据该块数据的大小会分成n个36服务进行数据的传输工作；在该块数据都传输完成后，通过一个37服务进行传输退出的请求。即升级文件中的每个块的传输过程，由1个34服务、n个（根据该块数据量大小确定）36服务，1个37服务完成。 诊断报文解析 UDS 的诊断数据的发送与接收都是基于CAN，所以每个数据流都包含基本的CAN Message 的架构：CAN Message =CAN ID + CAN DATA 每个PDU（协议数据单元）的格式：Address information（N_AI）+Protocol control information（N_PCI）+Data field（N_Data） 网络层PDU（协议数据单元）PCI（协议控制信息）格式：

N_PDU name N_PCI bytes 帧类型 Bit7-4 Bit3-0 Byte 2 Byte 3 单帧（SF） N_PCItype=0 SF_DL N/A N/A 首帧（FF） N_PCItype=1 FF_DL N/A 连续帧（CF） N_PCItype=2 SN N/A N/A 流控帧（FC） N_PCItype=3 FS BS ST_min

SF_DL代表单帧中数据字节数（取值0-7） N/A代表不适用 FF_DL代表连续帧中数据字节数 SN代表此帧为连续帧的第几帧 FS代表流控制帧，有三种状态：继续发送0、保持发送1、数据溢出2 BS规定发送端允许持续传输连续帧数据的最大值（0-255） ST_min限定连续帧相互之间所允许的最小时间间隔，单位ms。此外，BS和ST_min等于00的话代表，连续帧没有message数量和时间间隔的具体限制，发送方可以将数据以最快最多的方式发送。连续帧的序号从21开始到2F，之后从20开始到2F进行循环使用。

0x 单帧（SF）：首个字节为：0（4bit）+ Data Length(4bit)，控制信息占用1个字节。

<img src="https://img-blog.csdnimg.cn/direct/dd9235a49cad4e44854b7ff23bf7e63f.png" alt="在这里插入图片描述"> 举例：Data 02 10 02 55 55 55 55 55，02表示接收方应知晓，这一个单帧只有2个有效字节。后续的字节是自动填充的无效字节

1x xx 首帧（FF）：前两个字节为：1（4bit）+ Data Length(12bit)，控制信息共占用2个字节。

<img src="https://img-blog.csdnimg.cn/direct/da913d383414442eac1209659ee295d1.png" alt="在这里插入图片描述">

举例：Data 10 14 2E F1 90 01 02 03，0x014表示，接收方应知晓，这一个多帧组合共有20个字节。

3x 流控制帧（FC）：前三个字节为：3（4bit）+流状态（FS，4bit）+块大小（BS，8bit）+最小间隔时间（STmin，8bit），控制信息共占用三个字节。

<img src="https://img-blog.csdnimg.cn/direct/9b36feaf79c74e3292e5f8427425342c.png" alt="在这里插入图片描述">

举例：Data 30 00 14 AA AA AA AA AA，多帧发送方应知晓，这是一个流控帧，允许发送方继续发送，CF数量无限制，上一个连续帧的确认接收（ACK）到新的连续帧开始发出的最小间隔时间为20ms。

ST_min：

<img src="https://img-blog.csdnimg.cn/direct/a5b2ad239e02443580d72a4ec99d76ad.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/98d444e5827c4b2c867ca5a2acf5a66e.png" alt="在这里插入图片描述">

2x 连续帧（CF）：第一个字节为2+SN（最多16个SN，溢出后从0开始重新计数），控制信息占用1个字节。

<img src="https://img-blog.csdnimg.cn/direct/11eca3f9428b47d0b0e35346d95f784b.png" alt="在这里插入图片描述"> Eg.数据发送：06 19 04 00 01 00 00 00 数据反馈：59 01 00 01 00 27 00 0B FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

<img src="https://img-blog.csdnimg.cn/direct/c5656308c97e461db1a4f0ee0d4ff95b.png" alt="在这里插入图片描述">

数据发送为单帧，所以06代表发送的数据中含有6个字节，回复为正反馈，为连续帧，10 代表连续帧的首帧，1E代表此连续帧含有30个字节，30代表此连续帧的流控制帧，21，22，23，24代表连续帧中的第几帧，21代表第一帧，22代表第二帧，依此类推，其中AA为填充位。

对报文数据的一些响应： 1.发送数据为单帧时，有三种响应情况 （1）肯定响应（单帧）；第一个字节是SID+0x40 （2）肯定响应（首帧）；第二个字节是SID+0x40 （3）否定响应：第二个字节是SID

2.发送数据为首帧时，有两种情况 （1）肯定响应（流控帧） （2）否定响应

网络层时间控制分析 网络层的时间管理是为了保证发送端和接收端不会因为等待而永久挂起，从而失去通信能力。 网络层定时参数定义了N_As、N_Ar、N_Bs、N_Br、N_Cs、N_Cr六个参数。

<img src="https://img-blog.csdnimg.cn/direct/55744bd719eb4966aed59fc12e9bd4d4.png" alt="在这里插入图片描述">

定时参数 方向 描述 N_As 发送方→接收方 首帧和连续帧在数据链路层传播的时间 （发送端将数据传送到接收端的最大时间） N_Ar 接收方→发送方 流控制帧在数据链路层传播的时间 （接收端将流控制传送到发送端的最大时间） N_Bs 发送方→接收方 接收方收到首帧时发出的ACK响应，与发送方收到流控帧的间隔时间 N_Br 接收方→发送方 自己（接收方）收到首帧，与自己开始发出流控制帧的间隔时间 N_Cs（STmin） 发送方→接收方 自己（发送方）收到流控制帧，或者是连续帧送达时产生的ACK响应，与自己开始发出新连续帧的间隔时间 N_Cr 接收方→发送方 自己（接收方）收到连续帧，到下一次自己收到连续帧的间隔时间 s代表发送者的定时参数，r代表接收者的定时参数

<img src="https://img-blog.csdnimg.cn/direct/4ade9b4e52c9438785928c68244c516a.png" alt="在这里插入图片描述">

N_As超时：发送方没有及时发送N_PDU。 N_Ar超时：接收方没有及时发送N_PDU。 N_Bs超时：发送方没有接收到流控帧。 N_Br超时：接收方没有发出流控帧。 N_Cs：即STmin，发送两个连续帧需要等待的最短时间。 N_Cr超时：接收方没有收到连续帧。

N_Bs = N_Br + N_Ar，在网络测试时，无法直接测试N_Br的值，但由于N_Ar极小，因此可以假定N_Br = N_Bs，通过测试N_Bs来测试N_Br

<img src="https://img-blog.csdnimg.cn/direct/3e27cd94375d47ac92b501ff39986e58.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/959fbf9d5b5046cca597403bdbb3b3b7.png" alt="在这里插入图片描述">

以02 10 01 xx xx xx xx xx为例，02中的0代表网络层单帧SF，2代表数据域有2个字节。

NRC:Negative Response Code（否定响应码），当ECU拒绝了一个请求，会回应相应的NRC。不同NRC含义如下：

<img src="https://img-blog.csdnimg.cn/direct/ebced2f9774142dda2eb730f6cb63ac6.png" alt="在这里插入图片描述"> 10 普通的拒绝指令，仅在没有办法使用别的错误码进行解释的时候的默认错误返回 11 诊断服务不支持。无法识别服务码，一般是因为等级不够或者是发送错误。 12 。无法识别服务码的子服务。一般也是因为等级不够或者发送错误。 13 错误的数据报格式或者长度，这个错误码一般出现在网络层或者应用层。用于判断是否是编码和协议出现错误。一般长度都会在服务定义的时候规定好，一般只要不符就会报错 14 过长的数据返回。一般是因为数据的定义协议与要传输的数据大小不符，一般是因为传输的数据报在打包的时候发现数据过长。 21 过忙导致无法执行。一般是不会遇到，但是当写入DTC或者清除DTC时发送可能会遇到。故一般会在这边与主机厂商议等待时间。一般诊断仪也会等待100ms~200ms. 22 不正确的输入条件，大概是需要输入的是ASCII，但是传入的是HEX这种情况。或者是没在扩展模式（权限较高）下查询特殊的DTC（SN） 24 发送的顺序不对。可能是类似于密码校验的顺序出错或者校准的错误。 25 处理的子网无法响应。如果给T-BOX类的服务中转网关就可能会遇到，也就是当前网段识别了这个指令但是发送到子网中无法被执行或者是当前ECU（服务器）无法满足足够的条件进行执行。 26 DTC出现了错误的记录 31 过长的请求目标。这个主要是因为当前制定的code超出了当前允许的最大范围，但是又不是参数的定义最大范围，比如0xff为当前数据定义最大的数据，但是应用层协议定义了0x7F，但是client发送了0xf0，就会超出当前的范围。 33 安全访问问题。这个一般是因为27服务没有正确的操作完成，并且访问了需要安全权限访问的服务 35 错误的访问key，这次涉及到了很长的安全保护逻辑，这种访问主要是因为想要错误的进行高权限的破解，所以也有很高的保护逻辑。 36 超出了错误的安全测试次数。这个一般是和0x35绑定的。 37 超出的错误次数延时的反馈，这个也是基本上绑定0x36的 70 传输错误。一般是定义的位置错误或者是传输了错误的控制指令 71 传输终端。这个和正常服务并不一致，是因为某种原因导致当前的传输错误。 72 日常的编程错误。一般是擦除或者是因为写入错误，但是没啥具体的错误。就可以发出这个故障。 73 错误的块计数器。因为下载一般在下载的时候传输的数据块少了，或者是下载的时候丢包。 78 收到诊断请求，等待响应。挂起的访问等待请求。这个严格上来讲不算是错误，仅在当前操作正在进行的时候出现了新的请求。ECU想要诊断仪进行相关的等待的反馈，这个反馈也要受到基础的操作超时限制。 7E 不满足当前要求请求子服务。就是在权限不够情况就请求了错误的服务。 7F 诊断服务在当前会话下不支持。不满足当前要求请求服务。这个和0x7E差不多，区别只在于当前这个服务是主服务，不是主服务内的子服务。 81 编程管理地址过高 82 编程管理地址过低 83 引擎运行 84 引擎未运行 85 引擎运行时间过短 86/87 温度过高/温度过低 88/89 车速过高/车速过低 8A/8B 踏板过高/踏板过低 8C/8D 不在空挡/不在指定挡位 8F 未开启制动开关（电子驻车或手刹） 90 车辆不在P档 91 变速离合开关无法满足要求 92 电压过高，一般会导致写入不稳定，但是不会坏 93 电压过低，一般会导致无法写入或擦除

<img src="https://img-blog.csdnimg.cn/direct/b2d12e8c444747e99b27c939508781a0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/bd1795ab767240a29733419f0791bf26.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a4656e5ea2594e7a8fde02ef5e9e03f3.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/5839779ab21d4ac99325f1e2b7c62c24.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/55ded485e1c64b738cc3aa4293d6cddf.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/a32428ad1e8f4ff8b86a9074a2f190ae.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/b4f68a000da748e4b78adcd0adf8efc0.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/83f7ee3e9d864091824642fcda99a504.png" alt="在这里插入图片描述"> Flash Bootloader

Flash bootloader软件架构： CAN驱动：实现CAN报文的收发和CAN控制器硬件的操作。特点：初始化CAN控制器，CAN报文的收发，CAN报文事件反馈。

Flash驱动：用于操作Flash的擦除、写入和读取功能。特点：Flash硬件初始化，擦除Flash扇区，Flash块的数据写入，Flash块的数据读取，数据校验。

传输层：主要是提供数据的组包和拆包功能服务，能够实现报文的分段传输：长报文的分包发送，以及分包报文的组装接收。特点：分包和组装来自数据链路层的数据，长报文的流控制和定时参数的调整，数据传输过程中的错误检测和超时处理。

诊断层：当传输层采用基于ISO 15765协议规范时，诊断层作为可选项集成到Bootloader程序代码中。 诊断层实现ISO 15765-3/ISO 14229-1中定义的Bootloader程序刷写流程，包括：诊断会话切换、安全状态切换、标识符读写、程序刷写和ECU复位等。 诊断层主要有如下特点：实现ISO 14229中刷写相关的诊断服务，调用Flash Driver。

看门狗（Watch Dog）：为防止Bootloader出现超时操作，看门狗模块能够在超过一定时间后产生ECU复位操作，提高软件的可靠性。 看门狗定时有如下特点：监控Bootloader超时或者死机，对ECU复位；定时参数可以任意配置；实时性有保证

加密算法：主要用以处理软件加密和安全访问相关的诊断服务内容，实现程序下载的合法性和完整性。 加密算法模块有如下特点：根据用户需求不同，作为可选项；下载工具的合法性校检，Seed &amp; Key诊断服务；程序下载的完整性校检，如CRC校检

Bootloader主要完成的三个功能： （1）与上位机或者远程主机建立通信，完成应用程序的下载； （2）应用程序的格式解析； （3）将解析后的应用程序二进制代码编程到ECU的非易失性存储器中

与Bootloader相关的ECU信息主要有车辆VIN号、已经下载的软硬件版本、已下载次数、最后一次下载时间，该信息主要用在Bootloader下载过程中测试仪对比ECU信息，信息对比正确，则下载软件进入下一步流程，否则下载终止，该服务主要是保证下载软件可靠性和安全性重要保证。

Bootloader程序更新流程：上位机向ECU发送启动程序更新的指令，ECU收到指令之后，进入Bootloader程序，FlashDriver可以从外部下载到RAM空间，也可以将Bootloader更新指令放在RAM区，FlashDriver程序启动擦除程序并下载数据到Flash中完成程序的更新操作。

<img src="https://img-blog.csdnimg.cn/direct/5a81fdba2c2d40b7b38dd50b1229987e.png" alt="在这里插入图片描述">
1. Bootloader应支持的UDS服务 在boot程序中，10/27/11/3E的基础诊断服务需要支持，22/2E读写DID的服务需要支持，31/34/36/37这四个boot主打服务需要支持，共需要10个UDS服务。 在app段程序中，85和28服务需要支持，保证暂停CAN正常通信，暂停记录DTC，可以正在升级的设备专心升级。
<img src="https://img-blog.csdnimg.cn/direct/38f486a1a2cf465799ed9374bafa79e5.png" alt="在这里插入图片描述"> 2. Bootloader的编程阶段 （1）预编程阶段 ①3E TP报文 ②10服务切换到03扩展模式 ③85/28服务，用来关闭DTC和非诊断报文，使整个CAN网络处于安静的状态，这是对整车网络进行操作的，一般都是以功能寻址的方式进行。（注：先使用85关闭DTC，再使用28关闭报文）

<img src="https://img-blog.csdnimg.cn/direct/ad8d90b1fa0f4c3794f00cc73fa93fb4.png" alt="在这里插入图片描述"> （2）主编程阶段 ⑴10服务切换到编程模式，这里要注意，正确的方式是App段程序回复0x78 NRC，接下来跳转到boot段程序，最后由Boot段程序来回复10 02的肯定响应。错误的方式是由App段回复10 02的肯定响应，再进行跳转。 ⑵读取一个DID，tester要判断一下返回值。返回值里面可能包含密钥的一部分信息 ⑶27服务，解锁，通过安全验证

<img src="https://img-blog.csdnimg.cn/direct/cd3406d00c2d4daeb4f2f94cdaf57261.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/7eefea27308c4bb5a3200e9f3e84a5c8.png" alt="在这里插入图片描述"> ⑷写DID指纹，标记写软件人的身份，ECU回复写指纹成功。（根据OEM要求来执行） ⑸31服务，擦除Flash。ECU肯定响应，擦除成功。 ⑹34服务，请求数据下载，ECU回复确认最大块大小 ⑺36服务，开始传输数据。每个块传输完成后，ECU肯定响应。判断是否还有更多块需要下载。最多可以支持255个块 ⑻37服务，请求退出传输。ECU肯定响应 ⑼31服务-校验APP段程序，检查编程一致性/完整性。ECU肯定响应。校验成功 ⑽若有更多块需要下载，重新执行31（擦除Flash区域）-34-36-37-31（校验）服务。若无，往下执行。 ⑾11服务，ECU复位。之后应直接跳转到新下载的APP段程序中。

<img src="https://img-blog.csdnimg.cn/direct/6a4664f7bc704fd9bd38b243dd2a4737.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/2daace3956d24e34b4b6b670c5ac2070.png" alt="在这里插入图片描述"> （3）后编程状态 ①10服务切换到03扩展会话。 ②执行28服务和85服务，使能非诊断报文和DTC。这是对整车网络进行操作的，一般都是以功能寻址的方式来发送。注意先执行28，后执行85，避免DTC误报。

<img src="https://img-blog.csdnimg.cn/direct/912da4a03ad84cd5b3c894a5b42dd89a.png" alt="在这里插入图片描述">

③27服务，安全校验，准备写入数据 ④2E服务，将编程信息写入到ECU中 ⑤10服务，退回01默认会话。结束

<img src="https://img-blog.csdnimg.cn/direct/c53c8bb948994202bc5262f8f7ef6896.png" alt="在这里插入图片描述">
1.  BootLoader的启动顺序与转换流程 ①ECU上电或复位后，先进入Boot段。从Flash/EEPROM中读取App有效标志，运行boot标志。 ②判断运行boot标志，若为1，则进入Boot段的编程会话（安全等级为上锁），之后写Flash/EEPROM（不安全操作），运行boot标志清零。若S3定时器超时则退回Boot段默认会话。 ③经过安全访问进入Level2解锁状态，开始执行App内存擦除，擦除后App有效标志清零（不安全操作）。 ④开始烧写。烧写成功后运行boot标志写0，App有效标志写1。 ②*.判断运行boot标志，若为0，则进入Boot段的默认会话。 ③*.50ms后判断App有效标志，若为1，则跳转到App段默认会话。实现时使用汇编指令执行APP段程序；若为0，退回Boot段默认会话，且不再判断App有效标志，不会再尝试进入App段。 ④*.App段程序若收到了编程会话请求，运行boot标志写1，随即执行ECU复位，这样会重新进入boot段程序。 注：从BOOT跳入APP前需要判断APP的数据完整性，例如进行CRC校验。 1.  服务支持的会话与寻址方式 <img src="https://img-blog.csdnimg.cn/direct/c2f09b841764430e874c17b8fd4427ff.png" alt="在这里插入图片描述"> CRC校验（循环冗余校验）： CRC算法参数模型解释： NAME：参数模型名称。 WIDTH：宽度，即CRC比特数。 POLY：生成项的简写，以16进制表示。例如：CRC-32即是0x04C11DB7，忽略了最高位的"1"，即完整的生成项是0x104C11DB7。 INIT：这是算法开始时寄存器（crc）的初始化预置值，十六进制表示。 REFIN：待测数据的每个字节是否按位反转，True或False。 REFOUT：在计算之后，异或输出之前，整个数据是否按位反转，True或False。 XOROUT：计算结果与此参数异或后得到最终的CRC值。 
<img src="https://img-blog.csdnimg.cn/direct/02cf4667288e46ca9ce1c022e0744242.png" alt="在这里插入图片描述">

.S19文件 S格式文件中的每一行称为一个S记录，每个S记录由记录类型、记录长度、存储地址、代码/数据、校验和五个部分组成；每行最大是78个字节。156个字符。 记录类型：1个字节，用来描述记录的类型，一共定义了8种类型： S0：S格式文件的第一个记录，表示文件名（含路径），存储地址部分没有使用，以0000置位。S0表示记录的开始，无需下载到MCU S1：地址为2个字节的记录 S2：地址为3个字节的记录 S3：地址为4个字节的记录 S5：标记本文件的S1、S2、S3记录的个数（不是一个S文件所必须的） S7：地址为4个字节，表示程序开始执行的地址，代码/数据部分没有被使用，此行表示程序的结束，无需下载到MCU。 S8：地址为3字节，表示程序的开始执行地址，代码/数据部分没有被使用，此行表示程序的结束，无需下载到MCU。 S9：地址为2字节，表示程序的开始执行地址，代码/数据部分没有被使用，此行表示程序的结束，无需下载到MCU。 记录长度：2个字符(即1个字节)，显示在记录中剩余的字节数。即 记录长度 = 存储地址字节数 + 代码/数据字节数 + 校验和字节数 存储地址：2或3或4个字节(由记录类型决定)，用来表示代码/数据应该装载的起始地址。 代码/数据：0-64字符(即0-32字节)，表示需要下载到MCU中的数据。 校验和：2个字符(即1字节),校验数据，计算方法: 校验和 = 0xff – (记录长度 + 存储地址 + 代码/数据) (注意，校验和不是字符的校验和，而是实际二进制数的校验和)

例子： S01F0000443A5C50726F6A6563745F335C62696E5C50726F6A6563742E61627371 S123C000CF2100C6055B134A800BFE4A8000FE0000C015C031000000000000000000000092 S218FE8020F2FEC013EC31270BED31180A30700434F920F10A0B S9030000FC 说明; 第一行：S0,表示S19文件格式开始；1F为剩余字节数；0000无用；443A5C50726F6A6563745F335C62696E5C50726F6A6563742E616273为D:\Project_3\bin\Project.abs的ASCII码；71为校验和. 第二行：S1，表示本条记录存储地址长度为2字节；23(注意为16进制)剩余字节数，C000，表示起始地址，92表示校验和。即，本行表示将CF2100C6055B134A800BFE4A8000FE0000C015C0310000000000000000000000依次下载到从地址C000开始的一段连续地址中。 第三行：S2，表示本条记录存储地址长度为3字节，18(16进制数)表示剩余字节数，FE8020表示起始地址，0B为校验和。 第四行：S9，表示程序的结束，03为剩余字节数，地址为2个字节，表示程序开始执行的地址为0000，FC为校验和。

.hex文件 Hex文件以行为单位，每行以冒号开头，内容全部为16进制码。 Hex文件由数据长度（1个字节，只包含纯数据长度）、数据地址（2个字节）、数据类型（1个字节）、数据（n个字节）、校验（1个字节） 数据类型： ‘00’ Data Record//数据记录 ‘01’ End of File Record//文件结束记录 ‘02’ Extended Segment Address Record//扩展段地址记录（扩展段地址记录也叫HEX86记录,它包括4-19位数据地址段.指此后到下一个扩展线性地址出现之前的数据在内存中的基地址的高4-16位的值,所以此地址要向左移4位后与数据段读出的地址相加,才是此数据段在内存中的真实地址.此种格式实际寻址范围是16位的,即64K） ‘03’ Start Segment Address Record//开始段地址记录 ‘04’ Extended Linear Address Record//扩展线性地址记录（其后数据为基地址，扩展线性地址记录也叫作32位地址记录或HEX386记录） ‘05’ Start Linear Address Record//开始线性地址记录

例子： :020000040004F6 :1000000018F09FE518F09FE518F09FE518F09FE5C0 :1000100018F09FE5805F20B9F0FF1FE518F09FE51D 第一行，是Extended Linear Address Record，里面的数据，也就是基地址是0x0004，第二行是Data Record，里面的地址值是0x0000。那么数据18F09FE518F09FE518F09FE518F09FE5要写入FLASH中的地址为(0x0004 &lt;&lt; 16) | 0x0000，也就是写入FLASH的0x40000这个地址。同样，第三行的数据的写入地址为0x40010。当一个HEX文件的数据超过7k的时候，文件中就会出现多个Extended Linear Address Record。 End of File Record 行是每一个HEX文件的最后一行。例如： :00000001FF 这样的一行数据内容是固定的，数据长度为0，地址为0。

校验和的算法为：计算从数据长度的所有各字节的和模256的余。即各字节二进制算术和，不计超过256的溢出值，然后用0x100减去这个算数累加和，得出得值就是此行得校验和。 校验和=0x100-（数据长度+数据地址+数据类型+数据）

关于扩展段地址看个例子: :020000021100EB :10232200464C5549442050524F46494C4500464C74 从第一行得出扩展段地址值为0x1100,第二行数据得出的地址为0x2322,扩展段地址左移4位后与基地址相加即0x11000+0x2322=0x13322;

扩展线性地址:在32位寻址系统中使用,代表地址的16-31位(bit),指此后到下一个扩展线性地址出现之前的数据在内存中的基地址的高16位的值,所以此地址要向左移16位后与数据段读出的地址相加,才是此数据段在内存中的真实地址.
