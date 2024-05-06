import random
import smtplib
import datetime

# Note: this is old code and created in rush for functionality implementattion
# and fun only, hence you see all code is in one file and didn't use env vars or db.
# Will be modifying all of this in free time.


my_email = "dummy@gmail.com"
password = "dummy"
quotes = None

with open("quotes.txt") as file:
    quotes = file.readlines()

now = datetime.datetime.now()
day = now.weekday()

if day in [1, 2, 4, 6]:
    msg_data = random.choice(quotes)
    # connection to mail server #smtp.mail.yahoo.com
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()  # provide security by encrypting the mail
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="gauravchand1998@yahoo.com",
        msg=f"Subject: {msg_data.split('-')[1].strip()} \n\n{msg_data.split('-')[0].strip()}",
    )
    connection.close()
