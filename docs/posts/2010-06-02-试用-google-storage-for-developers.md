---
title: "试用 Google Storage for Developers"
date: 2010-06-02
author: pengjianqing
categories: ['Tech']
tags: ['Google', 'Google Storage', 'gs', 'gsutil']
---

**试用 Google Storage for Developers**

关于Google Storage详细信息请参考这里：
http://code.google.com/apis/storage/docs/getting-started.html
http://code.google.com/apis/storage/

由于目前还只是试用版，需要在这里去登记排队：
http://gs-signup-redirect.appspot.com/
如果收到 Google的invite link邮件，恭喜你可以点击它给的链接开通这个服务了。

并且这个链接不能转让，这是原文：
Please note that this invitation is not transferable.
During the preview period, you will receive up to 100GB of data storage and 300GB monthly bandwidth at no charge. To learn more, please visit our website: http://code.google.com/apis/storage. We would love to hear you feedback at gs-discussion@googlegroups.com

Google 很大方，在"preview period"阶段，就给了100G空间，每月300G流量，个人用用应该是足够的了。

闲话少说，看看怎么用它吧。

如果需要查看GS的介绍，请点这里：http://code.google.com/apis/storage/docs /getting-started.html

 Google提供了一个用来资源管理的工具，叫Gsutil。
使用可能参考 http://code.google.com/apis/storage/docs/gsutil.html
这个工具是用python写的，所以可以跨平台，Linux当然是原生支持了，Windows需要安装python,还有cygwin才可以，但今天在办公室试了下，没成功。
所以在Linux下使用python才是王道。
1.下载安装
axel http://commondatastorage.googleapis.com/pub/gsutil.tar.gz
tar xvf gsutil.tar.gz -C   ~/
2.设置PATH
vim ~/.bashrc
新增一行，修改PATH路径：
export PATH=${PATH}:/home/pjq/gsutil
3.更新一下环境变量
source ~/.bashrc

至此已经完成了gsutil的安装。
用which gsutil查一下，如果存在这个命令就表示安装成功了。

然后是第一次运行 gsutil,按照提示，输入Access Key和Secret.
Key可以在这个地方找到：
https://sandbox.google.com/storage/m/manage

现在是万事俱备，只欠东风了。
1.如何创建一个Buckets呢？
Buckets有点像我们平时所说的文件夹，可以从那篇Getting Started里找到详细的说明。
先让我们来创建一个叫hellogs的Buckets:
gsutil mb gs://hellogs

2. 如何上传文件到Buckets:
让我来把刚才下载的gsutil.tar.gz上传到hellogs:
gsutil cp gsutil.tar.gz gs://hellogs

3.如何查看Buckets中的文件信息
可以用gsutil ls 或gsutil ls -l
pjq@gentoo-pjq ~ $ gsutil ls
gs://hellogs
 pjq@gentoo-pjq ~ $ gsutil ls -l
gs://hellogs:
    ACL:
        00b4903a97c79e48805bb4c8d48e7db8329f12ae7067a50ef13d0c6d2e77****: FULL_CONTROL
pjq@gentoo-pjq ~ $ gsutil ls -l gs://hellogs
gs://hellogs:
    ACL:
        00b4903a97c79e48805bb4c8d48e7db8329f12ae7067a50ef13d0c6d2e77****: FULL_CONTROL
看起来一切都比较简单。

4.如何下载上传的文件呢
也是用cp命令，只不过和上传时的两个参数调换了一下
gsutil cp gs://hellogs/gsutil.tar.gz gsutil.tar.gz2

5.如何删除呢
删除一个Buckets:
gsutil rb gs://hellogs
删除一个文件
gsutil rm gs://hellogs

6.当然也可以移动文件：
gsutil mv gs://dogs/*.jpg gs://cats/
文件重命名：
gsutil mv gs://cats/poodle.jpg gs://cats/siamese.jpg
看起来和我们一般用到的mv命令没什么两样，只不过参数要换成Google Storage定义的形式。

7.如何进行权限控制
权限控制，俗称ACLs.Google为我们提供了比较全面的权限控制机制，具体可以参考：
http://code.google.com/apis/storage/docs/developer-guide.html#authorization

使用命令setacl:
gsutil setacl bucket-owner-full-control gs://hellogs/gsutil.tar.gz

另外如果要管理资源文件，可以不用这个命令行的方式，可以直接通过浏览器使用Google Storage Manager：https://sandbox.google.com/storage
登录这个管理后台，可以看到我刚才上传的文件，还有一个share link:http://commondatastorage.googleapis.com/hellogs/gsutil.tar.gz
通过这个链接就可以下载了。

总得说来，还是比较简单的，有了这个我们就可以更加方便的共享大文件了，不用再四处找上传空间了。还有Google的提供的空间足够大100G,一般日常用用肯定是足够的。如果不够大，还可以另外再申请一个帐号，当然如果是用来上传某些XX比较大的文件，那就另说了。

目前我还没试过上传比较大的文件，比如一个电影，如果中途出错了，再上传的话，是否会接着上次的位置继续上传，而不用重新上传。另外也没看到上传时有什么进度的提示信息。

貌似目前关注的人还不是很多，在gsutil的google group有我发的第一贴：
https://groups.google.com/group/gsutil-discuss
欢迎围观。

.