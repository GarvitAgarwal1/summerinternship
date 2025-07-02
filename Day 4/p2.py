from urllib import response

import requests

def weather(city, api_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}"
    try:
     respose = requests.get(url)
  #   respose.raise_for_status()   Raise an error for bad responses (4xx or 5xx)
     data = respose.json()
     temp = data["main"]["temp"]
     humidity = data["main"]["humidity"]
     feels_like = data["main"]["feels_like"]


     print(f"Weather in {city}:")
     print(f"Temperature: {temp} kelvin (feels like {feels_like} kelvin)")
     print(f"Humidity: {humidity}%")
     print(f"Description: {data["weather"][0]["description"].capitalize()}")
     print(f"Wind speed:", data["wind"]["speed"], "m/s")
     print(f"Sunrise: ", data["sys"]["sunrise"], "UTC")
     print(f"Sunset: ", data["sys"]["sunset"], "UTC")
     print(f"Country: ", data["sys"]["country"])

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    city = input("Enter city name: ")
    api_id = input("Enter your API key: ")
    weather(city, api_id)