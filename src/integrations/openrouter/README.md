# Langchain and OpenRouter integration

> [!NOTE]
> For more details, refer to the [OpenRouter integrations](https://docs.langchain.com/oss/python/integrations/providers/openrouter)

[OpenRouter](https://openrouter.ai/)
[Free Models](https://openrouter.ai/models?max_price=0&order=most-popular)

> [!WARNING]
> `openrouter` latest version may be installed automatically, causing a version mismatch with `langchain-openrouter`.

```bash
uv add "langchain-openrouter==0.2.0" "openrouter==0.7.11"
```

```bash
uv run -m src.integrations.openrouter.main
```
