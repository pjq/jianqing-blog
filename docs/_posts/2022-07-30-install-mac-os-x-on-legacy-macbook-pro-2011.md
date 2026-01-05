---
title: "Install Mac OS X On legacy MacBook Pro 2011"
date: 2022-07-30
author: pengjianqing
categories: ['Tech']
---

After I click the "Upgrade" in the old MacBook Pro 2011, High Sierra, after upgrade for a while, then I saw the blue screen, waiting for a long time, it's still show the blue screen.

Try force reboot, with "Option" key, it has options

- EFI BOOT
- Mac OS X Install
- Max OS X

I have try all of them, [1] will show some errors with some text, [2] & [3] will show the same blue screen.

Then also tried

- Recovery Mode, doesn't work
- Network Recovery Mode, doesn't work
- Hardware test, seems check passed.
- CMD+v, verbose mode, it works.

## Create USB bootable disk

Follow the official guideline

- https://support.apple.com/en-us/HT201372

It doesn't work on my new M1 MacBook Pro 2021.

Found kind of solution like this, doesn't work.

```
`cd /Applications/Install\ macOS\ Mojave.app/Contents/Resources/

codesign -s - -f createinstallmedia`
```

## Convert dmg to iso

Finally try convert dmg to iso, and burn it with "dd"

```
`hdiutil convert InstallMacOSX.dmg -format UDTO -o InstallMacOSX.iso
mv InstallMacOSX.iso.cdr InstallMacOSX.iso
sudo dd bs=8m if=InstallMacOSX.iso of=/dev/disk6`
```

Still doesn't work, blue screen.

## Download Images

I save it to the baidu netdisk, feel free to download

```
`链接: https://pan.baidu.com/s/1MyEik1hHeD4KPzHdZApzNg 提取码: ey44 复制这段内容后打开百度网盘手机App，操作更方便哦`
```

```
`macOS High Sierra 10.13.6 by macOShome.com.dmg 2022-07-3018:08 5G

USB Install macOS Sierra 10.12.6(16G29).dmg 2022-07-3018:08 4.7G

USB Install macOS High Sierra 10.13.6(17G66).dmg 2022-07-3018:08 4.9G`
```