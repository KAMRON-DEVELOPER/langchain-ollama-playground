import base64
from io import BytesIO
from pathlib import Path

from langchain_core.messages import HumanMessage
from PIL import Image

from src.integrations.ollama.main import create_ollama_model


def multimodal():
    r"""
    Demonstrates multimodal (vision + text) input with a local Ollama model.

    Flow:

        1. Open a local JPEG with Pillow and encode it as a base64 data URL.
        2. Build a `HumanMessage` with both a text prompt and the image URL.
        3. Invoke the model and print its description of the image.
    """

    llm = create_ollama_model(model="qwen3.5:4b")

    fp = Path(__file__).parent.parent.parent / "assets" / "llama.jpg"
    img = Image.open(fp)
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    image_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    msg = [
        HumanMessage(
            content=[
                {"type": "text", "text": "What is in this image?"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{image_b64}",
                },
            ]
        )
    ]

    print(llm.invoke(msg))
