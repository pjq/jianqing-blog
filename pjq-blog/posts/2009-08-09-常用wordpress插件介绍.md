---
title: "常用wordpress插件介绍"
date: 2009-08-09
author: pengjianqing
categories: ['自由分类']
---

装上了很多wordpress插件，下面简单介绍一下：

1.adsense-injection：顾名思义是关于adsense的，装上它，只要简单的设置一下你的ID，就会自动往你博客上放google广告了，可以指定位置，也可以随机，还可以指定广告牌大小，哪些页面显示，哪些不显示，功能强大，看起来很智能，投放google adsense广告必备工具。
2.google-analyticator：与google-analyticator帐号关联的插件，如果你已经注册了google-analyticator，就可以用它了，可以直接利用google-analyticator的网站统计数据。
3.plugin-manager：用来安装插件的，搜到你想要的插件后，直接点击安装就可以了，再不需要手动下载再上传了。

4.statpresscn:一个详细的网站统计工具，我之前写过一编[比较网站统计工具](http://www.impjq.net/blog/2009/08/02/google-analytics%e4%b8%8e%e9%9b%85%e8%99%8e%e9%87%8f%e5%ad%90%e7%bb%9f%e8%ae%a1%e5%88%86%e6%9e%90%e6%af%94%e8%be%83/)里有简单介绍。它生成的包括真的可以说是无所不包了。
5.twitter-for-wordpress:一个就是twitter了，看看我的网站就知道了，简单的设置好了你的twitter 帐号后，就会将你发的twitter内容链接显示过来了,twitter fans可以试试。
6.wordpress-thread-comment：发表评论插件，有了它，评论时就可以达到ajax效果，并且支持嵌套评论，还可以设置评论者邮箱，网址，很方便，很强大，如果你还没用过，完全有必要试试。
7.wp-mail-smtp：发邮件的，有时给别人评论时，都会提示”有新回复时是否发送邮件提醒“，那一般如何可以发送邮件了，特别服务器上没有邮件服务器？有了它，只要经过简单的设置，就可以自动连上你的邮箱，发邮件了，我设置的是gmail邮箱，很好用，有人评论时，第一时间，只要打开邮箱，就可以看到了。
8.wp-pagenavi：页面导航的，看看我的博客底下：age 1 of 1312345»10...Last »，就是它了，装上它，翻页就会很简单了。
9.wp-postviews：很重要的一个插件，装上它，就能直接看到你的某一篇文章的访问量了，你是不是很需要它？那还等什么赶紧装上吧。
10.wp-syntax：这个在贴代码时需要用到的，高亮显示语法的，贴代码时必备，比如java,c,c++等。
11.wp-wall:wall?=墙，没错，有点图鸦墙的意思，可以用它来实现快速回复，而不需要点到某篇文章之后再评论，怎么样，是不是很酷，有了它，朋友访问时想留言，只要简单的点下reply就行了，想试试它的效果吗？完全是ajax效果，试试我的就知道了。

暂时就用到了这么多插件，看看我的页面差不多都能对号入座了。
我把这些插件都打包了，以后要重装wordpress只要将他们上传，解压就好了，而不用再一个个去查找下载了。
[点这里下载](http://gentoo-pjq.cn/wp-content/plugins/wp_plugins.zip)。

那要如何解压呢？
将下面这段PHP代码，保存成unzip_wp_plugins.php
```

```

然后上传到wordpress安装plugins的目录，一般就是：/wp-content/plugins/，上面的那个压缩包也是放在这个目录下的。
然后再通过网页访问它这个PHP文件，就会自动解压了。

附：插件列表：
```

pjq@gentoo-pjq ~/Desktop/WP/wp_plugins/plugins $ ls -l
total 2152
drwxr-xr-x 2 pjq users    4096 2009-08-08 16:21 adsense-injection
drwxr-xr-x 3 pjq users    4096 2009-08-08 11:06 google-analyticator
drwxr-xr-x 3 pjq users    4096 2009-07-18 15:52 plugin-manager
drwxr-xr-x 5 pjq users    4096 2009-06-23 08:37 statpresscn
drwxr-xr-x 2 pjq users    4096 2009-07-10 19:22 twitter-for-wordpress
drwxr-xr-x 2 pjq users    4096 2009-08-08 11:06 wordpress-thread-comment
drwxr-xr-x 2 pjq users    4096 2009-08-08 11:06 wp-mail-smtp
drwxr-xr-x 2 pjq users    4096 2009-07-08 23:07 wp-pagenavi
-rw-r--r-- 1 pjq users 2147773 2009-08-08 16:43 wp_plugins.zip
drwxr-xr-x 2 pjq users    4096 2009-08-08 11:17 wp-postviews
drwxr-xr-x 4 pjq users    4096 2009-06-17 05:23 wp-syntax
drwxr-xr-x 3 pjq users    4096 2009-08-08 11:32 wp-wall

```