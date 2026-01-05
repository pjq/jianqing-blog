---
title: "无意中看到autounmask BUG解决方法了"
date: 2008-09-04
author: pengjianqing
categories: ['gentoo']
---

在http://forums.gentoo.org看到了张乐的将blog加入到planet的贴子，然后就点开那个[planet](http://planet.gentoo-cn.org/)随便浏览了一下，就看到了autounmask 的[解决方法](http://www.jdkcn.com/entry/autounmask-loops-never-ending.html)了
[
BUG在这里
](http://bugs.gentoo.org/show_bug.cgi?id=216484)

只要将my $arch               = $pxs->getArch();
改为my $arch                = '~x86';
就行了。
最近linuxsir一直被和谐了，有传言说有人在上面发买卖军火的帖子，不知真假。
那上面有很多总结很好的帖子，现在上不去都不知道去哪里找寻问题答案了，英文的GENTOO官方，我这里上去很慢，点开一个网页还要等半天，什么时候也能够有一个独立的GETNOO-CN中文论坛？
r0bertz一直很努力，希望不久的将来就能有了。
牛人比较强大，在很多地方都有老巢：
Zhang Le, Robert
http://www.gentoo-cn.org
http://r0bertz.blogspot.com
http://zhllg.spaces.live.com