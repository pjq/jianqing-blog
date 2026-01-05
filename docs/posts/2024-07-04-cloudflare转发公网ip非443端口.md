---
title: "Cloudflare转发公网IP非443端口"
date: 2024-07-04
author: pengjianqing
categories: ['Tech']
tags: ['Cloudflare', 'DNS', '公网']
---

上海电信公网IP开通后，一些常用的端口如80和443不能使用。因此，必须使用其他端口，例如将443端口改为8443端口。访问时还需要在URL中加入特定的端口号：https://host:8443。

昨天搜了一下，原来Cloudflare支持转发非443端口，你需要做的就两步

- DNS enable proxy

- Rules->Origin Rules->Custom Filter Expression, 在这里添加一些转换规则-> Then rewrite to "8443"

这样就设置好了，通过访问https://host， Cloudflare就会自动转到了源地址https://host:8443

![](../images/29d4b306.png)