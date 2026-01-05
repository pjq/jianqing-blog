---
title: "Fix syno storage management"
date: 2024-05-01
author: pengjianqing
categories: ['Tech']
tags: ['syno', 'synostoraged']
---

## Problem

In the syno storage management, it can't show the disk information. 

## Check the "invalid ELF" log

So first check the "invalid ELF" log in the "/var/log"

```
`root@DiskStation:/var/log# grep -R "invalid ELF" * 

grep -R "2024-05-01.*invalid ELF" *`
```

```
`messages:2024-05-01T22:48:55+08:00 DiskStation synoscgi_SYNO.Core.System_1_info[24603]: APIRunner.cpp:758 cannot open library: lib/SYNO.Core.System.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:48:59+08:00 DiskStation synoscgi_SYNO.Core.System_1_info[24624]: APIRunner.cpp:758 cannot open library: lib/SYNO.Core.System.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:11+08:00 DiskStation synoscgi_SYNO.Entry.Request_1_request[25071]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:11+08:00 DiskStation synoscgi_SYNO.Core.Storage.Volume_1_list[25071]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:20+08:00 DiskStation synoscgi_SYNO.Entry.Request_1_request[25177]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:20+08:00 DiskStation synoscgi_SYNO.Core.Storage.Volume_1_list[25177]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:24+08:00 DiskStation synoscgi_SYNO.Entry.Request_1_request[25179]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header
messages:2024-05-01T22:49:24+08:00 DiskStation synoscgi_SYNO.Core.Storage.Volume_1_list[25179]: APIRunner.cpp:758 cannot open library: lib/libStorage.so. error = /lib/libsynostoragemgmt.so: invalid ELF header`
```

## Replace the libsynostoragemgmt.so

The replace the so file(You need to download the correct syno system before replace the so files.)

- https://www.synology.cn/zh-cn/support/download/DS3617xs?version=6.1#system

- And decompress the pat file, and the so file in 

- DSM_DS3617xs_15284/hda1/lib/libsynoshare.so.6 

- DSM_DS3617xs_15284/hda1/lib/libsynopkg.so

- DSM_DS3617xs_15284/hda1/lib/libstoragemanager.so

```
`cd /volumeUSB2/usbshare/syno
ls -alht

total 1.3G
drwxr-xr-x  4 root root 4.0K May  1 23:09 .
drwxrwxrwx 11 root root 4.0K Dec 17 22:50 ..
drwxr-xr-x 36 root root  36K Dec  6  2022 diskstation_backup_lib
-rw-r--r--  1 root root  76K Dec  6  2022 DSM_DS3617xs_15284.zip
drwxrwxrwx  3 root root 4.0K Dec  6  2022 4.24_DS3617-6.17up3
-rw-r--r--  1 root root 1.2G Dec 13  2019 4.24_DS3617-6.17up3.zip
-rw-r--r--  1 root root 111K May 19  2018 libstoragemanager.so
-rw-r--r--  1 root root 579K May 19  2018 libsynostoragemgmt.so
-rw-r--r--  1 root root 1.1M May 19  2018 libsynopkg.so.1
-rw-r--r--  1 root root 242K May 19  2018 libsynoshare.so.6

cp libsynostoragemgmt.so /lib`
```

```
`cd  /volumeUSB2/usbshare/syno && cp libsynoshare.so.6 /lib && cp libsynopkg.so.1 /lib && cp libstoragemanager.so /lib` && cp libsynostoragemgmt.so /lib
```

## Restart the synostoraged service

```
`synoservice -enable synostoraged`
```

If not work, then may need to restart the DSM service

```
`synopkg start synoscgi 
synoservice -enable DSM 
synoservice -status DSM Service 
synoservice -enable synostoraged`
```

## Reference

- https://xpenology.com/forum/topic/12406-how-to-fix-sorry-that-page-doesnt-exist/

- https://www.cnblogs.com/LandWind/p/13675986.html

- http://c4c.club/index.php/2020/08/03/%E7%BE%A4%E6%99%96%E6%89%BE%E4%B8%8D%E5%88%B0%E9%A1%B5%E9%9D%A2%E5%8F%8A%E5%82%A8%E5%AD%98%E7%A9%BA%E9%97%B4%E7%AE%A1%E7%90%86%E5%A4%B1%E6%95%88%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/