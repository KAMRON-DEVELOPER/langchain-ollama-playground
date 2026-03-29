from langchain_ollama import ChatOllama


def create_ollama_model(
    model: str,
    temperature: float | None = None,
    reasoning: bool | str | None = None,
    validate_model_on_init: bool = False,
    num_gpu: int | None = None,
):
    r"""
    Helper to create a model.

    Args:
        model (str): Model name to use.
        temperature (float | None): The temperature of the model.  Increasing the temperature will make the model answer more creatively.  (Default: 0.8)
        reasoning (bool | str | None): Controls the reasoning/thinking mode for [supported models](https://ollama.com/search?c=thinking).

            - `True`: Enables reasoning mode. The model's reasoning process will be
                captured and returned separately in the `additional_kwargs` of the
                response message, under `reasoning_content`. The main response
                content will not include the reasoning tags.

            - `False`: Disables reasoning mode. The model will not perform any reasoning,
                and the response will not include any reasoning content.

            - `None` (Default): The model will use its default reasoning behavior. Note
                however, if the model's default behavior *is* to perform reasoning, think tags
                (`<think>` and `</think>`) will be present within the main response content
                unless you set `reasoning` to `True`.

            - `str`: e.g. `'low'`, `'medium'`, `'high'`. Enables reasoning with a custom
                intensity level. Currently, this is only supported `gpt-oss`.
        validate_model_on_init (bool): Whether to validate the model exists in Ollama locally on initialization.
        num_gpu (int | None): The number of GPUs to use.

    """
    return ChatOllama(
        model=model,
        temperature=temperature,
        reasoning=reasoning,
        validate_model_on_init=validate_model_on_init,
        num_gpu=num_gpu,
    )
