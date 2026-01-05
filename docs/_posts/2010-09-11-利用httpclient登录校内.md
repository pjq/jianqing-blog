---
title: "利用HttpClient登录校内"
date: 2010-09-11
author: pengjianqing
categories: ['Java']
tags: ['github', 'HttpClient', 'Java', 'Xiaonei']
---

利用HttpClient登录校内
[Google Doc](https://docs.google.com/document/pub?id=1VjfaANgQu7BOWNOm6acOQLeC-fHqcCOmjPkD2WGjz1I)

先抄录一段简介:

> HttpClient简介
HTTP 协议可能是现在 Internet 上使用得最多、最重要的协议了，越来越多的 Java 应用程序需要直接通过 HTTP 协议来访问网络资源。虽然在 JDK 的 java.net 包中已经提供了访问 HTTP 协议的基本功能，但是对于大部分应用程序来说，JDK 库本身提供的功能还不够丰富和灵活。HttpClient 是 Apache Jakarta Common 下的子项目，用来提供高效的、最新的、功能丰富的支持 HTTP 协议的客户端编程工具包，并且它支持 HTTP 协议最新的版本和建议。

网上有大量关于HttpClient的信息,这里就不做介绍了.

回到本文重点,
**1.如何利用HttpClient登录校内网?**

由于我们要利用HttpClient的特性模仿Browser的登录流程,那自然第一步就是要得到Browser登录校内的具体流程了.
这个流程要怎么得到呢?这就要感谢强大的wireshark分析功能了,利用它可以很轻松的抓取登录时的网络数据包.如何使用wireshark,不是本文重点,网上有大量教程,这里简单说下:Capture->Option->Capture Filter:填入host  youripaddress(这是最简单的,会抓取所有的数据包)然后start就可以了.抓取完了之后,选中某一条记录右键->Follow Tcp Stream,就可以看到这次网络数据包的具体信息了.

下图是我抓到的校内登录过程:
[![BrowserLoginXiaonei](http://farm5.static.flickr.com/4133/4979158780_7a79af72d6.jpg)](http://www.flickr.com/photos/pengjianqing/4979158780/)

Login只是一个POST数据的过程,POST的数据包含```
email,password,originURL,domain
```
这四个参数,那我们只要在利用HttpClient POST数据时,依照这个样子把参数设置进去就行了:
```

HttpPost httpPost = new HttpPost(loginUri);
       List nvp = new ArrayList();
       nvp.add(new BasicNameValuePair("email", username));
       nvp.add(new BasicNameValuePair("password", password));
       nvp.add(new BasicNameValuePair("originUrl", originUrl));
       nvp.add(new BasicNameValuePair("domain", domain));
       httpPost.setEntity(new UrlEncodedFormEntity(nvp, HTTP.UTF_8));

```

然后用httpClient.execute执行这次Post:```

           HttpResponse response = httpClient.execute(httpPost);
```

这样就完成了一次完整的Login过程,之后可以根据response实据情况再做处理:
在这里它返回了302 Found,表示要再次打开另外一个页面,也就是上图Header 中Location对应的值(Uri).
之后我们可以再利用HttpGet获取这个Uri中的内容,里面应该就是你登录后,看到的内容,只是我们得到的是Html源码文件.

至此我们已经完成了利用HttpClient登录校内的过程,接下来你是不是会想,既然已经登录了,那是不是可以继续做一些事情呢?比如说更新一个状态.
**2.如何更新状态**

既然想到了这里,还是老办法,利用wireshark抓取Browser更新状态的数据包.
下图是我抓到的一个数据包,更新状态内容为:testabcdefg
[![BrowserPostToXiaonei](http://farm5.static.flickr.com/4107/4979158784_c2770dae32.jpg)](http://www.flickr.com/photos/pengjianqing/4979158784/)

这里面共带了4个参数:```
c,raw,publisher_form_ticket,requestToken
```

其中c=raw,publisher_form_ticket=requestToken,这两个值为什么会相等,这个我就不得而知了.
这其中的ticket是什么参数呢,从哪个地方可以得到呢?
你对你的Browser点右键,查看网页源代码,把抓到的这个ticket在上面搜索下就可以找到了,既然在网页源码里面可以找到,那我们自然是先要抓取这个网页源码得到ticket才后进行下一步操作.
需要抓取的网页源码就是在Login时看到的Location后面的uri,把这个uri内容抓下来,然后再找到ticket就好了.
```

    HttpGet httpGet = new HttpGet(uri);

           try {
               HttpResponse response = httpClient.execute(httpGet);
               Log.e(tag, "" + response.getStatusLine());
               HttpEntity httpEntity = response.getEntity();

               if (null != httpEntity) {
                   String entity = EntityUtils.toString(httpEntity);

                   ticket = getTicket(entity);
                   Log.e(tag, "ticket=" + ticket);
                   // Log.e(tag, entity);
                   httpEntity.consumeContent();
               }

```

其中getTicket实现为,这个方法不保证长期有效,只能说目前有效,说不定什么时候校内又更新的网页.
```

public static String getTicket(String str) {
       str = str.split("publisher_form_ticket\" value=\"")[1];
       return str.split("\"")[0];
   }

```

得到ticket之后,就可以模拟POST的过程了;
```

HttpPost httpPost = new HttpPost(postStatusUrl);

       List nvp = new ArrayList();
       nvp.add(new BasicNameValuePair("c", status));
       nvp.add(new BasicNameValuePair("raw", status));
       String requestToken = ticket;
       nvp.add(new BasicNameValuePair("publisher_form_ticket", ticket));
       nvp.add(new BasicNameValuePair("requestToken", requestToken));

       try {
           httpPost.setEntity(new UrlEncodedFormEntity(nvp, HTTP.UTF_8));
           HttpResponse httpResponse = httpClient.execute(httpPost);

```

可以将它的结果都打印出来看看:
```

Log.e(tag, "post status finished:" + httpResponse.getStatusLine());

           HttpEntity httpEntity = httpResponse.getEntity();

           if (null != httpEntity) {
               Log.e(tag, EntityUtils.toString(httpEntity));
           }

```

如果能看到类似于下面这样的信息就表示成功了:
```

{"allMsg":"test1234","updateStatusId":1.397876723e9,"dtime":"Sat Sep 11 15:14:57 CST 2010","code":0,"msg":"test1234"}

```

至此我们已经实现了更新状态的功能,我想其它的功能也类似于这样就可以实现了,这时就不做深究了.

我已经将这些测试 源代码放到github上了:
[http://github.com/PercyPeng/sns/tree/](http://github.com/PercyPeng/sns/tree/)
需要的自己clone,直接导入到eclipse就可以了.
main函数入口在SNS.java.