import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from pydantic import SecretStr


def create_groq_model(model: str = "qwen/qwen3-32b"):
    """
    Helper to create a model.

    Args:
        model (str): model name. (e.g. llama-3.1-8b-instant, llama-3.3-70b-versatile, qwen/qwen3-32b, openai/gpt-oss-20b, openai/gpt-oss-120b)
    """

    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    api_key = SecretStr(os.environ.get("GROQ_API_KEY", ""))

    if not api_key.get_secret_value():
        raise Exception("GROQ_API_KEY environment variable not set")

    return ChatGroq(model=model)


def main():
    """"""
    model = create_groq_model()
    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = model.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    main()
