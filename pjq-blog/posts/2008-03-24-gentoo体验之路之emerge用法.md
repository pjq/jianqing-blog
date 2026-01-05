---
title: "Gentoo体验之路之emerge用法"
date: 2008-03-24
author: pengjianqing
categories: ['Command', 'gentoo']
---

Gentoo下emerge用法

避免升级覆盖掉版本更高的软件

emerge -uU world
emerge --update --upgradeonly world

查找名称包含mozilla的包

emerge -s mozilla
emerge search mozilla

查找描述包含mozilla

emerge -S mozilla
emerge --searchdesc mozilla

使用本地编好的包，没有就下源码(尽量避免编译)

emerge -k mozilla
emerge --usepkg mozilla

只使用本地编好的，否则不安装(绝对不编译，所有依赖的包都有binary才装)

emerge -K mozilla
emerge --usepkgonly mozilla

卸载
emerge -C mozilla
emerge unmerge mozilla

升级portage树

emerge sync

下载snapshot包来完成sync
emerge-webrsync

查看已安装包的changelog

emerge -pl mozilla
emerge --pretend --changelog mozilla

查看依赖关系(这个包还没装)
(--pretend保证这一次操作实际上不做任何事情，可以跟任何options组合)
emerge -p mozilla
emerge --pretend mozilla

只下载某个软件的源码(以及它所依赖的)

emerge -f mozilla
emerge --fetchonly mozilla

查看从哪下的源码

emerge -fp mozilla

安装指定版本号的

emerge "..........."

emerge -k "

从网上下binary包来装

emerge -g mozilla
emerge --getbinpkg mozilla
(注意，实际上没有任何binary包存在于官方的mirror中
所以这个基本上是无用，在manpage也没有出现。除非自
己用livecd来setup一个这样的站点。不知道以后会不会
出现这样的mirror。gentoo.org论坛上似乎也有讨论这个。)

查看binary包依赖

emerge -gp mozilla
emrege --getbinpkg --pretend mozilla

查看依赖关系(这个包已经装了)

emerge -ep opera
emerge --emptytree --pretend opera
(不用pretend会重新编译这所有依赖的包，glibc因为安全关系没有列出)

不使用依赖关系安装软件

emerge -O opera
emerge --nodeps opera

只安装其依赖的软件
emerge -o opera
emerge --onlydeps opera

升级软件
emerge -u opera
emerge --update opera

升级系统软件

emerge -u system

升级整个系统

emerge -u world

避免升级覆盖掉版本更高的软件

emerge -uU world
emerge --update --upgradeonly world

查看可用的USE参数

emerge -pv opera

emerge -uD --newuse world

emerge -uD --newuse system