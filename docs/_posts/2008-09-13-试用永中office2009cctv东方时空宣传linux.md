---
title: "试用永中office2009&CCTV东方时空宣传linux"
date: 2008-09-13
author: pengjianqing
categories: ['gentoo', 'Linux', 'Software']
---

1.先下载

axel -o /home/pjq/EIO2009_Trial_ZH_Lin.tar.gz  http://218.90.147.70/EverMore/EIOffice2009/EIO2009_Trial_ZH_Lin.tar.gz

2.然后参考安装文档安装

先卸载EIOffice 2007

sudo rmeio

cd 到目录

sudo chmod +x setup

sudo ./setup

安装完后，发现一个问题，启动eio发现字体不能正常显示，都是一个小方框。

网上搜索了一下，原来是字体权限有问题，

于是：sudo  chmod +r /usr/share/fonts/zh_CN/TrueType/*

再启动一下，正常显示。

由于安装了compiz,要修改/usr/bin/eio

添加  export AWT_TOOLKIT=MToolkit
打开文件一看里面有个判断的地方，我将里面的ubuntu直接改成了gentoo。

然后在compiz下正常启动eio, 一切OK

eioffice2009支持我国的UOF格式，从这点上也要顶一下。

linux上一直用的是永中office, 功能挺全的，也挺好的，希望它能够得到更好的发展。

**********************************************************************************************
今天在IRC#ubuntu-cn上看到东方时空关于“番茄花园案”的一个节目，马上打开链接，刚开始看到的是mms格式的链接，用mplayer打开速度太卡了。然后在网上搜索了一下，找到了[下载链接](http://v.cctv.com/flash//dongfangshikong/2008/09/dongfangshikong_300_20080912_1.flv)，然后赶紧下载下来：（大小89M）wget http://v.cctv.com/flash//dongfangshikong/2008/09/dongfangshikong_300_20080912_1.flv -cS
后面有一段介绍linux的内容，介绍的挺不错的，希望更多的人都能试用一下linux.