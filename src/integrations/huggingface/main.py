import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


def main():
    """"""

    api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

    if not api_token:
        print("HUGGINGFACEHUB_API_TOKEN environment variable not set")
        return

    repo_id = "Qwen/Qwen3.5-27B"

    llm = HuggingFaceEndpoint(
        model="", repo_id=repo_id, task="text-generation", provider="auto"
    )

    chat_model = ChatHuggingFace(llm=llm)

    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = chat_model.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    main()
