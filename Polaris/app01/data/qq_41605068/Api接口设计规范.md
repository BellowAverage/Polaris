
--- 
title:  Api接口设计规范 
tags: []
categories: [] 

---
****<strong><em>接口设计：****</em></strong>

<img alt="" height="342" src="https://img-blog.csdnimg.cn/20210407145012229.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxNjA1MDY4,size_16,color_FFFFFF,t_70" width="554">

 

### **<strong><strong>一 安全性问题**</strong></strong>

安全性问题是一个接口必须要保证的规范。如果接口保证不了安全性，那么你的接口相当于直接暴露在公网环境中任人蹂躏。

#### **<strong><strong>1.1 调用接口的先决条件-token**</strong></strong>

token，使用参数client_id，timestamp，client_sercet，state来获取token，作为系统调用的唯一凭证。token可以设置一次有效（这样安全性更高），也可以设置时效性，这里推荐设置时效性。如果一次有效的话这个接口的请求频率可能会很高。token推荐加到请求头上，这样可以跟业务参数完全区分开来。

#### **<strong><strong>1.2 使用POST作为接口请求方式**</strong></strong>

一般调用接口最常用的两种方式就是GET和POST。两者的区别也很明显，GET请求会将参数暴露在浏览器URL中，而且对长度也有限制。为了更高的安全性，所有接口都采用POST方式请求。

#### **<strong><strong>1.3 客户端IP白名单**</strong></strong>

ip白名单是指将接口的访问权限对部分ip进行开放。这样就能避免其他ip进行访问攻击，设置ip白名单比较麻烦的一点就是当你的客户端进行迁移后，就需要重新联系服务提供者添加新的ip白名单。设置ip白名单的方式很多，除了传统的防火墙之外，spring cloud alibaba提供的组件sentinel也支持白名单设置。为了降低api的复杂度，推荐使用防火墙规则进行白名单设置。

#### **<strong><strong>1.4 单个接口针对ip限流**</strong></strong>

限流是为了更好的维护系统稳定性。使用redis进行接口调用次数统计，ip+接口地址作为key，访问次数作为value，每次请求value+1，设置过期时长来限制接口的调用频率。

#### **<strong><strong>1.5 记录接口请求日志**</strong></strong>

使用aop全局记录请求日志，快速定位异常请求位置，排查问题原因。

#### **<strong><strong>1.6 敏感数据脱敏**</strong></strong>

在接口调用过程中，可能会涉及到手机号等敏感数据，这类数据通常需要脱敏处理，最常用的方式就是加密。加密方式使用安全性比较高的RSA非对称加密。非对称加密算法有两个密钥，这两个密钥完全不同但又完全匹配。只有使用匹配的一对公钥和私钥，才能完成对明文的加密和解密过程。

 

### **<strong><strong>二 幂等性问题**</strong></strong>

幂等性是指任意多次请求的执行结果和一次请求的执行结果所产生的影响相同。说的直白一点就是查询操作无论查询多少次都不会影响数据本身，因此查询操作本身就是幂等的。但是新增操作，每执行一次数据库就会发生变化，所以它是非幂等的。幂等问题的解决有很多思路，这里讲一种比较严谨的。提供一个生成随机数的接口，随机数全局唯一。调用接口的时候带入随机数。第一次调用，业务处理成功后，将随机数作为key，操作结果作为value，存入redis，同时设置过期时长。第二次调用，查询redis，如果key存在，则证明是重复提交，直接返回错误。

### **<strong><strong>三 数据规范问题**</strong></strong>

#### **<strong><strong>3.1 版本控制**</strong></strong>

一套成熟的API文档，一旦发布是不允许随意修改接口的。这时候如果想新增或者修改接口，就需要加入版本控制，版本号可以是整数类型，也可以是浮点数类型。一般接口地址都会带上版本号，http://ip:port//v1/list。

#### **<strong><strong>3.2 响应状态码规范**</strong></strong>
<td style="width:63.6pt;"> **<strong>分类**</strong> </td><td style="width:444.15pt;"> **<strong>描述**</strong> </td>

**<strong>描述**</strong>
<td style="width:63.6pt;"> 1xx </td><td style="width:444.15pt;"> 信息，服务器收到请求，需要请求者继续执行操作 </td>

信息，服务器收到请求，需要请求者继续执行操作
<td style="width:63.6pt;"> 2xx </td><td style="width:444.15pt;"> 成功 </td>

成功
<td style="width:63.6pt;"> 3xx </td><td style="width:444.15pt;"> 重定向，需要进一步的操作以完成请求 </td>

重定向，需要进一步的操作以完成请求
<td style="width:63.6pt;"> 4xx </td><td style="width:444.15pt;"> 客户端错误，请求包含语法错误或无法完成请求 </td>

客户端错误，请求包含语法错误或无法完成请求
<td style="width:63.6pt;"> 5xx </td><td style="width:444.15pt;"> 服务端错误 </td>

服务端错误

#### **<strong><strong>3.3 统一响应数据格式**</strong></strong>

为了方便给客户端响应，响应数据会包含三个属性，状态码（code）,信息描述（message）,响应数据（data）。客户端根据状态码及信息描述可快速知道接口，如果状态码返回成功，再开始处理数据。

响应结果定义及常用方法：

```
public class R implements Serializable {



    private static final long serialVersionUID = 793034041048451317L;



    private int code;

    private String message;

    private Object data = null;



    public int getCode() {

        return code;

    }

    public void setCode(int code) {

        this.code = code;

    }



    public String getMessage() {

        return message;

    }

    public void setMessage(String message) {

        this.message = message;

    }



    public Object getData() {

        return data;

    }



    /**

     * 放入响应枚举

     */

    public R fillCode(CodeEnum codeEnum){

        this.setCode(codeEnum.getCode());

        this.setMessage(codeEnum.getMessage());

        return this;

    }



    /**

     * 放入响应码及信息

     */

    public R fillCode(int code, String message){

        this.setCode(code);

        this.setMessage(message);

        return this;

    }



    /**

     * 处理成功，放入自定义业务数据集合

     */

    public R fillData(Object data) {

        this.setCode(CodeEnum.SUCCESS.getCode());

        this.setMessage(CodeEnum.SUCCESS.getMessage());

        this.data = data;

        return this;

    }

}
```

 
