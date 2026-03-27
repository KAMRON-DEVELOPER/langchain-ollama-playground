# Langchain Ollama

## Installation

> [!NOTE]
> [Linux](https://docs.ollama.com/linux)
>
> [ArchWiki](https://wiki.archlinux.org/title/Ollama)

```bash
sudo pacman -S ollama-vulkan
sudo systemctl enable --now ollama.service
```

### Change models directory

```bash
mkdir -p ~/ollama
sudo chown -R ollama:ollama ~/ollama
sudo mkdir -p /etc/systemd/system/ollama.service.d/
sudo nvim /etc/systemd/system/ollama.service.d/override.conf
```

Add this to `/etc/systemd/system/ollama.service.d/override.conf` file

> [!NOTE]
> You can peek `/usr/lib/systemd/system/ollama.service`

```conf
[Service]
Environment="OLLAMA_MODELS=/home/kamronbek/ollama"
ProtectHome=no
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama.service
```

## Models

| Name                                                              | Size                | Context | Purpose                   |
| :---------------------------------------------------------------- | :------------------ | :------ | :------------------------ |
| [qwen2.5](https://ollama.com/library/qwen2.5)                     | 4.7GB-9.0GB         | 32K     | tools                     |
| [qwen2.5-coder](https://ollama.com/library/qwen2.5-coder)         | 4.7GB-9.0GB         | 32K     | tools                     |
| [qwen3](https://ollama.com/library/qwen3)                         | 5.2GB-9.3GB         | 40K     | tools, thinking           |
| [qwen3.5](https://ollama.com/library/qwen3.5)                     | 6.6GB               | 256K    | vision, tools, thinking   |
| [llama3.1](https://ollama.com/library/llama3.1)                   | 4.9GB               | 128K    | tools                     |
| [gemma2](https://ollama.com/library/gemma2)                       | 5.4GB               | 8K      |                           |
| [gemma3](https://ollama.com/library/gemma3)                       | 8.1GB               | 128K    | vision                    |
| [mistral](<https://ollama.com/library/mistral>)                   | 4.4GB               | 32K     | tools                     |
| [mistral-nemo](https://ollama.com/library/mistral-nemo)           | 7.1GB               | 1000K   | tools                     |
| [ministral-3](https://ollama.com/library/ministral-3)             | 6.0GB-9.1GB         | 256K    | vision, tools             |
| [deepseek-r1](https://ollama.com/library/deepseek-r1)             | 4.7GB-5.2GB-9.0GB   | 128K    | tools, thinking           |
| [yi-coder](https://ollama.com/library/yi-coder)                   | 5.0GB               | 128K    |                           |
| [nomic-embed-text](https://ollama.com/library/nomic-embed-text)   | 274MB               | 2K      |                           |

| Name              | Description                                                                                                                                                                       |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| qwen2.5           | Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset, encompassing up to 18 trillion tokens. The model supports up to 128K tokens and has multilingual support.  |
| qwen2.5-coder     | The latest series of Code-Specific Qwen models, with significant improvements in code generation, code reasoning, and code fixing.                                                |
| qwen3             | Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models.                              |
| qwen3.5           | Qwen 3.5 is a family of open-source multimodal models that delivers exceptional utility and performance.                                                                          |
| llama3.1          | Llama 3.1 is a new state-of-the-art model from Meta available in 8B, 70B and 405B parameter sizes.                                                                                |
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
ollama pull qwen2.5:7b
ollama pull qwen2.5:14b

ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b

ollama pull qwen3:8b
ollama pull qwen3:14b

ollama pull qwen3.5:9b

ollama pull llama3.1:8b

ollama pull gemma2:9b
ollama pull gemma3:12b

ollama pull mistral:7b

ollama pull ministral-3:8b
ollama pull ministral-3:14b

ollama pull deepseek-r1:7b
ollama pull deepseek-r1:8b
ollama pull deepseek-r1:14b

ollama pull yi-coder:9b
```

I choose `qwen3.5:9b`,`qwen2.5-coder:14b`, `deepseek-r1:14b`, `llama3.1:8b`. Size ~29,5GB.

## Project Setup

```bash
uv add python-dotenv langchain-ollama
```
