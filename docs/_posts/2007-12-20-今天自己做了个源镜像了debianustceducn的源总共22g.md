---
title: "今天自己做了个源，镜像了(debian.ustc.edu.cn)的源,总共22G"
date: 2007-12-20
author: pengjianqing
categories: ['Ubuntu']
---

今天自己做了个源，镜像了(debian.ustc.edu.cn)的源,总共22G

最新加入了ubuntu-cn源!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

版本：ubuntu 7.10(gutsy)
参考：http://forum.ubuntu.org.cn/viewtopic.php?t=53155

###############################################

如果想做源的话，可以将我ftp根目录下/var目录下载下来，
然后请参考下面3种的设置方法中的一种设置一下，就可以用了：）
祝你好运 :)

###########################################
ps.ftp地址:ftp://10.0.1.112（一般情况下都是这个）

###########################################

时间不能保证，一般我开机后，就可以用了
时间：11：30am-1:00pm/5:30pm-6:30pm/10:10pm-11:00pm

有问题，可以发到我的邮箱

##############################################
下面是我的源地址(请选用ftp,http暂时没开):
在我ftp目录/mysourcelist下面也有

*******************************************************************
1. 建在vsftp上
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu gutsy main restricted universe multiverse
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu gutsy-backports restricted universe multiverse
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu  gutsy-proposed main restricted universe multiverse
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu  gutsy-security main restricted universe multiverse
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu  gutsy-updates main restricted universe multiverse

#ubuntu-cn
deb ftp://10.0.1.112/var/spool/apt-mirror/mirror/archive.ubuntu.org.cn/ubuntu-cn/ gutsy main restricted universe multiverse

******************************************************************
2.或者http(http服务暂时没开,因为vsftp可以正常使用,自己测试过没问题)

deb http://10.0.1.112/ubuntu/ubuntu/ gutsy main restricted universe multiverse
deb http://10.0.1.112/ubuntu/ubuntu/ gutsy-backports restricted universe multiverse
deb http://10.0.1.112/ubuntu/ubuntu/ gutsy-proposed main restricted universe multiverse
deb http://10.0.1.112/ubuntu/ubuntu/ gutsy-security main restricted universe multiverse
deb http://10.0.1.112/ubuntu/ubuntu/ gutsy-updates main restricted universe multiverse

#ubuntu-cn
deb http://10.0.1.112/ubuntu-cn/ubuntu-cn/ gutsy main restricted universe multiverse

********************************************************************
3. 如果只是自己用用，可以如下设置源(这是我的,仅供参考)
(/media/sda6=windows下e盘)

deb file:///media/sda6/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu/ gutsy main restricted universe multiverse
deb file:///media/sda6/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu/ gutsy-backports restricted universe multiverse
deb file:///media/sda6/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu/ gutsy-proposed main restricted universe multiverse
deb file:///media/sda6/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu/ gutsy-security main restricted universe multiverse
deb file:///media/sda6/var/spool/apt-mirror/mirror/debian.ustc.edu.cn/ubuntu/ gutsy-updates main restricted universe multiverse

#ubuntu-cn
deb file:///media/sda6/var/spool/apt-mirror/mirror/archive.ubuntu.org.cn/ubuntu-cn/ gutsy main restricted universe multiverse

################################################
下面是广告时间：                                                                            ##
ubuntu----linux for human beings                                              ##
http://www.ubuntu.org.cn                                                            ##
中文论坛:http://forum.ubuntu.org.cn                                           # #
################################################