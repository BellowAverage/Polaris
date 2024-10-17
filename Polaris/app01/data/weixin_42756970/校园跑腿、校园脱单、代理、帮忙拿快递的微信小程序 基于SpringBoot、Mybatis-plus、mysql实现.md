
--- 
title:  校园跑腿、校园脱单、代理、帮忙拿快递的微信小程序 基于SpringBoot、Mybatis-plus、mysql实现 
tags: []
categories: [] 

---
## 一、文件夹说明

代码下载 地址:
<li>server 后端项目 
  <ul><li>project： 项目 
    <ul><li>CBD： 校园跑腿服务（校园CBD中心） 
      <ul>- server-app: 小程序api- server-pc: 小程序后台管理- service-cgs-base-service: 项目mapper公共包- 后台系统用户- 登陆- 权限- 部门- 角色
## 二、有部分是自己造的轮子(需要找我要jar包)
<li> 根 pom.xml 
  <ul><li> 上传工具类 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;cn.yj&lt;/groupId&gt;
    &lt;artifactId&gt;tools-upload&lt;/artifactId&gt;
    &lt;version&gt;1.0-SNAPSHOT&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> 启用方法： App启动累加上注解： <pre><code class="prism language-java">  @SpringBootApplication
  @Import(value = {<!-- -->InitUploadImportSelector.class})
  public class App {<!-- -->
  public static void main(String[] args) {<!-- -->
          SpringApplication.run(App.class, args);
     }
  }
</code></pre> 支持 Minio和fasdfs 、本地方式上传，对应的配置文件：`application-upload.yml` <pre><code class="prism language-yaml">   
 ##############  mino分布式图片存储 ####################
 file:
   upload-type: MINIO # MINIO、LOCAL
   local:
     path: /Users/yongjian/work/file/ # 本地上传文件到目录
     host: http://127.0.0.1:${<!-- -->server.port}/${<!-- -->server.servlet.context-path}/localFile  # 资源访问前缀
 minio:
   end:
     point: http://thisforyou.cn:9004
     point1: http://thisforyou.cn:9004
   accessKey: minioadmin
   secretKey: 123456
   bucket: cbd-dev
 
 
 
 ##############  fastdfs 配置  ####################
 fastdfs:
   connect_timeout_in_seconds: 60
   network_timeout_in_seconds: 60
   charset: UTF-8
   http_tracker_http_port: 80
   http_anti_steal_token: false
   http_secret_key: 123456
   tracker_servers: memoryoverflow.cn\:22122
</code></pre> </li><li> HTTP工具类 <pre><code class="prism language-xml">&lt;dependency&gt;
  &lt;groupId&gt;cn.yj.tools&lt;/groupId&gt;
  &lt;artifactId&gt;tools-http&lt;/artifactId&gt;
  &lt;version&gt;${http-utils}&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> </li><li> Service 类的接口的参数非空校验包 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;cn.yj&lt;/groupId&gt;
    &lt;artifactId&gt;service-params-check&lt;/artifactId&gt;
    &lt;version&gt;${service-params-check}&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> 启用校验：启动累加上注解：@EnableCheckMethodParams <pre><code class="prism language-java">  @SpringBootApplication
  @EnableCheckMethodParams
  public class App {<!-- -->
  public static void main(String[] args) {<!-- -->
          SpringApplication.run(App.class, args);
     }
  }
</code></pre> 使用方式：有两个注解 `@CheckObjectValue(keyValue = @KeyValue(type = Map.class, name = {"articleNo"}))` ，`@Require` 例如： <pre><code class="prism language-java">    @CheckObjectValue(keyValue = @KeyValue(type = Task.class, name = {<!-- -->"effectivTime", "userCode", "content",
          "urgentState"}))
    @Override
    public R publish(TaskVo task) {<!-- -->
          // ...
    }
</code></pre> KeyValue-type:当前接口的校验类，name：当前类的要校验非空的字段 <pre><code class="prism language-java"> public boolean agreeComment(@Require String commentNo, @Require String userCode) {<!-- -->
      // ....
 }
</code></pre> @Require 校验非空状态 </li><li> 分页组件工具 该主件事基于pageHelper的包装，不影响原有的pageHelper的使用 <pre><code class="prism language-xml">&lt;dependency&gt;
    &lt;groupId&gt;cn.yj&lt;/groupId&gt;
    &lt;artifactId&gt;annotation-pagehelper&lt;/artifactId&gt;
    &lt;version&gt;${annotation-pagehelper}&lt;/version&gt;
&lt;/dependency&gt;
</code></pre> 1、在mapper接口上加上注解：`@StartPage` 例如： <pre><code class="prism language-java">  @StartPage
  List&lt;ArticleVo&gt; findList(@Param("map") Map&lt;String, Object&gt; map, @Param("page") Page&lt;? extends Article&gt; page);
</code></pre> mapper接口上必须要有入参：Page 对象。 service上使用： <pre><code class="prism language-java">@Override
public Page&lt;ArticleVo&gt; listPage(Map&lt;String, Object&gt; params, Page&lt;ArticleVo&gt; page) {<!-- -->
    baseMapper.findList(params, page);
  return page;
}
</code></pre> 2、也可以不使用注解的形式 <pre><code class="prism language-java">@Override
public Page&lt;ArticleVo&gt; listPage(Map&lt;String, Object&gt; params, Page&lt;ArticleVo&gt; page) {<!-- -->
  page.startPage();
    page.setRows(baseMapper.findList(params, page));
  return page;
}
</code></pre> 该工具包事SpringBoot的starter自动配置包。引入即可使用。 </li>
部分基础异常类包装

```
&lt;dependency&gt;
    &lt;groupId&gt;cn.yj&lt;/groupId&gt;
    &lt;artifactId&gt;tools-exception&lt;/artifactId&gt;
    &lt;version&gt;${tools-exception}&lt;/version&gt;
&lt;/dependency&gt;

```

部分公共基础工具

```
&lt;dependency&gt;
    &lt;groupId&gt;cn.yj.tools&lt;/groupId&gt;
    &lt;artifactId&gt;tools-common-utils&lt;/artifactId&gt;
    &lt;version&gt;${tools-utils-v}&lt;/version&gt;
&lt;/dependency&gt;

```

yml文件读取工具包

```
&lt;dependency&gt;
    &lt;groupId&gt;cn.yj.tools&lt;/groupId&gt;
    &lt;artifactId&gt;tools-read-config&lt;/artifactId&gt;
    &lt;version&gt;${read-config}&lt;/version&gt;
&lt;/dependency&gt;

```

该工具类事主要提供静态方法读取 yaml,properties文件的工具。启用该工具：

```
  @SpringBootApplication
  @EnableReadConfig(classLoader = App.class)
  public class App {<!-- -->
  public static void main(String[] args) {<!-- -->
          SpringApplication.run(App.class, args);
     }
  }

```

工具类：

```
/**
 * &lt;br&gt;
 * &lt;p&gt;
 * 该工具类 只做读取资源文件的功能操作。 基于SpringBoot使用
 * &lt;p&gt;
 * &lt;p&gt;
 * &lt;p&gt;
 * 1、工具类加载会默认读取：
 * &lt;p&gt;
 * &lt;p&gt;
 * &lt;p&gt;
 * 开发环境：resources/config 目录下的资源文件 其次是  resources/
 * jar包环境：jar包同级目录下的 config 资源文件每其次是 jar同级的资源文件，其次是 jar包内 config资源文件，其次是 jar包内的 资源文件。
 * &lt;p&gt;
 * resources/config -&gt; resources/
 * jar=config --&gt; jar/ --&gt; jar内的resources/config --&gt; jar包内的resources/
 * &lt;p&gt;
 * &lt;p&gt;
 * 1、默认优先加载 application.yml 资源文件 其次是yml文件。这一点与SpringBoot相似
 * 2、文件加载顺序 非jar包环境 开发环境下:
 * 优先读取 resources/config 资源目录下的 application.yml 和 config.yml/config.properties 文件，如果读取成功，就不会继续加载 resources 下的其他配置文件。
 * 默认会加载 application  application-dev/application-prod application-test 这三个。
 * dev test prod 会取决于  application 文件下的 active配置：假如是 dev 就会加载对应的 application-dev 文件。
 * config.yml优先于config.properties
 * 3、jar包读取：
 * 优先读取与jar包同级下的 config目录下的资源文件，其次是与jar包同级的资源文件 其次就是读取 jar包内的资源文件。
 * &lt;p&gt;
 * 4、自定义资源文件加载：
 * 支持文件 yml 和 properties 两种后缀的文件。不支持 xml文件。自定义文件的加载顺序，在前面者优先加载。
 * &lt;p&gt;
 * &lt;p&gt;
 * 5、关于相同文件名：如果存在相同的文件名（包含路径不同）后者不会被加载。
 * &lt;p&gt;
 * 6、取值问题：取值的顺序是 先加载的文件，后取值。会先取后面加载的资源文件的先，如果存在相同的key 后面的文件优先。
 * &lt;p&gt;
 * * 暂时不支持直接读取 map 和 list 的配置
 * *
 * * 例如：
 * * user:
 * *  lists:
 * *     - 张三
 * *     - 李四
 * *     - 王五
 *   但是可以自定义格式：lists:[张三,李四,王五] or lists:张三,李四,王五
 *
 *   map格式： map:{name:tom,age:18} //
 * *
 * &lt;p&gt;
 * &lt;p&gt;
 * &lt;p&gt;
 * 7、自定义加载文件问题：加载系统资源文件务必上上 `classpath:`
 * 例如：classpath: user.config
 * 加载系统资源文件： 例如：/Users/yongjian/work/shell/config.properties
 *
 * @author 永健
 * @since 2020-09-17 13:46
 */
public class PropertiesUtils extends ConfigRead
{<!-- -->
    /**
     * 加载文件
     * &lt;p&gt;
     * 系统路径写法：系统路径：/Users/yongjian/application.yml
     * 类路径：classpath:application.yml 或者 classpath:spring/application.yml
     *
     * @param path 文件路径
     */
    private static void load(String... path)
    {<!-- -->
        if (path != null &amp;&amp; path.length != 0)
        {<!-- -->
            for (int i = 0; i &lt; path.length; i++)
            {<!-- -->
                String filePath = path[i].trim();
                if (filePath.length() &gt; 0)
                {<!-- -->
                    System.out.println("加载资源文件："+filePath);
                }
            }
        }
    }


    /**
     * 获取属性值
     * &lt;p&gt;
     * &lt;p&gt;
     * 加载顺序冲从上往下，读取顺序从下网上。
     * application.yml
     * application-dev.yml
     * application-prod.yml
     * application-test.yml
     * config.yml
     * 自定义加载的文件
     *
     * &lt;p&gt;
     * 获取顺序： 自定义加载的/config.yml/config.properties-&gt;prod/dev/test-&gt;application
     * 如果有重复的key,会优先于读取后面加载的文件key。
     *
     * @param key key
     * @return 值
     */
    public static String getStringValue(String key, String defaultValue)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? defaultValue : String.valueOf(value);
    }

    public static String getStringValue(String key)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? null : String.valueOf(value);
    }

    public static int getIntValue(String key, Integer defaultValue)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? defaultValue : Integer.valueOf(value.toString());
    }

    public static int getIntValue(String key)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? 0 : Integer.valueOf(value.toString());
    }

    public static boolean getBooleanValue(String key, boolean defaultValue)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? defaultValue : Boolean.valueOf(value.toString());
    }

    public static boolean getBooleanValue(String key)
    {<!-- -->
        Object value = getObjectValue(key);
        return value == null ? false : Boolean.valueOf(value.toString());
    }

    public static &lt;T&gt; List&lt;T&gt; getList(String key)
    {<!-- -->
        Object value = getObjectValue(key);
        String vl = "";
        if (value != null)
        {<!-- -->
            vl = value.toString().replaceAll(" ", "");

            vl = vl.replace("[", "").replace("]", "");
            String[] split = vl.split(",");

            return (List&lt;T&gt;) Arrays.asList(split);
        }
        return null;
    }

    public static Map&lt;String, Object&gt; getMap(String key)
    {<!-- -->
        Object value = getObjectValue(key);
        String vl = "";
        if (value != null)
        {<!-- -->
            vl = value.toString();
            return changeMap(vl);
        }
        return null;
    }

    private static Map&lt;String, Object&gt; changeMap(String vl)
    {<!-- -->
        Map&lt;String, Object&gt; map = null;
        vl = vl.replaceAll(" ", "");
        if (vl.startsWith("{") &amp;&amp; vl.endsWith("}"))
        {<!-- -->
            vl = vl.replace("{", "").replace("}", "");
            String[] split = vl.split(",");
            map = new HashMap&lt;&gt;();
            for (String item : split)
            {<!-- -->
                if (!item.contains(":"))
                {<!-- -->
                    throw new RuntimeException("解析数据出错,请按照格式配置,例如：{name:tom,age:18}");
                }
                String[] keyValues = item.split(":");
                if (keyValues.length != 2 || "".equals(keyValues[0]))
                {<!-- -->
                    throw new RuntimeException("解析数据出错,请按照格式配置,例如：{name:tom,age:18}");
                }
                map.put(keyValues[0], keyValues[1]);
            }
        }
        return map;
    }

}


```

微信小程序相关接口包装工具；小程序获取Token解密 获取获取用户信息等

```
&lt;dependency&gt;
  &lt;groupId&gt;cn.yj.wechat&lt;/groupId&gt;
  &lt;artifactId&gt;wechat&lt;/artifactId&gt;
  &lt;version&gt;0.0.1&lt;/version&gt;
&lt;/dependency&gt;

```

## 三、 项目配置说明

好像没有多少事需要特别注意的。不懂的可以私我。
<li> 高德key需要替换成自己的 <pre><code class="prism language-yaml">  applications:
    geoKey: 085f5a65cd254be133e74cbd5ee160c0456
</code></pre> </li>-  小程序需要替换成自己的 
```
  applications:
    wechat:
      mini:
        appId: wx53c2168b5ad5c0a525
        secret: ded80da4f198338a061e1ae31480e1cc21

```
<li>文件上传（自己封装的工具只实现了 本地图片上传和minio文件服务器上传，其它需要自己实现） 
  <ul>- 提供了上传文件接口 FileUpload.java- 增加实现的话,需要重写 `InitUploadImportSelector.java` 的 `selectImports(AnnotationMetadata annotationMetadata)` 方法,按需加载 。然后App启动类上替换成自己的 `@Import(value = {InitUploadImportSelector.class})` 将 `InitUploadImportSelector` 替换成自己的即可。- file.upload-type: 指定系统实例化上传实现
```
  file:
    upload-type: LOCAL # MINIO(minio服务器)、LOCAL(本地上传)
    local:
      path: /Users/yongjian/work/file/ # 本地上传文件到目录 文件默认要加上 /。否则文件无法映射
      host: http://127.0.0.1:${<!-- -->server.port}/${<!-- -->server.servlet.context-path}/localFile  # 资源访问前缀
    minio:
      end:
        point: http://thisforyou.cn:9004 # 两个填写一致就行了。这个是上传文件ip。内网的时候可以填写不一致
        point1: http://thisforyou.cn:9004 # 这个是外网访问minio图片的ip
      accessKey: minioadmin
      secretKey: 123456

```
<li>启动盲盒支付 
  <ul>- 在 service-wx-pay 模块中的配置文件 application-wxPay.yml。 wechat.pay.start：true 开启盲盒支付。默认不开启- 引用微信支付模块需 注册 PayAutoConfig.class
```
  #  微信
  wechat:
    pay:
      start: true
      appId: wx8944343 #小程序id
      mchId: 12313123131  #商户id
      mchSerialNo: 11
      apiV3Key: 1
      key-path: classpath:apiclient_key.pem
      # 支付成功回调
      pay-notice-url: https://aliyun.thisforyou.cn/api/pay/wxPayNotice
      refund-notice-url: https://aliyun.thisforyou.cn/api/pay/wxRefundNotice

```
-  个人开发者在小程序授权的时候会失败，无法获取手机号（需要自行更改） -  邮件配置（请查看application.email.yml）进行修改成自己的账号 
## 四、项目演示地址：

请各位进入如后台的时候，不要删除必要数据，谢谢各位。

### 1、后台管理
-  PC后台管理 第一次访问可能有点慢，访问地址： https://aliyun.thisforyou.cn/server-view/#/login 账号：test/123456 （没有修改权限） 
<img src="https://img-blog.csdnimg.cn/e310d5bc8f264273ab3d8baa2b33e2dd.png" alt="在这里插入图片描述">

### 小程序
-  小程序 <img src="https://img-blog.csdnimg.cn/55bf5abf921545839ff5259ab136ad4f.png" alt="在这里插入图片描述"> 
<img src="https://img-blog.csdnimg.cn/0be81c29acbb44528870cc355f2398f5.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/419247406ace4ff18f37ba9a60602f2e.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/ce009deda7504f2c962763cfe162249c.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/dea229aefc3d46e5b41a3f2b35ab3e78.png" alt="在这里插入图片描述">

代码下载 地址:
