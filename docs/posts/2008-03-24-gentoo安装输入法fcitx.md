---
title: "gentoo安装输入法fcitx"
date: 2008-03-24
author: pengjianqing
categories: ['gentoo', 'Software']
---

##  安装

为了能够正确显示中文，安装时要在use中加上truetype
```
# USE="truetype" emerge fcitx
```

##  自动启动

为了使fcitx随X启动，需要编辑（或创建）文件*~/.xprofile*，其内容为：
```
export XMODIFIERS=@im=fcitx
export GTK_IM_MODULE="fcitx"
fcitx
```

保存文件，重新启动X，小企鹅输入法就可以用了。

在每次编译内核后，如果不能正确显示中文

需要重新编译fcitx
```
 USE="truetype" emerge fcitx
```