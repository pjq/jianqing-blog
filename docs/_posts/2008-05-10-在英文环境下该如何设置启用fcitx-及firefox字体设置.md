---
title: "在英文环境下该如何设置启用fcitx 及firefox字体设置"
date: 2008-05-10
author: pengjianqing
categories: ['Software']
tags: ['en_US.UTF-8', 'fcitx', 'firefox', 'LC_CTYPE', '字体']
---

原文讨论在这里

 http://www.linuxsir.org/bbs/thread327733.html

将系统登录时候设置为英文，查看locale
`locale
LANG=en_US.UTF-8
LC_CTYPE=zh_CN.UTF-8 //输入法设置
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
`

启用fcitx

` cat ~/.profile
export LANG="en_US.UTF-8"
export LANGUAGE="en_US:en"
export LC_CTYPE="zh_CN.UTF-8"
export XMODIFIERS="@im=fcitx"
export XIM="fcitx"
export XIM_PROGRAM="fcitx"
`

然后在开始会话中加入
`fcitx -d`
注销之后，进入系统，就能在英文环境下启用fcitx了
进入英文系统后，我们会发现firefox中文显示出问题了，感觉很别扭，而且自己在firefox里设置的字体不起作用。
到网上找了一通，找到了一个设置firefox 字体的方法。试了一下管用.

> 有关gnome & gtk*的字体配置，在各人机器上总会有些不一。一种配置，适合我；可能并不一定适合别人。软件本身的说明往往是最有说服力，配置起来也最有效果的吧。这里也提供一个参考，给字体设置的朋友一点微薄的希望。

firefox官方doc中写道：
Code:
Much of Mozilla's fonts and colors are controlled via CSS (Cascading Style Sheets).
These are set in .css files in Mozilla's chrome directories, but the user can override them with two plain text files, called userContent.css and userChrome.css.

那下面就写一下最最简单的一种配置吧。

1、建立*.css
Code:
$cd ~/.mozilla/firefox/*.default/chrome
$cp userChrome-example.css userChrome.css
$cp userContent-example.css userContent.css

2、写入内容
1）把下面一段attach到userChrome.css后面：
Code:
* {
font-size: 9pt !important;
font-family: 微软雅黑 !important;
}

Note：那“微软xx"是自己设定的。正确的字体名称很重要。在文件浏览器中输入fonts://，查看字体属性，name一栏的就是。

上面的通配符，包括了bookmarks和tab字体的显示。有这方面困惑的朋友不妨一试。

2）把下面一段attach到userContent.css后面：
Code:
* {
font-size: 9pt !important;
font-family: 微软雅黑 !important;
}

Note：同上。
很明显这是网页内容的字体设置了。

3、Notes：
1）浏览器的preference中的font类型设置，默认就行。请允许页面选择自己的字体，这也是默认的。调整好最小字体大小。

2）1024x768的dpi(gnome的在字体设置的details里面)，最好设置为90左右。gnome程序界面字体大小，请自行调整。别的分辨率的dpi，请google。

3）通配符未免一棒打死，失去了页面的多样性。深入些的，请查看官方css自定义帮助。

我试了下，感觉第3条（1）没什么作用，

字体大小可以根据自己的情况试一下，我的设为font-size: 12pt !important;
重启firefox字体是不变得和以前一样好看了呢？