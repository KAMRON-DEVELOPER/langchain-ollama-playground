import os
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


def create_huggingface_model(
    model: str = "",
    repo_id: str | None = "Qwen/Qwen3.5-27B",
    task: str | None = "text-generation",
    provider: str | None = "auto",
):
    """
    Helper to create a model.

    Args:
        repo_id (str | None): Repo to use. If `endpoint_url` is not specified then this needs to given. (e.g. Qwen/Qwen3-8B, Qwen/Qwen3.5-9B, Qwen/Qwen3-32B, Qwen/Qwen3.5-27B, moonshotai/Kimi-K2.5, MiniMaxAI/MiniMax-M2.5, meta-llama/Llama-3.1-8B-Instruct, meta-llama/Llama-3.3-70B-Instruct, openai/gpt-oss-20b, openai/gpt-oss-120b)
        task (str | None): Task to call the model with. Should be a task that returns `generated_text`.
        provider (str | None): Name of the provider to use for inference with the model specified in repo_id. e.g. "cerebras". if not specified, Defaults to "auto" i.e. the first of the
            providers available for the model, sorted by the user's order in https://hf.co/settings/inference-providers.
            available providers can be found in the huggingface_hub documentation.
    """

    dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"
    load_dotenv(dotenv_path)

    api_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

    if not api_token:
        raise Exception("HUGGINGFACEHUB_API_TOKEN environment variable not set")

    llm = HuggingFaceEndpoint(
        model=model, repo_id=repo_id, task=task, provider=provider
    )

    return ChatHuggingFace(llm=llm)


def main():
    """"""
    model = create_huggingface_model()
    messages = [HumanMessage(content="what is Elixir programming language?")]
    res = model.invoke(messages)
    pprint(res.content)


if __name__ == "__main__":
    main()
