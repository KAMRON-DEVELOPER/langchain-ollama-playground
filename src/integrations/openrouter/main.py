import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openrouter import ChatOpenRouter
from pydantic import SecretStr


def create_openrouter_model(model: str = "nvidia/nemotron-3-super-120b-a12b:free"):
    """
    Helper to create a model.

    Args:
        model (str): Same as model_name. (e.g. nvidia/nemotron-3-super-120b-a12b:free, stepfun/step-3.5-flash:free, arcee-ai/trinity-mini:free, minimax/minimax-m2.5:free, openai/gpt-oss-20b:free, openai/gpt-oss-120b:free, meta-llama/llama-3.3-70b-instruct:free, google/gemma-3-27b-it:free)
    """

    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    api_key = SecretStr(os.environ.get("OPENROUTER_API_KEY", ""))

    if not api_key.get_secret_value():
        raise Exception("OPENROUTER_API_KEY environment variable not set")

    # Go to https://openrouter.ai/workspaces/default/guardrails and
    # toggle off `Always Enforce Allowed` or add the provider to `Allowed Providers`
    return ChatOpenRouter(
        model=model,
        openrouter_provider={
            "sort": "throughput",
            "data_collection": "allow",
            "allow_fallbacks": True,
        },
    )


def main():
    """"""
    model = create_openrouter_model()
    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = model.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    main()
