import requests
from bs4 import BeautifulSoup


# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.

headers = {
    "User-Agent": "Chrome/91.0.4472.124",
    "Accept-Language": "en-IN",
    "Accept-Charset": "utf-8",
}

site = (
    "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/"
    "ref=sr_1_4?dchild=1&keywords=instant+pot&qid=1625911687&sr=8-4"
)

response = requests.get(url=site, headers=headers).text

soup = BeautifulSoup(response, "html.parser")
soup.encode("utf-8")
# <span id="price_inside_buybox" class="a-size-medium a-color-price"> $89.00 </span>
price = soup.find_all("span", class_="a-offscreen")
price_as_float = float((price[0].getText()).split("$")[1])
print(price_as_float)
# print((price[0].getText()).split(".")[0])
# print(float(price.split("$")[1]))

import smtplib

my_email = "dummy@gmail.com"
password = "dummypass"

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{site}".encode("utf-8"),
        )
