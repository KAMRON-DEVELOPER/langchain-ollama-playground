from pydantic import field_validator
from datetime import datetime, date, time

from pydantic import BaseModel, Field


# WttrResponse
class WttrResponse(BaseModel):
    current_condition: list[CurrentConditionSchema]
    nearest_area: list[NearestAreaSchema]
    request: list[RequestSchema]
    weather: list[WeatherSchema]


## CurrentConditionSchema
class WeatherDescSchema(BaseModel):
    value: str


class WeatherIconUrlSchema(BaseModel):
    value: str


class CurrentConditionSchema(BaseModel):
    feels_like_c: int = Field(alias="FeelsLikeC")
    feels_like_f: int = Field(alias="FeelsLikeF")
    cloud_cover: int = Field(alias="cloudcover")
    humidity: int
    local_obs_date_time: datetime = Field(alias="localObsDateTime")
    observation_time: time
    precip_inches: float = Field(alias="precipInches")
    precip_mm: float = Field(alias="precipMM")
    pressure: int
    pressure_inches: int = Field(alias="pressureInches")
    temp_c: int = Field(alias="temp_C")
    temp_f: int = Field(alias="temp_F")
    uv_index: int = Field(alias="uvIndex")
    visibility: int
    visibility_miles: int = Field(alias="visibilityMiles")
    weather_code: int = Field(alias="weatherCode")
    weather_desc: list[WeatherDescSchema] = Field(alias="weatherDesc")
    weather_icon_url: list[WeatherIconUrlSchema] = Field(alias="weatherIconUrl")
    wind_dir_16_point: str = Field(alias="winddir16Point")
    wind_dir_degree: int = Field(alias="winddirDegree")
    wind_speed_kmph: int = Field(alias="windspeedKmph")
    wind_speed_miles: int = Field(alias="windspeedMiles")

    @field_validator("observation_time", mode="before")
    @classmethod
    def parse_time(cls, v):
        if isinstance(v, str):
            # Converts "12:10 PM" to a Python time object
            return datetime.strptime(v, "%I:%M %p").time()
        return v

    @field_validator("local_obs_date_time", mode="before")
    @classmethod
    def parse_datetime(cls, v):
        if isinstance(v, str):
            # Handles the specific format "2026-03-27 12:05 PM"
            return datetime.strptime(v, "%Y-%m-%d %I:%M %p")
        return v


## NearestAreaSchema
class AreaNameSchema(BaseModel):
    value: str


class CountrySchema(BaseModel):
    value: str


class RegionSchema(BaseModel):
    value: str


class WeatherUrlSchema(BaseModel):
    value: str


class NearestAreaSchema(BaseModel):
    area_name: list[AreaNameSchema] = Field(alias="areaName")
    country: list[CountrySchema]
    latitude: float
    longitude: float
    population: int
    region: list[RegionSchema]
    weather_url: list[WeatherUrlSchema] = Field(alias="weatherUrl")


## RequestSchema
class RequestSchema(BaseModel):
    query: str
    type: str


## WeatherSchema
class AstronomySchema(BaseModel):
    moon_illumination: int
    moon_phase: str
    moonrise: time
    moonset: time
    sunrise: time
    sunset: time

    @field_validator("moonrise", "moonset", "sunrise", "sunset", mode="before")
    @classmethod
    def parse_time(cls, v):
        if isinstance(v, str):
            # Converts "12:10 PM" to a Python time object
            return datetime.strptime(v, "%I:%M %p").time()
        return v


### HourlySchema
class HourlySchema(BaseModel):
    dew_point_c: int = Field(alias="DewPointC")
    dew_point_f: int = Field(alias="DewPointF")
    feels_like_c: int = Field(alias="FeelsLikeC")
    feels_like_f: int = Field(alias="FeelsLikeF")
    heat_index_c: int = Field(alias="HeatIndexC")
    heat_index_f: int = Field(alias="HeatIndexF")
    wind_chill_c: int = Field(alias="WindChillC")
    wind_chill_f: int = Field(alias="WindChillF")
    wind_gust_kmph: int = Field(alias="WindGustKmph")
    wind_gust_miles: int = Field(alias="WindGustMiles")
    chance_of_fog: int = Field(alias="chanceoffog")
    chance_of_frost: int = Field(alias="chanceoffrost")
    chance_of_high_temp: int = Field(alias="chanceofhightemp")
    chance_of_overcast: int = Field(alias="chanceofovercast")
    chance_of_rain: int = Field(alias="chanceofrain")
    chance_of_remdry: int = Field(alias="chanceofremdry")
    chance_of_snow: int = Field(alias="chanceofsnow")
    chance_of_sunshine: int = Field(alias="chanceofsunshine")
    chance_of_thunder: int = Field(alias="chanceofthunder")
    chance_of_windy: int = Field(alias="chanceofwindy")
    cloud_cover: int = Field(alias="cloudcover")
    diffRad: float
    humidity: int
    precip_inches: float = Field(alias="precipInches")
    precip_mm: float = Field(alias="precipMM")
    pressure: int
    pressure_inches: int = Field(alias="pressureInches")
    shortRad: float
    tempC: int
    tempF: int
    time: int
    uv_index: int = Field(alias="uvIndex")
    visibility: int
    visibility_miles: int = Field(alias="visibilityMiles")
    weather_code: int = Field(alias="weatherCode")
    weather_desc: list[WeatherDescSchema] = Field(alias="weatherDesc")
    weather_icon_url: list[WeatherIconUrlSchema] = Field(alias="weatherIconUrl")
    wind_dir_16_point: str = Field(alias="winddir16Point")
    wind_dir_degree: int = Field(alias="winddirDegree")
    wind_speed_kmph: int = Field(alias="windspeedKmph")
    wind_speed_miles: int = Field(alias="windspeedMiles")


class WeatherSchema(BaseModel):
    astronomy: list[AstronomySchema]
    avg_temp_c: int = Field(alias="avgtempC")
    avg_temp_f: int = Field(alias="avgtempF")
    date: date
    hourly: list[HourlySchema]
    max_temp_c: int = Field(alias="maxtempC")
    max_temp_f: int = Field(alias="maxtempF")
    min_temp_c: int = Field(alias="mintempC")
    min_temp_f: int = Field(alias="mintempF")
    sun_hour: float = Field(alias="sunHour")
    total_snow_cm: float = Field(alias="totalSnow_cm")
    uv_index: int = Field(alias="uvIndex")
