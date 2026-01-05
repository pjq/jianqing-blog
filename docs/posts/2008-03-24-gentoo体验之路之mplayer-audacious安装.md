---
title: "gentoo体验之路之mplayer audacious安装"
date: 2008-03-24
author: pengjianqing
categories: ['gentoo', 'Software']
---

要让audacious能够播放mp3需要加入mp3 wma wmv mpd USE

其中mpd很重要如果没有mpd USE就不能播放mp3了

USE="mp3 wma wmv mpd" emerge audacious

安装mplayer

cat emergemplayer.sh

#!/bin/sh
USE="aac real win32codecs -ipv6" emerge mplayer
emerge mplayerplug-in

如果双击提示找不到文件时，

将Exec=gmplayer %U改为

Exec=gmplayer %f或者去掉%U

cat /usr/share/applications/mplayer.desktop
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=MPlayer
GenericName=Multimedia player
Comment=Multimedia player
Comment[de]=Multimedia-Player
Comment[es]=Reproductor multimedia
Comment[fr]=Lecteur multimédia
Comment[it]=Lettore multimediale
Icon=mplayer.xpm
TryExec=gmplayer
Exec=gmplayer %f
Terminal=false
Categories=GTK;AudioVideo;Audio;Video;Player;TV;
MimeType=application/ogg;application/x-ogg;application/sdp;application/smil;application/x-smil;application/streamingmedia;application/x-streamingmedia;application/vnd.rn-realmedia;application/vnd.rn-realmedia-vbr;audio/aac;audio/x-aac;audio/m4a;audio/x-m4a;audio/mp1;audio/x-mp1;audio/mp2;audio/x-mp2;audio/mp3;audio/x-mp3;audio/mpeg;audio/x-mpeg;audio/mpegurl;audio/x-mpegurl;audio/mpg;audio/x-mpg;audio/rn-mpeg;audio/scpls;audio/x-scpls;audio/vnd.rn-realaudio;audio/wav;audio/x-pn-windows-pcm;audio/x-realaudio;audio/x-pn-realaudio;audio/x-ms-wma;audio/x-pls;audio/x-wav;video/mpeg;video/x-mpeg;video/x-mpeg2;video/msvideo;video/x-msvideo;video/quicktime;video/vnd.rn-realvideo;video/x-ms-afs;video/x-ms-asf;video/x-ms-wmv;video/x-ms-wmx;video/x-ms-wvxvideo;video/x-avi;video/x-fli;video/x-theora;video/x-matroska;