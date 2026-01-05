---
title: "镜像配置文件/etc/apt/mirror.list"
date: 2007-12-30
author: pengjianqing
categories: ['Config Files', 'Ubuntu']
---

`  sudo gedit /etc/apt/mirror.list`

`
############# config ##################
#
set base_path    /media/sda6/var/spool/apt-mirror
#
# if you change the base path you must create the directories below with write privlages
#
set mirror_path  $base_path/mirror
set skel_path    $base_path/skel
set var_path     $base_path/var
# set cleanscript $var_path/clean.sh
# set defaultarch  
set nthreads     5
set tilde 0
#
############# end config ##############
#ubuntu-cn
deb http://archive.ubuntu.org.cn/ubuntu-cn/ gutsy main restricted universe multiverse
#中国科技大学(USTC) ubuntu 7.10 源
deb http://debian.ustc.edu.cn/ubuntu/ gutsy main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ gutsy-backports restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ gutsy-proposed main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ gutsy-security main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ gutsy-updates main restricted universe multiverse
`