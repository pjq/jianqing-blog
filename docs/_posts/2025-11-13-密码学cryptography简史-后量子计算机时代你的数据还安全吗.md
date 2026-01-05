---
title: "密码学(Cryptography)简史--后量子计算机时代你的数据还安全吗"
date: 2025-11-13
author: pengjianqing
categories: ['Cryptography', 'Tech']
tags: ['AES', 'Asymmetric', 'Cryptography', 'DH', 'ECC', 'PQC', 'RSA', 'Symmetric']
---

最近可能大家也看到了一些关于量子计算机进展的新闻，比如Google 推出「量子迴聲」算法，量子计算机实际应用里程碑

- https://blog.google/intl/zh-tw/company-news/technology/quantum-echoes-willow-verifiable-quantum-advantage/

当看到这些新闻的时候，你是否心里再想真厉害，量子计算机能够实现指数级的运算速度的提升。

所以呢，人类最近一直在想办法解决量子计算机发展对加密算法的威胁。

但量子计算机对哪些加密算法有威胁呢？估计没有多少人能说的清楚。

首先我们要知道量子计算机和传统计算机不一样，计算速度能够指数级提升，那对于破解我们现在的加密算法，是否也能指数级提升？

要回答这个问题，我们要一步步展开讲。

## 对称加密和非对称加密

我们先要有个概念，我们加密算法一般分为对称加密和非对称加密，使用的原理不一样，具体操作过程先放到一边。

对称加密，比如AES，基于各种替换转换操作(SPN)

- AES - ECB

- AES - CBC

- AES - CTR

- AES - GCM

非对称加密，比如

- RSA， 数学原理基于大整数的因式分解

- DH，基于离散对数难解问题(DLP)

- ECC，基于椭圆曲线难解问题

所以非对称加密算法基本都是基于一些难解的数学问题，而刚好这些问题有可能被某些量子计算机算法破解。

## Shor算法

Shor算法，详见维斯百科，1994年发明

- https://en.wikipedia.org/wiki/Shor%27s_algorithm

我们都说量子计算机对加密算法有威胁，这个威胁其实就是来自于Shor算法。

具体的算过程我也看不懂，但简单来说这个算法可以在量子计算机上快速计算大整数的因式分解，也就是RSA基于的两个大整数(质数)p, q相乘得到N = p * q, 当知道N的情况下无法推导出p, q。

所以我们对照上面的密码学中的非对称加密，就能知道，Shor算法对于非对称加密有很大的危险，而对于对称加密威胁并没有那么大，所以AES还是安全的。

因此非对称加密的这些算法，RSA, DH, ECC，在Shor算法下处于很危险的地步，需要换掉。

## Grover算法

Grover算法也是一种量子计算的算法，1996年发明，它确实对对称加密算法AES造成了威胁。

威胁的原因是它可以导致AES的密钥长度有效性减半，我们知道AES有3种长度的密钥

- AES - 128

- AES - 192

- AES - 256

所以用上Grover算法后，它的长度有效性会变为

- 2^128 -> 2^64，降为64位安全

- 2^192 -> 2^96 ，仍然安全

- 2^256 -> 2^128，非常安全

所以我们可以看到，虽然有量子计算机+Grover算法的加持，目前AES-192，  AES-256仍然是很安全的。

## 后量子计算机时代(PQC)

后量子计算机时代加密算法(Post Quantum Cryptography=PQC), 基于上面这些量子算法的危险应运而生。

- https://csrc.nist.gov/projects/post-quantum-cryptography

所以美国NIST在2017年发起全球挑战，在全球范围内征集PQC时代加密算法，经过多轮比拼，最终在今年2025年3月11日选定了PQC时代加密算法。

> 

***HQC was selected for standardization on March 11, 2025. NIST IR 8545, [Status Report on the Fourth Round of the NIST Post-Quantum Cryptography Standardization Process](https://csrc.nist.gov/pubs/ir/8545/final) is now available.***

[***FIPS 203, FIPS 204 and FIPS 205***](https://csrc.nist.gov/publications/fips)***, which specify algorithms derived from CRYSTALS-Dilithium, CRYSTALS-KYBER and SPHINCS+, were ******published August 13, 2024******. ***

目前一些大公司已经开始在使用这些抗量子机的加密算法了。

所以PQC时代的这些加密算法，主要是用来解决非对称加密算法易被量子计算机破解的问题，比如非对称加密经常用到的是密钥协商(DH), 数字签名(RSA)，还有ECC等就需要用这些新的算法进行替换。

算法名称 (曾用名) 标准号解决的主要问题算法基础**ML-KEM** (CRYSTALS-Kyber)FIPS 203**通用加密/密钥协商**：保护网络流量和存储数据的机密性。基于格（Lattice-based）**ML-DSA** (CRYSTALS-Dilithium)FIPS 204**数字签名**：用于身份验证和确保数据完整性（例如远程签署文件）。基于格（Lattice-based）**SLH-DSA** (SPHINCS+)FIPS 205**数字签名**：提供基于哈希函数的备选方案，作为基于格的数字签名的补充备份。基于哈希（Hash-based）

总结就是基于这些数学难解问题发明的算法需要进行更新替换，而对称加密AES，因为加密过程是经常各种转换操作反而没有受到太多影响，就感觉很神奇。

## 我们可以做什么呢

其实对我们普通人来说，在后量子计算机时代，我们只要跟着大佬就行，大佬说需要更新算法了就去更新好了，密码长度长一些复杂一些，让爆破难度增加一些。

之前国内有科学家说可以破解RSA，这里是有一个限制的，就是RSA整数长度，我们现在的RSA长度都是需要1024及以上，而上海大学破解的只是50位的。

量子计算机里面有个概念叫物理量子比特(Physical Qubits), 这个数量长度越多，说明计算机越厉害。而量子比特的稳定性是目前最大挑站之一。所以什么时候人类能够让更多的量子比特稳定，然后位数又多，那我们现在用到的这些非对称加密算法的末日也就到头了。当然目前还是有很长的路要走，但威胁确实是一步步的在接近。

在这个网站上我们能够看到最近到2030年之前密钥长度推荐

- https://www.keylength.com/en/compare/

可以看到ECC还是很厉害的，256位可以达到RSA 3072位的密码强度。

![](../images/10b1b42c.png)

看了上面的介绍，希望大家能够一下后量子计算机时代加密算法到底意味着什么，也不用慌，魔高一尺，道高一丈，循环迭代，螺旋式上升，应该还是人类在密码学领域不断演进的方式。

所以说谁用量子计算机破解了加密算法，那就是耍流氓，一定要上限制，比如某种加密算法，密钥长度多少，毕竟如果密钥长度很短的话，现有的计算机一样可以破解的。