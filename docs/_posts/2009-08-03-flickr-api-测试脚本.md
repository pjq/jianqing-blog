---
title: "Flickr API 测试脚本"
date: 2009-08-03
author: pengjianqing
categories: ['Android', 'BASH', 'flickr', 'shell', '自由分类']
---

最近在研究flickr以及它的API，为了测试它的API，写了一个脚本，这样就可以很方便地测试它提供的API了。
参考这个地方：http://www.flickr.com/services/api/auth.spec.html

PS.你先要修改脚本中的：
API_KEY=****************************（这里是api_key）
API_SECRET=************************（这里是对应的公钥）
改成你自己的KEY，而且要先编译底下的那个md5.java文件，以确认它能够正常对字符串进行加密。

```

pjq@gentoo-pjq ~/flickr $ cat flickr.sh
#########################################################################
# Author: pengjianqing@gmail.com
# Created Time: Mon 03 Aug 2009 07:48:46 PM CST
# File Name: flickr.sh
# Description:
#########################################################################
#!/bin/bash

API_KEY=****************************
API_SECRET=************************
#echo "API_KEY=${API_KEY}"
#echo "API_SECRET=${API_SECRET}"

echo "*********************************************************"
echo "Get frob..."
echo "*********************************************************"
URL=http://flickr.com/services/rest/?
METHORD=flickr.auth.getFrob
SIG=${API_SECRET}api_key${API_KEY}method${METHORD}
echo SIG=${SIG}
API_SIG=`java md5 ${SIG}`
echo API_SIG=${API_SIG}
FLICKR_URL="${URL}method=${METHORD}&api_key=${API_KEY}&api_sig=${API_SIG}"
echo FLICKR_URL=${FLICKR_URL}
wget  ${FLICKR_URL} -O frob.xml

FROB=`cat frob.xml |grep frob|cut -d "" -f2`
echo FROB=${FROB}

echo "*********************************************************"
echo "Load firefox to Confirm the authentication."
echo "*********************************************************"
SIG=${API_SECRET}api_key${API_KEY}frob${FROB}permswrite
echo SIG=${SIG}
API_SIG=`java md5 ${SIG}`
echo API_SIG=${API_SIG}

FLICKR_URL="http://flickr.com/services/auth/?api_key=${API_KEY}&perms=write&frob=${FROB}&api_sig=${API_SIG}"
echo "Loading ${FLICKR_URL}"
firefox ${FLICKR_URL}
read -p "Check OK[yes/no]:" CHOOSE
echo Your input:${CHOOSE}

echo "*********************************************************"
echo "Get auth token..."
echo "*********************************************************"
METHORD=flickr.auth.getToken
SIG=${API_SECRET}api_key${API_KEY}frob${FROB}method${METHORD}
echo SIG=${SIG}
API_SIG=`java md5 ${SIG}`
echo API_SIG=${API_SIG}

FLICKR_URL="http://flickr.com/services/rest/?method=flickr.auth.getToken&api_key=${API_KEY}&frob=${FROB}&api_sig=${API_SIG}"

wget  ${FLICKR_URL} -O token.xml
#cat token.xml
TOKEN=`cat token.xml|grep -i token|cut -d ">" -f2|cut -d "

	
	

```

上面两个链接就是我自己的设置。
至此，简单的验证了Flickr的API。

![](http://img.zemanta.com/pixy.gif?x-id=6d6b92a8-2f78-84ea-be1a-8fa9b63dbaeb)