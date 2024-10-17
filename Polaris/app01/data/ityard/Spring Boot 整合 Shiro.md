
--- 
title:  Spring Boot 整合 Shiro 
tags: []
categories: [] 

---
### 1 简介

Shiro是Apache下一个开源的安全框架，提供了认证、授权、加密、会话管理，与 Spring Security 相比，Shiro 是一个轻量级框架，使用了比较简单易懂易于使用的授权方式。

##### 1.1 Shiro特性

<img src="https://img-blog.csdnimg.cn/20191002074059470.png#pic_center" alt="">
-  **Authentication**：身份认证/登录，验证用户是不是拥有相应的身份； -  **Authorization**：授权，即权限验证，验证某个已认证的用户是否拥有某个权限； -  **Session Manager**：会话管理，用户登录后就是一次会话，在没有退出之前，它的所有信息都在会话中； -  **Cryptography**：加密，保护数据的安全性，如密码加密存储到数据库，而不是明文存储； -  **Web Support**：Web支持，可以非常容易的集成到Web环境； -  **Caching**：缓存，比如用户登录后，其用户信息、拥有的角色/权限不必每次去查，这样可以提高效率； -  **Concurrency**：Shiro支持多线程应用的并发验证，如在一个线程中开启另一个线程，能把权限自动传播过去； -  **Testing**：提供测试支持； -  **Run As**：允许一个用户假装为另一个用户（如果他们允许）的身份进行访问； -  **Remember Me**：记住我，这个是非常常见的功能，即一次登录后，下次访问就不用登录了。 
##### 1.2 High-Level Overview 高级概述

<img src="https://img-blog.csdnimg.cn/20191002074551865.png#pic_center" alt="">
-  **Subject**：当前用户，Subject 可以是一个人，也可以是第三方服务； -  **SecurityManager**：管理所有Subject，SecurityManager 是 Shiro 架构的核心，配合内部安全组件共同组成安全伞； -  **Realms**：用于进行权限信息的验证，我们自己实现，本质上是一个特定的安全 DAO，它封装与数据源连接的细节，得到 Shiro 所需的相关的数据，在配置 Shiro 的时候，必须指定至少一个Realm 来实现认证（Authentication）或授权（Authorization）。 
### 2 快速上手

**1）添加 pom 依赖**

```
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
  &lt;artifactId&gt;spring-boot-starter-data-jpa&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
  &lt;artifactId&gt;spring-boot-starter-thymeleaf&lt;/artifactId&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
  &lt;artifactId&gt;shiro-spring&lt;/artifactId&gt;
  &lt;version&gt;1.4.0&lt;/version&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;mysql&lt;/groupId&gt;
  &lt;artifactId&gt;mysql-connector-java&lt;/artifactId&gt;
  &lt;scope&gt;runtime&lt;/scope&gt;
&lt;/dependency&gt;
&lt;dependency&gt;
  &lt;groupId&gt;net.sourceforge.nekohtml&lt;/groupId&gt;
  &lt;artifactId&gt;nekohtml&lt;/artifactId&gt;
  &lt;version&gt;1.9.22&lt;/version&gt;
&lt;/dependency&gt;

```

**2）配置文件**

```
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/shiro?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false&amp;serverTimezone=UTC
    username: root
    password: root
    driver-class-name: com.mysql.jdbc.Driver
  jpa:
    database: mysql
    show-sql: true
    hibernate:
      ddl-auto: update
      naming:
        physical-strategy: org.springframework.boot.orm.jpa.hibernate.SpringPhysicalNamingStrategy
  thymeleaf:
    cache: false
    mode: HTML

```

**3）新建实体类**

用户信息

```
@Entity
public class SysUser implements Serializable {<!-- -->
    @Id
    @GeneratedValue
    private Integer uid;
    @Column(unique =true)
    private String username;//帐号
    private String name;//名称
    private String password; //密码;
    private String salt;//加密密码的盐
    private byte state;//用户状态,0:创建未认证, 1:正常状态,2：用户被锁定.
    @ManyToMany(fetch= FetchType.EAGER)//立即从数据库中进行加载数据;
    @JoinTable(name = "SysUserRole", joinColumns = {<!-- --> @JoinColumn(name = "uid") }, inverseJoinColumns ={<!-- -->@JoinColumn(name = "roleId") })
    private List&lt;SysRole&gt; roleList;// 一个用户具有多个角色

    public Integer getUid() {<!-- -->
        return uid;
    }

    public void setUid(Integer uid) {<!-- -->
        this.uid = uid;
    }

    public String getUsername() {<!-- -->
        return username;
    }

    public void setUsername(String username) {<!-- -->
        this.username = username;
    }

    public String getName() {<!-- -->
        return name;
    }

    public void setName(String name) {<!-- -->
        this.name = name;
    }

    public String getPassword() {<!-- -->
        return password;
    }

    public void setPassword(String password) {<!-- -->
        this.password = password;
    }

    public String getSalt() {<!-- -->
        return salt;
    }

    public void setSalt(String salt) {<!-- -->
        this.salt = salt;
    }

    public byte getState() {<!-- -->
        return state;
    }

    public void setState(byte state) {<!-- -->
        this.state = state;
    }

    public List&lt;SysRole&gt; getRoleList() {<!-- -->
        return roleList;
    }

    public void setRoleList(List&lt;SysRole&gt; roleList) {<!-- -->
        this.roleList = roleList;
    }

    public String getCredentialsSalt(){<!-- -->
        return this.username+this.salt;
    }
}

```

角色信息

```
@Entity
public class SysRole implements Serializable{<!-- -->
    @Id@GeneratedValue
    private Integer id; // 编号
    private String role; // 角色
    private String description; // 角色描述
    private Boolean available = Boolean.FALSE; // 是否可用

    //角色 -- 权限关系：多对多关系;
    @ManyToMany(fetch= FetchType.EAGER)
    @JoinTable(name="SysRolePermission",joinColumns={<!-- -->@JoinColumn(name="roleId")},inverseJoinColumns={<!-- -->@JoinColumn(name="permissionId")})
    private List&lt;SysPermission&gt; permissions;

    // 用户 - 角色关系定义;
    @ManyToMany
    @JoinTable(name="SysUserRole",joinColumns={<!-- -->@JoinColumn(name="roleId")},inverseJoinColumns={<!-- -->@JoinColumn(name="uid")})
    private List&lt;SysUser&gt; userInfos;// 一个角色对应多个用户

    public Integer getId() {<!-- -->
        return id;
    }

    public void setId(Integer id) {<!-- -->
        this.id = id;
    }

    public String getRole() {<!-- -->
        return role;
    }

    public void setRole(String role) {<!-- -->
        this.role = role;
    }

    public String getDescription() {<!-- -->
        return description;
    }

    public void setDescription(String description) {<!-- -->
        this.description = description;
    }

    public Boolean getAvailable() {<!-- -->
        return available;
    }

    public void setAvailable(Boolean available) {<!-- -->
        this.available = available;
    }

    public List&lt;SysPermission&gt; getPermissions() {<!-- -->
        return permissions;
    }

    public void setPermissions(List&lt;SysPermission&gt; permissions) {<!-- -->
        this.permissions = permissions;
    }

    public List&lt;SysUser&gt; getUserInfos() {<!-- -->
        return userInfos;
    }

    public void setUserInfos(List&lt;SysUser&gt; userInfos) {<!-- -->
        this.userInfos = userInfos;
    }
}

```

权限信息

```
@Entity
public class SysPermission implements Serializable {<!-- -->
    @Id@GeneratedValue
    private Integer id;//主键.
    private String name;//名称.
    @Column(columnDefinition="enum('menu','button')")
    private String resourceType;//资源类型，[menu|button]
    private String url;//资源路径.
    private String permission; //权限字符串,menu例子：role:*，button例子：role:create,role:update,role:delete,role:view
    private Long parentId; //父编号
    private String parentIds; //父编号列表
    private Boolean available = Boolean.FALSE;
    @ManyToMany
    @JoinTable(name="SysRolePermission",joinColumns={<!-- -->@JoinColumn(name="permissionId")},inverseJoinColumns={<!-- -->@JoinColumn(name="roleId")})
    private List&lt;SysRole&gt; roles;

    public Integer getId() {<!-- -->
        return id;
    }

    public void setId(Integer id) {<!-- -->
        this.id = id;
    }

    public String getName() {<!-- -->
        return name;
    }

    public void setName(String name) {<!-- -->
        this.name = name;
    }

    public String getResourceType() {<!-- -->
        return resourceType;
    }

    public void setResourceType(String resourceType) {<!-- -->
        this.resourceType = resourceType;
    }

    public String getUrl() {<!-- -->
        return url;
    }

    public void setUrl(String url) {<!-- -->
        this.url = url;
    }

    public String getPermission() {<!-- -->
        return permission;
    }

    public void setPermission(String permission) {<!-- -->
        this.permission = permission;
    }

    public Long getParentId() {<!-- -->
        return parentId;
    }

    public void setParentId(Long parentId) {<!-- -->
        this.parentId = parentId;
    }

    public String getParentIds() {<!-- -->
        return parentIds;
    }

    public void setParentIds(String parentIds) {<!-- -->
        this.parentIds = parentIds;
    }

    public Boolean getAvailable() {<!-- -->
        return available;
    }

    public void setAvailable(Boolean available) {<!-- -->
        this.available = available;
    }

    public List&lt;SysRole&gt; getRoles() {<!-- -->
        return roles;
    }

    public void setRoles(List&lt;SysRole&gt; roles) {<!-- -->
        this.roles = roles;
    }
}

```

**4）Shiro 配置**

```
@Configuration
public class MyShiroConfig {<!-- -->
  @Bean
  public ShiroFilterFactoryBean shirFilter(SecurityManager securityManager) {<!-- -->
    System.out.println("ShiroConfiguration.shirFilter()");
    ShiroFilterFactoryBean shiroFilterFactoryBean = new ShiroFilterFactoryBean();
    shiroFilterFactoryBean.setSecurityManager(securityManager);
    //拦截器.
    Map&lt;String,String&gt; filterChainDefinitionMap = new LinkedHashMap&lt;String,String&gt;();
    // 配置不会被拦截的链接 顺序判断
    filterChainDefinitionMap.put("/static/**", "anon");
    //配置退出 过滤器,其中的具体的退出代码Shiro已经替我们实现了
    filterChainDefinitionMap.put("/logout", "logout");
    //过滤链定义，authc:所有url都必须认证通过才可以访问; anon:所有url都都可以匿名访问
    filterChainDefinitionMap.put("/**", "authc");
    // 如果不设置默认会自动寻找Web工程根目录下的"/login.jsp"页面
    shiroFilterFactoryBean.setLoginUrl("/login");
    // 登录成功后要跳转的链接
    shiroFilterFactoryBean.setSuccessUrl("/index");

    //未授权界面;
    shiroFilterFactoryBean.setUnauthorizedUrl("/403");
    shiroFilterFactoryBean.setFilterChainDefinitionMap(filterChainDefinitionMap);
    return shiroFilterFactoryBean;
  }

  /**
   * 凭证匹配器
   * （由于我们的密码校验交给Shiro的SimpleAuthenticationInfo进行处理了）
   * @return
   */
  @Bean
  public HashedCredentialsMatcher hashedCredentialsMatcher(){<!-- -->
    HashedCredentialsMatcher hashedCredentialsMatcher = new HashedCredentialsMatcher();
    hashedCredentialsMatcher.setHashAlgorithmName("md5");//散列算法:使用MD5算法;
    hashedCredentialsMatcher.setHashIterations(2);//散列的次数，相当于 md5(md5(""));
    return hashedCredentialsMatcher;
  }

  @Bean
  public MyShiroRealm myShiroRealm(){<!-- -->
    MyShiroRealm myShiroRealm = new MyShiroRealm();
    myShiroRealm.setCredentialsMatcher(hashedCredentialsMatcher());
    return myShiroRealm;
  }


  @Bean
  public SecurityManager securityManager(){<!-- -->
    DefaultWebSecurityManager securityManager =  new DefaultWebSecurityManager();
    securityManager.setRealm(myShiroRealm());
    return securityManager;
  }

  /**
   *  开启shiro aop注解支持.
   *  使用代理方式;所以需要开启代码支持;
   * @param securityManager
   * @return
   */
  @Bean
  public AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor(SecurityManager securityManager){<!-- -->
    AuthorizationAttributeSourceAdvisor authorizationAttributeSourceAdvisor = new AuthorizationAttributeSourceAdvisor();
    authorizationAttributeSourceAdvisor.setSecurityManager(securityManager);
    return authorizationAttributeSourceAdvisor;
  }

  @Bean(name="simpleMappingExceptionResolver")
  public SimpleMappingExceptionResolver
  createSimpleMappingExceptionResolver() {<!-- -->
    SimpleMappingExceptionResolver r = new SimpleMappingExceptionResolver();
    Properties mappings = new Properties();
    mappings.setProperty("DatabaseException", "databaseError");//数据库异常处理
    mappings.setProperty("UnauthorizedException","403");
    r.setExceptionMappings(mappings);
    r.setDefaultErrorView("error");
    r.setExceptionAttribute("ex");
    return r;
  }
}

```

```
public class MyShiroRealm extends AuthorizingRealm {<!-- -->
    @Resource
    private SysUserService sysUserService;
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {<!-- -->
        SimpleAuthorizationInfo authorizationInfo = new SimpleAuthorizationInfo();
        SysUser sysUser  = (SysUser)principals.getPrimaryPrincipal();
        for(SysRole role:sysUser.getRoleList()){<!-- -->
            authorizationInfo.addRole(role.getRole());
            for(SysPermission p:role.getPermissions()){<!-- -->
                authorizationInfo.addStringPermission(p.getPermission());
            }
        }
        return authorizationInfo;
    }

    /*主要是用来进行身份认证的，也就是说验证用户输入的账号和密码是否正确。*/
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token)
            throws AuthenticationException {<!-- -->
        System.out.println("MyShiroRealm.doGetAuthenticationInfo()");
        //获取用户的输入的账号.
        String username = (String)token.getPrincipal();
        System.out.println(token.getCredentials());
        //通过username从数据库中查找 User对象，如果找到，没找到.
        //实际项目中，这里可以根据实际情况做缓存，如果不做，Shiro自己也是有时间间隔机制，2分钟内不会重复执行该方法
        SysUser sysUser = sysUserService.findByUsername(username);
        System.out.println("sysUser:   "+sysUser);
        if(sysUser == null){<!-- -->
            return null;
        }
        SimpleAuthenticationInfo authenticationInfo = new SimpleAuthenticationInfo(
                sysUser, //用户
                sysUser.getPassword(), //密码
                ByteSource.Util.bytes(sysUser.getCredentialsSalt()),//salt=username+salt
                getName()  //realm name
        );
        return authenticationInfo;
    }
}

```

**5）Dao 层实现**

```
public interface SysUserDao extends CrudRepository&lt;SysUser,Long&gt; {<!-- -->
    public SysUser findByUsername(String username);
}

```

**6）Service 层实现**

```
public interface SysUserService {<!-- -->
    public SysUser findByUsername(String username);
}

```

```
@Service
public class SysUserServiceImpl implements SysUserService {<!-- -->
    @Resource
    private SysUserDao sysUserDao;
    @Override
    public SysUser findByUsername(String username) {<!-- -->
        System.out.println("UserInfoServiceImpl.findByUsername()");
        return sysUserDao.findByUsername(username);
    }
}

```

**7）Controller 层实现**

```
@Controller
@RequestMapping("/sysUser")
public class SysUserController {<!-- -->

    /**
     * 用户查询.
     * @return
     */
    @RequestMapping("/query")
    @RequiresPermissions("sysUser:query")
    public String userList(){<!-- -->
        return "queryUser";
    }

    /**
     * 用户添加;
     * @return
     */
    @RequestMapping("/add")
    @RequiresPermissions("sysUser:add")
    public String addUser(){<!-- -->
        return "addUser";
    }

    /**
     * 用户删除;
     * @return
     */
    @RequestMapping("/del")
    @RequiresPermissions("sysUser:del")
    public String delUser(){<!-- -->
        return "delUser";
    }
}

```

```
@Controller
public class HomeController {<!-- -->
    @RequestMapping({<!-- -->"/","/index"})
    public String index(){<!-- -->
        return"/index";
    }

    @RequestMapping("/login")
    public String login(HttpServletRequest request, Map&lt;String, Object&gt; map) throws Exception{<!-- -->
        System.out.println("HomeController.login()");
        // 登录失败从request中获取shiro处理的异常信息。
        // shiroLoginFailure:异常类的全类名.
        String exception = (String) request.getAttribute("shiroLoginFailure");
        System.out.println("exception=" + exception);
        String msg = "";
        if (exception != null) {<!-- -->
            if (UnknownAccountException.class.getName().equals(exception)) {<!-- -->
                System.out.println("UnknownAccountException -- &gt; 账号不存在");
                msg = "UnknownAccountException -- &gt; 账号不存在";
            } else if (IncorrectCredentialsException.class.getName().equals(exception)) {<!-- -->
                System.out.println("IncorrectCredentialsException -- &gt; 密码不正确");
                msg = "IncorrectCredentialsException -- &gt; 密码不正确";
            } else if ("kaptchaValidateFailed".equals(exception)) {<!-- -->
                System.out.println("kaptchaValidateFailed -- &gt; 验证码错误");
                msg = "kaptchaValidateFailed -- &gt; 验证码错误";
            } else {<!-- -->
                msg = "other "+exception;
                System.out.println("other -- &gt;" + exception);
            }
        }else {<!-- -->
            msg = "";
        }
        map.put("msg", msg);
        // 此方法不处理登录成功,由shiro进行处理
        return "/login";
    }

    @RequestMapping("/403")
    public String unauthorizedRole(){<!-- -->
        System.out.println("403 -- &gt; 没有权限");
        return "403";
    }
}

```

**8）新建 6 个简单页面**

index.html（首页）

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;index&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;首页&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;

```

login.html（登录页）

```
&lt;!DOCTYPE html&gt;
&lt;html xmlns:th="http://www.thymeleaf.org"&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;login&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;form action="" method="post"&gt;
    &lt;p&gt;账号：&lt;input type="text" name="username" value="admin"/&gt;&lt;/p&gt;
    &lt;p&gt;密码：&lt;input type="text" name="password" value="123456"/&gt;&lt;/p&gt;
    &lt;p&gt;&lt;input type="submit" value="登录"/&gt;&lt;/p&gt;
&lt;/form&gt;
&lt;div th:if="${msg != null &amp;&amp; msg != ''}"&gt;
    错误信息：&lt;h4 th:text="${msg}"&gt;&lt;/h4&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

addUser.html（新增页）

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;addUser&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;新增界面&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;

```

delUser.html（删除页）

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;delUser&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h3&gt;删除界面&lt;/h3&gt;
&lt;/body&gt;
&lt;/html&gt;

```

queryUser.html（查询页）

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;queryUser&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;查询界面&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;

```

403.html（无权限提示页面）

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;403&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;没有权限&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;

```

**9）新增几条数据**

```
INSERT INTO `sys_user` (`uid`,`username`,`name`,`password`,`salt`,`state`) VALUES ('1', 'admin', '管理员', 'd3c59d25033dbf980d29554025c23a75', '8d78869f470951332959580424d4bf4f', 0);
INSERT INTO `sys_permission` (`id`,`available`,`name`,`parent_id`,`parent_ids`,`permission`,`resource_type`,`url`) VALUES (1,0,'查询用用',0,'0/','sysUser:query','menu','sysUser/query');
INSERT INTO `sys_permission` (`id`,`available`,`name`,`parent_id`,`parent_ids`,`permission`,`resource_type`,`url`) VALUES (2,0,'新增用户',1,'0/1','sysUser:add','button','sysUser/add');
INSERT INTO `sys_permission` (`id`,`available`,`name`,`parent_id`,`parent_ids`,`permission`,`resource_type`,`url`) VALUES (3,0,'删除用户',1,'0/1','sysUser:del','button','sysUser/del');
INSERT INTO `sys_role` (`id`,`available`,`description`,`role`) VALUES (1,0,'管理员','admin');
INSERT INTO `sys_role` (`id`,`available`,`description`,`role`) VALUES (3,1,'测试','test');
INSERT INTO `sys_role_permission` (`permission_id`,`role_id`) VALUES (1,1);
INSERT INTO `sys_role_permission` (`permission_id`,`role_id`) VALUES (2,1);
INSERT INTO `sys_role_permission` (`permission_id`,`role_id`) VALUES (3,2);
INSERT INTO `sys_user_role` (`role_id`,`uid`) VALUES (1,1);

```

### 3 测试

1、访问 http://localhost:8080/index ，由于未登录跳转到首页 http://localhost:8080/login； 2、点击登录，登录后再访问 http://localhost:8080/index 和 http://localhost:8080/sysUser/add 正常跳转；再访问 http://localhost:8080/sysUser/del,跳转到没有权限提示页面。 `注`：MyShiroRealm 的 doGetAuthorizationInfo 方法进行权限校验。

参考： 

<img src="https://img-blog.csdnimg.cn/20191007101439261.JPG#pic_center" alt="在这里插入图片描述" width="600" height="350">
