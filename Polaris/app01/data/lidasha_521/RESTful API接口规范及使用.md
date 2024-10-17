
--- 
title:  RESTful API接口规范及使用 
tags: []
categories: [] 

---


#### RESTful API接口规范及使用



>  
 REST 指的是一组架构和原则。满足这些约束条件和原则的应用程序或设计就是 RESTful。 

- 非Rest设计，以往我们都会这么写：以不同的URL进行不通的操作
```
@RestController
@RequestMapping("/user")
@Api(tags = "用户管理模块")
public class UserController{<!-- -->

	@Resource
    private UserService userService;

	/** 添加用户 */
	@RequestMapping("/addUser")
	public String addUser(User user){<!-- -->
		return userService.addUser(user);
	}
	
	/** 删除用户 */
	@RequestMapping("/deleteUser")
	public String deleteUser(String userId){<!-- -->
		return userService.deleteUser(user);
	}
	
	/** 修改用户 */
	@RequestMapping("/updateUser")
	public String updateUser(User user){<!-- -->
		return userService.updateUser(userId);
	}
	
	/** 查询用户 */
	@RequestMapping("/queryUser")
	public User queryUser(String userId){<!-- -->
		return userService.queryUser(userId);
	}
}

```

（添加用户）

 （删除用户）

 （更新用户）

 （查询用户）
<li>Rest架构： 
  <ul>- 在我们定义一个接口的URL时，可以通过以下两种方式实现<li>第一种方式：指定请求方式 
    <ul>- `@RequestMapping(value ="/user", method = RequestMethod.GET)` 查询- `@RequestMapping(value ="/user", method = RequestMethod.POST)`添加或修改- `@RequestMapping(value ="/user", method = RequestMethod.PUT)` 修改- `@RequestMapping(value ="/user", method = RequestMethod.DELETE)` 删除- `@PostMapping("/user")` 添加或修改- `@DeleteMapping("/user/{userId}")` 删除- `@PutMapping("/user")` 修改- `@GetMapping("/user/{userId}")`查询
```
@RestController
@RequestMapping("/admin")
@Api(tags = "用户管理模块")
public class UserController{<!-- -->

	@Resource
    private UserService userService;

	/**添加用户*/
	@PostMapping("/user")
	@RequestMapping(value = "/user", method = RequestMethod.POST)
	public String addUser(User user){<!-- -->
		return userService.addUser(user);
	}
	
	/**删除用户*/
	@DeleteMapping("/user/{userId}")
	@RequestMapping(value ="/user", method = RequestMethod.DELETE)
	public String deleteUser(@PathVariable("/userId")String userId){<!-- -->
		return userService.deleteUser(userId);
	}
	
	/**修改用户*/
	@PutMapping("/user")
	@RequestMapping(value ="/user", method = RequestMethod.PUT)
	// @PostMapping("/user")  // 也可以用 PostMapping
    // @RequestMapping(value = "/user", method = RequestMethod.POST)
    public String updateUser(User user){<!-- -->
		return userService.updateUser(user);
	}
	
	/**查询用户*/
	@GetMapping("/user/{userId}")
	@RequestMapping(value ="/user", method = RequestMethod.GET)
	public User queryUser(@PathVariable("/userId")String userId){<!-- -->
		return userService.queryUser(userId);
	}
}

```

 （查询用户ID为1的数据信息）

 （删除用户ID为1的数据信息）
<li>RESTfui API接口响应的资源（返回给前端的数据格式）的表现形式为`JSON`或`XML` 
  <ul>- 方式一：在控制类（controller类）上添加`@ResponseBody` 注解- 方式二：在每个接口的方法上添加`@ResponseBody` 注解- 方式三：直接在控制类（controller类）使用`@RestController注解`<li>前端通过无状态的http协议与后端进行接口交互 
  <ul>- 无状态：每一次请求都是独立的，每一次请求都不会有请求记录
 

```
200：服务器成功返回用户请求的数据，该操作是幂等的。
201：用户新建或修改数据成功。
202：表示一个请求已经进入后台排队（异步任务）
204：用户删除数据成功。
301：永久重定向
302：暂时重定向
400：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401：表示用户没有权限（令牌、用户名、密码错误）。
403：表示用户得到授权（与401错误相对），但是访问是被禁止的。
404：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410：用户请求的资源被永久删除，且不会再得到的。
422：当创建一个对象时，发生一个验证错误。
500：服务器发生错误，用户将无法判断发出的请求是否成功。

```
