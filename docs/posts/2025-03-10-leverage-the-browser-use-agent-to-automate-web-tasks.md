---
title: "Leverage the browser-use agent to automate Web tasks."
date: 2025-03-10
author: pengjianqing
categories: ['Tech']
---

Here is one simple demo about using browser-use to automate the Web tasks

- https://github.com/browser-use/browser-use

```
`from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(
        task="Summarize all my tasks in the Jira: https://jira.xxxx, my account: xxxx",
         llm=ChatOpenAI(model="gpt-4o", base_url="http://127.0.0.1:5000/v1", api_key="sk-or"),
    )
    await agent.run()

asyncio.run(main())`
```