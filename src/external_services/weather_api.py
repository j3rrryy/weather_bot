from aiohttp import ClientSession

from src.config import load_config
from src.errors import GetWeatherError

config = load_config()


async def get_weather(today: bool, **commands: str):
    """
    Get weather info for today or for the following days.
    """

    TOKEN = config.bot.wthr_token

    params = "&".join([f"{k}={v}" for k, v in commands.items()])

    if today:
        # get weather forecast for today
        url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&{params}"
    else:
        # get weather forecast for the following days
        url = f"http://api.weatherapi.com/v1/forecast.json?key={TOKEN}&{params}"

    async with ClientSession() as session:
        async with session.get(url) as resp:
            res = await resp.json(encoding="utf-8")

    if "error" in res.keys():
        raise GetWeatherError

    return res
