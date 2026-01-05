---
title: "[Gentoo]Clean up world file"
date: 2008-05-03
author: pengjianqing
categories: ['Command', 'Config Files', 'gentoo']
---

**[Gentoo]Clean up world file**

 

 

let me name it "reverse approach".

You first make a back up and empty your world file:
1) gentoo ~ #cp /var/lib/portage/world ~/ && >/var/lib/portage/world
and then build it again:
2) gentoo ~ #regenworld

"regenworld" will put some packages which it thinks belong to the world
list.
Now check what portage finds to be useless when the world set is almost
empty:
3) gentoo ~ #emerge --depclean --pretend

From the list shown by the above command you chose the program packages
you *want* to have installed and put them in the world file. One "atom"
("category-name/package-name", without version numbers) per line.
Now do as "emerge --depclean" recommends:

4) gentoo ~ #emerge --update --newuse --deep world

Repeat the steps from (2) to (4) until (3) shows only packages that are
not familiar to you and (4) doesn't want to install anything.

Next. Check if there are no system packages in the list (3) shows:
5) gentoo ~ #emerge -pve system

It should not happen that (3) wants to remove system packages but its
better to be sure.

Now "cross your fingers" and execute emerge --deplcean for real (without
--pretend).
6) emerge --deplcean
Immediately after (6) finishes you *must* do:
7) emerge -DuN world
8) revdep-rebuild

When (8) is successfully finished you should have a "clean" world set
within a healthy system.
If something goes wrong you can bring back your working "world" and
recheck all packages:

#cp ~/world /var/lib/portage/world
#emerge -DuN world
#revdep-rebuild