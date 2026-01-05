---
title: "Nginx Proxy for OpenAI API"
date: 2023-07-27
author: pengjianqing
categories: ['Tech']
tags: ['Nginx', 'OpenAI', 'Proxy']
---

If you want to add the Nginx proxy for OpenAI API

You can use the following nginx configs.

```
` location /v1/chat/completions {
        proxy_pass https://api.openai.com/v1/chat/completions;
        proxy_ssl_name api.openai.com; 
        proxy_ssl_server_name on;
        # Forward all headers
        proxy_pass_request_headers on;
        # proxy_http_version 1.1;
    }`
```

And then restart the Nginx server

```
`sudo nginx -t
sudo systemctl restart nginx
`
```