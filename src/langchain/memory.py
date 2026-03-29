from pprint import pprint

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import AgentMiddleware
from src.integrations.ollama.model import create_ollama_model


class CustomState(AgentState):
    user_preferences: dict


class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState


def memory():
    model = create_ollama_model(
        model="qwen3.5:9b",
        temperature=0,
        num_gpu=0,
    )

    agent = create_agent(
        model=model,
        middleware=[CustomMiddleware()],
    )

    res = agent.invoke(
        {
            "messages": [{"role": "user", "content": "what is Go?"}],
            "user_preferences": {"style": "technical", "verbosity": "detailed"},
        }  # type: ignore
    )

    pprint(res)
    pprint(res.get("structured_response"))
