---
title: "Time to enable https--letsencrypt"
date: 2017-11-30
author: pengjianqing
categories: ['Linux']
tags: ['https', 'ssl']
---

It's almost at the end of Year 2017, now it's time to enable https for my website, after some search, I choose to use letsencrypt, it's free and community support widely. So it's easy for me to find the [tutorials](https://certbot.eff.org/#ubuntuxenial-nginx).

![](data:image/png;base64,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)

So now you can visit my wiki, and it will be force redirect to the [https link](https://wiki.pjq.me)

**How to install**

**Solution #1**

```
sudo apt-get install letsencrypt
sudo service nginx stop
sudo letsencrypt certonly --standalone
sudo service nginx restart

```

**Solution #2**

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx

```

**Refer**
https://bitmingw.com/2017/02/02/letsencrypt-tutorial/
https://github.com/certbot/certbot
https://certbot.eff.org/#ubuntuxenial-nginx

**nginx config**

```
server {
listen 80;
server_name ef.pjq.me;
return 301 https://$server_name$request_uri;
}

server {
listen 80;
server_name wiki.pjq.me;
return 301 https://$server_name$request_uri;
}
server {
listen 443;
server_name ef.pjq.me;
ssl on;
ssl_certificate /etc/letsencrypt/live/ef.pjq.me/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/ef.pjq.me/privkey.pem;
ssl_session_timeout 5m;
root /var/www/ef/;
index index.html index.htm index.php;
location / {
try_files $uri $uri/ =404;
autoindex on;
}
location ~ \.php$ {
try_files $uri =404;
fastcgi_pass unix:/run/php/php7.0-fpm.sock;
fastcgi_index index.php;
fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
include fastcgi_params;

}
location ~ \.php$ {
fastcgi_split_path_info ^(.+\.php)(/.+)$;
fastcgi_pass unix:/var/run/php5-fpm.sock;
fastcgi_index index.php;
include fastcgi_params;
}
}
server {
listen 443;
root /var/www/dokuwiki/wiki/;
index index.html index.htm index.php;
server_name wiki.pjq.me;
ssl on;
ssl_certificate /etc/letsencrypt/live/ef.pjq.me/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/ef.pjq.me/privkey.pem;
ssl_session_timeout 5m;
location / {
try_files $uri $uri/ =404;
}
location ~ /(data|conf|bin|inc)/ {
deny all;
}
location ~ \.php$ {
fastcgi_pass unix:/run/php/php7.0-fpm.sock;
fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
fastcgi_index index.php;
include fastcgi_params;
}
location ~ /\.ht {
deny all;
}
}

```

```
**Wildcard support **
Letsencypt already support wildcard, reference [https://www.jianshu.com/p/c5c9d071e395](https://www.jianshu.com/p/c5c9d071e395)
```

```
`sudo certbot certonly -d *.pjq.me -d pjq.me --manual  --server https://www.jianshu.com/p/c5c9d071e395https://acme-v02.api.letsencrypt.org/directory`
```

```
`pjq@pjqmes1vcpu1gbsfo2-s-1vcpu-1gb-sfo2-01:~$ sudo certbot certonly -d *.pjq.me --manual  --server https://acme-v02.api.letsencrypt.org/directory
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator manual, Installer None
Obtaining a new certificate
Performing the following challenges:
dns-01 challenge for pjq.me

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NOTE: The IP of this machine will be publicly logged as having requested this
certificate. If you're running certbot in manual mode on a machine that is not
your server, please ensure you're okay with that.

Are you OK with your IP being logged?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name
_acme-challenge.pjq.me with the following value:

QuTEKz6IaSk6xc_AAiTp47cNXXTps9wJZp1jViV9jTY

Before continuing, verify the record is deployed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
Waiting for verification...
Cleaning up challenges

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/pjq.me/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/pjq.me/privkey.pem
   Your cert will expire on 2020-03-01. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le`
```