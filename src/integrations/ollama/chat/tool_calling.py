from langchain_core.messages import AnyMessage, HumanMessage, ToolMessage

from src.integrations.ollama.main import create_ollama_model
from src.tools.get_weather import get_weather


def tool_calling():
    r"""
    Demonstrates LangChain tool calling with a local Ollama model.

    Flow:

        1. Bind `get_weather` to the LLM via `.bind_tools()`.
        2. Send a user message that should trigger a tool call.
        3. If the model emits `tool_calls`, invoke each tool and append a `ToolMessage` with the result to the conversation history.
        4. Re-invoke the LLM with the full history so it can produce a final natural-language answer grounded in the tool output.
        5. If no tool calls are made, the initial AI response is used directly.
    """

    tools = [get_weather]
    tools_names = {t.name: t for t in tools}

    model = create_ollama_model(
        model="qwen3.5:4b", validate_model_on_init=True, num_gpu=0
    ).bind_tools(tools)

    messages: list[AnyMessage] = [
        HumanMessage(content="What is the current weather in Tashkent?")
    ]

    ai_msg = model.invoke(messages)
    messages.append(ai_msg)

    if ai_msg.tool_calls:
        for tool_call in ai_msg.tool_calls:
            tool_id = tool_call.get("id")
            tool_name = tool_call.get("name")
            tool_args = tool_call.get("args")

            if tool_name in tools_names:
                tool_to_run = tools_names[tool_name]
                tool_output = tool_to_run.invoke(tool_args)

                messages.append(
                    ToolMessage(content=str(tool_output), tool_call_id=tool_id)
                )
            else:
                messages.append(
                    ToolMessage(
                        content=f"Error: Tool {tool_name} does not exist.",
                        tool_call_id=tool_call.get("id"),
                    )
                )
        res = model.invoke(messages)
    else:
        res = ai_msg

    print(res.content)
