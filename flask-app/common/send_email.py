import smtplib
from common.database import Database
import common.config as config

sender_email = config.EMAIL_ADDRESS
password = config.PASSWORD


def send_email(user_email):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    message = f"Greetings \n\nHello Mr/Mrs.{user_email}"

    smtp.sendmail(sender_email, user_email, message)

    smtp.quit()


def send_emails_registered(user_emails, subject):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    for email in user_emails:
        message = f"{subject} \n\nHello Mr/Mrs.{email}"
        smtp.sendmail(sender_email, email['email'], message)

    smtp.quit()
