---
title: "Android:自动生成keystore和自动签名及自动重装APK的脚本"
date: 2009-06-07
author: pengjianqing
categories: ['Android']
tags: ['Android', 'keystore', 'SHELL']
---

每次要生成keystore都要输入一堆命令，而且难记，顺便就写了几个小脚本：
可以在这里下载
http://github.com/pjq/AndroidShell/tree/master

用来生成keystore的，并且自动对当前工程APK文件进行签名，需要在工程根目录下执行
比如要产生 myapp.keystore
只要执行：./genkey myapp
```

cat /usr/local/bin/genkey
#!/bin/sh
#Author:pengjianqing@sina.com
#Date:20090607
#description:used to gen the keystore
#Filename:genkey.sh
#USAGE:
#Example:
#./genkey.sh appname
#
#

echo "========================================"
APKFILE=`ls bin/ -l|grep apk|cut -d " " -f8`
echo "APKFILE=${APKFILE}"
echo "========================================"

echo "Generage the keystore:"
echo "keytool -genkey -v -keystore ${1}.keystore -alias ${1} -keyalg RSA -validity 10000"
keytool -genkey -v -keystore ${1}.keystore -alias ${1} -keyalg RSA -validity 10000

echo "show the MD5 of the keystore:"
echo "keytool -list  -keystore ${1}.keystore"
keytool -list  -keystore ${1}.keystore

echo "Sign the apk:"
echo "jarsigner -verbose -keystore ${1}.keystore bin/${APKFILE} ${1}"
jarsigner -verbose -keystore ${1}.keystore bin/${APKFILE} ${1}

#echo"Uninstall the apk"
#adb uninstall com.pjq.googlemapsample

#echo "Install the apk"
#adb install bin/GooglemapSample.apk

```

自动签名，并自动重新安装APK文件,需要在工程根目录下执行
./sa.sh
：

```

 cat sa.sh
#########################################################################
# Author: pengjianqing@sina.com
# Created Time: Sat 06 Jun 2009 11:31:57 PM CST
# File Name: SignAndroid.sh:sa.sh
# Description:Used to auto sign the apk file,then reinstall it.
#Example:
#./sa.sh
#########################################################################
#!/bin/bash
echo "========================================"
KEYSTORE=`ls -l|grep keystore|cut -d " " -f8`
echo "KEYSTORE=${KEYSTORE}"
PRENAME=`echo ${KEYSTORE}|cut -d "." -f1`
echo "PRENAME=${PRENAME}"
PACKAGE=`grep package AndroidManifest.xml|cut -d "\"" -f2`
echo "PACKAGE=${PACKAGE}"
APKFILE=`ls bin/ -l|grep apk|cut -d " " -f8`
echo "APKFILE=${APKFILE}"
echo "========================================"

echo "****************************************"
echo "Sign the apk:"
echo "jarsigner -verbose -keystore ${KEYSTORE} bin/${APKFILE} ${PRENAME}"
jarsigner -verbose -keystore ${KEYSTORE} bin/${APKFILE}  ${PRENAME}
echo "****************************************"

echo "Uninstall the apk:"
echo "adb uninstall ${PACKAGE} "
adb uninstall ${PACKAGE}
echo "****************************************"

echo "Install apk:"
echo "adb install bin/${APKFILE}"
adb install bin/${APKFILE}
echo "****************************************"
echo "Finished!!"
echo "****************************************"

```