from pprint import pprint
from typing import Annotated, cast

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

from src.integrations.cerebras.main import create_cerebras_model

# from integrations.groq.main import create_groq_model
# from integrations.huggingface.main import create_huggingface_model
# from integrations.openrouter.main import create_openrouter_model
from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import AgentMiddleware
from langchain.messages import AIMessage, HumanMessage

# from src.integrations.ollama.model import create_ollama_model


class CustomState(AgentState):
    messages: Annotated[list[AnyMessage], add_messages]
    user_preferences: dict


class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState


def streaming():
    """"""
    # model = create_ollama_model(model="qwen3.5:4b", temperature=0, num_gpu=0)
    model = create_cerebras_model()
    # model = create_groq_model()
    # model = create_huggingface_model()
    # model = create_openrouter_model()

    agent = create_agent(model=model, middleware=[CustomMiddleware()])

    input: CustomState = {
        "messages": [
            HumanMessage(content="I like Dart programming language. Do you know why?"),
        ],
        "user_preferences": {"style": "technical", "verbosity": "detailed"},
    }

    # The agent can now track additional state beyond messages
    res = cast(CustomState, agent.invoke(input))  # type: ignore
    messages = res.get("messages", [])

    for msg in messages:
        print_message(msg)

    input = {
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
        print_message(latest_message)


def print_message(msg: AnyMessage):
    if isinstance(msg, HumanMessage):
        if msg.content:
            pprint(f"User: {msg.content}")

    elif isinstance(msg, AIMessage):
        if msg.content:
            pprint(f"Agent: {msg.content}")

        if msg.tool_calls:
            tool_names = [tc.get("name") for tc in msg.tool_calls]
            pprint(f"Calling tools: {tool_names}")
