---
title: "Gentoo体验之路之fcitx安装"
date: 2008-03-27
author: pengjianqing
categories: ['gentoo', 'Software']
---

源里的fcitx版本太低了，要安装fcitx3.5时要unmask

如果没有autounmask请先emerge autounmask

autounmask  app-i18n/fcitx-3.5_pre070703

然后再emerge fcitx

如果不能正常显示中文

需要添加USE=“truetype”