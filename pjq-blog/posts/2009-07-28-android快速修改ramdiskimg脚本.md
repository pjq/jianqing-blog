---
title: "Android:快速修改ramdisk.img脚本"
date: 2009-07-28
author: pengjianqing
categories: ['Android', 'shell']
tags: ['Android', 'Ramdisk.img']
---

有时候要修改Android的ramdisk.img,如果每次都将那些命令都敲一遍，那确实有点烦，那有没有快速简单的方法呢？有，就是将这些命令放在一起，创建了一个简单的脚本：
这个脚本很简单，直接将脚本放到放有ramdisk.img的目录下，运行就行了，
运行时，输入1,会将ramdisk.img解压出来，输入2会将修改后的ramdisk重新打包成ramdisk.img。
```

root@o-2rl2:/home/percy# cat shell/ramdisk
#!/bin/bash

echo "Modify the ramdisk.img"

echo "1.Inflate the image"
echo "2.Create the image"

read -p "Choose:" CHOOSE

#case ${CHOOSE} in
#1)inflate();;
#2)create() ;;
#esac

if [ "1" = ${CHOOSE} ];then
	echo "inflate()"
	cp ramdisk.img ramdisk.cpio.gz
	gzip -d ramdisk.cpio.gz
	[ -e "tmp" ] ||{ echo "mkdir tmp"; mkdir tmp;}
	cp ramdisk.cpio tmp/
	cd tmp
	cpio -i -F ramdisk.cpio
elif [ "2" = ${CHOOSE} ];then
	echo "create()"
	[ -e "tmp" ] && { cd tmp;cpio -i -t -F ../ramdisk.cpio | cpio -o -H newc -O ../ramdisk_new.cpio;echo "Create ramdisk_new.cpio finished ";}

fi

```

顺便说一下，将博客名改成以前一直用的[那个](http://percy.blog.ubuntu.org.cn)了，毕竟用了一段时间了。
电脑背景改成淡绿色代码：RGB：204,232,207

 
alimama_pid="mm_13663287_1930864_8012022"; 
alimama_titlecolor="0000FF"; 
alimama_descolor ="000000"; 
alimama_bgcolor="FFFFFF"; 
alimama_bordercolor="E6E6E6"; 
alimama_linkcolor="008000"; 
alimama_bottomcolor="FFFFFF"; 
alimama_anglesize="0"; 
alimama_bgpic="0"; 
alimama_icon="0"; 
alimama_sizecode="12"; 
alimama_width=468; 
alimama_height=60; 
alimama_type=2; 
 
 

![](http://img.zemanta.com/pixy.gif?x-id=e8315d5b-4237-80e8-81e7-95b55eab5445)