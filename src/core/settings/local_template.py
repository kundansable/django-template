# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$!*2()f0l@7tlfgfpq^j0^d#=+qz=2xn5vvdw_am2+77h_6c)='

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

ALLOWED_HOSTS = []

############# Database options #######################

# sqLite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myproject',
#         'USER': 'myprojectuser',
#         'PASSWORD': 'password',
#     }
# }
