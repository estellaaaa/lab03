import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = ""
email_password = ""

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = email_address
msg['To'] = "shoultfighter@gmail.com"
msg.set_content("This is email message")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
