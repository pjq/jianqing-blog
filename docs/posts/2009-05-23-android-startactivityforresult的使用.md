---
title: "Android startActivityForResult的使用"
date: 2009-05-23
author: pengjianqing
categories: ['Android']
tags: ['Android', 'Intent']
---

当我们调用其它activity的时候，如果需要那个调用的activity返回数据，这个时候我们就需要使用startActivityForResult了。网上也有很多关于这个的介绍。

http://www.blogjava.net/marshal-hird/archive/2008/07/25/217389.html

这是一篇翻译的文章。不知道是不是敲错了，[onActivityResult(int, int, String, Bundle)](http://code.google.com/android/reference/android/app/Activity.html#onActivityResult%28int,%20int,%20java.lang.String,%20android.os.Bundle%29) 这个函数参数错了。我照着这个函数参数，一直无法跑到这个回调，我用的是最新的SDK 1.5 r1,查了好久也没发现哪个地方错了。最后，没办法，去SDK中搜了一下。在app.android.Activity下， 原来是这样的：onActivityResult(int, int, Intent)

是三个参数。难道是版本的原因。将参数改过之后就能跑到这个加调了。

下面是我用来测试的代码：

1.主入口：

```

/*
* Copyright (C) 2007 The Android Open Source Project
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package com.example.android.helloactivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.*;
//import android.view.*;

/**
* A minimal "Hello, World!" application.
*/
public class HelloActivity extends Activity implements OnClickListener{

private Button getData;
private TextView textView;
private int RQ_RESULT;
public HelloActivity() {
}

/**
* Called with the activity is first created.
*/
@Override
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);

// Set the layout for this activity.  You can find it
// in res/layout/hello_activity.xml
setContentView(R.layout.a);

getData = (Button)findViewById(R.id.aButton);
textView = (TextView)findViewById(R.id.aTextView);

getData.setOnClickListener(this);

}

@Override
public void onClick(View v)
{
Intent intent = new Intent();
intent.setClass(HelloActivity.this, B.class);
startActivityForResult(intent, RQ_RESULT);
}

protected void  onActivityResult(int requestCode, int resultCode, Intent intent)
{

Log.i(this.getLocalClassName(), "onActivityResult");

if (RQ_RESULT == requestCode && RESULT_OK == resultCode)
{
String text = intent.getCharSequenceExtra("data").toString();
textView.setText(text);
}
}
}

```

2.类B，是被调用的activity,并从中返回数据。
```

package com.example.android.helloactivity;

import android.app.*;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.*;

public class B extends Activity implements OnClickListener{
private Button button;
private EditText editText;

@Override
public void onCreate(Bundle savedInstanceState)
{
super.onCreate(savedInstanceState);

setContentView(R.layout.b);

button = (Button)findViewById(R.id.bButton);
editText = (EditText)findViewById(R.id.bEditText);
button.setOnClickListener(this);

}

@Override
public void onClick(View v)
{
String text = editText.getText().toString();
Bundle bundle = new Bundle();
//bundle.putString(key, value);
bundle.putString("data", text);

Intent intent = new Intent();
intent.putExtras(bundle);
setResult(RESULT_OK,intent);
finish();

}

}

```