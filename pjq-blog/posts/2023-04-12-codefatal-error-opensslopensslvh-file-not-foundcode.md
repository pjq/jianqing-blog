---
title: "<code>fatal error: 'openssl/opensslv.h' file not found</code>"
date: 2023-04-12
author: pengjianqing
categories: ['Tech']
---

brew install openssl 

env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" pip install cryptography