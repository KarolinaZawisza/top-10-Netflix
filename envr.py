import os
from dotenv import load_dotenv
load_dotenv('C:/Users/zawis/Documents/EV/.env')

MAIN_EMAIL = os.getenv('main_email')
MAIN_EMAIL_PASSWORD = os.getenv('main_email_password')
M_EMAIL = os.getenv('m_email')
MAY_EMAIL = os.getenv('may_email')