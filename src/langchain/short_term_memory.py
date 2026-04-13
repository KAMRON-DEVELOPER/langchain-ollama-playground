from pprint import pprint
from langgraph.checkpoint.postgres import PostgresSaver
from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver

# from src.integrations.ollama.model import create_ollama_model
from src.integrations.cerebras.main import create_cerebras_model

# from integrations.groq.main import create_groq_model
# from integrations.huggingface.main import create_huggingface_model
# from integrations.openrouter.main import create_openrouter_model

DB_URI = (
    "postgresql://postgres:password@localhost:5432/langchain_ollama?sslmode=disable"
)
with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()  # auto create tables in PostgreSQL
    agent = create_agent(
        "gpt-5",
        checkpointer=checkpointer,
    )


class CustomAgentState(AgentState):
    user_id: str
    preferences: dict


def advanced_agent():
    """"""
    # model = create_ollama_model(model="qwen3.5:4b", temperature=0, num_gpu=0)
    model = create_cerebras_model()
    # model = create_groq_model()
    # model = create_huggingface_model()
    # model = create_openrouter_model()

    agent = create_agent(
        model=model,
        state_schema=CustomAgentState,
        checkpointer=InMemorySaver(),
    )

    input = {
        "messages": [{"role": "user", "content": "Hello"}],
        "user_id": "user_123",
        "preferences": {"theme": "dark"},
    }

    # Custom state can be passed in invoke
    res = agent.invoke(input, {"configurable": {"thread_id": "1"}})  # type: ignore

    pprint(res)
