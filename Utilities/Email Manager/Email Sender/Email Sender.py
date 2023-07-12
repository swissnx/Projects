
import smtplib
import ssl
import configparser
from email.message import EmailMessage


class EmailSenderEngine:
    def __init__(self):
        config_file = input("Config file Path: ")
        config = configparser.ConfigParser()
        config.read(config_file)

        self.__sender_email = config['DEFAULT']['Email']
        self.__password = config['DEFAULT']['Password']
        # self.__sender_email = input("Your Email: ")
        # self.__password = input("Your password: ")
        self.__receiver_email = input("To: ")
        self.__cc = input("CC (sep. with a comma): ")
        self.__bcc = input("BCC (sep. with a comma): ")
        self.__subject = input("Subject: ")
        self.__body = input("Content/Body: ")

    def __create_message(self):
        message = EmailMessage()
        message['From'] = self.__sender_email
        message['To'] = self.__receiver_email
        if self.__cc:
            message['Cc'] = self.__cc
        if self.__bcc:
            message['Bcc'] = self.__bcc
        message['Subject'] = self.__subject
        message.set_content(self.__body)
        return message

    def _send_email(self, message):
        raise NotImplementedError('Subclasses must implement the _send_email method')

    def __run(self):
        try:
            message = self.__create_message()
            self._send_email(message)
            print('Email sent successfully')
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        self.__run()


class GmailSender(EmailSenderEngine):
    def _send_email(self, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(self._EmailSenderEngine__sender_email, self._EmailSenderEngine__password)
            server.send_message(message)


class OutlookSender(EmailSenderEngine):
    def _send_email(self, message):
        context = ssl.create_default_context()
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls(context=context)
            server.login(self._EmailSenderEngine__sender_email, self._EmailSenderEngine__password)
            server.send_message(message)


class ProtonSender(EmailSenderEngine):
    def _send_email(self, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('mail.protonmail.com', 465, context=context) as server:
            server.login(self._EmailSenderEngine__sender_email, self._EmailSenderEngine__password)
            server.send_message(message)


if __name__ == "__main__":
    gmail_sender = GmailSender()
    gmail_sender.run()

    outlook_sender = OutlookSender()
    outlook_sender.run()

    proton_sender = ProtonSender()
    proton_sender.run()
