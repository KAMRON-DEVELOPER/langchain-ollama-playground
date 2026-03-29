import sys

from src.integrations.ollama.chat.invocation import invocation
from src.integrations.ollama.chat.multimodal import multimodal
from src.integrations.ollama.chat.reasoning import reasoning
from src.integrations.ollama.chat.tool_calling import tool_calling


def main():
    commands = {
        "invocation": invocation,
        "tool_calling": tool_calling,
        "multimodal": multimodal,
        "reasoning": reasoning,
    }

    key = sys.argv[1] if len(sys.argv) > 1 else next(iter(commands))

    func = commands.get(
        key,
        lambda: print(f"{key!r} is not valid. Available: {', '.join(commands.keys())}"),
    )

    func()


if __name__ == "__main__":
    main()
