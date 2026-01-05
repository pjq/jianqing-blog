---
title: "Tailscale"
date: 2022-09-16
author: pengjianqing
categories: ['Tech']
---

Tailscale is one powerful VPN mesh solution, it's very easy to build your internal virtual network without any complicate config or setup.
I just learn it today, and just follow the official website, to setup for my NAS/Android/Linux Server.

- https://tailscale.com/download

![](../images/adc19ee1.png)

## Enable the exit node

```
`tailscale up --advertise-exit-node`
```

## Enable the subnet routers

```
`tailscale up --advertise-routes=192.168.1.0/24`
```

Or you can enable both

```
`sudo tailscale up --advertise-routes=192.168.1.0/24 --advertise-exit-node
sudo tailscale up --advertise-routes=192.168.1.0/24,192.168.71.0/24 --advertise-exit-node`
```

So which means after you enable the exit node, and you can use it as the proxy if you want to bypass the GFW in the Android App, you can switch the different `exit node`, maybe in local or another Country. And subnet routers means you can visit the local network directly, and which is really simple and convenient, and powerful feature.

```
`tailscale up --exit-node=100.76.xxx.xxx --exit-node-allow-lan-access --advertise-exit-node --advertise-routes=192.168.1.0/24,192.168.8.1/24,192.168.71.0/24`
```