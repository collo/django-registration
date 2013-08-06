#!/usr/bin/env python

import os
import sys

ROOT = os.path.abspath('.')

from django.conf import settings

settings.configure(
    DEBUG=True,
    SITE_ID=1,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    ROOT_URLCONF='registration.backends.backend.urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'django.contrib.sites',
        'registration',
    ),
    TEMPLATE_DIRS=(os.path.join(ROOT, 'templates'),),
    #ACCOUNT_ACTIVATION_DAYS=7,
)

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)

if __name__ == '__main__':
    failures = test_runner.run_tests(['registration', ])
    if failures:
        sys.exit(failures)
