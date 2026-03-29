import sys

from src.langchain.basic_agent import basic_agent
from src.langchain.memory import memory
from src.langchain.streaming import streaming


def main():
    commands = {"basic_agent": basic_agent, "memory": memory, "streaming": streaming}

    key = sys.argv[1] if len(sys.argv) > 1 else next(iter(commands))

    func = commands.get(
        key,
        lambda: print(f"{key!r} is not valid. Available: {', '.join(commands.keys())}"),
    )

    func()


if __name__ == "__main__":
    main()
