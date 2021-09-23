import smtplib
from envr import MAIN_EMAIL, MAIN_EMAIL_PASSWORD, M_EMAIL, MAY_EMAIL

class EmailManager:

    @staticmethod
    def send_email(message, time):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MAIN_EMAIL, password=MAIN_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MAIN_EMAIL,
                                to_addrs=MAY_EMAIL,
                                msg=message.encode('utf-8')
                                )
            print(f'Send to {M_EMAIL} at {time}')