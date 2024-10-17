
--- 
title:  idea整合 protobuf 
tags: []
categories: [] 

---1. 安装插件 <img src="https://img-blog.csdnimg.cn/575b2e0171a8485caef117ad03eea23d.png" alt="在这里插入图片描述"> 点击 file -&gt; setting -&gt; plugins -&gt; 搜索protobuf，安装即可。小编已经安装过了，因此才会出现 disable 按钮1. 引入依赖和build构建
```
        &lt;dependency&gt;
            &lt;groupId&gt;com.google.protobuf&lt;/groupId&gt;
            &lt;artifactId&gt;protobuf-java&lt;/artifactId&gt;
            &lt;version&gt;3.4.0&lt;/version&gt;
        &lt;/dependency&gt;

    &lt;build&gt;
        &lt;extensions&gt;
            &lt;extension&gt;
                &lt;groupId&gt;kr.motd.maven&lt;/groupId&gt;
                &lt;artifactId&gt;os-maven-plugin&lt;/artifactId&gt;
                &lt;version&gt;1.4.1.Final&lt;/version&gt;
            &lt;/extension&gt;
        &lt;/extensions&gt;
        &lt;plugins&gt;
            &lt;!-- Protobuf插件 --&gt;
            &lt;plugin&gt;
                &lt;groupId&gt;org.xolstice.maven.plugins&lt;/groupId&gt;
                &lt;artifactId&gt;protobuf-maven-plugin&lt;/artifactId&gt;
                &lt;version&gt;0.5.0&lt;/version&gt;
                &lt;configuration&gt;
                    &lt;protoSourceRoot&gt;${<!-- -->project.basedir}/src/main/proto&lt;/protoSourceRoot&gt;
                    &lt;protocArtifact&gt;
                        com.google.protobuf:protoc:3.1.0:exe:${<!-- -->os.detected.classifier}
                    &lt;/protocArtifact&gt;
                &lt;/configuration&gt;
                &lt;executions&gt;
                    &lt;execution&gt;
                        &lt;goals&gt;
                            &lt;goal&gt;compile&lt;/goal&gt;
                        &lt;/goals&gt;
                    &lt;/execution&gt;
                &lt;/executions&gt;
            &lt;/plugin&gt;
        &lt;/plugins&gt;
    &lt;/build&gt;


```
1. 新建文件夹并编写 .protobuf文件 <img src="https://img-blog.csdnimg.cn/e3b9365304c6446fadfccd7acd16506a.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/d4d4ba07fbb6469fa461fe91106dfe3b.png" alt="在这里插入图片描述">
在 main 目录下，新建 proto 文件夹，该文件夹为 Test Resources Root类型。

```
syntax = "proto3";
option optimize_for = SPEED; // 加快解析
option java_package="com.ruoyi.ruoyitest.tcp.netty01";   //指定生成到哪个包下
option java_outer_classname="MyDataInfo"; // 外部类名, 文件名

//protobuf 可以使用message 管理其他的message
message MyMessage {<!-- -->

    //定义一个枚举类型
    enum DataType {<!-- -->
        StudentType = 0; //在proto3 要求enum的编号从0开始
        WorkerType = 1;
    }

    //用data_type 来标识传的是哪一个枚举类型
    DataType data_type = 1;

    //表示每次枚举类型最多只能出现其中的一个, 节省空间
    oneof dataBody {<!-- -->
        Student student = 2;
        Worker worker = 3;
    }

}


message Student {<!-- -->
    int32 id = 1;//Student类的属性
    string name = 2; //
}
message Worker {<!-- -->
    string name=1;
    int32 age=2;
}


```
1. 编译 <img src="https://img-blog.csdnimg.cn/653a498f2a0d4794911807f2e04b6da0.png" alt="在这里插入图片描述"> 双击 protobuf:compile，完成编译。1. 引用之即可 <img src="https://img-blog.csdnimg.cn/cdff875dd8814ebbbf3c325d929f24e4.png" alt="在这里插入图片描述">