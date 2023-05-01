#import os
#import smtplib
#from email.message import EmailMessage
#from dotenv import load_dotenv
#_ = load_dotenv()


def send_spam_email(to, subject, message):

    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_PASSWORD")

    # create email
    msg = EmailMessage()
    msg['spam of the month lol'] = subject
    msg['spamnewsletterlol@gmail.com'] = email_address
    msg['violetta.98@gmail.com'] = to
    msg.set_content(message)

    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
