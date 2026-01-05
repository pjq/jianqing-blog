---
title: "ubuntu GUI备份软件"
date: 2007-08-10
author: pengjianqing
categories: ['Software', 'Ubuntu']
---

ubuntu GUI备份软件

通过安装sbackup，再配合安装与sbackup对应的还原软件， 可以超过windwos系统还原的效果，但不能把ubuntu折腾捣鼓得过度：要能进到桌面，因为这个sbackup是个图形界面的软件
如果不能进桌面，一般
sudo dpkg-reconfigure xserver-xorg
即可

另外，我们也会经常会修改nautilus相关的配制，比如面板，对nautilus的配制进行备份可以安装：
sudo apt-get install gnome-reset
安装好后，点系统------>首选项-------->备份首选项
备份好后，如果有一天想恢复成原样，则
点系统------>首选项-------->恢复首选项