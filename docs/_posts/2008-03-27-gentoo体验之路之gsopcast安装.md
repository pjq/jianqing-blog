---
title: "Gentoo体验之路之gsopcast安装"
date: 2008-03-27
author: pengjianqing
categories: ['gentoo', 'Software']
---

先下载源码：新出的0.4.0版

http://lianwei3.googlepages.com/home2

参考里面的INSTALL

./configuration

make&&make install

在/usr/local/ bin中

ls /usr/local/bin/
drcomc    drcomd    gsopcast  .keep     sp-sc

下载[sp-sc](http://percy.blog.ubuntu.org.cn/2008/03/27/gentoo%e4%bd%93%e9%aa%8c%e4%b9%8b%e8%b7%af%e4%b9%8bgsopcast%e5%ae%89%e8%a3%85/sp-sc/)解压cp到/usr/local/bin就可以了

频道地址填

http://202.71.98.177/gchlxml

以前将列表下到本地，用自己的FTP也可以，不知道为什么，这个新版本不行！~~！

root不能直接启动，要将gsopcast ln到/sbin中

ln -s /usr/local/bin/gsopcast /sbin