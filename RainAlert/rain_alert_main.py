import requests
from twilio.rest import Client

# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.


API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "add_key"

account_sid = "dummy"
auth_token = "dummy"
from_phone = "+dummy"
to_phone = "+dummy"

weather_params = {
    "lat": 26.500490,
    "lon": 80.271233,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(API_ENDPOINT, params=weather_params)
# response.status_code
weather_data = response.json()
# print(weather_data)
hourly_list = weather_data["hourly"][:12]
umbrela = False
for hour in hourly_list:
    if hour["weather"][0]["id"] < 700:
        # print(f"{hour['weather'][0]['main']}")
        umbrela = True

if umbrela == True:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hey you, It's going to rain today, Don't forget to bring an Umbrella. ☔",
        from_=from_phone,
        to=to_phone,
    )
    print(message.status)
