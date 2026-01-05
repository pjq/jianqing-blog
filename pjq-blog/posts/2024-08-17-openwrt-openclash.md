---
title: "OpenWRT + OpenClash"
date: 2024-08-17
author: pengjianqing
categories: ['Uncategorized']
---

# iptables

opkg update
opkg install coreutils-nohup bash iptables dnsmasq-full curl ca-certificates ipset ip-full iptables-mod-tproxy iptables-mod-extra libcap libcap-bin ruby ruby-yaml kmod-tun kmod-inet-diag unzip luci-compat luci luci-base

# nftables

opkg update
opkg install coreutils-nohup bash dnsmasq-full curl ca-certificates ipset ip-full libcap libcap-bin ruby ruby-yaml kmod-tun kmod-inet-diag unzip kmod-nft-tproxy luci-compat luci luci-base

[https://github.com/vernesong/OpenClash/releases](https://github.com/vernesong/OpenClash/releases)

[https://chitchat.pjq.me/download/luci-app-openclash_0.46.014-beta_all.ipk](https://chitchat.pjq.me/download/luci-app-openclash_0.46.014-beta_all.ipk)

## ShellClash

- https://github.com/juewuy/ShellCrash/blob/dev/README_CN.md

```
export url='https://gh.jwsc.eu.org/master' && sh -c "$(curl -kfsSl $url/install.sh)" && source /etc/profile &> /dev/null
```

```
`export url='https://fastly.jsdelivr.net/gh/juewuy/ShellCrash@master' && wget -q --no-check-certificate -O /tmp/install.sh $url/install.sh  && sh /tmp/install.sh && source /etc/profile &> /dev/null`
```