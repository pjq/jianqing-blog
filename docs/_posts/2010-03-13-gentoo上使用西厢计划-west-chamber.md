---
title: "Gentoo上使用“西厢计划” (west-chamber)"
date: 2010-03-13
author: pengjianqing
categories: ['gentoo', 'Linux']
tags: ['GFW', 'west-chamber', '西厢计划，iptables']
---

[ Gentoo上使用“西厢计划” (west-chamber)](http://docs.google.com/View?id=dg9p7dc4_93cp347zgh)Technorati Tags: [GFW](http://technorati.com/tag/GFW), [西厢计划](http://technorati.com/tag/西厢计划), [Gentoo](http://technorati.com/tag/Gentoo), [west-chamber](http://technorati.com/tag/west-chamber), [iptables](http://technorati.com/tag/iptables)

这里是此项计划的说明：
[http://code.google.com/p/scholarzhang/wiki/README](http://code.google.com/p/scholarzhang/wiki/README)

此项计划一出立刻在网络上，引起了轰动，到处都是关于它的讨论。
我也对这个很好奇，想早点看一下这个到底是什么东西。

下面简要记述一下我安装的过程和遇到的一些问题：
1.下载
[http://scholarzhang.googlecode.com/files/west-chamber-0.0.1.tar.gz](http://scholarzhang.googlecode.com/files/west-chamber-0.0.1.tar.gz)

2.安装
[http://code.google.com/p/scholarzhang/wiki/INSTALL](http://code.google.com/p/scholarzhang/wiki/INSTALL)安装说明中有如下说明：
```

iptables >= 1.4.3
kernel >= 2.6.17 (>= 2.6.18.5 if 2.6.18.x)
- CONFIG_NF_CONNTRACK or CONFIG_IP_NF_CONNTRACK
- CONFIG_NF_CONNTRACK_MARK or CONFIG_IP_NF_CONNTRACK_MARK enabled =y or as module (=m)

```

（1）在实际的安装过程中，有遇到iptables版本不对，match-set不存在的错误，只好将iptables 升级到新版本。
目前我的版本：

```

gentoo-pjq xtables # iptables --version
iptables v1.4.7

```

（2）还有就是ipset的版本不对：
```

gentoo-pjq examples # ipset -R  /etc/resolv.conf

```

如果不想每次都把这些命令敲一遍，把它们都扔到一个脚本里：
```

pjq@gentoo-pjq ~/Downloads/west-chamber-0.0.1/examples $ cat startwest.sh
#!/bin/bash

echo "ipset -R /etc/resolv.conf"
echo "nameserver 8.8.8.8" >/etc/resolv.conf
pjq@gentoo-pjq ~/Downloads/west-chamber-0.0.1/examples $

```

4.如果在使用iptables设置规则的时候没出现什么问题，
那就应该设置成功了，可以查看一下，
应该可以看到类似于下面的结果：
```

gentoo-pjq xtables # iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
DROP       tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw
DROP       tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw
DROP       tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw
ZHANG      tcp  --  anywhere             anywhere            tcp spt:http flags:FIN,SYN,RST,ACK/SYN,ACK state ESTABLISHED match-set NOCLIP src
DROP       udp  --  anywhere             anywhere            udp spt:domain state ESTABLISHED gfw
ZHANG      tcp  --  anywhere             anywhere            tcp spt:http flags:FIN,SYN,RST,ACK/SYN,ACK state ESTABLISHED match-set NOCLIP src
LOG        tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw LOG level info prefix `gfw: '
DROP       udp  --  anywhere             anywhere            udp spt:domain state ESTABLISHED gfw
ZHANG      tcp  --  anywhere             anywhere            tcp spt:http flags:FIN,SYN,RST,ACK/SYN,ACK state ESTABLISHED match-set NOCLIP src
LOG        tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw LOG level info prefix `gfw: '
DROP       udp  --  anywhere             anywhere            udp spt:domain state ESTABLISHED gfw
ZHANG      tcp  --  anywhere             anywhere            tcp spt:http flags:FIN,SYN,RST,ACK/SYN,ACK state ESTABLISHED match-set NOCLIP src
LOG        tcp  --  anywhere             anywhere            tcp spt:http state ESTABLISHED gfw LOG level info prefix `gfw: '
DROP       udp  --  anywhere             anywhere            udp spt:domain state ESTABLISHED gfw

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
gentoo-pjq xtables #

```

5.如果一切顺利，可以测试网页了。
很郁闷的是，我还是不能打开youtube.com,但可以打开facebook.com,好像只有一次打开了youtube.com,之后就没打开过了，但facebook一直可以打开的。
感觉现在“西厢计划”现在还不是太稳定。很多功能还有待完善。

但还是非常感谢作者的努力，让我们看到了一些希望，希望“西厢计划”能够日臻完善，越来越强大，自由翻越GFW，

目前在Gentoo上还有更简单的方法安装它了，已经有人写了ebuild放到gentoo-china overlay了，感谢viogus。
见：
[http://code.google.com/p/scholarzhang/issues/detail?id=10](http://code.google.com/p/scholarzhang/issues/detail?id=10)
[http://www.linuxsir.org/bbs/thread364811.html](http://www.linuxsir.org/bbs/thread364811.html)

安装方法:
添加gentoo-china overlay就可以安装了
```

layman -a gentoo-china
layman -S
FEATURES="-sandbox" emerge west-chamber -av

```

![](http://img.zemanta.com/pixy.gif?x-id=91c2db39-b66e-85bd-a548-b3690e41540e)