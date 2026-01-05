---
title: "Build the LLM Agent with Google ADK and self deployed LLM Model"
date: 2025-04-10
author: pengjianqing
categories: ['Tech']
tags: ['ADK', 'Agent', 'AI', 'LLM']
---

Here it shows how we build the LLM Agent with Google ADK(Agent Development Kit), and we integrate it with our own models.

Follow the quick start to setup the project

- https://google.github.io/adk-docs/get-started/quickstart/

And the project structure will be like

```
` tree
.
├── multi_tool_agent
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── __init__.cpython-39.pyc
│   │   ├── agent.cpython-312.pyc
│   │   └── agent.cpython-39.pyc
│   └── agent.py
└── requirements.txt`
```

Install the requirements

```
`cat requirements.txt
google-adk
litellm`
```

```
`pip install -r requirements.txt`
```

Here is the agent.py

```
`import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (41 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}

# Endpoint URL provided
api_base_url = "http://127.0.0.1:3001/v1"

# Model name as specified
model_name = "gpt-4o"

# API Key
api_key = "sk-or-v1-xxxx"

root_agent = LlmAgent(
    name="weather_time_agent",
    model=LiteLlm(
        model=model_name,
        api_base=api_base_url,
        api_key=api_key
    ),
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "I can answer your questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)`
```

## adk debug

Start the Web Application

```
`adk web
INFO:     Started server process [68331]
INFO:     Waiting for application startup.
+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://localhost:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)`
```

![](../images/bc66befe.png)

## Reference

- https://google.github.io/adk-docs/get-started/quickstart/

- https://google.github.io/adk-docs/get-started/tutorial/#step-2-going-multi-model-with-litellm

- https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/