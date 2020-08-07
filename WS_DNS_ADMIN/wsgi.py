"""
WSGI config for WS_DNS_ADMIN project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site

python_home = '/usr/local/venvs/pizza'

site.addsitedir(python_home + '/lib/python2.7/site-packages')

sys.path.append('/var/www/pizzasl')
sys.path.append('/var/www/pizzasl/WS_DNS_ADMIN')

activate_env=os.path.expanduser(python_home + '/bin/activate_this.py')
execfile(activate_env, dict(__file__=activate_env))

#activate_this = python_home + '/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WS_DNS_ADMIN.settings")

application = get_wsgi_application()
