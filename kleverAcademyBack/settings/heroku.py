from os import getenv

DEBUG = getenv('DEBUG', False)

SECRET_KEY = getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('USER'),
        'USER': getenv('USER'),
        'PASSWORD': getenv('PASSWORD'),
        'HOST': getenv('KLEVER_ACADEMY_RDS'),
        'PORT': getenv('PORT'),
    }
}
