import os

import django_cache_url

LOCATION = 'django.core.cache.backends.memcached.PyLibMCCache'


def test_setting_default_var():
    config = django_cache_url.config(default='memcached://127.0.0.1:11211')
    assert config['BACKEND'] == LOCATION
    assert config['LOCATION'] == '127.0.0.1:11211'


def test_setting_env_var_name():
    os.environ['HERP'] = 'memcached://127.0.0.1:11211'
    config = django_cache_url.config(env='HERP')
    assert config['BACKEND'] == LOCATION
    assert config['LOCATION'] == '127.0.0.1:11211'
