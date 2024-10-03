from .base import *

DEBUG = False

ALLOWED_HOST = ['127.0.0.1', 'localhost', 'dominio-produccion.com']

DATABASES ={ 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        #POSTGRESQL
        #'ENGINE': 'django.db.backends.POSTGRESQL',

        #'NAME': os.getenv('db_NAME')
        #'USER': os.getenv('db_USER')
        #'PASSWORD': os.getenv('db_PASSWORD')
        #'HOST': os.getenv('db_HOST')
        #'PORT': os.getenv('db_PORT')
    }
}
os.environ['DJANGO_PORT'] = '8080'

