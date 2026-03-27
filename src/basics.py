import base64
from io import BytesIO

import requests
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_core.messages import ChatMessage
from langchain_ollama import ChatOllama
from PIL import Image

from src.schemas import WttrResponse


@tool
def get_weather(city: str) -> str:
    """
    Fetch the current weather for a given city using wttr.in.

    Args:
        city (str): Name of the city (e.g., "Tashkent").

    Returns:
        A formatted string summarizing current weather conditions.
    """
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    response.raise_for_status()

    data = WttrResponse.model_validate(response.json())

    cc = data.current_condition[0]
    location = data.nearest_area[0]
    area_name = location.area_name[0].value
    country = location.country[0].value
    desc = cc.weather_desc[0].value

    report = (
        f"Weather report for {area_name}, {country}:\n"
        f"- Current Temperature: {cc.temp_c}°C (Feels like {cc.feels_like_c}°C)\n"
        f"- Conditions: {desc}\n"
        f"- Wind: {cc.wind_speed_kmph} km/h ({cc.wind_dir_16_point})\n"
        f"- Humidity: {cc.humidity}%\n\n"
        f"Forecast:\n"
    )

    for day in data.weather:
        report += f"- {day.date}: High {day.max_temp_c}°C, Low {day.min_temp_c}°C\n"

    return report


def tool_calling():
    """
    Demonstrates LangChain tool calling with a local Ollama model.

    Binds the `get_weather` tool to the LLM and sends a prompt.
    If the model decides to call a tool, the resulting tool_calls
    are printed. Uses llama3.1 which supports function/tool calling.
    """
    llm = ChatOllama(
        model="llama3.1",
        validate_model_on_init=True,
        temperature=0,
    ).bind_tools([get_weather])

    result = llm.invoke("What is the current weather in Tashkent?")

    print("result: ", result)
    print("result.content: ", result.content)
    print("result.tool_calls: ", result.tool_calls)


def multimodal():
    """
    Demonstrates multimodal (vision) input with a local Ollama model.

    Loads a local image, encodes it as a base64 data URL, and sends
    it alongside a text prompt to qwen3.5:9b, which supports vision.
    Prints the model's description of the image.
    """
    llm = ChatOllama(model="qwen3.5:9b", temperature=0)

    img = Image.open("../assets/llama.jpg")
    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    image_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    msg = HumanMessage(
        content=[
            {"type": "text", "text": "What is in this image?"},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{image_b64}"},
        ]
    )

    print(llm.invoke([msg]))


def reasoning():
    """
    Demonstrates thinking/reasoning mode using a custom message role.

    To enable thinking on supported models, pass a ChatMessage with role
    set to "control" and content set to "thinking". Since "control" is a
    non-standard message role, ChatMessage is used instead of HumanMessage
    or SystemMessage.
    """
    llm = ChatOllama(model="qwen3.5:9b")

    messages = [
        ChatMessage(role="control", content="thinking"),
        HumanMessage("What is 3^3?"),
    ]

    response = llm.invoke(messages)
    print(response.content)
