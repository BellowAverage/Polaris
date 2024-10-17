
--- 
title:  2023毕业设计-基于Java的公交管理系统（完整源码+sql源文件【附下载链接】） 
tags: []
categories: [] 

---
### 2023毕业设计-公交管理系统（完整源码+sql源文件）

****

系统技术 前端 layui ajax 后端 springBoot mybatis-plus 运行环境 JDk 1.8 maven 3.6.1 mysql 5.8及其以上版本 项目编写工具 idea 系统前台效果

<img src="https://img-blog.csdnimg.cn/5ce793d14fa64ce892f3e25db8d7dd63.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/b598724df4ee45248c443e676c29706b.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/3bd3e32721dd42eb8dd28c1ac1e25154.png" alt="在这里插入图片描述">

<img src="https://img-blog.csdnimg.cn/7349232f58864cdca8dd63f4636d5732.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/001145cb7b634fe99506beb4bb138ffd.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/c7cf0bcbcff94fd78a442f3413d880e6.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/9d5df84df99b440c92865126d0c727ef.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/794754f2bb82445794825df2d7623de3.png" alt="在这里插入图片描述">

部分代码展示： /**
-  首页控制器 <li> @author Administrator **/ @Controller public class IndexController {<!-- --> @Autowired UserService userService; @Autowired InfoService infoService; @Autowired NoticeService noticeService; @Autowired VehicleService vehicleService; @Autowired SiteService siteService; @Autowired RouteSiteService routeSiteService; @Autowired RouteService routeService;//线路 /*** 
  <ul>- 首页跳转- @return */ @GetMapping(“”) public String index(Model model) {<!-- --> //获去网站信息 Info info = infoService.getInfo(); //获取公告信息 List noticeList = noticeService.getWebNoticeList(); //获取6条公交信息 List vehicleList=vehicleService.getSixVehicle(); //返回网站信息 model.addAttribute(“info”,info); model.addAttribute(“noticeList”,noticeList); model.addAttribute(“vehicleList”,vehicleList); return “index”; }
@GetMapping(“/goUser/{id}”) public String goUser(Model model, @PathVariable Long id){<!-- --> //根据id获取用户对象 User user = userService.getById(id); model.addAttribute(“user”,user); return “userInfo”; }

/**
- 根据id获取公交信息- @param id- @return */ @GetMapping(“/getVehicle/{id}”) public String getVehicleById(@PathVariable Long id, Model model){<!-- --> //获取公交信息 WebVehicleInfo webVehicleInfo=vehicleService.getwebVehicleInfoById(id); //获取公交中间站点信息 WebVehicleSiteInfo webSiteInfo=vehicleService.getwebVehicleSiteInfoById(id); webSiteInfo.setMiddleSite(webSiteInfo.getMiddleSite()!=null?webSiteInfo.getMiddleSite().replaceAll(“,”,“–&gt;”):“”); model.addAttribute(“webVehicleInfo”,webVehicleInfo); model.addAttribute(“webSiteInfo”,webSiteInfo); return “vehicleInfo”;
}

/**
- 公交信息页跳转- @return */ @GetMapping(“/vehicle”) public String goVehicle(Model model,String name,Long endSite,Long startSite) {<!-- --> //获取站点信息 List siteList=siteService.getSiteList(); //传递站点信息 model.addAttribute(“siteList”,siteList); //获取公交数据 /**VehicleVo vehicleVo = new VehicleVo(); vehicleVo.setStartSite(startSite); vehicleVo.setEndSite(endSite); vehicleVo.setLimit(10000); vehicleVo.setPage(1); vehicleVo.setName(name); List list; if(vehicleVo.getStartSite()==null &amp;&amp; vehicleVo.getEndSite()==null){<!-- --> //根据名字查询以及正常查询 list=vehicleService.getVehicleList(vehicleVo); model.addAttribute(“WebVehicleList”,list); }else {<!-- --> //根据路线查询 list=vehicleService.getVehicleListByRoute(vehicleVo); model.addAttribute(“WebVehicleList”,list); }**/ return “vehicle”; }

