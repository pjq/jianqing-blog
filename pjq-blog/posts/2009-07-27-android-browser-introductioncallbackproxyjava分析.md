---
title: "Android Browser Introduction:CallbackProxy.java分析"
date: 2009-07-27
author: pengjianqing
categories: ['自由分类']
tags: ['Android', 'Browser', 'Webkit', 'WebView']
---

文件在:frameworks\base\core\java\android\webkit
CallbackProxy:
这是一个继承自Handle的类,用来实现UI和WebViewCore之间交换的桥梁.
它里面定义了很多函数,这些函数里面基本上都只是完成了一个sendmessage的作用.它将message发送给自身的HandleMessage().然后按照类型再进去分发.
它定义了一些事件ID:
```

    // Message Ids
    private static final int PAGE_STARTED         = 100;
    private static final int RECEIVED_ICON        = 101;
    private static final int RECEIVED_TITLE       = 102;
    private static final int OVERRIDE_URL         = 103;
    private static final int AUTH_REQUEST         = 104;
    private static final int SSL_ERROR            = 105;
    private static final int PROGRESS             = 106;
    private static final int UPDATE_VISITED       = 107;
    private static final int LOAD_RESOURCE        = 108;
    private static final int CREATE_WINDOW        = 109;
    private static final int CLOSE_WINDOW         = 110;
    private static final int SAVE_PASSWORD        = 111;
    private static final int JS_ALERT             = 112;
    private static final int JS_CONFIRM           = 113;
    private static final int JS_PROMPT            = 114;
    private static final int JS_UNLOAD            = 115;
    private static final int ASYNC_KEYEVENTS      = 116;
    private static final int TOO_MANY_REDIRECTS   = 117;
    private static final int DOWNLOAD_FILE        = 118;
    private static final int REPORT_ERROR         = 119;
    private static final int RESEND_POST_DATA     = 120;
    private static final int PAGE_FINISHED        = 121;
    private static final int REQUEST_FOCUS        = 122;
    private static final int SCALE_CHANGED        = 123;
    private static final int RECEIVED_CERTIFICATE = 124;
    private static final int SWITCH_OUT_HISTORY   = 125;

```

这里的每个ID都在HandleMessage()里做了相应的处理.

先看看第一个吧:PAGE_STARTED
这个应该是开始load page了,而且跑到这个地方的page一定要是:iframes or framesets(这两个是什么?),其它形式的页面不会跑这个.
很奇怪onPageStarted的函数内容为空.WebViewClient里的函数也都是空了,查了一下,原来在BrowserActivity里面Override了:
```

    private final WebViewClient mWebViewClient = new WebViewClient()
    private final WebChromeClient mWebChromeClient = new WebChromeClient()

```

知道了这个,我们就可以想象从WebCore传上来某个事件,通过某些途径调用了CallbackProxy里处理函数.
然后再通过HandleMessage()来分发出去.分发的时候,主要有两个client:WebViewClien,WebChromeClient,这两个client分别定义了一些处理函数,并在BrowserActivity里实现了函数体.
分析到这里我们就能理解了为什么说CallbackProxy里沟通WebCore和UI Thread的桥梁了.

试了一个离线发布Blog的Firefox插件：[ScribeFire](https://addons.mozilla.org/en-US/firefox/addon/1730),原来发布博客是这么简单的事情，以前都是登录到后台进行操作的，看来落后太多了。

-------------------------------------华丽的分割线-------------------------------------------
原来mpd可以播放ape,avi格式了，不知道还有其它格式吗？
创建数据库：mpd --create-db
将所有歌曲加到播放列表中去：mpc listall|mpc add
然后随便播放了，贴一个我写的播放的脚本：
```

pjq@gentoo-pjq ~ $ cat /usr/local/bin/pp
#########################################################################
# Author: pengjianqing@gmail.com
# Created Time: Wed 04 Feb 2009 06:41:20 PM CST
# File Name: pp.sh
# Description:
#########################################################################
#!/bin/bash
echo  -n Input the Music name:
read  music
list=`mpc listall|cat -n|grep -i $music`
echo "$list"
#mpc listall|cat -n|grep -i $music|cut -b-7|while read music
#do
#echo mpc play $music
#mpc play $music&
#done

echo -n Input the Music Number:
read  music
name=`echo "$list"|grep $music`
echo "Now playing music:"
mpc play $music

```

使用方法：
```

pjq@gentoo-pjq ~ $ pp
**Input the Music name:欧美**
  1521    occident golden records欧美金唱盘/01爱的力量(席琳迪翁).ape
  1522    occident golden records欧美金唱盘/03因为我爱你(沙金斯帝文).ape
  1523    occident golden records欧美金唱盘/04带走我的呼吸(柏林乐队).ape
  1524    occident golden records欧美金唱盘/05卡萨布兰卡(贝特希金斯).ape
  1525    occident golden records欧美金唱盘/07此情可待(理查马克斯).ape
  1526    occident golden records欧美金唱盘/08奔放的旋律(正直兄弟).ape
  1527    occident golden records欧美金唱盘/09爱你在心口难开(劳赛尔).ape
  1528    occident golden records欧美金唱盘/10以吻封缄(波比维顿).ape
  1529    occident golden records欧美金唱盘/11寂静之声(西蒙加芬克尔).ape
  1530    occident golden records欧美金唱盘/12一切都为你(布来恩亚当斯).ape
  1531    occident golden records欧美金唱盘/13昨日重现(卡本特).ape
  1532    occident golden records欧美金唱盘/14柠檬树(愚人花园).ape
  1533    occident golden records欧美金唱盘/15鸽子(胡利奥伊格莱西亚斯).ape
  1534    occident golden records欧美金唱盘/16斯卡布罗集市(莎拉.布莱曼).ape
  1535    occident golden records欧美金唱盘/17加州旅馆(老鹰乐队).ape
  1536    occident golden records欧美金唱盘/18去年圣诞(威猛乐队).ape
  1537    occident golden records欧美金唱盘/19巴比伦河(波尼姆).ape
  1538    occident golden records欧美金唱盘/20我发誓(四合为一).ape
  1539    occident golden records欧美金唱盘/21你的爱有多深(比吉斯).ape
  1540    occident golden records欧美金唱盘/22你的每次呼吸(斯汀).ape
  1541    occident golden records欧美金唱盘/23甜蜜的一天(玛丽亚.凯丽&男人男孩).ape
  1542    occident golden records欧美金唱盘/24航行.ape
  1543    occident golden records欧美金唱盘/25鞠一个躬(麦丹娜).ape
  1544    occident golden records欧美金唱盘/26说我爱你...却说谎言(迈克尔.鲍顿).ape
  1545    occident golden records欧美金唱盘/27无论如何(男孩地带).ape
  1546    occident golden records欧美金唱盘/28天使(莎拉.克劳克兰).ape
  1547    occident golden records欧美金唱盘/29英雄(玛丽亚.凯丽).ape
  1548    occident golden records欧美金唱盘/30玫瑰之吻(席尔).ape
  1549    occident golden records欧美金唱盘/31天长地久(丹佛格伯).ape
  1550    occident golden records欧美金唱盘/32我相信我能飞(阿.凯利).ape
  1551    occident golden records欧美金唱盘/33别让我担心(托尼.布莱克斯顿).ape
  1552    occident golden records欧美金唱盘/34迷失的爱(空气补给者).ape
  1553    occident golden records欧美金唱盘/35诺言来之不易(卡诺.南汀格尔).ape
  1554    occident golden records欧美金唱盘/36无须知道太多(阿隆内维尔与琳达罗斯坦).ape
  1555    occident golden records欧美金唱盘/37改变世界(艾力克.克莱普顿).ape
  1556    occident golden records欧美金唱盘/38每当我闭上双眼(娃娃脸).ape
  1557    occident golden records欧美金唱盘/39当我最需要你的时候(南迪范华梅).ape
  1558    occident golden records欧美金唱盘/40风之彩(凡妮莎.威廉姆斯).ape
  1559    occident golden records欧美金唱盘/41你仍是唯一(仙妮亚.唐恩).ape
  1560    occident golden records欧美金唱盘/42好男人(罗比.威廉姆斯).ape
  1561    occident golden records欧美金唱盘/43没有你(玛丽亚凯丽).ape
  1562    occident golden records欧美金唱盘/44爱情圣手(萨黛).ape
  1563    occident golden records欧美金唱盘/45泪洒天堂(艾力克克莱普顿).ape
  1564    occident golden records欧美金唱盘/46情深似海(科里夫理查德).ape
  1565    occident golden records欧美金唱盘/47有你相伴(费丝.希尔).ape
  1566    occident golden records欧美金唱盘/48你的至爱(格雷佛勒).ape
  1567    occident golden records欧美金唱盘/49我将永远爱你(惠特尼休斯顿).ape
  1568    occident golden records欧美金唱盘/50也会伤害我的心(阿隆.内维尔).ape
  1569    occident golden records欧美金唱盘/51真诚的.疯狂的.深刻的(野人花园).ape
  1570    occident golden records欧美金唱盘/52让我拥抱你.宝贝(翠西.查普蔓).ape
  1571    occident golden records欧美金唱盘/53无心呢喃(威猛乐队).ape
  1572    occident golden records欧美金唱盘/54谢谢(蒂朵).ape
  1573    occident golden records欧美金唱盘/55冲破禁忌(菲尔.柯林斯).ape
  1574    occident golden records欧美金唱盘/56亲亲吾爱(西域男孩).ape
  1575    occident golden records欧美金唱盘/57天堂里的另一天(菲尔科林斯).ape
  1576    occident golden records欧美金唱盘/58无尽的爱(莱昂里奇戴安娜罗斯).ape
  1577    occident golden records欧美金唱盘/59当男女相爱时(迈克鲍顿).ape
  1578    occident golden records欧美金唱盘/60一切都为你(布来恩亚当斯).ape
  1579    occident golden records欧美金唱盘/61一无所有(惠特尔.休斯顿).ape
  1580    occident golden records欧美金唱盘/62真情自我(克里斯汀娜).ape
  1581    occident golden records欧美金唱盘/63亲密接触(洛德.斯图尔特).ape
  1582    occident golden records欧美金唱盘/64我该如何生活.ape
  1583    occident golden records欧美金唱盘/65只有爱(真情马克).ape
  1584    occident golden records欧美金唱盘/66悲伤布兰妮(小甜甜布兰妮).ape
  1585    occident golden records欧美金唱盘/67风中之烛(艾尔顿.约翰).ape
  1586    occident golden records欧美金唱盘/68世界无限大(艾美莉亚).ape
  1587    occident golden records欧美金唱盘/69那是你离去的理由(麦克学摇滚).ape
  1588    occident golden records欧美金唱盘/70你并不孤独(迈克尔.杰克逊).ape
  1589    occident golden records欧美金唱盘/71我用那种方式(后街男孩).ape
  1590    occident golden records欧美金唱盘/72每一次你离去(保罗杨).ape
Input the Music Number:1525
Now playing music:
理查.马克斯 - 此情可待
[playing] #1525/1590   0:00/4:32 (0%)
volume: 80%   repeat: off   random: off

```