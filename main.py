import sys

from src.basics import multimodal, reasoning, tool_calling


def main():
    commands = {
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
