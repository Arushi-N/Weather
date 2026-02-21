🌤️ Weather App (Python)

A simple Python CLI application that fetches the current temperature of any city using the WeatherAPI.

This project demonstrates:

API integration

Environment variable usage for security

Basic error handling

🚀 Features

Get real-time temperature in Celsius 🌡️

Secure API key handling using environment variables 🔐

Simple command-line interface

Basic error handling

🛠️ Tech Stack

Python 3

requests library

WeatherAPI

📂 Project Structure
weather-app/
│
├── weather.py
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/weather-app.git
cd weather-app
2️⃣ Install Dependencies
pip install requests
3️⃣ Get Your API Key

Create an account at:
https://www.weatherapi.com/

Copy your API key.

4️⃣ Set Environment Variable (Important 🔐)
🪟 Windows (PowerShell)
setx WEATHER_API_KEY "your_api_key_here"

Restart your terminal after this.

🍎 Mac/Linux
export WEATHER_API_KEY="your_api_key_here"
▶️ Run the Program
python weather.py

Example:

Enter the city name: London
The temperature in London is: 12°C
🔐 Security Best Practice

This project does NOT store the API key directly in the source code.

Instead, it uses:

os.getenv("WEATHER_API_KEY")

This prevents accidental exposure of sensitive information on GitHub.

📈 Future Improvements

Show humidity and wind speed

Add weather condition description

Add forecast feature

Convert into a web app using Flask

Add Docker support
