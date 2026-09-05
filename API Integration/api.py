import requests

# Get city name
city = input("Enter city name: ")

# Step 1: Find the city's latitude and longitude
geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

geo_response = requests.get(geo_url, params=geo_params)

if geo_response.status_code == 200:
    geo_data = geo_response.json()

    if "results" in geo_data:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        city_name = geo_data["results"][0]["name"]

        # Step 2: Get weather information
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
        }

        weather_response = requests.get(weather_url, params=weather_params)

        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            current = weather_data["current"]

            print("\n--- Weather Information ---")
            print("City:", city_name)
            print("Temperature:", current["temperature_2m"], "°C")
            print("Humidity:", current["relative_humidity_2m"], "%")
            print("Wind Speed:", current["wind_speed_10m"], "km/h")
            print("Weather Code:", current["weather_code"])

        else:
            print("Unable to fetch weather data.")

    else:
        print("City not found.")

else:
    print("Unable to find city.")