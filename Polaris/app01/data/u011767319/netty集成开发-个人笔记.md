
--- 
title:  netty集成开发-个人笔记 
tags: []
categories: [] 

---
### 导包

>  
 本人项目是用web形式启用netty的（看个人需求） 


```
&lt;dependency&gt;
    &lt;groupId&gt;org.apache.dubbo&lt;/groupId&gt;
    &lt;artifactId&gt;dubbo-spring-boot-starter&lt;/artifactId&gt;
&lt;/dependency&gt;

```

>  
 单独引入使用 


```
&lt;dependency&gt;
	&lt;groupId&gt;io.netty&lt;/groupId&gt;
	&lt;artifactId&gt;netty-all&lt;/artifactId&gt;
	&lt;version&gt;4.1.63.Final&lt;/version&gt;
&lt;/dependency&gt;

```

### 项目代码

>  
 启动类 


```
package com.ronrun.communication.config.nertty;

import com.ronrun.common.util.LogPrintUtil;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import lombok.Data;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;

@Component
@Data
public class NettyServer {<!-- -->

	//netty服务绑定端口
    private int port = 9999;

    // 构造方法少了会报错
    public NettyServer() {<!-- -->
    }

    /**
     * 描述：启动Netty Websocket服务器
     */
    @PostConstruct //这个注解会随着类加载而加载 就不需要使用 ServletContextListener（服务上下文监听了）
    public void start() throws Exception {<!-- -->
    	//EventLoopGroup事件循环组-NioEventLoopGroup非阻塞的事件循环组
    	//boss组（老板） 用于处理ServerSocketChannel的数据
        NioEventLoopGroup bossGroup = new NioEventLoopGroup();
        //worker组（工人） 用于处理SocketChannel的数据
        NioEventLoopGroup workerGroup = new NioEventLoopGroup();
        //netty服务启动类
        ServerBootstrap serverBootstrap = new ServerBootstrap();
        serverBootstrap.group(bossGroup, workerGroup) //boss辅助客户端的tcp连接请求  worker负责与客户端之前的读写操作
                .channel(NioServerSocketChannel.class) //配置客户端的channel类型-一般使用非阻塞的管道
                .childHandler(new NettyServerInitialzer()); //绑定I/O事件的处理类,WebSocketChildChannelHandler中定义

		//sync 一定要开启同步，否则会在nio机制的影响，netty还没启动完，就先执行其他代码
        ChannelFuture sync = serverBootstrap.bind(port).sync();
        //检查ChannelFuture是否启动完毕
        if (sync.isSuccess()) {<!-- -->
        	//忽略这个是我写静态日志调用类
            LogPrintUtil.logRes("Netty Websocket服务器启动完成, ms:已绑定端口&lt;{}&gt;阻塞式等候客户端连接",port);
        }
    }

}


```

>  
 添加netty服务配置 


```
package com.ronrun.communication.config.nertty;

import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpServerCodec;
import io.netty.handler.codec.http.websocketx.WebSocketServerProtocolHandler;
import io.netty.handler.timeout.IdleStateHandler;

/*
 * 功能描述:
 * 〈netty服务配置类〉
 *
 * @param null 1
 * @return :
 * @author : ljq-刘俊秦
 * @date : 2020/5/29 0029 下午 8:14
 */
public class NettyServerInitialzer extends ChannelInitializer&lt;SocketChannel&gt; {<!-- -->

    @Override
    protected void initChannel(SocketChannel socketChannel) throws Exception {<!-- -->

        //========================  支持http协议的 =========================
        ChannelPipeline pipeline = socketChannel.pipeline();
        // websocket 基于http协议，所以要有http编解码器
        pipeline.addLast(new HttpServerCodec());
        // 对httpMessage进行聚合，聚合成FullHttpRequest或FullHttpResponse
        // 几乎在netty中的编程，都会使用到此handler 1024*64=65536
        pipeline.addLast(new HttpObjectAggregator(65536));

        //========================  增加心跳支持 start =========================
        pipeline.addLast(new IdleStateHandler(8, 10, 12));
        //自定义心跳空闲检查
        pipeline.addLast(new HeartBaeatHandler());
        //========================  增加心跳支持 end =========================

        /*
         * websocket 服务处理协议，用于指定给客户端连接的访问路由：/ws
         * */
        pipeline.addLast(new WebSocketServerProtocolHandler("/ws"));


        //自定义
        pipeline.addLast(new ChatHandler());
    }

}


```

>  
 自定义心跳检测 


```
package com.ronrun.communication.config.nertty;

import com.ronrun.common.util.LogPrintUtil;
import io.netty.channel.Channel;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleStateEvent;

/**
 * 功能描述:
 * 〈心跳检测〉
 *
 * @author : ljq-刘俊秦
 * @return :
 * @date : 2020/6/2 0002 下午 8:09
 */

public class HeartBaeatHandler extends ChannelInboundHandlerAdapter {<!-- -->

    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object evt) throws Exception {<!-- -->
        Channel channel = ctx.channel();
        if (evt instanceof IdleStateEvent) {<!-- -->
            IdleStateEvent event = (IdleStateEvent) evt;
            switch (event.state()) {<!-- -->
                case READER_IDLE :
                    //进入读空闲，不做处理
                    LogPrintUtil.logRes("移除读空闲通道", channel.id().asLongText());
                    break;
                case WRITER_IDLE :
                    //进入写空闲不做处理
                    LogPrintUtil.logRes("移除写空闲通道", channel.id().asLongText());
                    break;
                case ALL_IDLE :
                    channel.close();
                    LogPrintUtil.logRes("移除读写空闲通道", channel.id().asLongText());
                    break;
            }
        }
    }
}



```

>  
 自定义聊天通道处理器 


```
package com.ronrun.communication.config.nertty;

import com.ronrun.common.util.LogPrintUtil;
import com.ronrun.communication.service.impl.NettyAllChannelServiceImpl;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;

public class ChatHandler extends SimpleChannelInboundHandler&lt;TextWebSocketFrame&gt; {<!-- -->

    @Override
    protected void channelRead0(ChannelHandlerContext channelHandlerContext, TextWebSocketFrame textWebSocketFrame) throws Exception {<!-- -->
        String content = textWebSocketFrame.text();
        String f_text = "服务器接收到的参数：" + content;
        LogPrintUtil.logRes(f_text);
        NettyAllChannelServiceImpl.sendAllStatic(new TextWebSocketFrame(f_text));
    }

    @Override
    public void handlerAdded(ChannelHandlerContext ctx) throws Exception {<!-- -->
        NettyAllChannelServiceImpl.addChannel(ctx.channel());
    }

    @Override
    public void handlerRemoved(ChannelHandlerContext ctx) throws Exception {<!-- -->
        //管道组会自动移除所以不需要解决
//        channels.remove(ctx.channel());
    }
}


```

>  
 简易的远程调用接口（duboo形式实现） 


```
package com.ronrun.communication.service.impl;

import com.ronrun.common.service.INettyAllChannelService;
import io.netty.channel.Channel;
import io.netty.channel.group.ChannelGroup;
import io.netty.channel.group.DefaultChannelGroup;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import io.netty.util.concurrent.GlobalEventExecutor;
import org.apache.dubbo.config.annotation.Service;

@Service
public class NettyAllChannelServiceImpl implements INettyAllChannelService {<!-- -->

    private static ChannelGroup channels = new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);

    public static void addChannel(Channel channel) {<!-- -->
        channels.add(channel);
    }

    public static void removeChannel(Channel channel) {<!-- -->
        channels.remove(channel);
    }

    public static void sendAllStatic(TextWebSocketFrame textWebSocketFrame) {<!-- -->
        channels.writeAndFlush(textWebSocketFrame);
    }

    @Override
    public boolean sendAll(String text) {<!-- -->
        //不能直接使用channels 需要调用静态自己分方法。否则会报错
        sendAllStatic(new TextWebSocketFrame(text));
        return true;
    }
}


```
