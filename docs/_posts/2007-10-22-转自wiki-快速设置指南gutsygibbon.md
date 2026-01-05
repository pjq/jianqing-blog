---
title: "转自wiki 快速设置指南/GutsyGibbon"
date: 2007-10-22
author: pengjianqing
categories: ['Ubuntu', '自由分类']
---

快速设置指南/GutsyGibbon
出自Ubuntu中文
[http://wiki.ubuntu.org.cn/%E5%BF%AB%E9%80%9F%E8%AE%BE%E7%BD%AE%E6%8C%87%E5%8D%97/GutsyGibbon](http://wiki.ubuntu.org.cn/%E5%BF%AB%E9%80%9F%E8%AE%BE%E7%BD%AE%E6%8C%87%E5%8D%97/GutsyGibbon)

当你刚刚安装完毕之後，我们来花10分钟设置一下系统，让其有一个更加舒适的中文环境。──本文的作用

目录
[隐藏]

* 1 前言
* 2 修改源并更新你的(k/x/ed)ubuntu
* 3 设置系统中文环境支持
o 3.1 安装语言包
o 3.2 scim输入法安装及设置
o 3.3 fcitx输入法安装及设置（Kubuntu下推荐使用）
o 3.4 安装文泉驿字体（可选）
o 3.5 解决PDF电子文档的中文乱码
* 4 安装JAVA环境支持
* 5 安装QQ软件（可选）
o 5.1 安装EVA，Kubuntu推荐使用
o 5.2 安装LumaQQ，需JAVA支持
* 6 多媒体应用环境设置'
o 6.1 安装多媒体解码器
o 6.2 安装mplayer播放器
o 6.3 Xine前端播放器设置（可选）
* 7 安装英汉辞典
* 8 安装设置Firefox浏览器
o 8.1 安装flash播放插件
o 8.2 安装插件/扩展
o 8.3 配置firefox
* 9 安装支持BT/电驴/Gnutella1/Gnutella2等下载软件
o 9.1 安装BT下载软件
o 9.2 安装电驴下载软件（可选）
* 10 其他参考

[编辑] 前言

* 本文直接来自于feisty快速设置指南，不适用gusty的部分请有能力的尽快修改。
* 本文适用于采用i386安装光盘安装的系统，部分内容适合AMD64和PPC安装(如有问题请到论坛咨询)。
* 如果您看到"$"的符号，意思是你必须在终端状态下运行此命令（应用程序 -> 附件 -> 终端）。
* "sudo"的意思是“以超级用户执行[Superuser Do]”。"sudo"需要提供当前登录用户的密码"Password:"。请输入您指定的用户密码(你输入的密码不会被显示，你输入完毕直接按回车确定即可)。
* 注意：apt，aptitude，dpkg，Adept，新立得 等软件管理工具在同一时间只能有一个运行。
* 文中所提到的下载地址http://ftp.ubuntu.org.cn/ 帐号: ubuntu，密码: ubuntuftp。

[编辑] 修改源并更新你的(k/x/ed)ubuntu

* 不同的网络状况连接以下源的速度不同。建议在添加前手动验证以下源的连接速度（ping下就行）。比如说北京网通用户连接cn99就非常慢，而ftp.sjtu.edu.cn是相对较快的源。选择最快的源可大大节省下载时间，请根据自己网络环境设置更新服务器，以达到最快的速度。
* 注意，你可以同时加入几个源。尽量选择一组官方的源（也就是下面的Archive.ubuntu.com的条目）直接加在文件的最后，以避免非官方源软件包不全时出现 404 Not Found 文件未发现的错误。建议电信用户使用cn99和台湾大学的源，网通用户使用台湾大学的源，教育网用户使用教育网的源。

打开终端方法：

按下ALT+F2 -> gnome-terminal -> 运行          #(ed)ubuntu
按下ALT+F2 -> konsole -> 运行                 #Kubuntu
按下ALT+F2 -> xfce4-terminal -> 运行          #xubuntu

在终端执行命令

备份当前的源列表，以便日后需要时恢复：

sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup

编辑源列表

gksu gedit /etc/apt/sources.list             #(ed)ubuntu
kdesu kate /etc/apt/sources.list             #kubuntu
gksu mousepad /etc/apt/sources.list          #xubuntu
sudo vim /etc/apt/sources.list               #通用

从以下各服务器列表内容中选择一段替换文件中的所有内容，为防止非官方源中软件包不全的问题，请在sources.list文件中尾部添加一组官方源。

Archive.ubuntu.com更新服务器（欧洲，此为官方源，电信网通用户使用)：

deb [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy main restricted universe multiverse
deb [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-proposed main restricted universe multiverse
deb [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-proposed main restricted universe multiverse
deb-src [http://archive.ubuntu.com/ubuntu/](http://archive.ubuntu.com/ubuntu/) gutsy-backports main restricted universe multiverse

Ubuntu.cn99.com更新服务器（江苏省常州市电信，推荐电信用户使用）：

deb [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy main restricted universe multiverse
deb [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-proposed main restricted universe multiverse
deb [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-proposed main restricted universe multiverse
deb-src [http://ubuntu.cn99.com/ubuntu/](http://ubuntu.cn99.com/ubuntu/) gutsy-backports main restricted universe multiverse
deb [http://ubuntu.cn99.com/ubuntu-cn/](http://ubuntu.cn99.com/ubuntu-cn/) gutsy main restricted universe multiverse

Mirrors.shlug.org更新服务器（电信服务器，Ubuntu China Official Mirror, maintained by Shanghai Linux User Group）：

deb [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy main restricted universe multiverse
deb [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-security main restricted universe multiverse
deb [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-updates main restricted universe multiverse
deb [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-backports main restricted universe multiverse
deb [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-proposed main restricted universe multiverse
deb-src [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy main restricted universe multiverse
deb-src [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-security main restricted universe multiverse
deb-src [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-updates main restricted universe multiverse
deb-src [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-backports main restricted universe multiverse
deb-src [http://cn.archive.ubuntu.com/ubuntu](http://cn.archive.ubuntu.com/ubuntu) gutsy-proposed main restricted universe multiverse

Mirror.lupaworld.com更新服务器（浙江省杭州市双线服务器）：

deb [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy main restricted universe multiverse
deb [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-security main restricted universe multiverse
deb [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-updates main restricted universe multiverse
deb [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-backports main restricted universe multiverse
deb [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-proposed main restricted universe multiverse
deb-src [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy main restricted universe multiverse
deb-src [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-security main restricted universe multiverse
deb-src [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-updates main restricted universe multiverse
deb-src [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-backports main restricted universe multiverse
deb-src [http://mirror.lupaworld.com/ubuntu](http://mirror.lupaworld.com/ubuntu) gutsy-proposed main restricted universe multiverse

厦门大学更新服务器（教育网服务器）：

deb [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy main restricted universe multiverse
deb [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-backports restricted universe multiverse
deb [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-proposed main restricted universe multiverse
deb [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-security main restricted universe multiverse
deb [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy main restricted universe multiverse
deb-src [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-proposed main restricted universe multiverse
deb-src [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [ftp://ubuntu.realss.cn/ubuntu/](ftp://ubuntu.realss.cn/ubuntu/) gutsy-updates main restricted universe multiverse

成都市 电子科技大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb-src [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [http://ubuntu.uestc.edu.cn/ubuntu/](http://ubuntu.uestc.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe

== 如果无法解析uestc.edu.cn域名，请使用以下地址 ==

deb [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy main multiverse restricted universe
deb [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-backports main multiverse restricted universe
deb [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-security main multiverse restricted universe
deb [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy main multiverse restricted universe
deb-src [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [http://ubuntu.dormforce.net/ubuntu/](http://ubuntu.dormforce.net/ubuntu/) gutsy-updates main multiverse restricted universe

上海市上海交通大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb-src [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [http://ftp.sjtu.edu.cn/ubuntu/](http://ftp.sjtu.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe

中国科学技术大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy main multiverse restricted universe
deb-src [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [http://debian.ustc.edu.cn/ubuntu/](http://debian.ustc.edu.cn/ubuntu/) gutsy-updates main multiverse restricted universe

北京市清华大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy main multiverse restricted universe
deb [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-backports main multiverse restricted universe
deb [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-security main multiverse restricted universe
deb [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy main multiverse restricted universe
deb-src [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [http://mirror9.net9.org/ubuntu/](http://mirror9.net9.org/ubuntu/) gutsy-updates main multiverse restricted universe

沈阳市东北大学更新服务器（教育网，推荐校园网和网通用户使用）：

deb [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy  main multiverse restricted universe
deb [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-backports main multiverse restricted universe
deb [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-proposed main multiverse restricted universe
deb [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-security main multiverse restricted universe
deb [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-updates main multiverse restricted universe
deb-src [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy main multiverse restricted universe
deb-src [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-backports main multiverse restricted universe
deb-src [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-security main multiverse restricted universe
deb-src [ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/](ftp://ftp.neu.edu.cn/mirror/archive.ubuntu.com/ubuntu/) gutsy-updates main multiverse restricted universe

中国台湾省台湾大学更新服务器（推荐网通用户使用，电信PING平均响应速度41MS。强烈推荐此源，比较完整，较少出现同步问题）：

deb [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy main restricted universe multiverse
deb [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-backports main restricted universe multiverse
deb [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://ubuntu.csie.ntu.edu.tw/ubuntu/](http://ubuntu.csie.ntu.edu.tw/ubuntu/) gutsy-proposed main restricted universe multiverse

Mirror.vmmatrix.net更新服务器（上海市电信，推荐电信网通用户使用）：

deb [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy main restricted universe multiverse
deb [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-backports main restricted universe multiverse
deb [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://mirror.vmmatrix.net/ubuntu/](http://mirror.vmmatrix.net/ubuntu/) gutsy-proposed main restricted universe multiverse

ubuntu.cnsite.org更新服务器（福建省福州市 电信）：

deb [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy main restricted universe multiverse
deb [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-backports main restricted universe multiverse
deb [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://ubuntu.cnsite.org/ubuntu/](http://ubuntu.cnsite.org/ubuntu/) gutsy-proposed main restricted universe multiverse

mirror.rootguide.org更新服务器（上海市 电信）：

deb [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy main restricted universe multiverse
deb-src [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy main restricted universe multiverse
deb [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-updates main restricted universe multiverse
deb-src [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-updates main restricted universe multiverse
deb [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-backports main restricted universe multiverse
deb-src [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-backports main restricted universe multiverse
deb [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-security main restricted universe multiverse
deb-src [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-security main restricted universe multiverse
deb [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-proposed main multiverse restricted universe
deb-src [http://mirror.rootguide.org/ubuntu/](http://mirror.rootguide.org/ubuntu/) gutsy-proposed main restricted universe multiverse
deb [http://mirror.rootguide.org/ubuntu-cn/](http://mirror.rootguide.org/ubuntu-cn/) gutsy main restricted universe multiverse

台湾的官方源速度也相当不错，有时甚至快于内地的：

deb [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy main restricted universe multiverse
deb [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-security main restricted universe multiverse
deb [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-updates main restricted universe multiverse
deb [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-backports main restricted universe multiverse
deb [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-proposed main restricted universe multiverse
deb-src [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy main restricted universe multiverse
deb-src [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-security main restricted universe multiverse
deb-src [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-updates main restricted universe multiverse
deb-src [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-backports main restricted universe multiverse
deb-src [http://tw.archive.ubuntu.com/ubuntu](http://tw.archive.ubuntu.com/ubuntu) gutsy-proposed main restricted universe multiverse

也可以到以下网址自定义产生若干源：

[http://www.ubuntulinux.nl/source-o-matic](http://www.ubuntulinux.nl/source-o-matic)

以下网址有极其全面的源，以供补充：

[http://italy.copybase.ch/blog/lista-repository-sourceslist-ottimizzata-per-ubuntu-kubuntu-linux/](http://italy.copybase.ch/blog/lista-repository-sourceslist-ottimizzata-per-ubuntu-kubuntu-linux/)

官方采集的源列表：

[https://launchpad.net/ubuntu/+archivemirrors](https://launchpad.net/ubuntu/+archivemirrors)

保存编辑好的文件，执行以下命令更新

sudo apt-get update    #这一步是更新你的源列表，换源后必须执行
sudo apt-get dist-upgrade   #这一步是更新软件，如果你对新版本软件的需求不是那么迫切，可以不执行

[编辑] 设置系统中文环境支持
[编辑] 安装语言包

Kubuntu

主菜单 -> 系统设置 -> 区域与语言 -> 安装新语言 -> Chinese -> 安装
主菜单 -> 系统设置 -> 区域与语言 -> 选择系统语言 -> 简体中文 -> 确定。

相对的命令是:
sudo apt-get install language-pack-kde-zh-base language-pack-kde-zh

Ubuntu:

系统 -> 系统管理 -> 语言支持，在列表中的Chinese条目打勾。
同时将默认语言修改为Chinese（中国）并确定。

如果你设置的是非中文环境，但需要系统提供中文支持，那么请按照以下情况执行命令：

sudo apt-get install kde-i18n-zhcn kde-i18n-zhtw     #kubuntu
sudo apt-get install language-pack-zh                #ubuntu

配置字体，使中文看起来更漂亮（可选）

sudo fontconfig-voodoo -f -s zh_CN

[编辑] scim输入法安装及设置

如果您要在非CJK（中日韩）的locales下使用scim，请在终端执行如下命令（如果默认是中文环境不需要这一步，系统已经设置好了）：

sudo apt-get install scim scim-modules-socket scim-modules-table scim-pinyin scim-tables-zh scim-gtk2-immodule  im-switch libapt-pkg-perl

sudo gedit /etc/X11/xinit/xinput.d/default

加入

XIM=SCIM
XIM_PROGRAM=/usr/bin/scim
XIM_ARGS="-d"
GTK_IM_MODULE=scim
QT_IM_MODULE=scim
DEPENDS="scim,scim-gtk2-immodule | scim-qtimm"

重启Gnome以后生效。

提示：带table的包为输入法码表，安装之后才有除拼音以外的输入法，如五笔、二笔、自然码等，如果你只使用拼音输入法就不用装这些包了。

sudo im-switch -s scim -z default

如果在KDE下面使用scim，建议使用如下设置：

sudo apt-get install im-switch libapt-pkg-perl
sudo im-switch -s scim-xim -z default

Scim输入法的可选设置

注意：gutsy下不建议进行这步操作，尤其在kubuntu下强烈建议不进行这步操作。默认的scim输入法可能会与 realplay、acrobat reader、openoffice等程序有冲突。如果有这样的问题，建议使用scim-bridge替换scim。安装scim-bridge 和scim-qtimm。请确保已正确设置中文环境，打开终端，执行以下命令，或使用《新立得软件管理器》，在其中搜索"scim-bridge"、 "scim-qtimm"并标记安装。

sudo apt-get install scim-qtimm
sudo im-switch -s scim

编辑im-switch生成的scim配置文件

gksu gedit /etc/X11/xinit/xinput.d/scim

将默认的 GTK_IM_MODULE=scim 修改为 GTK_IM_MODULE="scim-bridge"。

[编辑] fcitx输入法安装及设置（Kubuntu下推荐使用）

fcitx安装：

sudo apt-get install im-switch fcitx
im-switch -s fcitx -z default # 注意，前面千万不要加sudo

完成设置最好重启一下X，输入法就生效了

fcitx设置(可选)

kate ~/.fcitx/config          #kubuntu
gedit ~/.fcitx/config         #ubuntu
mousepad ~/.fcitx/config      #xubuntu

如果英文界面下输入栏与输入文字为方块的现像，只需修改config中的字体即可，例如：

显示字体(中)=SimSun
显示字体(英)=SimSun

提示:可以设为自己喜欢的字体，但必须保证你所使用的字体支持中文。

英文locale下fcitx输入设置，解决部份非QT(如firefox/swiftfox等)程序的输入问题

kdesu kate /usr/lib/gtk-2.0/2.10.0/immodule-files.d/libgtk2.0-0.immodules       #kubuntu
gksu gedit /usr/lib/gtk-2.0/2.10.0/immodule-files.d/libgtk2.0-0.immodules       #ubuntu
gksu mousepad /usr/lib/gtk-2.0/2.10.0/immodule-files.d/libgtk2.0-0.immodules    #xubuntu
sudo vim /usr/lib/gtk-2.0/2.10.0/immodule-files.d/libgtk2.0-0.immodules         #通用

找到下面这个部份

"/usr/lib/gtk-2.0/2.10.0/immodules/im-xim.so"
"xim" "X Input Method" "gtk20" "/usr/share/locale" "ko:ja:th:zh"

将"ko:ja:th:zh" 改为 "en:ko:ja:th:zh"

设置完毕，注销一下电脑。输入法（按Ctrl+空格键激活输入法）就应该可以使用了。

更多fcitx设置，请访问中文输入法fcitx
[编辑] 安装文泉驿字体（可选）

安装：执行下面的命令前请确保你已经将上面源中ubuntu-cn的源加进去了。

sudo apt-get install xfonts-wqy

安装后应该可以在字体管理器中找到WenQuanYi Bitmap Song字体了，如果你的系统中找不到，请执行下面的命令：

sudo dpkg-reconfigure fontconfig-config

系统总共会问你三个问题，其中第三个为：

Enable bitmapped fonts by default?  # 即是否启用Bitmap字体

移动tab键至Yes，回车，字体管理器中就应该有WenQuanYi Bitmap Song字体了。
[编辑] 解决PDF电子文档的中文乱码

* KPDF/Evince:前者为Kubuntu自带，后者为ubuntu自带。

sudo apt-get install xpdf-chinese-simplified xpdf-chinese-traditional

如果上面的方法仍然不起作用，比如阅读chinapub的pdf电子书时，可以这么做

wget [http://poppler.freedesktop.org/poppler-data-0.1.tar.gz](http://poppler.freedesktop.org/poppler-data-0.1.tar.gz)
tar xzvf poppler-data-0.1.tar.gz && cd poppler-data-0.1
sudo make install datadir=/usr/share

* Adobe acrobat英文版：到下面的地址下载简体语言包（中文版的就不需要了）。

Adobe reader8.1简体中文字体包http://ftp.ubuntu.org.cn

更多版本字体请访问：http://www.adobe.com/products/acrobat/acrrasianfontpack.html
[编辑] 安装JAVA环境支持

打开终端，执行以下命令，或使用Adept/新立得软件管理器，在其中分别搜索"sun-java6-jre"和"sun-java6-jdk"并标记安装。

sudo apt-get install sun-java6-jre

如果空间富裕，建议安装一个JDK。

sudo apt-get install sun-java6-jdk

提示：安装过程中需要你回答是否同意使用协议（终端中红蓝色的提示界面），此时按tab键至OK，再按回车即可正常安装。

设置当前默认的java解释器：

sudo update-alternatives --config java

执行后会出现类似如下的画面:

There are 2 alternatives which provide `java'.

Selection    Alternative
-----------------------------------------------
1    /usr/bin/gij-wrapper-4.1
*+        2    /usr/lib/jvm/java-6-sun/jre/bin/java

Press enter to keep the default[*], or type selection number:

输入 有包含 "sun" 的行的前面的数字。如上面显示，则输入2，然后回车确定。

配置JAVA环境变量:

sudo gedit /etc/environment

在其中添加如下两行：

CLASSPATH=/usr/lib/jvm/java-6-sun/lib
JAVA_HOME=/usr/lib/jvm/java-6-sun

sudo gedit /etc/jvm

将文件中的

/usr/lib/jvm/java-6-sun

这一行填入到配置块的顶部

安装浏览器的JAVA Plugin（可选）：

sudo apt-get install sun-java6-plugin

[编辑] 安装QQ软件（可选）
[编辑] 安装EVA，Kubuntu推荐使用

sudo apt-get install eva

安装完成之后，按Alt+F2，输入eva回车即可，也可以在主菜单 -> 网络 -> eva 启动。

[编辑] 安装LumaQQ，需JAVA支持

1. 下载并安装安装QQ需要先安装上一步的JAVA环境，也可以到lumaqq官方网站下载最新版本进行安装（依次执行以下命令）

wget -c [http://lumaqq.linuxsir.org/download/2005/lumaqq_2005-linux_gtk2_x86_no_jre.tar.gz](http://lumaqq.linuxsir.org/download/2005/lumaqq_2005-linux_gtk2_x86_no_jre.tar.gz)
sudo tar zxvf lumaqq_2005-linux_gtk2_x86_no_jre.tar.gz -C /opt/
wget -c [http://lumaqq.linuxsir.org/download/patch/lumaqq_2005_patch_2006.02.02.15.00.zip](http://lumaqq.linuxsir.org/download/patch/lumaqq_2005_patch_2006.02.02.15.00.zip)
sudo unzip -o lumaqq_2005_patch_2006.02.02.15.00.zip -d /opt/LumaQQ/lib
sudo chown -R root:root /opt/LumaQQ/
sudo chmod -R 755 /opt/LumaQQ/
sudo gedit /usr/share/applications/LumaQQ.desktop

2. 在新增的文件内加入下面这几行

[Desktop Entry]
Name=LumaQQ
Comment=QQ Client
Exec=/opt/LumaQQ/lumaqq
Icon=/opt/LumaQQ/QQ.png
Terminal=false
Type=Application
Categories=Application;Network;

3. 保存编辑过的文件 安装完成后的快捷方式在（应用程序 -> Internat -> LumaQQ）。

[编辑] 多媒体应用环境设置'
[编辑] 安装多媒体解码器

安装下面这些解码器，常见的多媒体格式基本都可以播放了仅适合x86，ppc的请参见另外文件。如果出现需要输入[Y/n]或[y/N]，一律输入y并回车。

ubuntu/xubuntu：

sudo apt-get install audacious audacious-plugins audacious-plugins-extra libdvdcss2 gstreamer0.10-pitfdll gstreamer0.10-plugins-bad
gstreamer0.10-plugins-bad-multiverse gstreamer0.10-plugins-ugly-multiverse
libavcodec1d libavutil1d libcdaudio1 libdvdnav4 libfaad2-0 libfreebob0
libgsm1 libjack0 libmjpegtools0c2a libmms0 libopenspc0 libquicktime1
libsoundtouch1c2

提示：audacious是linux下一款出色的音频播放器，当然你如果有其他喜欢的就可以把它删去。

或者这里有一个可以用来一次性安装编码器、Flash、Java、MS 字体的捆绑包：

sudo apt-get install ubuntu-restricted-extras

Kubuntu ：

sudo apt-get install libdvdcss2 libdvdnav4 libdvdplay0 libdvdread3 w32codecs libxine-extracodecs gstreamer0.10-pitfdll gstreamer0.10-ffmpeg gstreamer0.10-plugins-bad gstreamer0.10-plugins-bad-multiverse gstreamer0.10-plugins-ugly  gstreamer0.10-plugins-ugly-multiverse

或者这里有一个可以用来一次性安装编码器、Flash、Java、MS 字体的捆绑包：

sudo apt-get install xubuntu-restricted-extras

[编辑] 安装mplayer播放器

sudo apt-get install mplayer-fonts mplayer mplayer-skins mozilla-mplayer

在开始用它进行视频播放前还需要进行以下设置（先启动它），然后右键弹出主菜单 -> Preferences/属性 -> Video/视频，在"Available drivers/可用驱动"中选择"x11"或"xv"，在同一窗口下半部份钩上"允许掉帧/Enable frame dropping"。

[编辑] Xine前端播放器设置（可选）

如果使用xine引擎的播放器，如kaffeine，gxine，totem-xine等在播放有些rmvb文件的时候可能会出现没有声音的现象（如果你没遇到，就不要进行这一步了），解决办法如下：

首先关闭播放器，然后使用你喜欢的文本编辑器，比如 kate，gedit，vim等打开文件 ~/.xine/catalog.cache，（比如 gedit ~/.xine/catalog.cache）打开该文件。找到其中的

/usr/lib/xine/plugins/1.1.4/xineplug_decode_real_audio.so

代码段，将其下的 decoder_priority 的数值修改成 10

修改完毕后这一段应该看起来是这样子的

/usr/lib/xine/plugins/1.1.4/xineplug_decode_real_audio.so
....
....
decoder_priority=10

[编辑] 安装英汉辞典

如果出现需要输入[Y/n]或[y/N]，一律输入y并回车。

Ubuntu

sudo apt-get install stardict stardict-cdict-gb stardict-cedict-gb stardict-hanzim stardict-langdao-ce-gb stardict-langdao-ec-gb stardict-oxford-gb stardict-xdict-ce-gb stardict-xdict-ec-gb

安装完成后的快捷方式在（应用程序 -> 附件 -> 星际译王）

Kubuntu

sudo apt-get install sox stardict-gtk stardict-common stardict-cdict-gb stardict-cedict-gb stardict-hanzim stardict-langdao-ce-gb stardict-langdao-ec-gb stardict-oxford-gb stardict-xdict-ce-gb stardict-xdict-ec-gb

安装完成后的快捷方式在（主菜单 -> 附件 -> 星际译王）

如果需要给stardict添加更多的词库或真人发音，请访问星际译王

[编辑] 安装设置Firefox浏览器
[编辑] 安装flash播放插件

* 如果你能连接国外网站并支持https，请执行：

sudo apt-get install flashplugin-nonfree

如果不满足条件而你不幸误执行了以上命令，并看到类似下面的消息：

正在设置 flashplugin-nonfree (9.0.48.0.0ubuntu1~7.04.1) ...
Downloading...
--20:47:05--
[http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_9_](http://fpdownload.macromedia.com/get/flashplayer/current/install_flash_player_9_)
linux.tar.gz
=> `./install_flash_player_9_linux.tar.gz'
Resolving fpdownload.macromedia.com... 122.252.42.70
Connecting to fpdownload.macromedia.com|122.252.42.70|:80...

那么请Ctrl+c结束，然后

sudo apt-get remove --purge flashplugin-nonfree

* 如果不能连接国外网站或不支持https，请到http://ftp.ubuntu.org.cn 下载

下载后安装：

tar -zxvf install_flash_player_9_linux.tar.gz
cd install_flash_player_9_linux/
sudo ./flashplayer-installer

[编辑] 安装插件/扩展

查看firefox当前所安装的插件,在地址栏中输入：

about:plugins

从这个地址安装多线程下载扩展downthemall ：

[http://addons.mozine.cn/firefox/89/](http://addons.mozine.cn/firefox/89/)

从这个地址安装在线观看视频扩展mediawarp ：

[http://addons.mozine.cn/firefox/116/](http://addons.mozine.cn/firefox/116/)

从这个地址安装广告过滤扩展Adblock_Plus：

[http://addons.mozine.cn/firefox/125/](http://addons.mozine.cn/firefox/125/)

[编辑] 配置firefox

在址址栏中输入：

about:config

如果你对第三方Firefox发行版Swiftfox感兴趣，请访问Swiftfox浏览器

[编辑] 安装支持BT/电驴/Gnutella1/Gnutella2等下载软件
[编辑] 安装BT下载软件

1. 在Ubuntu中，打开终端，执行以下命令，或使用新立得，在其中搜索azureus并标记安装。

sudo apt-get install deluge-torrent

安装完成后的快捷方式在应用程序 -> Interne t-> Deluge BitTorrent Client，该软件支持Bit Torrent协议。

2. 在Kubuntu中，打开终端，执行以下命令，或使用Adept manager，在其中搜索ktorrent，并标记安装。

sudo apt-get install ktorrent

安装完成后的快捷方式在应用程序 -> Internet -> Ktorrent，该软件支持Bit Torrent协议。
[编辑] 安装电驴下载软件（可选）

安装支持p2p/ftp/http的下载软件mldoneky。

在Ubuntu中，打开终端，执行以下命令，或使用Adept/新立得，在其中搜索并标记安装。

sudo apt-get install kmldonkey mldonkey-server

安装过程中，需要用户配置是否在开机时自动启动：

mldonkey-server(Launch MLDonkey at startup?

这时建议选择"是"，以方便进行配置。若选择是以后，在接下来的配置过程中对大部份选项都用默认设置，不过在设置的帐号密码时，最好重新设置下。安装完mldonkey以后，若想开机不自行启动mldonkey-server，可以运行sudo dpkg-reconfigure mldonkey-server进行设置。

当完成kmldonkey mldonkey-server的安装以后，可以在firefox或者konqueror等浏览器的地址栏里输入http://127.0.0.1:4080/ 来直接访问mldonkey，也可以使用快捷方式（应用程序 -> Internet -> KMLDonkey）。

mldonkey缺省只支持电驴（edonkey2000）协议，若要支持BT/ftp/http/Gnutella等协议，需自行在配置菜单里开启。详细步骤请参考文档或自行摸索。