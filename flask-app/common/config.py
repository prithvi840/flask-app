from os import getenv

EMAIL_ADDRESS = getenv('EMAIL_ADDRESS')
PASSWORD = getenv('PASSWORD')
DB_URI = getenv('DB_URI')
SECRET_KEY = getenv('SECRET_KEY')
SMTP_HOST = getenv('SMTP_HOST')
SMTP_PORT = int(getenv('SMTP_PORT', 587))
