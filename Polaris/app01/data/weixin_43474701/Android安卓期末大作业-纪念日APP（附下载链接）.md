
--- 
title:  Android安卓期末大作业-纪念日APP（附下载链接） 
tags: []
categories: [] 

---
### Android安卓期末大作业-纪念日APP

 `“我们”，记录结婚纪念日` 也可以作为备忘录APP app启动截图： <img src="https://img-blog.csdnimg.cn/88d6828ffc5f44cfba2383cd2f5b8c32.png" alt="在这里插入图片描述"> APP打开首页 <img src="https://img-blog.csdnimg.cn/63be5d6911f942a8aa79c62d580761e3.png" alt="在这里插入图片描述">

可以修改日期 <img src="https://img-blog.csdnimg.cn/fc199ea061f544a69fb560178008a358.png" alt="在这里插入图片描述"> 部分代码

```
public void initView() {<!-- -->
        ImmersionBar.with(this)
                .statusBarDarkFont(true)  //状态栏字体是深色，不写默认为亮色
                .init();
        selectedDate = Calendar.getInstance();//系统当前时间

        id = getIntent().getLongExtra("id", 0);
        time = getIntent().getStringExtra("time");
        isDayima = getIntent().getBooleanExtra("isDayima", false);
        if (time != null) {<!-- -->
            tvTitle.setText("修改");
            tvTime.setText(time);
        } else {<!-- -->
            tvTitle.setText("新增");
            tvTime.setText(TimeUtils.dateToString(TimeUtils.getTimeStame(), "yyyy-MM-dd"));
        }

        if (isDayima) {<!-- -->
            sb.setChecked(true);
        } else {<!-- -->
            sb.setChecked(false);
        }
    }

```


