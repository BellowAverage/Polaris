
--- 
title:  2023安卓期末大作业-记事本app（含数据库可以登录，含下载链接，含完整源码+程序设计报告+运行视频+apk导出文件） 
tags: []
categories: [] 

---
### 2023安卓期末大作业-记事本app（可以登录，含完整源码+程序设计报告+运行视频+apk导出文件）

 打包文件如下图所示: <img src="https://img-blog.csdnimg.cn/direct/2293e83c02314510af947fb84cf97bab.png" alt="在这里插入图片描述"> 基于Android系统的简单记事本，它能够便携记录生活和工作的诸多事情,从而帮助人们有条理的进行时间管理。一个记事本，能够输入标题和内容，创建日期、最新修改日期等信息。如果没有输入标题则使用内容的第一句话作为标题，创建日期和修改日期均由系统自动生成，无需用户干预。 实现了简单的记事本功能，`登录`，`新建笔记`，`删除笔记`，`保存笔记`，显示第一条笔记内容和标题。 此次做的Android简易记事本的存储方式使用了`SQlite数据库`，然后界面的实现比较简单，但是，具有`增删改查`的基本功能。 查看笔记数量，查看最后一条笔记的内容和标题等基础功能，其中笔记通过数据库保存，重启不丢失。 结构图如下所示： <img src="https://img-blog.csdnimg.cn/direct/37d9fefb246141cbbefa4db0f561633e.png" alt="在这里插入图片描述"> <img src="https://img-blog.csdnimg.cn/direct/be4e67b565e94d8eada053148462dd6a.png" alt="在这里插入图片描述">

app截图如下所示： **登陆界面：** <img src="https://img-blog.csdnimg.cn/direct/70769fd3d4f548b99847a430481c8052.png" alt="在这里插入图片描述"> **记事本主界面：** <img src="https://img-blog.csdnimg.cn/direct/71677149b12c41bbbe340480ef845ffa.png" alt="在这里插入图片描述"> **记事功能界面：** <img src="https://img-blog.csdnimg.cn/direct/53ddb0e135394e80891208fb9db37d1c.png" alt="在这里插入图片描述"> **保存后主界面：** <img src="https://img-blog.csdnimg.cn/direct/0bb46dddee34451faefe8332e025e6f9.png" alt="在这里插入图片描述"> 部分代码展示，注释非常详细： //设置组件点击事件 note_back.setOnClickListener(this); switch (v.getId()) {<!-- --> case R.id.note_back: //返回键的点击事件 finish(); break; case R.id.delete: //删除按钮的点击事件 content.setText(“”); break; case R.id.note_save: //保存按钮的点击事件 //拿到顶部输入框的数据 String noteContent=content.getText().toString().trim(); if (id != null){//修改操作 //id != null 是上个页面点击列表进来，执行修改操作的 if (noteContent.length()&gt;0){<!-- --> //数据库更新这条数据 if (mSQLiteHelper.updateData(id, noteContent, DBUtils.getTime(),noteTitle.getText().toString())){<!-- --> //数据库更新成功，销毁页面，返回上级页面 showToast(“修改成功”); case R.id.last: //点击上一条的点击事件 SQLiteHelper sqLiteHelper = new SQLiteHelper(this); //把id-1,根据id去查询上一条数据 i =Integer.parseInt(id)-1; id=i+“”;


