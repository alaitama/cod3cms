from settings import *


DEBUG = True
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME

# SITE_ID=1

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
EXISTS_POSTGRESQL = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
if os.environ.has_key('OPENSHIFT_APP_NAME'):
    DB_NAME = os.environ['OPENSHIFT_APP_NAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_USERNAME'):
    EXISTS_POSTGRESQL = True
    DB_USER = os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PASSWORD'):
    DB_PASSWD = os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_HOST'):
    DB_HOST = os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
if os.environ.has_key('OPENSHIFT_POSTGRESQL_DB_PORT'):
    DB_PORT = os.environ['OPENSHIFT_POSTGRESQL_DB_PORT']


if EXISTS_POSTGRESQL:
    # os.environ['OPENSHIFT_DB_*'] variables can be used with databases created
    # with rhc app cartridge add (see /README in this git repo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': DB_NAME,               # Or path to database file if using sqlite3.
            'USER': DB_USER,               # Not used with sqlite3.
            'PASSWORD': DB_PASSWD,         # Not used with sqlite3.
            'HOST': DB_HOST,               # Set to empty string for localhost. Not used with sqlite3.
            'PORT': DB_PORT,               # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'),
        }
    }


SECRET_KEY = 'your-super-secret-key'


MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')


from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())


# AWS AMAZON S3 Configurations

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
FILEBROWSER_DIRECTORY = ''  # either by default load to uploads and sotes in /media/uploads

# Say to browser cache for lont term, better perfomance
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}
