
--- 
title:  Java过阿里NC滑块 
tags: []
categories: [] 

---
>  
 - Java+selenium- 获得滑块的sessiond+token- 阿里滑块是本地生成，当我们滑块成功后，会生成sessiond和token，当我们使用返回的参数时，会先通过阿里后端接口进行认证，阿里认证只会判断该sessiond和token是否使用过，就过了。- 因此，我们可以在本地通过selenium模拟人工进行滑动。 


##  一、H5页面

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;meta charset="utf-8" /&gt;
    &lt;script src="https://g.alicdn.com/AWSC/AWSC/awsc.js"&gt;&lt;/script&gt;
    &lt;script src="./jquery/request.js"&gt;&lt;/script&gt;
    &lt;script src="./jquery/jquery-3.2.1.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div id="nc"&gt;&lt;/div&gt;
&lt;div id="sessionId"&gt;&lt;/div&gt;
&lt;div id="sig"&gt;&lt;/div&gt;
&lt;div id="token"&gt;&lt;/div&gt;
&lt;script&gt;
    // 实例化nc
    AWSC.use("nc", function (state, module) {
        // 初始化
        window.nc = module.init({
            // 应用类型标识。它和使用场景标识（scene字段）一起决定了滑动验证的业务场景与后端对应使用的策略模型。您可以在阿里云验证码控制台的配置管理页签找到对应的appkey字段值，请务必正确填写。
            appkey: "FFFF0N0000000000A949",
            //使用场景标识。它和应用类型标识（appkey字段）一起决定了滑动验证的业务场景与后端对应使用的策略模型。您可以在阿里云验证码控制台的配置管理页签找到对应的scene值，请务必正确填写。
            scene: "nc_other_h5",
            // 声明滑动验证需要渲染的目标ID。
            renderTo: "nc",
            //前端滑动验证通过时会触发该回调参数。您可以在该回调参数中将会话ID（sessionId）、签名串（sig）、请求唯一标识（token）字段记录下来，随业务请求一同发送至您的服务端调用验签。
            success: function (data) {
                $("#sessionId").text(data.sessionId)
                $("#sig").text(data.sig)
                $("#token").text(data.token)
                // window.console &amp;&amp; console.log(data.sessionId)
                // window.console &amp;&amp; console.log(data.sig)
                // window.console &amp;&amp; console.log(data.token)
            },
            // 滑动验证失败时触发该回调参数。
            fail: function (failCode) {
                 window.console &amp;&amp; console.log(failCode)
            },
            // 验证码加载出现异常时触发该回调参数。
            error: function (errorCode) {
                 window.console &amp;&amp; console.log(errorCode)
            }
        });
    })
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

## 二、java+selenium

```
public static JSONObject openChrome(String drivePath, String htmlPath) {
        // 隐藏 window.navigator.webdriver
        ChromeOptions option = new ChromeOptions();
        option.addArguments("--incognito");//无痕
        option.addArguments("disable-cache");//禁缓存
        option.addArguments("--remote-allow-origins=*");
        option.setExperimentalOption("useAutomationExtension", false);
        option.setExperimentalOption("excludeSwitches", Lists.newArrayList("enable-automation"));
        option.addArguments("--disable-blink-features=AutomationControlled");//window.navigator.webdriver 开发出现true  正常出现false

        //设置为 headless 模式避免报错用的参数
        option.addArguments("--disable-gpu");

        //禁用沙箱
        option.addArguments("--no-sandbox");

        // 禁用阻止弹出窗口
        option.addArguments("--disable-popup-blocking");

        //使用后台打开chrome的方式
        //option.addArguments("--headless");

        JSONObject proxy = ProxyUtil.getProxy();
        //添加代理
        option.addArguments("--proxy-server=http://"+proxy.getString("sever")+":"+proxy.getInteger("port"));

        System.setProperty(FirefoxDriver.SystemProperty.BROWSER_LOGFILE, "/dev/null");
        System.setProperty("webdriver.chrome.driver", drivePath);
        // 1.打开Chrome浏览器
//        chromeDriver.get("file:///D:\\WorkSpace\\Java\\yslm\\src\\main\\resources\\static\\AliBaBa_nc.html");
        chromeDriver = new ChromeDriver(option);
        chromeDriver.get(htmlPath);
        return huakuai(chromeDriver);
    }

    public static JSONObject huakuai(ChromeDriver driver) {
        // 实例化鼠标操作对象Actions
        String sessionId = null, sig = null, token = null;
        JSONObject object = null;
        do {
            WebElement Slider = driver.findElement(By.xpath("//*[@id=\"nc_1_n1z\"]"));// 拿到滑块按钮
            Actions action = new Actions(driver);
            int count = 120;
            do {
                count += 60;
                action.dragAndDropBy(Slider, count, 0).perform();// 移动一定位置
            } while (count &lt; 300);
            WebDriver.Navigation navigate = driver.navigate();
            sessionId = driver.findElement(By.xpath("//*[@id=\"sessionId\"]")).getText();
            sig = driver.findElement(By.xpath("//*[@id=\"sig\"]")).getText();
            token = driver.findElement(By.xpath("//*[@id=\"token\"]")).getText();
//            System.out.println("sessionId:" + sessionId);
//            System.out.println("sig:" + sig);
//            System.out.println("token:" + token);
            log.info("--&gt;token:{}", token);
            object = new JSONObject();
            object.put("sessionId", sessionId);
            object.put("sig", sig);
            object.put("token", token);
            navigate.refresh();
        } while (sessionId == null || sig == null || token == null
                || sessionId.equals("") || sig.equals("") || token.equals(""));
        driver.close();
        driver.quit();
        System.out.println("结果："+object.toJSONString());
        return object;
    }
```
