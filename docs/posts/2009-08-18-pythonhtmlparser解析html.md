---
title: "Python:HTMLParser,解析html"
date: 2009-08-18
author: pengjianqing
categories: ['Tech']
---

记录一段用HTMLParser解析html的python代码:
```

data = urllib.urlopen('http://10.85.40.153').read()

#data = response.read()
print data

class parseHtml(HTMLParser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        if 'input'.__contains__(tag):
            for name, value in attrs:
                print 'name=%s,value=%s' % (name, value)
                if value.__contains__('Home'):
                    print value
                    print self.get_starttag_text()

parse = parseHtml()
parse.feed(data)

```

![](http://img.zemanta.com/pixy.gif?x-id=57946abf-ee5f-8805-90f7-b1e55e7d4d70)