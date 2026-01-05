---
title: "Gentoo上安装compiz fusion"
date: 2008-09-13
author: pengjianqing
categories: ['gentoo']
---

好长时间没玩3D桌面了，今天心血来潮想装了玩玩。
    以前在ubuntu上玩过。

   要安装compiz fusion要加上desktop-effects（layman -a desktop-effects）,然后更新它（layman -S）

    然后参考了这里的[帖子](http://liyanrui.is-programmer.com/show/2182.html)
现在正在安装中。
安装最新的9999

[这是Gentoo Wiki上关于安装Compiz-fusion的文章。](http://gentoo-wiki.com/Compiz_Fusion)
写得挺全的。
主要安装三个部分：compiz-fusion fusion-icon ccsm
1.取消mask
autounmask x11-wm/compiz-fusion-9999
autounmask x11-apps/fusion-icon-9999
autounmask x11-apps/ccsm-9999
2. 然后emerge compiz-fusion fusion-icon ccsm

3.配置xorg.conf支持Desktop Effects
[参考
](http://gentoo-wiki.com/HOWTO_nVidia_GL_Desktop_Effects)
主要参考了这段：
Section "Module"
        ...
#       "dri" and "GLcore" should be commented out or absent
#       Load  "GLcore"
#       Load  "dri"
#       The "glx" entry should exist as shown:
        Load  "glx"
        ...
EndSection

Section "Device"
        Option      "AddARGBGLXVisuals" "true"
        # This option must be either undeclared or
        # false, in order to avoid periodic short-term
        # freezes on beryl and other OpenGL intensive
        # programs
        Option      "UseEvents"         "false"

EndSection

Section "Extensions"
        Option      "Composite"   "enable"
EndSection

4.然后重启X
 # xdpyinfo | grep Composite
    Composite
# eselect opengl set nvidia

5.然后打开Applications->System Tools->compiz fusion icon.

应该就可以看到效果了。

PS：之前没有修改xorg.conf,就出不了3D效果，所以一定要记得修改xorg.conf文件。
     由于是用的git，要从[国外网站](//anongit.compiz-fusion.org/fusion/compizconfig/ccsm)下载，所以下载速度比较慢，要有点耐心。

附上安装compiz修改后的文件：
附件1：xorg.conf
`localhost pjq # cat /etc/X11/xorg.conf
Section "ServerLayout"
	Identifier     "X.org Configured"
	Screen      0  "Screen0" 0 0
	InputDevice    "Mouse0" "CorePointer"
	InputDevice    "Keyboard0" "CoreKeyboard"
EndSection

Section "Files"
	RgbPath      "/usr/share/X11/rgb"
	ModulePath   "/usr/lib/xorg/modules"
	FontPath     "/usr/share/fonts/misc/"
	FontPath     "/usr/share/fonts/TTF/"
	FontPath     "/usr/share/fonts/OTF"
	FontPath     "/usr/share/fonts/Type1/"
	FontPath     "/usr/share/fonts/100dpi/"
	FontPath     "/usr/share/fonts/75dpi/"
EndSection

Section "Module"
	Load  "dbe"
#	Load  "dri"
	Load  "xtrap"
	Load  "glx"
	Load  "record"
	Load  "extmod"
#	Load  "GLcore"
	Load  "type1"
	Load  "freetype"
EndSection

Section "InputDevice"
	Identifier  "Keyboard0"
	Driver      "kbd"
EndSection

Section "InputDevice"
	Identifier  "Mouse0"
	Driver      "mouse"
	Option	    "Protocol" "Auto"
	Option	    "Device" "/dev/input/mice"
	Option	    "ZAxisMapping" "4 5 6 7"
EndSection

Section "Monitor"

	#DisplaySize	  340   270	# mm
 ### Comment all HorizSync and VertRefresh values to use DDC:
	Identifier   "Monitor0"
	VendorName   "PHL"
	ModelName    "Philips 170S"
 ### Comment all HorizSync and VertRefresh values to use DDC:
	HorizSync    31.5 - 64.3
	VertRefresh  56.0 - 76.0
	Option	    "DPMS"
EndSection

Section "Device"
         Option      "AddARGBGLXVisuals" "true"
         # This option must be either undeclared or
	 # false, in order to avoid periodic short-term
	 # freezes on beryl and other OpenGL intensive
	 # programs
        Option      "UseEvents"         "false"
        ### Available Driver options are:-
        ### Values: : integer, : float, : "True"/"False",
        ### : "String", : " Hz/kHz/MHz"
        ### [arg]: arg optional
        #Option     "SWcursor"           	# []
        #Option     "HWcursor"           	# []
        #Option     "NoAccel"            	# []
        #Option     "ShadowFB"           	# []
        #Option     "UseFBDev"           	# []
        #Option     "Rotate"             	# []
        #Option     "VideoKey"           	# 
        #Option     "FlatPanel"          	# []
        #Option     "FPDither"           	# []
        #Option     "CrtcNumber"         	# 
        #Option     "FPScale"            	# []
        #Option     "FPTweak"            	# 
        #Option     "DualHead"           	# []
	Identifier  "Card0"
	Driver      "nvidia"
	VendorName  "nVidia Corporation"
	BoardName   "G70 [GeForce 7600 GS]"
	BusID       "PCI:6:0:0"
EndSection

Section "Screen"
	Identifier "Screen0"
	Device     "Card0"
	Monitor    "Monitor0"
	SubSection "Display"
		Viewport   0 0
		Depth     1
	EndSubSection
	SubSection "Display"
		Viewport   0 0
		Depth     4
	EndSubSection
	SubSection "Display"
		Viewport   0 0
		Depth     8
	EndSubSection
	SubSection "Display"
		Viewport   0 0
		Depth     15
	EndSubSection
	SubSection "Display"
		Viewport   0 0
		Depth     16
	EndSubSection
	SubSection "Display"
		Viewport   0 0
		Depth     24
	EndSubSection
EndSection

Section "DRI"
	Group        0
EndSection

Section "Extensions"
        Option      "Composite"   "enable"
EndSection
`

附件2：/etc/portage/package.keywords 中关于compiz的部分，由autounmask自动生成。
`# ---
# BEGIN: x11-wm/compiz-fusion-9999
# ---
=x11-wm/compiz-fusion-9999 **
=x11-libs/compizconfig-backend-gconf-9999 **
=x11-wm/compiz-9999 **
=x11-libs/libcompizconfig-9999 **
# ---
# END: x11-wm/compiz-fusion-9999
# ---

# ---
# BEGIN: x11-apps/fusion-icon-9999
# ---
=x11-apps/fusion-icon-9999 **
=dev-python/compizconfig-python-9999 **
# ---
# END: x11-apps/fusion-icon-9999
# ---

# ---
# BEGIN: x11-apps/ccsm-9999
# ---
=x11-apps/ccsm-9999 **
# ---
# END: x11-apps/ccsm-9999
# ---

`