---
title: "Virtualbox与主机共享，建立桥接方法（转）"
date: 2007-12-06
author: pengjianqing
categories: ['Software', 'Ubuntu']
---

转自：http://forum.ubuntu.org.cn/viewtopic.php?t=63120

今晚无意中发现了virtualbox安装后放在/opt/VirtualBox-1.4.0目录中的用 户手册文件UserManual.pdf，打开一看，哈哈！里面说得真是详细啊！可惜是英文的，但凭自己这么蹩脚的英语也还基本能看懂一些。这里将我根据 其中的说明实现“主机”和“虚拟机”之间的桥接模式的过程描述一下。整个过程非常简单，比网上找到的方法简单多了，而且一次配置完了可以永久生效。

先简单描述一下我的电脑的基本情况：
主机硬件：惠普v3009tu
主机操作系统：ubuntu 7.04
主机网卡：有线网卡（eth0）一块（无线网卡我没用）
主机网络环境：内部局域网，通过路由器上网
虚拟机：用virtualbox建立，虚拟机操作系统为windows xp sp2

再说配置过程，并作简单说明：

第一步，安装必备的工具（若已安装可跳过）：
（1）安装uml-utilities，该工具包含建立虚拟网络设备（所谓的“TAP interfaces”）的工具：
sudo apt-get install uml-utilities
（2）安装桥接工具bridge-utils：
sudo apt-get install bridge-utils

第二步，为了使你的虚拟机能够访问网络接口，你必须将运行虚拟主机的用户的用户名（通常是你的ubuntu登录用户名）添加到uml-net用户组。命令行的运行方法是（请用你的用户名替换其中的“vboxuser”）：
sudo gpasswd -a vboxuser uml-net
你也可以通过gnome面板上的“系统—系统管理—用户和组”来添加，方法从略。
请注意：为了使改动生效，请重新启动你的电脑。

第三步，向你的ubuntu操作系统描述你要添加的虚拟网络设备：
sudo gedit /etc/network/interfaces
在打开的文件后面添加下面的内容（请用你的用户名替换其中的“vboxuser”），保存好：

auto tap0
iface tap0 inet manual
up ifconfig $IFACE 0.0.0.0 up
down ifconfig $IFACE down
tunctl_user vboxuser

auto br0
iface br0 inet dhcp
bridge_ports all tap0

上面第一部分的大概意思是将虚拟网络接口命名为“tap0”，指定该接口IP配置方法为手动，并指定使用该接口的用户。第二部分的大概意思是建立 一个名叫“br0”的桥，该桥的IP配置方法为通过DHCP配置，主机中的所有网络接口，也包括tap0这个虚拟网络接口，都将建立在这个桥之上。

第四步，激活刚才建立的虚拟网络接口和网络桥：
sudo /sbin/ifup tap0
sudo /sbin/ifup br0
这个步骤只需要做一次，下次主机重新启动时，这个接口和桥将自动激活。

第五步，启动virtualbox，在主界面上选中要使用刚才建立的虚拟网络接口tap0的虚拟机，点“设置”，在弹出的窗口中选“网络”，选中 其中一块网卡（通常为“网络适配器 0”），选中“启用网络适配器”，“连接到”后面选“Host Interface”，选中“接入网线”，然后在“主机网络界面名称”中填入刚才建立的虚拟网络接口的名字“tap0”，确定。

第六步，配置主机和虚拟机的网络。这步太简单了，两者你想怎么配置怎么配置。无论是主机，还是虚拟机，都是既可以手工指定静态IP，也可以从DHCP动态获取IP地址（当然，主机和虚拟机应该在同一个网段）。不过前提是要你的网管放行才行！

好了，经过上面的配置后，主机和虚拟机就成了局域网中地位相同的两台机器了，想怎么共享就怎么共享啰！

**下面是我的/etc/network/interfaces**

** auto lo
iface lo inet loopback**

**auto tap0
iface tap0 inet manual
up ifconfig $IFACE 0.0.0.0 up
down ifconfig $IFACE down
tunctl_user pjq**

**auto br0
iface br0 inet static
bridge_ports all tap0
address 10.0.1.112
netmask 255.255.255.0
network 10.0.1.0
broadcast 10.0.1.255
gateway 10.0.1.1**