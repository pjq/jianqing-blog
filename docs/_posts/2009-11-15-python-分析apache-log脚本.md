---
title: "Python 分析apache log脚本"
date: 2009-11-15
author: pengjianqing
categories: ['自由分类']
---

为了统计每个IP的访问次数，偿试着写了一个python脚本，得到前10个访问次数最多的IP：

```

def countstatics(result):
    """Compute the statics."""
    li = result.split('\n')
    l = {}
    for a in set(li):
        l[a] = 0

    for a in li:
        l[a] = l[a] + 1

    print "The uniq ip number is ", len(l)
    return l

def apachelog(path):
    """analyse the apachelog,get the top 10 ip address which visit my server
    """
    print 'analyse the apachelog,get the top 10 ip address which visit my server'
    cmd = 'cut -d " " -f1 ' + path
    result = exec_shell(cmd)
    li = countstatics(result)

    l = ["%s %s" % (k, v) for v, k in li.items() if k > 1000]
    l.sort(cmp=None, key=None, reverse=True)
    #print l
    for i in range(10):
        print l[i]

if __name__ == "__main__":
    print 'main'

    apachelog("/var/log/apache2/access_log")

    print 'finished'

```

运行结果：
main
apachelog
The uniq ip number is  30907
97374 192.168.0.160
8676 59.42.196.130
8313 121.228.230.114
7909 59.49.232.157
7909 221.239.137.161
6130 117.80.191.13
6056 121.227.155.37
5666 119.32.45.219
5633 220.166.172.5
5295 123.124.228.6
finished

访问次数最多的还是本地IP，再接上whois就可以查看详细的信息了。

![](http://img.zemanta.com/pixy.gif?x-id=b25e6a07-8df9-8a37-951d-367ef537afce)