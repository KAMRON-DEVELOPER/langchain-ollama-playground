import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openrouter import ChatOpenRouter
from pydantic import SecretStr


def main():
    """"""

    api_key = SecretStr(os.environ.get("OPENROUTER_API_KEY", ""))

    if not api_key.get_secret_value():
        print("OPENROUTER_API_KEY environment variable not set")
        return

    # Go to https://openrouter.ai/workspaces/default/guardrails and
    # toggle off `Always Enforce Allowed` or add the provider to `Allowed Providers`
    llm = ChatOpenRouter(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        openrouter_provider={
            "sort": "throughput",
            "data_collection": "allow",
            "allow_fallbacks": True,
        },
    )

    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = llm.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    main()
