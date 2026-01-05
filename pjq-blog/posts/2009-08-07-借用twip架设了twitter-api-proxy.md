---
title: "借用twip架设了Twitter API proxy"
date: 2009-08-07
author: pengjianqing
categories: ['自由分类']
---

参考了这里http://li2z.cn/2009/08/07/twip/
过程很简单，将twip程序下载，上传到网站空间上，然后访问这个目录就可以了。
我放在网站根目录（/t）下，这样访问时只要通过http://www.impjq.net/t/访问就行了。

在~/.mozilla目录下找到文件nsTwitterFox.js，修改它就行了。
```

pjq@gentoo-pjq ~ $ find ~/.mozilla/ -iname "*.js"|grep -i twit
/home/pjq/.mozilla/firefox/4om5p239.default/extensions/twitternotifier@naan.net/defaults/preferences/twitternotifier.js
/home/pjq/.mozilla/firefox/4om5p239.default/extensions/twitternotifier@naan.net/components/nsTwitterFox.js
/home/pjq/.mozilla/firefox/4om5p239.default/extensions/twitternotifier@naan.net/components/nsTwitterFoxHttpRequest.js
/home/pjq/.mozilla/firefox/4om5p239.default/extensions/twitternotifier@naan.net/components/nsTwitterFoxDatabase.js

```

编辑它，大概在38行的样子：
```

vim ~/.mozilla/firefox/4om5p239.default/extensions/twitternotifier@naan.net/components/nsTwitterFox.js

```

```

//var TWITTER_API_URL = "https://twitter.com/";
var TWITTER_API_URL = "http://www.impjq.net/t/";

```

它原来链接用的是https,所以怪不得当时twitter被封时，通过https还能访问时，twitterfox
也能够登录，原来它就是用的https

![](http://img.zemanta.com/pixy.gif?x-id=439ee768-ef84-8f6c-bda6-4ebb0622eab4)