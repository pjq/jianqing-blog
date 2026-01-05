---
title: "Android ImageView用法"
date: 2009-05-26
author: pengjianqing
categories: ['Android']
tags: ['Android', 'ImageView', 'XML']
---

详见：http://gentoo-pjq.vicp.net/bbs/viewtopic.php?f=8&t=85&p=100&sid=f1b441b45cf00aaa9b3c88e74fc45902#p100

代码可以到这里下载：http://github.com/pjq/weatherUI/tree/master
用git clone:
**代码:**
git clone git@github.com:pjq/weatherUI.git
要做一个weather report 的UI。
用Droiddraw画了一个UI。
写了一些测试代码，当点到一张图片的时候，并将这张图片显示出来。
这里要注意这一段：
**代码:**
public boolean onTouch(View v, MotionEvent event) {
ImageView imageview = (ImageView)findViewById(v.getId());
imageview.setBackgroundDrawable(v.getBackground());
按理说不应该再重新设置背景了，但很奇怪的是，当第一次点到一张图片时，会将这张点到的图片放到，所以在那么小的ImageView里就会显示不全，而只显示放大后的图片的一部分。
------后来又试了一下，好像又没问题，奇怪！！！
```
pjq@localhost ~/eclipse/workspace/weatherUI/src/com/qisda/weather $ cat weatherUI.java
package com.qisda.weather;

import android.app.Activity;
import android.os.Bundle;
import android.view.*;
import android.view.View.OnFocusChangeListener;
import android.view.View.OnTouchListener;
import android.widget.ImageView;

public class weatherUI extends Activity implements OnTouchListener {
/** Called when the activity is first created. */

private ImageView w1;
private ImageView w2;
private ImageView w3;
private ImageView w4;

private ImageView wcurrent;

@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.main);

w1 = (ImageView) findViewById(R.id.w1);
w2 = (ImageView) findViewById(R.id.w2);
w3 = (ImageView) findViewById(R.id.w3);
w4 = (ImageView) findViewById(R.id.w4);
wcurrent = (ImageView) findViewById(R.id.wcurrent);

w1.setBackgroundResource(R.drawable.weather_clear);
w2.setBackgroundResource(R.drawable.weather_clear_night);
w3.setBackgroundResource(R.drawable.weather_cloudy);
w4.setBackgroundResource(R.drawable.weather_showers);
wcurrent.setBackgroundResource(R.drawable.weather_storm);

/*
* wcurrent.setOnFocusChangeListener(new View.OnFocusChangeListener() {
* public void onFocusChange(View v, boolean hasFocus) { if (true ==
* hasFocus) { wcurrent.setBackgroundDrawable(v.getBackground());
*
* } else {
*
* } } }); / wcurrent.setOnTouchListener(new View.OnTouchListener() {
* public boolean onTouch(View v, MotionEvent event) {
*
* return true; }
*
* });
*/

w1.setOnTouchListener(this);
w2.setOnTouchListener(this);
w3.setOnTouchListener(this);
w4.setOnTouchListener(this);
wcurrent.setOnTouchListener(this);

}

@Override
public boolean onTouch(View v, MotionEvent event) {
ImageView imageview = (ImageView)findViewById(v.getId());
imageview.setBackgroundDrawable(v.getBackground());

switch (v.getId()) {
case R.id.w1:
wcurrent.setBackgroundDrawable(v.getBackground());
break;
case R.id.w2:
wcurrent.setBackgroundDrawable(v.getBackground());
break;

case R.id.w3:
wcurrent.setBackgroundDrawable(v.getBackground());
break;

case R.id.w4:
wcurrent.setBackgroundDrawable(v.getBackground());
break;

case R.id.wcurrent:
wcurrent.setBackgroundDrawable(v.getBackground());
break;

default:
break;

}
return true;
}
}pjq@localhost ~/eclipse/workspace/weatherUI/src/com/qisda/weather $
```

Layout:
```

```

运行效果：

[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/Shv_8GRUJTI/AAAAAAAAACo/DOlK0GueLk0/s400/2009-05-26-215141_374x728_scrot.jpg)](http://picasaweb.google.com/lh/photo/T6u0oW8eG-q3NaGSaQhfVQ?feat=embedwebsite)

发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/ShwALqBlKAI/AAAAAAAAACw/VHV9ffkmBmE/s400/2009-05-26-215153_386x756_scrot.jpg)](http://picasaweb.google.com/lh/photo/HS0DfV4HWueUrT9b2Z99gw?feat=embedwebsite)

发件人 [snapshoot](http://picasaweb.google.com/pengjianqing/Snapshoot?feat=embedwebsite)

![weather](http://picasaweb.google.com/lh/photo/HS0DfV4HWueUrT9b2Z99gw?feat=directlink)