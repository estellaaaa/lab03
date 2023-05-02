import csv
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
_ = load_dotenv()


#def send_email(to, subject, content):

email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")
subject = os.environ.get("SUBJECT")
to = os.environ.get("TO")
content = "amogus"


# create email
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = email_address
msg['To'] = to
msg.set_content(content)

# send email
#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#    smtp.login(email_address, email_password)
#    smtp.send_message(msg)

#if __name__ == '__main__':
#    to = input("Enter emails: ")
#    subject = input("Enter subject: ")
#    content = input("Enter content: ")

#    send_email(to, subject, content)

#import yagmail
#yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
#yag.send("mail", "subject", "message")

#import smtplib
#from email.message import EmailMessage

#email_address = "mail"
#email_password = "apppassword"

#msg = EmailMessage()
#msg['Subject'] = "Email subject"
#msg['From'] = email_address
#msg['To'] = "to-address@gmail.com"
#msg.set_content("This is eamil message")

#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#    smtp.login(email_address, email_password)
#    smtp.send_message(msg)

rows = []
with open("subscriber - Tabellenblatt1 (1).csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
