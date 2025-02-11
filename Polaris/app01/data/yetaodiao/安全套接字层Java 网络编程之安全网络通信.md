
--- 
title:  安全套接字层Java 网络编程之安全网络通信 
tags: []
categories: [] 

---
SSL（Secure Socket Layer，安全套接字层）是一种保证网络上的两个节点进行安全通信的协议。IETF（Interet Engineering Task Force）国际组织对 SSL 作了标准化，制定了 RFC2246 规范，并将其称为传输层安全（Transport Layer Security，TLS）

SSL 和 TLS 都建立在 TCP/IP 的基础上，一些应用层协议，如 HTTP 和 IMAP，都可以采用 SSL 来保证安全通信。建立在 SSL 协议上的 HTTP 被称为 HTTPS 协议。HTTP 使用的默认端口为 80，而 HTTPS 使用的默认端口为 443

SSL 采用加密技术来实现安全通信，保证通信数据的保密性和完整性，并且保证通信双方可以验证对方的身份

##### **1. 加密通信**

当客户与服务器进行通信时，通信数据有可能被网络上的其他计算机非法监听，SSL 使用加密技术实现会话双方信息的安全传递。加密技术的基本原理是，数据从一端发送到另一端时，发送者先对数据加密，然后把它发送给接收者。这样，在网络上传输的是经过加密的数据。如果有人在网络上非法截获了这批数据，由于没有解密的密钥，数无法获取真正的原始数据。接收者接收到加密的数据后，先对数据解密，然后处理

##### **2. 安全证书**

<img alt="" height="442" src="https://img-blog.csdnimg.cn/53901fe4d46a4d698f2683cc534fcb1a.png" width="962">



除了对数据加密通信，SSL 还采用了身份认证机制，确保通信双方都可以验证对方的真实身份。这和生活中我们使用身份证来证明自己的身份很相似，比如你到银行去取钱，你自称自己是张三，如何让对方相信你的身份呢？最有效的办法就是出示身份证。每人都拥有唯一的身份证，这个身份证上记录了你的真实信息。身份证由国家权威机构颁发，不允许伪造。在身份证不能被别人假冒复制的前提下，只要你出示身份证，就可以证明你自己的身份

个人可以通过身份证来证明自己的身份，对于一个单位，比如商场，可以通过营业执照来证明身份。营业执照也由国家权威机构颁发，不允许伪造，它保证了营业执照的可信性

SSL 通过安全证书来证明客户或服务器的身份，当客户通过安全的连接和服务器通信时，服务器会先向客户出示它的安全证书，这个证书声明该服务器是安全的，而且的确是这个服务器，每一个证书在全世界范围内都是唯一的，其他非法服务器无法假冒，可以把安全证书比作电子身份证

对于单个客户来说，到公认的权威机构去获取安全证书是云件麻烦的事。为了扩大客户群并且便于客户的访问，许多服务器不要求客户出示安全证书。在某些情况下，服务器也会要求客户出示安全证书，以便核实该客户的身份，这主要是在 B2B 事务中

获取安全证书有两种方式，一种方式是从权威机构获得证书，还有一种方式是创建自我签名证书

###### **2.1 从权威机构获取证书**

安全证书由国际权威的证书机构颁发，它们保证了证书的可信性。申请安全证书时，必须支付一定的费用。一个安全证书只对一个 IP 地址有效，如果用户的系统环境中有多个 IP 地址须为每个 IP 地址都购买安全证书

###### **2.2 创建自我签名证书**

在某些场合，通信双方只关心数据在网络上可以被安全传输，并不需要对方进行身份验证，在这种情况下，可以创建自我签名的证书。就像用户自己制作的名片，缺乏权威性，达不到身份认证的目的。当你向对方递交名片时，名片上声称你是某个大公司的老总，信不信只能由对方自己去判断

既然自我签名证书不能有效地证明自己的身份，那么有何意义呢？在技术上，无论是从权威机构获得的证书，还是自己制作的证书，采用的加密技术都是一样的，使用这些证书，都可以实现安全地加密通信

##### **3. SSL 握手**

安全证书既包含了用于加密数据的密钥，又包含了用于证实身份的数字签名。安全证书采用公钥加密技术，公钥加密指使用一对非对称的密钥进行加密或解密。每一对密钥由公钥和私钥组成，公钥被广泛发布，私钥是隐藏的，不公开。用公钥加密的数据只能够私钥解密，反过来，使用私钥加密的数据只能被公钥解密

客户与服务器通信时，首先要进行 SSL 握手，SSL 握手主要完成以下任务：
- 协商使用的加密套件，加密套件中包括一组加密参数，这些参数指定了加密算法和密钥的长度等信息- 验证对方的身份，此操作是可选的- 确定使用的加密算法
SSL 握手过程采用非对称加密方法传递数据，由此来建立一个安全的会话。SSL 握手完成后，通信双方将采用对称加密方法传递实际的应用数据。所谓对称加密，指通信双方使用同样的密钥来加密数据

SSL 握手的具体流程如下：
1. 客户将自己的 SSL 版本号、加密参数、与会话有关的数据以及其他一些必要信息发送到服务器1. 服务器将自己的 SSL 版本号、加密参数、与会话有关的数据以及其他一些必要信息发送给客户，同时发送给客户的还有服务器的证书。如果服务器需要验证客户身份，那么服务器还会发出要求客户提供安全证书的请求1. 客户端验证服务器证书，如果验证失败，就提示不能建立 SSL 连接。如果成功，就继续下一步骤1. 客户端为本次会话生成预备主密码（pre-master secret），并将其用服务器安全证书附带的公钥加密后发送给服务器1. 如果服务器要求验证客户身份，那么客户端还要再对另外一些数据签名后，将其与客户端证书一起发送给服务器1. 如果服务器要求验证客户身份，则检查签署客户证书的 CA 是否可信。如果不在信任列表中，则结束本次会话。如果检查通过，那么服务器用自己的私钥解密收到的预备主密码，并用它通过某些算法生成本次会话的主密码（master secret）1. 客户端与服务器均使用此主密码生成本次会话的会话密钥（对称密钥）。在双方 SSL 握手结束后传递任何消息均使用此会话密钥。这样做的主要原因是对称加密比非对称加密的运算量低一个数量级以上，能够显著提高双方会话时的运算速度1. 客户端通知服务器此后发送的消息都使用这个会话密钥进行加密，并通知服务器客户端已经完成本次 SSL 握手1. 服务器通知客户端此后发的消息都使用这个会话密钥进行加密，并通如服务器已经完成本次 SSL 握手1. 本次握手过程结束，会话已经建立。在接下来的会话过程中，双方使用同一个会话密钥分别对发送以及接收的信息进行加密和解密
##### **4. 创建自我签名的安全证书**

JDK 提供了制作证书的工具 keytool，它的位置为：&lt;JDK根目录&gt;\bin\keytool.exe

keytool 工具提出了密钥库的概念，密钥库中可以包含多个条目，每个条目包括一个自我签名的安全证书以及一对非对称密钥

通过 keytool 工具创建密钥库的命令为：

keytool -genkeypair -alias weiqin -keyalg RSA -keystore C:\chapter15\test.keystore
- genkeypair：生成一对非对称密钥- alias：指定条目以及密钥对的别名，该别名是公开的- keyalg：指定加密算法，本例中采用通用的 RSA 算法- keystore：设定密钥库文件的存放路径以及文件名字
命令的运行过程首先会提示输入密钥库的密码，然后提示输入个人信息，如姓名、组织单位和所在城市等，只要输入真实信息即可

以下命令查看 test.keystore 密库的信息，会列出所包含的条目的信息

keytool -list -v -keystore C:\chapter15\test.keystore -storepass "123456”

以下命令把 test.keystore 密钥库中别名为 weiqin 的条目导出到一个安全证书，文件名为 weiqin.crt。weiqin.crt 文中包含了自我签名的安全证书，以及密钥对中的公钥，但不包含密钥对中的私钥

keytool -export -alias weigin -keystore C:\chapter15\test.keystore -file C:\chapter15\weigin.crt -storepass “123456”

以下命令删除 test.keystore 密钥库中的别名为 weiqin 的条目

keytool -delete -alias weigin -keystore C:\chapter15\test.keystore -storepass “123456”

以下命令把 weiqin.crt 安全证书导入 testTrust.keystore 密库中生成别名为 weiqin 的条目，这个条目中包含密钥对中的公钥，但不包含密钥对中的私钥

keytool -import -alias weiqin -keystore C:\chapter15\testTrust.keystore -file C:\chapter15\weiqin.crt -storepass "123456"



### ****2****|****0******JSSE 简介**

JSSE 封装了底层复杂的安全通信细节，使得开发人员能方便地用它来开发安全的网络应用程序

##### **1. KeyStore、KeyManager 与 TrustManager 类**

在进行安全通信时，要求客户端与服务器端都支持 SSL 或 TCL 协议。客户端与服务器端可能都需要设置用于证实自身身份的安全证书，还要设置信任对方的哪些安全证书。更常见的情况是，服务器端只需要设置用于证实自身身份的安全证书，而客户端只需要设置信任服务器的哪些安全证书

KeyStore 类用于存放包含安全证书的密钥库，以下程序代码创建了一个 KeyStore 对象，它从 test.keystore 密钥库文件中加载安全证书

String passphrase = "123456"; //JKS是JDK 支持的KeyStore的类型 KeyStore keyStore = KeyStore.getInstance("JKS"); char[] password = passphrase.toCharArray(); //password参数用于打开密钥库 keyStore.load(new FileInputStream("test.keystore"), password);

KeyManager 接口的任务是选择用于证实自身身份的安全证书，把它发送给对方。KeyManagerFactory 负责创建 KeyManager 对象，例如

KeyManagerFactory keyManagerFactory = KeyManagerFactory.getInstance("SunX509"); keyManagerFactory.init(keyStore, password); KeyManager[] keyManagers = keyManagerFactory.getKeyManagers();

TrustManager 接口的任务是，决定是否信任对方的安全证书。TruesManagerFactory 负责创建 TrustManager 对象，例如

TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance("SunX509"); trustManagerFactory.init (keyStore); TrustManager[] trustManagers = trustManagerFactory.getTrustManagers();

##### **2. SSLContext 类**

SSLContext 类负责设置与安全通信有关的各种信息，比如使用的协议（SSL 或者 TLS），自身的安全证书以及对方的安全证书。SSLContext 还负责构造 SSLServerSocketFactory、SSLSocketFactory 和 SSLEngine 对象

以下程序代码创建并初始化了一个 SSLContext 对象，然后由它创建了一个 SSLServerSocketFactory 对象

SSLContext sslCtx = SSLContext.getInstance("TLS");//采用TLS协议 sslCtx.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null); SSLServerSocketFactory ssf = sslCtx.getServerSocketFactory();

SSLContext 的 init 方法的定义如下

public final void init(KeyManager[] km, TrustManager[] tm, SecureRandom random) throws KeyManagementException
- 参数 random 用于设置安全随机数，如果该参数为 null，init 方法就会采用默认的 SecureRandom 实现- 如果参数 km 为 null，那 init 方法会创建默认的 KeyManager 对象以及与之关联的 KeyStore 对象，KeyStore 对象从系统属性 javax.net.ssl.keyStore 取安全证书。如果不存在这样的系统属性，那么KeyStore 对象内容为空<li>如果参数 tm 为 null，那么 init 方法会创建一个默认的 TrustManager 对象以及与之关联的 KeyStore 对象，KeyStore 对象按照如下步骤获取安全证书： 
  <ul>- 先尝试从系统属性 javax.net.ssl.trustStore 获取安全证书- 如果上一步失败，就把 &lt;JDK 根目录&gt;/lib/security/jssecacerts 文件作为安全证书- 如果上一步失败，就把 &lt;JDK 根目录&gt;/lib/security/cacerts 文件作为安全证书- 如果上一步失败，那么 KeyStore 对象的内容为空
##### **3. SSLServerSocketFactory类**

SSLServerSocketFactory 类负责创建 SSLServerSocket 对象

SSLServerSocket serverSocket = (SSLServerSocket) sslServerSocketFactory.createServerSocket(8000); // 监听端口8000

SSLServerSocketFactory 对象有两种创建方法：
- 调用 SSLContext 类的 getServerSocketFactory 方法- 调用 SSLServerSocketFactory 类的静态 getDefault 方法
SSLServerSocketFactory 类的静态 getDefault 方法返回一个默认的 SSLServerSocketFactory 对象，它与一个默认的 SSLContext 对象关联，getDefault 方法的实现按照如下方式初始化这个默认的 SSLContext 对象

sslContext.init(null,null,null);

##### **4. SSLSocketFactory 类**

SSLSocketFactory 类负责创建 SSLSocket 对象

SSLSocket socket = (SSLSocket) sslSocketFactory.createSocket("localhost",8000);

SSLSocketFactory 对象有两种创建方法
- 调用 SSLContext 类的 getSocketFactory 方法- 调用 SSLSocketFactory 类的静态 getDefault 方法
SSLSocketFactory 类的静态 getDefault 方法返回一个默认的 SSLSocketFactory 对象，它与一个默认的 SSLContext 对象关联，getDefault 方法的实现按照如下方式初始化这个默认的 SSLContext 对象

sslContext.init(null,null,null);

##### **5. SSLSocket类**

SSLSocket 类是 Socket 类的子类，因此两者的用法有许多相似之处。此外，SSLSocket 类还具有与安全通信有关的方法

###### **5.1 设置加密套件**

客户与服务器在握手阶段需要协商实际使用的加密套件，以下两种情况都会导致握手失败：
- 不存在双方都可以使用的相同加密套件- 尽管存在这样的加套件，但是有一方或双方没有使用该加密套件的安全证书
SSLSocket 类的 getSupportedCipherSuites 方法返回一个字符串数组，它包含当 SSLSocket 对象所支持的加索套件组。SSLSocket 类的 setEnabledCipherSuites(String[] suites) 方法设置当前 SSLSocket 对象的可使用的加密套件组，可使用的加密件组应该是所支持的加密套件组的子集

以下代码仅仅启用了具有高加密强度的加密套件，这可以提高该通信端的安全性，禁止那些不支持强加密的通信端连接当前通信端

String[] strongSuites = { "SSL_RSA_WITH_RC4_128_MD5", "SSL_RSA_WITH_RC4_128_SHA", "SSL_RSA_WITH_3DES_EDE_CBC_SHA" }; sslSocket.setEnabledCipherSuites(strongSuites);

###### **5.2 处理握手结束事件**

SSL 握手需要花很长的时间，当 SSL 握手完成，会发出一个 HandshakeCompletedEvent 事件，该事件由 HandshakeCompletedListener 负责监听。SSLSocket 类的 addHandshakeCompletedListener 方法负责注册 HandshakeCompletedListener 监听器

下例为 SSLSocket 注册了 HandshakeCompletedListener

socket.addHandshakeCompletedListener { new HandshakeCompletedListener() { public void handshakeCompleted(HandshakeCompletedEvent event) { System.out.println("握手结束"); System.out.println("加密套件为:" + event.getCipherSuite()); System.out.println("会话为:" + event.getSession()); System.out.println("通信对方为:" + event.getSession().getPeerHost()); } }); }

###### **5.3 管理 SSL 会话**

一个客户程序可能会向一个服务器的同一个端口打开多个安全套接字。如果对于每一安全连接都进行 SSL 握手，就会大大降低通信效率。为了提高安全通信的效率，SSL 协议允许多个 SSLSocket 共享同一个 SSL 会话。在同一个会话中，只有第一个打开的 SSLSocket 要进行 SSL 握手，负责生成密钥以及交换密钥，其余的 SSLSocket 都共享密钥信息。在一段合理的时间范围内，如果客户程序向一个服务器的同一个端口打开多个安全套接字，JSSE 就会自动重用会话

SSLSocket 的 getSession 方法返回 SSLSocket 所属的会话。SSLSocket 的 setEnableSessionCreation(boolean flag) 方法决定 SSLSocket 是否允许创建新的会话。flag 的默认值为 true。如果 flag 参数为 true，那么对于新创建的 SSLSocket，如果当前已经有可用的会话，就直接加入该会话，如果没有可用的会话，就创建一个新的会话。如果 flag 为 false 参数，那么对于新创建的 SSLSocket，如果当前已经有可用的会话，就直接加入该会话，如果没有可用的会话，那么该 SSLSocket 无法与对方进行安全通信

SSLSocket的 startHandshake 方法显式地执行一次 SSL 握手，该方法具有以下用途：
- 使得会话使用新的密钥- 使得会话使用新的加密套件- 重新开始一个会话。为了保证不重用原先的会话，应该先将原先的会话失效、、
socket.getSession().invalidate(); socket.startHandshake();

###### **5.4 客户端模式**

多数情况下客户端无须向服务器证实自己的身份，因此当一个通信端无须向对方证实自己身份时，就称它处于客户模式，否则称它处于服务器模式。通信双方只能有一方处于服务器模式，另一方则处于客户模式

SSLSocket 的 setUseClientMode(boolean mode) 方法被用来设置客户模式或者服务器模式。如果 mode 参数为 true，就表示处于客户模式，即无须向对方证实自己的身份；如果 mode 为 false，就表示处于服务器模式，即需要向对方证实自己的身价

当 SSL 初始握手已经开始，就不允许再调用 SSLSocket 的 seUseClientMode(boolean mode) 方法，否则会导致异常

当 SSLSocket 处于服务器模式，还可以通过以下方法来决定是否要求对方提供身份认证：
- setWantClientAuth(boolean want):：当 want 参数为 true 时，表示希望对方提供身份认证。如果对方未出示安全证书，则连接不会中断，通信可继续进行 setNeedClientAuth(boolean need)：当 need 参数为 true 时，表示要求对方必须提供身份认证。如果对方未出示安全证书，则连接中断，通信无法继续
##### **6. SSLServerSocket类**

SSLServerSocket 类是 ServerSocket 类的子类，因此两者的用法有许多相似之处。此外，SSLServerSocket 类还具有与安全通信有关的方法，这些方法与 SSLSocket 类中的同名方法具有相同的作用

##### **7. SSLEngine 类**

SSLEngine 类与 SocketChannel 类联合使用，就能实现非阻塞的安全通信。SSLEngine 类封装了与安全通信有关的细节，把应用程序发送的应用数据打包为网络数据，打包指对应用数据进行加密，加入 SSL 握手数据，把它变为网络数据。SSLEngine 类还能把接收的网络数据展开为应用数据，展开指对网络数据解密，并且去除其中的 SSL 握手数据，从而还原为应用程序可以处理的应用数据。SSLEngine 类的 wrap 方法负责打包应用数据，unwrap 方法负责展开网络数据

public class SSLEngineDemo { private static boolean logging = true; private SSLContext sslc; private SSLEngine clientEngine; //客户端Engine private ByteBuffer clientOut; //存放客户端发送的应用数据 private ByteBuffer clientIn; //存放客户端接收到的应用数据 private SSLEngine serverEngine; //服务器端Engine private ByteBuffer serverOut; //存放服务器端发送的应用数据 private ByteBuffer serverIn; //存放服务器端接收到的应用数据 private ByteBuffer cTOs;//存放客户端向服务器端发送的网络数据 private ByteBuffer sTOc;//存放服务器向客户海发送的网络数据 //设置密钥库文件和信任库文件以及口令 private static String keyStoreFile = "test.keystore"; private static String trustStorefile = "test.keystore"; private static String passphrase = "123456"; public static void main(String args[]) throws Exception { SSLEngineDemo demo = new SSLEngineDemo(); demo.runDemo(); } /**初始化SSLContext*/ public SSLEngineDemo() throws Exception { KeyStore ks = KeyStore.getInstance("JKS"); KeyStore ts = KeyStore.getInstance("JKS"); char[] password = passphrase.toCharArray(); ks.load(new FileInputStream(keyStoreFile), password); ts.load(new FileInputStream(trustStoreFile), password); KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509"); kmf.init(ks, password); TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509"); tmf.init(ts); SSLContext sslCtx = SSLContext.getInstance("TLS"); sslCtx.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null); sslc = sslCtx; } private void runDemo() throws Exception { boolean dataDone = false; /*创建客户端以及服务器端的SSLEngine*/ serverEngine = sslc.createSSLEnqine(); serverEngine.setUseClientMode(false); serverEngine.setNeedClientAuth(true); clientEngine = sslc.createSSLEngine("client", 80); clientEngine.setUseClientMode(true); /*创建客户端以及服务器的应用冲区和网络缓冲区*/ SSLSession session = clientEngine.getsSession(); int appBufferMax = session.getApplicationBufferSize(); int netBufferMax = session.getPacketBufferSize(); clientIn = ByteBuffer.allocate(appBufferMax + 50); serverIn = ByteBuffer.allocate(appBufferMax + 50) cTOs = ByteBuffer.allocateDirect(netBufferMax); sTOc = ByteBuffer.allocateDirect(netBufferMax); clientOut = ByteBuffer.wrap("Hi Server, I'm Client".getBytes()); serverOut = ByteBuffer.wrap("Hello Client, I'm Server".getBytes()); SSLEngineResult clientResult; SSLEngineResult serverResult; while (!isEnqineClosed(clientEngine) || !isEngineClosed(serverEngine)) { log("=================="); //客户端打包应用数据 clientResult = clientEngine.wrap(clientOut, cTOs); log("client wrap:", clientResult); //完成握手任务 runDelegatedTasks(clientResult, clientEngine); //服务器端打包应用数据 serverResult = serverEngine.wrap(serverOut, sTOc); log("server wrap:", serverResult); //完成握手任务 runDelegatedTasks(serverResult, serverEngine); cTOs.flip(); sTOc.flip(); log("---------------"); //客户端展开网络数据 clientResult = clientEngine.unwrap(sTOc, clientIn); log("client unwrap:", clientResult); //完成握手任务 runDelegatedTasks(clientResult, clientEngine); //服务器端展开网络数据 serverResult = serverEngine.unwrap(cTOs, serverIn); log("server unwrap:", serverResult); //完成握手任务 runDeleqatedTasks(serverResult, serverEngine); cTOs.compact(); sTOc.compact(); if (!dataDone &amp;&amp; (clientOut.limit() == serverIn.position()) &amp;&amp; (serverOut,limit()=m clientIn.position())) { checkTransfer(serverOut, clientIn); checkTransfer(clientOut, serverIn); log("\tClosing clientEngine's *OUTBOUND*..."); clientEngine.closeOutbound(); dataDone = true; } } } /**当SSLEngine的输出与输入都关闭时，意味着SSLEngine被关闭*/ private static boolean isEngineClosed(SSLEngine engine) { return(engine.isOutboundDone() &amp;&amp; engine.isInboundDone()); } /**执行SSL握手任务*/ private static void runDelegatedTasks(SSLEngineResult result, SSLEngine engine) throws Exception { if(result.getHandshakeStatus() == HandshakeStatus.NEED_TASK) { Runnable runnable; while((runnable = engine.getDelegatedTask()) != null) { log("\trunning delegated task..."); runnable.run(); } HandshakeStatus hsStatus = engine.getHandshakeStatus(); if(hsStatus == HandshakeStatus.NEED_TASK) { throw new Exception("handshake shouldn't need additional tasks"); } log("\tnew HandshakeStatus:" + hsStatus); } } /**判断两个缓冲区内容是否相同*/ private static void checkTransfer(ByteBuffer a, ByteBuffer b) throws Exception { a.flip(); b.flip(); if(!a.equals(b)) { throw new Exception("pata didn't transfer cleanly"); } else { log("\tData transferred cleanly"); } a.position(a.limit()); b.position(b.limit()); a.limit(a.capacity()); b.limit(b.capacity()); } private static boolean resultOnce = true; /**输出日志,打印SSLEngineResult的结果*/ private static void log(String str, SSLEngineResult result) { if(resultOnce) { resultOnce = false; System.out.println("The format of the SSLEngineResult is: \n" +"\t\"getStatus() / getHandshakeStatus()\”+\n" +"\t\"bytesConsumed() / bytesProduced()\"\n"); } HandshakeStatus hsStatus = result.getHandshakeStatus(); log(str + result,getStatus() + "/" + hsStatus + "," + result,bytesConsumed() + "/" + result.bytesProduced() + " bytes"); if (hsStatus == HandshakeStatus.FINISHED) { log("\t...ready for application data"); } } /**输出日志*/ private static void log(String str) { System.out.printin(str); } }



### ****3****|****0******创建基于 SSL 的安全服务器和安全客户**

public class EchoServer { private int port = 8000; private SSLServerSocket serverSocket; public EchoServer() throws Exception { //输出跟踪日志 SSLContext context = createSSLContext(); SSLServerSocketFactory factory = context.getServerSocketFactory(); serverSocket = (SSLServerSocket)factory.createServerSocket(poxt); String[] supported = serverSocket.getSupportedCipherSuites(); serverSocket.setEnabledCipherSuites(supported); } public SSLContext createSSLContext() throws Exception { //服务器用于证实自己身份的安全证书所在的密钥库 String keyStoreFile = "test.keystore"; String passphrase = "123456"; KeyStore ks = KeyStore.getInstance("JKS"); char[] password = passphrase.toCharArray(); ks.load(new FileInputStream(keyStoreFile), password); KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509"); kmf.init(ks, password); SSLContext sslContext = SSLContext.getInstance("SSL"); sslContext.init(kmf.getKeyManagers(), null, null); //当要求客户端提供安全证书时，服务器端可创建TrustManagerFactory, //并由它创建TrustManager,TrustManger根据与之关联的KeyStore中的信息 //决定是否相信客户提供的安全证书 //客户端用于证实自己身份的安全证书所在的密钥库 //String trustStorefile = "test.keystore"; //KeyStore ts = KeyStore.getInstance("JKS"); //ts.load(new FileInputStream(trustStoreFile), password); //TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509"); //tmf.init(ts); //sslContext.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null); return sslContext; } private PrintWriter getWriter(Socket socket) throws IOException { OutputStream socketOut = socket.getOutputStream(); return new PrintWriter(socketOut, true); } private BufferedReader getReader(Socket socket) throws IOException { InputStream socketIn = socket.getInputstream(); return new BufferedReader(new InputStreamReader(socketIn)); } public void service() { while (true) { Socket socket = null; try { //等特客户连接 socket = serverSocket.accept(); BufferedReader br = getReader(socket); PrintWriter pw = getWriter(socket); String msg = null; while ((msg = br.readLine()) != null) { System.out.println(msg); if (msg.equals("bye")) { break; } } } catch (IOException e) { e.printStackTrace(); } finally { try { if(socket != null) socket.close(); //断开连接 } catch (IOException e) { e.printStackTrace(); } } } } public static void main(String args[]) throws Exception { new EchoServer().service(); } }

public class EchoClient { private String host = "localhost"; private int port = 8000; private SSLSocket socket; public EchoClient() throws IOException { SSLContext context = createSSLContext(); SSLSocketFactory factory = context.getSocketFactory(); socket = (SSLSocket)factory.createSocket(host,port); Stringl] supported = socket.getSupportedCipherSuites(); socket.setEnabledCipherSuites(supported); } public SSLContext createSSLContext() throws Exception { String passphrase = "123456"; char[] password = passphrase.toCharArray(); //设置客户端所信任的安全证书所在的密钥库 String trustStoreFile = "test.keystore"; KeyStore ts = KeyStore.getInstance("JKS"); ts.load(new FileInputStream(trustStoreFile), password)); TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509"); tmf.init(ts); SSLContext sslContext = SSLContext.getInstance("SSL"); sslContext.init(null, tmf.getTrustManagers(), null); return sslContext; } public static void main(String args[]) throws IOException { new EchoClient().talk(); } public void talk()throws IOException { try { BufferedReader br = getReader(socket); PrintWriter pw = getWriter(socket); BufferedReader localReader = new BufferedReader(new InputStreamReader(System.in)); String msg = null; while((msg = localReader.readLine()) != null) { pw.println(msg); System.out.println(br.readline()); if(msg.equals("bye")) { break; } } } catch(IOException e) { e.printStackTrace(); } finally { try { if(socket != null) socket.close(); //断开连接 } catch (IOException e) { e.printStackTrace(); } } } private PrintWriter getWriter(Socket socket) throws IOException { OutputStream socketOut = socket.getoutputstream(); return new PrintWriter(socketOut, true); } private BufferedReader getReader(Socket socket) throws IOException { InputStream socketIn = socket.getInputstream(); return new BufferedReader(new InputStreamReader(socketIn)); } }
