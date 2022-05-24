from os import getenv
import dotenv
import environ


dotenv.load_dotenv(dotenv.find_dotenv())

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}
