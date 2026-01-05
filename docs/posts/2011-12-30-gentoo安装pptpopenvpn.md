---
title: "Gentoo安装PPTP/OpenVPN"
date: 2011-12-30
author: pengjianqing
categories: ['生活随笔']
---

在Gentoo上安装PPTP/OpenVPN客户端

需要在kernel打开相关选项
1.PPTP参考:
http://en.gentoo-wiki.com/wiki/PPTP
```

 Device Drivers --->
   Networking support --->

    PPP (point-to-point protocol) support
   [ ] PPP multilink support (EXPERIMENTAL)
   [*] PPP filtering

    PPP support for async serial ports
    PPP support for sync tty ports
    PPP Deflate compression
    PPP BSD-Compress compression
    Microsoft PPP compression/encryption (MPPC/MPPE)

 -*- Cryptographic API  --->

      SHA224 and SHA256 digest algorithm
      SHA384 and SHA512 digest algorithms

    Deflate compression algorithm

```

2.OpenVPN参考:

http://en.gentoo-wiki.com/wiki/OpenVPN
```

Device Drivers --->
   Network device support --->
[*]Network device support
   Universal TUN/TAP device driver support  // This option must be enabled

```

3.同时升级了一下Linux Kernel到3.0.6
使用之前的.config文件
```
cp config-2.6.39-r3  linux/.config
```

Copy一下之前的bcm firmware网卡驱动
```

cp linux-2.6.39-gentoo-r3/firmware/bcm43xx-0.fw* linux/firmware/

```

4.编译，安装新内核
```

make -j5
make modules_install
cp arch/x86/boot/bzImage /boot/kernel-3.0.6-gentoo
module-rebuild rebuild
grub2-mkconfig -o /boot/grub2/grub.cfg

```

5.使用PPTP/OpenVPN
```

pptpsetup --create pptpvpn --server 173.255.xx.xx --username xxxx --password xxxx
openvpn --config client.conf

```

Issues:
1.发现用OpenVPN后,无法解析ip
只好添加一个DNS,添加后一切正常:
```

echo "nameserver 8.8.8.8" >>/etc/resolv.conf

```

2.安装NetworkManager
http://en.gentoo-wiki.com/wiki/NetworkManager
添加到默认启动
```

rc-update add NetworkManager default

```

安装nm-applet时,发生了编译错误,参考添加keywords:
http://forums.gentoo.org/viewtopic-t-903500-start-0.html
```

  gentoo init.d # grep nm-applet /etc/portage/package.keywords 
 gnome-extra/nm-applet ~x86

```

3.直接创建一个alias,方便启动OpenVPN
```

alias openvpn_start='cd /etc/openvpn&&sudo openvpn --config client.conf'

```