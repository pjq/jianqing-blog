---
title: "My server is flagged as hacked"
date: 2023-11-21
author: pengjianqing
categories: ['Uncategorized']
---

## Background

8 security vendors flagged this URL as malicious

- [https://www.virustotal.com/gui/url/3523cf904e82993fe621505619245f236c8cdfe8894cdcc1cb742a2348c2a1e2?nocache=1](https://www.virustotal.com/gui/url/3523cf904e82993fe621505619245f236c8cdfe8894cdcc1cb742a2348c2a1e2?nocache=1)

![](../images/a225595c.png)

## tcpdump to figure out the force ssh attack from the server

```
` sudo tcpdump -vv -i eth0 src 165.227.xx.xx and not dst 101.230.xx.xx  port 22 -X -n`
```

So here we need to exclude the data that I am using connect to

So let's monitor the logs, the server is trying to ssh to the other servers.

```
`tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes

18:24:01.659278 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto TCP (6), length 60)
    165.227.51.176.22 > 36.92.214.178.59718: Flags [S.], cksum 0xd4d0 (incorrect -> 0xe8ba), seq 15158420, ack 2800055874, win 65160, options [mss 1460,sackOK,TS val 3933769059 ecr 2697666402,nop,wscale 7], length 0
	0x0000:  4500 003c 0000 4000 4006 661a a5e3 33b0  E.. 36.92.214.178.59718: Flags [.], cksum 0xd4c8 (incorrect -> 0x1270), seq 1, ack 23, win 509, options [nop,nop,TS val 3933769254 ecr 2697666604], length 0
	0x0000:  4500 0034 8cd2 4000 4006 d94f a5e3 33b0  E..4..@.@..O..3.
	0x0010:  245c d6b2 0016 e946 00e7 4c95 a6e5 7658  $\.....F..L...vX
	0x0020:  8010 01fd d4c8 0000 0101 080a ea78 8e26  .............x.&
	0x0030:  a0cb 202c                                ...,
18:24:01.873054 IP (tos 0x0, ttl 64, id 36051, offset 0, flags [DF], proto TCP (6), length 93)
    165.227.51.176.22 > 36.92.214.178.59718: Flags [P.], cksum 0xd4f1 (incorrect -> 0xe704), seq 1:42, ack 23, win 509, options [nop,nop,TS val 3933769273 ecr 2697666604], length 41: SSH: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.4
	0x0000:  4500 005d 8cd3 4000 4006 d925 a5e3 33b0  E..]..@.@..%..3.
	0x0010:  245c d6b2 0016 e946 00e7 4c95 a6e5 7658  $\.....F..L...vX
	0x0020:  8018 01fd d4f1 0000 0101 080a ea78 8e39  .............x.9
	0x0030:  a0cb 202c 5353 482d 322e 302d 4f70 656e  ...,SSH-2.0-Open
	0x0040:  5353 485f 382e 3970 3120 5562 756e 7475  SSH_8.9p1.Ubuntu
	0x0050:  2d33 7562 756e 7475 302e 340d 0a         -3ubuntu0.4..
18:24:02.067852 IP (tos 0x0, ttl 64, id 36052, offset 0, flags [DF], proto TCP (6), length 1132)
    165.227.51.176.22 > 36.92.214.178.59718: Flags [P.], cksum 0xd900 (incorrect -> 0xa4a9), seq 42:1122, ack 23, win 509, options [nop,nop,TS val 3933769467 ecr 2697666808], length 1080
	0x0000:  4500 046c 8cd4 4000 4006 d515 a5e3 33b0  E..l..@.@.....3.
	0x0010:  245c d6b2 0016 e946 00e7 4cbe a6e5 7658  $\.....F..L...vX
	0x0020:  8018 01fd d900 0000 0101 080a ea78 8efb  .............x..
	0x0030:  a0cb 20f8 0000 0434 0714 2885 704e d88b  .......4..(.pN..
	0x0040:  935e b97f ee38 d001 6452 0000 0109 6375  .^...8..dR....cu
	0x0050:  7276 6532 3535 3139 2d73 6861 3235 362c  rve25519-sha256,
	0x0060:  6375 7276 6532 3535 3139 2d73 6861 3235  curve25519-sha25
	0x0070:  3640 6c69 6273 7368 2e6f 7267 2c65 6364  6@libssh.org,ecd
	0x0080:  682d 7368 6132 2d6e 6973 7470 3235 362c  h-sha2-nistp256,
	0x0090:  6563 6468 2d73 6861 322d 6e69 7374 7033  ecdh-sha2-nistp3
	0x00a0:  3834 2c65 6364 682d 7368 6132 2d6e 6973  84,ecdh-sha2-nis
	0x00b0:  7470 3532 312c 736e 7472 7570 3736 3178  tp521,sntrup761x
	0x00c0:  3235 3531 392d 7368 6135 3132 406f 7065  25519-sha512@ope
	0x00d0:  6e73 7368 2e63 6f6d 2c64 6966 6669 652d  nssh.com,diffie-
	0x00e0:  6865 6c6c 6d61 6e2d 6772 6f75 702d 6578  hellman-group-ex
	0x00f0:  6368 616e 6765 2d73 6861 3235 362c 6469  change-sha256,di
	0x0100:  6666 6965 2d68 656c 6c6d 616e 2d67 726f  ffie-hellman-gro
	0x0110:  7570 3136 2d73 6861 3531 322c 6469 6666  up16-sha512,diff
	0x0120:  6965 2d68 656c 6c6d 616e 2d67 726f 7570  ie-hellman-group
	0x0130:  3138 2d73 6861 3531 322c 6469 6666 6965  18-sha512,diffie
	0x0140:  2d68 656c 6c6d 616e 2d67 726f 7570 3134  -hellman-group14
	0x0150:  2d73 6861 3235 3600 0000 3972 7361 2d73  -sha256...9rsa-s
	0x0160:  6861 322d 3531 322c 7273 612d 7368 6132  ha2-512,rsa-sha2
	0x0170:  2d32 3536 2c65 6364 7361 2d73 6861 322d  -256,ecdsa-sha2-
	0x0180:  6e69 7374 7032 3536 2c73 7368 2d65 6432  nistp256,ssh-ed2
	0x0190:  3535 3139 0000 006c 6368 6163 6861 3230  5519...lchacha20
	0x01a0:  2d70 6f6c 7931 3330 3540 6f70 656e 7373  -poly1305@openss
	0x01b0:  682e 636f 6d2c 6165 7331 3238 2d63 7472  h.com,aes128-ctr
	0x01c0:  2c61 6573 3139 322d 6374 722c 6165 7332  ,aes192-ctr,aes2
	0x01d0:  3536 2d63 7472 2c61 6573 3132 382d 6763  56-ctr,aes128-gc
	0x01e0:  6d40 6f70 656e 7373 682e 636f 6d2c 6165  m@openssh.com,ae
	0x01f0:  7332 3536 2d67 636d 406f 7065 6e73 7368  s256-gcm@openssh
	0x0200:  2e63 6f6d 0000 006c 6368 6163 6861 3230  .com...lchacha20
	0x0210:  2d70 6f6c 7931 3330 3540 6f70 656e 7373  -poly1305@openss
	0x0220:  682e 636f 6d2c 6165 7331 3238 2d63 7472  h.com,aes128-ctr
	0x0230:  2c61 6573 3139 322d 6374 722c 6165 7332  ,aes192-ctr,aes2
	0x0240:  3536 2d63 7472 2c61 6573 3132 382d 6763  56-ctr,aes128-gc
	0x0250:  6d40 6f70 656e 7373 682e 636f 6d2c 6165  m@openssh.com,ae
	0x0260:  7332 3536 2d67 636d 406f 7065 6e73 7368  s256-gcm@openssh
	0x0270:  2e63 6f6d 0000 00d5 756d 6163 2d36 342d  .com....umac-64-
	0x0280:  6574 6d40 6f70 656e 7373 682e 636f 6d2c  etm@openssh.com,
	0x0290:  756d 6163 2d31 3238 2d65 746d 406f 7065  umac-128-etm@ope
	0x02a0:  6e73 7368 2e63 6f6d 2c68 6d61 632d 7368  nssh.com,hmac-sh
	0x02b0:  6132 2d32 3536 2d65 746d 406f 7065 6e73  a2-256-etm@opens
	0x02c0:  7368 2e63 6f6d 2c68 6d61 632d 7368 6132  sh.com,hmac-sha2
	0x02d0:  2d35 3132 2d65 746d 406f 7065 6e73 7368  -512-etm@openssh
	0x02e0:  2e63 6f6d 2c68 6d61 632d 7368 6131 2d65  .com,hmac-sha1-e
	0x02f0:  746d 406f 7065 6e73 7368 2e63 6f6d 2c75  tm@openssh.com,u
	0x0300:  6d61 632d 3634 406f 7065 6e73 7368 2e63  mac-64@openssh.c
	0x0310:  6f6d 2c75 6d61 632d 3132 3840 6f70 656e  om,umac-128@open
	0x0320:  7373 682e 636f 6d2c 686d 6163 2d73 6861  ssh.com,hmac-sha
	0x0330:  322d 3235 362c 686d 6163 2d73 6861 322d  2-256,hmac-sha2-
	0x0340:  3531 322c 686d 6163 2d73 6861 3100 0000  512,hmac-sha1...
	0x0350:  d575 6d61 632d 3634 2d65 746d 406f 7065  .umac-64-etm@ope
	0x0360:  6e73 7368 2e63 6f6d 2c75 6d61 632d 3132  nssh.com,umac-12
	0x0370:  382d 6574 6d40 6f70 656e 7373 682e 636f  8-etm@openssh.co
	0x0380:  6d2c 686d 6163 2d73 6861 322d 3235 362d  m,hmac-sha2-256-
	0x0390:  6574 6d40 6f70 656e 7373 682e 636f 6d2c  etm@openssh.com,
	0x03a0:  686d 6163 2d73 6861 322d 3531 322d 6574  hmac-sha2-512-et
	0x03b0:  6d40 6f70 656e 7373 682e 636f 6d2c 686d  m@openssh.com,hm
	0x03c0:  6163 2d73 6861 312d 6574 6d40 6f70 656e  ac-sha1-etm@open
	0x03d0:  7373 682e 636f 6d2c 756d 6163 2d36 3440  ssh.com,umac-64@
	0x03e0:  6f70 656e 7373 682e 636f 6d2c 756d 6163  openssh.com,umac
	0x03f0:  2d31 3238 406f 7065 6e73 7368 2e63 6f6d  -128@openssh.com
	0x0400:  2c68 6d61 632d 7368 6132 2d32 3536 2c68  ,hmac-sha2-256,h
	0x0410:  6d61 632d 7368 6132 2d35 3132 2c68 6d61  mac-sha2-512,hma
	0x0420:  632d 7368 6131 0000 0015 6e6f 6e65 2c7a  c-sha1....none,z
	0x0430:  6c69 6240 6f70 656e 7373 682e 636f 6d00  lib@openssh.com.
	0x0440:  0000 156e 6f6e 652c 7a6c 6962 406f 7065  ...none,zlib@ope
	0x0450:  6e73 7368 2e63 6f6d 0000 0000 0000 0000  nssh.com........
	0x0460:  0000 0000 0000 0000 0000 0000            ............
18:24:02.112049 IP (tos 0x0, ttl 64, id 36053, offset 0, flags [DF], proto TCP (6), length 52)
    165.227.51.176.22 > 36.92.214.178.59718: Flags [.], cksum 0xd4c8 (incorrect -> 0x0878), seq 1122, ack 999, win 502, options [nop,nop,TS val 3933769512 ecr 2697666808], length 0`
```

## Find out the process

>>**So how can I know which process is doing the ssh connection?**

GPT-4 Response

If you want to check which processes are making SSH connections on your machine, you can use the `netstat`, `lsof` or `ss` commands combined with `grep` to filter the results.

Here are three options:

- Using `netstat` with `grep`:

```
`   netstat -tunp | grep ':22'`
```

The `-tunp` options represent TCP, UDP, numeric (don't resolve names), and programs respectively.

- Using `lsof` with `grep`:

```
`   lsof -i :22`
```

This commands lists all the processes using Internet connections on port 22.

- Using `ss` with `grep`:

```
`   ss -tunp | grep ':22'`
```

The `-tunp` options represent TCP, UDP, numeric (don't resolve names), and processes respectively.

All of these commands will display a list of active SSH connections along with the PID (Process ID) and the name of the process which is holding that connection. You will need root privileges (`sudo`) to see all information.

It's a good practice to keep an eye on active connections, especially if you suspect unauthorized activity. Always be sure you trust the processes that are making SSH connections from your machine.

**>>Here I use the ss command to find out one connection is not my connection**

`tcp ESTAB 0 532 165.227.51.176:22 36.92.214.178:40918 users:(("sshd",pid=655101,fd=4),("sshd",pid=655095,fd=4))`

**So write the bash script to loop check the command outputs, and excluded the 100.117.199.33 and 101.230.72.103(which can be configed, it's my machine), then get the pid, and printout the pid information, so I can know which file/process is running in the background**

```
`sudo ss -tunp | grep ':22'

tcp   ESTAB      0      124    165.227.51.176:22     100.117.199.33:65038 users:(("sshd",pid=654707,fd=4),("sshd",pid=654658,fd=4))
tcp   ESTAB      0      532    165.227.51.176:22      36.92.214.178:40918 users:(("sshd",pid=655101,fd=4),("sshd",pid=655095,fd=4))
tcp   ESTAB      0      0      165.227.51.176:22     101.230.72.103:8857  users:(("sshd",pid=653119,fd=4),("sshd",pid=653030,fd=4))`
```

Yes, you can indeed write a Bash script that will automate the process of checking for unwanted SSH connections. Here's an example of how you can achieve this:

```
`#!/bin/bash

# Define the IP addresses to exclude (comma-separated, without spaces)
exclude_ips="100.117.199.33,101.230.72.103"

while true
do
    sudo ss -tunp | grep ':22' | while read line 
    do
        if echo $line | grep -qE $(echo $exclude_ips | tr "," "|"); then
            continue
        else
            pid=$(echo $line | sed -n -r 's/.*pid=([0-9]+).*/\1/p')
            echo "Unusual SSH connection found from:"
            echo $line
            echo "Here are more details about the process with PID: $pid"
            ps -f -p $pid
            # Uncomment below line if you want to kill the process
            # kill -9 $pid
            echo "-----------"
        fi
    done

    # Wait for 5 seconds before the next check
    sleep 5
done`
```

This script will continuously monitor for new SSH connections, excluding the ones from IP addresses you specified. If it finds a connection from an IP address not in the exclude list, it will print the details of that connection along with information about the process that owns the connection.

Remember to make the script executable with `chmod +x scriptname.sh` before running it.

Please do remember that killing a process should always be your last resort as it can lead to data corruption/loss.

>>**And I got some logs**

```
`www-data  537886  537882  0 Nov20 ?        00:02:34 nginx: worker process
-----------
Unusual SSH connection found from:
tcp ESTAB 0 0 165.227.51.176:22 218.92.0.51:30886 users:(("sshd",pid=663116,fd=4))
Here are more details about the process with PID: 663116
UID          PID    PPID  C STIME TTY          TIME CMD
root      663116     814  0 18:51 ?        00:00:00 sshd: [accepted]
-----------
Unusual SSH connection found from:
tcp ESTAB 0 0 165.227.51.176:443 47.128.53.113:22290 users:(("nginx",pid=537886,fd=48))
Here are more details about the process with PID: 537886
UID          PID    PPID  C STIME TTY          TIME CMD
www-data  537886  537882  0 Nov20 ?        00:02:34 nginx: worker process
-----------
Unusual SSH connection found from:
tcp ESTAB 0 0 165.227.51.176:443 172.69.23.105:22256 users:(("nginx",pid=537886,fd=49))
Here are more details about the process with PID: 537886
UID          PID    PPID  C STIME TTY          TIME CMD
www-data  537886  537882  0 Nov20 ?        00:02:34 nginx: worker process
-----------
Unusual SSH connection found from:
tcp ESTAB 0 0 165.227.51.176:22 218.92.0.51:30886 users:(("sshd",pid=663116,fd=4))
Here are more details about the process with PID: 663116
UID          PID    PPID  C STIME TTY          TIME CMD
root      663116     814  0 18:51 ?        00:00:00 sshd: [accepted]
`
```

Based on the logs you provided, here's what I can observe:

- There are several connections established from your machine to remote IP addresses over common ports such as 22 (SSH) and 443 (HTTPS).

- The processes making these connections are:

- `sshd` (PID: 663116), which is the OpenSSH server process, suggests incoming SSH connections to your machine.

- `nginx` (PID: 537886), which is a popular web server and reverse proxy server. You can see in the logs that from PID 663116, there have been an unknown incoming SSH connection from the IP address 218.92.0.51. Also, from PID 537886 the `nginx` process has made connections to two different remote addresses: 47.128.53.113 and 172.69.23.105. These are likely regular web traffic, but if you did not expect it, further investigation would be prudent.

Without more context, it's unclear whether these connections are normal operations or indicative of a problem. It will depend on what these services are usually doing on your system.

For the `nginx` process connections, you may want to inspect the nginx access and error logs for any unusual requests or activities.

For the SSH connection, if this connection is not made by you, it is definitely suspicious. You might want to check the auth logs (`/var/log/auth.log`) for further details.

Please ensure to have your system and services updated to the latest security patches. Also, regularly monitor system logs and network activities to keep your system secure.
>>**In general the nginx should not call the ssh connection to the other server, right?**

That's correct, under normal circumstances, it's unlikely for Nginx, a web server, to initiate SSH connections by itself. The Nginx service typically serves HTTP and HTTPS requests and doesn't connect to other servers using SSH.

The log you've shared indicates that Nginx is connecting to a remote server on port 443 (HTTPS), which is expected if it's configured to act as a reverse proxy fetching data from that server. Nginx doesn't establish SSH connections.

If you see SSH connections originating from the Nginx process, that's unusual and could potentially be a sign of a misconfiguration or even malicious activity such as an exploit of a vulnerability in Nginx or one of your web applications running under Nginx. In such a case, it would be prudent to perform a thorough security review and possibly engage a professional organization specializing in this if needed.

>>**How to print more information the PID, e.g. which file is executing**

To find detailed information about the process, such as which file is executing, you can use a few different commands. Here are a few examples using the PID:

- Using `/proc/[PID]/exe`: The `/proc` filesystem provides a lot of information about running processes. For any given process PID, `/proc/[PID]/exe` is a symbolic link that points to the executable of the process.

```
`   ls -l /proc/537886/exe`
```

- Using `lsof`: This provides a list of files that are opened by the process.

```
`   lsof -p 537886`
```

- Use `ps`. This prints current information about the process, including the command that was used to run it.

```
`   ps -fp 537886`
```

- `pwdx`: This command provides the current working directory of the process.

```
`   pwdx 537886`
```

Remember to replace `537886` with the PID in question. All of these commands can be used to gather more information about the process that is currently running.

**>>So update the scripts**

```
`#!/bin/bash

# Define the IP addresses to exclude (comma-separated, without spaces)
exclude_ips="100.117.199.33,101.230.72.103"

while true
do
    # Find unwanted ssh connections
    sudo ss -tunp | grep 'sshd' | grep ':22' | while read line 
    do
        if echo $line | grep -qE $(echo $exclude_ips | tr "," "|"); then
            continue
        else
            pid=$(echo $line | sed -n -r 's/.*pid=([0-9]+).*/\1/p')

            echo "Unusual SSH connection found from:"
            echo $line

            echo "Here are more details about the process with PID: $pid"

            # Information about the process executing file
            echo ""
            sudo ls -l /proc/$pid/exe

            # Information about the process files
            echo ""
            sudo lsof -p $pid

            # Detailed information about the process
            echo ""
            ps -fp $pid

            # Current working directory of the process
            echo ""
            sudo pwdx $pid

            echo "-----------"
        fi
    done

    # Wait for 5 seconds before the next check
    sleep 5
done
`
```

**>>The script has some problem, and here need to remove grep 'sshd'**

```
`    sudo ss -tunp | grep 'sshd' | grep ':22' | while read line 
`
```

**>>So I got some logs**, it seems the nginx have some problem, so no idea what's going on.

```
`-----------
Unusual SSH connection found from:
tcp ESTAB 0 0 165.227.51.176:443 172.71.159.62:22620 users:(("nginx",pid=678521,fd=14))
Here are more details about the process with PID: 678521

lrwxrwxrwx 1 www-data www-data 0 Nov 21 19:11 /proc/678521/exe -> /usr/sbin/nginx

COMMAND    PID     USER   FD      TYPE             DEVICE SIZE/OFF    NODE NAME
nginx   678521 www-data  cwd       DIR              252,1     4096       2 /
nginx   678521 www-data  rtd       DIR              252,1     4096       2 /
nginx   678521 www-data  txt       REG              252,1  1240136  918417 /usr/sbin/nginx
nginx   678521 www-data  mem       REG              252,1   309600  919685 /usr/lib/x86_64-linux-gnu/libnss_systemd.so.2
nginx   678521 www-data  DEL       REG                0,1          6388434 /dev/zero
nginx   678521 www-data  mem       REG              252,1    68552  934912 /usr/lib/x86_64-linux-gnu/libresolv.so.2
nginx   678521 www-data  mem       REG              252,1    22600 1013751 /usr/lib/x86_64-linux-gnu/libkeyutils.so.1.9
nginx   678521 www-data  mem       REG              252,1    52016  921085 /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
nginx   678521 www-data  mem       REG              252,1    18504 1013745 /usr/lib/x86_64-linux-gnu/libcom_err.so.2.1
nginx   678521 www-data  mem       REG              252,1   182864  918286 /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
nginx   678521 www-data  mem       REG              252,1   827936  922399 /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
nginx   678521 www-data  mem       REG              252,1   338648  918905 /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
nginx   678521 www-data  mem       REG              252,1   182912 1013742 /usr/lib/x86_64-linux-gnu/libtirpc.so.3.0.0
nginx   678521 www-data  mem       REG              252,1    93280  928845 /usr/lib/x86_64-linux-gnu/libnsl.so.2.0.1
nginx   678521 www-data  mem       REG              252,1    55808 1013736 /usr/lib/x86_64-linux-gnu/libnss_nis.so.2.0.0
nginx   678521 www-data  mem       REG              252,1    44024  934900 /usr/lib/x86_64-linux-gnu/libnss_compat.so.2
nginx   678521 www-data  mem       REG              252,1  2216304  923246 /usr/lib/x86_64-linux-gnu/libc.so.6
nginx   678521 www-data  mem       REG              252,1   108936  918017 /usr/lib/x86_64-linux-gnu/libz.so.1.2.11
nginx   678521 www-data  mem       REG              252,1  4451632  921043 /usr/lib/x86_64-linux-gnu/libcrypto.so.3
nginx   678521 www-data  mem       REG              252,1   667864  921044 /usr/lib/x86_64-linux-gnu/libssl.so.3
nginx   678521 www-data  mem       REG              252,1   477296 1013769 /usr/lib/x86_64-linux-gnu/libpcre.so.3.13.3
nginx   678521 www-data  mem       REG              252,1   198664 1013758 /usr/lib/x86_64-linux-gnu/libcrypt.so.1.1.0
nginx   678521 www-data  mem       REG              252,1   240936  918569 /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2
nginx   678521 www-data  DEL       REG                0,1          6388435 /dev/zero
nginx   678521 www-data    0u      CHR                1,3      0t0       5 /dev/null
nginx   678521 www-data    1u      CHR                1,3      0t0       5 /dev/null
nginx   678521 www-data    2w      REG              252,1    73824  393461 /var/log/nginx/error.log
nginx   678521 www-data    3u     IPv4            3635152      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.23.194:11840 (ESTABLISHED)
nginx   678521 www-data    4w      REG              252,1    73824  393461 /var/log/nginx/error.log
nginx   678521 www-data    5u     unix 0xffff92c3c4199dc0      0t0 3609748 type=STREAM
nginx   678521 www-data    6u     IPv4            2914913      0t0     TCP *:http (LISTEN)
nginx   678521 www-data    7u     IPv4            2914914      0t0     TCP *:https (LISTEN)
nginx   678521 www-data    8u     IPv6            2914915      0t0     TCP *:http (LISTEN)
nginx   678521 www-data    9u  a_inode               0,14        0   12477 [eventpoll]
nginx   678521 www-data   10w      REG              252,1  4306893  393353 /var/log/nginx/access.log
nginx   678521 www-data   11u  a_inode               0,14        0   12477 [eventfd]
nginx   678521 www-data   12u     IPv4            3660000      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.23.203:46174 (ESTABLISHED)
nginx   678521 www-data   13u     IPv4            3660003      0t0     TCP localhost:35822->localhost:21307 (ESTABLISHED)
nginx   678521 www-data   14u     IPv4            3640297      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.71.159.62:22620 (ESTABLISHED)
nginx   678521 www-data   15u     IPv4            3645173      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-39-69.ap-southeast-1.compute.amazonaws.com:12852 (ESTABLISHED)
nginx   678521 www-data   16u     IPv4            3649346      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-50-166.ap-southeast-1.compute.amazonaws.com:50742 (ESTABLISHED)
nginx   678521 www-data   17u     IPv4            3633140      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-28-172.ap-southeast-1.compute.amazonaws.com:23546 (ESTABLISHED)
nginx   678521 www-data   18u     IPv4            3652681      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.71.158.175:27534 (ESTABLISHED)
nginx   678521 www-data   19u     IPv4            3653597      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-36-192.ap-southeast-1.compute.amazonaws.com:51360 (ESTABLISHED)
nginx   678521 www-data   20u     IPv4            3638677      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-39-92.ap-southeast-1.compute.amazonaws.com:11358 (ESTABLISHED)
nginx   678521 www-data   21u     IPv4            3654651      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->162.158.166.240:44088 (ESTABLISHED)
nginx   678521 www-data   22u     IPv4            3656031      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.22.188:59364 (ESTABLISHED)
nginx   678521 www-data   23u     IPv4            3640664      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-39-8.ap-southeast-1.compute.amazonaws.com:32148 (ESTABLISHED)
nginx   678521 www-data   24u     IPv4            3634798      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-18-196.ap-southeast-1.compute.amazonaws.com:30886 (ESTABLISHED)
nginx   678521 www-data   25u     IPv4            3658718      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-27-156.ap-southeast-1.compute.amazonaws.com:48594 (ESTABLISHED)
nginx   678521 www-data   26u     IPv4            3614112      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.23.107:10872 (ESTABLISHED)
nginx   678521 www-data   27u     IPv4            3628738      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.23.177:26760 (ESTABLISHED)
nginx   678521 www-data   28u     IPv4            3614113      0t0     TCP localhost:41336->localhost:21307 (ESTABLISHED)
nginx   678521 www-data   34u     IPv4            3635046      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.71.159.28:44026 (ESTABLISHED)
nginx   678521 www-data   36u     IPv4            3636306      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.22.39:54134 (ESTABLISHED)
nginx   678521 www-data   37u     IPv4            3636307      0t0     TCP localhost:32820->localhost:21307 (ESTABLISHED)
nginx   678521 www-data   38u     IPv4            3636503      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.23.89:41840 (ESTABLISHED)
nginx   678521 www-data   39u     IPv4            3637091      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->ec2-47-128-39-81.ap-southeast-1.compute.amazonaws.com:44492 (ESTABLISHED)
nginx   678521 www-data   40u     IPv4            3643796      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.134.181:61650 (ESTABLISHED)
nginx   678521 www-data   43u     IPv4            3636519      0t0     TCP pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:https->172.69.134.83:63856 (ESTABLISHED)

UID          PID    PPID  C STIME TTY          TIME CMD
www-data  678521  537882  0 19:01 ?        00:00:00 nginx: worker process

678521: /
-----------`
```