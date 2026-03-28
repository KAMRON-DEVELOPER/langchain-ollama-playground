# Langchain Ollama Playground

## Installation

> [!NOTE]
> For more details, refer to the [Ollama Linux documentation](https://docs.ollama.com/linux) and the [ArchWiki](https://wiki.archlinux.org/title/Ollama).
>
> *Warning: `ollama-vulkan` may experience performance issues on older hardware.*

```bash
sudo pacman -S ollama
# or
sudo pacman -S ollama-vulkan
```

start the service, so we don't need to run `ollama server` every time.

```bash
sudo systemctl enable --now ollama.service
```

### Configuring a Custom Models Directory

By default, Ollama stores models in the root directory(`/var/lib/ollama`). To change this to a custom user directory:

```bash
mkdir -p ~/ollama
sudo chown -R ollama:ollama ~/ollama
sudo mkdir -p /etc/systemd/system/ollama.service.d/
sudo nvim /etc/systemd/system/ollama.service.d/override.conf
```

Add the following environment variables to your /etc/systemd/system/ollama.service.d/override.conf file:

> [!NOTE]
> You can peek `/usr/lib/systemd/system/ollama.service`

```conf
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
Environment="OLLAMA_MODELS=/home/kamronbek/ollama"
ProtectHome=no
```

Apply the changes and restart the daemon:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama.service
```

## Models

| Name                                                              | Size                | Context         | Purpose                   |
| :---------------------------------------------------------------- | :------------------ | :-------------- | :------------------------ |
| [phi4-mini](https://ollama.com/library/phi4-mini)                 | 2.5GB               | 128K            | tools                     |
| [nemotron-3-nano](https://ollama.com/library/nemotron-3-nano)     | 2.8GB               | 256K            | tools, thinking           |
| [granite3.1-moe](https://ollama.com/library/granite3.1-moe)       | 2.0GB               | 128K            | tools                     |
| [granite4](https://ollama.com/library/granite4)                   | 2.1GB               | 128K            | tools                     |
| [qwen2.5](https://ollama.com/library/qwen2.5)                     | 1.9GB-4.7GB-9.0GB   | 32K-32K-32K     | tools                     |
| [qwen2.5-coder](https://ollama.com/library/qwen2.5-coder)         | 1.9GB-4.7GB-9.0GB   | 32K-32K-32K     | tools                     |
| [qwen3](https://ollama.com/library/qwen3)                         | 2.5GB-5.2GB-9.3GB   | 256K-40K-40K    | tools, thinking           |
| [qwen3.5](https://ollama.com/library/qwen3.5)                     | 2.7GB-3.4GB-6.6GB   | 256K-256K-256K  | vision, tools, thinking   |
| [llama3.1](https://ollama.com/library/llama3.1)                   | 4.9GB               | 128K            | tools                     |
| [llama3.2](https://ollama.com/library/llama3.2)                   | 2.0GB               | 128K            | tools                     |
| [gemma2](https://ollama.com/library/gemma2)                       | 5.4GB               | 8K              |                           |
| [gemma3](https://ollama.com/library/gemma3)                       | 3.3GB-8.1GB         | 128K-128K       | vision                    |
| [mistral](<https://ollama.com/library/mistral>)                   | 4.4GB               | 32K             | tools                     |
| [mistral-nemo](https://ollama.com/library/mistral-nemo)           | 7.1GB               | 1000K           | tools                     |
| [ministral-3](https://ollama.com/library/ministral-3)             | 6.0GB-9.1GB         | 256K-256K       | vision, tools             |
| [deepseek-r1](https://ollama.com/library/deepseek-r1)             | 4.7GB-5.2GB-9.0GB   | 128K-128K-128K  | tools, thinking           |
| [yi-coder](https://ollama.com/library/yi-coder)                   | 5.0GB               | 128K            |                           |
| [nomic-embed-text](https://ollama.com/library/nomic-embed-text)   | 274MB               | 2K              |                           |

| Name              | Description                                                                                                                                                                       |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| phi4-mini         | Phi-4-mini brings significant enhancements in multilingual support, reasoning, and mathematics, and now, the long-awaited function calling feature is finally supported.          |
| nemotron-3-nano   | Nemotron-3-Nano is a new Standard for Efficient, Open, and Intelligent Agentic Models, now updated with a 4B parameter count model.                                               |
| granite3.1-moe    | The IBM Granite 1B and 3B models are long-context mixture of experts (MoE) Granite models from IBM designed for low latency usage.                                                |
| granite4          | Granite 4 features improved instruction following (IF) and tool-calling capabilities, making them more effective in enterprise applications.                                      |
| qwen2.5           | Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset, encompassing up to 18 trillion tokens. The model supports up to 128K tokens and has multilingual support.  |
| qwen2.5-coder     | The latest series of Code-Specific Qwen models, with significant improvements in code generation, code reasoning, and code fixing.                                                |
| qwen3             | Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models.                              |
| qwen3.5           | Qwen 3.5 is a family of open-source multimodal models that delivers exceptional utility and performance.                                                                          |
| llama3.1          | Llama 3.1 is a new state-of-the-art model from Meta available in 8B, 70B and 405B parameter sizes.                                                                                |
| llama3.2          | Meta's Llama 3.2 goes small with 1B and 3B models.                                                                                                                                |
| gemma2            | Google Gemma 2 is a high-performing and efficient model available in three sizes: 2B, 9B, and 27B.                                                                                |
| gemma3            | The current, most capable model that runs on a single GPU.                                                                                                                        |
| mistral           | The 7B model released by Mistral AI, updated to version 0.3.                                                                                                                      |
| mistral-nemo      | A state-of-the-art 12B model with 128k context length, built by Mistral AI in collaboration with NVIDIA.                                                                          |
| ministral-3       | The Ministral 3 family is designed for edge deployment, capable of running on a wide range of hardware.                                                                           |
| deepseek-r1       | DeepSeek-R1 is a family of open reasoning models with performance approaching that of leading models, such as O3 and Gemini 2.5 Pro.                                              |
| yi-coder          | Yi-Coder is a series of open-source code language models that delivers state-of-the-art coding performance with fewer than 10 billion parameters.                                 |
| nomic-embed-text  | A high-performing open embedding model with a large token context window.                                                                                                         |

pull commands:

```bash
ollama pull phi4-mini:3.8b
ollama pull nemotron-3-nano:4b
ollama pull granite3.1-moe:3b
ollama pull granite4:3b

ollama pull qwen2.5:3b
ollama pull qwen2.5:7b
ollama pull qwen2.5:14b

ollama pull qwen2.5-coder:3b
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b

ollama pull qwen3:4b
ollama pull qwen3:8b
ollama pull qwen3:14b

ollama pull qwen3.5:2b
ollama pull qwen3.5:4b
ollama pull qwen3.5:9b

ollama pull llama3.1:8b
ollama pull llama3.2:3b

ollama pull gemma2:9b
ollama pull gemma3:4b
ollama pull gemma3:12b

ollama pull mistral:7b

ollama pull ministral-3:8b
ollama pull ministral-3:14b

ollama pull deepseek-r1:7b
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:14b

ollama pull yi-coder:9b
```

### Selected Models

For this project, I am utilizing a ~36.5GB stack of the following models:

- qwen3.5:4b (vision, tools, thinking)
- nemotron-3-nano:4b (tools, thinking, agentic workflow)
- phi4-mini:3.8b (reasoning, planning)
- granite3.1-moe:3b (reasoning, planning)
- qwen3.5:9b (vision, tools, thinking)
- qwen2.5-coder:14b (code generation)
- deepseek-r1:14b (advanced reasoning)
- llama3.1:8b (general tools)

## Project Setup

```bash
uv add langchain langchain-ollama python-dotenv pydantic pyrefly
```

```bash
uv add --dev basedpyright ruff black
```
