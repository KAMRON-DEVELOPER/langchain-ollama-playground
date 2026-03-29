from src.integrations.ollama.model import create_ollama_model


def invocation():
    r"""
    Demonstrates basic LLM invocation with a system and human message.

    Sends a simple system and user message to the model and prints
    the generated response. This example does not involve tools,
    reasoning mode, or multimodal input — it is intended to show
    the minimal request/response workflow.
    """
    model = create_ollama_model(model="granite3.1-moe:3b")

    messages = [
        ("system", "You are a helpful assistant"),
        ("human", "what is Rust programming language?"),
    ]
    ai_msg = model.invoke(messages)
    print(ai_msg.content)
