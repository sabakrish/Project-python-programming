# Weather Data Analyzer

temps = []

import requests # import requests module to make HTTP requests  
print(requests.__file__) # print the location of requests module
print(requests.__version__) # print the version of requests module


url = "https://api.open-meteo.com/v1/forecast" # request info from open-meteo. It is free weather API and does not require an API key.   
#data collected from metrological agencies: NOAA (National Oceanic and Atmospheric Administration), Environment Canada, DWD(Germany), ECMWF(Europe),MeteoFrance and others. 
cities = {
    1: ("Toronto", 43.65107, -79.347015),
    2: ("Brampton", 43.7315, -79.7624),
    3: ("Scarborough", 43.7725, -79.257),
    4: ("Mississauga", 43.589, -79.6441),
    5: ("Vancouver", 49.2827, -123.1207),
    6: ("Montreal", 45.5019, -73.5674),
    7: ("Calgary", 51.0447, -114.0719),
    8: ("Ottawa", 45.4215, -75.6972),
    9: ("Edmonton", 53.5461, -113.4938),
    10: ("Winnipeg", 49.8951, -97.1384),
    11: ("Quebec City", 46.8139, -71.2080),
    12: ("Hamilton", 43.2557, -79.8711),
    13: ("Kitchener", 43.4516, -80.4925),
    14: ("Halifax", 44.6488, -63.5752),
    15: ("London", 42.9849, -81.2453),
    16: ("Victoria", 48.4284, -123.3656)
    }

print("Welcome to weekly weather report\nSelect a city:")
for num, city in cities.items():
    print(f"{num}. {city[0]}")
try:
    choice = int(input("Enter city number: "))
    if choice not in cities:
        print("Invalid selection.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

city_name, lat, lon = cities[choice]

params = { "latitude": lat, # city latitude
          "longitude": lon, # city longitude 
          "daily": "temperature_2m_max,temperature_2m_min",
          "hourly": "wind_speed_10m",
          "timezone": "America/Toronto" 
          }
 
response = requests.get(url, params=params) # make a GET request to the API with the specified parameters
data = response.json() # parse the JSON response into a Python dictionary
#print(data) # print the entire JSON data

print(f"For next 7 Days temperatures in {city_name}:")
for i in range(7):
    day= data["daily"]["time"][i] # get the date for the day
    tmax = data["daily"]["temperature_2m_max"][i] # get the max temperature for the day
    tmin = data["daily"]["temperature_2m_min"][i] # get the min temperature for the day
    wind_speed = data["hourly"]["wind_speed_10m"][i] # get the wind speed for the day    
    print(f"Day {i+1} ({day}): Max Temp: {tmax}°C, Min Temp: {tmin}°C, Wind Speed: {wind_speed} km/h") # print the temperatures for the day
   # degree Celsius power symbol: °C is typed using: Alt + 0176 on numeric keypad
    ###temps.append((tmax, tmin)) # append the max and min temperatures as a tuple to the temps list   
    #Note: we can include other parameters like humidity, precipitation, etc. by modifying the API request parameters above.    
