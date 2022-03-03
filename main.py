
import datetime as dt
now= dt.datetime.today()

today_day=now.day
today_month=now.month
today = (today_month, today_day)


import pandas as pd

df = pd.read_csv('birthdays.csv')
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in df.iterrows()}


import random
import smtplib

if today in birthdays_dict:
    person_bd=birthdays_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as reader:
        contents=reader.read()
        new_contents=contents.replace("[NAME]", person_bd["name"])

    my_email = "###@gmail.com" #sender's
    password = '***'  #semder's

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=person_bd["email"], msg=f"Subject:Happy Birthday! \n\n {new_contents}.")







