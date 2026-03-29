from pprint import pprint
from typing import Annotated, cast

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import AgentMiddleware
from langchain.messages import AIMessage, HumanMessage
from src.integrations.ollama.main import create_ollama_model


class CustomState(AgentState):
    messages: Annotated[list[AnyMessage], add_messages]
    user_preferences: dict


class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState


def streaming():
    model = create_ollama_model(model="qwen3.5:4b", temperature=0, num_gpu=0)
    agent = create_agent(model=model, middleware=[CustomMiddleware()])

    input: CustomState = {
        "messages": [
            HumanMessage(content="what is jQuery?"),
        ],
        "user_preferences": {"style": "technical", "verbosity": "detailed"},
    }

    for chunk in agent.stream(input, stream_mode="values"):  # type: ignore
        state = cast(CustomState, chunk)
        messages = state.get("messages", [])

        if not messages:
            continue

        latest_message = messages[-1]

        if isinstance(latest_message, HumanMessage):
            if latest_message.content:
                pprint(f"User: {latest_message.content}")

        elif isinstance(latest_message, AIMessage):
            if latest_message.content:
                pprint(f"Agent: {latest_message.content}")

            if latest_message.tool_calls:
                tool_names = [tc.get("name") for tc in latest_message.tool_calls]
                pprint(f"Calling tools: {tool_names}")
