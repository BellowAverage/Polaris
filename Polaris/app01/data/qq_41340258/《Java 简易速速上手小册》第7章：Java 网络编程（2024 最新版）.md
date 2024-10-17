
--- 
title:  《Java 简易速速上手小册》第7章：Java 网络编程（2024 最新版） 
tags: []
categories: [] 

---
<img src="https://img-blog.csdnimg.cn/direct/200b2986fdc545e6918ec6f9f2cbcceb.png#pic_center" alt="在这里插入图片描述">



#### 文章目录
- - <ul><li>- - - - - - - - - - - 


## 7.1 网络基础和 Java 中的网络 - 揭开神秘的面纱

在这个章节，我们将像是揭开一个神秘世界的面纱，探索网络通信的基础知识，并了解如何在Java中应用这些知识来建立连接和进行数据交换。

### 7.1.1 基础知识
-  **IP地址**：每台连接到网络的设备都有一个唯一的IP地址，用于标识设备在网络上的位置，类似于现实世界中的邮寄地址。 -  **端口号**：端口号用于标识设备上的特定程序，允许一个IP地址提供多种不同的服务。想象一下，一个大楼（IP地址）有多扇门（端口号），每扇门后都是不同的服务。 -  **TCP和UDP**：TCP（传输控制协议）提供了一种可靠的数据传输方式，确保数据完整无误地从源传到目的地；而UDP（用户数据报协议）则是一种简单的协议，不保证数据的可靠传输，但在某些情况下能提供更快的数据传输速度。 -  **Socket编程**：Socket是网络编程的基石，提供了建立TCP连接和数据传输的方法。在Java中，通过`java.net`包中的`Socket`类和`ServerSocket`类，我们可以轻松实现网络通信。 
### 7.1.2 重点案例：实现一个简单的聊天程序

我们将创建一个简单的聊天程序，其中包含一个服务器和一个客户端，演示基于TCP的Socket通信。

**服务器端**:

```
import java.io.*;
import java.net.*;

public class ChatServer {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(5555);
        System.out.println("Server is waiting for client...");
        Socket clientSocket = serverSocket.accept();
        PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        
        String inputLine;
        while ((inputLine = in.readLine()) != null) {<!-- -->
            System.out.println("Client says: " + inputLine);
            out.println("Echo: " + inputLine);
        }
    }
}

```

**客户端**:

```
import java.io.*;
import java.net.*;

public class ChatClient {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        Socket socket = new Socket("localhost", 5555);
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

        String userInput;
        while ((userInput = stdIn.readLine()) != null) {<!-- -->
            out.println(userInput);
            System.out.println("Server response: " + in.readLine());
        }
    }
}

```

### 7.1.3 拓展案例 1：使用 UDP 进行消息广播

除了TCP，我们还可以使用UDP进行数据传输。下面是一个简单的使用UDP进行消息广播的示例。

**广播消息**:

```
import java.net.*;

public class UdpBroadcast {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        DatagramSocket socket = new DatagramSocket();
        byte[] buf = "Hello, UDP!".getBytes();
        InetAddress address = InetAddress.getByName("255.255.255.255");
        DatagramPacket packet = new DatagramPacket(buf, buf.length, address, 4445);
        socket.send(packet);
        socket.close();
    }
}

```

### 7.1.4 拓展案例 2：建立一个简单的 Web 服务器

使用Java的`ServerSocket`，我们可以建立一个简单的Web服务器，响应HTTP请求。

```
import java.io.*;
import java.net.*;

public class SimpleWebServer {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(8080);
        while (true) {<!-- -->
            Socket clientSocket = serverSocket.accept();
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            out.println("HTTP/1.1 200 OK");
            out.println("Content-Type: text/html");
            out.println("\r\n");
            out.println("&lt;h1&gt;Hello, World!&lt;/

h1&gt;");
            clientSocket.close();
        }
    }
}

```

通过这些案例，我们可以看到网络编程并不是什么遥不可及的技术。无论是实现基于TCP的聊天程序，使用UDP进行数据广播，还是建立一个简单的Web服务器，Java都为我们提供了强大的工具。现在，拿起你的工具，开始在Java的网络世界中探险吧！

<img src="https://img-blog.csdnimg.cn/direct/af5098958fd548c09f2509060ce6ecc8.png#pic_center" alt="在这里插入图片描述" width="400">

## 7.2 创建客户端和服务器 - 构建沟通的桥梁

在Java网络编程的旅程中，创建客户端和服务器是基本而关键的一步，就像是在两座孤岛之间构建沟通的桥梁。客户端和服务器之间的交流基础是建立在网络协议之上的，而TCP/IP协议是最常用的协议之一，它能够确保数据的可靠传输。

### 7.2.1 基础知识
-  **Socket**：在Java中，Socket是实现网络通信的核心，客户端通过Socket连接到服务器，服务器接受客户端的连接请求来建立连接。 -  **ServerSocket**：在服务器端，ServerSocket用于监听来自客户端的连接请求。 -  **TCP连接的建立**：客户端通过指定服务器的IP地址和端口号发起连接请求，服务器监听到请求后，通过接受请求来建立连接。 
### 7.2.2 重点案例：实现文件传输系统

假设我们要构建一个简单的文件传输系统，允许客户端向服务器上传文件。

**服务器端**:

```
import java.io.*;
import java.net.*;

public class FileTransferServer {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(6666);
        System.out.println("Server is running and waiting for file...");

        Socket socket = serverSocket.accept();
        DataInputStream dis = new DataInputStream(socket.getInputStream());
        FileOutputStream fos = new FileOutputStream("received_file.txt");
        byte[] buffer = new byte[4096];
        
        int filesize = 15123; // Send file size in separate msg
        int read = 0;
        int totalRead = 0;
        int remaining = filesize;
        while((read = dis.read(buffer, 0, Math.min(buffer.length, remaining))) &gt; 0) {<!-- -->
            totalRead += read;
            remaining -= read;
            System.out.println("read " + totalRead + " bytes.");
            fos.write(buffer, 0, read);
        }
        
        fos.close();
        dis.close();
        System.out.println("File received!");
    }
}

```

**客户端**:

```
import java.io.*;
import java.net.*;

public class FileTransferClient {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        Socket socket = new Socket("localhost", 6666);
        FileInputStream fis = new FileInputStream("to_send_file.txt");
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        byte[] buffer = new byte[4096];
        
        while (fis.read(buffer) &gt; 0) {<!-- -->
            dos.write(buffer);
        }
        
        fis.close();
        dos.close();
        System.out.println("File sent!");
    }
}

```

### 7.2.3 拓展案例 1：构建简单的聊天应用

我们可以通过Socket编程构建一个更实用的应用，比如一个简单的聊天应用，允许客户端和服务器互发消息。

**聊天服务器**

服务器端的任务是接受客户端连接，并转发客户端发送的消息到所有其他已连接的客户端。

```
import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

public class ChatServer {<!-- -->
    private static final int PORT = 6666;
    private static final List&lt;ClientHandler&gt; clients = new CopyOnWriteArrayList&lt;&gt;();
    private static ExecutorService pool = Executors.newCachedThreadPool();

    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(PORT);

        System.out.println("Chat Server is listening on port " + PORT);

        while (true) {<!-- -->
            Socket clientSocket = serverSocket.accept();
            System.out.println("Accepted new connection from " + clientSocket);
            ClientHandler clientHandler = new ClientHandler(clientSocket, clients);
            clients.add(clientHandler);
            pool.execute(clientHandler);
        }
    }
}

class ClientHandler implements Runnable {<!-- -->
    private Socket clientSocket;
    private List&lt;ClientHandler&gt; clients;
    private PrintWriter out;
    private BufferedReader in;

    public ClientHandler(Socket socket, List&lt;ClientHandler&gt; clients) throws IOException {<!-- -->
        this.clientSocket = socket;
        this.clients = clients;
        this.out = new PrintWriter(clientSocket.getOutputStream(), true);
        this.in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    @Override
    public void run() {<!-- -->
        try {<!-- -->
            String message;
            while ((message = in.readLine()) != null) {<!-- -->
                broadcastMessage(message);
            }
        } catch (IOException e) {<!-- -->
            System.out.println("Error in ClientHandler: " + e.getMessage());
        } finally {<!-- -->
            try {<!-- -->
                in.close();
                out.close();
                clientSocket.close();
            } catch (IOException e) {<!-- -->
                e.printStackTrace();
            }
        }
    }

    private void broadcastMessage(String message) {<!-- -->
        for (ClientHandler aClient : clients) {<!-- -->
            if (aClient != this) {<!-- -->
                aClient.out.println(message);
            }
        }
    }
}

```

**聊天客户端**

客户端的任务是连接到服务器，发送自己的消息，并接收从服务器转发的其他客户端的消息。

```
import java.io.*;
import java.net.*;

public class ChatClient {<!-- -->
    private static final String SERVER_IP = "127.0.0.1";
    private static final int SERVER_PORT = 6666;

    public static void main(String[] args) throws IOException {<!-- -->
        Socket socket = new Socket(SERVER_IP, SERVER_PORT);

        BufferedReader keyboardInput = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        // Create a new thread to read messages from the server
        new Thread(new Runnable() {<!-- -->
            public void run() {<!-- -->
                try {<!-- -->
                    String serverMessage;
                    while ((serverMessage = in.readLine()) != null) {<!-- -->
                        System.out.println("Server says: " + serverMessage);
                    }
                } catch (IOException e) {<!-- -->
                    System.out.println("Connection to server broken.");
                }
            }
        }).start();

        // Read messages from the keyboard and send them to the server
        System.out.println("Enter your message: ");
        String userInput;
        while ((userInput = keyboardInput.readLine()) != null) {<!-- -->
            out.println(userInput);
        }
    }
}

```

在这个聊天应用中，服务器能够接收多个客户端连接，并将任一客户端发来的消息广播给所有其他客户端。客户端可以发送消息给服务器，服务器则将这些消息转发给所有其他已连接的客户端。这样，就实现了一个基础的多人聊天室功能。

### 7.2.4 拓展案例 2：多客户端支持的服务器

要让服务器能够同时处理多个客户端，我们可以为每个连接创建一个新的线程来处理。

**服务器端**:

```
public class MultiClientServer {<!-- -->
    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(6666);
        System.out.println("Server is running...");

        while (true) {<!-- -->
            Socket socket = serverSocket.accept();
            new Thread(new ClientHandler(socket)).start();
        }
    }
}

class ClientHandler implements Runnable {<!-- -->
    private Socket socket;

    public ClientHandler(Socket socket) {<!-- -->
        this.socket = socket;
    }

    @Override
    public void run() {<!-- -->
        // 处理客户端请求
    }
}

```

通过实现这些案例，你已经学会了如何在Java中创建客户端和服务器，以及如何通过Socket进行基本的网络通信。无论是实现文件传输系统、构建简单的聊天应用，还是支持多客户端的服务器，这些基础知识都将为你打开网络编程的大门，帮助你构建更复杂和强大的网络应用。

<img src="https://img-blog.csdnimg.cn/direct/bcc93459c6bf49c9aefce7c28fef9bd1.png#pic_center" alt="在这里插入图片描述" width="400">

## 7.3 高效网络编程技巧 - 提升你的网络魔法效率

在Java网络编程的世界中，掌握一些高效的技巧可以大大提升你的应用性能和用户体验。就像一个熟练的魔法师，通过精细的魔法控制和策略，可以在战斗中取得压倒性的胜利。让我们一起探索如何成为网络编程领域的高级魔法师。

### 7.3.1 基础知识
-  **非阻塞I/O（NIO）**：Java NIO是一种基于通道(Channel)和缓冲区(Buffer)的I/O方式，它可以让你非阻塞地读写数据，提升I/O操作的效率。 -  **I/O多路复用**：这是一种允许单个线程同时监控多个I/O通道的技术，如果某个通道准备好了I/O操作，系统就会通知线程。这减少了线程的数量和上下文切换的开销。 -  **线程池**：使用线程池可以避免为每个请求创建新线程的开销，复用线程资源，提高应用性能。 -  **连接池**：网络应用中，频繁地建立和关闭连接会造成资源的浪费，使用连接池可以复用已经建立的连接。 
### 7.3.2 重点案例：基于 NIO 的聊天服务器

我们将构建一个基于Java NIO的聊天服务器，这个服务器可以非阻塞地处理多个客户端的连接和消息传输。

**聊天服务器**:

```
import java.nio.*;
import java.nio.channels.*;
import java.net.*;
import java.util.*;

public class ChatServer {<!-- -->
    public void startServer() throws IOException {<!-- -->
        Selector selector = Selector.open();
        ServerSocketChannel serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(5555));
        serverChannel.configureBlocking(false);
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);

        while (true) {<!-- -->
            selector.select(); // 阻塞，直到至少有一个通道在你注册的事件上就绪了
            Set&lt;SelectionKey&gt; selectedKeys = selector.selectedKeys();
            Iterator&lt;SelectionKey&gt; iter = selectedKeys.iterator();

            while (iter.hasNext()) {<!-- -->
                SelectionKey key = iter.next();

                if (key.isAcceptable()) {<!-- -->
                    register(selector, serverChannel);
                }

                if (key.isReadable()) {<!-- -->
                    broadcast(selector, key);
                }

                iter.remove();
            }
        }
    }

    private void register(Selector selector, ServerSocketChannel serverChannel) throws IOException {<!-- -->
        SocketChannel client = serverChannel.accept();
        client.configureBlocking(false);
        client.register(selector, SelectionKey.OP_READ);
    }

    private void broadcast(Selector selector, SelectionKey key) throws IOException {<!-- -->
        SocketChannel client = (SocketChannel) key.channel();
        ByteBuffer buffer = ByteBuffer.allocate(256);
        client.read(buffer);
        String message = new String(buffer.array()).trim();

        for (SelectionKey k : selector.keys()) {<!-- -->
            Channel target = k.channel();
            if (target instanceof SocketChannel &amp;&amp; target != client) {<!-- -->
                ((SocketChannel) target).write(ByteBuffer.wrap(message.getBytes()));
            }
        }
    }

    public static void main(String[] args) throws IOException {<!-- -->
        new ChatServer().startServer();
    }
}

```

### 7.3.3 拓展案例 1：使用线程池处理 Socket 连接

在多用户网络应用中，使用线程池来处理Socket连接可以大大提升性能。

```
import java.net.*;
import java.util.concurrent.*;

public class ThreadPoolEchoServer {<!-- -->
    private static final int PORT = 5555;
    private static final ExecutorService pool = Executors.newFixedThreadPool(10);

    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("Echo server is running.");

        while (true) {<!-- -->
            Socket clientSocket = serverSocket.accept();
            pool.execute(new EchoClientHandler(clientSocket));
        }
    }
}

class EchoClientHandler implements Runnable {<!-- -->
    private Socket clientSocket;

    public EchoClientHandler(Socket socket) {<!-- -->
        this.clientSocket = socket;
    }

    @Override


    public void run() {<!-- -->
        // 处理客户端请求
    }
}

```

### 7.3.4 拓展案例 2：优化长连接的性能

在需要维护长时间连接的应用中，合理管理这些连接是提升性能的关键。

优化长连接的性能是网络编程中的一个常见需求，尤其是在需要维护与客户端持续交互的应用中。以下是一个使用Java实现的简单心跳机制和连接池管理来优化长连接性能的示例。

**心跳机制：**心跳机制（Heartbeat）用于维持客户端与服务器之间的长连接，通过定期发送轻量级的心跳消息来确认连接的活性。

**服务器端示例**:

```
import java.io.*;
import java.net.*;
import java.util.concurrent.*;

public class HeartbeatServer {<!-- -->
    private static final int PORT = 5555;
    private static final ExecutorService pool = Executors.newCachedThreadPool();

    public static void main(String[] args) throws IOException {<!-- -->
        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("Server started, waiting for connections...");

        while (true) {<!-- -->
            Socket clientSocket = serverSocket.accept();
            pool.execute(new ClientHandler(clientSocket));
        }
    }

    static class ClientHandler implements Runnable {<!-- -->
        private final Socket clientSocket;

        public ClientHandler(Socket socket) {<!-- -->
            this.clientSocket = socket;
        }

        @Override
        public void run() {<!-- -->
            try (DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                 DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {<!-- -->
                
                while (true) {<!-- -->
                    String message = dis.readUTF(); // Read heartbeat message
                    if ("HEARTBEAT".equals(message)) {<!-- -->
                        dos.writeUTF("ACK"); // Acknowledge heartbeat
                    } else {<!-- -->
                        // Handle other messages
                    }
                }
            } catch (IOException e) {<!-- -->
                System.out.println("Client disconnected.");
            }
        }
    }
}

```

**客户端示例**:

```
import java.io.*;
import java.net.*;

public class HeartbeatClient {<!-- -->
    public static void main(String[] args) {<!-- -->
        try (Socket socket = new Socket("localhost", 5555);
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
             DataInputStream dis = new DataInputStream(socket.getInputStream())) {<!-- -->
            
            while (true) {<!-- -->
                dos.writeUTF("HEARTBEAT"); // Send heartbeat message
                String response = dis.readUTF(); // Wait for server acknowledgment
                if ("ACK".equals(response)) {<!-- -->
                    System.out.println("Heartbeat acknowledged by server.");
                }
                Thread.sleep(5000); // Send heartbeat every 5 seconds
            }
        } catch (IOException | InterruptedException e) {<!-- -->
            System.out.println("Error: " + e.getMessage());
        }
    }
}

```

**连接池管理**

在需要维护多个长连接时，使用连接池可以提高资源的复用率和应用性能。虽然Java标准库中没有直接支持连接池的API，但我们可以通过第三方库如Apache Commons Pool或HikariCP来实现连接池管理。以下是概念性描述，具体实现将依赖于选用的连接池库：

```
// 创建连接池配置
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:mysql://localhost:3306/yourdatabase");
config.setUsername("user");
config.setPassword("password");
config.addDataSourceProperty("cachePrepStmts", "true");
config.addDataSourceProperty("prepStmtCacheSize", "250");
config.addDataSourceProperty("prepStmtCacheSqlLimit", "2048");

// 实例化连接池
HikariDataSource dataSource = new HikariDataSource(config);

// 使用连接池获取连接
try (Connection conn = dataSource.getConnection();
     PreparedStatement stmt = conn.prepareStatement("your SQL query")) {<!-- -->
    // 处理数据库操作
} catch (SQLException e) {<!-- -->
    // 异常处理
}

```

通过这些技术，你可以有效地管理长连接，提升应用的性能和稳定性。心跳机制确保连接的活性，而连接池管理则提高了资源的利用率和响应速度。这些高级技巧将在网络编程中赋予你更大的力量和灵活性。
