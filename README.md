# GET WEATHER FOR DIFFERENT CITIES
## PROJCT OVERVIEW
This project is a Flask-based weather application that retrieves and displays weather information for a user-specified city.  
I used the Geopy library for geocoding and the Open-Meteo API for weather data.

## Setup Instructions
1. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Application Structure
- **`app.py`**: Main application logic.
- **`templates/index.html`**: User input form.
- **`templates/weather.html`**: Weather results display.
- **`run.py`**:Runs the application

## Code Explanation
- **Flask Routes**:
  - `/`: Renders the input form.
  - `/weather`: Processes the city input and displays weather information.
  - `/visits`:Shows the cities visited

- **Geocoding**:
  - I used Geopy to convert city names to coordinates.

- **Weather Data**:
  - Fetches weather data from the Open-Meteo API.

## User Interface
- **Form**: User inputs a city and submit to receive weather details.
- **Visited Cities**: This checks for previously visited cities and number of times visited.

## Running the app
```bash
  python3 run.py
```
## Code Quality Check
I ensured the code adheres to PEP 8 style guidelines by running:
```bash
pycodestyle app.py
```
# REMARKS
This project was a great learning experience  and I enjoyed integrating geolocation and weather data with Flask.  
It enhanced my skills and provided valuable hands-on experience.