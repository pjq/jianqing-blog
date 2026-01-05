---
title: "删除distfiles里面过期文件的方法"
date: 2008-03-24
author: pengjianqing
categories: ['Command', 'gentoo']
---

# eclean-dist -d

-d 表示仅保留最少的源码包 - 仅包含目前系统中安装的那些, 以备 rebuild 某个软件时使用.

为了安全, 可以先加 -p 选项看看都有哪些包会被清除:

**代码:**

# eclean-dist -p -d