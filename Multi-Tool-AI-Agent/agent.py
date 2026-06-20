from dotenv import load_dotenv
import os
import requests
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner, function_tool

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
fixer_api_key = os.getenv("FIXER_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")
if not fixer_api_key:
    raise ValueError("FIXER_API_KEY is not set in .env")
if not weather_api_key:
    raise ValueError("WEATHER_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def currency_converter(amount: float, from_currency: str, to_currency: str):
    url = f"https://v6.exchangerate-api.com/v6/{fixer_api_key}/pair/{from_currency.upper()}/{to_currency.upper()}/{amount}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        return round(data["conversion_result"], 2)
    else:
        return f"Error from ExchangeRate API: {data.get('error-type', 'Unknown error')}"


@function_tool
def get_weather(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() 
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"The current weather in {city} is {temp}°C with {condition}."
    else:
        return f"Could not fetch weather data for {city}. Please try again later."

agent = Agent(
    name="Agent 007",
    instructions="You can help the user by either converting currencies or providing the current weather for any city they request.",
    tools=[currency_converter, get_weather]
)

result = Runner.run_sync(
    agent,
    "Convert 1200 USD into Euro",
    run_config=config
)

print(result.final_output)