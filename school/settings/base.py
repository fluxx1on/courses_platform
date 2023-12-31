from datetime import timedelta
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-g_jsj_&-ih=)og06=^&0oxii0u^p-ue2yk94$dkd!4u%&hi&zb'

INSTALLED_APPS = [
    'school_api.apps.SchoolApiConfig',
    'school_app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', 
    'rest_framework_api_key',
    'channels',
    'channels_redis',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'school.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'school.asgi.application'
WSGI_APPLICATION = 'school.wsgi.application'

LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'school_app/static/')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_ALLOWED_EXTENSIONS = ['svg', 'jpg', 'jpeg', 'png', 'gif']
#STATIC_ROOT_DIR
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'school_app/media/')

CELERY_BROKER_URL = 'redis://localhost:6379/0'

CELERY_BEAT_SCHEDULE = {
    'update_lesson_access': {
        'task': 'school_app.tasks.update_lesson_access',
        'schedule': timedelta(minutes=1),  # Расписание выполнения задачи (в данном случае каждая минута)
    },
}