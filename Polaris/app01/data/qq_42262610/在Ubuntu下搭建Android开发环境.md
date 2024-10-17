
--- 
title:  在Ubuntu下搭建Android开发环境 
tags: []
categories: [] 

---
**1、安装Java jdk**

**2、安装Android studio**

**3、安装android-sdk**

将上述三个文件安装在任意目录下（/home/malinjie/Android1）

1.**安装Java jdk** 直接百度“Javajdk”，然后进入Oracle的官网

这里要注意，勾选上面的“Accept License Agreement”，不勾选的话会无法下载jdk。 勾选之后选择相应的版本，因为笔者的系统是64位的ubuntu，所以选择"Linux X64”版本，这里可以看到，Linux64版本有两个，后缀不同，ubuntu系统要选择后缀为“.gz”的那个。 下载完成之后就开始配置Java环境了。 这里笔者下载的文件名为：jdk-16.0.2_linux-x64_bin.tar.gz



如果环境搭建成功，运行以上两个命令之后会出现Java的版本信息以及简单的一些命令格式说明


-  解压  tar -zxvf  jdk-16.0.2_linux-x64_bin.tar.gz -  将文件夹'jdk16.0.2'移动到'/home/malinjie/Android1'下      -  sudo mv jdk16.0.2 /home/malinjie/Android1/ -  修改环境变量 -  sudo vi ~/.bashrc -  在最末尾添加如下内容： -  #set Java environment -  export JAVA_HOME=/home/malinjie/Android1/jdk-16.0.2 export JRE_HOME=/home/malinjie/Android1/jdk-16.0.2/jre export PATH=/home/malinjie/Android1/jdk-16.0.2/bin:$PATH export CLASSPATH=.:/home/malinjie/Android1/jdk-16.0.2/lib:/home/malinjie/Android1/jdk-16.0.2/jre/lib <li> 保存并退出，使用source命令让它生效 <pre><code> 	source ~/.bashrc
</code></pre> </li><li> 测试，是否搭建完成 <pre><code> 	java -version
 	javac
</code></pre> </li>- 至此，Java环境搭建完成
**2.安装 Android studio(****)**
- 在'/home/malinjie/Android1/'下新建一个'AndroidStudio'文件夹，将下载好的压缩包解压到该文件夹下- unzip android-studio-ide-173.4907809-linux.zip- 解压完成之后，得到一个'android-studio'目录
**3.安装Android-sdk**
- 启动- 在/home/malinjie/Android1/AndroidStudio/android-studio/bin目录下执行- sudo ./studio.sh
打开Android-studio后，会显示没有安装**Android-sdk，根据提示安装Android-sdk，并安装ndk，ndk的安装目录在Android-sdk目录下**
- 大功告成！