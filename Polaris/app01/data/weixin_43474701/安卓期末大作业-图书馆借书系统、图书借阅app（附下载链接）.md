
--- 
title:  安卓期末大作业-图书馆借书系统、图书借阅app（附下载链接） 
tags: []
categories: [] 

---
### 安卓期末大作业-图书馆借书系统、借书APP（可以注册登录，保存数据记录，含源码和导出app,运行截图）

安卓期末大作业，图书借阅APP，老师给了95分，可以注册登录，借阅书籍，还书，含数据库存储借书记录，导入AndroidStudio即可使用，代码注释详细  <img src="https://img-blog.csdnimg.cn/971b83b1682f426099378f56bb5a933b.png" alt="在这里插入图片描述">

进入APP界面： <img src="https://img-blog.csdnimg.cn/746bdc4059c24a22ac64af322ddf272c.png" alt="请添加图片描述">

注册登录界面如下所示： <img src="https://img-blog.csdnimg.cn/014fe3fbc8a5467e971c0edc013a6878.png" alt="请添加图片描述"> 登录界面： <img src="https://img-blog.csdnimg.cn/a7cbc673699144838b893c7394be0505.png" alt="请添加图片描述"> 注册部分代码： @Override protected void onStop() {<!-- --> super.onStop(); //关闭数据库连接 // mHelper.closeLink(); } @Override public void onClick(View v) {<!-- --> String uid = et_userid.getText().toString(); String pwd = et_pwd.getText().toString(); int User_status = 0; Intent intent = new Intent(); switch (v.getId()) {<!-- --> case R.id.btn_login: list = mHelper.queryByUid(uid, pwd); for (User u : list) {<!-- --> Log.e(“ning”, u.toString()); System.out.println(“超市菜市场测试测试测试测试测试测试从” + u.getUserid()); if (u.getUserid().equals(uid)) if (u.getPassword() == Long.parseLong(pwd)) {<!-- --> ToastUtil.show(this, “登录成功”); // intent.putExtra(“uid”, uid); User_status = u.getUser_status(); //用SharedPreferences 将uid存起来，方便后面的页面使用 SharedPreferences.Editor edit = preferences.edit(); edit.putString(“uid”, uid); edit.putInt(“User_status”, User_status); edit.apply(); intent.setClass(this, MainActivity.class); startActivity(intent); } } break; case R.id.btn_register: ToastUtil.show(this, “注册”); intent.setClass(LoginActivity.this, RegisterActivity.class); startActivity(intent); break; }

**可以修改账号密码：** <img src="https://img-blog.csdnimg.cn/54798b9289824a6a94ca176c392dd9c0.png" alt="请添加图片描述"> 主页界面如下所示： <img src="https://img-blog.csdnimg.cn/f23a8d9b6ec1487d8aa4e6fe129c654e.png" alt="请添加图片描述"> 借书界面如下图所示： <img src="https://img-blog.csdnimg.cn/9a9fb95be4264542b1c83844313f9e5c.png" alt="请添加图片描述"> 借书记录如下图所示： <img src="https://img-blog.csdnimg.cn/ec449454706b4d1f895f9667b4a972c8.png" alt="请添加图片描述"> 点我下载项目源码 
