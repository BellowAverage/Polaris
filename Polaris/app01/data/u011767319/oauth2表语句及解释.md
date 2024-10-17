
--- 
title:  oauth2表语句及解释 
tags: []
categories: [] 

---
### 表解释

**oauth_client_details**

|字段|解释
|------
|client_id|主键,必须唯一,不能为空.用于唯一标识每一个客户端(client); 在注册时必须填写(也可由服务端自动生成).对于不同的grant_type,该字段都是必须的. 在实际应用中的另一个名称叫appKey,与client_id是同一个概念.
|–|–
|resource_ids|客户端所能访问的资源id集合,多个资源时用逗号(,)分隔,如: “unity-resource,mobile-resource”.可以根据上图知道，我们有Resource Server资源服务器。，资源服务器可以有多个，我们可以为每一个Resource Server（一个微服务实例）设置一个resourceid。Authorization Server给client第三方客户端授权的时候，可以设置这个client可以访问哪一些Resource Server资源服务，如果没设置，就是对所有的Resource Server都有访问权限。
|–|–
|client_secret|用于指定客户端(client)的访问密匙; 在注册时必须填写(也可由服务端自动生成).对于不同的grant_type,该字段都是必须的. 在实际应用中的另一个名称叫appSecret,与client_secret是同一个概念.
|–|–
|scope|指定客户端申请的权限范围,可选值包括read,write,trust;若有多个权限范围用逗号(,)分隔,如: “read,write”.@EnableGlobalMethodSecurity(prePostEnabled = true)启用方法级权限控制,然后在方法上注解标识@PreAuthorize("#oauth2.hasScope(‘read’)")
|–|–
|authorized_grant_types|指定客户端支持的grant_type,可选值包括authorization_code,password,refresh_token,implicit,client_credentials, 若支持多个grant_type用逗号(,)分隔,如: “authorization_code,password”.在实际应用中,当注册时,该字段是一般由服务器端指定的,而不是由申请者去选择的,最常用的grant_type组合有: “authorization_code,refresh_token”(针对通过浏览器访问的客户端); “password,refresh_token”(针对移动设备的客户端).implicit与client_credentials在实际中很少使用，可以根据自己的需要，在OAuth2.0 提供的地方进行扩展自定义的授权
|–|–
|web_server_redirect_uri|客户端的重定向URI,可为空, 当grant_type为authorization_code或implicit时, 在Oauth的流程中会使用并检查与注册时填写的redirect_uri是否一致. 下面分别说明:当grant_type=authorization_code时, 第一步 从 spring-oauth-server获取 'code’时客户端发起请求时必须有redirect_uri参数, 该参数的值必须与 web_server_redirect_uri的值一致. 第二步 用 ‘code’ 换取 ‘access_token’ 时客户也必须传递相同的redirect_uri.在实际应用中, web_server_redirect_uri在注册时是必须填写的, 一般用来处理服务器返回的code, 验证state是否合法与通过code去换取access_token值.在spring-oauth-client项目中, 可具体参考AuthorizationCodeController.java中的authorizationCodeCallback方法.当grant_type=implicit时通过redirect_uri的hash值来传递access_token值.如:http://localhost:7777/spring-oauth-client/implicit#access_token=dc891f4a-ac88-4ba6-8224-a2497e013865&amp;token_type=bearer&amp;expires_in=43199,然后客户端通过JS等从hash值中取到access_token值.
|–|–
|authorities|@PreAuthorize(“hasAuthority(‘admin’)”)可以在方法上标志 用户或者说client 需要说明样的权限,指定客户端所拥有的Spring Security的权限值,可选, 若有多个权限值,用逗号(,)分隔, 如: “ROLE_UNITY,ROLE_USER”.对于是否要设置该字段的值,要根据不同的grant_type来判断, 若客户端在Oauth流程中需要用户的用户名(username)与密码(password)的(authorization_code,password),则该字段可以不需要设置值,因为服务端将根据用户在服务端所拥有的权限来判断是否有权限访问对应的API.但如果客户端在Oauth流程中不需要用户信息的(implicit,client_credentials),则该字段必须要设置对应的权限值, 因为服务端将根据该字段值的权限来判断是否有权限访问对应的API.(请在spring-oauth-client项目中来测试不同grant_type时authorities的变化)
|–|–
|access_token_validity|设定客户端的access_token的有效时间值(单位:秒),可选, 若不设定值则使用默认的有效时间值(60 * 60 * 12, 12小时).在服务端获取的access_token JSON数据中的expires_in字段的值即为当前access_token的有效时间值.在项目中, 可具体参考DefaultTokenServices.java中属性accessTokenValiditySeconds.在实际应用中, 该值一般是由服务端处理的, 不需要客户端自定义.
|–|–
|refresh_token_validity|设定客户端的refresh_token的有效时间值(单位:秒),可选, 若不设定值则使用默认的有效时间值(60 * 60 * 24 * 30, 30天).若客户端的grant_type不包括refresh_token,则不用关心该字段 在项目中, 可具体参考DefaultTokenServices.java中属性refreshTokenValiditySeconds.在实际应用中, 该值一般是由服务端处理的, 不需要客户端自定义.
|–|–
|additional_information|这是一个预留的字段,在Oauth的流程中没有实际的使用,可选,但若设置值,必须是JSON格式的数据,如:{“country”:“CN”,“country_code”:“086”}按照spring-security-oauth项目中对该字段的描述Additional information for this client, not need by the vanilla OAuth protocol but might be useful, for example,for storing descriptive information.(详见ClientDetails.java的getAdditionalInformation()方法的注释) 在实际应用中, 可以用该字段来存储关于客户端的一些其他信息,如客户端的国家,地区,注册时的IP地址等等.
|–|–
|create_time|数据的创建时间,精确到秒,由数据库在插入数据时取当前系统时间自动生成(扩展字段)
|–|–
|autoapprove|设置用户是否自动Approval操作, 默认值为 ‘false’, 可选值包括 ‘true’,‘false’, ‘read’,‘write’.该字段只适用于grant_type="authorization_code"的情况,当用户登录成功后,若该值为’true’或支持的scope值,则会跳过用户Approve的页面, 直接授权.

**oauth_client_token**

|字段|解释
|------
|create_time|数据的创建时间,精确到秒,由数据库在插入数据时取当前系统时间自动生成(扩展字段)
|–|–
|token_id|从服务器端获取到的access_token的值.
|–|–
|token|这是一个二进制的字段, 存储的数据是OAuth2AccessToken.java对象序列化后的二进制数据.
|–|–
|authentication_id|该字段具有唯一性, 是根据当前的username(如果有),client_id与scope通过MD5加密生成的. 具体实现请参考DefaultClientKeyGenerator.java类.
|–|–
|user_name|登录时的用户名
|–|–
|client_id|在注册时必须填写(也可由服务端自动生成).对于不同的grant_type,该字段都是必须的. 在实际应用中的另一个名称叫appKey,与client_id是同一个概念.

**oauth_access_token**

|字段|解释
|------
|create_time|数据的创建时间,精确到秒,由数据库在插入数据时取当前系统时间自动生成(扩展字段)
|–|–
|token_id|该字段的值是将access_token的值通过MD5加密后存储的.
|–|–
|token|存储将OAuth2AccessToken.java对象序列化后的二进制数据, 是真实的AccessToken
|的数据值.|
|–|–
|authentication_id|该字段具有唯一性, 其值是根据当前的username(如果有),client_id与scope通过MD5加密生成的. 具体实现请参考DefaultAuthenticationKeyGenerator.java类.
|–|–
|user_name|登录时的用户名, 若客户端没有用户名(如grant_type=“client_credentials”),则该值等
|于client_id|
|–|–
|client_id|在注册时必须填写(也可由服务端自动生成).对于不同的grant_type,该字段都是必须的. 在实际应用中的另一个名称叫appKey,与client_id是同一个概念.
|–|–
|authentication|存储将OAuth2Authentication.java对象序列化后的二进制数据.
|–|–
|refresh_token|该字段的值是将refresh_token的值通过MD5加密后存储的. 在项目中,主要操作oauth_access_token表的对象是JdbcTokenStore.java. 更多的细节请参考该类

**oauth_refresh_token**

|字段|解释
|------
|create_time|数据的创建时间,精确到秒,由数据库在插入数据时取当前系统时间自动生成(扩展字段)
|–|–
|token_id|该字段的值是将refresh_token的值通过MD5加密后存储的.
|–|–
|token|存储将OAuth2RefreshToken.java对象序列化后的二进制数据.
|–|–
|authentication|存储将OAuth2Authentication.java对象序列化后的二进制数据.

**oauth_code**

|字段|解释
|------
|create_time|数据的创建时间,精确到秒,由数据库在插入数据时取当前系统时间自动生成(扩展字段)
|–|–
|code|存储服务端系统生成的code的值(未加密).
|–|–
|authentication|存储将AuthorizationRequestHolder.java对象序列化后的二进制数据.

### 表语句

```
CREATE TABLE `oauth_access_token` (
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `token_id` varchar(255) DEFAULT NULL,
  `token` blob DEFAULT NULL,
  `authentication_id` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `client_id` varchar(255) DEFAULT NULL,
  `authentication` blob DEFAULT NULL,
  `refresh_token` varchar(255) DEFAULT NULL,
  UNIQUE KEY `authentication_id` (`authentication_id`),
  KEY `token_id_index` (`token_id`),
  KEY `authentication_id_index` (`authentication_id`),
  KEY `user_name_index` (`user_name`),
  KEY `client_id_index` (`client_id`),
  KEY `refresh_token_index` (`refresh_token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='授权成功token';

CREATE TABLE `oauth_client_details` (
  `client_id` varchar(255) NOT NULL,
  `resource_ids` varchar(255) DEFAULT NULL,
  `client_secret` varchar(255) DEFAULT NULL,
  `scope` varchar(255) DEFAULT NULL,
  `authorized_grant_types` varchar(255) DEFAULT NULL,
  `web_server_redirect_uri` varchar(255) DEFAULT NULL,
  `authorities` varchar(255) DEFAULT NULL,
  `access_token_validity` int(11) DEFAULT NULL,
  `refresh_token_validity` int(11) DEFAULT NULL,
  `additional_information` text DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `archived` tinyint(1) DEFAULT 0,
  `trusted` tinyint(1) DEFAULT 0,
  `autoapprove` varchar(255) DEFAULT 'false',
  PRIMARY KEY (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='客户端详情';

CREATE TABLE `oauth_code` (
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `code` varchar(255) DEFAULT NULL,
  `authentication` blob DEFAULT NULL,
  KEY `code_index` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='授权code';

CREATE TABLE `oauth_refresh_token` (
  `create_time` timestamp NOT NULL DEFAULT current_timestamp(),
  `token_id` varchar(255) DEFAULT NULL,
  `token` blob DEFAULT NULL,
  `authentication` blob DEFAULT NULL,
  KEY `token_id_index` (`token_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='更新token';

-- Add indexes
create index token_id_index on oauth_access_token (token_id);
create index authentication_id_index on oauth_access_token (authentication_id);
create index user_name_index on oauth_access_token (user_name);
create index client_id_index on oauth_access_token (client_id);
create index refresh_token_index on oauth_access_token (refresh_token);
 
create index token_id_index on oauth_refresh_token (token_id);
 
create index code_index on oauth_code (code);

```
