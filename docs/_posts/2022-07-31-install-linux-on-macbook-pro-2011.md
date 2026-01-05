---
title: "Install Linux on MacBook Pro 2011"
date: 2022-07-31
author: pengjianqing
categories: ['Linux', 'Tech']
---

## Can't create symlink on fat32

```
`Failed to create symlink to vmlinuz-5.4.0-42-generic: Operation not permitted at /usr/bin/linux-update-symlinks line 64
`
```

Disable do_symlinks  in `/etc/kernel-img.conf `

```
`cat /etc/kernel-img.conf 
# Kernel Image management overrides
# See kernel-img.conf(5) for details
do_symlinks = no
do_bootloader = no
`
```

## Upgrade and clean

```
`sudo apt update && sudo apt upgrade && sudo apt autoremove && sudo apt clean && sudo apt autoclean && sudo apt --fix-broken install`
```

## Fix wireless network(WiFI)

```
`sudo apt-get update
sudo apt-get --reinstall install bcmwl-kernel-source

sudo modprobe -r b43 ssb wl brcmfmac brcmsmac bcma`
```

## Open TTY

On Mac, you can switch between Desktop between tty with the keys:

```
`fn+control+option(alt)+f1...f6...f7(Desktop)`
```

## Install rEFind

- https://www.rodsbooks.com/refind/installing.html

```
sudo apt-add-repository ppa:rodsmith/refind
sudo apt-get update
sudo apt-get install refind
sudo refind-install
```

## Install boot-repair

If can't boot the system, it's recommend to fix it via the boot-repair with LIVE CD

- https://help.ubuntu.com/community/Boot-Repair

```
`sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt update
sudo apt install -y boot-repair && boot-repair`
```

## lspci -k

```
`root@jianqing-MacBookPro:/boot# lspci -k
00:00.0 Host bridge: Intel Corporation 2nd Generation Core Processor Family DRAM Controller (rev 09)
	Subsystem: Apple Inc. MacBookPro8,2 [Core i7, 15", 2011]
00:01.0 PCI bridge: Intel Corporation Xeon E3-1200/2nd Generation Core Processor Family PCI Express Root Port (rev 09)
	Kernel driver in use: pcieport
00:01.1 PCI bridge: Intel Corporation Xeon E3-1200/2nd Generation Core Processor Family PCI Express Root Port (rev 09)
	Kernel driver in use: pcieport
00:02.0 VGA compatible controller: Intel Corporation 2nd Generation Core Processor Family Integrated Graphics Controller (rev 09)
	Subsystem: Apple Inc. 2nd Generation Core Processor Family Integrated Graphics Controller
	Kernel modules: i915
00:16.0 Communication controller: Intel Corporation 6 Series/C200 Series Chipset Family MEI Controller #1 (rev 04)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: mei_me
	Kernel modules: mei_me
00:1a.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Universal Host Controller #5 (rev 05)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: uhci_hcd
00:1a.7 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #2 (rev 05)
	Subsystem: Intel Corporation Server Board S1200BT Family / Apple MacBook Pro 8,1/8,2
	Kernel driver in use: ehci-pci
00:1b.0 Audio device: Intel Corporation 6 Series/C200 Series Chipset Family High Definition Audio Controller (rev 05)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
00:1c.0 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 1 (rev b5)
	Kernel driver in use: pcieport
00:1c.1 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 2 (rev b5)
	Kernel driver in use: pcieport
00:1c.2 PCI bridge: Intel Corporation 6 Series/C200 Series Chipset Family PCI Express Root Port 3 (rev b5)
	Kernel driver in use: pcieport
00:1d.0 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Universal Host Controller #1 (rev 05)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: uhci_hcd
00:1d.7 USB controller: Intel Corporation 6 Series/C200 Series Chipset Family USB Enhanced Host Controller #1 (rev 05)
	Subsystem: Intel Corporation Server Board S1200BT Family / Apple MacBook Pro 8,1/8,2
	Kernel driver in use: ehci-pci
00:1f.0 ISA bridge: Intel Corporation HM65 Express Chipset LPC Controller (rev 05)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: lpc_ich
	Kernel modules: lpc_ich
00:1f.2 SATA controller: Intel Corporation 6 Series/C200 Series Chipset Family 6 port Mobile SATA AHCI Controller (rev 05)
	Subsystem: Intel Corporation Apple MacBookPro8,2 [Core i7, 15", 2011]
	Kernel driver in use: ahci
	Kernel modules: ahci
00:1f.3 SMBus: Intel Corporation 6 Series/C200 Series Chipset Family SMBus Controller (rev 05)
	Subsystem: Intel Corporation Server Board S1200BT Family / Apple MacBook Pro 8,1/8,2
	Kernel driver in use: i801_smbus
	Kernel modules: i2c_i801
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Whistler [Radeon HD 6630M/6650M/6750M/7670M/7690M]
	Subsystem: Apple Inc. MacBookPro8,2 [Core i7, 15", Late 2011]
	Kernel modules: radeon
01:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Turks HDMI Audio [Radeon HD 6500/6600 / 6700M Series]
	Kernel driver in use: snd_hda_intel
	Kernel modules: snd_hda_intel
02:00.0 Ethernet controller: Broadcom Inc. and subsidiaries NetXtreme BCM57765 Gigabit Ethernet PCIe (rev 10)
	Subsystem: Broadcom Inc. and subsidiaries NetXtreme BCM57765 Gigabit Ethernet PCIe
	Kernel driver in use: tg3
	Kernel modules: tg3
02:00.1 SD Host controller: Broadcom Inc. and subsidiaries BCM57765/57785 SDXC/MMC Card Reader (rev 10)
	Subsystem: Broadcom Inc. and subsidiaries BCM57765/57785 SDXC/MMC Card Reader
	Kernel driver in use: sdhci-pci
	Kernel modules: sdhci_pci
03:00.0 Network controller: Broadcom Inc. and subsidiaries BCM4331 802.11a/b/g/n (rev 02)
	Subsystem: Apple Inc. AirPort Extreme
	Kernel driver in use: wl
	Kernel modules: bcma, wl
04:00.0 FireWire (IEEE 1394): LSI Corporation FW643 [TrueFire] PCIe 1394b Controller (rev 08)
	Subsystem: LSI Corporation FW643 [TrueFire] PCIe 1394b Controller
	Kernel driver in use: firewire_ohci
	Kernel modules: firewire_ohci
05:00.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
06:00.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
06:03.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
06:04.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
06:05.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
06:06.0 PCI bridge: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Kernel driver in use: pcieport
07:00.0 System peripheral: Intel Corporation CV82524 Thunderbolt Controller [Light Ridge 4C 2010]
	Subsystem: Device 2222:1111
	Kernel driver in use: thunderbolt
	Kernel modules: thunderbolt
`
```

## Shortcuts

- Reset NVRAM: Option+Command+P+R
- Reset SMC: Shift+Control+Option+Power Button
- Hardware Test: Option+d+Power