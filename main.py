import datetime as dt
import random

import pandas as pd
import smtplib

id = "itsmayankinbox@gmail.com"
key = "ogzdfxfvsntnoifj"

month = dt.datetime.today().date().month
day = dt.datetime.today().date().day

birthday_dict = pd.read_csv("birthdays.csv").to_dict("index")

raw_message = open(f"letter_templates/letter_" + str(random.randint(1, 3)) + ".txt").read()

for index, value in birthday_dict.items():
    if month == value["month"]:
        if day == value["day"]:
            receiver_name = value["name"]
            message = raw_message.replace("[NAME]", receiver_name)
            receiver_email = value["email"]
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=id, password=key)
                connection.sendmail(from_addr=id, to_addrs=receiver_email, msg=f"Subject:Happy"
                                                                                        f" Birthday\n\n{message}")




