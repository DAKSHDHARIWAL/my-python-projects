import requests

def get_weather(city):
    try:
        # API URL (free weather API)
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        # Check request success
        if response.status_code != 200:
            print("Failed to fetch data from API")
            return

        data = response.json()

        # Extract useful info
        current = data["current_condition"][0]

        temperature = current["temp_C"]
        weather_desc = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        # Display data
        print("\nWeather Information")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_desc}")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException:
        print(" Network error! Please check your internet.")
    
    except Exception as e:
        print(" Error:", e)


# User input
city_name = input("Enter city name: ")

# Function call
get_weather(city_name)