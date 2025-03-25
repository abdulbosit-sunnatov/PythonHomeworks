import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.openweathermap.org/data/2.5/weather"

GEO_URL = "http://api.openweathermap.org/geo/1.0/direct"

if not API_KEY:
    raise ValueError("API_KEY is missing in the .env file.")
            
def get_coordinates(city):
    """Fetch latitude and longitude for a given city."""
    params = {"q": city, "appid": API_KEY, "limit": 1}

    try:
        response = requests.get(GEO_URL, params=params, timeout=10)  
        response.raise_for_status()
        data = response.json()

        if not data:
            print(f"❌ No data found for '{city}'")
            return None, None

        return data[0]["lat"], data[0]["lon"]

    except requests.exceptions.Timeout:
        print("❌ Request timed out. Please check your connection.")
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")

    return None, None

def get_weather(city):
    """Fetch weather data using city coordinates."""
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return {"error": f"Could not find coordinates for {city}."}

    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"  # Get temperature in Celsius
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "❌ Request timed out. Please check your internet connection."}
    except requests.exceptions.RequestException as e:
        return {"error": f"❌ API Error: {e}"}


def main():
    city = input("🌍 Enter city name: ").strip()
    if not city:
        print("❌ City name cannot be empty.")
        return

    weather_data = get_weather(city)

    if "error" in weather_data:
        print(weather_data["error"])
    else:
     print("\n" + "=" * 32)
     print(" 🌦️  WEATHER REPORT ")
     print("=" * 32)
     print(f" 📍 City       : {city.title()}")
    print(f" 🌡️  Temperature: {weather_data['main']['temp']}°C")
    print(f" 🌤️  Condition  : {weather_data['weather'][0]['description'].capitalize()}")
    print(f" 💧 Humidity   : {weather_data['main']['humidity']}%")
    print(f" 🌬️  Wind Speed : {weather_data['wind']['speed']} m/s")
    print("=" * 32 + "\n")



if __name__ == "__main__":
    main()
