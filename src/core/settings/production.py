# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = False


SECRET_KEY = os.environ.get(
    "SECRET_KEY", '2()f0l@7tlfgfpq^j0^d#=+qz=2xn5vvdw_am2+77h_6c)=')

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get("DATABASE_URL"))
DATABASES = {"default": DEFAULT_CONNECTION}
ALLOWED_HOSTS = json.loads(os.environ.get("ALLOWED_HOSTS", "[\"*\"]"))
