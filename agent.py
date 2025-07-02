
from google.adk.agents import Agent


import requests

API_KEY = "f00be0f6259737c4bf728349353dfea4"  # <-- Replace this with your actual API key



def get_weather(city: str) -> str:
    """
    Get current weather for a city using Weatherstack API.
    """
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"API error: {response.status_code}"
    
    data = response.json()
    
    if "error" in data:
        return f"Error fetching weather for {city}: {data['error']['info']}"
    
    location = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temperature"]
    description = ", ".join(data["current"]["weather_descriptions"])
    feels_like = data["current"]["feelslike"]
    humidity = data["current"]["humidity"]
    
    return (f"The current weather in {location}, {country} is {description}. "
            f"Temperature: {temperature}°C (feels like {feels_like}°C), "
            f"Humidity: {humidity}%.")


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather],
)
