
--- 
title:  laravel5.8中实现验证码组件的安装和验证 
tags: []
categories: [] 

---
>  
 本篇文章主要讲解使用laravel5.8自带的验证码库实现验证码验证的效果教程。通过本教程你可以快速接入到自己的项目中开发相应的验证功能。 作者：任聪聪 (rccblogs.com) 日期：2023年12月17日 


## 实际效果

<img src="https://img-blog.csdnimg.cn/img_convert/22c384f278de63cfd11a954315ef162b.png" alt="file">

## 安装步骤

### 步骤一、输入命令

```
composer require mews/captcha

```

<img src="https://img-blog.csdnimg.cn/img_convert/b3f9b5d2585ec3b843cc2681226beb35.png" alt="file">

### 步骤二、配置 config/app.php文件内容

1.providers部分

```
        Mews\Captcha\CaptchaServiceProvider::class,

```

2.aliases 部分

```
        'Captcha' =&gt; Mews\Captcha\Facades\Captcha::class,

```

### 步骤三、发布

```
php artisan vendor:publish

```

弹出下面信息时，依据自己对应的编号继续输入即可 <img src="https://img-blog.csdnimg.cn/img_convert/aec30a7c12ee67a9abf3394e11b6ec48.png" alt="file">

这里我输入的是数字：9

#### 发布成功提示：

```
Copied File [\vendor\mews\captcha\config\captcha.php] To [\config\captcha.php]
Publishing complete.

E:\develop\php\51powand&gt;

```

## 使用验证码

### 一、配置验证码信息

<img src="https://img-blog.csdnimg.cn/img_convert/38c28ca4193cdf507d6b0c97bb77597e.png" alt="file"> 在新的验证码的配置文件中。 <img src="https://img-blog.csdnimg.cn/direct/2bd51b6983f84111bc2b387d865f9582.png" alt="在这里插入图片描述">

### 二、页面中调用

```
                            &lt;img src="{<!-- -->{captcha_src()}}" style="cursor: pointer" onclick="this.src='{<!-- -->{captcha_src()}}'+Math.random()" &gt;


```

### 三、方法中进行验证

```
			use Illuminate\Support\Facades\Validator;
			
			
			
			$messages = [
                'verificationCode.required' =&gt; '验证码不可为空',
                'verificationCode.captcha' =&gt; '验证码错误',
            ];
			
            $validator = Validator::make($request-&gt;all(), [
                'verificationCode' =&gt; 'required|captcha',
            ], $messages);
			
            if ($validator-&gt;fails()) {<!-- -->
                $errorMessage = $validator-&gt;errors()-&gt;first();
                return $errorMessage;
            }


```
