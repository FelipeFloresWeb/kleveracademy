from dotenv import load_dotenv

from kleverAcademyBack.settings.base import *


load_dotenv()

KLEVER_ACADEMY_ENDPOINT = getenv('KLEVER_ACADEMY_ENDPOINT')
KLEVER_ACADEMY_PORT = getenv('KLEVER_ACADEMY_PORT')
PASSWORD = getenv('PASSWORD')
DEBUG = getenv('DEBUG', False)
ALLOWED_HOSTS = getenv('ALLOWED_HOSTS')

DEBUG = DEBUG

SECRET_KEY = PASSWORD

ALLOWED_HOSTS = ALLOWED_HOSTS

DATABASES = {
    "default": KLEVER_ACADEMY_ENDPOINT(),
}
