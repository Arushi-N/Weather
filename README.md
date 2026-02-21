# 🌤️ Weather App CLI

A simple Python-based Command Line Weather Application that fetches real-time temperature data using WeatherAPI.

This project securely retrieves weather data using environment variables for API key protection.

Created by Arushi 💙

---

## 🚀 Features

- 🌡️ Get real-time temperature of any city
- 🔐 Secure API key handling (environment variables)
- ⚡ Fast and lightweight
- 💻 Runs directly in terminal
- ❌ Handles invalid city input gracefully

---

## 🛠️ Tech Stack

- Python  
- requests library  
- WeatherAPI  
 
 ---
 

## 📁 Project Structure

```
weather-app/
│── weather.py
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/weather-app.git
```

### 2️⃣ Navigate to the project folder

```bash
cd weather-app
```

### 3️⃣ Install dependencies

```bash
pip install requests
```

### 4️⃣ Get Your API Key

1. Create an account at: https://www.weatherapi.com/
2. Generate your API key from the dashboard.

---

### 5️⃣ Set your API key (Important 🔐)

#### Windows (PowerShell)

```bash
setx WEATHER_API_KEY "your_api_key_here"
```

Restart your terminal after running this command.

#### Mac/Linux

```bash
export WEATHER_API_KEY="your_api_key_here"
```

---

### 6️⃣ Run the program

```bash
python weather.py
```

---

## 💻 Example Usage

When you run the program:

```bash
Enter the city name: London
```

The program will display:

```
The temperature in London is: 12°C
```

If the city is invalid:

```
Error fetching weather data. Please check the city name.
```

---

## 🔐 Security Note

This project does **NOT** store the API key directly in the source code.

It uses:

```python
os.getenv("WEATHER_API_KEY")
```

This prevents accidental exposure of sensitive information on GitHub.

---


## 🎯 Future Improvements

- Show humidity and wind speed  
- Add weather condition description  
- Add 3–5 day forecast  
- Build GUI version (Tkinter)  
- Deploy as web app (Flask)  
- Dockerize the project  

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Contribution

Feel free to fork this project and improve it.  
Pull requests are welcome!

