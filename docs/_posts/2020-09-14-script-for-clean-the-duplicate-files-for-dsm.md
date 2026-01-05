---
title: "Script for clean the duplicate files for DSM"
date: 2020-09-14
author: pengjianqing
categories: ['Tech']
tags: ['Bash', 'DS', 'Script', 'Storage']
---

2020年已经过去大半了，更新一下博客，刷一下存在感。

去年收了一个暴风影音播客云二期，安装了破解版的黑群晖。每三个月更新一次Let's Encrypt证书。

但它的Android客户端很奇怪，每次更新证书之后就无法再登录了，需要把App缓存清掉，重新登录，导致的后果就是需要重新设置备份文件目录。然后就每次重新开始备份手机上的视频照片，关键不是增量的，需要全部重新备份。

ssh进入系统后就可以看到重复的文件，文件名加了后缀_1, 例如 VID_20200913_170932_1.mp4, 文件太多超过2W个, 不能手动去删除，于是顺手就写了一个脚本去自动删除。

原理很简单，先找到那些不含_1后缀的文件，然后查看是否存在_1后缀的文件，文件存在的话就直接删掉，310G变到202G了，清理了100G+的空间。

```
`#!/bin/sh
count=0
remove=0
for file in `ls|grep -v "_1\." `
do
	((count++))
	#echo -n "${count} "
	name=`echo ${file}|cut -d "." -f1`
	ext=`echo ${file}|cut -d "." -f2`
	dup_file=${name}_1.${ext}
	echo -n  "total:${count}, remove:${remove}"
	if [ -f ${dup_file} ]; then
		#echo ${dup_file}
		((remove++))
		echo " rm ${dup_file}"
		rm ${dup_file}
	else
		echo ""
	fi
done

#echo "total:${count}, remove:${remove}"`
```

运行效果如下

```
`total:12308, remove:11144 rm VID_20200724_211814_1.mp4
total:12309, remove:11145 rm VID_20200724_212118_1.mp4
total:12310, remove:11146 rm VID_20200724_212337_1.mp4
total:12311, remove:11147 rm VID_20200724_212405_1.mp4
total:12312, remove:11148 rm VID_20200725_171104_1.mp4
total:12313, remove:11149 rm VID_20200725_172253_1.mp4
total:12314, remove:11150 rm VID_20200725_174056_1.mp4
total:12315, remove:11151 rm VID_20200725_175208_1.mp4
total:12316, remove:11152 rm VID_20200729_200525_1.mp4
total:12317, remove:11153 rm VID_20200731_221342_1.mp4
total:12318, remove:11154 rm VID_20200731_221555_1.mp4`
```