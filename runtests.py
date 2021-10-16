#!/usr/bin/env python

import sys
from django.core.management.utils import get_random_secret_key

DEFAULT_SETTINGS = dict(
    SECRET_KEY = get_random_secret_key(),
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'django.contrib.messages',
        'ads_txt',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    },
    ROOT_URLCONF='test_utils.urls',
    SITE_ID=1,
    MIDDLEWARE=[
        'django.middleware.http.ConditionalGetMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
    ],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }]
)

def runtests():
    import django
    from django.conf import settings

    # Compatibility with Django 1.7's stricter initialization
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    if hasattr(django, 'setup'):
        django.setup()

    from django.test.runner import DiscoverRunner
    test_args = ['tests']
    failures = DiscoverRunner(
            verbosity=1, interactive=True, failfast=False
    ).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
