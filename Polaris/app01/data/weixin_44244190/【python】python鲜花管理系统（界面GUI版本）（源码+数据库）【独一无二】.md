
--- 
title:  【python】python鲜花管理系统（界面GUI版本）（源码+数据库）【独一无二】 
tags: []
categories: [] 

---
>  
 <img src="https://img-blog.csdnimg.cn/6e2c8c7bccdc41cd911dc26a692693a2.jpeg" alt="请添加图片描述"> 
 <hr> 
 👉博__主👈：米码收割机 👉技__能👈：C++/Python语言 👉公众号👈：测试开发自动化【获取源码+商业合作】 👉荣__誉👈：阿里云博客专家博主、51CTO技术博主 👉专__注👈：专注主流机器人、人工智能等相关领域的开发、测试技术。 


>  
 <h2>python鲜花管理系统（GUI版本）（源码+数据库）【独一无二】</h2> 
 <hr> 
  
  
  <h4>目录</h4> 
  - - - - <ul><li>- - - - - -  
   </li>- </ul> 
  
  


## 一、设计要求
<li> **登录功能**： 
  1. 用户可以输入用户名和密码进行登录。1. 提供了一个登录窗口（`LoginWindow`类），用户输入正确的用户名和密码后，可以根据用户角色（管理员或普通用户）打开对应的窗口。 </li><li> **用户界面**（`UserWindow`类）： 
  1. 用户可以查看花店中的花卉列表。1. 可以将选定的花卉添加到购物车中。1. 可以查看购物车中的花卉，并进行结账。 </li><li> **管理员界面**（`AdminWindow`类）： 
  1. 管理员可以查看花店中的花卉列表。1. 可以添加新的花卉到花店的库存中。1. 可以查看订单列表。 </li><li> **购物车功能**（`CartWindow`类）： 
  1. 用户可以查看购物车中的花卉。1. 用户可以从花卉列表中选择花卉，添加到购物车中。1. 用户可以结账，将购物车中的花卉结算。 </li><li> **数据存储**： 
  1. 用户、花卉、购物车等数据以文本文件形式存储，通过`.sql`文件扩展名进行标识，如`flower.sql`、`cart.sql`、`orders.sql`等。1. 用户的用户名、密码和角色信息存储在`users`字典中。1. 花卉信息以及订单信息也存储在相应的文本文件中。 </li>- 用户可以查看花店中的花卉列表。- 可以将选定的花卉添加到购物车中。- 可以查看购物车中的花卉，并进行结账。- 用户可以查看购物车中的花卉。- 用户可以从花卉列表中选择花卉，添加到购物车中。- 用户可以结账，将购物车中的花卉结算。
总体而言，这个应用程序实现了一个花店管理系统，提供了基本的用户登录、购物、结账、管理员管理等功能。

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 


## 二、功能展示

>  
 `管理账号`：admin `密码`：admin123 `用户账号`：user `密码`：user123 


### 2.1. 管理员/用户登录

<img src="https://img-blog.csdnimg.cn/direct/40ac458b597d4969a76d2d3fe6cb3b14.png" alt="在这里插入图片描述">

### 2.2. 管理员界面

<img src="https://img-blog.csdnimg.cn/direct/d982eb5ccea74e2a946a9598f96256eb.png" alt="在这里插入图片描述">

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 


### 2.3. 上架商品

<img src="https://img-blog.csdnimg.cn/direct/bec0e968c89344f8b9b34a5340664c64.png" alt="在这里插入图片描述">

### 2.4. 卖家界面

<img src="https://img-blog.csdnimg.cn/direct/3d9297ec7f6748ebb70011a07828f3ca.png" alt="在这里插入图片描述">

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 


### 2.5. 添加商品至购物车

<img src="https://img-blog.csdnimg.cn/direct/a57bf2aab99044f28c915b5a41573259.png" alt="在这里插入图片描述">

### 2.6. 查看购物车商品

<img src="https://img-blog.csdnimg.cn/direct/a7e028e1435743858a36b0847fc2bdb0.png" alt="在这里插入图片描述">

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 


### 2.7. 结账

<img src="https://img-blog.csdnimg.cn/direct/4500bbed54fa43908d864caf3e13bf92.png" alt="在这里插入图片描述">

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 


## 三、代码展示

`部分代码`展示如下：

```

class UserWindow(object):
    def __init__(self, app):
        super().__init__()
        self.app = app
        #&gt;👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈


    def add_to_cart(self):
        selected_row = self.flowers_table.currentRow()
        if selected_row != -1:
            flower_type = self.flowers_table.item(selected_row, 0).text()
            flower_color = self.flowers_table.item(selected_row, 1).text()
            flower_price = self.flowers_table.item(selected_row, 2).text()
            self.cart.append({<!-- -->"type": flower_type, "color": flower_color, "price": flower_price})
        QMessageBox.information(self, "添加到购物车", "已添加选中的花到购物车。")
		# &gt;👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈

class FlowerShopApp:
    def __init__(self):
        self.login_window = LoginWindow(self)
        self.user_window = UserWindow(self)
        self.admin_window = AdminWindow()
        self.cart_window = CartWindow()

    def open_user_window(self):
        self.user_window.show()

    def open_admin_window(self):
        self.admin_window.show()

    def open_cart_window(self):
        self.cart_window.load_cart()
        self.cart_window.show()

```

>  
 👉👉👉 `源码获取` 关注【测试开发自动化】公众号，回复 “ 鲜花管理系统 ” 获取。👈👈👈 

