# app/app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your API key if needed
# API_URL = "https://api.open-meteo.com/v1/forecast"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('app.html')
# def index():
#     forecast = None
#     if request.method == 'POST':
#         city = request.form.get('city')
#         # Here you would have logic to get weather data
#         # For simplicity, let's assume we use the Open Meteo API
#         params = {
#             'latitude': '52.52',  # Default to Berlin; replace with actual coordinates
#             'longitude': '13.4050',
#             'hourly': 'temperature_2m'
#         }
#         response = requests.get(API_URL, params=params)
#         data = response.json()
#         forecast = data['hourly']['temperature_2m']  # Simplified example
#     return render_template('app.html', forecast=forecast)

if __name__ == "__main__":
    app.run(debug=True)
