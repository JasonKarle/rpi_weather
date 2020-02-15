#!/usr/bin/env python

"""
This is the core program enabling the local weather and date and time
to be read for a location and parsed. This is intended to provide
the base data to then be graphically displayed on a RPi 3" LCD screen,
which will (may) be executed in a separate module
"""
__author__ = "Jason Karle"
__copyright__ = "Copyright 2020, The RPi Weather Project"
__credits__ = ["nil"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Jason Karle"
__email__ = "jasonpkarle@outlook.com"
__status__ = "Development"

#test

# module imports
import requests
import datetime

# variables
    # weather API key, location and formatting
url = "http://api.openweathermap.org/data/2.5/forecast?id=6324729&APPID=a93c2213b87caa16add92c8d0470c01d&units=metric"
    # gets current DTG
now = datetime.datetime.now()

    #defines degree symbology
degree = "\u00B0"
degreeC = "\u2103"
degreeF = "\u2109"

json_data = requests.get(url).json() # grabs weather data from OpenWeatherMap.org in JSON format

    # extracts specific weather data from jason_data and sets in dedicated variable
current_temp = round(json_data['list'][0]['main']['temp'])
feels_like_temp = round(json_data['list'][0]['main']['feels_like'])
weather_desc = json_data['list'][0]['weather'][0]['description']
icon = json_data['list'][0]['weather'][0]['icon'] # place holder for graphic symbol once GUI is implemented
clouds = json_data['list'][0]['clouds']['all']
wind_speed = json_data['list'][0]['wind']['speed']
wind_kph = round(wind_speed * ((60*60)/1000))
wind_dir = json_data['list'][0]['wind']['deg']
time = now.strftime("%H:%M")
date = now.strftime(("%d %b %Y"))

    #prints the desired information to screen

print(f"The time is: {time}, {date}\n")
print(f"The current temperature is: {current_temp}{degreeC}")
print(f"But it feels like: {feels_like_temp}{degreeC}")
print(f"It is currently: {weather_desc}")
print(f"{icon} {clouds}% cloud coverage")
print(f"The wind is coming from {wind_dir}{degree} at {wind_kph} kph")
