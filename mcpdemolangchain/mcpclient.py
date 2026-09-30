from langchain_mcp_adapters.client import MultiServerMCPClient

from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent

import asyncio


import os
from dotenv import load_dotenv
load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio" 
            },
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable_http",
            }
        }
    )
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")

    tools = await client.get_tools()
    model_name = "claude-haiku-4-5-20251001"

    model = ChatAnthropic(model=model_name)
    agent = create_agent(model , tools)

    math_response = await agent.ainvoke({"messages": [("user", "What is 2+2 ?")]})
    print(math_response["messages"][-1].content)


    weather_response = await agent.ainvoke({"messages":[("user, what is the weather in Hyderabad?")]})
    print(weather_response["messages"][-1].content)

asyncio.run(main())