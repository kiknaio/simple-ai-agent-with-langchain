from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key as an environment variable or directly in this file")

def get_weather(query: str):
    # Parse latitude and longitude from query
    try:
        lat_lon = query.strip().split(',')
        latitude = float(lat_lon[0].strip())
        longitude = float(lat_lon[1].strip())
    except:
        # Default to New York if parsing fails
        latitude, longitude = 40.7128, -74.0060
        
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]
    return f"The current temperature is {temperature}°C with a wind speed of {wind_speed} m/s."


llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY)

tools = [
    Tool(
        name="Weather",
        func=get_weather,
        description="Get current weather. Input should be latitude and longitude as two numbers separated by a comma (e.g., '40.7128, -74.0060')."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
response = agent.run("What's the weather like in Tbilisi, Georgia?")
print(response)
