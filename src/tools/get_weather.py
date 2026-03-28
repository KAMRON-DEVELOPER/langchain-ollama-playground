import json

import requests

from langchain.tools import tool
from src.schemas.get_weather import WttrResponse


@tool
def get_weather(city: str) -> dict:
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
    country = location.country[0].value
    area_name = location.area_name[0].value
    desc = cc.weather_desc[0].value

    report = {
        "city": area_name,
        "country": country,
        "temperature_c": cc.temp_c,
        "feels_like_c": cc.feels_like_c,
        "conditions": desc,
        "humidity": cc.humidity,
        "wind": f"{cc.wind_speed_kmph} km/h ({cc.wind_dir_16_point})",
        "forecast": [
            f"{day.date}: High {day.max_temp_c}°C, Low {day.min_temp_c}°C"
            for day in data.weather
        ],
    }

    print("report: ", json.dumps(report, indent=4))

    return report
