import os


_PATH = os.path.abspath(os.path.dirname(__file__))
_MODULE = os.path.basename(_PATH)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'example.db'

ROOT_URLCONF = _MODULE + '.urls'

MEDIA_ROOT = os.path.join(_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_DIRS = (
    os.path.join(_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'friends',
    'profiles',
)

SECRET_KEY = '7-(!m)8+avqdg!di(yc&&w%k9anf7_aj@%jcskjps&ddvkg^je'
