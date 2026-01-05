---
title: "Time Machine备份"
date: 2022-07-14
author: pengjianqing
categories: ['Tech']
---

知道苹果有这个东西，但一直没用过。最近要换新电脑，想到了Time Machine，想着应该能够无缝迁移吧。

在NAS上开了一个共享空间，打开了afp设置，同一个网络下，自动就搜到了，然后就开始了漫长的备份过程。，

发现了一些问题，体验并不那么好

- 第一是慢，是真的慢，备份了好几次都没有一次成功
- 因为上班有时要连VPN，有时要切有线/无线，断了之后，又重新开始计算，体验太糟糕
- 一次到了98%, 时间显示7分钟，但是等了好长时间还是显示7分钟，时间估算太差
- 每次断了，重新计算都需要等很的时间，进度也是莫名其妙
- 空间已经占了1T+，但依旧还没有备份完成

网上搜到几个密令

```
` 1. sudo sysctl debug.lowpri_throttle_enabled=0
 2. sudo fs_usage backupd`
```

[1]说是可以解除CPU/IO限制，可以全速备份

[2]可以看到当前的备份状态

如果需要恢复限制，只需要把0->1

```
` sudo sysctl debug.lowpri_throttle_enabled=1
`
```

早点没有看到这个命令，要不可以省很多时间吧。

当然除了用Time Machine备份，我也使用了传统的备份方式

- 1. 单独压缩需要备份的目录
- 2. NFS/SMB挂载远程目录
- 3. cp file.zip /remote/path

实际使用发现

- 启用压缩能够节省很多时间，可能是小文件比较多，压缩需要一点时间，但cp速度可以快太多，比直接cp快很多
- 使用Mac Find 通过ctrl+c, ctrl+v的方式，完全比不过直接用cp命令