---
title: "Android: 给APK文件签名方法（示例）"
date: 2009-06-02
author: pengjianqing
categories: ['Android']
---

Description:
Android 给APK文件签名.
默认生成的APK文件是debug签名的,如果要发布到Android Market那么需要另外用
keytool和jarsigner来给你的APK签名(主要是设定时间和所有者).

按照常见步骤
第一步:
keytool -genkey -v -keystore your-release-key.keystore -alias your-alias-name -keyalg RSA -validity 20000

第二步:
jarsigner -verbose -keystore your-release-key.keystore  your-release.apk your-alias-name

我的详细操作过程：
```

pjq@gentoo-pjq ~/eclipse/workspace/QWeather $ keytool -genkey -v -keystore QWeather.keystore -alias QWeather -keyalg RSA -validity 10000
输入keystore密码：
再次输入新密码:
您的名字与姓氏是什么？
[Unknown]：  pjq
您的组织单位名称是什么？
[Unknown]：  pjq
您的组织名称是什么？
[Unknown]：  pjq
您所在的城市或区域名称是什么？
[Unknown]：  suzhou
您所在的州或省份名称是什么？
[Unknown]：  jiangsu
该单位的两字母国家代码是什么
[Unknown]：  CN
CN=pjq, OU=pjq, O=pjq, L=suzhou, ST=jiangsu, C=CN 正确吗？
[否]：  Y

正在为以下对象生成 1,024 位 RSA 密钥对和自签名证书 (SHA1withRSA)（有效期为 10,000 天）:
CN=pjq, OU=pjq, O=pjq, L=suzhou, ST=jiangsu, C=CN
输入的主密码
（如果和 keystore 密码相同，按回车）：
[正在存储 QWeather.keystore]
pjq@gentoo-pjq ~/eclipse/workspace/QWeather $ jarsigner -verbose -keystore QWeather.keystore QWeather.apk QWeather
输入密钥库的口令短语：
正在添加： META-INF/QWEATHER.SF
正在添加： META-INF/QWEATHER.RSA
正在签名： res/anim/fade.xml
正在签名： res/anim/hyperspace_in.xml
正在签名： res/anim/hyperspace_out.xml
正在签名： res/anim/push_left_in.xml
正在签名： res/anim/push_left_out.xml
正在签名： res/anim/push_up_in.xml
正在签名： res/anim/push_up_out.xml
正在签名： res/anim/wave_scale.xml
正在签名： res/drawable/about.png
正在签名： res/drawable/background.jpg
正在签名： res/drawable/cloudy.jpg
正在签名： res/drawable/dersert.jpg
正在签名： res/drawable/find.png
正在签名： res/drawable/green.jpg
正在签名： res/drawable/icon.png
正在签名： res/drawable/qweathericon.jpg
正在签名： res/drawable/search.png
正在签名： res/drawable/settings.png
正在签名： res/drawable/shape_1.xml
正在签名： res/drawable/shape_2.xml
正在签名： res/drawable/shape_3.xml
正在签名： res/drawable/shape_4.xml
正在签名： res/drawable/shape_5.xml
正在签名： res/drawable/sun.jpg
正在签名： res/drawable/switchicon.png
正在签名： res/drawable/switchicon2.png
正在签名： res/drawable/weather_clear.png
正在签名： res/drawable/weather_clear_night.png
正在签名： res/drawable/weather_cloudy.png
正在签名： res/drawable/weather_few_clouds.png
正在签名： res/drawable/weather_few_clouds_night.png
正在签名： res/drawable/weather_night_clear.png
正在签名： res/drawable/weather_night_few_clouds.png
正在签名： res/drawable/weather_overcast.png
正在签名： res/drawable/weather_severe_alert.png
正在签名： res/drawable/weather_showers.png
正在签名： res/drawable/weather_showers_scattered.png
正在签名： res/drawable/weather_snow.png
正在签名： res/drawable/weather_storm.png
正在签名： res/drawable/weather_sunny.png
正在签名： res/layout/main.xml
正在签名： res/layout/searchdialog.xml
正在签名： res/layout/searchdialog2.xml
正在签名： AndroidManifest.xml
正在签名： resources.arsc
正在签名： classes.dex
正在签名： com/qisda/qweather/.SearchDialog.java.swp

```

可以看到在目录下会产生一个QWeather.keystore文件，QWeather.apk这个文件也在当前目录下。

刚开始遇到一个错误：
jarsigner： 无法对 jar 进行签名： java.util.zip.ZipException: invalid entry compressed size (expected 639 but got 642 bytes)
这是因为默认给apk做了debug 签名，所以无法做新的签名
这时就必须点工程右键->Android Tools ->Export Unsigned Application Package.
或者从AndroidManifest.xml的 Exporting上也是一样的
然后再基于这个导出的unsigned apk做签名，导出的时候最好将其目录选在你之前产生keystore的那个目录下，这样操作起来就方便了。