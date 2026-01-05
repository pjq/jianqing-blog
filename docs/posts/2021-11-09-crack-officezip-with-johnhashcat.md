---
title: "Crack Office/zip with John/hashcat"
date: 2021-11-09
author: pengjianqing
categories: ['Uncategorized']
---

It's very easy to crack the password with john/hashcat

`zip2john music.zip >music.hash
john music.hash
john --show music.hash`

Let's see how many command john support

```
`which john
ls /usr/sbin/*|grep john
locate office2john`
```

![](../images/7515d459.png)

## Examples

hashcat -a 3 -m 9600 hash.txt -1 "?l?d" "?1?1korea"   --show
hashcat -a 3 -m 0 34d8d24499f2d3d4fa9c42a5988a4c69 ?d?d?l?l?s?s --show
34d8d24499f2d3d4fa9c42a5988a4c69:12ab$%
hashcat --force --status --hash-type=13751 --attack-mode=0 --workload-profile=2 container wordlist.txt
john --wordlist:wiki.txt4 keeppass.hash
john --wordlist:name_food_city.txt id_rsa_secret.hash
kali@kali:/mnt/hgfs/ctf/ctf_kali/veracryptcrack2/containerfiles$ hashcat -g 20000 -m 16500 -a 0 JWT.txt  rockyou_korea.txt