import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from pydantic import SecretStr


def main():
    """"""

    api_key = SecretStr(os.environ.get("GROQ_API_KEY", ""))

    if not api_key.get_secret_value():
        print("GROQ_API_KEY environment variable not set")
        return

    llm = ChatGroq(model="qwen/qwen3-32b")

    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = llm.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    main()
