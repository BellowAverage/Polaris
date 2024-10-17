
--- 
title:  证书工具类（csr、cer） 
tags: []
categories: [] 

---- csr证书也称为p10证书- ，cer证书就是我们可以被系统识别到的证书。- 所有证书都是ans.1格式的，ans.1相当于json格式而已，对于这种格式可以用相关的工具查看，推荐一款工具，我自己用的查看工具：- api是国密的包，基础的包、provider包（第三方厂商包），bcpkix（扩展包），mail（邮件加密包），这里大量用了基础包和bcpkix包
>  
 Java加密的常用的加密算法类型有三种 
 1单向加密：也就是不可逆的加密，例如MD5,SHA,HMAC 
 2对称加密：也就是加密方和解密方利用同一个秘钥对数据进行加密和解密，例如DES，PBE等等 
 3非对称加密：非对称加密分为公钥和秘钥，二者是非对称的，例如用私钥加密的内容需要使用公钥来解密，使用公钥加密的内容需要用私钥来解密，DSA，RSA... 
 而keyGenerator,KeyPairGenerator,SecretKeyFactory的三种使用方法刚好和这三种加密算法类型对上 
 keyGenerator：秘钥生成器，也就是更具算法类型随机生成一个秘钥，例如HMAC，所以这个大部分用在非可逆的算法中 
 SecretKeyFactory：秘密秘钥工厂，言外之意就是需要根据一个秘密（password）去生成一个秘钥,例如DES，PBE，所以大部分使用在对称加密中 
 KeyPairGenerator:秘钥对生成器，也就是可以生成一对秘钥，也就是公钥和私钥，所以大部分使用在非对称加密中 


 

>  
 **CSR****是什么** 
 CSR是Certificate Signing Request的英文缩写，即证书签名请求文件，是证书申请者在申请数字证书时由CSP(加密服务提供者)在生成私钥的同时也生成证书请求文件，证书申请者只要把CSR文件提交给证书颁发机构后，证书颁发机构使用其根证书私钥签名就生成了证书公钥文件，也就是颁发给用户的证书。 
 **CSR****什么样** 
 CSR是以-----BEGIN CERTIFICATE REQUEST-----开头，-----END CERTIFICATE REQUEST-----为结尾的base64格式的编码。将其保存为文本文件，就是所谓的CSR文件。 
 <img alt="" src="https://img-blog.csdnimg.cn/img_convert/f8c3c9682c997b0c4443a5058a306efb.png"> 
 CSR生成工具非常多，比如openssl工具，keystore explore，XCA等   在线工具： 
 这里有几个关键的要注意下： 
 -  域名必须正确输入（如果是非SSL证书，则输入相应的通用名）。 -  密钥算法选择RSA的话，密钥长度需要2048bit以上（这个默认是2048，没有特殊情况，不要特殊设置）；ECC则是256bit以上。 -  摘要签名虽说目前可以任意，但建议是sha2-256以上。  
 **CSR****生成注意事项** 
 **匹配的****KEY****必须保存** 
 有CSR必定有KEY，是成对的，CSR最终变成为证书，和私钥key配对使用。Key是以-----BEGIN RSA PRIVATE KEY-----开头的，-----END RSA PRIVATE KEY-----结尾的。Key必须保存好。 
 <img alt="33.jpg" src="https://img-blog.csdnimg.cn/img_convert/1460d2ca92c64a6b88a95256c1d8aceb.png"> 
 **CSR****生命周期** 
 证书下发后，CSR无需使用，仅提交时候需要。 


 代码实现：

```
public static void main(String[] args) {

Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        KeyPairGenerator localKeyPairGenerator = KeyPairGenerator.getInstance("EC", new BouncyCastleProvider());
        localKeyPairGenerator.initialize(256);
        KeyPair localKeyPair = localKeyPairGenerator.genKeyPair();
        X500NameBuilder localX500NameBuilder = new X500NameBuilder(BCStyle.INSTANCE);
        localX500NameBuilder.addRDN(BCStyle.CN, "www.baidu.com");//通用名称
        localX500NameBuilder.addRDN(BCStyle.C, "CN"); //国家
            localX500NameBuilder.addRDN(BCStyle.O, "CNOOC");//组织
        localX500NameBuilder.addRDN(BCStyle.L, "tianjin");//城市
        localX500NameBuilder.addRDN(BCStyle.ST, "tianjin");//省份
        localX500NameBuilder.addRDN(BCStyle.EmailAddress, "admin@39dian.com");
        X500Name localX500Name = localX500NameBuilder.build();
        JcaPKCS10CertificationRequestBuilder p10Builder = new JcaPKCS10CertificationRequestBuilder(localX500Name, localKeyPair.getPublic());
        JcaContentSignerBuilder csBuilder = new JcaContentSignerBuilder("SM3WITHSM2");// 签名算法
        ContentSigner signer = csBuilder.build(localKeyPair.getPrivate());
        PKCS10CertificationRequest csr = p10Builder.build(signer);// PKCS10的请求
        byte[] bytes = csr.getEncoded();
        String s = Base64.getEncoder().encodeToString(bytes);
       // String s1="-----BEGIN CERTIFICATE REQUEST-----";
        //String s2= "-----END CERTIFICATE REQUEST-----";
        System.out.println(s);

}
```

>  
 在线校验csr： 
 生成csr： 


>  
  一般的数字证书产品的主题通常含有如下字段： 公用名称 (Common Name) 简称：CN 字段，对于 SSL 证书，一般为网站域名；而对于代码签名证书则为申请单位名称；而对于客户端证书则为证书申请者的姓名；  单位名称 (Organization Name) ：简称：O 字段，对于 SSL 证书，一般为网站域名；而对于代码签名证书则为申请单位名称；而对于客户端单位证书则为证书申请者所在单位名称；  证书申请单位所在地：  所在城市 (Locality) 简称：L 字段  所在省份 (State/Provice) 简称：S 字段  所在国家 (Country) 简称：C 字段，只能是国家字母缩写，如中国：CN  其他一些字段： 电子邮件 (Email) 简称：E 字段  多个姓名字段 简称：G 字段  介绍：Description 字段  电话号码：Phone 字段，格式要求 + 国家区号 城市区号 电话号码，如： +86 732 88888888  地址：STREET  字段  邮政编码：PostalCode 字段  显示其他内容 简称：OU 字段 


使用OpenSSL生成：

```
C:\Users\cakin&gt;cd D:\OpenSSL\bin
C:\Users\cakin&gt;d:
D:\OpenSSL\bin&gt;openssl req -new -nodes -newkey rsa:2048 -keyout domain.key -out domain.csr
Loading 'screen' into random state - done
Generating a 2048 bit RSA private key
......................+++
....................+++
writing new private key to 'domain.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:cn
State or Province Name (full name) [Some-State]:sanxi
Locality Name (eg, city) []:xian
Organization Name (eg, company) [Internet Widgits Pty Ltd]:network technology
Organizational Unit Name (eg, section) []:IT
Common Name (eg, YOUR name) []:
Email Address []:
 
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

从Email地址开始，下面的信息都不需要，请保留为空，直接回车。 
