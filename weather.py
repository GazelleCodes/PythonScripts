# Getting weather data from a weather API

import requests
city = "London "
url = "http://api.weatherapi.com/v1/current.json?key=e8fdbeb9527a44dba4055301252712&q=" + city + "&aqi=no"

response = requests.get(url)
weather_data = response.json()

temp = weather_data.get('current').get('temp_f')
condition = weather_data.get('current').get('condition').get('text')

print("Todays weather in", city, "is", condition, "and", temp, "degrees")