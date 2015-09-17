
######################
# OPENSHIFT CONFIG #
####################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'sqlite3.db'),
    }
}


SECRET_KEY = 'your-super-secret-key'


MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'media')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../../data/media/')
