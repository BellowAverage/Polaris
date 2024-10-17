
--- 
title:  安卓listview使用的一种方法 
tags: []
categories: [] 

---
先上个效果图  <img src="https://img-blog.csdn.net/20161019123621150" alt="这里写图片描述" title="">  温度报警设置是用listview容器装载。包含两个textview和两个button。

首先，声明两个必要组建，ListView和ArrayList是两个必要的容器

```
private ListView listView;
private ArrayList&lt;String&gt; data = new ArrayList&lt;&gt;();
```

listview的初始化处理

```
listView = (ListView)findViewById(R.id.alert_setting_list);
generateListContent();
listView.setAdapter(new MyListAdapter(this,R.layout.alert_setting_item,data));
```

generateListContent的实现

```
private void generateListContent(){
    for (int i = 0; i &lt; 3; i++) {
        data.add("This is no " + i);
    }
}
```

MyListAdapter的实现

```
private class MyListAdapter extends ArrayAdapter&lt;String&gt; {

        private int layout;
        public MyListAdapter(Context context, int resource, List&lt;String&gt; objects) {
            super(context, resource, objects);
            layout = resource;
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            ViewHolder mainViewHolder = null;
            if (convertView == null){
                LayoutInflater layoutInflater = LayoutInflater.from(getContext());
                convertView = layoutInflater.inflate(layout, parent, false);
                final ViewHolder viewHolder = new ViewHolder();
                viewHolder.textTitle = (TextView)convertView.findViewById(R.id.setting_title);
                viewHolder.addButton = (Button)convertView.findViewById(R.id.add_button);
                viewHolder.textContent = (TextView)convertView.findViewById(R.id.setting_content);
                viewHolder.minusButton = (Button)convertView.findViewById(R.id.minus_button);
                switch (position){
                    case 0:
                        viewHolder.textTitle.setText("高温报警线");
                        viewHolder.textContent.setText("38.0");
                        viewHolder.addButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });

                        viewHolder.minusButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });
                        break;
                    case 1:
                        viewHolder.textTitle.setText("低温报警线");
                        viewHolder.textContent.setText("36.0");
                        viewHolder.addButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });

                        viewHolder.minusButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });
                        break;
                    case 2:
                        viewHolder.textTitle.setText("间隔时间");
                        viewHolder.textContent.setText(String.valueOf(10));
                        viewHolder.addButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });

                        viewHolder.minusButton.setOnClickListener(new View.OnClickListener() {
                            @Override
                            public void onClick(View v) {
                                //在这里添加对按钮点击的响应事件
                            }
                        });
                        break;
                    default:
                        break;
                }

                convertView.setTag(viewHolder);
            }else{
                mainViewHolder = (ViewHolder)convertView.getTag();
            }
            return convertView;
        }
    }

    public class ViewHolder{
        TextView textTitle;
        Button addButton;
        TextView textContent;
        Button minusButton;
    }
```

Layout文件  activity_main.xml

```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    tools:context="com.example.will.listviewdemp.MainActivity"&gt;

    &lt;TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="温度报警设置"/&gt;

    &lt;ListView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/alert_setting_list" /&gt;
&lt;/LinearLayout&gt;

```

alert_setting_item.xml

```
&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"&gt;

    &lt;TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="New Text"
        android:id="@+id/setting_title"
        android:layout_centerVertical="true"
        android:layout_alignParentStart="true" /&gt;

        &lt;Button
            android:layout_width="50dp"
            android:layout_height="wrap_content"
            android:text="+"
            android:textSize="30dp"
            android:id="@+id/add_button"
            android:layout_gravity="center_horizontal"
            android:layout_alignParentTop="true"
            android:layout_toStartOf="@+id/setting_content" /&gt;

        &lt;TextView
            android:layout_width="30dp"
            android:layout_height="wrap_content"
            android:text="38"
            android:layout_centerVertical="true"
            android:id="@+id/setting_content"
            android:layout_below="@+id/setting_title"
            android:layout_toStartOf="@+id/minus_button" /&gt;

        &lt;Button
            android:layout_width="50dp"
            android:layout_height="wrap_content"
            android:text="-"
            android:textSize="30dp"
            android:id="@+id/minus_button"
            android:layout_gravity="right"
            android:layout_alignParentTop="true"
            android:layout_alignParentEnd="true" /&gt;

&lt;/RelativeLayout&gt;
```

这样就能基本完成一个listview的界面，当然listview的实现方法不止这一种，仅提供一种参考，欢迎讨论。代码资源：  参考链接：
