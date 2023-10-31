import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()


class Email:
    def __init__(self, name, email, phone_number, message):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.message = message

    def send_email(self):
        my_email = os.environ.get('SENDER_EMAIL')
        password = os.environ.get('PASSWORD')
        receiver_email = 'alisadaintanvir@gmail.com'
        try:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(my_email, password)
                email_msg = EmailMessage()
                email_msg.set_content(f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone_number}\nMessage: "
                                      f"{self.message}")
                email_msg['subject'] = "Restful Blog's contact form"
                email_msg['from'] = my_email
                email_msg['to'] = receiver_email
                connection.send_message(email_msg)
        except smtplib.SMTPException as e:
            print(f"An error occurred while sending the email: {e}")