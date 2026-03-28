from src.integrations.ollama.llm import get_llm


def invocation():
    r"""
    Demonstrates basic LLM invocation with a system and human message.

    Sends a simple system and user message to the model and prints
    the generated response. This example does not involve tools,
    reasoning mode, or multimodal input — it is intended to show
    the minimal request/response workflow.
    """

    llm = get_llm(model="granite3.1-moe:3b")

    messages = [
        ("system", "You are a helpful assistant"),
        ("human", "what is Rust programming language?"),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)
