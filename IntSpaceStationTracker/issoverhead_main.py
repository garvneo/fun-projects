import requests
import smtplib
import time
from datetime import datetime

# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.

my_email = # provide_mail
password = # pass

MY_LAT = # latitude
MY_LONG = # longitude


def is_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # My position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 < iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour()

    if time_now >= sunset or time_now <= sunrise:
        return True


while (True):
    time.sleep(60)
    if is_issoverhead() and is_night():
        # connection to mail server #smtp.mail.yahoo.com
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()  # provide security by encrypting the mail
        connection.login(user=my_email, password=password)
        print("Hello")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="grv@yahoo.com",
            msg=f"Subject: Look In the Skies \n\nThe ISS ia above you now"
        )
        connection.close()
