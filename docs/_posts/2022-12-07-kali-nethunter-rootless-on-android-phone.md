---
title: "Kali Nethunter Rootless on Android Phone"
date: 2022-12-07
author: pengjianqing
categories: ['Tech']
tags: ['Android', 'Kali', 'Rootless']
---

## Install

Install some Apps

- Install the NetHunter-Store app from [store.nethunter.com](https://store.nethunter.com/)

- From the NetHunter Store, install **Termux**, **NetHunter-KeX client**, and **Hacker’s keyboard**

Install via Termux terminal

```
`kali@kali:~$ termux-setup-storage
kali@kali:~$ curl -o install-nethunter-termux https://offs.ec/2MceZWr -L
kali@kali:~$ chmod +x install-nethunter-termux
kali@kali:~$ ./install-nethunter-termux`
```

## Command list

`nethunter`start Kali NetHunter command line interface`nethunter kex passwd`configure the KeX password (only needed before 1st use)`nethunter kex &`start Kali NetHunter Desktop Experience user sessions`nethunter kex stop`stop Kali NetHunter Desktop Experience`nethunter `run in NetHunter environment`nethunter -r`start Kali NetHunter cli as root`nethunter -r kex passwd`configure the KeX password for root`nethunter -r kex &`start Kali NetHunter Desktop Experience as root`nethunter -r kex stop`stop Kali NetHunter Desktop Experience root sessions`nethunter -r kex kill`Kill all KeX sessions`nethunter -r `run `` in NetHunter environment as root

![](../images/c8b4e23e.jpg)

![](../images/5520b8e3.jpg)

Reference

- [https://www.kali.org/docs/nethunter/nethunter-rootless/](https://www.kali.org/docs/nethunter/nethunter-rootless/)

- https://www.youtube.com/watch?v=WiONcVNeQ-o