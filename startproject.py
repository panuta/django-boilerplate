import os, sys

class CommandError(Exception):
    pass

try:
    project_name = sys.argv[1]
except IndexError:
    print >> sys.stderr, 'Error: Project name is missing. "python startproject.py [project name]"'
    sys.exit(2)

# Validate project name
import re
import shutil
if not re.search(r'^[_a-zA-Z]\w*$', project_name):
    if not re.search(r'^[_a-zA-Z]', project_name):
        message = 'make sure the name begins with a letter or underscore'
    else:
        message = 'use only numbers, letters and underscores'
    print >> sys.stderr, 'Error: %r is not a valid project name. Please %s.' % (project_name, message)
    sys.exit(2)

# Duplicate django_boilerplate content
base_path = os.path.dirname(__file__)
project_dir = os.path.join(base_path, project_name)
try:
    shutil.copytree(os.path.join(base_path, 'django_boilerplate/'), project_dir, ignore=shutil.ignore_patterns('*.pyc'))
except OSError, e:
    print >> sys.stderr, 'Error: Cannot create a project folder. %s.' % e
    sys.exit(2)

# Prompt for user input
user_input = raw_input('Activate Django Admin? [Yes/No]:')
print user_input.lower()
is_activate_django_admin = user_input.lower() in (None, '', 'y', 'yes')

# Modify settings file
settings_file = open(os.path.join(project_dir, 'settings.py'), 'r')
settings_file_content = settings_file.read()
settings_file.close()

# Settings : Project Name
settings_file_content = settings_file_content.replace('django_boilerplate', project_name)

# Settings : Secret Key
from random import choice
secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
settings_file_content = settings_file_content.replace('{{SECRET_KEY}}', secret_key)

# Settings : Django Admin
settings_file_content = settings_file_content.replace('# \'django.contrib.admin\',', '\'django.contrib.admin\',' if is_activate_django_admin else '')

settings_file = open(os.path.join(project_dir, 'settings.py'), 'w')
settings_file.write(settings_file_content)
settings_file.close()

# Modify urls file
urls_file = open(os.path.join(project_dir, 'urls.py'), 'r')
urls_file_content = urls_file.read()
urls_file.close()

# Urls : Project Name
urls_file_content = urls_file_content.replace('django_boilerplate', project_name)

# Urls : Django Admin
urls_file_content = urls_file_content.replace('# from django.contrib import admin', 'from django.contrib import admin' if is_activate_django_admin else '')
urls_file_content = urls_file_content.replace('# admin.autodiscover()', 'admin.autodiscover()' if is_activate_django_admin else '')

urls_file_content = urls_file_content.replace('# url(r\'^admin/\', include(admin.site.urls)),', 'url(r\'^admin/\', include(admin.site.urls)),' if is_activate_django_admin else '')

urls_file = open(os.path.join(project_dir, 'urls.py'), 'w')
urls_file.write(urls_file_content)
urls_file.close()

print '########## What\'sNext ##########'
print '1. Config database information in settings.py and dev_settings.py file '
print '2. Start developing in \'homepage\' app (or delete this app entirely if not need)'

"""
TODO
- Log settings
"""