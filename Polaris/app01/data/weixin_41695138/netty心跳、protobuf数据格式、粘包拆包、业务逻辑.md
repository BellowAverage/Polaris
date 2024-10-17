
--- 
title:  netty心跳、protobuf数据格式、粘包拆包、业务逻辑 
tags: []
categories: [] 

---
### netty心跳、protobuf数据格式、粘包拆包、业务逻辑

参考了 和，结合自己的理解，整理了一下netty相关的功能
1. 引入依赖：
```
        &lt;dependency&gt;
            &lt;groupId&gt;io.netty&lt;/groupId&gt;
            &lt;artifactId&gt;netty-all&lt;/artifactId&gt;
        &lt;/dependency&gt;

        &lt;dependency&gt;
            &lt;groupId&gt;com.google.protobuf&lt;/groupId&gt;
            &lt;artifactId&gt;protobuf-java&lt;/artifactId&gt;
            &lt;version&gt;3.4.0&lt;/version&gt;
        &lt;/dependency&gt;

```
1. 定义好proto文件：SubscribeReq.proto SubscribeResp…proto
```
// 区分不同的protobuf版本，必须有
syntax = "proto2";
 
package netty;
// 生成的目标类的包路径
option java_package = "cn.ddlover.nettystudy.protobuf";
// 生成的目标类的名字
option java_outer_classname = "SubscribeReqProto";
 
message SubscribeReq{<!-- -->
    required int32 subReqID = 1;
    required string userName = 2;
    required string productName = 3;
    repeated string address = 4;
}

```

```
syntax = "proto2";
package netty;

option java_package = "cn.ddlover.nettystudy.protobuf";
option java_outer_classname = "SubscribeRespProto";

message SubscribeResp{<!-- -->
    required int32 subReqID = 1;
    required int32 respCode = 2;
    required string desc = 3;
}

```

有关idea整合protobug的相关内容，可以参考  3. 服务端

```

import cn.ddlover.nettystudy.protobuf.SubscribeReqProto;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.protobuf.ProtobufDecoder;
import io.netty.handler.codec.protobuf.ProtobufEncoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32FrameDecoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32LengthFieldPrepender;
import io.netty.handler.logging.LogLevel;
import io.netty.handler.logging.LoggingHandler;
import io.netty.handler.timeout.IdleStateHandler;
import java.util.concurrent.TimeUnit;

/**
 * 服务端
 */
public class SubReqServer {<!-- -->
    private static final int PORT = 9000;

    public static void main(String[] args) {<!-- -->
        bind(PORT);
    }

    private static void bind(int port) {<!-- -->
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        ServerBootstrap b = new ServerBootstrap();
        try {<!-- -->
            b.group(bossGroup, workerGroup)
                    .channel(NioServerSocketChannel.class)
                    .option(ChannelOption.SO_BACKLOG, 100)
                    .handler(new LoggingHandler(LogLevel.INFO))
                    .childHandler(new ChannelInitializer&lt;SocketChannel&gt;() {<!-- -->
                        @Override
                        protected void initChannel(SocketChannel socketChannel) throws Exception {<!-- -->
                            socketChannel.pipeline().addLast(new IdleStateHandler(5, 0, 0, TimeUnit.SECONDS));

                            //一对解码器
                            socketChannel.pipeline().addLast(new ProtobufVarint32FrameDecoder());
                            socketChannel.pipeline().addLast(new ProtobufDecoder(SubscribeReqProto.SubscribeReq.getDefaultInstance()));

                            //  一对解码器
                            socketChannel.pipeline().addLast(new ProtobufVarint32LengthFieldPrepender());
                            socketChannel.pipeline().addLast(new ProtobufEncoder());

                            socketChannel.pipeline().addLast(new BusinessServerHandler());  // 业务消息处理
                        }
                    });
            ChannelFuture future = b.bind(port).sync();
            future.channel().closeFuture().sync();
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }finally {<!-- -->
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }
}

```

```

import cn.ddlover.nettystudy.protobuf.SubscribeReqProto;
import cn.ddlover.nettystudy.protobuf.SubscribeRespProto;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;

public class BusinessServerHandler extends ChannelInboundHandlerAdapter {<!-- -->

    /** 空闲次数 */
    private int idle_count =1;
    /** 发送次数 */
    private int count = 1;

    /**
     * 超时处理
     * 如果5秒没有接受客户端的心跳，就触发;
     * 如果超过两次，则直接关闭;
     */
    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object obj) throws Exception {<!-- -->
        if (obj instanceof IdleStateEvent) {<!-- -->
            IdleStateEvent event = (IdleStateEvent) obj;
            if (IdleState.READER_IDLE.equals(event.state())) {<!-- -->
                //如果读通道处于空闲状态，说明没有接收到心跳命令
                System.out.println("已经5秒没有接收到客户端的信息了");
                if (idle_count &gt; 2) {<!-- -->
                    System.out.println("关闭这个不活跃的channel");
                    ctx.channel().close();
                }
                idle_count++;
            }
        } else {<!-- -->
            super.userEventTriggered(ctx, obj);
        }
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {<!-- -->
        SubscribeReqProto.SubscribeReq req = (SubscribeReqProto.SubscribeReq)msg;
        // 用张三来模拟是否是心跳的业务逻辑
        if ("张三".equals(req.getUserName())) {<!-- -->
            System.out.println("Server accept clietn subscribe req : ["+req.toString()+"]");
            ctx.writeAndFlush(resp(req.getSubReqID()));
            idle_count = 0;
        }else{<!-- -->
            System.out.println("处理非心跳的业务逻辑");
        }
    }

    /**
     *  把数据封装为 protobuf 类型
     * @param subReqID
     * @return
     */
    private SubscribeRespProto.SubscribeResp resp(int subReqID) {<!-- -->
        SubscribeRespProto.SubscribeResp.Builder builder = SubscribeRespProto.SubscribeResp.newBuilder();
        builder.setSubReqID(subReqID);
        builder.setRespCode(0);
        builder.setDesc("netty书籍下单成功，3天后将会送到你的住处");
        return builder. build();
    }

    /**
     *  处理异常信息
     * @param ctx
     * @param cause
     * @throws Exception
     */
    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {<!-- -->
        cause.printStackTrace();
        ctx.close();
    }
}

```

socketChannel.pipeline().addLast(new IdleStateHandler(5, 0, 0, TimeUnit.SECONDS)); 配置心跳相关的业务， //一对解码器 socketChannel.pipeline().addLast(new ProtobufVarint32FrameDecoder()); socketChannel.pipeline().addLast(new ProtobufDecoder(SubscribeReqProto.SubscribeReq.getDefaultInstance()));

// 一对解码器 socketChannel.pipeline().addLast(new ProtobufVarint32LengthFieldPrepender()); socketChannel.pipeline().addLast(new ProtobufEncoder()); 封装protobuf数据格式，并通过两次解码来处理拆包、粘包问题

```
/**
     * 超时处理
     * 如果5秒没有接受客户端的心跳，就触发;
     * 如果超过两次，则直接关闭;
     */
    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object obj) throws Exception {<!-- -->
        if (obj instanceof IdleStateEvent) {<!-- -->
            IdleStateEvent event = (IdleStateEvent) obj;
            if (IdleState.READER_IDLE.equals(event.state())) {<!-- -->
                //如果读通道处于空闲状态，说明没有接收到心跳命令
                System.out.println("已经5秒没有接收到客户端的信息了");
                if (idle_count &gt; 2) {<!-- -->
                    System.out.println("关闭这个不活跃的channel");
                    ctx.channel().close();
                }
                idle_count++;
            }
        } else {<!-- -->
            super.userEventTriggered(ctx, obj);
        }
    }

```

来判断心跳的次数
1. 客户端：
```

import cn.ddlover.nettystudy.protobuf.SubscribeRespProto;
import io.netty.bootstrap.Bootstrap;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.protobuf.ProtobufDecoder;
import io.netty.handler.codec.protobuf.ProtobufEncoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32FrameDecoder;
import io.netty.handler.codec.protobuf.ProtobufVarint32LengthFieldPrepender;

public class SubReqClient {<!-- -->
    private static final String HOST = "localhost";
    private static final int PORT = 9000;

    public static void main(String[] args) {<!-- -->
        connect(HOST, PORT);
    }

    private static void connect(String host, int port) {<!-- -->
        EventLoopGroup group = new NioEventLoopGroup();

        Bootstrap b = new Bootstrap();
        try {<!-- -->
            b.group(group).channel(NioSocketChannel.class)
                    .option(ChannelOption.TCP_NODELAY, true)
                    .handler(new ChannelInitializer&lt;SocketChannel&gt;() {<!-- -->
                        @Override
                        protected void initChannel(SocketChannel socketChannel) throws Exception {<!-- -->
                            socketChannel.pipeline().addLast(new ProtobufVarint32FrameDecoder());
                            socketChannel.pipeline().addLast(new ProtobufDecoder(SubscribeRespProto.SubscribeResp.getDefaultInstance()));
                            socketChannel.pipeline().addLast(new ProtobufVarint32LengthFieldPrepender());
                            socketChannel.pipeline().addLast(new ProtobufEncoder());
                            socketChannel.pipeline().addLast(new BusinessClientHandler());
                        }
                    });
            ChannelFuture f = b.connect(host, port).sync();
            f.channel().closeFuture().sync();
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }finally {<!-- -->
            group.shutdownGracefully();
        }
    }
}

```

```

import cn.ddlover.nettystudy.protobuf.SubscribeReqProto;
import cn.ddlover.nettystudy.protobuf.SubscribeRespProto;
import com.ruoyi.ruoyitest.tcp.netty02.threadtool.NettyThread;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import java.util.ArrayList;
import java.util.List;

public class BusinessClientHandler extends ChannelInboundHandlerAdapter {<!-- -->

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {<!-- -->
        for (int i =0;i&lt;10;i++) {<!-- -->
            ctx.write(subReq(i));
        }
        ctx.flush();
    }

    private SubscribeReqProto.SubscribeReq subReq(int i) {<!-- -->
        SubscribeReqProto.SubscribeReq.Builder builder = SubscribeReqProto.SubscribeReq.newBuilder();
        builder.setSubReqID(i);
        builder.setUserName("张三");
        builder.setProductName("Netty Book");
        List&lt;String&gt; address = new ArrayList&lt;&gt;();
        address.add("NanJing YuHuaTai");
        address.add("BeiJing LiuLiChang");
        address.add("ShenZhen HongShuLin");
        builder.addAllAddress(address);
        return builder.build();
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {<!-- -->
        SubscribeRespProto.SubscribeResp req = (SubscribeRespProto.SubscribeResp)msg;
        String desc = req.getDesc();
        int code = req.getRespCode();
        System.out.println("Receive server response : ["+ code + desc +"]");
        new Thread(new NettyThread(ctx, subReq(code + 1))).run();
    }


    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {<!-- -->
        cause.printStackTrace();
        ctx.close();
    }
}

```
1. 线程相关：
```

import cn.ddlover.nettystudy.protobuf.SubscribeReqProto;
import io.netty.channel.ChannelHandlerContext;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;

/**
 *  开启线程  来处理发送消息的任务
 */
@Slf4j
@Data
@AllArgsConstructor
public class NettyThread implements Runnable {<!-- -->

    private ChannelHandlerContext ctx;

    private SubscribeReqProto.SubscribeReq req;

    @Override
    public void run() {<!-- -->
        try {<!-- -->
            Thread.sleep(6000);
        } catch (InterruptedException e) {<!-- -->
            e.printStackTrace();
        }
        ctx.writeAndFlush(req);
    }

}


```
