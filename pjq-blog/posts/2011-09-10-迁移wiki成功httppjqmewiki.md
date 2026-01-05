---
title: "迁移wiki成功:http://pjq.me/wiki/"
date: 2011-09-10
author: pengjianqing
categories: ['Tech']
---

迁移wiki成功:http://pjq.me/wiki/
简单记录一下:
1.先用FTP把doku wiki数据下下来
2.用FTP把doku wiki上传到空间/wiki
3.修改hosts records:
试过可以用URL Frame,URL Redirect(301)方式定向到空间http://pjq.me/wiki
URL Frame可以直接访问二级域名:http://wiki.pjq.me
URL Redirect(301)会直接重定向到http://pjq.me/wiki/
最后选择了URL Redirect(301)方式
另外 ttp://wiki.impjq.net 也重定向到了新的wiki路径
目前wiki总共大小是59M，这个100M的空间放了wordpress+dokuwiki暂时跑跑问题不大，空间不够的话再升级吧.

欢迎访问我的wiki:
http://pjq.me/wiki/ 
另外下面几个链接也都可以:
http://w.pjq.me/
http://wiki.pjq.me/
http://wiki.impjq.net