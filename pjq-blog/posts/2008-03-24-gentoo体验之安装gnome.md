---
title: "Gentoo体验之安装gnome"
date: 2008-03-24
author: pengjianqing
categories: ['gentoo', 'Software']
---

Gentoo桌面文档资源
http://www.gentoo-cn.org/doc/zh_cn/index.xml?catid=desktop

gnome配置文档：

在配置xorg.conf时可以用xorgcfg     xorgconfig 这两个命令，

但我是直接将ubuntu中的xorg.conf copy过来的,因为硬件是一样的，所以配置也就应该差不多。事实说明这样确实管用，

http://www.gentoo-cn.org/doc/zh_cn/gnome-config.xml .

/etc/make.conf中USE范例
```
USE="-qt3 -qt4 -arts -kde X dbus gtk gnome hal avahi"
```

```

```

您可以添加brandingUSE标记来获得一个漂亮的“Gentoo牌”启动画面，取代默认的Gnome启动画面：
```
echo "gnome-base/gnome-session branding" >> /etc/portage/package.use
```

```

```

```
安装GNOME
emerge gnome
遇到依赖问题时可以先跳过去
```

```
emerge --skipfirst gnome
```

```

```

```
更新环境变量
# env-update && source /etc/profile
```

安装gamin，一个文件变更监视器
```
# emerge gamin
```

将hald和avahi-dnsconfd添加到默认启动级别
```
# /etc/init.d/hald start
# rc-update add hald default

# /etc/init.d/dbus start
# rc-update add dbus default

# /etc/init.d/avahi-dnsconfd start
# rc-update add avahi-dnsconfd default
```

```
设定GNOME为默认桌面环境
$ echo "exec gnome-session" > ~/.xinitrc
```

```

```

```

```

```
将xdm添加到默认运行级别
# rc-update add xdm default
```

```

```

```

```

```
编辑/etc/conf.d/xdm
DISPLAYMANAGER="gdm"
```

```

```

```

要使用hald的功能，只需启动gnome-volume-manager然后编辑它的选项。
```

```
并且，需要将您的用户添加到plugdev组。
```

```

```

```

```