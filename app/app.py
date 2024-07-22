""" This is the entry point of the Flask application."""
from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='../templates')

geolocator = Nominatim(user_agent="weather_app_1-0")
city_visit_counts = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    city = request.args.get('city')
    if city:
        try:
            location = geolocator.geocode(city)
            if not location:
                return "City not found", 404

            latitude = location.latitude
            longitude = location.longitude

            weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            if 'current_weather' not in weather_data:
                return "Weather data not available", 500

            current_weather = weather_data['current_weather']

            if city in city_visit_counts:
                city_visit_counts[city] += 1
            else:
                city_visit_counts[city] = 1

            visit_count = city_visit_counts[city]

            return render_template('weather.html', city=city, weather={
                'temperature': current_weather['temperature'],
                'windspeed': current_weather['windspeed'],
                'visit_count': visit_count
            })
        except Exception as e:
            return str(e), 500

    return "City not provided", 400


@app.route('/visits')
def visit_counts():
    return render_template('visit_counts.html', visit_counts=city_visit_counts)
