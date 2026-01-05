---
title: "如何把SAP AI Core 接入Cursor"
date: 2024-09-07
author: pengjianqing
categories: ['Tech', 'Uncategorized']
tags: ['AI', 'Cursor']
---

## SAP AI Core 接入Cursor

估计这是全网第一篇把SAP AI Core 接入Cursor 的教程。

教程很简单，按照下面项目README，跑一个本地AI Core LLM 代理服务器

- [https://github.com/pjq/sap-ai-core-llm-proxy](https://github.com/pjq/sap-ai-core-llm-proxy)

```
`http://127.0.0.1:5000`
```

接着找一台有公网IP的电脑，注册绑定好域名，在Nginx设置好反向代理

比如 https://ai-proxy

然后在Cursor 设置自定义Open AI URL

```
`https://ai-proxy/v1`
```

这个代理服务器是手工搓的，目前支持gpt-4,gpt-4o, Claude 3.5 sonnet 统一了OpenAI API协议，所以可以用到任何兼容OpenAI API 的客户端。

至此，Token自由。

## SAP AI Core LLM Proxy 介绍

`[sap-ai-core-llm-proxy](https://github.com/pjq/sap-ai-core-llm-proxy)` is a Python-based project that includes functionalities for token management, forwarding requests to the SAP AI Core API, and handling responses. The project uses Flask to implement the proxy server.

Now it support the following LLM models

- OpenAI: gpt-4o,gpt-4,gpt-4-32k

- Claude: anthropic--claude-3.5-sonnet

### Features[](https://github.com/pjq/sap-ai-core-llm-proxy#features)

- **Token Management**: Fetch and cache tokens for authentication.

- **Proxy Server**: Forward requests to the AI API with token management.

- **Model Management**: List available models and handle model-specific requests