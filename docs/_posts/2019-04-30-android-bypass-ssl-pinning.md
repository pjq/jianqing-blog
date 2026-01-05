---
title: "Android bypass SSL Pinning"
date: 2019-04-30
author: pengjianqing
categories: ['Android', 'Tech']
tags: ['Android', 'Frida', 'ssl', 'SSL Pinning']
---

很多Android App现在出于安全考虑都会加上SSL Pinning，有时在Charles Debug过程中会不是太方便，当然可以加一个设置一键关掉这个功能。

最近刚好看了一些关于Frida的资料，发现这个东西用来做代码注入很方便，而且平台通吃，Android/iOS/Linux/Mac。

找到下面这个JavaScript脚本，可以在不侵入原Apk的情况下，去掉SSL Pinning, 通过Charles启用SSL Proxy，在手机设置好Charle代理，直接明文抓到所有请求。

```
`Java.perform(function() {
    var array_list = Java.use("java.util.ArrayList");
    var ApiClient = Java.use('com.android.org.conscrypt.TrustManagerImpl');
    ApiClient.checkTrustedRecursive.implementation = function(a1, a2, a3, a4, a5, a6) {
        // console.log('Bypassing SSL Pinning');
        var k = array_list.$new();
        return k;
    }
}, 0);`
```

启动命令

```
`frida -U -l android_bypass_ssl.js --no-pause -f com.xxxx.android`
```

然后就可以在Charles看到这个App所有的明文请求。

当然在启动之前先在确保你电脑上已经安装好了Frida, 并且Emulator上已经跑了frida-server

```
`adb root && adb push frida-server-12.4.8-android-x86_64 /data/local/frida-server &&  adb shell chmod +x /data/local/frida-server  && adb shell /data/local/frida-server`
```

具体安装可以参考我写的另外一篇Wiki: [https://wiki.pjq.me/doku.php?id=android:fridump](https://wiki.pjq.me/doku.php?id=android:fridump)

参考链接: [https://techblog.mediaservice.net/2018/11/universal-android-ssl-pinning-bypass-2/](https://techblog.mediaservice.net/2018/11/universal-android-ssl-pinning-bypass-2/)