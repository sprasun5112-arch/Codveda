# Weather API Integration using Python

A simple Python program that interacts with the **Open-Meteo API** to fetch and display current weather information for a city entered by the user.

This project does **not require an API key** and does not use OpenWeatherMap.

## Features

- Get weather information for any city
- Uses an external weather API
- No API key required
- Displays:
  - City name
  - Temperature
  - Humidity
  - Wind speed
  - Weather code
- Simple command-line interface
- Built using Python

## Technologies Used

- **Python**
- **Requests Library**
- **Open-Meteo API**

## Requirements

Make sure Python is installed on your computer.

Install the required `requests` library:

```bash
pip install requests
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/weather-api-python.git
```

2. Open the project folder:

```bash
cd weather-api-python
```

3. Install the required library:

```bash
pip install requests
```

4. Run the Python program:

```bash
python api.py
```

5. Enter a city name when prompted:

```text
Enter city name: Alappuzha
```

## Example Output

```text
--- Weather Information ---
City: Alappuzha
Temperature: 28.4 °C
Humidity: 76 %
Wind Speed: 12.5 km/h
Weather Code: 2
```

## How It Works

The program works in two steps:

### 1. Geocoding

The program sends the city name to the Open-Meteo Geocoding API.

The API returns the:

- Latitude
- Longitude
- City name

### 2. Weather Data

The latitude and longitude are then sent to the Open-Meteo Weather API.

The program receives the current weather data and displays it in the terminal.

## Project Structure

```text
Weather-API-Integration/
│
├── api.py
└── README.md
```

## API Used

This project uses **Open-Meteo**, a free weather API that does not require an API key.

- Geocoding API: `https://geocoding-api.open-meteo.com`
- Weather API: `https://api.open-meteo.com`

## Error Handling

The program handles common errors such as:

- City not found
- Unable to connect to the API
- API request failure

## Future Improvements

- Display weather descriptions instead of weather codes
- Add a 7-day weather forecast
- Add sunrise and sunset times
- Create a graphical user interface (GUI)
- Add temperature unit selection
- Improve error messages

## Author

**Your Name**

## License

This project is created for educational and learning purposes.