---
title: "Square and Multiply"
date: 2024-11-26
author: pengjianqing
categories: ['Cryptography', 'Tech']
tags: ['Asymmetric Encryption', 'Cryptography', 'RSA']
---

在密码学中经常看到a^b mod n运算，当b很大的时候，就不能够按照简单的数学运算进行了。

"Square and Multiply"就是一种窍门。

把指数转换成2进制，从左到右开始计算

- 当指数二进制为1时 z^2*a mod n

- 当指数二进制为0时 z^2 mod n

其中z为上一个指数二进制计算结果(从左到右)，初始为1

举例a^b mod 21 = 3^11 mod 21 = 3^1011 mod 21

- z = 1

- z = z^2*a = 1^2 * 3 mod 21 = 3

- z = z^2 mod n = 3^2 mod 21 = 9

- z = z^2 mod n = 9^2 * 3 mod 21 = 12

- z= z^2 *a mod n = 12^2 * 3 mod 21 = 12

所以最终结果:3^11 mod 21 = 12

当然这种方式也存在一些安全问题 - Power consumption of an RSA decryption

- [https://www.chegg.com/homework-help/questions-and-answers/716-let-us-investigate-side-channel-attacks-rsa-simple-imple-mentation-rsa-without-counter-q74047610#question-transcript](https://www.chegg.com/homework-help/questions-and-answers/716-let-us-investigate-side-channel-attacks-rsa-simple-imple-mentation-rsa-without-counter-q74047610#question-transcript)

Reference

- https://scientia-potentia-est.com/zh/square-multiply-algorithm/