---
title: "Can't access NAS via public internet"
date: 2022-12-06
author: pengjianqing
categories: ['Tech']
tags: ['ChinaNet', 'DHCP', 'NAS']
---

One week ago, I found I can't access my NAS, even the wifi APP can't find the NAS in the device list, and it's very strange.

Also I found if my Phone connecting with ChinaNet Gateway Router, the ip address will be 

192.168.72.xx

So I guess some config changed in the Router, now I can just guess I have set the static IP address in the NAS admin center

```
`192.168.1.14`
```

And I need to use another router to set the network IP address range as 

192.168.1.1/24

Then I can access the NAS Admin center, and it's works.

So I can the IP address as DHCP auto mode, and connect NAS with ChinaNet Router, then it get the correct IP, and works

```
`192.168.72.10`
```

So the last thing is to find out what's happening, after Google, I found other guys also have the same problem, the solution is call the ChinaNet Network Admin.

After the Admin did some config change in their Admin Center, the Router IP address has changed to original range

192.168.1.1/24

And the public IP address also works as a magic.