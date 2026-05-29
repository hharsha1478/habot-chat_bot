#weather app by harsha 


import requests
def get_weather (city,api_key):
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try :
        response =requests.get(url)
        data = response.json()

        if data["cod"] ==200:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            condition =data["weather"][0]["description"].title()
            wind_speed = data["wind"]["speed"]

            print (f"\n______________________")
            print (f"weather 🌤 in {city_name}, {country}")
            print (f"_______________________")
            print (f"temperature : {temp}°C")
            print (f"feels like : {feels_like}°C")
            print (f"humidity : {humidity}%")
            print (f"condition : {condition}")
            print (f"wind speed : {wind_speed}km/h")


        else:
            print ("city not found 🤦‍♂️🤦‍♂️! please check the city name")

    except:
        print ("something went wrong 😔😔! please check your internet connection and try again")


#main program

api_key="80afc48000139f75a13d93c1c61a2598"

while True: 
    city= input ("\nenter city name (or 'quit'to exit):")
    
    if city.lower() == 'quit':
        print ("goodbye!😎")
        break

    get_weather(city, api_key)