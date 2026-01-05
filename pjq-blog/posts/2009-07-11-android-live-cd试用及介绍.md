---
title: "Android live cd试用及介绍"
date: 2009-07-11
author: pengjianqing
categories: ['Android']
tags: ['Android', 'livecd', 'Virtualbox']
---

无意中看到了有人创建了Android live cd镜像文件，能够和linux桌面系统一样，通过镜像文件引导进系统，运行在X86架构的系统之上，看起来真的很不错。心里自然就有了想一探究竟的冲动。
项目主页在这里：http://code.google.com/p/live-android/
据其介绍可以在VirtualBox和Vmware上运行，自然我的首选是VirtualBox,由于前一段时间将VirtualBox删掉了，所以还得重装。装VirtualBox过程中遇到了一些问题，试了好几个版本终于发现XXbin-2.2.2可以用了。
      很想知道是否能够在普通的PC上运行，但估计现在是比较困难的。目前好像只能在下列电脑中运行：
EeePC 701 , EeePC 701SD, EeePC 900, EeePC 900A, EeePC 901, EeePC 904HD, EeePC 1000, EeePC 1000HD 见：http://code.google.com/p/patch-hosting-for-android-x86-support/

废话少说，说下过程：
1.下载
在这个地方说得很清楚：http://live-android.googlecode.com/files/readmefirst.txt
下载那两个ISO文件：
wget http://live-android.googlecode.com/files/liveandroidv0.2.iso.001
wget http://live-android.googlecode.com/files/liveandroidv0.2.iso.002
然后把它们组装：
cat liveandroidv0.2.iso.001 liveandroidv0.2.iso.002 >liveandroidv0.2.iso
再验证MD5:
md5sum liveandroidv0.2.iso
03852bce8cb26aba21d147153c1fb120  liveandroidv0.2.iso
正确！！

2.然后用VirtualBox将它跑起来了，具体方法就不说了，用过VirtualBox应该都很清楚的：
下面是一些运行时的截图：
在VirtualBox新建一个，设置光驱挂载上面那个镜像文件：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/Sldp4QCD5jI/AAAAAAAAAWE/S3Bd0i3Iy1g/s400/2009-07-10-232120_930x535_scrot.png)](http://picasaweb.google.com/lh/photo/GKXpzT0oTqwp2gXMNDnbjQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

启动虚拟机：
很快一闪，然后打印出了一些启动信息，完全和linux一样：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/Sldp4pJfejI/AAAAAAAAAWI/-hs7FvdHYeI/s400/2009-07-11-000742_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/EQqLqeitQzLNLh8Rj3jFhA?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

然后迅速跳到这个地方，这个应该是一个splash了：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/Sldp4wQNChI/AAAAAAAAAWM/0hSUoYeuCKU/s400/2009-07-11-000745_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/RJltsQOZ2HlnHhKLVFQSJQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

然后跳到漫长的等待界面，和它那个emulator上一样：
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/Sldp4wd_syI/AAAAAAAAAWQ/9f1-tu1Ldgs/s400/2009-07-11-000750_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/IJs4BxA0dXwyoitxl03iEQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

继续等待：
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/Sldp44HnXAI/AAAAAAAAAWU/uJ4cxWy7pxA/s400/2009-07-11-000802_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/LytTau6FTr8DtX7iSgr0iQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

启动基本完成，这个时候会跳出一个关于电量不足的Warning,忽略之：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/SldqT9_B_HI/AAAAAAAAAWY/-L5CtKOBt9A/s400/2009-07-11-000818_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/6NW_8y_L-xS8w5Pgmbrpag?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

这时候界面上应该会有一个鼠标提示的一个东西，移动鼠标选中OK之后，进入主界面：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/SldqUCksN-I/AAAAAAAAAWc/SAVD7zPBRhg/s400/2009-07-11-000830_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/UORyfw8seVGXgW_a-WXwPw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

进入Browser,效果很不错，右ALT和右CTRL中间那个键，好像是打印键，可以调出menu菜单：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/SldqUEJZohI/AAAAAAAAAWg/yMVeav-g5iY/s400/2009-07-11-000853_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/BranxCGIbaC6pf9kOoVCPg?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

用键盘输入我的blog:
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/SldqUPJg9zI/AAAAAAAAAWk/rGGKvWFoMxk/s400/2009-07-11-001005_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/Lzq7EoN89tgjYF7TIb-CNw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

看一下效果是不是相当不错：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/SldqUW7MiuI/AAAAAAAAAWo/AxDZLxXPVGM/s400/2009-07-11-001018_808x677_scrot.png)](http://picasaweb.google.com/lh/photo/mjlMPBdUXfQjOBAtCr4zdw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

鼠标按住左键不放，可以上下左右拖拉，并且会出现一个放大和缩小的提示：

[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/Sldqg2jaivI/AAAAAAAAAXE/3SX_VZ3Phys/s400/2009-07-11-001039_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/aY_z_EI6-5eZ4wMgnAJCFQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

放大效果：
[![](http://lh4.ggpht.com/_GxH7-x2-l3Y/SldqhqbORcI/AAAAAAAAAXI/elBsBzc0DQE/s400/2009-07-11-001125_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/kGiVAI59tlkXKE4waI3qHw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

退出Browser，进入MainMenu，或者按那个在windows下用来打开开始菜单的键:
[![](http://lh3.ggpht.com/_GxH7-x2-l3Y/SldqilRhXSI/AAAAAAAAAXM/emGicnE64zE/s400/2009-07-11-001140_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/ed9zluKOoOQ2t-ZCX3mhHQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

接下来我偿试了安装软件，按alt+F1，可以进入终端，和linux下很像：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/SldqkEBdDFI/AAAAAAAAAXQ/TeG_HnFpraU/s400/2009-07-11-001150_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/Ye7MK8T1Uj3pMa-1s8HxFg?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

按照它的介绍，它里面预装了busybox，那应该就会有很多可用的命令了，试了一下wget还真有，看来将软件装上是很有希望的：我们知道自己安装的软件（APK文件）都在/data/app下面，如果能够将apk文件弄到这个目录下，那就表示能够装上软件了，我试了一下，还真的成功了，见下图，我是通过wget将文件下载到/data/app目录下：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/SldqlXyADhI/AAAAAAAAAXU/zUtIzdiNrgk/s400/2009-07-11-001228_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/DCv_PnCUgWIG2DZjvHdfjw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

然后再来验证是否安装成功：
按alt+f8可以回到图形界面，奇怪的是，在终端下面输入的命令好像在图形界面都能够接收到。
进入到主菜单：
[![](http://lh3.ggpht.com/_GxH7-x2-l3Y/SldqmiKZMcI/AAAAAAAAAXY/NZYRjp4DII4/s400/2009-07-11-001251_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/nXDEdSaJ1S_QlTiaSZzjRA?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

看到了我刚才安装的程序：
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/SldqnVtFPjI/AAAAAAAAAXc/RgwusmI7Ma8/s400/2009-07-11-001301_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/wvF3D3KcyDzEFY-UtX72gg?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

运行之，效果还行，就是layout有点变形错位了，但我感觉已经非常不错了，看来我写的这个程序在layout上还存在很大的问题，有空研究下如何适应不同的屏幕界面大小：
[![](http://lh3.ggpht.com/_GxH7-x2-l3Y/SldqoEGzoiI/AAAAAAAAAXk/IeCWuBJEsBs/s400/2009-07-11-001320_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/bWdt6pX4GPFJMW8aX6X1DA?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

按那个“打印键”，打开menu,进入Setting，设置好两个城市:
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/Sldqoy5_pzI/AAAAAAAAAXo/0lvgEb9_oDc/s400/2009-07-11-001324_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/VHmkdrg_AeB_yJknCdAtTw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

设置完毕返回：
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/Sldqp7tXnTI/AAAAAAAAAXs/XjN7tP9Rj8U/s400/2009-07-11-001402_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/s6nnafHMWsyVH8HhA0lhcw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

感觉怪怪的，奇怪的界面：
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/Sldqq9S3_gI/AAAAAAAAAXw/7_ex_ajoe0M/s400/2009-07-11-001407_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/F_OjbuxH91wEC57ckwUFBQ?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

按左上角那个Button,show 下3D旋转，旋转时中心轴出现问题了，不是在最中心位置，当时写程序的时候，是写死了那个中心轴，而不是根据实际情况得到的，看来这个地方也要改改了。
[![](http://lh6.ggpht.com/_GxH7-x2-l3Y/SldqrtNA2mI/AAAAAAAAAX0/I2nIlr7DblE/s400/2009-07-11-001416_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/FrfNQcbnMuaqQP51P2LFtw?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

旋转到和屏幕垂直了：
[![](http://lh5.ggpht.com/_GxH7-x2-l3Y/SldqsPKxyLI/AAAAAAAAAX4/LRLyDIBrSN4/s400/2009-07-11-001428_808x677_scrot.jpg)](http://picasaweb.google.com/lh/photo/16tezZyuRJVn1Om3HZEiBA?feat=embedwebsite)发件人 [Androidlivecd](http://picasaweb.google.com/pengjianqing/Androidlivecd?feat=embedwebsite)

Over.
试用完后感觉还不错，一个手机上的系统能够变得如此强大，这些应该都可以归结于其底层是构建在linux的基础上。
现在暂时还没用弄到PC上去试试，应该只要用这个iso文件刻一张系统盘就行了，也可以用liveUSB的方式引导，可惜我的U盘忘在办公室了，Orz...但想想成功率应该会比较低的，毕竟它现在只是移自Eee pc,很多设备驱动都应该不太好。
希望这个有趣的项目能够继续走下去，持续关注中。