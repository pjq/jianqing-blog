---
title: "gentoo之gnome-light安装"
date: 2008-06-04
author: pengjianqing
categories: ['gentoo']
---

分区情况：

sda8         /swap            2G

sda9            /boot          100M

sda10          /home         8G

sda11          /                  17G

这次重新安装gentoo桌面选择了gnome-light,安装过程基本上顺利，

安装完之后，进入系统，欢迎界面很简单，只有一个登录框。

先是修改字体

http://zh.gentoo-wiki.com/index.php?title=HOWTO_%E5%A2%9E%E5%8A%A0%E5%AD%97%E4%BD%93&variant=zh-cn

之后设置firefox字体。

安装ntfs3g

安装usb自动挂载支持

http://zh.gentoo-wiki.com/index.php?title=HOWTO_%E8%87%AA%E5%8A%A8%E6%8C%82%E8%BD%BDUSB%E7%A7%BB%E5%8A%A8%E7%A1%AC%E7%9B%98%E5%B9%B6%E6%98%BE%E7%A4%BA%E4%B8%AD%E6%96%87&variant=zh-cn

安装输入法fcitx

不知为什么 pre070703版的编译不成功，只能选择默认的版本了。

http://zh.gentoo-wiki.com/index.php?title=HOWTO_%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95&variant=zh-cn

设置locale以在英文环境下使用中文输入法

http://zh.gentoo-wiki.com/index.php?title=HOWTO_%E4%B8%AD%E6%96%87%E8%BE%93%E5%85%A5%E6%B3%95%E7%94%A8%E4%BA%8E%E8%8B%B1%E6%96%87%E7%95%8C%E9%9D%A2&variant=zh-cn

安装stardict

安装pidgin

安装媒体播放器

mplayer,realplayer,audacious

安装文字编辑器

gedit

安装永中office

安装VirtualBox

安装gconf-editor

安装sun-jdk

安装gnome默认的PDF阅读器evince

gnome-light很简单， 要什么东西就装什么，很自由。

默认applications里只装了firefox,叫做Bon Echo，不知道为什么叫这个名字。System里只有Preference一项，记得以前是两项的，Preference里只有一些最基本的东西，只有13项。

很多howto在这里

http://zh.gentoo-wiki.com/index.php?title=Index:HOWTO&variant=zh-cn#.E5.AD.97.E4.BD.93

这里备份一些配置文件：

pjq@localhost ~ $ cat /etc/fstab
# /etc/fstab: static file system information.
#
# noatime turns off atimes for increased performance (atimes normally aren't
# needed; notail increases performance of ReiserFS (at the expense of storage
# efficiency).  It's safe to drop the noatime options if you want and to
# switch between notail / tail freely.
#
# The root filesystem should have a pass number of either 0 or 1.
# All other filesystems should have a pass number of 0 or greater than 1.
#
# See the manpage fstab(5) for more information.
#

#                                 

# NOTE: If your BOOT partition is ReiserFS, add the notail option to opts.
/dev/sda9        /boot        ext2        noauto,noatime    1 2
/dev/sda11        /        ext3        noatime        0 1
/dev/sda8        none        swap        sw        0 0
/dev/sda10              /home           ext3           noatime          0 1
/dev/cdrom        /mnt/cdrom    auto        noauto,ro    0 0
#/dev/fd0        /mnt/floppy    auto        noauto        0 0

/dev/sda1    /media/sda1      ntfs-3g    defaults,locale=zh_CN.UTF-8,umask=002  0   0
/dev/sda5   /media/sda5       ntfs-3g    defaults,locale=zh_CN.UTF-8,umask=002   0  0
/dev/sda6    /media/sda6     vfat      defaults,iocharset=utf8,umask=002 0  0
/dev/sda7     /media/sda7    vfat      defaults,iocharset=utf8,umask=002  0   0

# glibc 2.2 and above expects tmpfs to be mounted at /dev/shm for
# POSIX shared memory (shm_open, shm_unlink).
# (tmpfs is a dynamically expandable/shrinkable ramdisk, and will
#  use almost no memory if not populated with files)
shm            /dev/shm    tmpfs        nodev,nosuid,noexec    0 0

#挂入内存

none    /tmp   tmpfs       defaults    0     0
none   /var/tmp  tmpfs     defaults   0          0
引导文件：menu.lst

localhost pjq # cat /boot/grub/menu.lst
# menu.lst - See: grub(8), info grub, update-grub(8)
#            grub-install(8), grub-floppy(8),
#            grub-md5-crypt, /usr/share/doc/grub
#            and /usr/share/doc/grub-doc/.

#gfxmenu (hd0,10)/boot/message.cristal
splashimage=(hd0,8)/boot/grub/splash.xpm.gz
default        0

timeout        4

title Gentoo-2.6.24-r8
root (hd0,8)
kernel /boot/kernel-2.6.24-r8 root=/dev/sda11  plash=silent,fadein,theme:gentoo vga=791  CONSOLE=/dev/tty1   ramdisk=8192
boot

title        Microsoft Windows XP Professional
root        (hd0,0)
savedefault
makeactive
chainloader    +1

# This entry automatically added by the Debian installer for an existing
# linux installation on /dev/sda8.
#title        Debian GNU/Linux, kernel 2.6.22-14-generic (on /dev/sda8)
#root        (hd0,7)
#kernel        /boot/vmlinuz-2.6.22-14-generic root=/dev/sda8 ro
#initrd        /boot/initrd.img-2.6.22-14-generic
#savedefault
#boot

# This entry automatically added by the Debian installer for an existing
# linux installation on /dev/sda8.
#title        Debian GNU/Linux, kernel 2.6.22-14-generic (recovery mode) (on /dev/sda8)
#root        (hd0,7)
#kernel        /boot/vmlinuz-2.6.22-14-generic root=/dev/sda8 ro single
#initrd        /boot/initrd.img-2.6.22-14-generic
#savedefault
#boot

# This entry automatically added by the Debian installer for an existing
# linux installation on /dev/sda8.
#title        Debian GNU/Linux, kernel memtest86+ (on /dev/sda8)
#root        (hd0,7)
#kernel        /boot/memtest86+.bin
#savedefault
#boot
title Gentoo-2.6.24
ioot (hd0,7)
kernel /boot/kernel-2.6.24 root=/dev/sda9 splash quiet
boot
#title Gentoo Alsa Sound
#root (hd0,7)
#kernel /boot/kernel-gen root=/dev/sda9 splash quiet
#boot

#
#title Gentoo-gen
#root (hd0,7)
#kernel /boot/kernel-gen root=/dev/ram0 init=/linuxrc ramdisk=8192 real_root=/dev/sda9 udev splash quiet
#initrd /boot/initrd-gen

#title Gentoo install
#root (hd0,6)
#kernel /isolinux/gentoo root=/dev/ram0 init=/linuxrc acpi=ht looptype=squashfs loop=/image.squashfs udev nodevfs cdroot=/dev/hda7 doscsi vga=791 dokeymap splash=silent,theme:livecd-2007.0
#initrd /isolinux/gentoo.igz
#boot
title gentoo install
root (hd0,6)
kernel /isolinux/gentoo root=/dev/ram0 init=/linuxrc  dokeymap looptype=squashfs loop=/image.squashfs  cdroot initrd=gentoo.igz vga=791 splash=silent,theme:livecd-2006.1 CONSOLE=/dev/tty1 quiet
initrd /isolinux/gentoo.igz
boot