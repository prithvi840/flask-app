import smtplib
from common import EMAIL_ADDRESS, PASSWORD, SMTP_HOST, SMTP_PORT


class SendEmail(object):
    '''Contains functions to send the email to logged-in user(s).'''
    sender_email = EMAIL_ADDRESS
    password = PASSWORD
    __smtp = None
    
    def __enter__(self):
        SendEmail.__smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

        SendEmail.__smtp.ehlo()
        SendEmail.__smtp.starttls()
        SendEmail.__smtp.ehlo()

        SendEmail.__smtp.login(SendEmail.sender_email, SendEmail.password)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        SendEmail.__smtp.quit()
        return True

    @staticmethod
    def _send_email(receiver_email: str, message: str) -> None:
        SendEmail.__smtp.sendmail(SendEmail.sender_email, receiver_email, message)

    @staticmethod
    def signup_email(user_email: str) -> None:
        '''
        Forms the signup email message template & send it to the user.
        :param user_email: Email of the user

        :return: None
        '''
        message = f"Greetings \n\nHello Mr/Mrs {user_email}"
        SendEmail._send_email(user_email, message)
    
    @staticmethod
    def send_emails(emails: list[str], subject: str) -> None:
        '''
        Forms the msg and sends email to the given list of users.
        :param emails: List of user emails
        :param subject: A common subject line to send with email.

        :return: None
        '''
        for email in emails:
            msg = f'{subject} \n\nHello Mr/Mrs {email}'
            SendEmail._send_email(email, msg)
