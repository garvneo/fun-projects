import datetime
import smtplib
import pandas
import random

# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.


my_email = "dummy@gmail.com"
password = "dymmy"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(rows["month"], rows["day"]): rows for index, rows in data.iterrows()}

if today in birthdays_dict:
    birthday_data = birthdays_dict[today]
    file_path = f"letter/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contentss = contents.replace("[NAME]", birthday_data["name"])

    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_data["email"],
        msg=f"Subject: Happy Birthday!\n\n{contentss}",
    )
    connection.close()
