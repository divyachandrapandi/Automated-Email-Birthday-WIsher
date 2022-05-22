import datetime as dt
from random import *
import smtplib
import pandas

MY_EMAIL = "gmail.com"
MY_PASSWORD = "appp password"

# TODO - Random letter format
letters = ['letter_1', 'letter_2', 'letter_3']  # string to append in file to open
random_letter = choice(letters)

# TODO - TO get today year, month, day as tuple( y,d,m)
today = dt.datetime.now()
today_year = today.year
today_month = today.month
today_day = today.day
today_f = (today.year, today.day, today.month)

# TODO open birthday.csv and get details for birthday , email, name

df = pandas.read_csv("birthdays.csv")
data_dict = df.to_dict(orient='records')
# Another way Dictionary comprehension
# dict = {(data_row['year'], data_row['day']):data_row for (index, data_row) in df.iterrows()}
# print(dict)

# TODO - to range of entries in birthday.csv, we extract name, mail, y,m,d.
#  To append date of birth from csv and add to dob list as tuple (y,d,m).
#  if today is birthday of a person from csv, then send mail to them as follows.
#  open the random letter text, replace the name of birthday person, and get the body of the letter.
#  using smtplib connection provided and send the mail to respective persons


for i in range(0, len(data_dict)):
    details = data_dict[i]
    dob_name = details['name']
    dob_mail = details['email']
    dob_year = details['year']
    dob_month = details['month']
    dob_day = details["day"]
    dob = (dob_year, dob_day, dob_month)

    if today_f == dob:
        with open(f"./letter_templates/{random_letter}.txt") as file:
            content_head = file.readline()
            formatted_head = content_head.replace('[NAME]', f"{dob_name}")
            content_body = file.read()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=dob_mail,
                                msg=f"Subject:Happy Birthday to you!!!\n\n"
                                    f"{formatted_head}\n"
                                    f"{content_body}")
