import json
from dataclasses import dataclass, field

from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import ToolRuntime, tool
from src.integrations.ollama.llm import get_llm
from src.tools.get_weather import get_weather

SYSTEM_PROMPT = """
You are a weather assistant.

Use tools to answer weather questions.
- If a user asks about weather, call get_weather.
- If no city is mentioned, call get_user_location first.

IMPORTANT: Always return your final answer by calling the `ResponseSchema` tool.
Never return a plain text response.
Do not answer from memory.
"""


@dataclass
class Context:
    """Custom runtime context schema."""

    user_id: str


@dataclass
class ResponseSchema:
    """Response schema for the agent."""

    response: str
    city: str = ""
    country: str = ""
    temperature_c: str = ""
    feels_like_c: str = ""
    conditions: str = ""
    humidity: str = ""
    wind: str = ""
    forecast: list[str] = field(default_factory=list)


@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve the user's city based on their user ID."""
    user_id = runtime.context.user_id
    return "Tashkent" if user_id == "1" else "Beruniy"


checkpointer = InMemorySaver()


def basic_agent():
    llm = get_llm(
        model="qwen3.5:4b",
        temperature=0,
        validate_model_on_init=True,
        num_gpu=0,
    )

    agent = create_agent(
        model=llm,
        context_schema=Context,
        checkpointer=checkpointer,
        system_prompt=SYSTEM_PROMPT,
        tools=[get_user_location, get_weather],
        response_format=ToolStrategy(ResponseSchema),
    )

    # `thread_id` is a unique identifier for a given conversation.
    cfg: RunnableConfig = {"configurable": {"thread_id": "1"}}
    ctx = Context(user_id="1")

    res = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "What is the current weather in Tashkent?"},
            ]
        },
        config=cfg,
        context=ctx,
    )

    print("res: ", json.dumps(res, indent=4))
    print("structured_response: ", json.dumps(res.get("structured_response"), indent=4))

    # Note that we can continue the conversation using the same `thread_id`.
    # res = agent.invoke(
    #     {"messages": [HumanMessage(content="thank you!")]},
    #     config=cfg,
    #     context=ctx,
    # )

    # pprint(res)
    # pprint(res.get("structured_response"))
