import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras
from langchain_core.messages import HumanMessage
from pydantic import SecretStr


def create_cerebras_model(model: str = "llama-3.1-8b"):
    """
    Helper to create a model.

    Args:
        model (str): Same as model_name. (e.g. llama-3.1-8b, gpt-oss-120b, qwen-3-235b-a22b-instruct-2507)
    """

    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    api_key = SecretStr(os.environ.get("CEREBRAS_API_KEY", ""))

    if not api_key.get_secret_value():
        raise Exception("CEREBRAS_API_KEY environment variable not set")

    return ChatCerebras(model=model)


def main():
    """"""
    model = create_cerebras_model()
    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = model.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    main()
