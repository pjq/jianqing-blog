---
title: "弄好了网站访问统计工具:StatPressCN"
date: 2009-07-25
author: pengjianqing
categories: ['网站建设']
---

给wordpress装上了一个统计工具:StatPressCN,可以详细显示网站访问情况,一直很想要的效果,现在终于弄得差不多了.

备份一下详细配置:

```
自%since%起:
总访问量：%totalpagevisits%
总访问人数：%totalvisits%
文章总数：%blogtotalpost%
评论总数：%blogtotalcomment%
当前在线：%visitorsonline%
当前页面访问量：%thistotalvisits%
昨天访问人数：%yesterdayvisits%
您来自：%comefrom%
IP:%ip%
订阅数：%feeds%
最热门贴：%toppost%

```

现在改为下面这样了,需要通过查看网页源码才能查看到：
```

自%since%起:
总访问量:%totalpagevisits%
总访问人数:%totalvisits%
文章总数:%blogtotalpost%
评论总数:%blogtotalcomment%
当前在线:%visitorsonline%
当前页面访问量:%thistotalvisits%
昨天访问人数:%yesterdayvisits%
您来自:%comefrom%
IP:%ip%
订阅数:%feeds%
最热门贴:%toppost%

```

```

实际输出效果：
自2009年07月25日起:
总访问量:289
总访问人数:13
文章总数:115
评论总数:48
当前在线:1
当前页面访问量:201
昨天访问人数:13
您来自:江苏省
IP:114.219.89.190
订阅数:20
最热门贴:祝贺博客开通

```