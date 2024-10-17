
--- 
title:  安卓期末大作业-调色App（源码+导出apk+运行截图） 
tags: []
categories: [] 

---
### 安卓期末大作业-调色App（源码+导出apk+运行截图）

开发软件：Android Studio 开发语言：Java 2023年上半年移动开发期末大作业，比较简单的一个安卓项目，导入即可使用，适合初学者学习使用 点我下载资源  **app进入界面：** <img src="https://img-blog.csdnimg.cn/b410c441255c49d1a7483bcba42e8f6c.png" alt="请添加图片描述"> **调色卡app主界面：** <img src="https://img-blog.csdnimg.cn/bcd3d73200e0492aada0fd9f50251261.png" alt="请添加图片描述"> <img src="https://img-blog.csdnimg.cn/dc2aa206502e48649965ca05d6d35f11.png" alt="请添加图片描述"> 可以复制颜色代码 <img src="https://img-blog.csdnimg.cn/5c44c6f9effd48eebbad430eb34ae70e.png" alt="请添加图片描述">

**App主要代码展示：** public class ColorDetail extends AppCompatActivity {<!-- --> private ListView listView; //父颜色名称 private String[] fColor; //子颜色数组 private String[] zColor; @Override protected void onCreate(Bundle savedInstanceState) {<!-- --> super.onCreate(savedInstanceState); setContentView(R.layout.activity_color_detail); //接收子颜色数组 rxd(); //设置状态栏 setBarColor(this, parseColor(fColor[1])); //设置父颜色标题 TextView tv_title = findViewById(R.id.item_ld_title); tv_title.setText(fColor[0]); //导航栏背景 RelativeLayout bar = findViewById(R.id.item_ld_bar); bar.setBackgroundColor(parseColor(fColor[1])); //载入子颜色列表 listView = findViewById(R.id.color_list); ZiListAdapter adapter = new ZiListAdapter(zColor, this); listView.setAdapter(adapter); //列表点击事件 listView.setOnItemClickListener((adapterView, view, i, l) -&gt; {<!-- --> //复制颜色值 String color = zColor[i].substring(1); clipContent(this, color); sToast(this, “已复制：” + color); }); } 
