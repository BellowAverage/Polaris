
--- 
title:  基于java spring的邮件群发简单方式 
tags: []
categories: [] 

---
### 使用环境
- - - - - - 
### 准备工作
1. 使用maven将spring、mybatis、mysql、java mail所需要的包导入，具体导入的包见demo的pom.xml1. 申请一个邮箱账号（若有则跳过）1. 对于qq邮箱，需要申请授权码，路径：设置-&gt;账户-&gt;POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务-&gt;开启POP3/SMTP服务1. 在mysql中新建表user，并将想要发送的邮箱参数填入，表格式如下
>  
 <table><thead>|id|name|email
</thead></table> 


### 基础配置
- spring、mybatis 详细配置见demo<li>java mail 
  <ol><li>使用@PropertySource和@Value将mail.properties的内容读取出来。 <pre class="prettyprint"><code class=" hljs java">@Configuration
@PropertySource("mail.properties")
public class MailConfig {<!-- -->

@Value("${mail.host}")
private String mailHost;
@Value("${mail.port}")
private int mailPort;
@Value("${mail.username}")
private String username;
@Value("${mail.password}")
private String password;
@Value("${mail.auth}")
private String auth;
@Value("${mail.timeout}")
private String time0ut;
@Value("${mail.starttls.enable}")
private String starttlsEnable;
@Value("${mail.socketFactory.fallback}")
private String socketFactoryFallback;
@Value("${mail.socketFactory.class}")
private String socketFactoryClass;
......</code></pre></li><li>将上面读取的内容添加到mailsender中进行配置 <pre class="prettyprint"><code class=" hljs avrasm">@Bean
public MailSender mailSender(Environment env){
    JavaMailSenderImpl mailSender = new JavaMailSenderImpl();
    mailSender.setHost(mailHost);
    mailSender.setPort(Integer.valueOf(mailPort));
    mailSender.setUsername(username);
    mailSender.setPassword(password);
    mailSender.setDefaultEncoding("utf-8");
    Properties jpro = new Properties();
    jpro.setProperty("mail.smtp.auth", auth);
    jpro.setProperty("mail.smtp.timeout", time0ut);
    jpro.setProperty("mail.smtp.starttls.enable", starttlsEnable);
    jpro.setProperty("mail.smtp.socketFactory.port", String.valueOf(mailPort));
    jpro.setProperty("mail.smtp.socketFactory.fallback", socketFactoryFallback);
    jpro.setProperty("mail.smtp.socketFactory.class", socketFactoryClass);
    mailSender.setJavaMailProperties(jpro);
    return  mailSender;
}</code></pre></li></ol> 这样java mail的基础配置就基本完成</li>
### 发送邮件

目标是发送基于html的邮件，这样我们可以定制出各种各样的新鲜样式
<li>读取html文件  为了方便笔者直接使用了apache的读取文件内容 <pre class="prettyprint"><code class=" hljs vhdl">String text = "";
File file = ResourceUtils.getFile("classpath:mail.html");
text = FileUtils.readFileToString(file, "utf-8");</code></pre></li>- 读取数据库用户列表 使用mybatis读取mysql中的email列表实现群发功能，具体操作见demo<li>创建邮件  邮件至少由4个部分组成，分别是发送者，接受者，邮件名称，内容，可用以下参数配置 <pre class="prettyprint"><code class=" hljs cmake">MimeMessage message = mailSender.createMimeMessage();
MimeMessageHelper helper = new MimeMessageHelper(message, true, "utf-8");
helper.setFrom(mailUserName);
helper.setTo(email);
helper.setSubject("DEMO");
helper.setText(text, true);      //true可以显示html格式的文本</code></pre></li>- 发送邮件  最后使用`mailSender.send(message);`发送邮件即可。
### 源码下载
- csdn: - github: 
### 赞赏
<td align="center" colspan="2">赞赏</td>
<td align="center"> <img src="https://img-blog.csdn.net/20170521121423299?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="微信支付"> </td><td align="center"> <img src="https://img-blog.csdn.net/20170521131930503?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd2lsbDQ5MDY=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" width="200px" alt="支付宝"> </td>
<td align="center">微信</td><td align="center">支付宝</td>
