---
title: "编译Android源码For HTC G1（HTC Dream）"
date: 2009-12-24
author: pengjianqing
categories: ['Android']
---

[编译Android源码For HTC G1（HTC Dream）](http://docs.google.com/View?id=dg9p7dc4_64grfwx5cx)

1.参考Google:
http://source.android.com/documentation/building-for-dream
其中解压文件一步，好像现在目录已经改变了，需要将文件放到源码根目录，而不是vendor/htc/dream-open/
signed-dream_devphone_userdebug-ota-14721.zip

2.可以偿试编译cyanogen,基本步骤和Google的差不多
具体参考：http://github.com/cyanogen/android

（1）需要在源码根目录下创建文件：
pjq@gentoo-pjq ~/android/cyanogen $ cat buildspec.mk
TARGET_PRODUCT:=cyanogen_dream_us
TARGET_BUILD_VARIANT:=eng
TARGET_BUILD_TYPE:=release
(2) lunch cyanogen_dream_us-eng
(3)make -j2 (参数根据CPU个数定，一般是CPU个数+1)

3.如果编译正确，就会生成相关room了,之后就是将新生成的image刷到手机上了
(1)如果会用fastboot，就可以直接刷room了。
fastboot  flash boot boot.img
fastboot  flash system system.img
fastboot  flash userdata userdata.img

(2)就是打包成升级压缩包，到recover模式下，进行更新，我现在采用也是这种方法。
打包完成后需要进行签名，签名方法：http://docs.google.com/View?id=dg9p7dc4_58hsbwwbm4

打包注意：
打包其实很简单，要注意的是那个升级脚本：META-INF/com/google/android/update-script
这个脚本决定了，你会进行哪些操作。这个脚本我们没必要自己写，只要参照某一个升级包的就可以了。
（1）解压一个现成的升级包（用得cm的升级包），得到文件：
pjq@gentoo-pjq ~/Desktop/dream_image $ ls update-cm-4.2.9.1 -l
total 79340
-rw-r--r--  1 pjq users     6877 2009-12-12 21:04 backuptool.sh
-rw-r--r--  1 pjq users  2129920 2009-12-17 21:58 boot.img
drwxr-xr-x  3 pjq users     4096 2009-12-23 21:58 data
drwxr-xr-x  3 pjq users     4096 2009-12-23 21:58 META-INF
drwxr-xr-x 13 pjq users     4096 2009-12-23 21:58 system

（2）其中的boot.img data system就直接从新build的拷贝过来覆盖掉（分别对应到：out/target/product/dream-open/目录下的同名文件）

（3）ls out/target/product/dream-open/system/bin/ -l 用这个命令查看下文件，如果有很多链接格式文件话，那就需要去修改META-INF/com/google/android/update-script 将其中有关symlink的全部删掉，要不然会在升级的时候提示你无法创建 symlink文件（因为它们已经是链接文件了）。
如果不想修改升级脚本，可以从原来的升级包（update-cm-4.2.9.1）中将system/bin/文件拷贝过来覆盖掉（原来升级包中不是链接文件，可以通过ls update-cm-4.2.9.1/system/bin -l查看）。

（4）将相关文件覆盖后，正确处理了升级脚本的问题，接下去就可以进行打包了：
pjq@gentoo-pjq ~/Desktop/dream_image/update-cm-4.2.9.1 $ zip -r update-new.zip backuptool.sh META-INF/ boot.img data/ system/
这里要注意一定要在这些文件的同级目录进行打包，也就是和system data文件在同一目录，并记得将所有文件都打包进去。

（5）打包结束后，就生成了新的升级文件update-new.zip，但这个文件还不能直接用来升级，需要对它进行签名，签名方法参考：http://docs.google.com/View?id=dg9p7dc4_58hsbwwbm4

如果上述5步都正确，就可以用新的升级包进行升级了。
如果升级过程中提示某些文件不存在的时候，这时就要检查升级脚本了META-INF/com/google/android/update-script，检查里面操作的文件都是存在的。
改好后，再重新打包，签名，升级。

附：
1各機種進入 Recovery 模式及 Fastboot 模式的方法
http://windows7.cool3c.com/article/12221

2.Linux 下连adb的方法

http://forum.xda-developers.com/showthread.php?t=537508
我目前的情况：
gentoo-pjq update-cm-4.2.9.1 # lsusb
Bus 002 Device 002: ID 09da:000a A4 Tech Co., Ltd Port Mouse
Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
Bus 001 Device 008: ID 0bb4:0c02 High Tech Computer Corp.
Bus 001 Device 002: ID 0951:1613 Kingston Technology
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
其中“Bus 001 Device 008: ID 0bb4:0c02 High Tech Computer Corp. ”就是我的G1了
“0bb4”就代表HTC了。
在udev中添加相关rules:
gentoo-pjq update-cm-4.2.9.1 # cat /etc/udev/rules.d/99-android.rules
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0bb4", ATTRS{idProduct}=="0c02", MODE="0666", OWNER="pjq"

再重启udev:
gentoo-pjq update-cm-4.2.9.1 # /etc/init.d/udev restart

3.重新挂载system分区，变为可读写：
mount -o rw,remount -t yaffs2 /dev/block/mtdblock3 /system
这个很管用，有时需要修改一些配置文件，会提示read only,重新挂载后就可以用vi直接修改了.

4.通过无线网卡Adhoc 上网
http://www.gphone-cn.com/bbs/thread-12802-1-1.html
http://modmygphone.com/forums/archive/index.php/t-22681.html

5.SPL相关

http://www.hiapk.com/bbs/thread-3387-1-1.html

http://code.google.com/p/android-roms/wiki/SPL

6.如果需要打开swap分区，可以在系统启动的时候加入下面这行命令，需要根据实际情况修改swap分区目录。

 [ -e /dev/block/mmcblk0p3 ]&&{ echo "swapon /dev/block/mmcblk0p3"; swapon /dev/block/mmcblk0p3; }

由于我用了app2sd,所以我将这句加入到system/etc/init.d/04apps2sd

在adb shell下cd 到/system/etc/init.d

# head 04*
#!/system/bin/sh
#
# Enable Apps2SD

 [ -e /dev/block/mmcblk0p3 ]&&{ echo "swapon /dev/block/mmcblk0p3"; swapon /dev/block/mmcblk0p3; }
if [ -e /dev/block/mmcblk0p2 ];
then
    echo "--- Checking filesystems";

    # fsck the sdcard filesystem first

![](http://img.zemanta.com/pixy.gif?x-id=d4c5d622-751d-8e60-8e2d-883fc1534d00)