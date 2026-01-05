---
title: "修复本机mysql,wordpress,phpBB"
date: 2010-11-27
author: pengjianqing
categories: ['自由分类']
---

之前由于系统坏掉了，用了以前备份的stage4恢复了一下系统，遗留下来一些问题。
1.mysql启动不了
经过多方搜索后来发现是权限问题，由于恢复的东西很多都权限变成了root.root，幸好在恢复系统前将原有目录都做过备份，直接把有权限问题目录再覆盖一下，
其中mysql的目录是：/var/lib/mysql/
恢复之后restart mysql,done.
2.wordpress不能访问
这个问题确实很难搞，这个还徒涉到apache的VirtualHost配置，
之前在配置apache的时候，直接把Listen 192.168.1.4:80设成本機IP了，现在换了一个地方IP地址也都换了，所以需要更新这个配置：

vim /etc/apache2/vhosts.d/00_default_vhost.conf
直接换成本地IP：127.0.0.1:80。
这样设置之后，虽然可以访问到本地服务器，但wordpress对应的地址/blog还是不无法打开。
想起以前在安装wordpress的时候有一个配置site url，当时设置的是http://gentoo-pjq.vicp.net/blog/ 很明显这个地上已经过期了，但我又无法登录wordpress后台进行管理。
很快我就想到了通过修改wordpress的数据库来修改这个值。本想直接通过mysql来修改，但可惜对mysql的命令行操作不是太懂，于是就想找一个图形界面的工具，接着就找到了phpmyadmin,查了下，本机已经安装了，
通过本机访问http://127.0.0.1/phpmyadmin/,但死活就是登录不了，也偿试过修改phpmyadmin的配置文件 ，但就是不管用。
我想是不是需要修改一下mysql的密码,于是用root登录mysql,修改了mysql的权限：
 mysqladmin -u root password "yournewpassword" -p
很神奇，这个时候我再登录phpmyadmin，居然就行了，囧。
找到wordpress数据库，查找gentoo-pjq.vicp.net，很顺利的找到了，修改成本地地址http://127.0.0.1/blog,
再访问，OK了。

3.phpBB
还有一个本地phpBB论坛无法访问。
我偿试过重新emerge，用原来的文件覆盖，都不管用.
没办法，只好全新安装一下phpBB,跟着向导一路设置，之间需要用phpmyadmin新建一个database.
弄好之后可以用phpmyadmin导入到以前备份好的phpbb数据库（备份命令是mysqldump phpbb >phpbb_20101127.sql -p）或者修改config.php,把里面的数据库名字再换回来。
要在正式访问之前还要把目录下的install给移走，否则很多东西还是无法访问。
但奇怪的是，这时我再访问http://127.0.0.1/bbs,还是无法打开网页，提示什么压缩格式无法支持，需要修改GZip compress,还好这个时候可以访问控制台，找到gzip的配置，把它给取消掉，再访问，成功了！！

4.另外还有一些问题
(1) 页面上方总是提示什么 TImezone有问题，需要修改php.ini
vim /etc/php/apache2-php5/php.ini
添加TImezone:
date.timezone =Asia/Shanghai
(2) 还有之前所有与php有关的页面都无法打开，甚至是写的phpinfo都无法打开，还有以前用过的php探针也不能用，问题提示什么$end有问题，这个也需要修改php.ini,打开一个tag兼容选项：
short_open_tag = On

至此，完成了以上问题的修复，wordpress,phpBB又可以正常跑起来了,记录一下，以便以后查找

![](http://img.zemanta.com/pixy.gif?x-id=1221f87e-5f20-8aaf-bfa1-76dcf0a70151)