from langchain_core.messages import ChatMessage, HumanMessage

from src.integrations.ollama.model import create_ollama_model


def reasoning():
    r"""
    Demonstrates thinking/reasoning mode using a custom message role.

    To enable thinking on supported models, pass a `ChatMessage` with role
    set to `"control"` and content set to `"thinking"`. Since `"control"` is a
    non-standard message role, `ChatMessage` is used instead of `HumanMessage`
    or `SystemMessage`.
    """
    llm = create_ollama_model(model="nemotron-3-nano:4b")

    messages = [
        ChatMessage(role="control", content="thinking"),
        HumanMessage("What is 3^3?"),
    ]

    res = llm.invoke(messages)
    print(res.content)
